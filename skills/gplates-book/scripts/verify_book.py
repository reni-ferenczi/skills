#!/usr/bin/env python3
"""Gate the book: prove coverage, links, structure and index completeness.

    python scripts/verify_book.py                  # full check, prose must be written
    python scripts/verify_book.py --allow-pending  # skeleton stage: placeholders are fine
    python scripts/verify_book.py -v               # list every failure, not just the first few

Exit code 0 only when every check passes.  Nothing here trusts the generators:
coverage is recomputed from the index, and links are resolved against the files
and headings that actually exist on disk.
"""

from __future__ import annotations

import argparse
import collections
import posixpath
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import gen_skeleton  # noqa: E402
from bookkit import (  # noqa: E402
    BOOK_DIR, BookError, DATA_DIR, INDEX_FILES, PENDING, PROSE_ANY_RE,
    component_page, index_for, load_json, load_manifest, open_index, slugify,
)

LINK_RE = re.compile(r"\[(?:[^\]\\]|\\.)*\]\(([^)\s]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*$")
CODE_FENCE_RE = re.compile(r"^\s*```")


class Report:
    def __init__(self, verbose: bool):
        self.verbose = verbose
        self.failures: dict[str, list[str]] = collections.defaultdict(list)

    def fail(self, check: str, detail: str) -> None:
        self.failures[check].append(detail)

    def summary(self) -> int:
        total = sum(len(v) for v in self.failures.values())
        for check, details in self.failures.items():
            shown = details if self.verbose else details[:8]
            print(f"FAIL {check}: {len(details)} problem(s)")
            for d in shown:
                print(f"       {d}")
            if len(details) > len(shown):
                print(f"       ... {len(details) - len(shown)} more (use -v)")
        print("verify: PASS" if not total else f"verify: FAIL ({total} problem(s))")
        return 1 if total else 0


def load_pages() -> dict[str, str]:
    return {p.relative_to(BOOK_DIR).as_posix(): p.read_text(encoding="utf-8")
            for p in BOOK_DIR.rglob("*.md")}


def anchors_in(text: str) -> set[str]:
    """Heading anchors a Markdown page offers, ignoring fenced code."""
    out, in_fence = set(), False
    for line in text.splitlines():
        if CODE_FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = HEADING_RE.match(line)
        if m:
            out.add(slugify(m.group(2).replace("`", "")))
    return out


CODE_SPAN_RE = re.compile(r"(`+)(?:(?!\1).)+\1")
FENCE_BLOCK_RE = re.compile(r"^```.*?^```", re.M | re.S)


def strip_code(text: str) -> str:
    """Blank out code so a C++ signature cannot look like a Markdown link.

    `operator[](rot_id_t)` is a valid code span, not a link; GFM agrees, and the
    link checker has to as well.  Link labels are themselves code spans, so the
    replacement keeps the brackets intact.
    """
    return CODE_SPAN_RE.sub("C", FENCE_BLOCK_RE.sub("", text))


def check_links(pages, report) -> None:
    anchors = {rel: anchors_in(text) for rel, text in pages.items()}
    for rel, text in sorted(pages.items()):
        base = Path(rel).parent
        for raw in LINK_RE.findall(strip_code(text)):
            if raw.startswith(("http://", "https://", "mailto:")):
                continue
            target, _, anchor = raw.partition("#")
            if not target:
                if anchor and anchor not in anchors[rel]:
                    report.fail("links", f"{rel}: local anchor #{anchor} does not exist")
                continue
            joined = target if base.as_posix() == "." else f"{base.as_posix()}/{target}"
            dest = posixpath.normpath(joined)
            if dest not in pages:
                report.fail("links", f"{rel}: broken link -> {raw}")
            elif anchor and anchor not in anchors[dest]:
                report.fail("links", f"{rel}: {dest} has no anchor #{anchor} ({raw})")


