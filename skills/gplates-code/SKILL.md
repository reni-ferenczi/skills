---
name: gplates-code
description: Deeply index and search the GPlates 2.5+ C++/Python source tree. Finds the declaration, definition, usages, subclasses and base classes of any type, member, variable, template or preprocessor macro, plus Qt dialogs and signal/slot wiring, the GPGIM feature model, OpenGL shaders and sample data. Use for any question about GPlates or pyGPlates internals, or when writing code against them.
license: MIT
---

# GPlates Code

Search a local GPlates source tree (2.5.0 or later) through a prebuilt SQLite index.

The core is a **semantic index built with tree-sitter**: 121k entities — types,
members, variables, parameters, locals, templates and preprocessor macros — each
with its declaration and definition sites, 560k identifier occurrences bound to the
entity they name (91.8% resolved), and a transitive inheritance graph. Around that
sit an FTS5 index of every source line, the `#include` graph, Qt Designer forms, Qt
signal/slot connections, the Boost.Python bindings and the GPGIM feature model.

Everything is one command: `scripts/gpq.py`. Output is one result per line, mostly
`path:line: text`, so it pipes into `grep`, `head` and friends.

No GPlates build is required — nothing needs Qt, Boost, CGAL, GDAL or PROJ
installed. Setup downloads a 2.9 MB ctags binary and pip-installs tree-sitter into
the skill's own folder.

**Platform:** Windows (the ctags download is Windows-only; the rest is portable).
**Python:** `C:\Python312\python.exe`, or any Python 3.12+ on `PATH`.

## 1. Check the index

```bash
C:\Python312\python.exe scripts/gpq.py info
```

If that prints stats, skip to step 3. If it says *no index found*, do step 2.

## 2. One-time setup

The GPlates source download is gated behind a name+email form, so **the user must
download and extract it themselves** — from <https://www.gplates.org/download/>
(the *GPlates source code* archive), or by checking out the `release-gplates`
branch of <https://github.com/GPlates/GPlates>. Ask the user for the path if you
do not have one; do not try to fetch it.

```bash
C:\Python312\python.exe scripts/setup_index.py --source C:\Dev\gplates_2.5.0_src
```

This validates the tree is really GPlates ≥ 2.5.0, downloads Universal Ctags into
`data/tools/`, pip-installs tree-sitter into `data/pylibs/`, and writes
`data/gplates.db` (~191 MB, about 30 seconds). It refuses to continue on a wrong
directory, an old version, or an index that comes out short on any expected row count.

Useful variants: `--validate-only` (check the path, build nothing), `--check`
(re-verify an existing index), `--rebuild` (rebuild from the stored path),
`--ctags <path>` (use your own Universal Ctags).

## 3. Search

Five semantic commands answer *where is it declared, defined, used; what does it
inherit; what does it contain* — for **types, members, variables, parameters,
templates and preprocessor macros** alike:

```bash
python scripts/gpq.py decl ReconstructionTree      # declarations AND definitions
python scripts/gpq.py uses d_anchor_plate_id       # resolved usages, by role
python scripts/gpq.py hier LayerProxy              # bases and subclasses, transitively
python scripts/gpq.py members ReconstructionTree   # fields, methods, typedefs, enums
python scripts/gpq.py macro GPLATES_ASSERTION_SOURCE --uses
```

Text-level search remains for everything the parser cannot bind:

```bash
python scripts/gpq.py grep "anchored plate id"               # full-text over all lines
python scripts/gpq.py file src/app-logic/ReconstructUtils.h  # outline of one file
python scripts/gpq.py refs reconstruct_feature_geometries    # unresolved text fallback
```

Name lookups widen automatically — exact, then prefix, then substring — and the
`# ...` summary line says which mode produced the hits. Every command takes
`--limit N` (default 40) and `--json`.

The full command list, filters and worked recipes: **[references/SEARCH.md](references/SEARCH.md)**.

## 4. Find your way around GPlates

Start broad, then narrow — the index is built for exactly this:

```bash
python scripts/gpq.py info                     # module map: files and symbols per directory
python scripts/gpq.py tree src/app-logic       # what lives under one module
python scripts/gpq.py file <path>              # a file's symbols, in line order
python scripts/gpq.py def <symbol> --body      # finally, read the code
```

`info` and `tree` are cheap and give you the shape of a 850k-line codebase in two
commands. Reach for `def --body` or `file --range` only once you know where to look.

For what each module is responsible for, the namespace layout and the main classes:
**[references/ARCHITECTURE.md](references/ARCHITECTURE.md)**.

## Beyond plain code

GPlates is a Qt application with a domain model expressed in XML, so the index
covers more than C++:

| Question | Command |
|---|---|
| Where is this type/member/variable declared and defined? | `gpq decl <name>` |
| Where is it used, and how? | `gpq uses <name> --role call` |
| What derives from this class? What does it derive from? | `gpq hier <class>` |
| What is inside this class or namespace? | `gpq members <class> --kind field` |
| What does this macro expand to, and who uses it? | `gpq macro <name> --uses` |
| Which dialog has this button / label? | `gpq ui "Reconstruction Time"` |
| What is on this dialog? | `gpq ui TotalReconstructionPoles` |
| What reacts to this Qt signal? | `gpq signals reconstruction_time_changed` |
| What does the embedded Python API expose? | `gpq pyapi Feature` |
| Which properties does this feature type have? | `gpq gpgim Isochron --detail` |
| Which feature types use this property? | `gpq gpgim reconstructionPlateId --detail` |
| What is in the GLSL shaders? | `gpq grep "uniform sampler2D" --category shader` |

## Layout

```
skills/gplates-code/
├── SKILL.md
├── references/
│   ├── SEARCH.md          full gpq reference and recipes
│   ├── ARCHITECTURE.md    GPlates source tree map
│   └── INDEXING.md        how the index is built, schema, troubleshooting
├── scripts/
│   ├── setup_index.py     validate source, fetch tools, build the index
│   ├── gpq.py             the query CLI
│   ├── test_gpq.py        test suite
│   └── gplates_index/     common, schema, build, indexer,
│                          cpp_parse, cpp_extract, resolve
└── data/                  generated, git-ignored
    ├── config.json        remembered source path
    ├── tools/ctags.exe    downloaded Universal Ctags
    ├── pylibs/            tree-sitter + tree-sitter-cpp
    └── gplates.db         the index
```

The GPlates source tree itself is never copied or modified — `data/` only holds
the index and the ctags binary.

## Tests

```bash
C:\Python312\python.exe scripts/test_gpq.py
```

91 tests. Parser, extractor and source-tree validation tests run without an
index; index-integrity and CLI tests need one and are skipped (with a warning)
otherwise.

## When results look wrong

- `setup_index.py --check` re-runs every sanity check against the current index.
- The index is a **snapshot**. If the user edits the source tree, re-run
  `setup_index.py --rebuild`, or the line numbers will drift.
- `gpq sql "<SELECT ...>"` is the escape hatch for anything the subcommands do not
  cover; the schema is in [references/INDEXING.md](references/INDEXING.md).
- Resolution is syntactic, not compiled: `uses` labels every hit with a confidence
  and reports how many same-named occurrences it could **not** bind to a specific
  entity. Overload resolution and template instantiation are out of reach — the
  limits are spelled out in [references/SEARCH.md](references/SEARCH.md).
