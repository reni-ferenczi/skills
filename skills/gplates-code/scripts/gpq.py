#!/usr/bin/env python3
"""gpq - query the GPlates code index.

Quiet, line-oriented output meant to be read by an agent:
every result is one line, most of them in `path:line: text` form.

    python scripts/gpq.py info
    python scripts/gpq.py sym ReconstructLayerProxy
    python scripts/gpq.py def ReconstructLayerProxy --body
    python scripts/gpq.py grep "anchored plate id"
    python scripts/gpq.py refs reconstruct_feature_geometries
    python scripts/gpq.py file src/app-logic/ReconstructUtils.h
    python scripts/gpq.py ui ShapefileAttribute
    python scripts/gpq.py gpgim Isochron

Run `python scripts/gpq.py <command> -h` for per-command options.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from gplates_index.common import SkillError, open_db  # noqa: E402

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):  # pragma: no cover - exotic stdio
        pass

DEFAULT_LIMIT = 40
TEXT_WIDTH = 200

# Code first, prose last, so a truncated result set keeps the useful half.
CATEGORY_RANK = ("cpp", "python", "ui", "shader", "gpgim", "resource", "build", "data", "doc")
RANK_SQL = ("CASE f.category "
            + " ".join("WHEN '%s' THEN %d" % (c, i) for i, c in enumerate(CATEGORY_RANK))
            + " ELSE 99 END")

_out_rows = []
_json_mode = False


# ----------------------------------------------------------------------------
# Output helpers
# ----------------------------------------------------------------------------

def emit(line: str, record=None):
    if _json_mode:
        _out_rows.append(record if record is not None else {"line": line})
    else:
        print(line)


def note(text: str):
    """A single `#` summary line; suppressed in --json and with --no-header."""
    if not _json_mode:
        print("# " + text)


def flush():
    if _json_mode:
        json.dump(_out_rows, sys.stdout, indent=None, default=str)
        sys.stdout.write("\n")


def clip(text, width=TEXT_WIDTH):
    text = (text or "").strip()
    return text if len(text) <= width else text[:width - 3] + "..."


def qualified(scope, name):
    return (scope + "::" + name) if scope else name


# ----------------------------------------------------------------------------
# Matching helpers
# ----------------------------------------------------------------------------

MODES = ("exact", "prefix", "sub", "regex")


def name_clause(pattern, mode, column="name", lc_column="name_lc",
                case_sensitive=False):
    """Return (sql_fragment, params) for a name match, or (None, compiled_regex)."""
    if mode == "regex":
        return None, re.compile(pattern)
    col = column if case_sensitive else lc_column
    val = pattern if case_sensitive else pattern.lower()
    if mode == "exact":
        return "%s = ?" % col, [val]
    if mode == "prefix":
        return "%s LIKE ? ESCAPE '\\'" % col, [_esc(val) + "%"]
    return "%s LIKE ? ESCAPE '\\'" % col, ["%" + _esc(val) + "%"]


def _esc(s):
    return s.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")


def auto_modes(mode):
    """`auto` widens from exact to prefix to substring until something matches."""
    return list(MODES[:3]) if mode == "auto" else [mode]


# ----------------------------------------------------------------------------
# Commands
# ----------------------------------------------------------------------------

def cmd_info(con, args):
    meta = dict(con.execute("SELECT key, value FROM meta"))
    note("GPlates %s at %s" % (meta.get("gplates_version", "?"), meta.get("source_root", "?")))
    note("indexed %s in %ss" % (meta.get("built_at", "?"), meta.get("build_seconds", "?")))
    for key in sorted(k for k in meta if k.startswith("count_")):
        emit("%-18s %s" % (key[6:], meta[key]), {"stat": key[6:], "value": meta[key]})
    emit("")
    note("top-level source modules (files / symbols)")
    rows = con.execute(
        "SELECT CASE WHEN instr(f.dir, '/') > 0 "
        "         THEN substr(f.dir, 1, instr(f.dir || '/', '/') - 1) || '/' || "
        "              substr(f.dir || '/', instr(f.dir || '/', '/') + 1, "
        "                     instr(substr(f.dir || '/', instr(f.dir || '/', '/') + 1), '/') - 1) "
        "         ELSE f.dir END AS module, "
        "       COUNT(DISTINCT f.id), COUNT(s.id) "
        "FROM files f LEFT JOIN symbols s ON s.file_id = f.id "
        "WHERE f.dir <> '' GROUP BY module HAVING COUNT(DISTINCT f.id) > 3 "
        "ORDER BY COUNT(DISTINCT f.id) DESC").fetchall()
    for module, nfiles, nsyms in rows:
        emit("%-32s %5d %7d" % (module, nfiles, nsyms),
             {"module": module, "files": nfiles, "symbols": nsyms})
    return 0


def cmd_sym(con, args):
    where, params = ["1=1"], []
    rx = None
    for mode in auto_modes(args.mode):
        clause, extra = name_clause(args.name, mode, case_sensitive=args.case)
        w, p = list(where), list(params)
        if clause is None:
            rx = extra
        else:
            w.append(clause)
            p.extend(extra)
        if args.kind:
            w.append("s.kind IN (%s)" % ",".join("?" * len(args.kind)))
            p.extend(args.kind)
        if args.lang:
            w.append("s.lang = ?")
            p.append(args.lang)
        if args.path:
            w.append("f.path LIKE ?")
            p.append("%" + args.path + "%")
        if args.scope:
            w.append("s.scope LIKE ?")
            p.append("%" + args.scope + "%")
        if args.defs_only:
            w.append("s.is_def = 1")
        sql = ("SELECT s.name, s.kind, s.lang, s.line, s.end_line, s.scope, s.signature, "
               "       s.typeref, s.access, s.inherits, s.is_def, f.path "
               "FROM symbols s JOIN files f ON f.id = s.file_id "
               "WHERE " + " AND ".join(w) +
               " ORDER BY s.is_def DESC, length(s.name), s.name, f.path, s.line")
        rows = con.execute(sql, p).fetchall()
        if rx is not None:
            rows = [r for r in rows if rx.search(r["name"])]
        if rows:
            return _print_symbols(rows, mode, args)
    note("no symbol matches %r" % args.name)
    return 1


def _print_symbols(rows, mode, args):
    total = len(rows)
    shown = rows[:args.limit]
    note("%d symbol(s)%s [%s]"
         % (total, "" if total <= args.limit else ", showing %d" % len(shown), mode))
    for r in shown:
        sig = r["signature"] or ""
        typ = (" -> " + r["typeref"]) if r["typeref"] else ""
        span = str(r["line"]) if not r["end_line"] else "%d-%d" % (r["line"], r["end_line"])
        flag = "" if r["is_def"] else " (decl)"
        emit("%-11s %s%s%s  %s:%s%s"
             % (r["kind"], qualified(r["scope"], r["name"]), sig, typ, r["path"], span, flag),
             dict(r))
    if total > len(shown):
        note("%d more - narrow with --kind/--path or raise --limit" % (total - len(shown)))
    return 0


def cmd_def(con, args):
    rows = None
    for mode in auto_modes(args.mode):
        clause, extra = name_clause(args.name, mode, case_sensitive=args.case)
        params = list(extra) if clause else []
        sql = ("SELECT s.name, s.kind, s.scope, s.signature, s.line, s.end_line, f.path, f.id "
               "FROM symbols s JOIN files f ON f.id = s.file_id "
               "WHERE s.is_def = 1 AND " + (clause or "1=1"))
        if args.kind:
            sql += " AND s.kind IN (%s)" % ",".join("?" * len(args.kind))
            params.extend(args.kind)
        if args.path:
            sql += " AND f.path LIKE ?"
            params.append("%" + args.path + "%")
        sql += " ORDER BY (s.end_line IS NULL), s.line"
        got = con.execute(sql, params).fetchall()
        if clause is None:
            rx = extra
            got = [r for r in got if rx.search(r["name"])]
        if got:
            rows = got
            break
    if not rows:
        note("no definition found for %r" % args.name)
        return 1
    note("%d definition(s)" % len(rows))
    for r in rows[:args.limit]:
        span = "%d-%s" % (r["line"], r["end_line"] or "?")
        emit("%s %s%s  %s:%s"
             % (r["kind"], qualified(r["scope"], r["name"]), r["signature"] or "",
                r["path"], span), dict(r))
        if args.body:
            end = r["end_line"] or (r["line"] + args.context)
            end = min(end, r["line"] + args.max_body)
            for ln, text in con.execute(
                    "SELECT line, text FROM lines WHERE file_id = ? AND line BETWEEN ? AND ? "
                    "ORDER BY line", (r["id"], r["line"], end)):
                emit("%s:%d: %s" % (r["path"], ln, text.rstrip()),
                     {"path": r["path"], "line": ln, "text": text})
            emit("")
    return 0


FTS_SPECIAL = re.compile(r'[^\w]+')


def cmd_grep(con, args):
    if args.regex:
        return _grep_regex(con, args)
    tokens = [t for t in FTS_SPECIAL.split(args.query) if t]
    if not tokens:
        note("empty query")
        return 1
    match = " ".join('"%s"' % t for t in tokens)
    if args.phrase and len(tokens) > 1:
        match = '"%s"' % " ".join(tokens)
    where, params = ["lines_fts MATCH ?"], [match]
    if args.path:
        where.append("f.path LIKE ?")
        params.append("%" + args.path + "%")
    if args.category:
        where.append("f.category IN (%s)" % ",".join("?" * len(args.category)))
        params.extend(args.category)
    sql = ("SELECT f.path, l.line, l.text FROM lines_fts "
           "JOIN lines l ON l.id = lines_fts.rowid "
           "JOIN files f ON f.id = l.file_id "
           "WHERE " + " AND ".join(where) +
           " ORDER BY " + RANK_SQL + ", f.path, l.line LIMIT ?")
    rows = con.execute(sql, params + [args.limit + 1]).fetchall()
    return _print_lines(con, rows, args, "fts")


def _grep_regex(con, args):
    try:
        rx = re.compile(args.query if args.case else "(?i)" + args.query)
    except re.error as exc:
        note("bad regex: %s" % exc)
        return 2
    where, params = ["1=1"], []
    if args.path:
        where.append("f.path LIKE ?")
        params.append("%" + args.path + "%")
    if args.category:
        where.append("f.category IN (%s)" % ",".join("?" * len(args.category)))
        params.extend(args.category)
    sql = ("SELECT f.path, l.line, l.text FROM lines l JOIN files f ON f.id = l.file_id "
           "WHERE " + " AND ".join(where) + " ORDER BY " + RANK_SQL + ", f.path, l.line")
    rows = []
    for r in con.execute(sql, params):
        if rx.search(r["text"]):
            rows.append(r)
            if len(rows) > args.limit:
                break
    return _print_lines(con, rows, args, "regex")


def _print_lines(con, rows, args, mode):
    if not rows:
        note("no matches [%s]" % mode)
        return 1
    truncated = len(rows) > args.limit
    rows = rows[:args.limit]
    note("%d line(s)%s [%s]" % (len(rows), " (truncated)" if truncated else "", mode))
    for r in rows:
        emit("%s:%d: %s" % (r["path"], r["line"], clip(r["text"])),
             {"path": r["path"], "line": r["line"], "text": r["text"]})
    if truncated:
        note("more matches exist - raise --limit or add --path/--category")
    return 0


def cmd_refs(con, args):
    """Identifier occurrences, definitions listed first."""
    defs = con.execute(
        "SELECT f.path, s.line, s.kind, s.scope, s.name FROM symbols s "
        "JOIN files f ON f.id = s.file_id WHERE s.name = ? AND s.is_def = 1 "
        "ORDER BY f.path, s.line", (args.name,)).fetchall()
    if defs:
        note("%d definition(s)" % len(defs))
        for d in defs[:args.limit]:
            emit("%s:%d: [def %s] %s" % (d["path"], d["line"], d["kind"],
                                         qualified(d["scope"], d["name"])), dict(d))
    where, params = ["lines_fts MATCH ?"], ['"%s"' % args.name]
    if args.path:
        where.append("f.path LIKE ?")
        params.append("%" + args.path + "%")
    sql = ("SELECT f.path, l.line, l.text FROM lines_fts "
           "JOIN lines l ON l.id = lines_fts.rowid JOIN files f ON f.id = l.file_id "
           "WHERE " + " AND ".join(where) + " ORDER BY " + RANK_SQL + ", f.path, l.line")
    word = re.compile(r'\b%s\b' % re.escape(args.name))
    def_at = {(d["path"], d["line"]) for d in defs}
    rows = []
    for r in con.execute(sql, params):
        if (r["path"], r["line"]) in def_at:
            continue
        if word.search(r["text"]):
            rows.append(r)
            if len(rows) > args.limit:
                break
    if not rows:
        note("no other references")
        return 0 if defs else 1
    truncated = len(rows) > args.limit
    rows = rows[:args.limit]
    note("%d reference(s)%s" % (len(rows), " (truncated)" if truncated else ""))
    for r in rows:
        emit("%s:%d: %s" % (r["path"], r["line"], clip(r["text"])),
             {"path": r["path"], "line": r["line"], "text": r["text"]})
    return 0


def _resolve_file(con, path):
    rows = con.execute("SELECT id, path, category, lines, size FROM files WHERE path = ?",
                       (path.replace("\\", "/"),)).fetchall()
    if not rows:
        rows = con.execute(
            "SELECT id, path, category, lines, size FROM files WHERE path LIKE ? "
            "ORDER BY length(path) LIMIT 10", ("%" + path.replace("\\", "/") + "%",)).fetchall()
    return rows


def cmd_file(con, args):
    rows = _resolve_file(con, args.path)
    if not rows:
        note("no file matches %r" % args.path)
        return 1
    if len(rows) > 1 and not args.first:
        note("%d files match - pass a longer path or --first" % len(rows))
        for r in rows:
            emit("%s  (%s, %d lines)" % (r["path"], r["category"], r["lines"]), dict(r))
        return 0
    f = rows[0]
    note("%s  %s  %d lines  %d bytes" % (f["path"], f["category"], f["lines"], f["size"]))
    if args.cat or args.range:
        lo, hi = 1, f["lines"]
        if args.range:
            parts = args.range.split("-", 1)
            lo = int(parts[0])
            hi = int(parts[1]) if len(parts) > 1 and parts[1] else lo
        for ln, text in con.execute(
                "SELECT line, text FROM lines WHERE file_id = ? AND line BETWEEN ? AND ? "
                "ORDER BY line", (f["id"], lo, hi)):
            emit("%s:%d: %s" % (f["path"], ln, text.rstrip()),
                 {"path": f["path"], "line": ln, "text": text})
        return 0
    syms = con.execute(
        "SELECT name, kind, scope, signature, line, end_line, is_def FROM symbols "
        "WHERE file_id = ? ORDER BY line", (f["id"],)).fetchall()
    if syms:
        note("%d symbol(s)" % len(syms))
        for s in syms[:args.limit]:
            span = str(s["line"]) if not s["end_line"] else "%d-%d" % (s["line"], s["end_line"])
            emit("%s:%s: %-11s %s%s%s"
                 % (f["path"], span, s["kind"], qualified(s["scope"], s["name"]),
                    s["signature"] or "", "" if s["is_def"] else " (decl)"), dict(s))
        if len(syms) > args.limit:
            note("%d more symbols - raise --limit" % (len(syms) - args.limit))
    form = con.execute("SELECT class_name, base_class, title FROM ui_forms WHERE file_id = ?",
                       (f["id"],)).fetchone()
    if form:
        note("Qt form %s : %s  %r" % (form["class_name"], form["base_class"], form["title"]))
        for w in con.execute("SELECT widget_class, object_name, text FROM ui_widgets "
                             "WHERE file_id = ? ORDER BY rowid", (f["id"],)).fetchall()[:args.limit]:
            emit("  %-28s %-34s %s" % (w["widget_class"], w["object_name"],
                                       clip(w["text"] or "", 80)), dict(w))
    return 0


def cmd_tree(con, args):
    prefix = (args.prefix or "").replace("\\", "/").rstrip("/")
    depth = args.depth
    rows = con.execute(
        "SELECT dir, COUNT(*) AS n, SUM(lines) AS l FROM files "
        "WHERE dir LIKE ? GROUP BY dir ORDER BY dir",
        (prefix + "%" if prefix else "%",)).fetchall()
    if not rows:
        note("no directories under %r" % prefix)
        return 1
    base_depth = prefix.count("/") + 1 if prefix else 0
    agg = {}
    for r in rows:
        parts = r["dir"].split("/")
        key = "/".join(parts[:base_depth + depth]) or "."
        cur = agg.setdefault(key, [0, 0])
        cur[0] += r["n"]
        cur[1] += r["l"] or 0
    note("%d directories (depth %d under %r)" % (len(agg), depth, prefix or "."))
    for key in sorted(agg):
        emit("%-46s %5d files %8d lines" % (key, agg[key][0], agg[key][1]),
             {"dir": key, "files": agg[key][0], "lines": agg[key][1]})
    return 0


def cmd_includes(con, args):
    rows = _resolve_file(con, args.path)
    if not rows:
        note("no file matches %r" % args.path)
        return 1
    f = rows[0]
    if args.by:
        sql = ("SELECT f.path, i.line, i.header FROM includes i "
               "JOIN files f ON f.id = i.file_id WHERE i.target_id = ? "
               "ORDER BY f.path LIMIT ?")
        got = con.execute(sql, (f["id"], args.limit + 1)).fetchall()
        note("%d file(s) include %s" % (min(len(got), args.limit), f["path"]))
        for r in got[:args.limit]:
            emit("%s:%d: #include \"%s\"" % (r["path"], r["line"], r["header"]), dict(r))
        if len(got) > args.limit:
            note("more - raise --limit")
        return 0
    got = con.execute(
        "SELECT i.line, i.header, i.is_system, t.path AS target FROM includes i "
        "LEFT JOIN files t ON t.id = i.target_id WHERE i.file_id = ? ORDER BY i.line",
        (f["id"],)).fetchall()
    note("%s includes %d header(s)" % (f["path"], len(got)))
    for r in got[:args.limit]:
        mark = "<>" if r["is_system"] else '""'
        emit("%s:%d: %s %s%s" % (f["path"], r["line"], mark, r["header"],
                                 "  -> " + r["target"] if r["target"] else ""), dict(r))
    return 0


def cmd_hier_legacy(con, args):
    name = args.name
    bases = con.execute(
        "SELECT s.name, s.scope, s.inherits, f.path, s.line FROM symbols s "
        "JOIN files f ON f.id = s.file_id "
        "WHERE s.name = ? AND s.kind IN ('class','struct') AND s.is_def = 1",
        (name,)).fetchall()
    if not bases:
        note("no class/struct named %r" % name)
        return 1
    for b in bases:
        emit("class %s  %s:%d" % (qualified(b["scope"], b["name"]), b["path"], b["line"]), dict(b))
        if b["inherits"]:
            for parent in b["inherits"].split(","):
                emit("  base: %s" % parent.strip(), {"base": parent.strip()})
    subs = con.execute(
        "SELECT s.name, s.scope, s.inherits, f.path, s.line FROM symbols s "
        "JOIN files f ON f.id = s.file_id "
        "WHERE s.kind IN ('class','struct') AND s.is_def = 1 AND s.inherits IS NOT NULL "
        "AND (s.inherits = ? OR s.inherits LIKE ? OR s.inherits LIKE ? OR s.inherits LIKE ?) "
        "ORDER BY s.name",
        (name, name + ",%", "%," + name, "%,%" + name + ",%")).fetchall()
    extra = con.execute(
        "SELECT s.name, s.scope, s.inherits, f.path, s.line FROM symbols s "
        "JOIN files f ON f.id = s.file_id "
        "WHERE s.kind IN ('class','struct') AND s.is_def = 1 AND s.inherits LIKE ? "
        "ORDER BY s.name", ("%" + name + "%",)).fetchall()
    seen = {(s["path"], s["line"]) for s in subs}
    for e in extra:
        parts = [p.strip().split("<")[0].split("::")[-1] for p in (e["inherits"] or "").split(",")]
        if name in parts and (e["path"], e["line"]) not in seen:
            subs.append(e)
            seen.add((e["path"], e["line"]))
    note("%d direct subclass(es)" % len(subs))
    for s in sorted(subs, key=lambda r: r["name"])[:args.limit]:
        emit("  sub: %-46s %s:%d" % (qualified(s["scope"], s["name"]), s["path"], s["line"]),
             dict(s))
    return 0



# ----------------------------------------------------------------------------
# Deep index: entities, declarations, usages, hierarchy
# ----------------------------------------------------------------------------

ENTITY_COLS = ("SELECT e.id, e.name, e.qname, e.kind, e.line, e.col, e.end_line, "
               "e.type_text, e.signature, e.access, e.storage, e.is_def, e.is_template, "
               "e.template_params, f.path "
               "FROM entities e JOIN files f ON f.id = e.file_id ")


def _entity_line(r):
    tmpl = ("template%s " % r["template_params"]) if r["is_template"] else ""
    sig = r["signature"] or ""
    if r["kind"] in ("macro", "macro_function"):
        typ = ("  = " + clip(r["type_text"], 60)) if r["type_text"] else ""
    else:
        typ = (" -> " + r["type_text"]) if r["type_text"] else ""
    acc = (" [%s]" % r["access"]) if r["access"] else ""
    if not r["end_line"] or r["end_line"] == r["line"]:
        span = str(r["line"])
    else:
        span = "%d-%d" % (r["line"], r["end_line"])
    tag = "def" if r["is_def"] else "decl"
    return "%-12s %s%s%s%s%s  %s:%s (%s)" % (
        r["kind"], tmpl, r["qname"], sig, typ, acc, r["path"], span, tag)


def _find_entities(con, name, args, only_def=None, kinds=None):
    """Resolve a user-supplied name to entity rows, widening exact -> prefix -> substring."""
    for mode in auto_modes(getattr(args, "mode", "auto")):
        clause, extra = name_clause(name, mode, column="e.name", lc_column="e.name_lc",
                                    case_sensitive=getattr(args, "case", False))
        where, params, rx = [], [], None
        if clause is None:
            rx = extra
        else:
            where.append(clause)
            params.extend(extra)
        if "::" in name:
            where = ["(e.qname = ? OR e.qname LIKE ?)"]
            params = [name, "%::" + name]
            rx = None
        kind_filter = kinds if kinds is not None else getattr(args, "kind", None)
        if kind_filter:
            where.append("e.kind IN (%s)" % ",".join("?" * len(kind_filter)))
            params.extend(kind_filter)
        if getattr(args, "path", None):
            where.append("f.path LIKE ?")
            params.append("%" + args.path + "%")
        if only_def is not None:
            where.append("e.is_def = %d" % (1 if only_def else 0))
        sql = ENTITY_COLS + ("WHERE " + " AND ".join(where) if where else "")
        sql += " ORDER BY e.is_def DESC, length(e.qname), e.qname, f.path, e.line"
        rows = con.execute(sql, params).fetchall()
        if rx is not None:
            rows = [r for r in rows if rx.search(r["name"])]
        if rows:
            return rows, mode
    return [], None


def cmd_decl(con, args):
    """Declarations and definitions of anything: type, member, variable or macro."""
    rows, mode = _find_entities(con, args.name, args)
    if not rows:
        note("no declaration matches %r" % args.name)
        return 1
    defs = [r for r in rows if r["is_def"]]
    decls = [r for r in rows if not r["is_def"]]
    note("%d definition(s), %d declaration(s) [%s]" % (len(defs), len(decls), mode))
    for r in (defs + decls)[:args.limit]:
        emit(_entity_line(r), dict(r))
    if len(rows) > args.limit:
        note("%d more - narrow with --kind/--path or raise --limit" % (len(rows) - args.limit))
    return 0


USE_ROLES = ("call", "read", "write", "member", "member_write", "type",
             "base", "template_arg", "ns", "decl", "def")


def cmd_uses(con, args):
    """Resolved usages of an entity, grouped by the role the identifier plays."""
    rows, mode = _find_entities(con, args.name, args)
    if not rows:
        note("no entity named %r" % args.name)
        return 1
    ids = [r["id"] for r in rows]
    note("%d matching entities [%s]: %s" % (
        len(rows), mode,
        "; ".join("%s %s (%s:%d)" % (t["kind"], t["qname"], t["path"], t["line"])
                  for t in rows[:5])))
    where = ["o.entity_id IN (%s)" % ",".join("?" * len(ids))]
    params = list(ids)
    if args.role:
        where.append("o.role IN (%s)" % ",".join("?" * len(args.role)))
        params.extend(args.role)
    if args.path:
        where.append("f.path LIKE ?")
        params.append("%" + args.path + "%")
    if args.exclude_decl:
        where.append("o.role NOT IN ('def','decl')")
    counts = con.execute(
        "SELECT o.role, COUNT(*) c FROM occurrences o JOIN files f ON f.id = o.file_id "
        "WHERE " + " AND ".join(where) + " GROUP BY o.role ORDER BY c DESC",
        params).fetchall()
    if not counts:
        note("no recorded usages")
        return 1
    note("usages by role: " + ", ".join("%s=%d" % (c["role"], c["c"]) for c in counts))
    sql = ("SELECT f.path, o.line, o.role, o.confidence, l.text, e.qname AS ctx "
           "FROM occurrences o JOIN files f ON f.id = o.file_id "
           "LEFT JOIN lines l ON l.file_id = o.file_id AND l.line = o.line "
           "LEFT JOIN entities e ON e.id = o.container_id "
           "WHERE " + " AND ".join(where) +
           " ORDER BY " + RANK_SQL + ", f.path, o.line LIMIT ?")
    got = con.execute(sql, params + [args.limit + 1]).fetchall()
    for r in got[:args.limit]:
        ctx = (" [in %s]" % r["ctx"]) if r["ctx"] and args.context_symbol else ""
        emit("%s:%d: %-12s %s%s" % (r["path"], r["line"], r["role"],
                                    clip(r["text"] or "", 150), ctx), dict(r))
    if len(got) > args.limit:
        note("more usages - raise --limit or filter with --role/--path")
    unresolved = con.execute(
        "SELECT COUNT(*) FROM occurrences WHERE entity_id IS NULL AND name = ?",
        (rows[0]["name"],)).fetchone()[0]
    if unresolved:
        note("%d further occurrence(s) of this name were not bound to a specific "
             "entity; `gpq refs %s` shows them" % (unresolved, rows[0]["name"]))
    return 0


def cmd_hier(con, args):
    """Base classes and subclasses, transitively, from the resolved inheritance graph."""
    rows, mode = _find_entities(con, args.name, args,
                                kinds=("class", "struct", "union"))
    if not rows:
        note("no class or struct named %r" % args.name)
        return 1
    defined = [r for r in rows if r["is_def"]]
    rows = defined or rows
    target = rows[0]
    note("%s %s  %s:%d [%s]" % (target["kind"], target["qname"], target["path"],
                                target["line"], mode))
    if not args.down:
        direct = con.execute(
            "SELECT b.base_name, b.access, b.is_virtual, e.qname, f.path, e.line "
            "FROM bases b LEFT JOIN entities e ON e.id = b.base_entity_id "
            "LEFT JOIN files f ON f.id = e.file_id WHERE b.entity_id = ?",
            (target["id"],)).fetchall()
        for d in direct:
            where = ("  %s:%d" % (d["path"], d["line"])) if d["path"] \
                else "  (outside the GPlates tree)"
            emit("  base d1     %-52s%s" % (d["qname"] or d["base_name"], where), dict(d))
        anc = con.execute(
            "SELECT c.depth, e.qname, e.kind, f.path, e.line FROM inherit_closure c "
            "JOIN entities e ON e.id = c.ancestor_id JOIN files f ON f.id = e.file_id "
            "WHERE c.descendant_id = ? AND c.depth > 1 AND c.depth <= ? "
            "ORDER BY c.depth, e.qname", (target["id"], args.depth)).fetchall()
        for a in anc[:args.limit]:
            emit("  base d%-5d %-52s  %s:%d" % (a["depth"], a["qname"], a["path"],
                                                a["line"]), dict(a))
    if not args.up:
        subs = con.execute(
            "SELECT c.depth, e.qname, e.kind, f.path, e.line FROM inherit_closure c "
            "JOIN entities e ON e.id = c.descendant_id JOIN files f ON f.id = e.file_id "
            "WHERE c.ancestor_id = ? AND c.depth <= ? ORDER BY c.depth, e.qname",
            (target["id"], args.depth)).fetchall()
        note("%d subclass(es) within depth %d" % (len(subs), args.depth))
        for sub in subs[:args.limit]:
            emit("  sub  d%-5d %-52s  %s:%d" % (sub["depth"], sub["qname"], sub["path"],
                                                sub["line"]), dict(sub))
        if len(subs) > args.limit:
            note("%d more subclasses - raise --limit" % (len(subs) - args.limit))
    return 0


def cmd_members(con, args):
    """Everything declared inside a class, struct, enum or namespace."""
    container_kinds = ("class", "struct", "union", "enum", "namespace")
    rows, mode = _find_entities(con, args.name, args, kinds=container_kinds)
    if not rows:
        note("no type or namespace named %r" % args.name)
        return 1
    defined = [r for r in rows if r["is_def"]]
    rows = defined or rows
    target = rows[0]
    note("%s %s  %s:%d [%s]" % (target["kind"], target["qname"], target["path"],
                                target["line"], mode))
    where, params = ["e.parent_id = ?"], [target["id"]]
    if args.kind:
        where.append("e.kind IN (%s)" % ",".join("?" * len(args.kind)))
        params.extend(args.kind)
    if args.access:
        where.append("e.access = ?")
        params.append(args.access)
    got = con.execute(ENTITY_COLS + "WHERE " + " AND ".join(where) +
                      " ORDER BY e.kind, e.line", params).fetchall()
    if args.inherited:
        for (aid,) in con.execute(
                "SELECT ancestor_id FROM inherit_closure WHERE descendant_id = ?",
                (target["id"],)):
            got += con.execute(ENTITY_COLS + "WHERE e.parent_id = ? ORDER BY e.line",
                               (aid,)).fetchall()
    if not got:
        note("no members recorded")
        return 1
    note("%d member(s)" % len(got))
    for r in got[:args.limit]:
        emit("  " + _entity_line(r), dict(r))
    if len(got) > args.limit:
        note("%d more - raise --limit or filter with --kind" % (len(got) - args.limit))
    return 0


def cmd_macro(con, args):
    """Preprocessor symbols: where defined, what they expand to, where used."""
    like = "%" + (args.name or "") + "%"
    rows = con.execute(
        ENTITY_COLS + "WHERE e.kind IN ('macro','macro_function') AND e.name LIKE ? "
        "ORDER BY e.name", (like,)).fetchall()
    if not rows:
        note("no macro matches %r" % (args.name or ""))
        return 1
    note("%d macro(s)" % len(rows))
    for r in rows[:args.limit]:
        emit(_entity_line(r), dict(r))
        if args.uses:
            for u in con.execute(
                    "SELECT f.path, o.line, l.text FROM occurrences o "
                    "JOIN files f ON f.id = o.file_id "
                    "LEFT JOIN lines l ON l.file_id = o.file_id AND l.line = o.line "
                    "WHERE o.entity_id = ? AND o.role <> 'def' "
                    "ORDER BY f.path, o.line LIMIT ?", (r["id"], args.limit)):
                emit("    %s:%d: %s" % (u["path"], u["line"], clip(u["text"] or "", 140)),
                     dict(u))
    return 0


def cmd_ui(con, args):
    like = "%" + args.name + "%" if args.name else "%"
    forms = con.execute(
        "SELECT u.class_name, u.base_class, u.title, f.path FROM ui_forms u "
        "JOIN files f ON f.id = u.file_id "
        "WHERE u.class_name LIKE ? OR u.title LIKE ? OR f.path LIKE ? ORDER BY u.class_name",
        (like, like, like)).fetchall()
    widgets = []
    if len(forms) == 1:
        widgets = con.execute(
            "SELECT w.form, w.widget_class, w.object_name, w.text, f.path FROM ui_widgets w "
            "JOIN files f ON f.id = w.file_id WHERE f.path = ? ORDER BY w.rowid",
            (forms[0]["path"],)).fetchall()
    elif args.name:
        widgets = con.execute(
            "SELECT w.form, w.widget_class, w.object_name, w.text, f.path FROM ui_widgets w "
            "JOIN files f ON f.id = w.file_id "
            "WHERE w.object_name LIKE ? OR w.text LIKE ? OR w.widget_class LIKE ? "
            "ORDER BY w.form, w.object_name", (like, like, like)).fetchall()
    if not forms and not widgets:
        note("no Qt form or widget matches %r" % (args.name or ""))
        return 1
    if forms:
        note("%d form(s)" % len(forms))
        for r in forms[:args.limit]:
            emit("%-34s : %-22s %-32s %s"
                 % (r["class_name"], r["base_class"] or "", clip(r["title"] or "", 32),
                    r["path"]), dict(r))
    if widgets:
        note("%d widget(s)" % len(widgets))
        for r in widgets[:args.limit]:
            emit("%-24s %-28s %-30s %s"
                 % (r["form"], r["widget_class"], r["object_name"], clip(r["text"] or "", 50)),
                 dict(r))
        if len(widgets) > args.limit:
            note("%d more widgets - raise --limit" % (len(widgets) - args.limit))
    return 0


def cmd_signals(con, args):
    like = "%" + args.name + "%"
    rows = con.execute(
        "SELECT f.path, c.line, c.sender, c.signal, c.receiver, c.slot FROM qt_connections c "
        "JOIN files f ON f.id = c.file_id "
        "WHERE c.signal LIKE ? OR c.slot LIKE ? OR c.sender LIKE ? OR c.receiver LIKE ? "
        "ORDER BY f.path, c.line", (like, like, like, like)).fetchall()
    if not rows:
        note("no Qt connection mentions %r" % args.name)
        return 1
    note("%d connection(s)" % len(rows))
    for r in rows[:args.limit]:
        emit("%s:%d: %s.%s -> %s.%s"
             % (r["path"], r["line"], clip(r["sender"], 46), clip(r["signal"], 60),
                clip(r["receiver"], 46), clip(r["slot"], 60)), dict(r))
    if len(rows) > args.limit:
        note("%d more - raise --limit" % (len(rows) - args.limit))
    return 0


def cmd_pyapi(con, args):
    like = "%" + (args.name or "") + "%"
    rows = con.execute(
        "SELECT p.owner, p.name, p.kind, p.cpp_type, f.path, p.line FROM py_api p "
        "JOIN files f ON f.id = p.file_id "
        "WHERE p.name LIKE ? OR p.owner LIKE ? OR p.cpp_type LIKE ? "
        "ORDER BY p.owner, p.kind, p.name", (like, like, like)).fetchall()
    if not rows:
        note("no Python binding matches %r" % (args.name or ""))
        return 1
    note("%d Python binding(s)" % len(rows))
    for r in rows[:args.limit]:
        pyname = (r["owner"] + "." + r["name"]) if r["owner"] else r["name"]
        emit("%-11s %-44s %-46s %s:%d"
             % (r["kind"], pyname, clip(r["cpp_type"] or "", 46), r["path"], r["line"]), dict(r))
    if len(rows) > args.limit:
        note("%d more - raise --limit" % (len(rows) - args.limit))
    return 0


def cmd_gpgim(con, args):
    like = "%" + (args.name or "") + "%"
    feats = con.execute(
        "SELECT g.name, g.class_type, g.inherits, g.default_geometry, g.description, "
        "       f.path, g.line FROM gpgim_features g JOIN files f ON f.id = g.file_id "
        "WHERE g.name LIKE ? ORDER BY g.name", (like,)).fetchall()
    props = con.execute(
        "SELECT p.name, p.types, p.multiplicity, p.description, f.path, p.line "
        "FROM gpgim_properties p JOIN files f ON f.id = p.file_id "
        "WHERE p.name LIKE ? ORDER BY p.name", (like,)).fetchall()
    if not feats and not props:
        note("no GPGIM feature class or property matches %r" % (args.name or ""))
        return 1
    if feats:
        note("%d feature class(es)" % len(feats))
        for r in feats[:args.limit]:
            emit("feature  %-38s %-9s inherits=%-26s %s:%d"
                 % (r["name"], r["class_type"] or "", r["inherits"] or "-",
                    r["path"], r["line"]), dict(r))
            if args.detail:
                if r["description"]:
                    emit("    %s" % clip(r["description"], 300))
                if r["default_geometry"]:
                    emit("    default geometry: %s" % r["default_geometry"])
                own = con.execute(
                    "SELECT property FROM gpgim_feature_properties WHERE feature = ? "
                    "ORDER BY property", (r["name"],)).fetchall()
                if own:
                    emit("    properties: %s" % ", ".join(p[0] for p in own))
    if props:
        note("%d property(ies)" % len(props))
        for r in props[:args.limit]:
            emit("property %-38s %-11s %s  %s:%d"
                 % (r["name"], r["multiplicity"] or "", clip(r["types"] or "", 70),
                    r["path"], r["line"]), dict(r))
            if args.detail and r["description"]:
                emit("    %s" % clip(r["description"], 300))
            if args.detail:
                users = con.execute(
                    "SELECT feature FROM gpgim_feature_properties WHERE property = ? "
                    "ORDER BY feature", (r["name"],)).fetchall()
                if users:
                    emit("    used by: %s" % ", ".join(u[0] for u in users[:30]))
    return 0



# ----------------------------------------------------------------------------
# Code communities (Graphify + Leiden), from data/graph.db
# ----------------------------------------------------------------------------

def _graph_db_path():
    from gplates_index.common import DATA_DIR
    return DATA_DIR / "graph.db"


def attach_graph(con):
    """ATTACH the graph database read-only. Raises SkillError when absent."""
    path = _graph_db_path()
    if not path.exists():
        raise SkillError(
            "no code graph yet - build it with:  python scripts/build_graph.py\n"
            "(it is optional and separate from the main index)")
    con.execute("ATTACH DATABASE ? AS g", ("file:%s?mode=ro" % path.as_posix(),))
    return con


def _community_header(con, cid):
    row = con.execute(
        "SELECT id, name, size, top_dirs, top_nodes FROM g.communities WHERE id = ?",
        (cid,)).fetchone()
    if row is None:
        return None
    label = row["name"] or ("Community %d" % row["id"])
    note("community %d: %s  (%d nodes)" % (row["id"], label, row["size"]))
    if row["top_dirs"]:
        note("  dirs: %s" % row["top_dirs"])
    return row


def cmd_community(con, args):
    """Which cluster of the codebase a symbol belongs to, and what else is in it."""
    attach_graph(con)

    if args.list:
        rows = con.execute(
            "SELECT id, name, size, top_dirs, top_nodes FROM g.communities "
            "ORDER BY size DESC LIMIT ?", (args.limit,)).fetchall()
        total = con.execute("SELECT COUNT(*) FROM g.communities").fetchone()[0]
        note("%d communities, largest %d shown" % (total, len(rows)))
        for r in rows:
            emit("%-6d %-5d %-46s %s"
                 % (r["id"], r["size"], clip(r["top_dirs"] or "", 46),
                    clip(r["top_nodes"] or "", 70)), dict(r))
        return 0

    if args.id is not None:
        if _community_header(con, args.id) is None:
            note("no community with id %d" % args.id)
            return 1
        return _print_members(con, args.id, args)

    if not args.name:
        note("give a symbol name, --id N, or --list")
        return 2

    like = args.name if args.case else args.name.lower()
    col = "label" if args.case else "label_lc"

    # Graphify emits "stub" nodes for names it saw only in another file's
    # extraction: no source location, one edge, and a misleading community.
    # Rank against the entity index so a real definition always wins.
    rank = ("(CASE WHEN EXISTS (SELECT 1 FROM entities e JOIN files f ON f.id = e.file_id "
            "   WHERE f.path = n.path AND e.line = n.line AND e.is_def = 1) THEN 0 "
            " WHEN n.path IS NOT NULL AND n.line IS NOT NULL THEN 1 ELSE 2 END)")
    base = ("SELECT n.id, n.label, n.path, n.line, n.community, n.is_class, "
            + rank + " AS rank FROM g.graph_nodes n WHERE n.")
    rows = con.execute(base + "%s = ? ORDER BY rank, n.is_class DESC, n.path"
                       % col, (like,)).fetchall()
    if not rows:
        rows = con.execute(
            base + "%s LIKE ? ORDER BY rank, n.is_class DESC, length(n.label) LIMIT 40"
            % col, ("%" + like + "%",)).fetchall()
    if not rows:
        note("no graph node matches %r" % args.name)
        return 1

    real = [r for r in rows if r["rank"] == 0]
    stubs = len(rows) - len(real)
    shown = real or rows
    for r in shown[:args.limit]:
        tag = {0: "def", 1: "ref", 2: "stub"}[r["rank"]]
        emit("%-38s %-44s [%s] -> community %s"
             % (r["label"], "%s:%s" % (r["path"] or "?", r["line"] or "?"), tag,
                r["community"]), dict(r))
    if stubs and real:
        note("%d stub/reference node(s) hidden - they carry no definition" % stubs)
    elif not real:
        note("no node with a definition in the index; these may be stubs")

    seen = [r["community"] for r in shown if r["community"] is not None]
    if not seen:
        note("matched nodes carry no community (was the graph clustered?)")
        return 1
    uniq = list(dict.fromkeys(seen))
    if len(uniq) > 1:
        note("%d distinct communities matched; showing the best-ranked one" % len(uniq))
    emit("")
    _community_header(con, uniq[0])
    return _print_members(con, uniq[0], args)


def _print_members(con, cid, args):
    rows = con.execute(
        "SELECT label, path, line, is_class, is_callable FROM g.graph_nodes "
        "WHERE community = ? AND path IS NOT NULL "
        "ORDER BY is_class DESC, path, line", (cid,)).fetchall()
    hidden = con.execute(
        "SELECT COUNT(*) FROM g.graph_nodes WHERE community = ? AND path IS NULL",
        (cid,)).fetchone()[0]
    note("%d member(s) with a source location%s"
         % (len(rows), (", %d stubs hidden" % hidden) if hidden else ""))
    for r in rows[:args.limit]:
        kind = "class" if r["is_class"] else ("callable" if r["is_callable"] else "")
        emit("  %-10s %-44s %s:%s" % (kind, clip(r["label"], 44),
                                      r["path"] or "?", r["line"] or "?"), dict(r))
    if len(rows) > args.limit:
        note("%d more - raise --limit" % (len(rows) - args.limit))
    return 0


def cmd_neighbors(con, args):
    """Direct graph edges into and out of a symbol."""
    attach_graph(con)
    col = "label" if args.case else "label_lc"
    key = args.name if args.case else args.name.lower()
    # Same stub guard as `community`: prefer nodes that sit on a real definition,
    # then nodes that at least have a source location, then bare stubs.
    rank = ("(CASE WHEN EXISTS (SELECT 1 FROM entities e JOIN files f ON f.id = e.file_id "
            "   WHERE f.path = n.path AND e.line = n.line AND e.is_def = 1) THEN 0 "
            " WHEN n.path IS NOT NULL THEN 1 ELSE 2 END)")
    nodes = con.execute(
        "SELECT n.id, n.label, n.path, n.line, " + rank + " AS rank, "
        "  (SELECT COUNT(*) FROM g.graph_edges e2 "
        "     WHERE e2.src = n.id OR e2.dst = n.id) AS degree "
        "FROM g.graph_nodes n WHERE n.%s = ? "
        "ORDER BY rank, degree DESC, n.is_class DESC LIMIT 5" % col, (key,)).fetchall()
    if not nodes:
        note("no graph node named %r" % args.name)
        return 1
    connected = [n for n in nodes if n["degree"] > 0]
    if connected:
        nodes = connected[:args.nodes]
    else:
        nodes = nodes[:args.nodes]
    for n in nodes:
        note("%s  %s:%s  (degree %d)"
             % (n["label"], n["path"] or "?", n["line"] or "?", n["degree"]))
        where = "e.relation IN (%s)" % ",".join("?" * len(args.relation)) \
            if args.relation else "1=1"
        params = list(args.relation) if args.relation else []
        out = con.execute(
            "SELECT e.relation, t.label, t.path, t.line FROM g.graph_edges e "
            "JOIN g.graph_nodes t ON t.id = e.dst WHERE e.src = ? AND " + where +
            " ORDER BY e.relation, t.label LIMIT ?", [n["id"]] + params + [args.limit]
        ).fetchall()
        for r in out:
            emit("  -> %-14s %-40s %s:%s" % (r["relation"], clip(r["label"], 40),
                                             r["path"] or "?", r["line"] or "?"), dict(r))
        inc = con.execute(
            "SELECT e.relation, t.label, t.path, t.line FROM g.graph_edges e "
            "JOIN g.graph_nodes t ON t.id = e.src WHERE e.dst = ? AND " + where +
            " ORDER BY e.relation, t.label LIMIT ?", [n["id"]] + params + [args.limit]
        ).fetchall()
        for r in inc:
            emit("  <- %-14s %-40s %s:%s" % (r["relation"], clip(r["label"], 40),
                                             r["path"] or "?", r["line"] or "?"), dict(r))
        if not out and not inc:
            note("  (no edges)")
    return 0


def cmd_sql(con, args):
    """Escape hatch: raw read-only SQL against the index (graph attached as `g` if built)."""
    try:
        attach_graph(con)
    except SkillError:
        pass
    rows = con.execute(args.query).fetchall()
    note("%d row(s)" % len(rows))
    for r in rows[:args.limit]:
        emit(" | ".join("" if v is None else clip(str(v), 120) for v in tuple(r)), dict(r))
    return 0


# ----------------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------------

def build_parser():
    ap = argparse.ArgumentParser(prog="gpq", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true", help="emit JSON records instead of lines")
    ap.add_argument("--limit", type=int, default=DEFAULT_LIMIT, help="max rows (default 40)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    # Repeat the global options on every subcommand so they work in either position.
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--json", action="store_true", default=argparse.SUPPRESS,
                        help="emit JSON records instead of lines")
    common.add_argument("--limit", type=int, default=argparse.SUPPRESS,
                        help="max rows (default 40)")

    def add(name, fn, help_):
        p = sub.add_parser(name, help=help_, parents=[common])
        p.set_defaults(func=fn)
        return p

    add("info", cmd_info, "index stats and the top-level module map")

    p = add("sym", cmd_sym, "find symbols by name")
    p.add_argument("name")
    p.add_argument("--mode", choices=("auto",) + MODES, default="auto")
    p.add_argument("--kind", action="append", help="class, struct, function, member, ... (repeatable)")
    p.add_argument("--lang", help="C++ or Python")
    p.add_argument("--path", help="only files whose path contains this")
    p.add_argument("--scope", help="only symbols whose scope contains this")
    p.add_argument("--case", action="store_true", help="case sensitive")
    p.add_argument("--defs-only", action="store_true", help="skip declarations/prototypes")

    p = add("def", cmd_def, "locate a definition, optionally printing its body")
    p.add_argument("name")
    p.add_argument("--mode", choices=("auto",) + MODES, default="auto")
    p.add_argument("--kind", action="append")
    p.add_argument("--path")
    p.add_argument("--case", action="store_true")
    p.add_argument("--body", action="store_true", help="print the source of the definition")
    p.add_argument("--context", type=int, default=20, help="lines to show when the end is unknown")
    p.add_argument("--max-body", type=int, default=400, help="cap on body lines")

    p = add("grep", cmd_grep, "search source lines (full-text by default)")
    p.add_argument("query")
    p.add_argument("--regex", action="store_true", help="treat the query as a regex")
    p.add_argument("--phrase", action="store_true", help="match the words as an exact phrase")
    p.add_argument("--case", action="store_true", help="case sensitive (regex mode only)")
    p.add_argument("--path")
    p.add_argument("--category", action="append",
                   help="cpp, python, ui, shader, gpgim, resource, build, doc, data")

    p = add("refs", cmd_refs, "definitions plus other occurrences of an identifier")
    p.add_argument("name")
    p.add_argument("--path")

    p = add("file", cmd_file, "file outline, or its text with --cat/--range")
    p.add_argument("path")
    p.add_argument("--cat", action="store_true", help="print the whole file")
    p.add_argument("--range", help="print a line range, e.g. 120-180")
    p.add_argument("--first", action="store_true", help="use the first match when ambiguous")

    p = add("tree", cmd_tree, "directory map with file and line counts")
    p.add_argument("prefix", nargs="?", default="")
    p.add_argument("--depth", type=int, default=1)

    p = add("includes", cmd_includes, "include graph for a file")
    p.add_argument("path")
    p.add_argument("--by", action="store_true", help="list files that include this one instead")

    p = add("decl", cmd_decl, "declarations and definitions of a type/member/variable/macro")
    p.add_argument("name")
    p.add_argument("--mode", choices=("auto",) + MODES, default="auto")
    p.add_argument("--kind", action="append", help="class, method, field, macro, ...")
    p.add_argument("--path")
    p.add_argument("--case", action="store_true")

    p = add("uses", cmd_uses, "resolved usages of an entity, by syntactic role")
    p.add_argument("name")
    p.add_argument("--mode", choices=("auto",) + MODES, default="auto")
    p.add_argument("--kind", action="append")
    p.add_argument("--role", action="append", choices=USE_ROLES,
                   help="call, read, write, member, type, base, template_arg")
    p.add_argument("--path")
    p.add_argument("--case", action="store_true")
    p.add_argument("--exclude-decl", action="store_true",
                   help="hide the declaration and definition sites")
    p.add_argument("--context-symbol", action="store_true",
                   help="append the enclosing function to each line")

    p = add("hier", cmd_hier, "base classes and subclasses, transitively")
    p.add_argument("name")
    p.add_argument("--mode", choices=("auto",) + MODES, default="auto")
    p.add_argument("--kind", action="append")
    p.add_argument("--path")
    p.add_argument("--case", action="store_true")
    p.add_argument("--up", action="store_true", help="only base classes")
    p.add_argument("--down", action="store_true", help="only subclasses")
    p.add_argument("--depth", type=int, default=99, help="max inheritance depth")

    p = add("members", cmd_members, "members of a class, struct, enum or namespace")
    p.add_argument("name")
    p.add_argument("--mode", choices=("auto",) + MODES, default="auto")
    p.add_argument("--kind", action="append", help="field, method, typedef, enumerator, ...")
    p.add_argument("--access", choices=("public", "protected", "private"))
    p.add_argument("--inherited", action="store_true", help="include inherited members")
    p.add_argument("--path")
    p.add_argument("--case", action="store_true")

    p = add("macro", cmd_macro, "preprocessor symbols and their uses")
    p.add_argument("name", nargs="?", default="")
    p.add_argument("--uses", action="store_true", help="list use sites too")

    p = add("hier-ctags", cmd_hier_legacy, "inheritance from the ctags index (fallback)")
    p.add_argument("name")

    p = add("ui", cmd_ui, "Qt Designer forms and widgets")
    p.add_argument("name", nargs="?", default="")

    p = add("signals", cmd_signals, "Qt signal/slot connections mentioning a name")
    p.add_argument("name")

    p = add("pyapi", cmd_pyapi, "Python API exposed from C++ via Boost.Python")
    p.add_argument("name", nargs="?", default="")

    p = add("gpgim", cmd_gpgim, "GPGIM feature classes and properties")
    p.add_argument("name", nargs="?", default="")
    p.add_argument("--detail", action="store_true", help="include descriptions and property lists")

    p = add("community", cmd_community, "code communities (clusters) from the graph")
    p.add_argument("name", nargs="?", default="")
    p.add_argument("--id", type=int, help="show one community by id")
    p.add_argument("--list", action="store_true", help="list communities by size")
    p.add_argument("--case", action="store_true")

    p = add("neighbors", cmd_neighbors, "graph edges into and out of a symbol")
    p.add_argument("name")
    p.add_argument("--relation", action="append",
                   help="calls, references, inherits, contains, defines, imports, method")
    p.add_argument("--nodes", type=int, default=2,
                   help="how many same-named nodes to expand (default 2)")
    p.add_argument("--case", action="store_true")

    p = add("sql", cmd_sql, "run a read-only SQL query against the index")
    p.add_argument("query")

    return ap


def main(argv=None):
    global _json_mode
    args = build_parser().parse_args(argv)
    _json_mode = args.json
    try:
        con = open_db()
    except SkillError as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 2
    try:
        rc = args.func(con, args)
    except SkillError as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 2
    except Exception as exc:  # noqa: BLE001 - CLI boundary
        print("error: %s: %s" % (type(exc).__name__, exc), file=sys.stderr)
        return 3
    finally:
        con.close()
    flush()
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
