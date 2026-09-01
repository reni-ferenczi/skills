#!/usr/bin/env python3
"""Regenerate book/indexes/ from the code index and data/descriptions.jsonl.

Idempotent: run it after the skeleton, and again after every prose pass - the
one-liners the agents emit overwrite the Doxygen text the skeleton extracted, so
the indexes sharpen as the book fills in.

    python scripts/gen_indexes.py

Membership is decided by `bookkit.index_for`, the same function `verify_book.py`
uses to prove that every definition appears in exactly one index.
"""

from __future__ import annotations

import collections
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from bookkit import (  # noqa: E402
    BookError, DATA_DIR, INDEX_FILES, INDEX_TITLES, PENDING, component_page,
    load_descriptions, load_json, load_manifest, md_code, md_link, md_table,
    md_text, rel_link, write_page,
)

ANCHORS_PATH = DATA_DIR / "anchors.json"
# An include guard is a bodyless all-caps macro named after its own header.
GUARD_RE = re.compile(r"^[A-Z0-9_]+_(H|HH|H_|HPP|INL|CC)$")


def group_letter(name: str) -> str:
    bare = name.rsplit("::", 1)[-1].lstrip("_")
    first = bare[:1].upper()
    return first if first.isalpha() else "#"


def index_rows(anchors: dict, descriptions: dict) -> dict[str, list[dict]]:
    """Collapse entity records into display rows, one per (qname, kind, unit)."""
    merged: dict[tuple, dict] = {}
    for eid, rec in anchors.items():
        key = (rec["index"], rec["qname"], rec["kind"], rec["unit"])
        row = merged.get(key)
        if row is None:
            row = merged[key] = {"index": rec["index"], "qname": rec["qname"],
                                 "kind": rec["kind"], "unit": rec["unit"],
                                 "page": rec["page"], "anchor": rec["anchor"],
                                 "doc": rec["doc"], "ids": []}
        row["ids"].append(eid)
        if not row["doc"] and rec["doc"]:
            row["doc"] = rec["doc"]
        if not row["anchor"] and rec["anchor"]:
            row["anchor"] = rec["anchor"]

    out: dict[str, list[dict]] = collections.defaultdict(list)
    for row in merged.values():
        row["description"] = descriptions.get(row["qname"]) or row["doc"] or ""
        out[row["index"]].append(row)
    for rows in out.values():
        rows.sort(key=lambda r: (r["qname"].rsplit("::", 1)[-1].lower(), r["qname"].lower(),
                                 r["unit"]))
    return out


def render_index(name: str, rows: list[dict], page: str) -> list[str]:
    guards = []
    if name == "Macros":
        guards = [r for r in rows if GUARD_RE.match(r["qname"].rsplit("::", 1)[-1])]
        rows = [r for r in rows if r not in guards]

    out = [f"# {name}", "", md_link("Book TOC", page, "TOC.md"), "",
           f"Every in-tree definition of {INDEX_TITLES[name]}, from the "
           f"`gplates-code` index. {len(rows) + len(guards)} entries.", ""]
    if guards:
        out += [f"{len(guards)} of them are include guards, listed at the end.", ""]

    letters: dict[str, list[dict]] = collections.defaultdict(list)
    for row in rows:
        letters[group_letter(row["qname"])].append(row)
    if not letters:
        out += ["*None.*"]
    for letter in sorted(letters):
        out += [f"## {letter}", ""] + entry_table(letters[letter], page) + [""]

    if guards:
        out += ["## Include guards", "",
                "Header guards, one per header; they carry no meaning beyond "
                "protecting their own file.", ""]
        out += entry_table(guards, page, describe=False)
    return out


def entry_table(rows: list[dict], page: str, describe: bool = True) -> list[str]:
    headers = ["Name", "Unit"] + (["Description"] if describe else [])
    table = []
    for row in rows:
        link = f"[{md_code(row['qname'])}]({rel_link(page, row['page'], row['anchor'] or None)})"
        cells = [link, md_link(row["unit"], page, row["page"])]
        if describe:
            cells.append(md_text(row["description"]) if row["description"] else "")
        table.append(cells)
    return md_table(headers, table)


def render_components(units, extras, descriptions) -> list[str]:
    page = "indexes/Components.md"
    components = sorted({u["component"] for u in units} | set(extras))
    rows = []
    for comp in components:
        own = [u for u in units if u["component"] == comp]
        files = sum(len(u["files"]) + len(u["attached"]) for u in own) + \
            len(extras.get(comp, []))
        tiers = collections.Counter(u["tier"] for u in own)
        rows.append([
            md_link(comp, page, component_page(comp)), str(len(own)), str(files),
            f"{tiers[1]}/{tiers[2]}/{tiers[3]}",
            md_text(descriptions.get(f"component:{comp}", PENDING)),
        ])
    return ([f"# Components", "", md_link("Book TOC", page, "TOC.md"), "",
             f"{len(components)} components covering every file in the source tree. "
             f"The tier column counts units at tier 1 / 2 / 3.", ""]
            + md_table(["Component", "Units", "Files", "Tiers", "Responsibility"], rows))


def main() -> int:
    anchors = load_json(ANCHORS_PATH)
    if not anchors:
        raise BookError(f"{ANCHORS_PATH} not found - run scripts/gen_skeleton.py first")
    units = load_manifest()
    extras = load_json(DATA_DIR / "extras.json", {})
    descriptions = load_descriptions()

    write_page("indexes/Components.md", render_components(units, extras, descriptions))
    rows_by_index = index_rows(anchors, descriptions)
    for name in INDEX_FILES:
        rows = rows_by_index.get(name, [])
        page = f"indexes/{name}.md"
        write_page(page, render_index(name, rows, page))
        print(f"  {name + '.md':<16} {len(rows):5d} rows")
    print(f"wrote {len(INDEX_FILES) + 1} index pages")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BookError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
