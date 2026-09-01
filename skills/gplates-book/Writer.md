# Writer.md — plan for generating the GPlates developer's reference manual

This is the execution plan for building `book/` in this skill. It instantiates the
**structured-documentation** pipeline (setup → index & tier → describe →
cross-reference & modularize → enrich & verify → finalize) on top of the
**gplates-code** skill's prebuilt index (`skills/gplates-code/data/gplates.db`,
optional `graph.db`). Nothing here re-parses C++: every structural fact comes from
the index; AI effort is spent only on prose.

## Inputs (already built — do not rebuild)

| Source | What it provides |
|---|---|
| `../gplates-code/data/gplates.db` | `files` (3,081 rows: 2,368 C++ / 737k lines, 185 ui, 185 data, 194 other, 48 build, 38 shader, 28 python, 21 resource, 9 doc, 5 gpgim), `entities` (121,523 — types, members, functions, macros with decl/def sites, `is_template` flag), `occurrences` (560,598, of which 514,736 resolved → fan-in), `bases`/`inherit_closure`, `includes` (20,515), `ui_forms` (185)/`ui_widgets`, `qt_connections` (1,656), `py_api`, `gpgim_*` (109 features / 115 properties), `lines` (843,998)/FTS |
| `../gplates-code/data/graph.db` | 52,135 nodes, 92,908 edges, **1,960** Leiden communities — used to sub-group oversized components |
| `../gplates-code/scripts/gpq.py` | query CLI given to prose agents; `gpq sql` is the extraction backend for our scripts |
| `../gplates-code/references/ARCHITECTURE.md` | seed text for component responsibilities |

**These counts were verified against the index on 2026-09-01 (GPlates 2.5.0).**
They drift on every reindex, so `build_manifest.py` must derive them at run time,
never hard-code them; the numbers here only size the effort. Re-verify with
`gpq info` plus the queries quoted in each section below, and check that
`graph.db` is **newer than** `gplates.db` — the graph stores paths and line
numbers, so a stale graph silently mis-groups components.

Building the index needs `C:\Python312\python.exe`; querying it (everything this
plan does) uses only the standard library, so plain `python` is fine. If
`gpq.py info` reports no index, stop and have the user run the gplates-code setup
first.

## Output layout (everything generated lives under this skill)

```
skills/gplates-book/
├── SKILL.md              entry point (frontmatter + pointers) — committed
├── Writer.md             this plan — committed
├── scripts/              generators + verifier — committed
├── data/                 working data, cache keys, progress — git-ignored, keep between runs
│   ├── manifest.jsonl    one record per unit: files, sha256 (LF-normalized), component, tier, signals
│   ├── path_map.json     unit id → book page path (collision-resolved)
│   ├── descriptions.jsonl  one-line descriptions per entity (for the indexes)
│   ├── progress.json     prose-pass state (per unit: pending | done | failed, run number)
│   └── refgraph.json     unit→unit reference edges (from includes + occurrences)
└── book/                 the manual — committed
    ├── TOC.md            top level: project overview, component list, links to all indexes
    ├── indexes/
    │   ├── Components.md   component index
    │   ├── Classes.md      classes (and unions) by name, one-line description
    │   ├── Structs.md      structs by name, one-line description
    │   ├── Enums.md        enums by name, one-line description
    │   ├── Typedefs.md     typedefs and aliases by name, one-line description
    │   ├── Functions.md    global/namespace-scope free functions by name, one-line description
    │   └── Macros.md       preprocessor macros by name, one-line description
    ├── components/<name>.md          one page per component (~27 pages)
    └── src/<mirrored dirs>/<Unit>.md one page per unit (~1,372 pages)
```

Progressive disclosure: `SKILL.md` → `TOC.md` → component page → unit page →
source (via `gpq` commands quoted on the page). The flat indexes are the
by-name shortcut that skips the hierarchy. No page should require reading
another page to be understood; every page links up (component, TOC) and
sideways (referenced units).

## Unit = documentation atom

A **unit** is one `.h`/`.cc` pair (matched by stem within the same directory),
or a lone header/source. Verified: the 2,368 C++ files collapse to **1,372**
distinct `(dir, stem)` groups —

```sql
SELECT COUNT(*) FROM (SELECT dir, replace(replace(name,'.h',''),'.cc','') s
                      FROM files WHERE category='cpp' GROUP BY dir, s)
```

