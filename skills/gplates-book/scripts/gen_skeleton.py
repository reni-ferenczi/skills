#!/usr/bin/env python3
"""Emit every book page with its structural content filled in programmatically.

Prose is left as `[[[PROSE ...]]] ... [[[/PROSE]]]` placeholders; everything
else - tables, links, breadcrumbs, gpq recipes - is derived from the
gplates-code index and costs no tokens.

    python scripts/gen_skeleton.py                # unit + component pages + TOC
    python scripts/gen_skeleton.py --only-changed # skip units whose hash is unchanged
    python scripts/gen_skeleton.py --lint         # re-parse book/ and check structure

Regeneration never destroys prose: a section that no longer holds a placeholder
is carried over from the page on disk.
"""

from __future__ import annotations

import argparse
import collections
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from bookkit import (  # noqa: E402
    BOOK_DIR, BookError, DATA_DIR, PATH_MAP_PATH, PROSE_ANY_RE, PENDING,
    REFGRAPH_PATH, component_page, find_prose_blocks, index_meta, load_json,
    index_for, load_manifest, md_code, md_link, md_table, md_text, open_index,
    prose_block, rel_link, save_json, slugify, write_page,
)

ANCHORS_PATH = DATA_DIR / "anchors.json"

UNIT_HEADINGS = ("Overview", "Declared types", "Members", "Free functions and macros",
                 "Notes", "Used by", "Related", "Explore")
COMPONENT_HEADINGS = ("Overview", "Units", "Other files", "Depends on", "Used by", "Explore")
TOC_HEADINGS = ("Overview", "How to read this book", "Components", "Indexes", "Index facts")

NONE = "*None.*"
MAX_USED_BY = 20
MAX_RELATED_ROWS = 15
# Above this many units a component page is grouped into sections instead of
# being one unnavigable wall of links.
GROUPED_COMPONENT_UNITS = 60

TYPE_KINDS = ("class", "struct", "union", "enum", "typedef", "alias")
MEMBER_KINDS = ("constructor", "destructor", "method", "operator", "field", "variable",
                "typedef", "alias", "enum", "enumerator", "class", "struct", "union")
FREE_KINDS = ("function", "operator", "variable", "macro", "macro_function")

CATEGORY_LABEL = {
    "cpp": "C++", "python": "Python", "ui": "Qt form", "shader": "GLSL",
    "gpgim": "GPGIM", "resource": "resource", "build": "build", "doc": "doc",
    "data": "data", "other": "other",
}

# Component pages start from a fixed one-line role so the skeleton is readable
# before any prose exists; the synthesis pass replaces the page prose, not this.
COMPONENT_ROLE = {
    "entry-points": "The main() entry points and the Scribe export registration units.",
    "shaders": "GLSL shader programs compiled into the Qt resource bundle.",
    "sample-data": "Example data files shipped with GPlates.",
    "python-examples": "Stand-alone pyGPlates demo and utility scripts.",
    "build-and-docs": "CMake build system, packaging and repository documentation.",
}


# ---------------------------------------------------------------------------
# Doxygen / comment extraction
# ---------------------------------------------------------------------------

_COMMENT_RE = re.compile(r"^\s*(///|//!|//|/\*+|\*+/|\*)")
_STRIP_RE = re.compile(r"^\s*(/\*+<?|\*+/|///+<?|//!<?|//|\*+)\s?")
_CMD_RE = re.compile(r"[@\\](brief|short|details?|param\b.*|return[s]?|file|ingroup|"
                     r"class|struct|enum|fn|def|note|sa|see|since|todo|throws?)\s*", re.I)
_INLINE_CMD_RE = re.compile(r"[@\\](a|b|c|e|em|p|ref|link|endlink)\s+")
_NOISE_RE = re.compile(r"^[\s*=\-_~#]*$")
_LICENSE_RE = re.compile(r"copyright|general public license|\$revision|\$date|\$id",
                         re.I)


def doc_above(file_lines: dict[int, str], line: int, reach: int = 40) -> str:
    """The comment block immediately above `line`, cleaned to one sentence."""
    idx = line - 1
    blanks = 0
    while idx >= 1:
        text = file_lines.get(idx, "")
        if not text.strip():
            blanks += 1
            if blanks > 1:
                return ""
            idx -= 1
            continue
        if re.match(r"^\s*template\s*<", text) or text.strip() in ("{", "public:", "private:"):
            idx -= 1
            continue
        break
    end = idx
    if end < 1 or not _COMMENT_RE.match(file_lines.get(end, "")):
        return ""
    start = end
    while start > 1 and start > end - reach and _COMMENT_RE.match(file_lines.get(start - 1, "")):
        start -= 1
    raw = [file_lines.get(i, "") for i in range(start, end + 1)]
    if any(_LICENSE_RE.search(r) for r in raw):
        return ""
    cleaned = []
    for r in raw:
        r = _STRIP_RE.sub("", r).strip()
        r = _INLINE_CMD_RE.sub("", _CMD_RE.sub("", r))
        if r and not _NOISE_RE.match(r):
            cleaned.append(r)
    return first_sentence(" ".join(cleaned))


