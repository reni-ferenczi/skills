# How the index is built

## Pipeline

`scripts/setup_index.py` runs these steps in order and stops at the first failure.

1. **Validate the source tree** (`gplates_index/common.check_source_root`).
   Ten marker paths must exist — `CMakeLists.txt`, `CHANGELOG`,
   `cmake/modules/Version.cmake`, `src/gplates_main.cc`, `src/app-logic`,
   `src/qt-widgets`, `src/maths`, `src/model`, `src/CMakeLists.txt`,
   `src/qt-resources/gpgim/gpgim.xml` — and `GPLATES_VERSION_{MAJOR,MINOR,PATCH}`
   parsed out of `Version.cmake` must be ≥ 2.5.0. Nothing is downloaded before
   this passes.
2. **Get the parsers.** Universal Ctags, and tree-sitter (`pip install --target
   data/pylibs tree_sitter tree_sitter_cpp` — prebuilt wheels, no compiler).
   Universal Ctags: `data/tools/ctags.exe` if already there, else `ctags`
   on `PATH`, else download the pinned Windows build
   (`universal-ctags/ctags-win32` v6.1.0, x64, ~2.9 MB) and extract `ctags.exe`.
   The binary is then checked: it must report *Universal Ctags* (Exuberant Ctags
   cannot emit JSON) and list `json` among its compiled features.
3. **Walk the tree** and record every file, skipping `.git`, `.idea`, `build`,
   `__pycache__` and friends. Files with a known text extension and under 4 MB have
   their content stored line by line.
4. **Extract per file** — `#include` directives, Qt `connect()` calls, and
   Boost.Python `class_<>`/`def()` chains from the C++ sources.
5. **Resolve includes** — each quoted `#include` is matched against in-tree files
   by longest path suffix, giving a real dependency graph.
6. **Build the FTS5 index** over the stored lines.
7. **Run ctags** over `src/`, `scripts/` and `cmake/` with JSON output, and load
   the tags. Noise kinds (`parameter`, `local`, `tparam`, `macroparam`, `label`,
   `file`) and ctags' `qualified` duplicate tags are dropped.
8. **Parse the Qt `.ui` forms** and `gpgim.xml`.
9. **Deep-parse every C/C++ file with tree-sitter** (two passes: declarations, then
   occurrences), then resolve base classes, build the inheritance closure and bind
   occurrences to entities. See *The deep C++ pass* below.
10. **Verify.** Every count in `indexer.SANITY_MINIMUMS` must be met, or the build
   exits non-zero with the shortfalls listed. The thresholds sit roughly 20-25%
   below what GPlates 2.5.0 actually produces, so a newer release still passes but
   a broken parse does not.

Typical run on GPlates 2.5.0: about 30 seconds, `data/gplates.db` about 191 MB
(3081 files, 121k entities, 560k occurrences, 844k lines).

## The deep C++ pass

`cpp_parse.py` prepares each file with two **length-preserving** transforms, so
every byte offset, line and column in the parse tree still points at the real file:

* `neutralise_qt` rewrites Qt macros that are not valid C++ (`Q_OBJECT`,
  `signals:`, `Q_SLOTS:`, `SIGNAL(...)`, `SLOT(...)`, `Q_PROPERTY(...)`).
* `select_branches` keeps one arm of each `#if/#elif/#else` chain — the first,
  or the second for `#if 0` — because tree-sitter sees every arm at once.

Together these cut the share of bytes inside ERROR nodes on GPlates 2.5.0 from
1.357% to 0.063%. A test asserts both transforms preserve length and line count.

`cpp_extract.py` then walks each tree twice: once over the declaration structure
(building qualified names from a lexical container stack) and once flat, recording
each identifier with the role it plays. `resolve.py` binds base classes to real
classes, computes the transitive inheritance closure, and assigns each occurrence
an entity plus a confidence label.

## Where things live

| Path | Contents |
|---|---|
| `data/config.json` | remembered source root, version, ctags path and banner |
| `data/tools/ctags.exe` | the downloaded Universal Ctags |
| `data/gplates.db` | the index |

`data/` is git-ignored. The GPlates source tree is only ever read.

## Schema

Authoritative copy: `scripts/gplates_index/schema.py`.

