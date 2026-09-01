#!/usr/bin/env python3
"""Build the GPlates code knowledge graph and its communities (Graphify + Leiden).

    python scripts/build_graph.py                 # build (or rebuild) the graph
    python scripts/build_graph.py --check         # verify an existing graph
    python scripts/build_graph.py --no-cluster    # extract only, skip clustering
    python scripts/build_graph.py --label         # also name communities with an LLM

This is *additional* to the main SQLite index — it does not replace it. The graph
answers structural questions the entity index cannot: which cluster of code a
symbol belongs to, what a change reaches, and how two symbols connect.

Two GPlates-specific wrinkles are handled here:

* Graphify parses C++ with plain tree-sitter, which Qt's macros defeat. Running it
  directly on the GPlates tree leaves 224 files with syntax errors, several with
  no symbols at all. So the source is first mirrored through the same
  length-preserving preparation the main index uses (`cpp_parse.prepare`), which
  drops that to 44 and recovers whole Qt dialog headers. Because the transform
  preserves byte offsets and line counts, every line number in the graph still
  refers to the real file.
* Graphify writes `graphify-out/` beside the tree it graphs. GPlates source is
  read-only as far as this skill is concerned, so the mirror lives under `data/`
  and `GRAPHIFY_OUT` redirects the output there too.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sqlite3
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from gplates_index import cpp_parse  # noqa: E402
from gplates_index.common import (  # noqa: E402
    DATA_DIR, DB_PATH, SKILL_DIR, SkillError, check_source_root, open_db, read_config,
)

VENV_DIR = SKILL_DIR / ".venv"
GRAPHIFY_EXE = VENV_DIR / ("Scripts/graphify.exe" if os.name == "nt" else "bin/graphify")
MIRROR_DIR = DATA_DIR / "graph-src"
GRAPH_OUT = DATA_DIR / "graphify-out"
GRAPH_JSON = GRAPH_OUT / "graph.json"
GRAPH_DB = DATA_DIR / "graph.db"

# Extensions Graphify parses. C/C++ get the length-preserving preparation; the
# rest are copied verbatim so the graph keeps its non-code nodes too.
CPP_EXT = {".cc", ".cpp", ".cxx", ".c", ".h", ".hh", ".hpp", ".hxx"}
COPY_EXT = {".py", ".md", ".txt", ".json", ".sh", ".sql", ".cmake"}
MIRROR_EXT = CPP_EXT | COPY_EXT
SKIP_DIRS = {".git", ".svn", ".idea", ".vs", "build", "__pycache__", ".venv"}

MIN_NODES = 30000
MIN_EDGES = 60000
MIN_COMMUNITIES = 200

GRAPH_SCHEMA = """
PRAGMA journal_mode = OFF;
PRAGMA synchronous = OFF;

CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT);

CREATE TABLE communities (
    id        INTEGER PRIMARY KEY,
    name      TEXT,          -- 'Community N' unless labelled with --label
    size      INTEGER NOT NULL,  -- all member nodes, stubs included
    located   INTEGER,       -- members that carry a source path and line
    real_defs INTEGER,       -- members sitting on a real definition in the entity index
    top_dirs  TEXT,          -- dominant source directories, most common first
    top_nodes TEXT           -- a few representative member labels
);
CREATE INDEX idx_comm_size ON communities(size);
CREATE INDEX idx_comm_defs ON communities(real_defs);

CREATE TABLE graph_nodes (
    id          TEXT PRIMARY KEY,
    label       TEXT NOT NULL,
    label_lc    TEXT NOT NULL,
    path        TEXT,        -- source path relative to the GPlates root
    line        INTEGER,
    community   INTEGER REFERENCES communities(id),
    is_class    INTEGER NOT NULL,
    is_callable INTEGER NOT NULL,
    file_type   TEXT
);
CREATE INDEX idx_gn_label ON graph_nodes(label_lc);
CREATE INDEX idx_gn_comm ON graph_nodes(community);
CREATE INDEX idx_gn_path ON graph_nodes(path, line);

