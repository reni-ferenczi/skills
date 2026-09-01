"""Turn a parsed C++ translation unit into entities, bases and occurrences.

Two walks per file:

* `extract_entities` follows the declaration structure — namespaces, classes,
  templates, methods, fields, variables, typedefs, enums, macros — building a
  lexical container stack so every entity gets a qualified name and a line range.
* `extract_occurrences` is a flat scan that records every identifier token with
  the syntactic *role* it plays (call, member access, type use, write, base
  reference, template argument, ...).

Nothing here resolves names; that is `resolve.py`'s job.
"""

from __future__ import annotations

# Entity kinds -------------------------------------------------------------
CONTAINER_KINDS = {"namespace", "class", "struct", "union", "enum"}
TYPE_KINDS = {"class", "struct", "union", "enum", "typedef", "alias", "template_param"}
CALLABLE_KINDS = {"function", "method", "constructor", "destructor", "operator"}
VALUE_KINDS = {"field", "variable", "parameter", "local", "enumerator"}
MACRO_KINDS = {"macro", "macro_function"}

# Nodes that name something ------------------------------------------------
NAME_NODES = {"identifier", "type_identifier", "field_identifier",
              "namespace_identifier", "destructor_name", "operator_name",
              "primitive_type", "statement_identifier"}

_DECLARATOR_CHAIN = {
    "pointer_declarator", "reference_declarator", "array_declarator",
    "parenthesized_declarator", "init_declarator", "function_declarator",
    "abstract_pointer_declarator", "attributed_declarator",
}


def _text(data, node):
    return data[node.start_byte:node.end_byte].decode("utf-8", "replace")


def _pos(node):
    return node.start_point[0] + 1, node.start_point[1] + 1


def _field(node, name):
    return node.child_by_field_name(name)


def _squash(s):
    return " ".join(s.split())


def _declarator_name(data, node):
    """Peel a declarator chain down to the node that actually carries the name."""
    seen = 0
    while node is not None and seen < 12:
        seen += 1
        if node.type in NAME_NODES:
            return node
        if node.type == "qualified_identifier":
            inner = _field(node, "name")
            node = inner if inner is not None else None
            continue
        if node.type == "template_function":
            node = _field(node, "name")
            continue
        if node.type in _DECLARATOR_CHAIN:
            node = _field(node, "declarator") or (node.children[-1] if node.children else None)
            continue
        return None
    return None


def _qualified_prefix(data, node):
    """`Cache::size` -> `Cache` — the explicit scope written at a definition site."""
    parts = []
    cur = node
    while cur is not None and cur.type == "qualified_identifier":
        scope = _field(cur, "scope")
        if scope is None:
            break
        parts.append(_text(data, scope))
        cur = _field(cur, "name")
    return parts


class Sink:
    """Collects rows; kept separate so the walkers stay easy to test."""

    def __init__(self):
        self.entities = []      # dicts
        self.bases = []         # (entity_index, base_name, access, is_virtual)
        self.occurrences = []   # (line, col, name, role)

    def add_entity(self, **row):
        self.entities.append(row)
        return len(self.entities) - 1


# ---------------------------------------------------------------------------
# Declarations
# ---------------------------------------------------------------------------

def extract_entities(data: bytes, tree, sink: Sink):
    _walk_decls(data, tree.root_node, sink, container=None, scope=[], access=None)


def _walk_decls(data, node, sink, container, scope, access,
                template_params=None, storage=None):
    for child in node.children:
        _handle_decl(data, child, sink, container, scope, access,
                     template_params, storage)


