#!/usr/bin/env python3
"""Shared helpers for the GPlates book generators.

Everything structural comes from the gplates-code index; nothing here re-parses
C++.  The module owns the three things the generators must agree on exactly:

* the **unit model** (which files form a documentation atom, what it is called,
  which page it lands on),
* the **Markdown emitters** (`md_code`, `md_link`, `md_table`, `slugify`) so a
  C++ signature can never corrupt a page, and
* the **prose block grammar** (`[[[PROSE ...]]] ... [[[/PROSE]]]`).

`verify_book.py` re-uses the same helpers, so a link the generator emits and a
link the verifier checks are slugified by one function, not two.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sqlite3
import sys
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):  # pragma: no cover - exotic stdio
        pass

SKILL_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = SKILL_DIR / "data"
BOOK_DIR = SKILL_DIR / "book"
CODE_SKILL_DIR = SKILL_DIR.parent / "gplates-code"
GPLATES_DB = CODE_SKILL_DIR / "data" / "gplates.db"
GRAPH_DB = CODE_SKILL_DIR / "data" / "graph.db"

MANIFEST_PATH = DATA_DIR / "manifest.jsonl"
PATH_MAP_PATH = DATA_DIR / "path_map.json"
DESCRIPTIONS_PATH = DATA_DIR / "descriptions.jsonl"
PROGRESS_PATH = DATA_DIR / "progress.json"
REFGRAPH_PATH = DATA_DIR / "refgraph.json"

PENDING = "(pending)"


class BookError(Exception):
    """Fatal, expected condition - reported without a traceback."""


# ---------------------------------------------------------------------------
# Databases
# ---------------------------------------------------------------------------

def open_index() -> sqlite3.Connection:
    if not GPLATES_DB.exists():
        raise BookError(
            f"no code index at {GPLATES_DB}\n"
            "run the gplates-code setup first: "
            "C:\\Python312\\python.exe scripts/setup_index.py --source <gplates src>")
    db = sqlite3.connect(f"file:{GPLATES_DB.as_posix()}?mode=ro", uri=True)
    db.row_factory = sqlite3.Row
    return db


def open_graph() -> sqlite3.Connection | None:
    """The Leiden community graph is optional; callers degrade gracefully."""
    if not GRAPH_DB.exists():
        return None
    if GRAPH_DB.stat().st_mtime < GPLATES_DB.stat().st_mtime:
        raise BookError(
            f"{GRAPH_DB.name} is older than {GPLATES_DB.name}; the graph stores paths and "
            "line numbers, so a stale graph mis-groups components.\n"
            "rebuild it: C:\\Python312\\python.exe scripts/build_graph.py")
    db = sqlite3.connect(f"file:{GRAPH_DB.as_posix()}?mode=ro", uri=True)
    db.row_factory = sqlite3.Row
    return db


def index_meta(db: sqlite3.Connection) -> dict:
    return {r["key"]: r["value"] for r in db.execute("SELECT key, value FROM meta")}


# ---------------------------------------------------------------------------
# Components
# ---------------------------------------------------------------------------

# Components outside src/<module>/, each with the paths it owns.  Kept explicit
# so that `verify_book.py` can prove every files row lands in exactly one.
SYNTHETIC_COMPONENTS = ("entry-points", "shaders", "sample-data", "python-examples", "build-and-docs")

# Tier bias per component (see Writer.md "Tiering").
COMPONENT_TIER_BIAS = {
    "model": 1, "app-logic": 1, "maths": 1, "scribe": 1, "opengl": 1, "global": 1,
    "qt-widgets": -1, "unit-test": -1, "cli": -1,
    "sample-data": -2, "build-and-docs": -2, "qt-resources": -1,
}


def component_of(path: str, category: str) -> str:
    """Map a `files.path` to its component.  Total function - never returns None."""
    if category == "shader":
        return "shaders"
    if path.startswith("src/"):
        rest = path[4:]
        if "/" in rest:
            return rest.split("/", 1)[0]
        return "entry-points"
    top = path.split("/", 1)[0] if "/" in path else ""
    if top == "sample-data":
        return "sample-data"
    if top == "scripts":
        return "python-examples"
    return "build-and-docs"


def component_page(component: str) -> str:
    return f"components/{component}.md"


# ---------------------------------------------------------------------------
# Index membership
# ---------------------------------------------------------------------------

# Which by-name index a definition belongs to.  One function, used by the
# skeleton (to record anchors), by gen_indexes.py (to fill the pages) and by
# verify_book.py (to prove the partition is exact), so the three cannot drift.
INDEX_FILES = ("Classes", "Structs", "Enums", "Typedefs", "Functions", "Macros")

INDEX_TITLES = {
    "Classes": "classes and unions",
    "Structs": "structs",
    "Enums": "enumerations",
    "Typedefs": "typedefs and type aliases",
    "Functions": "free functions at namespace scope",
    "Macros": "preprocessor macros",
}


def index_for(kind: str, is_def: int, at_namespace_scope: bool) -> str | None:
    if kind in ("macro", "macro_function"):
        return "Macros"
    if not is_def:
        return None
    if kind in ("class", "union"):
        return "Classes"
    if kind == "struct":
        return "Structs"
    if kind == "enum":
        return "Enums"
    if kind in ("typedef", "alias"):
        return "Typedefs"
    if kind == "function" and at_namespace_scope:
        return "Functions"
    return None


# ---------------------------------------------------------------------------
# Markdown emitters
# ---------------------------------------------------------------------------

_SLUG_DROP = re.compile(r"[^\w\- ]", re.UNICODE)


def slugify(heading: str) -> str:
    """GitHub-flavoured heading anchor.

    Lower-cases, drops everything that is not word/space/hyphen, then turns
    spaces into hyphens.  The one and only implementation - the generators emit
    links with it and `verify_book.py` resolves them with it.
    """
    s = heading.strip().lower()
    s = _SLUG_DROP.sub("", s)
    return s.replace(" ", "-")


def md_code(text, limit: int = 0) -> str:
    """Wrap an identifier, signature, type or path in a code span.

    Collapses newlines (C++ signatures in the index keep their comments), and
    widens the fence when the value itself contains a backtick, so `<T>`, `*`,
    `_`, `&` and `|` can never leak into the surrounding Markdown.  `limit`
    truncates runaway values - some indexed types carry a whole comment block.
    """
    s = " ".join(str(text).split())
    if not s:
        return ""
    if limit and len(s) > limit:
        s = s[:limit].rstrip() + " ..."
    if "`" in s:
        run = max(len(m) for m in re.findall(r"`+", s)) + 1
        fence = "`" * run
        pad = " " if s.startswith("`") or s.endswith("`") else ""
        return f"{fence}{pad}{s}{pad}{fence}"
    return f"`{s}`"


def md_text(text) -> str:
    """Plain prose for a table cell: collapse whitespace, neutralise Markdown."""
    s = " ".join(str(text).split())
    return re.sub(r"([\\`*_\[\]<>])", r"\\\1", s)


def md_cell(value) -> str:
    """Escape a finished cell so a pipe cannot break the table."""
    return str(value).replace("|", "\\|")


def md_table(headers, rows) -> list[str]:
    """Emit a GFM table, asserting arity so a short row fails at generation."""
    n = len(headers)
    out = ["| " + " | ".join(md_cell(h) for h in headers) + " |",
           "|" + "|".join("---" for _ in headers) + "|"]
    for i, row in enumerate(rows):
        if len(row) != n:
            raise BookError(f"table row {i} has {len(row)} cells, header has {n}: {row!r}")
        out.append("| " + " | ".join(md_cell(c) if c not in (None, "") else "—" for c in row) + " |")
    return out


def rel_link(from_page: str, to_page: str, anchor: str | None = None) -> str:
    """A book-relative URL from one page to another (both `book/`-relative)."""
    src = Path(from_page).parent.as_posix()
    rel = os.path.relpath(to_page, src if src != "." else ".").replace(os.sep, "/")
    if anchor:
        rel += "#" + anchor
    return rel


def md_link(label: str, from_page: str, to_page: str, anchor: str | None = None) -> str:
    return f"[{label}]({rel_link(from_page, to_page, anchor)})"


# ---------------------------------------------------------------------------
# Prose block grammar
# ---------------------------------------------------------------------------

PROSE_OPEN_RE = re.compile(r"^\[\[\[PROSE (?P<attrs>[^\]]*)\]\]\]\s*$")
PROSE_CLOSE = "[[[/PROSE]]]"
PROSE_ANY_RE = re.compile(r"\[\[\[/?PROSE")


def prose_block(slot: str, unit: str, tier: int, instruction: str) -> list[str]:
    """One placeholder block; the agent replaces it whole, markers included."""
    return [f"[[[PROSE {slot} unit={unit} tier={tier}]]]", instruction, PROSE_CLOSE]


def find_prose_blocks(text: str) -> list[dict]:
    """Parse every well-formed block out of a page; used by lint and the verifier."""
    blocks, lines, i = [], text.splitlines(), 0
    while i < len(lines):
        m = PROSE_OPEN_RE.match(lines[i])
        if m:
            attrs = dict(part.split("=", 1) for part in m.group("attrs").split()[1:]
                         if "=" in part)
            attrs["slot"] = m.group("attrs").split()[0]
            for j in range(i + 1, len(lines)):
                if lines[j].strip() == PROSE_CLOSE:
                    attrs["start"], attrs["end"] = i, j
                    blocks.append(attrs)
                    i = j
                    break
            else:
                raise BookError(f"unterminated prose block at line {i + 1}")
        i += 1
    return blocks


# ---------------------------------------------------------------------------
# Working files
# ---------------------------------------------------------------------------

def load_manifest(path: Path = MANIFEST_PATH) -> list[dict]:
    if not path.exists():
        raise BookError(f"{path} not found - run scripts/build_manifest.py first")
    with path.open(encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def save_manifest(units: list[dict], path: Path = MANIFEST_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as fh:
        for unit in units:
            fh.write(json.dumps(unit, sort_keys=True) + "\n")


def load_json(path: Path, default=None):
    if not path.exists():
        return default
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def save_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as fh:
        json.dump(obj, fh, indent=1, sort_keys=True)
        fh.write("\n")


def load_descriptions() -> dict[str, str]:
    """qname -> one-liner; later lines win, so a prose pass overrides Doxygen."""
    out: dict[str, str] = {}
    if not DESCRIPTIONS_PATH.exists():
        return out
    with DESCRIPTIONS_PATH.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            if rec.get("qname") and rec.get("oneliner"):
                out[rec["qname"]] = " ".join(str(rec["oneliner"]).split())
    return out


def write_page(rel_path: str, lines: list[str]) -> None:
    dest = BOOK_DIR / rel_path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")


def read_page(rel_path: str) -> str:
    return (BOOK_DIR / rel_path).read_text(encoding="utf-8")


def sha256_lf(source_root: Path, rel_path: str, fallback: str | None = None) -> str:
    """Hash a member file with CRLF normalised away, so the key is OS-stable."""
    full = source_root / rel_path
    try:
        data = full.read_bytes()
    except OSError:
        if fallback is None:
            return ""
        data = fallback.encode("utf-8", "replace")
    return hashlib.sha256(data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")).hexdigest()


def die(msg: str) -> None:
    print(f"error: {msg}", file=sys.stderr)
    raise SystemExit(2)