def check_coverage(db, units, extras, pages, report) -> None:
    """Every files row reaches the reader through exactly one page."""
    owner: dict[str, str] = {}
    for unit in units:
        for path in unit["files"] + unit["attached"]:
            if path in owner:
                report.fail("coverage", f"{path} claimed by {owner[path]} and {unit['id']}")
            owner[path] = unit["id"]
    for comp, rows in extras.items():
        for row in rows:
            if row["path"] in owner:
                report.fail("coverage",
                            f"{row['path']} is both a unit member and a {comp} table row")
            owner[row["path"]] = f"component:{comp}"

    indexed = {r["path"] for r in db.execute("SELECT path FROM files")}
    for path in sorted(indexed - set(owner)):
        report.fail("coverage", f"{path} maps to no page")
    for path in sorted(set(owner) - indexed):
        report.fail("coverage", f"{path} is documented but is not in the index")

    # The unit page must exist and be linked from its component page.
    for unit in units:
        if unit["page"] not in pages:
            report.fail("coverage", f"{unit['id']}: page {unit['page']} missing")
            continue
        comp_page = component_page(unit["component"])
        if comp_page not in pages:
            report.fail("coverage", f"{unit['id']}: component page {comp_page} missing")
        elif f"/{Path(unit['page']).name})" not in pages[comp_page]:
            report.fail("coverage",
                        f"{unit['id']}: not linked from {comp_page}")
        text = pages[unit["page"]]
        if "TOC.md)" not in text:
            report.fail("coverage", f"{unit['id']}: page does not link back to the TOC")
        if Path(comp_page).name + ")" not in text:
            report.fail("coverage", f"{unit['id']}: page does not link back to its component")

    # Table rows are the fallback route; the path must really be on the page.
    for comp, rows in extras.items():
        page = component_page(comp)
        text = pages.get(page, "")
        for row in rows:
            if row["path"] not in text:
                report.fail("coverage", f"{row['path']} not listed on {page}")


def check_indexes(db, pages, report) -> None:
    """Every definition appears in exactly one index, and only where it belongs."""
    expected: dict[str, set[str]] = collections.defaultdict(set)
    qname_of = {}
    for r in db.execute("SELECT e.id, e.qname, e.kind, e.is_def, p.kind AS pkind "
                        "FROM entities e LEFT JOIN entities p ON p.id = e.parent_id"):
        target = index_for(r["kind"], r["is_def"],
                           r["pkind"] is None or r["pkind"] == "namespace")
        if target:
            expected[target].add(str(r["id"]))
            qname_of[str(r["id"])] = r["qname"]

    anchors = load_json(DATA_DIR / "anchors.json", {})
    listed: dict[str, set[str]] = collections.defaultdict(set)
    for eid, rec in anchors.items():
        listed[rec["index"]].add(eid)

    seen_anywhere: dict[str, str] = {}
    for name in INDEX_FILES:
        page = f"indexes/{name}.md"
        if page not in pages:
            report.fail("indexes", f"{page} missing")
            continue
        missing = expected[name] - listed[name]
        extra = listed[name] - expected[name]
        for eid in sorted(missing)[:20]:
            report.fail("indexes", f"{name}: {qname_of.get(eid, eid)} is not indexed")
        for eid in sorted(extra)[:20]:
            report.fail("indexes", f"{name}: indexes {eid}, which does not belong there")
        for eid in listed[name]:
            if eid in seen_anywhere:
                report.fail("indexes",
                            f"{qname_of.get(eid, eid)} appears in both "
                            f"{seen_anywhere[eid]} and {name}")
            seen_anywhere[eid] = name

    # Each display row must actually be rendered on its page.
    for name in INDEX_FILES:
        page = f"indexes/{name}.md"
        rows = sum(1 for line in pages.get(page, "").splitlines()
                   if line.startswith("| [`"))
        want = len({(rec["qname"], rec["kind"], rec["unit"])
                    for rec in anchors.values() if rec["index"] == name})
        if rows != want:
            report.fail("indexes", f"{page}: {rows} rows rendered, {want} expected")


def check_markers(pages, allow_pending, report) -> None:
    for rel, text in sorted(pages.items()):
        for n, line in enumerate(text.splitlines(), 1):
            if PROSE_ANY_RE.search(line):
                if not allow_pending:
                    report.fail("markers", f"{rel}:{n}: unfilled prose block")
            elif PENDING in line and not allow_pending:
                report.fail("markers", f"{rel}:{n}: '(pending)' left in the book")


def check_collisions(pages, report) -> None:
    seen: dict[str, str] = {}
    for rel in pages:
        key = rel.lower()
        if key in seen:
            report.fail("collisions", f"{rel} and {seen[key]} differ only by case")
        seen[key] = rel


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--allow-pending", action="store_true",
                    help="accept prose placeholders (skeleton stage)")
    ap.add_argument("-v", "--verbose", action="store_true", help="list every problem")
    args = ap.parse_args()

    if not BOOK_DIR.exists():
        raise BookError(f"{BOOK_DIR} does not exist - run scripts/gen_skeleton.py")

    db = open_index()
    units = load_manifest()
    extras = load_json(DATA_DIR / "extras.json", {})
    pages = load_pages()
    report = Report(args.verbose)

    print(f"verify: {len(pages)} pages, {len(units)} units")
    check_coverage(db, units, extras, pages, report)
    check_links(pages, report)
    check_indexes(db, pages, report)
    check_markers(pages, args.allow_pending, report)
    check_collisions(pages, report)
    if gen_skeleton.lint() != 0:
        report.fail("lint", "gen_skeleton.py --lint reported problems (see above)")

    db.close()
    return report.summary()


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BookError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
