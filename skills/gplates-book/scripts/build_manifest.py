#!/usr/bin/env python3
"""Build data/manifest.jsonl - one record per documentation unit.

Reads the gplates-code index, pairs source files into units, computes the tier
signals, resolves page paths and writes the manifest, the path map, the
component extras (files that get a component-page table row instead of a page)
and the unit-to-unit reference graph.

    python scripts/build_manifest.py            # build and print the summary
    python scripts/build_manifest.py --top 50   # also list the top tier-1 units

Every number is derived from the index at run time; nothing is hard-coded.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from bookkit import (  # noqa: E402
    BookError, COMPONENT_TIER_BIAS, DATA_DIR, PATH_MAP_PATH, REFGRAPH_PATH,
    component_of, index_meta, open_graph, open_index, save_json, save_manifest,
    sha256_lf,
)

# Share of units per tier (Writer.md "Tiering").  Applied to the bias-adjusted
# ranking, so the prior reorders units without inflating the expensive tiers.
TIER1_SHARE = 0.12
TIER2_SHARE = 0.45

# Score weights.  log10 throughout: fan-in spans five orders of magnitude and a
# linear term would let a single hub drown every other signal.
WEIGHTS = {
    "fan_in": 3.0,
    "fan_in_units": 1.5,
    "inherit": 0.7,
    "templates": 0.5,
    "lines": 1.2,
    "members": 0.5,
    "macros": 0.3,
}

# Units that are not C++ pairs do not compete in the ranking - their tier is
# their nature, not their fan-in.
FIXED_TIER_KINDS = {"shader": 2, "gpgim": 2, "python": 3}


def stem_of(name: str, ext: str) -> str:
    return name[: -len(ext)] if ext and name.endswith(ext) else name


def build_units(db):
    """Group `files` rows into units and return (units, extras, file_to_unit)."""
    files = [dict(r) for r in db.execute(
        "SELECT id, path, dir, name, ext, category, lines FROM files ORDER BY path")]
    by_id = {f["id"]: f for f in files}
    for f in files:
        f["component"] = component_of(f["path"], f["category"])

    units: dict[str, dict] = {}
    claimed: set[str] = set()

    def new_unit(uid, kind, name, directory, component):
        units[uid] = {"id": uid, "kind": kind, "name": name, "dir": directory,
                      "component": component, "files": [], "attached": []}
        return units[uid]

    # --- C++ units: one .h/.cc pair (or a lone file) per (dir, stem) ---------
    cpp_index: dict[tuple[str, str], str] = {}
    groups: dict[tuple[str, str], list[dict]] = collections.defaultdict(list)
    for f in files:
        if f["category"] == "cpp":
            groups[(f["dir"], stem_of(f["name"], f["ext"]))].append(f)
    for (directory, stem), members in sorted(groups.items()):
        component = members[0]["component"]
        uid = unit_id(directory, stem, component)
        unit = new_unit(uid, "cpp", stem, directory, component)
        # Header first: it is the page's natural reading order.
        unit["files"] = [m["path"] for m in sorted(members, key=lambda m: (m["ext"] != ".h", m["path"]))]
        cpp_index[(directory, stem)] = uid
        claimed.update(unit["files"])

    # --- shader units: one page per shader directory ------------------------
    shader_dirs: dict[str, list[dict]] = collections.defaultdict(list)
    for f in files:
        if f["category"] == "shader":
            shader_dirs[f["dir"]].append(f)
    for directory, members in sorted(shader_dirs.items()):
        stem = directory.rsplit("/", 1)[-1]
        unit = new_unit(f"shaders/{stem}", "shader", stem, directory, "shaders")
        unit["files"] = sorted(m["path"] for m in members)
        claimed.update(unit["files"])

    # --- the GPGIM model: one page over the whole XML/XSD/XSL set -----------
    gpgim = [f for f in files if f["category"] == "gpgim"]
    if gpgim:
        directory = "src/qt-resources/gpgim"
        unit = new_unit("qt-resources/gpgim", "gpgim", "gpgim", directory, "qt-resources")
        unit["files"] = sorted(f["path"] for f in gpgim)
        claimed.update(unit["files"])

    # --- the demo/utility Python scripts: one page ---------------------------
    py = [f for f in files if f["category"] == "python" and f["dir"] == "scripts"]
    if py:
        unit = new_unit("python-examples/scripts", "python", "python-examples",
                        "scripts", "python-examples")
        unit["files"] = sorted(f["path"] for f in py)
        claimed.update(unit["files"])

    # --- Qt Designer forms attach to the widget class they generate ---------
    # Most forms sit next to a same-named .h/.cc pair; the rest are resolved
    # through the class definition itself (several widgets share one header).
    class_file = {}
    for row in db.execute(
            "SELECT name, file_id FROM entities WHERE kind = 'class' AND is_def = 1"):
        class_file.setdefault(row["name"], row["file_id"])
    for row in db.execute("SELECT file_id, class_name FROM ui_forms"):
        f = by_id[row["file_id"]]
        if f["path"] in claimed:
            continue
        stem = stem_of(f["name"], f["ext"])
        owner = by_id.get(class_file.get(row["class_name"]))
        target = (cpp_index.get((f["dir"], row["class_name"]))
                  or cpp_index.get((f["dir"], stem[:-2] if stem.endswith("Ui") else stem))
                  or (owner and cpp_index.get(
                      (owner["dir"], stem_of(owner["name"], owner["ext"])))))
        if target:
            units[target]["attached"].append(f["path"])
            claimed.add(f["path"])

    # --- everything else is a component-page table row ----------------------
    extras: dict[str, list[dict]] = collections.defaultdict(list)
    for f in files:
        if f["path"] not in claimed:
            extras[f["component"]].append(
                {"path": f["path"], "category": f["category"], "lines": f["lines"]})

    file_to_unit = {}
    for unit in units.values():
        for path in unit["files"] + unit["attached"]:
            file_to_unit[path] = unit["id"]
    return units, dict(extras), file_to_unit, by_id


def unit_id(directory: str, stem: str, component: str) -> str:
    """Stable, human-readable id: `<component>/<sub dirs>/<stem>`."""
    prefix = directory
    for root in ("src/", ):
        if prefix.startswith(root):
            prefix = prefix[len(root):]
            break
    if prefix in ("src", "scripts", ""):
        prefix = component
    parts = [p for p in prefix.split("/") if p]
    if parts and parts[0] != component:
        parts = [component] + parts
    return "/".join(parts + [stem])


def page_for(unit: dict) -> str:
    """Book-relative page path, mirroring the source tree under `src/`."""
    directory = unit["dir"]
    if unit["kind"] == "shader":
        # A shader unit is a whole directory, so its page takes the directory's
        # own name rather than repeating it (`.../scalar_field_3d.md`).
        return f"src/{directory[4:]}.md"
    if directory.startswith("src/"):
        rel = directory[4:]
    elif directory == "src":
        rel = "entry-points"
    else:
        rel = directory
    return f"src/{rel}/{unit['name']}.md"


def resolve_pages(units: dict[str, dict]) -> dict[str, str]:
    """Assign pages, disambiguating case-insensitive collisions with a hash."""
    taken: dict[str, str] = {}
    path_map: dict[str, str] = {}
    for uid in sorted(units):
        page = page_for(units[uid])
        key = page.lower()
        if key in taken and taken[key] != uid:
            suffix = hashlib.sha256(uid.encode()).hexdigest()[:6]
            page = page[:-3] + f"-{suffix}.md"
            key = page.lower()
            if key in taken:
                raise BookError(f"unresolvable page collision for {uid}")
        taken[key] = uid
        units[uid]["page"] = page
        path_map[uid] = page
    return path_map


# ---------------------------------------------------------------------------
# Tier signals
# ---------------------------------------------------------------------------

def collect_signals(db, units, file_to_unit, by_id):
    """Aggregate index signals per unit, and the unit-to-unit reference graph."""
    path_of = {f["id"]: f["path"] for f in by_id.values()}
    unit_of_file_id = {fid: file_to_unit[p] for fid, p in path_of.items() if p in file_to_unit}

    sig = {uid: collections.Counter() for uid in units}
    for uid, unit in units.items():
        sig[uid]["lines"] = sum(by_id[fid]["lines"] for fid in path_of
                                if path_of[fid] in unit["files"] + unit["attached"])

    # A cheaper second pass over files avoids the O(units x files) loop above.
    lines_by_unit = collections.Counter()
    for fid, path in path_of.items():
        uid = unit_of_file_id.get(fid)
        if uid:
            lines_by_unit[uid] += by_id[fid]["lines"]
    for uid in units:
        sig[uid]["lines"] = lines_by_unit[uid]

    for row in db.execute("""
            SELECT file_id, kind, is_template, COUNT(*) AS n
            FROM entities GROUP BY file_id, kind, is_template"""):
        uid = unit_of_file_id.get(row["file_id"])
        if not uid:
            continue
        kind, n = row["kind"], row["n"]
        if row["is_template"]:
            sig[uid]["templates"] += n
        if kind in ("method", "field", "constructor", "destructor", "operator"):
            sig[uid]["members"] += n
        elif kind in ("macro", "macro_function"):
            sig[uid]["macros"] += n
        elif kind in ("class", "struct", "union", "enum"):
            sig[uid]["types"] += n

    for row in db.execute("""
            SELECT e.file_id AS fid, COUNT(*) AS n
            FROM inherit_closure ic JOIN entities e ON e.id = ic.ancestor_id
            GROUP BY e.file_id"""):
        uid = unit_of_file_id.get(row["fid"])
        if uid:
            sig[uid]["inherit"] += row["n"]

    # Fan-in and the reference graph come from the same aggregation.
    refs: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    for row in db.execute("""
            SELECT o.file_id AS src, e.file_id AS dst, COUNT(*) AS n
            FROM occurrences o JOIN entities e ON e.id = o.entity_id
            WHERE o.entity_id IS NOT NULL AND o.role NOT IN ('def', 'decl')
            GROUP BY o.file_id, e.file_id"""):
        src, dst = unit_of_file_id.get(row["src"]), unit_of_file_id.get(row["dst"])
        if not src or not dst or src == dst:
            continue
        refs[src][dst] += row["n"]
        sig[dst]["fan_in"] += row["n"]
        sig[dst]["fan_in_units"] += 1

    for row in db.execute("SELECT file_id, target_id FROM includes WHERE target_id IS NOT NULL"):
        src, dst = unit_of_file_id.get(row["file_id"]), unit_of_file_id.get(row["target_id"])
        if src and dst and src != dst:
            refs[src][dst] += 1

    return sig, {src: dict(counts) for src, counts in refs.items()}


def score_of(signals: collections.Counter) -> float:
    return sum(w * math.log10(1 + signals[key]) for key, w in WEIGHTS.items())


def assign_tiers(units: dict[str, dict]) -> None:
    """Rank the C++ units on their bias-adjusted score and cut at the shares."""
    ranked = [u for u in units.values() if u["kind"] == "cpp"]
    for unit in ranked:
        bias = COMPONENT_TIER_BIAS.get(unit["component"], 0)
        unit["adjusted"] = unit["score"] + bias * 0.9
    ranked.sort(key=lambda u: (-u["adjusted"], u["id"]))
    n = len(ranked)
    cut1, cut2 = int(n * TIER1_SHARE), int(n * (TIER1_SHARE + TIER2_SHARE))
    for i, unit in enumerate(ranked):
        unit["tier"] = 1 if i < cut1 else (2 if i < cut2 else 3)
    for unit in units.values():
        if unit["kind"] != "cpp":
            unit["tier"] = FIXED_TIER_KINDS[unit["kind"]]
            unit.setdefault("adjusted", unit["score"])
        if unit["deprecated"]:
            unit["tier"] = 3


def attach_communities(units: dict[str, dict]) -> None:
    """Label each unit with its dominant Leiden community, when the graph exists."""
    graph = open_graph()
    if graph is None:
        for unit in units.values():
            unit["community"] = None
            unit["community_name"] = None
        return
    names = {r["id"]: (r["name"] or f"Community {r['id']}")
             for r in graph.execute("SELECT id, name FROM communities")}
    by_path: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    for row in graph.execute("SELECT path, community FROM graph_nodes WHERE path IS NOT NULL"):
        if row["community"] is not None:
            by_path[row["path"]][row["community"]] += 1
    for unit in units.values():
        votes: collections.Counter = collections.Counter()
        for path in unit["files"]:
            votes.update(by_path.get(path, {}))
        if votes:
            top = votes.most_common(1)[0][0]
            unit["community"], unit["community_name"] = top, names.get(top, f"Community {top}")
        else:
            unit["community"] = unit["community_name"] = None
    graph.close()


# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--top", type=int, default=0, help="list the N highest scoring units")
    args = ap.parse_args()

    db = open_index()
    meta = index_meta(db)
    source_root = Path(meta["source_root"])

    units, extras, file_to_unit, by_id = build_units(db)
    signals, refs = collect_signals(db, units, file_to_unit, by_id)

    line_text = collections.defaultdict(list)
    for unit in units.values():
        unit["deprecated"] = any("deprecated" in p.lower() for p in unit["files"])
        unit["signals"] = dict(signals[unit["id"]])
        unit["score"] = round(score_of(signals[unit["id"]]), 3)

    assign_tiers(units)
    attach_communities(units)
    path_map = resolve_pages(units)

    # Cache key: LF-normalised content hash of every member file, folded into one.
    for unit in units.values():
        digests = [f"{path}:{sha256_lf(source_root, path)}"
                   for path in unit["files"] + unit["attached"]]
        unit["hash"] = hashlib.sha256("\n".join(digests).encode()).hexdigest()
        unit["adjusted"] = round(unit.get("adjusted", unit["score"]), 3)

    ordered = sorted(units.values(), key=lambda u: (u["component"], u["id"]))
    save_manifest(ordered)
    save_json(PATH_MAP_PATH, path_map)
    save_json(DATA_DIR / "extras.json", extras)
    save_json(REFGRAPH_PATH, refs)

    report(db, ordered, extras, by_id, args.top)
    db.close()
    return 0


def report(db, units, extras, by_id, top):
    total_files = len(by_id)
    covered = sum(len(u["files"]) + len(u["attached"]) for u in units)
    extra_files = sum(len(v) for v in extras.values())
    print(f"units {len(units)}   pages {len(units)}   "
          f"files {covered} in units + {extra_files} in component tables = "
          f"{covered + extra_files} / {total_files}")
    if covered + extra_files != total_files:
        raise BookError("coverage invariant broken: some files map nowhere")

    dist = collections.Counter(u["tier"] for u in units)
    print("\ntier distribution")
    for tier in (1, 2, 3):
        n = dist[tier]
        print(f"  tier {tier}: {n:5d}  {n / len(units) * 100:5.1f}%")

    print("\nper component (units / tier1 / tier2 / tier3 / extra files)")
    per = collections.defaultdict(collections.Counter)
    for u in units:
        per[u["component"]]["units"] += 1
        per[u["component"]][f"t{u['tier']}"] += 1
    for comp in sorted(per, key=lambda c: -per[c]["units"]):
        c = per[comp]
        print(f"  {comp:<18} {c['units']:5d} {c['t1']:5d} {c['t2']:5d} {c['t3']:5d}"
              f" {len(extras.get(comp, [])):6d}")
    for comp in sorted(set(extras) - set(per)):
        print(f"  {comp:<18} {0:5d} {0:5d} {0:5d} {0:5d} {len(extras[comp]):6d}")

    if top:
        print(f"\ntop {top} units by score")
        for u in sorted(units, key=lambda u: -u["adjusted"])[:top]:
            s = u["signals"]
            print(f"  t{u['tier']} {u['adjusted']:6.2f} {u['id']:<52} "
                  f"fan-in {s.get('fan_in', 0):6d} from {s.get('fan_in_units', 0):4d} units, "
                  f"{s.get('lines', 0):5d} lines")


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BookError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