def first_sentence(text: str, limit: int = 240) -> str:
    text = " ".join(text.split())
    if not text:
        return ""
    m = re.search(r"(?<=[.!?])\s+(?=[A-Z(`])", text)
    if m and m.start() < limit:
        text = text[: m.start()]
    if len(text) > limit:
        text = text[:limit].rsplit(" ", 1)[0] + " ..."
    return text


# ---------------------------------------------------------------------------
# Context loaded once, shared by every page
# ---------------------------------------------------------------------------

class Context:
    def __init__(self):
        self.db = open_index()
        self.meta = index_meta(self.db)
        self.units = load_manifest()
        self.by_id = {u["id"]: u for u in self.units}
        self.path_map = load_json(PATH_MAP_PATH, {})
        self.extras = load_json(DATA_DIR / "extras.json", {})
        self.refs = load_json(REFGRAPH_PATH, {})
        self.unit_of_file = {p: u["id"] for u in self.units
                             for p in u["files"] + u["attached"]}
        self.file_row = {r["path"]: dict(r) for r in
                         self.db.execute("SELECT id, path, category, lines FROM files")}
        self.fid_of_path = {p: r["id"] for p, r in self.file_row.items()}
        self.unit_of_fid = {self.fid_of_path[p]: uid for p, uid in self.unit_of_file.items()}

        self.rev_refs: dict[str, dict[str, int]] = collections.defaultdict(dict)
        for src, dsts in self.refs.items():
            for dst, weight in dsts.items():
                self.rev_refs[dst][src] = weight

        self.components = sorted({u["component"] for u in self.units} | set(self.extras))
        self.units_by_component = collections.defaultdict(list)
        for u in self.units:
            self.units_by_component[u["component"]].append(u)

        self.anchors: dict[str, dict] = {}
        self._load_relations()

    def _load_relations(self):
        db = self.db
        self.ui_forms = collections.defaultdict(list)
        for r in db.execute("SELECT file_id, class_name, base_class, title FROM ui_forms"):
            self.ui_forms[r["file_id"]].append(dict(r))
        self.ui_widget_count = collections.Counter()
        for r in db.execute("SELECT file_id, COUNT(*) n FROM ui_widgets GROUP BY file_id"):
            self.ui_widget_count[r["file_id"]] = r["n"]
        self.connections = collections.defaultdict(list)
        for r in db.execute("SELECT file_id, line, sender, signal, receiver, slot "
                            "FROM qt_connections ORDER BY file_id, line"):
            self.connections[r["file_id"]].append(dict(r))
        self.pyapi = collections.defaultdict(list)
        for r in db.execute("SELECT file_id, line, owner, name, kind, cpp_type "
                            "FROM py_api ORDER BY file_id, line"):
            self.pyapi[r["file_id"]].append(dict(r))

        # Qt resource paths (":/opengl/<dir>/<name>.glsl") tie a GL unit to the
        # shader directory it compiles.
        self.shader_users = collections.defaultdict(set)
        self.unit_shaders = collections.defaultdict(set)
        shader_by_res = {}
        for path in self.file_row:
            if self.file_row[path]["category"] == "shader":
                shader_by_res[path.replace("src/qt-resources/", ":/")] = path
        for r in db.execute("SELECT file_id, text FROM lines WHERE text LIKE '%.glsl%'"):
            uid = self.unit_of_fid.get(r["file_id"])
            if not uid:
                continue
            for res, path in shader_by_res.items():
                if res in r["text"]:
                    shader_unit = self.unit_of_file.get(path)
                    if shader_unit and shader_unit != uid:
                        self.shader_users[shader_unit].add(uid)
                        self.unit_shaders[uid].add(shader_unit)

    # -- per-unit lookups ---------------------------------------------------

    def entities_of(self, unit) -> list[dict]:
        fids = [self.fid_of_path[p] for p in unit["files"] if p in self.fid_of_path]
        if not fids:
            return []
        marks = ",".join("?" * len(fids))
        return [dict(r) for r in self.db.execute(
            f"SELECT * FROM entities WHERE file_id IN ({marks}) ORDER BY file_id, line", fids)]

    def lines_of(self, path: str) -> dict[int, str]:
        fid = self.fid_of_path.get(path)
        if fid is None:
            return {}
        return {r["line"]: r["text"] for r in self.db.execute(
            "SELECT line, text FROM lines WHERE file_id = ?", (fid,))}

    def bases_of(self, entity_ids) -> dict[int, list[dict]]:
        if not entity_ids:
            return {}
        out = collections.defaultdict(list)
        marks = ",".join("?" * len(entity_ids))
        for r in self.db.execute(
                f"SELECT b.entity_id, b.base_name, b.base_entity_id, b.access, b.is_virtual, "
                f"e.file_id AS base_file "
                f"FROM bases b LEFT JOIN entities e ON e.id = b.base_entity_id "
                f"WHERE b.entity_id IN ({marks})", list(entity_ids)):
            out[r["entity_id"]].append(dict(r))
        return out

    def subclass_count(self, entity_ids) -> dict[int, int]:
        if not entity_ids:
            return {}
        marks = ",".join("?" * len(entity_ids))
        return {r["ancestor_id"]: r["n"] for r in self.db.execute(
            f"SELECT ancestor_id, COUNT(*) n FROM inherit_closure "
            f"WHERE ancestor_id IN ({marks}) GROUP BY ancestor_id", list(entity_ids))}


