"""Walks a GPlates source tree and writes the SQLite index."""

from __future__ import annotations

import json
import os
import sqlite3
import sys
import time
from pathlib import Path

from . import build, cpp_extract, cpp_parse, resolve
from .common import DB_PATH, SkillError
from .schema import SCHEMA

# Minimum row counts a healthy GPlates index must reach. Anything less means the
# source tree, ctags, or an extractor is broken, so the build fails loudly.
SANITY_MINIMUMS = {
    "files": 2000,
    "cpp_files": 1800,
    "symbols": 40000,
    "classes": 2000,
    "functions": 20000,
    "lines": 500000,
    "includes": 15000,
    "ui_forms": 120,
    "ui_widgets": 2000,
    "qt_connections": 1000,
    "py_api": 50,
    "gpgim_features": 80,
    "gpgim_properties": 80,
    "entities": 80000,
    "entity_classes": 3000,
    "entity_methods": 15000,
    "entity_macros": 900,
    "bases": 1200,
    "inherit_closure": 800,
    "occurrences": 350000,
    "occurrences_resolved": 250000,
}


def log(quiet, msg):
    if not quiet:
        print(msg, file=sys.stderr, flush=True)


def walk_files(root: Path):
    """Yield (relative_posix_path, absolute Path) for every file worth recording."""
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in build.SKIP_DIRS)
        for fname in sorted(filenames):
            abs_path = Path(dirpath) / fname
            rel = abs_path.relative_to(root).as_posix()
            yield rel, abs_path


