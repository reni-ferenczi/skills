# Searching the index — `gpq.py` reference

All examples assume `python` is Python 3.12+ and you are in the skill directory.
Every command accepts `--limit N` (default 40) and `--json`, in either position:

```bash
python scripts/gpq.py --limit 5 sym Foo
python scripts/gpq.py sym Foo --limit 5     # identical
```

## Output contract

- Lines starting with `#` are summaries — result counts, the match mode that was
  used, truncation warnings. Everything else is a result.
- Most results are `path:line: text` or end in `path:line`, so they are clickable
  and greppable.
- Exit codes: `0` results, `1` no results, `2` bad usage or missing index,
  `3` unexpected error.
- `--json` prints one JSON array of records to stdout and drops the `#` lines.

## Match modes

`sym` and `def` take `--mode exact|prefix|sub|regex`, default `auto`.
`auto` tries **exact**, then **prefix**, then **substring**, and stops at the first
mode that returns anything — the `#` line reports which one won. Matching is
case-insensitive unless you pass `--case`. `--mode regex` uses Python regex syntax
against the bare symbol name (not the qualified one).

---

## Commands

### `info` — orientation

Index stats plus a module map (files and symbol counts per top-level directory).
Read this first in a new session.

### `sym <name>` — find symbols

```bash
python scripts/gpq.py sym ReconstructionTree --kind class
python scripts/gpq.py sym reconstruct --mode sub --path src/app-logic --defs-only
python scripts/gpq.py sym "^GL.*Raster$" --mode regex --kind class
```

| Flag | Effect |
|---|---|
| `--kind K` | restrict to a ctags kind; repeatable |
| `--lang C++\|Python` | restrict by language |
| `--path SUBSTR` | only files whose path contains `SUBSTR` |
| `--scope SUBSTR` | only symbols whose enclosing namespace/class contains `SUBSTR` |
| `--defs-only` | drop declarations and prototypes |
| `--case` | case-sensitive |

Kinds present in the index: `class`, `struct`, `union`, `enum`, `enumerator`,
`function`, `prototype`, `member`, `variable`, `typedef`, `namespace`, `macro`,
`using`, `alias`. Declarations are printed with a trailing `(decl)`.

A result line is `kind  Scope::name(signature) -> type  path:start-end`.

### `def <name>` — read a definition

```bash
python scripts/gpq.py def ReconstructionTree --kind class --body
python scripts/gpq.py def get_anchor_plate_id --body --limit 1
```

Takes `--mode`, `--kind`, `--path` and `--case` (not `--lang`, `--scope` or
`--defs-only`), plus:

| Flag | Effect |
|---|---|
| `--body` | print the source between the definition's start and end lines |
| `--max-body N` | cap on body lines (default 400) |
| `--context N` | lines to show when ctags could not find the end (default 20) |

C++ methods are usually declared in a `.h` and defined in a `.cc`; `def` only
returns definitions, so pair it with `--path` when both exist.

### `grep <query>` — search every indexed line

```bash
python scripts/gpq.py grep "anchored plate id"                  # all words, any order
python scripts/gpq.py grep "anchored plate id" --phrase         # exact phrase
python scripts/gpq.py grep "d_anchor_plate_id\s*=" --regex
python scripts/gpq.py grep isosurface --category shader
```

Default is FTS5 token search: the query is split on non-word characters and every
token must appear on the line. `_` counts as a word character, so
`reconstruct_feature_geometries` is a single token.

| Flag | Effect |
|---|---|
| `--phrase` | tokens must appear adjacent, in order |
| `--regex` | Python regex over the raw line; slower (full scan) but exact |
| `--case` | case-sensitive; regex mode only |
| `--path SUBSTR` | restrict by path |
| `--category C` | `cpp`, `python`, `ui`, `shader`, `gpgim`, `resource`, `build`, `data`, `doc`; repeatable (a tenth category, `other`, holds only binary files with no searchable text) |

Results are ranked code-first (cpp → python → ui → shader → gpgim → resource →
build → data → doc), so a truncated result set keeps the useful half. Use
`--category doc` when you *want* the CHANGELOG and README.

FTS cannot match partial tokens or punctuation — use `--regex` for
`operator->`, `d_ptr->foo`, or anything with wildcards inside a word.

---

## Semantic commands