# ---------------------------------------------------------------------------
# Prose preservation
# ---------------------------------------------------------------------------

def existing_sections(rel_path: str) -> dict[str, list[str]]:
    """Split a page on disk into `## Heading` -> body lines."""
    page = BOOK_DIR / rel_path
    if not page.exists():
        return {}
    sections, current = {}, None
    for line in page.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            sections[current] = []
        elif current is not None:
            sections[current].append(line)
    return {k: v for k, v in sections.items()}


def keep_or_placeholder(previous: dict[str, list[str]], heading: str,
                        slot: str, unit_id: str, tier: int, instruction: str) -> list[str]:
    """Reuse prose already written for this section, else emit the placeholder."""
    body = previous.get(heading)
    if body is not None:
        text = "\n".join(body).strip()
        if text and not PROSE_ANY_RE.search(text) and PENDING not in text:
            return text.splitlines()
    return prose_block(slot, unit_id, tier, instruction)


# ---------------------------------------------------------------------------
# Unit page
# ---------------------------------------------------------------------------

OVERVIEW_HINT = ("Replace this whole block, markers included, with 1-3 paragraphs: what this "
                 "unit is, why it exists, and how it fits the surrounding design. Do not "
                 "restate the tables below.")
NOTES_HINT = ("Replace this whole block, markers included, with invariants, ownership, "
              "threading or gotchas that are not visible in the tables. Write "
              "*None.* if there is nothing worth saying.")


def heading_anchor(text: str) -> str:
    """Anchor of a `### `-rendered heading, computed from what is written out.

    The heading is emitted as ``### {md_code(text)}``, so the anchor has to be
    derived from that exact string - md_code collapses the whitespace that
    template specialisations carry in their qualified names.
    """
    return slugify(md_code(text).replace("`", ""))


def unique_heading(text: str, seen: set[str]) -> str:
    candidate, n = text, 1
    while heading_anchor(candidate) in seen:
        n += 1
        candidate = f"{text} ({n})"
    seen.add(heading_anchor(candidate))
    return candidate


def dedupe(entities: list[dict]) -> list[dict]:
    """One row per (name, kind, signature); a definition beats a declaration."""
    best: dict[tuple, dict] = {}
    for e in entities:
        key = (e["qname"], e["kind"], " ".join((e["signature"] or "").split()))
        prev = best.get(key)
        if prev is None or (e["is_def"] and not prev["is_def"]):
            best[key] = e
    return sorted(best.values(), key=lambda e: (e["file_id"], e["line"]))