def build_index(source_root: Path, version, ctags_exe: Path, tags_file: Path,
                quiet: bool = False) -> dict:
    started = time.time()
    if DB_PATH.exists():
        DB_PATH.unlink()
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    con = sqlite3.connect(DB_PATH)
    con.executescript(SCHEMA)

    # ---- files ------------------------------------------------------------
    log(quiet, "scanning files...")
    file_ids = {}
    file_rows = []
    text_files = []
    for rel, abs_path in walk_files(source_root):
        try:
            size = abs_path.stat().st_size
        except OSError:
            continue
        name = abs_path.name
        ext = abs_path.suffix.lower()
        category = build.classify(rel, ext, name)
        wants_text = build.is_text(ext, name) and size <= build.MAX_TEXT_BYTES
        rel_dir = rel.rsplit("/", 1)[0] if "/" in rel else ""
        file_rows.append((rel, rel_dir, name, ext, category, size, wants_text))
        if wants_text:
            text_files.append((rel, abs_path))

    for i, (rel, rel_dir, name, ext, category, size, wants_text) in enumerate(file_rows, 1):
        file_ids[rel] = i
    con.executemany(
        "INSERT INTO files(id, path, dir, name, ext, category, size, lines, has_text) "
        "VALUES (?,?,?,?,?,?,?,0,?)",
        [(file_ids[r[0]], r[0], r[1], r[2], r[3], r[4], r[5], int(r[6])) for r in file_rows],
    )
    con.commit()
    log(quiet, "  %d files (%d with text content)" % (len(file_rows), len(text_files)))

    # ---- content, includes, Qt connections, python bindings ---------------
    log(quiet, "reading file contents...")
    line_rows, include_rows, conn_rows, pyapi_rows = [], [], [], []
    line_counts = {}
    rowid = 0
    for rel, abs_path in text_files:
        fid = file_ids[rel]
        try:
            text = abs_path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        lines = text.splitlines()
        line_counts[fid] = len(lines)
        for n, line in enumerate(lines, 1):
            rowid += 1
            line_rows.append((rowid, fid, n, line[:2000]))
        ext = abs_path.suffix.lower()
        if ext in build.CPP_EXT:
            for n, header, is_sys in build.extract_includes(text):
                include_rows.append((fid, n, header, is_sys))
            if "connect" in text:
                for row in build.extract_connections(text):
                    conn_rows.append((fid,) + row)
            if "class_<" in text or "enum_<" in text or "def(" in text:
                for n, owner, pyname, kind, cpp in build.extract_py_api(text):
                    pyapi_rows.append((fid, n, owner, pyname, kind, cpp))
        if len(line_rows) > 200000:
            con.executemany("INSERT INTO lines(id, file_id, line, text) VALUES (?,?,?,?)",
                            line_rows)
            line_rows = []
    if line_rows:
        con.executemany("INSERT INTO lines(id, file_id, line, text) VALUES (?,?,?,?)", line_rows)
    con.executemany("UPDATE files SET lines = ? WHERE id = ?",
                    [(v, k) for k, v in line_counts.items()])
    con.executemany("INSERT INTO includes(file_id, line, header, is_system, target_id) "
                    "VALUES (?,?,?,?,NULL)", include_rows)
    con.executemany("INSERT INTO qt_connections(file_id, line, sender, signal, receiver, slot) "
                    "VALUES (?,?,?,?,?,?)", conn_rows)
    con.executemany("INSERT INTO py_api(file_id, line, owner, name, kind, cpp_type) "
                    "VALUES (?,?,?,?,?,?)", pyapi_rows)
    con.commit()
    log(quiet, "  %d lines, %d includes, %d Qt connections, %d python bindings"
        % (rowid, len(include_rows), len(conn_rows), len(pyapi_rows)))

    # Resolve #include "..." to in-tree files by longest matching suffix.
    by_suffix = {}
    for rel in file_ids:
        by_suffix.setdefault(rel.rsplit("/", 1)[-1], []).append(rel)
    resolved = []
    for fid, n, header, is_sys in include_rows:
        base = header.rsplit("/", 1)[-1]
        best = None
        for cand in by_suffix.get(base, ()):
            if cand.endswith(header) and (best is None or len(cand) < len(best)):
                best = cand
        if best:
            resolved.append((file_ids[best], fid, n, header))
    con.executemany(
        "UPDATE includes SET target_id = ? WHERE file_id = ? AND line = ? AND header = ?",
        resolved)
    con.commit()
    log(quiet, "  %d includes resolved to in-tree headers" % len(resolved))

    # ---- full text search -------------------------------------------------
    log(quiet, "building full-text index...")
    con.execute("INSERT INTO lines_fts(lines_fts) VALUES ('rebuild')")
    con.commit()

    # ---- ctags symbols ----------------------------------------------------
    log(quiet, "running ctags...")
    targets = [d for d in ("src", "scripts", "cmake") if (source_root / d).is_dir()]
    if not targets:
        raise SkillError("no src/ directory to index under %s" % source_root)
    size = build.run_ctags(ctags_exe, source_root, tags_file, targets)
    log(quiet, "  ctags wrote %.1f MB of tags" % (size / 1048576))

    log(quiet, "loading symbols...")
    sym_rows = []
    skipped_paths = 0
    with tags_file.open(encoding="utf-8", errors="replace") as fh:
        for raw in fh:
            raw = raw.strip()
            if not raw or raw[0] != "{":
                continue
            try:
                tag = json.loads(raw)
            except json.JSONDecodeError:
                continue
            if tag.get("_type") != "tag":
                continue
            kind = tag.get("kind")
            if not kind or kind in build.SKIP_KINDS:
                continue
            rel = tag["path"].replace("\\", "/")
            fid = file_ids.get(rel)
            if fid is None:
                skipped_paths += 1
                continue
            if kind == "header":
                continue  # already covered by the includes table
            if "qualified" in (tag.get("extras") or ""):
                continue  # duplicate of the plain tag, with the scope baked into the name
            name = tag.get("name") or ""
            sym_rows.append((
                name, name.lower(), kind, tag.get("language"), fid,
                tag.get("line") or 0, tag.get("end"),
                tag.get("scope"), tag.get("scopeKind"), tag.get("signature"),
                tag.get("typeref"), tag.get("access"), tag.get("inherits"),
                0 if kind in build.DECL_KINDS else 1,
            ))
            if len(sym_rows) >= 50000:
                _insert_symbols(con, sym_rows)
                sym_rows = []
    if sym_rows:
        _insert_symbols(con, sym_rows)
    con.commit()
    if skipped_paths:
        log(quiet, "  warning: %d tags referenced unknown paths" % skipped_paths)

    # ---- Qt Designer forms ------------------------------------------------
    log(quiet, "parsing Qt .ui forms...")
    form_rows, widget_rows = [], []
    for rel, abs_path in text_files:
        if abs_path.suffix.lower() != ".ui":
            continue
        fid = file_ids[rel]
        form, widgets = build.extract_ui(abs_path)
        if form is None:
            continue
        form_rows.append((fid, form[0], form[1], form[2]))
        for wclass, wname, wtext in widgets:
            widget_rows.append((fid, form[0], wclass, wname, wtext))
    con.executemany("INSERT INTO ui_forms(file_id, class_name, base_class, title) "
                    "VALUES (?,?,?,?)", form_rows)
    con.executemany("INSERT INTO ui_widgets(file_id, form, widget_class, object_name, text) "
                    "VALUES (?,?,?,?,?)", widget_rows)
    con.commit()
    log(quiet, "  %d forms, %d widgets" % (len(form_rows), len(widget_rows)))

    # ---- GPGIM ------------------------------------------------------------
    log(quiet, "parsing GPGIM...")
    gpgim_path = source_root / "src" / "qt-resources" / "gpgim" / "gpgim.xml"
    gfid = file_ids.get("src/qt-resources/gpgim/gpgim.xml")
    features, properties, links = build.extract_gpgim(gpgim_path)
    con.executemany(
        "INSERT INTO gpgim_features(file_id, line, name, class_type, inherits, description, "
        "default_geometry) VALUES (?,?,?,?,?,?,?)",
        [(gfid,) + row for row in features])
    con.executemany(
        "INSERT INTO gpgim_properties(file_id, line, name, types, multiplicity, description) "
        "VALUES (?,?,?,?,?,?)",
        [(gfid,) + row for row in properties])
    con.executemany("INSERT INTO gpgim_feature_properties(feature, property) VALUES (?,?)", links)
    con.commit()
    log(quiet, "  %d feature classes, %d properties, %d links"
        % (len(features), len(properties), len(links)))

    # ---- deep C++ index (tree-sitter) -------------------------------------
    build_deep_index(con, source_root, file_ids, quiet)

    # ---- meta -------------------------------------------------------------
    meta = {
        "source_root": str(source_root),
        "gplates_version": ".".join(map(str, version)),
        "built_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "build_seconds": "%.1f" % (time.time() - started),
        "ctags": str(ctags_exe),
        "schema_version": "1",
    }
    con.executemany("INSERT INTO meta(key, value) VALUES (?,?)", sorted(meta.items()))
    con.commit()

    stats = collect_stats(con)
    con.executemany("INSERT INTO meta(key, value) VALUES (?,?)",
                    [("count_" + k, str(v)) for k, v in sorted(stats.items())])
    con.commit()
    con.execute("PRAGMA optimize")
    con.execute("VACUUM")
    con.close()
    return stats