so ~1,372 unit pages. Non-C++ inputs attach or group:

- `.ui` forms (185) → attached to the dialog unit that inherits `Ui::<Form>`
  (via `ui_forms.class_name`); orphans get a row on the `qt-resources` component page.
- Shaders (38) → one unit page per shader directory (`scalar_field_3d`, …),
  linked from the `GL*` unit that loads them.
- GPGIM XML (5) → one unit page, plus the feature/property tables generated from `gpgim_*`.
- Python (28): `src/api` bindings are C++ units already; top-level `scripts/*.py`
  → one "Python examples" unit page.
- `doc`, `build`, `data`, `resource`, `other` categories → summarized in tables on
  the owning component page (no per-file pages), so they are still reachable.

**Coverage invariant:** every row of `files` maps to exactly one unit page or one
component-page table row. `verify_book.py` enforces this — nothing is missed.

## Components (~27)

**Derive the list from the index, not from ARCHITECTURE.md** — the index has
**22** top-level `src/<dir>` modules (file counts, all categories):

| | | | |
|---|---|---|---|
| qt-widgets 632 | app-logic 272 | gui 261 | file-io 250 |
| qt-resources 229 | opengl 159 | maths 143 | property-values 126 |
| utils 94 | view-operations 83 | model 82 | unit-test 72 |
| data-mining 69 | scribe 63 | canvas-tools 52 | presentation 47 |
| feature-visitors 41 | global 40 | deprecated 37 | api 36 |
| cli 21 | system-fixes 4 | | |

ARCHITECTURE.md's table omits `src/system-fixes` — a reminder that the index is
the authority and any hand-written module list will silently drop code.

Everything outside `src/<dir>` also needs a home, or the coverage invariant
fails: `sample-data/` 186, `scripts/` 33, `cmake/` 21, repo root 12, `doc/` 6,
and **10 loose files directly in `src/`** — which include the three entry points
(`gplates_main.cc`, `gplates_demo_no_gui_main.cc`, `gplates_unit_test_main.cc`)
and `CMakeLists.txt`, the authoritative source inventory. Those 10 get a real
`entry-points` component page, not a table row; the rest go to `sample-data`,
`python-examples` (`scripts/*.py`), and `build-and-docs` (`cmake/`, `doc/`, root).

So: 22 `src` components + `entry-points`, `sample-data`, `python-examples`,
`build-and-docs`, `shaders` ≈ 27. Deprecated code stays under its own module
page (`src/deprecated`, 37 files) plus per-module `deprecated/` subdirectories
(178 files match `%deprecated%` overall) — flagged and forced to tier 3, but
still listed and reachable.

Components with >150 units (`qt-widgets` 439 C++ files, `app-logic` 262, `gui`
253, `file-io` 231, `opengl` 158) get sections on their component page grouped
by Leiden community (fallback: name prefix), so no page is an unnavigable wall
of links.

## Tiering (complexity → model)

Computed programmatically per unit in `build_manifest.py` from index signals —
no tokens spent. Score = weighted sum of:

- **fan-in**: resolved `occurrences` targeting the unit's entities from other
  units — the dominant term, and the only one with real dynamic range
  (514,736 resolved occurrences)
- **inheritance weight**: rows in `inherit_closure` where the unit declares the
  ancestor. Note the modest scale — 1,946 `bases` rows, only 1,194 resolved to
  an in-tree base, 1,734 closure rows — so this is a tie-breaker, not a driver;
  weight it accordingly and do not expect it to lift many units on its own
- **template density**: `is_template` entities (1,828 across the tree) / total
- **size**: lines (both files)
- **member count** and **macro definitions**
- **component prior**: `model`, `app-logic`, `maths`, `scribe`, `opengl`, `global` +1 tier bias;
  `qt-widgets` dialogs, `unit-test`, `cli` −1; `deprecated` forced to tier 3

Cut points target roughly: **Tier 1 ≈ 10–15%** (core engine: revisioned model,
reconstruction/layer-proxy machinery, spherical maths, Scribe, GL multi-resolution
rasters) — strong model (Opus). **Tier 2 ≈ 45%** (typical widgets, readers/writers,
visitors) — mid model (Sonnet). **Tier 3 ≈ 40%** (boilerplate dialogs, deprecated,
tests, property-value leaf types) — cheap model (Haiku). Tiers are stored in the
manifest; print the distribution and the top-50 tier-1 list for the user to sanity-check
before spending tokens.