These read the tree-sitter index: 121k **entities** (every type, member, variable,
parameter, local, template and macro, with its declaration *and* definition sites),
560k **occurrences** (identifier tokens tagged with the role they play), and a
transitive **inheritance graph**.

`decl`, `uses`, `hier` and `members` all take the same name-matching flags as `sym`
(`--mode`, `--kind`, `--path`, `--case`) and widen exact → prefix → substring.
Pass a qualified name (`GPlatesAppLogic::ReconstructionTree`) for an exact hit.

### `decl <name>` — declarations and definitions

```bash
python scripts/gpq.py decl ReconstructionTree --kind class
python scripts/gpq.py decl d_anchor_plate_id
python scripts/gpq.py decl GPLATES_ASSERTION_SOURCE
```

Every site where the name is introduced, definitions first, each tagged `(def)` or
`(decl)`. This separates a class's real definition from its forward declarations,
and a method's out-of-line definition from its in-class declaration.

Entity kinds (19): `namespace`, `class`, `struct`, `union`, `enum`, `enumerator`,
`typedef`, `alias`, `function`, `method`, `constructor`, `destructor`,
`operator`, `field`, `variable`, `parameter`, `local`, `macro`, `macro_function`.
(`using` is a *ctags* kind in `sym`, not an entity kind.)

Lines carry the declared/return type, the signature, access, and the template
parameter list for templates.

### `uses <name>` — resolved usages

```bash
python scripts/gpq.py uses d_anchor_plate_id
python scripts/gpq.py uses get_anchor_plate_id --role call
python scripts/gpq.py uses ReconstructionTree --kind class --role type
python scripts/gpq.py uses LayerProxy --exclude-decl --context-symbol
```

Occurrences bound to the entity, with a per-role breakdown first. Roles:

| Role | Meaning |
|---|---|
| `call` | called as a function, including `obj->method()` |
| `read` | read in an expression |
| `write` | assigned to |
| `member` | reached through `.` or `->` |
| `member_write` | assigned to through `.` or `->` |
| `type` | used as a type |
| `base` | named as a base class |
| `template_arg` | passed as a template argument |
| `ns` | used as a namespace/scope qualifier |
| `decl` / `def` | the declaration and definition sites themselves |

`--exclude-decl` drops the declaration sites; `--context-symbol` appends the
enclosing function to each line. When any same-named occurrences could **not** be
bound to a specific entity, a closing line says how many — use `gpq refs <name>`
to see those. The header marks which matched entities are definitions rather than
forward declarations.

### `hier <class>` — inheritance, transitively

```bash
python scripts/gpq.py hier LayerProxy
python scripts/gpq.py hier ReconstructLayerProxy --up
python scripts/gpq.py hier ReferenceCount --down --depth 2
```

Base classes (`base dN`) and subclasses (`sub dN`), where `N` is the inheritance
distance. `--up` / `--down` restrict the direction, `--depth` caps the distance.

Direct bases outside the GPlates tree — `QObject`, `QWidget`, `boost::noncopyable`
— are listed and marked *(outside the GPlates tree)* rather than silently dropped.

### `members <class>` — what is inside a type or namespace

```bash
python scripts/gpq.py members ReconstructionTree
python scripts/gpq.py members ReconstructionTree --kind field
python scripts/gpq.py members ReconstructionTree --kind method --access public
python scripts/gpq.py members ReconstructUtils --kind function
python scripts/gpq.py members ReconstructLayerProxy --inherited
```

Everything declared directly inside a class, struct, union, enum or namespace, with
types and access. `--kind` and `--access` filter the *members*; `--inherited` also
walks up the inheritance graph.

### `macro [name]` — preprocessor symbols

```bash
python scripts/gpq.py macro                       # every macro in the tree
python scripts/gpq.py macro GPLATES_ASSERTION_SOURCE --uses
```

Object-like and function-like macros: where defined, their parameter list, what
they expand to, and with `--uses` every place they are used.

---

### `refs <name>` — definitions plus call sites

```bash
python scripts/gpq.py refs reconstruct_feature_geometries --limit 30
```

`--path SUBSTR` restricts the search. Prints indexed definitions first
(`[def kind]`), then whole-word occurrences on other lines; the header reports the
true total, not just the number shown. This is the closest thing to "find usages"; it is text-based, so
overloads and same-named members of unrelated classes all show up.