def render_unit_page(ctx: Context, unit: dict) -> list[str]:
    page = unit["page"]
    previous = existing_sections(page)
    entities = ctx.entities_of(unit)
    by_eid = {e["id"]: e for e in entities}
    children = collections.defaultdict(list)
    for e in entities:
        children[e["parent_id"]].append(e)

    docs: dict[int, str] = {}
    for path in unit["files"]:
        file_lines = ctx.lines_of(path)
        fid = ctx.fid_of_path.get(path)
        for e in entities:
            if e["file_id"] == fid and e["kind"] not in ("parameter", "local"):
                text = doc_above(file_lines, e["line"])
                if text and not docs.get(e["id"]):
                    docs[e["id"]] = text

    def namespace_scope(e):
        parent = by_eid.get(e["parent_id"])
        return parent is None or parent["kind"] == "namespace"

    def enclosing_type(e, outermost=False):
        """The type that contains `e`, or the outermost one when asked."""
        found, node = None, by_eid.get(e["parent_id"])
        while node is not None:
            if node["kind"] in TYPE_KINDS:
                found = node
                if not outermost:
                    return found
            node = by_eid.get(node["parent_id"])
        return found

    # A type gets its own section unless another type already contains it, so
    # every type definition on this page is reachable by an anchor.
    types = dedupe([e for e in entities
                    if e["kind"] in TYPE_KINDS and e["is_def"] and enclosing_type(e) is None])
    frees = dedupe([e for e in entities
                    if e["kind"] in FREE_KINDS
                    and (e["kind"] in ("macro", "macro_function") or namespace_scope(e))])
    bases = ctx.bases_of([e["id"] for e in types])
    subs = ctx.subclass_count([e["id"] for e in types])

    out: list[str] = []
    out.append(f"# {unit['name']}")
    out.append("")
    out.append(breadcrumb(page, unit))
    out.append("")
    out += source_table(ctx, unit)
    out.append("")

    out.append("## Overview")
    out.append("")
    out += keep_or_placeholder(previous, "Overview", "overview", unit["id"], unit["tier"],
                               OVERVIEW_HINT)
    out.append("")

    out.append("## Declared types")
    out.append("")
    seen_anchors: set[str] = set()
    headings: dict[int, str] = {}
    if types:
        rows = []
        for e in types:
            heading = unique_heading(e["qname"], seen_anchors)
            headings[e["id"]] = heading
            rows.append([
                f"[{md_code(e['qname'])}](#{heading_anchor(heading)})",
                e["kind"],
                base_cells(ctx, page, bases.get(e["id"], [])),
                md_code(e["template_params"]) if e["is_template"] else "",
                str(subs.get(e["id"], 0)),
                md_text(docs.get(e["id"], "")),
            ])
        out += md_table(["Name", "Kind", "Bases", "Template", "Subclasses", "Description"], rows)
    else:
        out.append(NONE)
    out.append("")

    out.append("## Members")
    out.append("")
    if types:
        for e in types:
            out.append(f"### {md_code(headings[e['id']])}")
            out.append("")
            out += member_table(ctx, e, children, docs)
            out.append("")
    else:
        out.append(NONE)
        out.append("")

    out.append("## Free functions and macros")
    out.append("")
    out += free_table(ctx, frees, docs)
    out.append("")

    out.append("## Notes")
    out.append("")
    out += keep_or_placeholder(previous, "Notes", "notes", unit["id"], unit["tier"], NOTES_HINT)
    out.append("")

    out.append("## Used by")
    out.append("")
    out += used_by_table(ctx, unit)
    out.append("")

    out.append("## Related")
    out.append("")
    out += related_section(ctx, unit)
    out.append("")

    out.append("## Explore")
    out.append("")
    out += explore_block(ctx, unit, types)

    record_anchors(ctx, unit, entities, by_eid, types, headings, docs,
                   namespace_scope, enclosing_type)
    return out


def record_anchors(ctx, unit, entities, by_eid, types, headings, docs,
                   namespace_scope, enclosing_type) -> None:
    """Remember where each indexable definition landed, for `gen_indexes.py`.

    The skeleton is the only place that knows the final heading text (duplicate
    qnames get a numeric suffix), so it is the only place that may mint anchors.
    """
    own = {e["qname"]: heading_anchor(headings[e["id"]]) for e in types}
    for e in entities:
        target = index_for(e["kind"], e["is_def"], namespace_scope(e))
        if target is None:
            continue
        anchor = own.get(e["qname"])
        if anchor is None:
            owner = enclosing_type(e, outermost=True)
            anchor = own.get(owner["qname"]) if owner else None
        if anchor is None and e["kind"] in FREE_KINDS:
            anchor = slugify("Free functions and macros")
        ctx.anchors[str(e["id"])] = {
            "unit": unit["id"], "page": unit["page"], "anchor": anchor or "",
            "qname": e["qname"], "kind": e["kind"], "index": target,
            "doc": docs.get(e["id"], ""),
        }


def breadcrumb(page: str, unit: dict) -> str:
    parts = [md_link("Book TOC", page, "TOC.md"),
             md_link(unit["component"], page, component_page(unit["component"]))]
    if unit.get("community_name"):
        parts.append(f"cluster {unit['community_name']}")
    parts.append(f"tier {unit['tier']}")
    if unit["deprecated"]:
        parts.append("**deprecated**")
    return " · ".join(parts)


def source_table(ctx: Context, unit: dict) -> list[str]:
    rows = []
    for path in unit["files"] + unit["attached"]:
        row = ctx.file_row.get(path, {})
        rows.append([md_code(path), CATEGORY_LABEL.get(row.get("category"), "?"),
                     str(row.get("lines", 0))])
    return md_table(["Source file", "Kind", "Lines"], rows)


def base_cells(ctx: Context, page: str, base_rows: list[dict]) -> str:
    cells = []
    for b in base_rows:
        label = md_code(b["base_name"])
        target = ctx.unit_of_fid.get(b["base_file"]) if b["base_file"] else None
        if target and target in ctx.path_map:
            label = f"[{label}]({rel_link(page, ctx.path_map[target])})"
        if b["is_virtual"]:
            label += " *(virtual)*"
        cells.append(label)
    return "<br>".join(cells)