## Pipeline steps

### 1. `scripts/build_manifest.py`

Read `gplates.db` → pair files into units → compute SHA256 over LF-normalized
content of each member file (cache key; CRLF-safe per structured-documentation) →
assign component → compute tier signals and tier → resolve page paths, detecting
case-insensitive collisions (disambiguate with a short hash suffix; record in
`path_map.json`) → write `manifest.jsonl`. On re-run: units whose member hashes
all match the previous manifest keep their tier, page, and `done` status.

### 2. `scripts/gen_skeleton.py`

Emit every page **with all structural content filled in programmatically** and
prose left as placeholders.

**One canonical template per page kind** (unit, component, TOC), defined in a
single place in the script — never string-concatenated ad hoc. The template
emits **every section unconditionally, in fixed order**; a section with no data
renders an explicit `*None.*` line rather than being skipped. That makes a
missing field structurally impossible, keeps every page's heading sequence
identical (lintable, see below), and keeps regeneration diffs stable.

Unit page sections, in order:

1. H1 (unit name), breadcrumb links (TOC ‹ component), source paths + line counts
2. `## Overview` — prose placeholder (what/why/how, 1–3 paragraphs)
3. `## Declared types` table: name, kind, bases (linked when in-tree), template params — from `entities`/`bases`
4. `## Members` — one table per public type: signature, access — from `entities`
5. `## Free functions and macros` declared here — from `entities`
6. `## Notes` — prose placeholder (invariants, gotchas, threading, ownership — only if genuinely useful; the agent replaces the block with `*None.*` rather than padding)
7. `## Used by`: top in-tree dependents by fan-in, linked — from `occurrences` + `includes`
8. `## Related`: ui form / shaders / signals-slots / py_api rows (`*None.*` when absent)
9. `## Explore`: 2–3 concrete `gpq` command lines for this unit

**Markdown correctness is a generator responsibility**, not a reviewer hope.
All interpolated values pass through two helpers used everywhere:

- `md_code(text)` — wraps identifiers, signatures, types and paths in code
  spans, so `<T>`, `*`, `_`, `&` and `|` in C++ signatures cannot corrupt the
  page; escapes `|` inside table cells; uses double-backtick spans when the
  value itself contains a backtick.
- `md_link(unit_id, anchor=None)` — the only way links are produced, resolving
  through `path_map.json` with anchors slugified by one shared function (the
  same one `verify_book.py` uses to check them).

Tables are emitted by a `md_table(headers, rows)` helper that asserts every row
has the same arity as the header — a short row raises at generation time
instead of rendering a broken table.

**Prose placeholders** use a grammar chosen to be unmistakable and impossible
to confuse with code or normal Markdown (verified: `SELECT COUNT(*) FROM lines WHERE text LIKE '%[[[%'` returns **0**
across all 843,998 indexed lines; re-assert this at generation time):

```
[[[PROSE overview unit=app-logic/ReconstructionTree tier=1]]]
Replace this whole block (markers included) with the Overview prose.
[[[/PROSE]]]
```

Rules: opener and closer each on their own line; the agent replaces the entire
block including both markers; `unit=` carries the manifest id so a misplaced
edit is traceable; the token is trivially greppable (`\[\[\[PROSE`) and, unlike
an HTML comment, **visible in rendered Markdown**, so an unfilled page is
obvious to a human reader too.

Extract the Doxygen/comment block preceding each type/function declaration
(from `lines`) and place it under the table row as a starting description —
tier-3 agents mostly verify and compress these rather than reading code.

Also generate: component pages (member tables with placeholder one-liners,
one `[[[PROSE component ...]]]` block), `TOC.md`, and the index files with
`(pending)` descriptions. Store unit→unit edges in `refgraph.json`.

`gen_skeleton.py --lint` re-parses every emitted page and asserts: the required
heading sequence appears exactly once and in template order, every table is
well-formed, and each expected placeholder block (or its filled replacement) is
present. Run it as the last step of generation, and again from
`verify_book.py`.

### 3. `scripts/gen_indexes.py`

Regenerated (idempotent) from `entities` + `descriptions.jsonl`:

- **Components.md** — every component: name, responsibility one-liner, unit count, link.
- **Type indexes** — all in-tree type definitions (`is_def=1`), split by kind to
  keep each file light. Verified counts: **Classes.md** (`class` 2,041 +
  `union` 6), **Structs.md** (761), **Enums.md** (297), **Typedefs.md**
  (`typedef` 2,492 + `alias` 51).
  Alphabetical, grouped A–Z, each row `Name — description` linking to its unit
  page. Namespace-qualified where ambiguous.