def _handle_decl(data, node, sink, container, scope, access,
                 template_params=None, storage=None):
    t = node.type

    if t == "namespace_definition":
        name_node = _field(node, "name")
        name = _text(data, name_node) if name_node is not None else "(anonymous)"
        idx = _emit(sink, name, "namespace", node, scope, container, is_def=True)
        body = _field(node, "body")
        if body is not None:
            _walk_decls(data, body, sink, idx, scope + [name], None)
        return

    if t in ("class_specifier", "struct_specifier", "union_specifier"):
        _handle_class(data, node, sink, container, scope, access, template_params)
        return

    if t == "enum_specifier":
        _handle_enum(data, node, sink, container, scope, access)
        return

    if t == "template_declaration":
        params = _field(node, "parameters")
        ptext = _squash(_text(data, params)) if params is not None else ""
        for child in node.children:
            if child.type in ("template_parameter_list", "template"):
                continue
            _handle_decl(data, child, sink, container, scope, access,
                         template_params=ptext, storage=storage)
        return

    if t == "function_definition":
        _handle_function(data, node, sink, container, scope, access,
                         template_params, is_def=True)
        return

    if t in ("declaration", "field_declaration"):
        _handle_declaration(data, node, sink, container, scope, access,
                            template_params, in_class=(t == "field_declaration"))
        return

    if t == "type_definition":
        type_node = _field(node, "type")
        for decl in node.children:
            if type_node is not None and decl.id == type_node.id:
                continue
            nn = _declarator_name(data, decl)
            if nn is not None and nn.type in ("type_identifier", "identifier"):
                _emit(sink, _text(data, nn), "typedef", node, scope, container,
                      is_def=True, type_text=_squash(_text(data, type_node)) if type_node else None,
                      access=access)
        return

    if t == "alias_declaration":
        nn = _field(node, "name")
        tn = _field(node, "type")
        if nn is not None:
            _emit(sink, _text(data, nn), "alias", node, scope, container, is_def=True,
                  type_text=_squash(_text(data, tn)) if tn is not None else None,
                  access=access, template_params=template_params)
        return

    if t in ("preproc_def", "preproc_function_def"):
        nn = _field(node, "name")
        if nn is not None:
            body = _field(node, "value")
            params = _field(node, "parameters")
            _emit(sink, _text(data, nn),
                  "macro_function" if t == "preproc_function_def" else "macro",
                  node, [], None, is_def=True,
                  signature=_squash(_text(data, params)) if params is not None else None,
                  type_text=_squash(_text(data, body))[:400] if body is not None else None)
        return

    if t == "using_declaration":
        nn = _declarator_name(data, node.children[-1] if node.children else None)
        if nn is not None:
            _emit(sink, _text(data, nn), "using", node, scope, container, is_def=False,
                  type_text=_squash(_text(data, node)), access=access)
        return

    if t == "access_specifier":
        return

    # Recurse into anything that can still hold declarations.
    if t in ("translation_unit", "declaration_list", "field_declaration_list",
             "linkage_specification", "compound_statement", "preproc_ifdef",
             "preproc_if", "preproc_else", "preproc_elif", "extern"):
        _walk_decls(data, node, sink, container, scope, access)


def _handle_class(data, node, sink, container, scope, access, template_params):
    name_node = _field(node, "name")
    name = _text(data, name_node) if name_node is not None else "(anonymous)"
    kind = {"class_specifier": "class", "struct_specifier": "struct",
            "union_specifier": "union"}[node.type]
    body = _field(node, "body")
    idx = _emit(sink, name, kind, node, scope, container,
                is_def=body is not None, access=access, template_params=template_params)

    clause = None
    for child in node.children:
        if child.type == "base_class_clause":
            clause = child
            break
    if clause is not None:
        cur_access = "private" if kind == "class" else "public"
        virtual = False
        for child in clause.children:
            if child.type == "access_specifier":
                cur_access = _text(data, child)
            elif child.type == "virtual":
                virtual = True
            elif child.type in ("type_identifier", "qualified_identifier",
                                "template_type", "dependent_type"):
                sink.bases.append((idx, _squash(_text(data, child)), cur_access, virtual))
                virtual = False
    if body is not None:
        default_access = "private" if kind == "class" else "public"
        _walk_class_body(data, body, sink, idx, scope + [name], default_access)


def _walk_class_body(data, body, sink, container, scope, access):
    cur = access
    for child in body.children:
        if child.type == "access_specifier":
            cur = _text(data, child)
            continue
        _handle_decl(data, child, sink, container, scope, cur)


def _handle_enum(data, node, sink, container, scope, access):
    name_node = _field(node, "name")
    name = _text(data, name_node) if name_node is not None else "(anonymous enum)"
    idx = _emit(sink, name, "enum", node, scope, container, is_def=True, access=access)
    body = _field(node, "body")
    if body is None:
        return
    inner = scope + ([name] if name_node is not None else [])
    for child in body.children:
        if child.type == "enumerator":
            nn = _field(child, "name")
            if nn is not None:
                _emit(sink, _text(data, nn), "enumerator", child, inner, idx,
                      is_def=True, access=access)


