"""Bind occurrences and base-class references to the entities they name.

There is no compiler here, so resolution is scope-and-reachability based and
every result carries an honest confidence label:

    local      the target is a parameter/local of the enclosing function
    member     the target is a member of the enclosing class
    file       the only candidate declared in this same file
    unique     the name is declared exactly once in the whole tree
    include    the only candidate reachable through this file's #includes
    namespace  the only candidate sharing the file's dominant namespace
    ambiguous  several equally plausible candidates; entity_id is left NULL

`ambiguous` occurrences are still stored, so a name-based search finds them —
they simply do not claim a specific target.
"""

from __future__ import annotations

import re
from collections import defaultdict

# Kinds that can be named from another file at all.
_GLOBAL_KINDS = {"namespace", "class", "struct", "union", "enum", "enumerator",
                 "typedef", "alias", "using", "function", "method", "constructor",
                 "destructor", "operator", "field", "variable",
                 "macro", "macro_function"}
_SCOPED_KINDS = {"parameter", "local"}

_TEMPLATE_ARGS = re.compile(r"<.*>$", re.S)


def base_key(text: str) -> str:
    """`GPlatesUtils::ReferenceCount<Foo>` -> `ReferenceCount`."""
    text = text.strip()
    text = _TEMPLATE_ARGS.sub("", text).strip()
    if "::" in text:
        text = text.rsplit("::", 1)[-1]
    return text.strip()


def resolve_bases(con, log=lambda _m: None):
    """Point bases.base_entity_id at a real class/struct entity where possible."""
    by_key = defaultdict(list)
    for eid, name, kind in con.execute(
            "SELECT id, name, kind FROM entities "
            "WHERE kind IN ('class','struct','union','typedef','alias') AND is_def = 1"):
        by_key[name].append(eid)

    updates = []
    for rowid, entity_id, key in con.execute(
            "SELECT rowid, entity_id, base_key FROM bases"):
        cands = by_key.get(key)
        if not cands:
            continue
        if len(cands) == 1:
            updates.append((cands[0], rowid))
            continue
        # Several classes share the name: prefer one in the same file, then any.
        same_file = con.execute(
            "SELECT e.id FROM entities e "
            "WHERE e.id IN (%s) AND e.file_id = "
            "  (SELECT file_id FROM entities WHERE id = ?) LIMIT 1"
            % ",".join(str(c) for c in cands), (entity_id,)).fetchone()
        updates.append((same_file[0] if same_file else cands[0], rowid))
    con.executemany("UPDATE bases SET base_entity_id = ? WHERE rowid = ?", updates)
    con.commit()
    log("  resolved %d/%d base references"
        % (len(updates), con.execute("SELECT COUNT(*) FROM bases").fetchone()[0]))


def build_closure(con, log=lambda _m: None, max_depth=12):
    """Transitive inheritance: every (ancestor, descendant, depth) pair."""
    parents = defaultdict(set)
    for child, parent in con.execute(
            "SELECT entity_id, base_entity_id FROM bases WHERE base_entity_id IS NOT NULL"):
        if child != parent:
            parents[child].add(parent)

    rows = []
    for start in parents:
        seen = {start}
        frontier = {start}
        for depth in range(1, max_depth + 1):
            nxt = set()
            for node in frontier:
                nxt |= parents.get(node, set())
            nxt -= seen
            if not nxt:
                break
            for anc in nxt:
                rows.append((anc, start, depth))
            seen |= nxt
            frontier = nxt
    con.executemany(
        "INSERT INTO inherit_closure(ancestor_id, descendant_id, depth) VALUES (?,?,?)",
        rows)
    con.commit()
    log("  %d inheritance closure edges" % len(rows))