CREATE TABLE graph_edges (
    src      TEXT NOT NULL,
    dst      TEXT NOT NULL,
    relation TEXT NOT NULL,
    weight   REAL
);
CREATE INDEX idx_ge_src ON graph_edges(src);
CREATE INDEX idx_ge_dst ON graph_edges(dst);
CREATE INDEX idx_ge_rel ON graph_edges(relation);
"""


def log(quiet, msg):
    if not quiet:
        print(msg, file=sys.stderr, flush=True)


def ensure_graphify() -> Path:
    if not GRAPHIFY_EXE.is_file():
        raise SkillError(
            "graphify is not installed.\n"
            "  cd %s && uv sync\n"
            "(needs uv: pip install uv)" % SKILL_DIR)
    return GRAPHIFY_EXE


def check_fast_backend() -> bool:
    """graspologic gives the native Rust Leiden backend; without it clustering crawls."""
    py = VENV_DIR / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    proc = subprocess.run([str(py), "-c", "import graspologic"],
                          capture_output=True, text=True)
    return proc.returncode == 0


def build_mirror(source_root: Path, quiet=False) -> int:
    """Mirror the tree, running C/C++ through the length-preserving preparation."""
    if MIRROR_DIR.exists():
        shutil.rmtree(MIRROR_DIR)
    cpp_parse.ensure_parser()
    n = prepared = 0
    for dirpath, dirnames, filenames in os.walk(source_root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fname in filenames:
            src = Path(dirpath) / fname
            ext = src.suffix.lower()
            if ext not in MIRROR_EXT:
                continue
            rel = src.relative_to(source_root)
            dst = MIRROR_DIR / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            data = src.read_bytes()
            if ext in CPP_EXT:
                out = cpp_parse.prepare(data)
                if len(out) != len(data) or out.count(b"\n") != data.count(b"\n"):
                    raise SkillError("preparation changed the size of %s - "
                                     "line numbers would be wrong" % rel)
                dst.write_bytes(out)
                prepared += 1
            else:
                dst.write_bytes(data)
            n += 1
    log(quiet, "  mirrored %d files (%d C/C++ prepared)" % (n, prepared))
    return n


def run_graphify(exe: Path, args, quiet=False):
    env = dict(os.environ)
    env["GRAPHIFY_OUT"] = str(GRAPH_OUT)
    env["GRAPHIFY_NO_TIPS"] = "1"
    proc = subprocess.run([str(exe), *args], env=env, capture_output=True, text=True,
                          encoding="utf-8", errors="replace")
    tail = (proc.stdout or "") + (proc.stderr or "")
    for line in tail.strip().splitlines():
        if line.strip():
            log(quiet, "    " + line.strip()[:200])
    if proc.returncode != 0:
        raise SkillError("graphify %s failed (exit %d)" % (args[0], proc.returncode))
    return tail


def rewrite_mirror_paths(source_root: Path, quiet=False) -> int:
    """Graphify records a few absolute paths; point them back at the real tree."""
    data = json.loads(GRAPH_JSON.read_text(encoding="utf-8"))
    mirror = str(MIRROR_DIR)
    real = str(source_root)
    fixed = 0
    for node in data.get("nodes", []):
        for key in ("definition_file", "source_file"):
            val = node.get(key)
            if isinstance(val, str) and mirror in val:
                node[key] = val.replace(mirror, real)
                fixed += 1
    if fixed:
        GRAPH_JSON.write_text(json.dumps(data), encoding="utf-8")
    log(quiet, "  rewrote %d mirror paths back to the source tree" % fixed)
    return fixed


def import_graph(source_root: Path, quiet=False) -> dict:
    """Load nodes, edges and communities into data/graph.db."""
    data = json.loads(GRAPH_JSON.read_text(encoding="utf-8"))
    nodes, links = data.get("nodes", []), data.get("links", [])
    if GRAPH_DB.exists():
        GRAPH_DB.unlink()
    con = sqlite3.connect(GRAPH_DB)
    con.executescript(GRAPH_SCHEMA)

    mirror = str(MIRROR_DIR).replace("\\", "/")
    real = str(source_root).replace("\\", "/")
    node_rows = []
    for n in nodes:
        path = (n.get("source_file") or "").replace("\\", "/")
        path = path.replace(mirror + "/", "").replace(real + "/", "")
        loc = n.get("source_location") or ""
        line = int(loc[1:]) if loc[:1].upper() == "L" and loc[1:].isdigit() else None
        node_rows.append((
            n["id"], n.get("label") or "", (n.get("label") or "").lower(),
            path or None, line, n.get("community"),
            1 if n.get("_callable_class") else 0,
            1 if n.get("_callable") else 0,
            n.get("file_type")))
    con.executemany(
        "INSERT OR REPLACE INTO graph_nodes(id, label, label_lc, path, line, community,"
        " is_class, is_callable, file_type) VALUES (?,?,?,?,?,?,?,?,?)", node_rows)

    con.executemany(
        "INSERT INTO graph_edges(src, dst, relation, weight) VALUES (?,?,?,?)",
        [(l.get("source"), l.get("target"), l.get("relation") or "?", l.get("weight"))
         for l in links])

    # Community summaries: size, dominant directories, representative members.
    con.execute("""
        INSERT INTO communities(id, name, size, located, real_defs, top_dirs, top_nodes)
        SELECT community, NULL, COUNT(*),
               SUM(CASE WHEN path IS NOT NULL THEN 1 ELSE 0 END), 0, NULL, NULL
        FROM graph_nodes WHERE community IS NOT NULL GROUP BY community""")
    names = {}
    for n in nodes:
        c = n.get("community")
        if c is not None and c not in names:
            names[c] = n.get("community_name")
    updates = []
    for (cid,) in con.execute("SELECT id FROM communities").fetchall():
        dirs = con.execute(
            "SELECT CASE WHEN instr(path,'/')>0 "
            "  THEN substr(path,1,length(path)-length(replace(path,'/','')) "
            "       - length(replace(path,'/','')) ) ELSE path END, COUNT(*) c "
            "FROM graph_nodes WHERE community=? AND path IS NOT NULL "
            "GROUP BY 1 ORDER BY c DESC LIMIT 3", (cid,)).fetchall()
        top_dirs = ", ".join(d[0] for d in dirs if d[0])
        members = con.execute(
            "SELECT label FROM graph_nodes WHERE community=? "
            "ORDER BY is_class DESC, length(label) LIMIT 6", (cid,)).fetchall()
        updates.append((names.get(cid), top_dirs or None,
                        ", ".join(m[0] for m in members), cid))
    con.executemany(
        "UPDATE communities SET name=?, top_dirs=?, top_nodes=? WHERE id=?", updates)

    _count_real_defs(con)

    stats = {
        "nodes": con.execute("SELECT COUNT(*) FROM graph_nodes").fetchone()[0],
        "edges": con.execute("SELECT COUNT(*) FROM graph_edges").fetchone()[0],
        "communities": con.execute("SELECT COUNT(*) FROM communities").fetchone()[0],
    }
    meta = {
        "source_root": str(source_root),
        "built_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "graph_json": str(GRAPH_JSON),
        **{"count_" + k: str(v) for k, v in stats.items()},
    }
    con.executemany("INSERT INTO meta(key, value) VALUES (?,?)", sorted(meta.items()))
    con.commit()
    con.execute("VACUUM")
    con.close()
    log(quiet, "  imported %d nodes, %d edges, %d communities"
        % (stats["nodes"], stats["edges"], stats["communities"]))
    return stats


def _count_real_defs(con):
    """How many members of each community sit on a real definition, not a stub.

    The largest communities are dominated by forward declarations, so raw node
    count is a poor guide to which cluster is worth reading. This gives
    `gpq community --list` something meaningful to rank by.
    """
    _MAIN_DB = DB_PATH
    if not _MAIN_DB.exists():
        return
    # Plain path, not a file: URI - this connection was not opened with uri=True.
    con.execute("ATTACH DATABASE ? AS main_idx", (str(_MAIN_DB),))
    con.execute("""
        UPDATE communities SET real_defs = (
            SELECT COUNT(*) FROM graph_nodes n
            WHERE n.community = communities.id
              AND EXISTS (SELECT 1 FROM main_idx.entities e
                          JOIN main_idx.files f ON f.id = e.file_id
                          WHERE f.path = n.path AND e.line = n.line AND e.is_def = 1))""")
    con.commit()
    con.execute("DETACH DATABASE main_idx")


def resolve_dirs(quiet=False):
    """Fill communities.top_dirs using real directory names (simpler in Python)."""
    con = sqlite3.connect(GRAPH_DB)
    import collections
    per = collections.defaultdict(collections.Counter)
    for cid, path in con.execute(
            "SELECT community, path FROM graph_nodes "
            "WHERE community IS NOT NULL AND path IS NOT NULL"):
        per[cid][path.rsplit("/", 1)[0] if "/" in path else "."] += 1
    con.executemany("UPDATE communities SET top_dirs = ? WHERE id = ?",
                    [(", ".join("%s(%d)" % (d, n) for d, n in c.most_common(3)), cid)
                     for cid, c in per.items()])
    con.commit()
    con.close()


def verify(quiet=False) -> int:
    if not GRAPH_DB.exists():
        raise SkillError("no graph index - run: python scripts/build_graph.py")
    con = sqlite3.connect(GRAPH_DB)
    stats = {k: con.execute("SELECT COUNT(*) FROM " + t).fetchone()[0]
             for k, t in (("nodes", "graph_nodes"), ("edges", "graph_edges"),
                          ("communities", "communities"))}
    meta = dict(con.execute("SELECT key, value FROM meta"))
    con.close()
    print("graph  : %s (%.1f MB)" % (GRAPH_DB, GRAPH_DB.stat().st_size / 1048576))
    print("source : %s" % meta.get("source_root"))
    print("built  : %s" % meta.get("built_at"))
    for k, v in sorted(stats.items()):
        print("  %-14s %d" % (k, v))
    problems = []
    if stats["nodes"] < MIN_NODES:
        problems.append("nodes: %d (expected >= %d)" % (stats["nodes"], MIN_NODES))
    if stats["edges"] < MIN_EDGES:
        problems.append("edges: %d (expected >= %d)" % (stats["edges"], MIN_EDGES))
    if stats["communities"] < MIN_COMMUNITIES:
        problems.append("communities: %d (expected >= %d)"
                        % (stats["communities"], MIN_COMMUNITIES))
    if problems:
        print("\nFAILED checks:", file=sys.stderr)
        for p in problems:
            print("  " + p, file=sys.stderr)
        return 1
    print("\ngraph checks passed")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="verify an existing graph and exit")
    ap.add_argument("--no-cluster", action="store_true",
                    help="extract only; skip Leiden community detection")
    ap.add_argument("--label", action="store_true",
                    help="name communities with an LLM (slow; needs a configured backend)")
    ap.add_argument("--keep-mirror", action="store_true",
                    help="keep data/graph-src after the build (for debugging)")
    ap.add_argument("-q", "--quiet", action="store_true")
    args = ap.parse_args(argv)

    try:
        if args.check:
            return verify(args.quiet)

        cfg = read_config()
        source_root, version = check_source_root(cfg["source_root"])
        exe = ensure_graphify()
        log(args.quiet, "source : %s (GPlates %s)"
            % (source_root, ".".join(map(str, version))))

        fast = check_fast_backend()
        if not fast and not args.no_cluster:
            log(args.quiet, "WARNING: graspologic missing - clustering will use the slow "
                            "single-core fallback (tens of minutes). Fix with: uv sync")
        else:
            log(args.quiet, "clustering backend: %s"
                % ("native Rust Leiden (fast)" if fast else "n/a (--no-cluster)"))

        started = time.time()
        log(args.quiet, "mirroring source with Qt/preprocessor preparation...")
        build_mirror(source_root, args.quiet)

        log(args.quiet, "extracting graph...")
        GRAPH_OUT.mkdir(parents=True, exist_ok=True)
        run_graphify(exe, ["update", str(MIRROR_DIR), "--no-cluster"], args.quiet)

        if not args.no_cluster:
            log(args.quiet, "clustering (Leiden)...")
            cluster_args = ["cluster-only", str(MIRROR_DIR), "--no-viz"]
            if not args.label:
                cluster_args.append("--no-label")
            run_graphify(exe, cluster_args, args.quiet)

        rewrite_mirror_paths(source_root, args.quiet)
        log(args.quiet, "importing into %s ..." % GRAPH_DB.name)
        stats = import_graph(source_root, args.quiet)
        resolve_dirs(args.quiet)

        if not args.keep_mirror:
            shutil.rmtree(MIRROR_DIR, ignore_errors=True)

        log(args.quiet, "done in %.0fs" % (time.time() - started))
        print("graph ready: %s (%.1f MB)"
              % (GRAPH_DB, GRAPH_DB.stat().st_size / 1048576))
        print("  %d nodes, %d edges, %d communities"
              % (stats["nodes"], stats["edges"], stats["communities"]))
        print("next: python scripts/gpq.py community <symbol>")
        return 0
    except SkillError as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