```sql
meta(key, value)                 -- source_root, gplates_version, built_at, count_*

files(id, path, dir, name, ext,  -- path is relative to the source root, '/' separated
      category, size, lines, has_text)
      -- category: cpp | python | ui | shader | gpgim | resource | build | doc | data | other

symbols(id, name, name_lc, kind, lang, file_id, line, end_line,
        scope, scope_kind, signature, typeref, access, inherits, is_def)
        -- is_def = 0 for prototypes/declarations

includes(file_id, line, header, is_system, target_id)  -- target_id: resolved files.id

lines(id, file_id, line, text)                          -- text truncated at 2000 chars
lines_fts                                               -- FTS5 over lines.text,
                                                        -- unicode61 with '_' as a token char

ui_forms(file_id, class_name, base_class, title)
ui_widgets(file_id, form, widget_class, object_name, text)
qt_connections(file_id, line, sender, signal, receiver, slot)
py_api(file_id, line, owner, name, kind, cpp_type)
        -- kind: class | enum | function | method | staticmethod | attribute | enum_value

gpgim_features(file_id, line, name, class_type, inherits, description, default_geometry)
gpgim_properties(file_id, line, name, types, multiplicity, description)
gpgim_feature_properties(feature, property)

-- deep C++ index (tree-sitter)
entities(id, name, name_lc, qname, kind, file_id, line, col, end_line,
         parent_id,          -- lexical container
         type_text, signature, access, storage,
         is_def,             -- 0 = declaration only
         is_template, template_params)

bases(entity_id, base_name,  -- as written, e.g. Base<T>
      base_key,              -- normalised: template args and scope stripped
      base_entity_id,        -- NULL when the base lives outside the tree
      access, is_virtual)

inherit_closure(ancestor_id, descendant_id, depth)

occurrences(id, file_id, line, col, name, name_lc, role,
            container_id,    -- enclosing function/method
            entity_id,       -- resolved target, NULL when ambiguous
            confidence)      -- local|member|file|unique|include|ambiguous
```

Query it directly when the subcommands are not enough:

```bash
python scripts/gpq.py sql "SELECT f.path, COUNT(*) c FROM symbols s
  JOIN files f ON f.id = s.file_id WHERE s.kind = 'class'
  GROUP BY f.path ORDER BY c DESC LIMIT 10"
```

## Maintenance

```bash
python scripts/setup_index.py --check          # re-verify the current index
python scripts/setup_index.py --rebuild        # rebuild from the stored source path
python scripts/setup_index.py --source <DIR>   # point at a different source tree
python scripts/setup_index.py --validate-only --source <DIR>
python scripts/test_gpq.py                     # 91 tests
```

Rebuild whenever the source tree changes — the index stores absolute line numbers,
and stale ones are worse than none.

To start completely fresh, delete `data/` and re-run setup.

## Troubleshooting

**`error: ... does not look like a GPlates source tree`** — the path is wrong or the
archive was extracted one level too deep. The message names the missing markers;
the right directory is the one containing `CMakeLists.txt` and `src/`.

**`error: GPlates 2.4.0 found ..., but this skill requires 2.5.0 or later`** — the
extractors and the module map target 2.5+. Get a newer source archive.

**`could not download ctags`** — no network, or GitHub is blocked. Download
`ctags-v6.1.0-x64.zip` from
<https://github.com/universal-ctags/ctags-win32/releases> by hand, put `ctags.exe`
in `data/tools/`, and re-run. Or install Universal Ctags anywhere and pass
`--ctags <path>`.

**`is not Universal Ctags` / `built without JSON support`** — a `ctags` on `PATH`
shadowed the right one (often Exuberant Ctags or the Emacs `etags` shim). Pass
`--ctags` explicitly, or delete `data/tools/ctags.exe` to force a fresh download.

**`index built but FAILED sanity checks`** — the index exists but is short on
something; the message names which counts and by how much. Usually a truncated or
partial source extraction. Re-extract and rebuild.

**A search returns nothing you expected** — check the match mode on the `#` line.
FTS cannot match inside a token or across punctuation; switch to `--regex`. For
symbols, try `--mode sub` or drop `--kind`.

**Line numbers are off by a few** — the index is stale. Rebuild.

**`tree-sitter is not installed`** — the deep pass needs it. Re-run
`setup_index.py`, which installs it, or do it by hand:
`python -m pip install --target data/pylibs tree_sitter tree_sitter_cpp`.

**`uses` misses a call site** — resolution is syntactic. Check whether the name is
reached through a macro, a template instantiation, or an overload; `gpq refs` finds
it textually.

## Extending the index

Adding a new extraction is three edits:

1. a table in `gplates_index/schema.py`,
2. an extractor function — `gplates_index/build.py` for regex/XML sources,
   `gplates_index/cpp_extract.py` for anything that needs the C++ parse tree —
   plus its call site in `gplates_index/indexer.py` (and a row in
   `SANITY_MINIMUMS` if it should be guaranteed non-empty),
3. a subcommand in `gpq.py` and a test in `test_gpq.py`.

Extractors take text (or a path) and yield plain tuples, so they unit-test without
an index — see the `Extractors` test case for the pattern.