def member_table(ctx: Context, owner: dict, children, docs) -> list[str]:
    members = dedupe([e for e in children.get(owner["id"], []) if e["kind"] in MEMBER_KINDS])
    if not members:
        return [NONE]
    rows = []
    for e in members:
        name = e["name"] + (e["signature"] or "") if e["kind"] in (
            "method", "constructor", "destructor", "operator", "function") else e["name"]
        rows.append([md_code(name, 320), e["kind"], md_code(e["type_text"], 180),
                     e["access"] or "", md_text(docs.get(e["id"], ""))])
    return md_table(["Member", "Kind", "Type", "Access", "Description"], rows)


def free_table(ctx: Context, frees: list[dict], docs) -> list[str]:
    if not frees:
        return [NONE]
    rows = []
    for e in frees:
        name = e["name"] + (e["signature"] or "") if e["kind"] in ("function", "operator") else e["name"]
        rows.append([md_code(name, 320), e["kind"], md_code(e["type_text"], 180),
                     md_text(docs.get(e["id"], ""))])
    return md_table(["Name", "Kind", "Type / body", "Description"], rows)


def used_by_table(ctx: Context, unit: dict) -> list[str]:
    dependents = sorted(ctx.rev_refs.get(unit["id"], {}).items(),
                        key=lambda kv: (-kv[1], kv[0]))
    if not dependents:
        return ["*Nothing in the tree references this unit.*"]
    rows = []
    for uid, weight in dependents[:MAX_USED_BY]:
        other = ctx.by_id.get(uid)
        if not other:
            continue
        rows.append([md_link(uid, unit["page"], other["page"]), other["component"], str(weight)])
    lines = md_table(["Unit", "Component", "References"], rows)
    if len(dependents) > MAX_USED_BY:
        lines += ["", f"*... and {len(dependents) - MAX_USED_BY} more units.*"]
    return lines


def related_section(ctx: Context, unit: dict) -> list[str]:
    out: list[str] = []
    fids = [ctx.fid_of_path[p] for p in unit["files"] + unit["attached"]
            if p in ctx.fid_of_path]

    forms = [(f, form) for f in fids for form in ctx.ui_forms.get(f, [])]
    if forms:
        out.append("**Qt Designer forms**")
        out.append("")
        out += md_table(["Form class", "Base widget", "Title", "Widgets"],
                        [[md_code(form["class_name"]), md_code(form["base_class"] or ""),
                          md_text(form["title"] or ""), str(ctx.ui_widget_count[fid])]
                         for fid, form in forms])
        out.append("")

    shaders = sorted(ctx.unit_shaders.get(unit["id"], set()))
    if shaders:
        out.append("**Shader programs compiled by this unit**")
        out.append("")
        out += md_table(["Shader unit", "Component"],
                        [[md_link(s, unit["page"], ctx.by_id[s]["page"]),
                          ctx.by_id[s]["component"]] for s in shaders])
        out.append("")

    users = sorted(ctx.shader_users.get(unit["id"], set()))
    if users:
        out.append("**Compiled by**")
        out.append("")
        out += md_table(["Unit", "Component"],
                        [[md_link(u, unit["page"], ctx.by_id[u]["page"]),
                          ctx.by_id[u]["component"]] for u in users])
        out.append("")

    conns = [c for f in fids for c in ctx.connections.get(f, [])]
    if conns:
        out.append(f"**Qt signal/slot connections** ({len(conns)} in this unit)")
        out.append("")
        out += md_table(["Sender", "Signal", "Receiver", "Slot"],
                        [[md_code(c["sender"]), md_code(c["signal"]),
                          md_code(c["receiver"]), md_code(c["slot"])]
                         for c in conns[:MAX_RELATED_ROWS]])
        if len(conns) > MAX_RELATED_ROWS:
            out += ["", f"*... and {len(conns) - MAX_RELATED_ROWS} more connections.*"]
        out.append("")

    api = [a for f in fids for a in ctx.pyapi.get(f, [])]
    if api:
        out.append("**Python bindings**")
        out.append("")
        out += md_table(["Python name", "Kind", "Owner", "C++"],
                        [[md_code(a["name"]), a["kind"], md_code(a["owner"] or ""),
                          md_code(a["cpp_type"] or "")] for a in api[:MAX_RELATED_ROWS]])
        if len(api) > MAX_RELATED_ROWS:
            out += ["", f"*... and {len(api) - MAX_RELATED_ROWS} more bindings.*"]
        out.append("")

    if unit["kind"] == "gpgim":
        out += gpgim_tables(ctx)

    return out or [NONE]


def gpgim_tables(ctx: Context) -> list[str]:
    features = [dict(r) for r in ctx.db.execute(
        "SELECT name, class_type, inherits, default_geometry, description "
        "FROM gpgim_features ORDER BY name")]
    props = [dict(r) for r in ctx.db.execute(
        "SELECT name, types, multiplicity, description FROM gpgim_properties ORDER BY name")]
    out = ["**GPGIM feature types**", ""]
    out += md_table(["Feature", "Class", "Inherits", "Default geometry", "Description"],
                    [[md_code(f["name"]), f["class_type"] or "", md_code(f["inherits"] or ""),
                      md_code(f["default_geometry"] or ""), md_text(f["description"] or "")]
                     for f in features])
    out += ["", "**GPGIM property types**", ""]
    out += md_table(["Property", "Value types", "Multiplicity", "Description"],
                    [[md_code(p["name"]), md_code(p["types"] or ""), p["multiplicity"] or "",
                      md_text(p["description"] or "")] for p in props])
    out.append("")
    return out


