"""SQLite schema for the GPlates code index."""

SCHEMA = r"""
PRAGMA journal_mode = OFF;
PRAGMA synchronous = OFF;

CREATE TABLE meta (
    key   TEXT PRIMARY KEY,
    value TEXT
);

CREATE TABLE files (
    id       INTEGER PRIMARY KEY,
    path     TEXT NOT NULL UNIQUE,   -- forward-slash path relative to the source root
    dir      TEXT NOT NULL,
    name     TEXT NOT NULL,
    ext      TEXT NOT NULL,          -- lower case, with dot; '' when none
    category TEXT NOT NULL,          -- cpp|python|ui|shader|gpgim|resource|build|doc|data|other
    size     INTEGER NOT NULL,
    lines    INTEGER NOT NULL,       -- 0 when the content was not indexed
    has_text INTEGER NOT NULL        -- 1 when per-line content is stored
);
CREATE INDEX idx_files_dir ON files(dir);
CREATE INDEX idx_files_cat ON files(category);
CREATE INDEX idx_files_name ON files(name);

CREATE TABLE symbols (
    id         INTEGER PRIMARY KEY,
    name       TEXT NOT NULL,
    name_lc    TEXT NOT NULL,
    kind       TEXT NOT NULL,
    lang       TEXT,
    file_id    INTEGER NOT NULL REFERENCES files(id),
    line       INTEGER NOT NULL,
    end_line   INTEGER,
    scope      TEXT,                 -- enclosing namespace/class, '::'-joined
    scope_kind TEXT,
    signature  TEXT,
    typeref    TEXT,                 -- return / declared type
    access     TEXT,
    inherits   TEXT,                 -- comma separated base classes
    is_def     INTEGER NOT NULL      -- 1 = definition, 0 = declaration/prototype
);
CREATE INDEX idx_sym_name ON symbols(name);
CREATE INDEX idx_sym_name_lc ON symbols(name_lc);
CREATE INDEX idx_sym_file ON symbols(file_id, line);
CREATE INDEX idx_sym_kind ON symbols(kind);
CREATE INDEX idx_sym_scope ON symbols(scope);

CREATE TABLE includes (
    file_id   INTEGER NOT NULL REFERENCES files(id),
    line      INTEGER NOT NULL,
    header    TEXT NOT NULL,         -- text between the <> or ""
    is_system INTEGER NOT NULL,
    target_id INTEGER                -- resolved files.id when the header is in-tree
);
CREATE INDEX idx_inc_file ON includes(file_id);
CREATE INDEX idx_inc_header ON includes(header);
CREATE INDEX idx_inc_target ON includes(target_id);

CREATE TABLE lines (
    id      INTEGER PRIMARY KEY,
    file_id INTEGER NOT NULL REFERENCES files(id),
    line    INTEGER NOT NULL,
    text    TEXT NOT NULL
);
CREATE INDEX idx_lines_file ON lines(file_id, line);

CREATE VIRTUAL TABLE lines_fts USING fts5(
    text,
    content='lines',
    content_rowid='id',
    tokenize="unicode61 tokenchars '_'"
);

CREATE TABLE ui_forms (
    file_id    INTEGER NOT NULL REFERENCES files(id),
    class_name TEXT NOT NULL,        -- <class> of the form, e.g. AboutDialog
    base_class TEXT,                 -- widget class of the root widget, e.g. QDialog
    title      TEXT
);
CREATE INDEX idx_uiform_class ON ui_forms(class_name);

CREATE TABLE ui_widgets (
    file_id     INTEGER NOT NULL REFERENCES files(id),
    form        TEXT NOT NULL,
    widget_class TEXT NOT NULL,      -- QPushButton, GPlatesQtWidgets::..., ...
    object_name TEXT NOT NULL,
    text        TEXT                 -- visible label / title when present
);
CREATE INDEX idx_uiwidget_obj ON ui_widgets(object_name);
CREATE INDEX idx_uiwidget_class ON ui_widgets(widget_class);
CREATE INDEX idx_uiwidget_form ON ui_widgets(form);

CREATE TABLE qt_connections (
    file_id  INTEGER NOT NULL REFERENCES files(id),
    line     INTEGER NOT NULL,
    sender   TEXT,
    signal   TEXT,
    receiver TEXT,
    slot     TEXT
);
CREATE INDEX idx_conn_signal ON qt_connections(signal);
CREATE INDEX idx_conn_slot ON qt_connections(slot);
CREATE INDEX idx_conn_file ON qt_connections(file_id);

CREATE TABLE py_api (
    file_id   INTEGER NOT NULL REFERENCES files(id),
    line      INTEGER NOT NULL,
    owner     TEXT,                  -- python class the member belongs to, '' for module level
    name      TEXT NOT NULL,         -- python-visible name
    kind      TEXT NOT NULL,         -- class|enum|function|method|attribute|enum_value
    cpp_type  TEXT                   -- C++ type/function it is bound to, when detectable
);
CREATE INDEX idx_pyapi_name ON py_api(name);
CREATE INDEX idx_pyapi_owner ON py_api(owner);

CREATE TABLE gpgim_features (
    file_id          INTEGER NOT NULL REFERENCES files(id),
    line             INTEGER NOT NULL,
    name             TEXT NOT NULL,  -- e.g. gpml:Isochron
    class_type       TEXT,           -- concrete / abstract
    inherits         TEXT,
    description      TEXT,
    default_geometry TEXT
);
CREATE INDEX idx_gpgimf_name ON gpgim_features(name);

CREATE TABLE gpgim_properties (
    file_id      INTEGER NOT NULL REFERENCES files(id),
    line         INTEGER NOT NULL,
    name         TEXT NOT NULL,      -- e.g. gpml:reconstructionPlateId
    types        TEXT,               -- comma separated property value types
    multiplicity TEXT,
    description  TEXT
);
CREATE INDEX idx_gpgimp_name ON gpgim_properties(name);

CREATE TABLE gpgim_feature_properties (
    feature  TEXT NOT NULL,
    property TEXT NOT NULL
);
CREATE INDEX idx_gpgimfp_feature ON gpgim_feature_properties(feature);
CREATE INDEX idx_gpgimfp_prop ON gpgim_feature_properties(property);

CREATE TABLE entities (
    id              INTEGER PRIMARY KEY,
    name            TEXT NOT NULL,
    name_lc         TEXT NOT NULL,
    qname           TEXT NOT NULL,      -- namespace/class qualified, '::' joined
    kind            TEXT NOT NULL,      -- namespace|class|struct|union|enum|enumerator|
                                        -- typedef|alias|using|function|method|constructor|
                                        -- destructor|operator|field|variable|parameter|
                                        -- local|macro|macro_function
    file_id         INTEGER NOT NULL REFERENCES files(id),
    line            INTEGER NOT NULL,
    col             INTEGER,
    end_line        INTEGER,
    parent_id       INTEGER REFERENCES entities(id),   -- lexical container
    type_text       TEXT,               -- declared/return type, or macro body
    signature       TEXT,
    access          TEXT,               -- public|protected|private
    storage         TEXT,               -- static|extern|mutable...
    is_def          INTEGER NOT NULL,   -- 0 = declaration only
    is_template     INTEGER NOT NULL,
    template_params TEXT
);
CREATE INDEX idx_ent_name ON entities(name_lc);
CREATE INDEX idx_ent_qname ON entities(qname);
CREATE INDEX idx_ent_kind ON entities(kind);
CREATE INDEX idx_ent_file ON entities(file_id, line);
CREATE INDEX idx_ent_parent ON entities(parent_id);

CREATE TABLE bases (
    entity_id      INTEGER NOT NULL REFERENCES entities(id),
    base_name      TEXT NOT NULL,       -- exactly as written, e.g. Base<T>
    base_key       TEXT NOT NULL,       -- normalised: template args and scope stripped
    base_entity_id INTEGER REFERENCES entities(id),
    access         TEXT,
    is_virtual     INTEGER NOT NULL
);
CREATE INDEX idx_bases_entity ON bases(entity_id);
CREATE INDEX idx_bases_key ON bases(base_key);
CREATE INDEX idx_bases_target ON bases(base_entity_id);

CREATE TABLE inherit_closure (
    ancestor_id   INTEGER NOT NULL REFERENCES entities(id),
    descendant_id INTEGER NOT NULL REFERENCES entities(id),
    depth         INTEGER NOT NULL
);
CREATE INDEX idx_closure_anc ON inherit_closure(ancestor_id, depth);
CREATE INDEX idx_closure_desc ON inherit_closure(descendant_id, depth);

CREATE TABLE occurrences (
    id           INTEGER PRIMARY KEY,
    file_id      INTEGER NOT NULL REFERENCES files(id),
    line         INTEGER NOT NULL,
    col          INTEGER,
    name         TEXT NOT NULL,
    name_lc      TEXT NOT NULL,
    role         TEXT NOT NULL,         -- def|decl|call|read|write|member|member_write|
                                        -- type|base|template_arg|ns
    container_id INTEGER REFERENCES entities(id),   -- enclosing function/method
    entity_id    INTEGER REFERENCES entities(id),   -- resolved target, NULL if ambiguous
    confidence   TEXT                   -- local|file|unique|include|namespace|ambiguous
);
CREATE INDEX idx_occ_name ON occurrences(name_lc);
CREATE INDEX idx_occ_entity ON occurrences(entity_id);
CREATE INDEX idx_occ_file ON occurrences(file_id, line);
CREATE INDEX idx_occ_role ON occurrences(role);
"""