DEEP_EXTS = {".cc", ".cpp", ".cxx", ".c", ".h", ".hh", ".hpp", ".hxx"}


def build_deep_index(con, source_root, file_ids, quiet=False):
    """Parse every C/C++ file with tree-sitter and record entities, bases, occurrences."""
    cpp_parse.ensure_parser()
    targets = [(rel, fid) for rel, fid in sorted(file_ids.items())
               if Path(rel).suffix.lower() in DEEP_EXTS and (source_root / rel).is_file()]
    log(quiet, "deep parse: %d C/C++ files" % len(targets))

    # Pass 1 - declarations.
    ent_rows, base_rows = [], []
    next_id = 1
    err_bytes = tot_bytes = 0
    for rel, fid in targets:
        data = cpp_parse.prepare((source_root / rel).read_bytes())
        tree = cpp_parse.parse(data)
        tot_bytes += len(data)
        err_bytes += cpp_parse.error_extent(tree)
        sink = cpp_extract.Sink()
        cpp_extract.extract_entities(data, tree, sink)
        base_id = next_id
        for e in sink.entities:
            parent = None if e["parent"] is None else base_id + e["parent"]
            ent_rows.append((next_id, e["name"], e["name"].lower(), e["qname"], e["kind"],
                             fid, e["line"], e["col"], e["end_line"], parent,
                             e["type_text"], e["signature"], e["access"], e["storage"],
                             e["is_def"], e["is_template"], e["template_params"]))
            next_id += 1
        for idx, bname, access, virt in sink.bases:
            base_rows.append((base_id + idx, bname, resolve.base_key(bname),
                              access, 1 if virt else 0))
    con.executemany(
        "INSERT INTO entities(id, name, name_lc, qname, kind, file_id, line, col, end_line,"
        " parent_id, type_text, signature, access, storage, is_def, is_template,"
        " template_params) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", ent_rows)
    con.executemany(
        "INSERT INTO bases(entity_id, base_name, base_key, base_entity_id, access, is_virtual)"
        " VALUES (?,?,?,NULL,?,?)", base_rows)
    con.commit()
    log(quiet, "  %d entities, %d base edges (%.3f%% of bytes unparsed)"
        % (len(ent_rows), len(base_rows), 100.0 * err_bytes / max(tot_bytes, 1)))

    known = {row[0] for row in con.execute("SELECT DISTINCT name FROM entities")}

    # Pass 2 - occurrences.
    occ_rows = []
    oid = 0
    for rel, fid in targets:
        data = cpp_parse.prepare((source_root / rel).read_bytes())
        tree = cpp_parse.parse(data)
        sink = cpp_extract.Sink()
        cpp_extract.extract_occurrences(data, tree, sink, known)
        for line, col, name, role in sink.occurrences:
            oid += 1
            occ_rows.append((oid, fid, line, col, name, name.lower(), role))
        if len(occ_rows) >= 200000:
            _insert_occurrences(con, occ_rows)
            occ_rows = []
    if occ_rows:
        _insert_occurrences(con, occ_rows)
    con.commit()
    log(quiet, "  %d occurrences" % oid)

    # Enclosing function/method for each occurrence.
    con.execute(
        "UPDATE occurrences SET container_id = ("
        "  SELECT e.id FROM entities e"
        "  WHERE e.file_id = occurrences.file_id AND e.is_def = 1"
        "    AND e.kind IN ('function','method','constructor','destructor','operator')"
        "    AND occurrences.line BETWEEN e.line AND e.end_line"
        "  ORDER BY e.end_line - e.line LIMIT 1)")
    con.commit()

    log(quiet, "resolving references...")
    resolve.resolve_bases(con, lambda m: log(quiet, m))
    resolve.build_closure(con, lambda m: log(quiet, m))
    resolve.resolve_occurrences(con, lambda m: log(quiet, m))