### `file <path>` — one file

```bash
python scripts/gpq.py file src/app-logic/ReconstructUtils.h          # outline
python scripts/gpq.py file ReconstructUtils                          # list candidates
python scripts/gpq.py file src/app-logic/ReconstructUtils.h --range 60-120
python scripts/gpq.py file src/qt-widgets/AboutDialogUi.ui           # form + widgets
```

Bare, it prints every symbol in line order — the fastest way to understand a header.
A partial path lists the candidates instead; `--first` picks the shortest match.
`--range LO-HI` and `--cat` print the stored text with line numbers.

For `.ui` files the output also includes the form class, its base widget and every
named widget with its visible text.

### `tree [prefix]` — directory map

```bash
python scripts/gpq.py tree              # top level
python scripts/gpq.py tree src --depth 1
python scripts/gpq.py tree src/qt-resources --depth 2
```

File and line counts per directory. `--depth` counts levels below `prefix`.

### `includes <path>` — include graph

```bash
python scripts/gpq.py includes src/app-logic/ReconstructUtils.h        # what it includes
python scripts/gpq.py includes src/app-logic/ReconstructionTree.h --by # what includes it
```

Quoted includes are resolved to in-tree files where possible (`-> path`), so `--by`
answers "who depends on this header".

### `hier-ctags <class>` — inheritance from the ctags index

Superseded by `hier`; kept as a fallback if the tree-sitter pass is unavailable.

### `ui [name]` — Qt Designer forms

```bash
python scripts/gpq.py ui                          # every form
python scripts/gpq.py ui TotalReconstructionPoles # one form and all its widgets
python scripts/gpq.py ui "Reconstruction Time"    # search widget labels
```

Matches form class names, window titles, file paths, widget object names, widget
classes and visible text. When exactly one form matches, its full widget list is
printed — the fast way from a label the user saw on screen to the widget object
name you need to grep for in the `.cc`.

### `signals <name>` — Qt signal/slot wiring

```bash
python scripts/gpq.py signals reconstruction_time_changed
python scripts/gpq.py signals ApplicationState
```

Every `connect(...)` call using the `SIGNAL()`/`SLOT()` macros, printed as
`path:line: sender.signal(...) -> receiver.slot(...)`. Matches against any of the
four parts — but those are stored as written *expressions* (`this`,
`d_application_state_ptr`), so search for a signal, slot or variable name rather
than a class name. Function-pointer style connections carry no macro and are not indexed —
find those with `gpq grep "connect(" --regex`.

### `pyapi [name]` — Python bindings

```bash
python scripts/gpq.py pyapi              # everything exposed to Python
python scripts/gpq.py pyapi Feature
```

The Boost.Python surface registered from `src/api/` — classes, methods, attributes
and free functions, each with the C++ entity it is bound to and where it is
registered. This is the API available in the GPlates Python console.

### `gpgim [name]` — the GPlates Geological Information Model

```bash
python scripts/gpq.py gpgim Isochron --detail
python scripts/gpq.py gpgim reconstructionPlateId --detail
python scripts/gpq.py gpgim --limit 200          # every feature class and property
```

Feature classes (with `ClassType`, `Inherits` and default geometry property) and
property definitions (with value types, multiplicity and description), parsed from
`src/qt-resources/gpgim/gpgim.xml`. `--detail` adds descriptions, the property list
of a feature class, and the feature classes that use a property.

### `community` / `neighbors` — code clusters and graph edges

From the optional code graph (`scripts/build_graph.py`). Full reference:
[GRAPH.md](GRAPH.md).

```bash
python scripts/gpq.py community ReconstructLayerProxy
python scripts/gpq.py community --list --limit 20
python scripts/gpq.py community --id 65
python scripts/gpq.py neighbors LayerProxy --relation inherits
```

Both rank candidates against the entity index, so a real definition beats one of
graphify's location-less stub nodes; lines are tagged `[def]`, `[ref]`, `[stub]`.
Both also take `--case`; `neighbors` takes `--nodes N` (how many same-named nodes
to expand, default 2) and `community` takes `--by-size`.

### `sql <query>` — escape hatch

```bash
python scripts/gpq.py sql "SELECT kind, COUNT(*) FROM symbols GROUP BY kind ORDER BY 2 DESC"
```