def explore_block(ctx: Context, unit: dict, types: list[dict]) -> list[str]:
    """Concrete gpq commands, run from the gplates-code skill directory."""
    cmds = [f"python scripts/gpq.py file {unit['files'][0]}"] if unit["files"] else []
    if types:
        primary = max(types, key=lambda e: (e["end_line"] or 0) - e["line"])
        cmds.append(f"python scripts/gpq.py def {primary['qname']} --body")
        cmds.append(f"python scripts/gpq.py uses {primary['name']} --kind {primary['kind']}")
        if primary["kind"] in ("class", "struct"):
            cmds.append(f"python scripts/gpq.py hier {primary['name']}")
    elif unit["kind"] == "shader":
        cmds.append(f"python scripts/gpq.py grep uniform --category shader "
                    f"--path {unit['dir']}")
    elif unit["kind"] == "gpgim":
        cmds.append("python scripts/gpq.py gpgim Isochron")
    return (["Run these from the `gplates-code` skill directory:", "", "```bash"]
            + cmds + ["```"])


# ---------------------------------------------------------------------------
# Component pages and TOC
# ---------------------------------------------------------------------------

COMPONENT_HINT = ("Replace this whole block, markers included, with 2-4 paragraphs: what this "
                  "component is responsible for, the load-bearing units and how it connects to "
                  "neighbouring components. Do not restate the unit table.")
TOC_HINT = ("Replace this whole block, markers included, with the project overview: what GPlates "
            "is, and the path a change takes through model -> app-logic -> presentation -> "
            "view-operations/gui -> opengl. Aim for 4-8 paragraphs.")


def render_component_page(ctx: Context, component: str) -> list[str]:
    page = component_page(component)
    previous = existing_sections(page)
    units = sorted(ctx.units_by_component.get(component, []), key=lambda u: u["id"])
    descriptions = ctx.descriptions

    out = [f"# {component}", "", md_link("Book TOC", page, "TOC.md")]
    role = COMPONENT_ROLE.get(component)
    if role:
        out += ["", role]
    out += ["", f"{len(units)} unit page(s), "
                f"{sum(len(u['files']) + len(u['attached']) for u in units)} source file(s) "
                f"documented here, "
                f"{len(ctx.extras.get(component, []))} further file(s) listed below.", ""]

    out += ["## Overview", ""]
    out += keep_or_placeholder(previous, "Overview", "component", f"component:{component}", 1,
                               COMPONENT_HINT)
    out += ["", "## Units", ""]
    if units:
        out += component_unit_sections(ctx, page, units, descriptions)
    else:
        out.append(NONE)

    out += ["", "## Other files", ""]
    extras = ctx.extras.get(component, [])
    if extras:
        out += md_table(["File", "Kind", "Lines"],
                        [[md_code(x["path"]), CATEGORY_LABEL.get(x["category"], "?"),
                          str(x["lines"])] for x in sorted(extras, key=lambda x: x["path"])])
    else:
        out.append(NONE)

    depends, used = component_edges(ctx, component)
    out += ["", "## Depends on", ""]
    out += (md_table(["Component", "References"], [[md_link(c, page, component_page(c)), str(n)]
                                                   for c, n in depends]) if depends else [NONE])
    out += ["", "## Used by", ""]
    out += (md_table(["Component", "References"], [[md_link(c, page, component_page(c)), str(n)]
                                                   for c, n in used]) if used else [NONE])

    out += ["", "## Explore", "", "Run these from the `gplates-code` skill directory:", "",
            "```bash"]
    sample_dir = units[0]["dir"] if units else (extras[0]["path"].rsplit("/", 1)[0]
                                               if extras else "src")
    out += [f"python scripts/gpq.py tree {sample_dir}",
            f"python scripts/gpq.py sym . --mode sub --path {sample_dir} --defs-only",
            "```"]
    return out


_PREFIX_RE = re.compile(r"^(GL|GPlates|Gpml|Gpgim|Py|Qt)?([A-Z][a-z0-9]*|[A-Z]+)")


def name_prefix(name: str) -> str:
    """First CamelCase word, keeping the well-known GPlates prefixes attached."""
    m = _PREFIX_RE.match(name)
    return (m.group(1) or "") + m.group(2) if m else name[:1].upper() or "Other"