def _handle_function(data, node, sink, container, scope, access,
                     template_params, is_def):
    # A class/struct/enum can appear as the *type* of a function definition, both
    # legitimately (`struct S {...} f();`) and when tree-sitter's error recovery
    # mis-nests a namespace-level class under a bogus function_definition — which
    # is what happens to GPlatesScribe::Scribe. Extract it either way.
    type_node = _field(node, "type")
    if type_node is not None and type_node.type in (
            "class_specifier", "struct_specifier", "union_specifier", "enum_specifier"):
        _handle_decl(data, type_node, sink, container, scope, access)

    declarator = _field(node, "declarator")
    if declarator is None:
        return
    fdecl = declarator
    hops = 0
    while fdecl is not None and fdecl.type != "function_declarator" and hops < 8:
        hops += 1
        fdecl = _field(fdecl, "declarator")
    if fdecl is None:
        return
    inner = _field(fdecl, "declarator")
    name_node = _declarator_name(data, inner)
    if name_node is None:
        return
    name = _text(data, name_node)
    extra_scope = _qualified_prefix(data, inner) if inner is not None else []

    kind = "function"
    bare = name.lstrip("~")
    if name.startswith("~") or (inner is not None and inner.type == "destructor_name"):
        kind = "destructor"
    elif name.startswith("operator"):
        kind = "operator"
    elif container is not None and sink.entities[container]["kind"] in ("class", "struct", "union"):
        kind = "constructor" if bare == sink.entities[container]["name"] else "method"
    elif extra_scope and bare == extra_scope[-1]:
        kind = "constructor"
    elif extra_scope:
        kind = "method"

    params = _field(fdecl, "parameters")
    ret = _field(node, "type")
    idx = _emit(sink, name, kind, node, scope + extra_scope, container,
                is_def=is_def, access=access, template_params=template_params,
                signature=_squash(_text(data, params)) if params is not None else "()",
                type_text=_squash(_text(data, ret)) if ret is not None else None)

    if params is not None:
        for p in params.children:
            if p.type in ("parameter_declaration", "optional_parameter_declaration"):
                pn = _declarator_name(data, _field(p, "declarator"))
                pt = _field(p, "type")
                if pn is not None:
                    _emit(sink, _text(data, pn), "parameter", p, scope + extra_scope, idx,
                          is_def=True,
                          type_text=_squash(_text(data, pt)) if pt is not None else None)
    body = _field(node, "body")
    if body is not None:
        _collect_locals(data, body, sink, idx, scope + extra_scope)


def _collect_locals(data, body, sink, container, scope):
    """Locals inside a function body, plus any types declared there.

    Types matter more than they look: C++ allows local classes, and tree-sitter's
    error recovery sometimes mis-nests a whole namespace-level class under a
    `function_definition` (GPlatesScribe::Scribe is one). Without this, such a
    class would be missing from the index entirely.
    """
    stack = list(body.children)
    while stack:
        n = stack.pop()
        if n.type in ("class_specifier", "struct_specifier", "union_specifier"):
            _handle_class(data, n, sink, container, scope, None, None)
            continue
        if n.type == "enum_specifier":
            _handle_enum(data, n, sink, container, scope, None)
            continue
        if n.type == "declaration":
            tn = _field(n, "type")
            if tn is not None and tn.type in ("class_specifier", "struct_specifier",
                                              "union_specifier", "enum_specifier"):
                _handle_decl(data, tn, sink, container, scope, None)
            for child in n.children:
                if tn is not None and child.id == tn.id:
                    continue
                nn = _declarator_name(data, child)
                if nn is not None and nn.type == "identifier":
                    _emit(sink, _text(data, nn), "local", nn, scope, container, is_def=True,
                          type_text=_squash(_text(data, tn)) if tn is not None else None)
        elif n.type in ("compound_statement", "for_statement", "if_statement",
                        "while_statement", "do_statement", "switch_statement",
                        "try_statement", "catch_clause", "case_statement",
                        "for_range_loop", "declaration_list", "template_declaration"):
            stack.extend(n.children)