Read-only SQL against the index. The connection is opened `mode=ro`, so writes fail.
When the code graph exists it is attached as schema `g` (`g.communities`,
`g.graph_nodes`, `g.graph_edges`, `g.meta`). Schema: [INDEXING.md](INDEXING.md).

---

## Recipes

**"Where does GPlates compute stage rotations?"**
```bash
python scripts/gpq.py sym stage_rotation --mode sub --defs-only
python scripts/gpq.py def get_stage_pole --body
```

**"What happens when the user changes the reconstruction time?"**
```bash
python scripts/gpq.py signals reconstruction_time_changed
python scripts/gpq.py refs set_reconstruction_time --limit 30
```

**"Which dialog is 'Manage Feature Collections'?"**
```bash
python scripts/gpq.py ui "Manage Feature Collections"
python scripts/gpq.py file src/qt-widgets/ManageFeatureCollectionsDialog.h
```

**"What can a gpml:MidOceanRidge hold?"**
```bash
python scripts/gpq.py gpgim MidOceanRidge --detail
python scripts/gpq.py gpgim leftPlate --detail
```

**"Who depends on ApplicationState?"**
```bash
python scripts/gpq.py includes src/app-logic/ApplicationState.h --by --limit 100
```

**"How is a .gpml file parsed?"**
```bash
python scripts/gpq.py sym GpmlReader --kind class
python scripts/gpq.py file src/file-io/GpmlReader.cc --limit 100
python scripts/gpq.py grep "gpml:FeatureCollection" --category data --limit 5
```

**"Which shader does the 3D scalar field use?"**
```bash
python scripts/gpq.py tree src/qt-resources/opengl --depth 1
python scripts/gpq.py sql "SELECT path FROM files WHERE ext = '.glsl' AND path LIKE '%scalar_field%'"
python scripts/gpq.py grep "uniform sampler2D" --category shader
```

## What the semantic index can and cannot do

Built from tree-sitter's *syntax* tree, not from a compiler. There is no
preprocessor expansion, no template instantiation and no overload resolution, so:

- **Resolution is scope-and-reachability based.** Every occurrence carries a
  confidence: `local` (a parameter/local of the enclosing function), `member` (a
  member of the enclosing class), `file`, `unique` (the name is declared once in
  the whole tree), `include` (reachable through this file's `#include`s),
  `ambiguous` (several equal candidates) or `unknown` (no candidate at all).
  `ambiguous` and `unknown` both leave `entity_id` NULL. 91.8% of the 560k occurrences bind to a specific entity; the rest
  are still stored and still findable by name, they just do not claim a target.
- **Overloads are not distinguished.** Two methods with the same name in the same
  class share their usage sites.
- **Macro bodies are not expanded**, so a symbol only reachable through a macro
  expansion is not linked. The macro itself, and its use sites, are indexed.
- **Only one arm of each `#if/#else` survives.** The first arm is kept (or the
  second, for `#if 0`), so code behind a non-default configuration is not indexed.
- **Qt's macros are neutralised before parsing** — `Q_OBJECT`, `signals:`,
  `Q_SLOTS:`, `SIGNAL(...)`, `SLOT(...)` — using length-preserving substitutions,
  so line and column numbers stay exact. Signal/slot wiring is indexed separately
  via `gpq signals`.
- **Base classes outside the tree do not resolve.** `QObject`, `QWidget` and
  `boost::noncopyable` are reported by name and marked as external. Every in-tree
  base resolves; a test asserts no `GPlates*` base is left unresolved.
- **0.06% of source bytes fail to parse** and are simply absent from the entity
  and occurrence tables. The residue is preprocessor-conditional oddities.

When the semantic index cannot answer, fall back to `gpq grep` (full text) and
`gpq refs` (whole-word text matching with definitions ranked first).

## Limits worth knowing

- The index is a snapshot taken at build time; re-run `setup_index.py --rebuild`
  after the source tree changes.
- `sym` and `def` read the older ctags index, which is kept because it also covers
  Python. For C++ prefer `decl`, which is richer and distinguishes declarations
  from definitions.
- `refs` and `signals` are text-driven, not semantic — no overload resolution.
- Lines longer than 2000 characters are stored truncated.
- Binary files (`.png`, `.shp`, `.gz`, `.ico`) are listed in `files` but have no
  indexed text.