- **Functions.md** — `kind='function'`, `is_def=1`, at namespace/global scope (2,069 rows), same format.
- **Macros.md** — `macro` (1,398) + `macro_function` (86) = 1,484 rows, same format.

Descriptions start from extracted Doxygen text, and are overwritten by the
one-liners the prose agents emit (step 4), so the indexes sharpen as passes complete.

### 4. Prose pass — parallel sub-agents

Batches of 8–12 units, homogeneous by (tier, component). Scheduler reads
`progress.json`, marks a batch `in-flight`, launches agents in parallel; each agent:

- gets: component responsibility paragraph, the batch's skeleton pages, and the
  `gpq` cheat-sheet (`def --body`, `uses`, `hier`, `members`)
- reads real code via `gpq` (tier 1: read the unit fully; tier 3: skim declarations + Doxygen)
- replaces each `[[[PROSE ...]]]…[[[/PROSE]]]` block in place (markers
  included — no marker text may survive), and appends one JSONL line per public
  entity (`{qname, oneliner}`) to a per-batch file merged into `descriptions.jsonl`
- **prose rules** (put verbatim in the agent prompt): explain purpose, design
  intent, and non-obvious behavior only; never restate what the structural tables
  already show; never speculate — every claim must come from code the agent
  actually read; if there is nothing beyond the tables to say, say nothing
- model by tier: tier 1 → Opus-class, tier 2 → Sonnet-class, tier 3 → Haiku-class

Batch completion is recorded before the next wave starts; a crash costs at most
one wave. Failed units are retried once, then flagged in `progress.json`.

### 5. Component synthesis (vertical propagation)

After a component's units are done, one tier-appropriate agent per component reads
its unit overviews and writes the component page prose: responsibilities, the 5–10
load-bearing units, how it connects to neighboring components (edges from
`refgraph.json` aggregated to component level). Then one Opus-class agent writes
the TOC project overview from the finished component pages — the "read this first"
map of the reconstruction pipeline (model → app-logic → presentation →
view-operations/gui → opengl).

### 6. `scripts/verify_book.py` — gate before declaring done

Programmatic checks, all must pass:

- every `files` row reachable: mapped to a unit page linked from its component page, or present in a component-page table
- every index row's link resolves to an existing page + anchor; every unit page links back to TOC and component
- no `[[[PROSE` / `[[[/PROSE]]]` or `(pending)` markers anywhere in `book/`
- `gen_skeleton.py --lint` passes: every page has the full heading sequence in
  template order (empty sections as explicit `*None.*`, never omitted) and all
  tables are well-formed
- no case-insensitive path collisions in `book/`
- every type/function/macro definition in `entities` appears in exactly one index

Plus a small sampled AI review (structured-documentation step 15, ≤6 rounds): pick
~20 pages across tiers, check the prose answers "what is this and when do I touch
it" without opening the source; regressions send those units back to step 4.

### 7. Incremental refresh

Re-run order after a source/index update: `build_manifest.py` (hash diff) →
`gen_skeleton.py --only-changed` (regenerates structural tables everywhere — cheap
and programmatic — but preserves existing prose blocks for unchanged units) →
prose pass over changed units only → re-synthesize only components containing
changed units → `gen_indexes.py` → `verify_book.py`.

## Cost envelope

1,372 unit pages at the target cut points: ≈180 tier-1 (Opus), ≈620 tier-2
(Sonnet), ≈570 tier-3 (Haiku), plus ~27 component syntheses, the TOC overview
and verification samples. Skeleton, indexes, coverage, and
cross-references cost zero AI tokens — they are all derived from the SQLite index.
Present the tier distribution and this estimate to the user for approval **before**
launching the prose pass.

## Order of implementation

1. Write `build_manifest.py`; run; review tier distribution with user.
2. Write `gen_skeleton.py` + `gen_indexes.py`; run; run `verify_book.py`
   (coverage + links must already pass with prose markers allowed via `--allow-pending`).
3. Prose pass tier 3 first (cheap dry run of the harness), then tier 2, then tier 1.
4. Component synthesis, TOC overview.
5. Full `verify_book.py`, sampled review loop, final summary of any recorded gaps.