def _handle_declaration(data, node, sink, container, scope, access,
                        template_params, in_class):
    type_node = _field(node, "type")
    type_text = _squash(_text(data, type_node)) if type_node is not None else None
    storage = None
    for child in node.children:
        if child.type == "storage_class_specifier":
            storage = _text(data, child)

    # A nested class/struct/enum used as the declaration's type.
    if type_node is not None and type_node.type in (
            "class_specifier", "struct_specifier", "union_specifier", "enum_specifier"):
        _handle_decl(data, type_node, sink, container, scope, access)

    for child in node.children:
        if (type_node is not None and child.id == type_node.id) or child.type in (
                "storage_class_specifier", "type_qualifier", "access_specifier",
                "virtual", "explicit_function_specifier", ";"):
            continue
        # function prototype?
        fdecl = child
        hops = 0
        while fdecl is not None and fdecl.type != "function_declarator" and hops < 6:
            hops += 1
            nxt = _field(fdecl, "declarator")
            if nxt is None:
                break
            fdecl = nxt
        if fdecl is not None and fdecl.type == "function_declarator":
            _handle_function(data, node, sink, container, scope, access,
                             template_params, is_def=False)
            return
        nn = _declarator_name(data, child)
        if nn is None:
            continue
        kind = "field" if in_class else "variable"
        if storage == "static" and in_class:
            kind = "field"
        _emit(sink, _text(data, nn), kind, node, scope, container, is_def=True,
              type_text=type_text, access=access, storage=storage,
              template_params=template_params)


def _emit(sink, name, kind, node, scope, container, is_def,
          type_text=None, signature=None, access=None, storage=None,
          template_params=None):
    line, col = _pos(node)
    qname = "::".join([s for s in scope if s] + [name]) if scope else name
    return sink.add_entity(
        name=name, qname=qname, kind=kind, line=line, col=col,
        end_line=node.end_point[0] + 1, parent=container, is_def=1 if is_def else 0,
        type_text=(type_text or None), signature=signature, access=access,
        storage=storage, template_params=template_params,
        is_template=1 if template_params else 0)


# ---------------------------------------------------------------------------
# Occurrences
# ---------------------------------------------------------------------------

def extract_occurrences(data: bytes, tree, sink: Sink, known_names):
    """Record identifier tokens whose name is a known entity somewhere in the tree."""
    stack = [tree.root_node]
    while stack:
        node = stack.pop()
        children = node.children
        if children:
            stack.extend(children)
        if node.type not in NAME_NODES or node.type == "primitive_type":
            continue
        name = _text(data, node)
        if name not in known_names:
            continue
        role = _role_of(node)
        if role is None:
            continue
        line, col = _pos(node)
        sink.occurrences.append((line, col, name, role))


def _ancestor_is(node, types, max_up=4):
    """True when one of the nearest `max_up` ancestors has one of `types`."""
    cur = node.parent
    for _ in range(max_up):
        if cur is None:
            return False
        if cur.type in types:
            return True
        cur = cur.parent
    return False


def _role_of(node):
    parent = node.parent
    if parent is None:
        return "read"
    ptype = parent.type
    field = None
    for i, child in enumerate(parent.children):
        if child.id == node.id:
            field = parent.field_name_for_child(i)
            break

    if ptype in ("preproc_def", "preproc_function_def") and field == "name":
        return "def"
    if ptype == "call_expression" and field == "function":
        return "call"
    if ptype == "field_expression" and field == "field":
        gp = parent.parent
        if gp is not None:
            gp_fn = gp.child_by_field_name("function")
            gp_lhs = gp.child_by_field_name("left")
            if gp.type == "call_expression" and gp_fn is not None and gp_fn.id == parent.id:
                return "call"
            if gp.type == "assignment_expression" and gp_lhs is not None \
                    and gp_lhs.id == parent.id:
                return "member_write"
        return "member"
    if ptype == "assignment_expression" and field == "left":
        return "write"
    if ptype in ("update_expression",):
        return "write"
    if ptype == "base_class_clause" or _ancestor_is(node, {"base_class_clause"}, 3):
        return "base"
    if ptype == "template_argument_list" or _ancestor_is(node, {"template_argument_list"}, 3):
        return "template_arg"
    if ptype == "namespace_definition" and field == "name":
        return "def"
    if ptype == "enumerator" and field == "name":
        return "def"
    if node.type == "namespace_identifier":
        return "ns"
    if node.type == "type_identifier":
        if ptype in ("class_specifier", "struct_specifier", "union_specifier",
                     "enum_specifier") and field == "name":
            return "def"
        if ptype == "alias_declaration" and field == "name":
            return "def"
        return "type"
    if node.type == "field_identifier":
        if ptype in ("field_declaration", "function_declarator"):
            return "decl"
        return "member"
    if ptype == "qualified_identifier":
        return "read"
    if ptype in ("function_declarator", "init_declarator", "parameter_declaration",
                 "pointer_declarator", "reference_declarator", "array_declarator"):
        return "decl"
    if ptype == "new_expression":
        return "type"
    if ptype == "sizeof_expression":
        return "type"
    return "read"