def unit_groups(units: list[dict]) -> list[tuple[str, list[dict]]]:
    """Split a long unit list into readable sections.

    Leiden communities are preferred when they are coarse enough to be useful;
    on this tree they are not (about one community per unit), so the name-prefix
    fallback normally wins.  Groups smaller than three collapse into `Other`.
    """
    communities = collections.Counter(u.get("community_name") for u in units
                                      if u.get("community_name"))
    if communities and len(units) / len(communities) >= 3:
        key = lambda u: u.get("community_name") or "Ungrouped"  # noqa: E731
    else:
        key = lambda u: name_prefix(u["name"])  # noqa: E731

    buckets: dict[str, list[dict]] = collections.defaultdict(list)
    for u in units:
        buckets[key(u)].append(u)
    small = [u for label, group in buckets.items() if len(group) < 3 for u in group]
    sections = [(label, group) for label, group in buckets.items() if len(group) >= 3]
    sections.sort(key=lambda kv: kv[0].lower())
    if small:
        sections.append(("Other", small))
    return sections


def component_unit_sections(ctx: Context, page: str, units, descriptions) -> list[str]:
    header = ["Unit", "Tier", "Lines", "Fan-in", "Description"]

    def row(u):
        return [md_link(u["name"], page, u["page"]), str(u["tier"]),
                str(u["signals"].get("lines", 0)), str(u["signals"].get("fan_in", 0)),
                md_text(descriptions.get(f"unit:{u['id']}", PENDING))]

    def table(group):
        return md_table(header, [row(u) for u in sorted(group, key=lambda u: u["id"])])

    dirs = sorted({u["dir"] for u in units})
    if len(dirs) == 1 and len(units) <= GROUPED_COMPONENT_UNITS:
        return table(units)

    out: list[str] = []
    for directory in dirs:
        in_dir = [u for u in units if u["dir"] == directory]
        level = "###"
        if len(dirs) > 1:
            out += [f"### {md_code(directory)}", ""]
            level = "####"
        if len(in_dir) <= GROUPED_COMPONENT_UNITS:
            out += table(in_dir) + [""]
            continue
        for label, group in unit_groups(in_dir):
            out += [f"{level} {label}", ""] + table(group) + [""]
    return out


def component_edges(ctx: Context, component: str):
    out_edges, in_edges = collections.Counter(), collections.Counter()
    for src, dsts in ctx.refs.items():
        src_comp = ctx.by_id[src]["component"] if src in ctx.by_id else None
        for dst, weight in dsts.items():
            dst_comp = ctx.by_id[dst]["component"] if dst in ctx.by_id else None
            if src_comp == component and dst_comp and dst_comp != component:
                out_edges[dst_comp] += weight
            if dst_comp == component and src_comp and src_comp != component:
                in_edges[src_comp] += weight
    return out_edges.most_common(), in_edges.most_common()


def render_toc(ctx: Context) -> list[str]:
    previous = existing_sections("TOC.md")
    out = ["# GPlates Developer's Reference", "",
           f"Generated from the `gplates-code` index of GPlates "
           f"{ctx.meta.get('gplates_version', '?')} "
           f"(`{ctx.meta.get('source_root', '?')}`), indexed "
           f"{ctx.meta.get('built_at', '?')}.", ""]

    out += ["## Overview", ""]
    out += keep_or_placeholder(previous, "Overview", "toc", "book", 1, TOC_HINT)

    out += ["", "## How to read this book", "",
            "- Start here, pick a component, then a unit page; every unit page links back "
            "up to its component and to this table of contents.",
            "- Use the indexes below when you already know a name.",
            "- Every unit page ends with `gpq` commands that open the real source, so the "
            "book never has to be trusted over the code.",
            "- Tier 1 pages cover the load-bearing engine units, tier 3 the boilerplate; the "
            "tier is shown in each page's breadcrumb.", ""]

    out += ["## Components", ""]
    rows = []
    for comp in sorted(ctx.components):
        units = ctx.units_by_component.get(comp, [])
        files = sum(len(u["files"]) + len(u["attached"]) for u in units) + \
            len(ctx.extras.get(comp, []))
        rows.append([md_link(comp, "TOC.md", component_page(comp)), str(len(units)), str(files),
                     md_text(ctx.descriptions.get(f"component:{comp}",
                                                  COMPONENT_ROLE.get(comp, PENDING)))])
    out += md_table(["Component", "Units", "Files", "Responsibility"], rows)

    out += ["", "## Indexes", ""]
    out += md_table(["Index", "Contents"], [
        [md_link("Components", "TOC.md", "indexes/Components.md"), "every component, with its unit count"],
        [md_link("Classes", "TOC.md", "indexes/Classes.md"), "classes and unions"],
        [md_link("Structs", "TOC.md", "indexes/Structs.md"), "structs"],
        [md_link("Enums", "TOC.md", "indexes/Enums.md"), "enumerations"],
        [md_link("Typedefs", "TOC.md", "indexes/Typedefs.md"), "typedefs and type aliases"],
        [md_link("Functions", "TOC.md", "indexes/Functions.md"), "free functions at namespace scope"],
        [md_link("Macros", "TOC.md", "indexes/Macros.md"), "preprocessor macros, include guards last"],
    ])

    out += ["", "## Index facts", ""]
    keys = [("count_files", "source files"), ("count_cpp_files", "C++ files"),
            ("count_lines", "indexed lines"), ("count_entities", "entities"),
            ("count_occurrences", "identifier occurrences"),
            ("count_occurrences_resolved", "of them resolved"),
            ("count_includes", "resolved #include edges"),
            ("count_ui_forms", "Qt Designer forms"),
            ("count_qt_connections", "signal/slot connections"),
            ("count_gpgim_features", "GPGIM feature types"),
            ("count_gpgim_properties", "GPGIM property types")]
    out += md_table(["Fact", "Count"],
                    [[label, ctx.meta.get(key, "?")] for key, label in keys
                     if key in ctx.meta])
    out += ["", f"Unit pages: {len(ctx.units)}. Component pages: {len(ctx.components)}."]
    return out