def _insert_occurrences(con, rows):
    con.executemany(
        "INSERT INTO occurrences(id, file_id, line, col, name, name_lc, role)"
        " VALUES (?,?,?,?,?,?,?)", rows)


def _insert_symbols(con, rows):
    con.executemany(
        "INSERT INTO symbols(name, name_lc, kind, lang, file_id, line, end_line, scope, "
        "scope_kind, signature, typeref, access, inherits, is_def) "
        "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", rows)


def collect_stats(con) -> dict:
    q = lambda sql: con.execute(sql).fetchone()[0]
    return {
        "files": q("SELECT COUNT(*) FROM files"),
        "cpp_files": q("SELECT COUNT(*) FROM files WHERE category='cpp'"),
        "symbols": q("SELECT COUNT(*) FROM symbols"),
        "classes": q("SELECT COUNT(*) FROM symbols WHERE kind IN ('class','struct','union')"),
        "functions": q("SELECT COUNT(*) FROM symbols WHERE kind IN ('function','prototype')"),
        "lines": q("SELECT COUNT(*) FROM lines"),
        "includes": q("SELECT COUNT(*) FROM includes"),
        "ui_forms": q("SELECT COUNT(*) FROM ui_forms"),
        "ui_widgets": q("SELECT COUNT(*) FROM ui_widgets"),
        "qt_connections": q("SELECT COUNT(*) FROM qt_connections"),
        "py_api": q("SELECT COUNT(*) FROM py_api"),
        "gpgim_features": q("SELECT COUNT(*) FROM gpgim_features"),
        "gpgim_properties": q("SELECT COUNT(*) FROM gpgim_properties"),
        "entities": q("SELECT COUNT(*) FROM entities"),
        "entity_classes": q("SELECT COUNT(*) FROM entities WHERE kind IN "
                            "('class','struct','union')"),
        "entity_methods": q("SELECT COUNT(*) FROM entities WHERE kind IN "
                            "('method','function','constructor','destructor','operator')"),
        "entity_macros": q("SELECT COUNT(*) FROM entities WHERE kind IN "
                           "('macro','macro_function')"),
        "bases": q("SELECT COUNT(*) FROM bases"),
        "inherit_closure": q("SELECT COUNT(*) FROM inherit_closure"),
        "occurrences": q("SELECT COUNT(*) FROM occurrences"),
        "occurrences_resolved": q("SELECT COUNT(*) FROM occurrences "
                                  "WHERE entity_id IS NOT NULL"),
    }


def verify_stats(stats: dict):
    """Return the list of sanity checks that came out short."""
    return [
        "%s: %d (expected at least %d)" % (key, stats.get(key, 0), minimum)
        for key, minimum in sorted(SANITY_MINIMUMS.items())
        if stats.get(key, 0) < minimum
    ]