def resolve_occurrences(con, log=lambda _m: None):
    """Assign occurrences.entity_id / confidence."""
    # name -> candidates, split by how far they are visible.
    globals_by_name = defaultdict(list)   # name -> [(eid, file_id, kind, parent_id)]
    scoped_by_name = defaultdict(list)    # name -> [(eid, file_id, parent_id, lo, hi)]
    ent_span = {}                         # eid -> (file_id, line, end_line)
    for eid, name, kind, file_id, line, end_line, parent_id in con.execute(
            "SELECT id, name, kind, file_id, line, end_line, parent_id FROM entities"):
        ent_span[eid] = (file_id, line, end_line or line)
        if kind in _SCOPED_KINDS:
            scoped_by_name[name].append((eid, file_id, parent_id))
        elif kind in _GLOBAL_KINDS:
            globals_by_name[name].append((eid, file_id, kind, parent_id))

    # file -> directly included files, for reachability.
    included = defaultdict(set)
    for f, t in con.execute(
            "SELECT file_id, target_id FROM includes WHERE target_id IS NOT NULL"):
        included[f].add(t)
    # one extra hop: a header's own includes count as reachable
    for f in list(included):
        extra = set()
        for t in included[f]:
            extra |= included.get(t, set())
        included[f] |= extra

    # Members of a class, so `d_items` inside a method binds to the class field.
    members_of = defaultdict(dict)        # class_eid -> {name: eid}
    for eid, name, parent_id in con.execute(
            "SELECT id, name, parent_id FROM entities "
            "WHERE kind IN ('field','method','constructor','destructor','operator',"
            "'typedef','alias','enumerator') AND parent_id IS NOT NULL"):
        members_of[parent_id].setdefault(name, eid)

    parent_of = dict(con.execute(
        "SELECT id, parent_id FROM entities WHERE parent_id IS NOT NULL"))

    updates = []
    stats = defaultdict(int)
    for oid, file_id, line, name, container_id in con.execute(
            "SELECT id, file_id, line, name, container_id FROM occurrences"):
        eid, conf = _resolve_one(name, file_id, line, container_id,
                                 globals_by_name, scoped_by_name, ent_span,
                                 included, members_of, parent_of)
        stats[conf] += 1
        updates.append((eid, conf, oid))
        if len(updates) >= 100000:
            con.executemany(
                "UPDATE occurrences SET entity_id = ?, confidence = ? WHERE id = ?", updates)
            updates = []
    if updates:
        con.executemany(
            "UPDATE occurrences SET entity_id = ?, confidence = ? WHERE id = ?", updates)
    con.commit()
    total = sum(stats.values()) or 1
    resolved = total - stats["ambiguous"] - stats["unknown"]
    log("  resolved %d/%d occurrences (%.1f%%): %s"
        % (resolved, total, 100.0 * resolved / total,
           ", ".join("%s=%d" % kv for kv in sorted(stats.items()))))
    return dict(stats)


def _resolve_one(name, file_id, line, container_id,
                 globals_by_name, scoped_by_name, ent_span,
                 included, members_of, parent_of):
    # 1. a parameter or local of the enclosing function
    if container_id is not None:
        for eid, f, parent in scoped_by_name.get(name, ()):
            if parent == container_id:
                return eid, "local"
        # 2. a member of the enclosing class (walk out through nested scopes)
        owner = parent_of.get(container_id)
        hops = 0
        while owner is not None and hops < 6:
            hops += 1
            hit = members_of.get(owner, {}).get(name)
            if hit is not None:
                return hit, "member"
            owner = parent_of.get(owner)

    cands = globals_by_name.get(name)
    if not cands:
        return None, "unknown"
    if len(cands) == 1:
        return cands[0][0], "unique"

    # 3. declared in this very file
    same_file = [c for c in cands if c[1] == file_id]
    if len(same_file) == 1:
        return same_file[0][0], "file"
    if same_file:
        # prefer a definition that lexically contains this line
        containing = [c for c in same_file
                      if ent_span[c[0]][1] <= line <= ent_span[c[0]][2]]
        if len(containing) == 1:
            return containing[0][0], "file"
        return same_file[0][0], "file"

    # 4. reachable through the include graph
    reach = included.get(file_id, ())
    via = [c for c in cands if c[1] in reach]
    if len(via) == 1:
        return via[0][0], "include"
    if via:
        return via[0][0], "include"

    return None, "ambiguous"