# ---------------------------------------------------------------------------
# Lint
# ---------------------------------------------------------------------------

def lint() -> int:
    from bookkit import load_manifest as _lm
    units = _lm()
    expected = {u["page"]: UNIT_HEADINGS for u in units}
    for comp in sorted({u["component"] for u in units} |
                       set(load_json(DATA_DIR / "extras.json", {}))):
        expected[component_page(comp)] = COMPONENT_HEADINGS
    expected["TOC.md"] = TOC_HEADINGS

    problems = []
    for rel, headings in sorted(expected.items()):
        path = BOOK_DIR / rel
        if not path.exists():
            problems.append(f"{rel}: missing")
            continue
        text = path.read_text(encoding="utf-8")
        found = tuple(line[3:].strip() for line in text.splitlines() if line.startswith("## "))
        if found != tuple(headings):
            problems.append(f"{rel}: heading sequence {found} != {tuple(headings)}")
        problems += lint_tables(rel, text)
        try:
            find_prose_blocks(text)
        except BookError as exc:
            problems.append(f"{rel}: {exc}")
    for p in problems[:60]:
        print(f"lint: {p}")
    print(f"lint: {len(expected)} pages checked, {len(problems)} problem(s)")
    return 1 if problems else 0


def cell_count(row: str) -> int:
    """Cells in a GFM table row, ignoring pipes escaped as `\\|`."""
    return len(re.findall(r"(?<!\\)\|", row)) - 1


def lint_tables(rel: str, text: str) -> list[str]:
    problems, lines = [], text.splitlines()
    i = 0
    while i < len(lines) - 1:
        if lines[i].startswith("| ") and re.match(r"^\|[\s:|-]+\|$", lines[i + 1]):
            width = cell_count(lines[i])
            if cell_count(lines[i + 1]) != width:
                problems.append(f"{rel}:{i + 2}: separator row has "
                                f"{cell_count(lines[i + 1])} cells, header has {width}")
            j = i + 2
            while j < len(lines) and lines[j].startswith("|"):
                if cell_count(lines[j]) != width:
                    problems.append(f"{rel}:{j + 1}: table row has "
                                    f"{cell_count(lines[j])} cells, header has {width}")
                j += 1
            i = j
        else:
            i += 1
    return problems


# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only-changed", action="store_true",
                    help="skip unit pages whose hash matches the last generation")
    ap.add_argument("--lint", action="store_true", help="check book/ structure and exit")
    args = ap.parse_args()

    if args.lint:
        return lint()

    from bookkit import load_descriptions
    ctx = Context()
    ctx.descriptions = load_descriptions()

    stamp_path = DATA_DIR / "skeleton_hashes.json"
    stamps = load_json(stamp_path, {}) if args.only_changed else {}
    # Anchors accumulate: a --only-changed run must not forget skipped pages.
    ctx.anchors = load_json(ANCHORS_PATH, {}) if args.only_changed else {}
    written = skipped = 0
    for unit in ctx.units:
        if args.only_changed and stamps.get(unit["id"]) == unit["hash"] \
                and (BOOK_DIR / unit["page"]).exists():
            skipped += 1
            continue
        write_page(unit["page"], render_unit_page(ctx, unit))
        stamps[unit["id"]] = unit["hash"]
        written += 1
        if written % 200 == 0:
            print(f"  {written} unit pages ...", flush=True)
    save_json(stamp_path, stamps)
    save_json(ANCHORS_PATH, ctx.anchors)

    for comp in ctx.components:
        write_page(component_page(comp), render_component_page(ctx, comp))
    write_page("TOC.md", render_toc(ctx))

    print(f"wrote {written} unit pages ({skipped} unchanged), "
          f"{len(ctx.components)} component pages, TOC.md")
    ctx.db.close()
    return lint()


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BookError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
