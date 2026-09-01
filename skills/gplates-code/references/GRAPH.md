# Code graph and communities

An **optional** layer on top of the main index, built with
[Graphify](https://pypi.org/project/graphifyy/) and Leiden community detection.
It answers questions the entity index cannot: which cluster of the codebase a
symbol belongs to, what else belongs with it, and how symbols connect.

It does not replace anything. `decl`, `uses`, `hier` and `members` stay the
authoritative answers for declarations, usages and inheritance.

## Build it

```bash
python scripts/build_graph.py
```

About 100 seconds, producing `data/graph.db` (~47 MB): 52,594 nodes,
94,481 edges, 1,747 communities. Requires the main index and the uv
environment (`uv sync`) — `graphifyy[leiden]` is declared in `pyproject.toml`.

| Flag | Effect |
|---|---|
| `--check` | verify an existing graph and exit |
| `--no-cluster` | extract the graph but skip community detection |
| `--label` | name communities with an LLM instead of `Community N` |
| `--keep-mirror` | keep `data/graph-src` for debugging |

Rebuild it after rebuilding the main index — it stores paths and line numbers.

## Query it

```bash
python scripts/gpq.py community ReconstructLayerProxy   # which cluster is this in
python scripts/gpq.py community --list --limit 20       # biggest clusters
python scripts/gpq.py community --id 65                 # one cluster's members
python scripts/gpq.py neighbors ReconstructionTree      # direct graph edges
python scripts/gpq.py neighbors LayerProxy --relation inherits
```

`community <symbol>` prints the matching nodes, then the winning community with
its dominant directories and members. `neighbors` prints outgoing (`->`) and
incoming (`<-`) edges; filter with `--relation` (repeatable).

Edge relations present: `references`, `imports`, `contains`, `defines`, `calls`,
`method`, `inherits`, plus a few `imports_from` / `indirect_call` / `uses`.

`gpq sql` can reach the graph too — it is attached as schema `g`:

```bash
python scripts/gpq.py sql "SELECT id, size, top_dirs FROM g.communities ORDER BY size DESC LIMIT 5"
```

## Two GPlates-specific fixes

**Qt macros.** Graphify parses C++ with plain tree-sitter, which Qt's `Q_OBJECT`,
`signals:` and `SIGNAL()`/`SLOT()` defeat. Run directly on the GPlates tree it
reports **224 files with syntax errors**, several extracting *no* symbols at all.
So `build_graph.py` first mirrors the source through the same length-preserving
preparation the main index uses (`cpp_parse.prepare`). That drops it to **44**
and recovers whole dialog headers — `HellingerDialog.h` gains 133 nodes,
`TopologyTools.h` 105. Because the transform preserves byte offsets and line
counts, every line number in the graph still points at the real file.

**Read-only source.** Graphify writes `graphify-out/` beside the tree it graphs.
The mirror lives in `data/graph-src` and `GRAPHIFY_OUT` redirects the output, so
the GPlates source tree is never written to. The mirror is deleted after the
build unless `--keep-mirror` is passed; the handful of absolute paths graphify
records are rewritten back to the real source root, and a test asserts no path
still mentions the mirror.

## Stub nodes

Graphify creates a node for every name it sees, including forward declarations in
unrelated files. These **stubs** carry no source location and a misleading
community — the reference skill this was ported from warns you to spot them by
hand.

Here it is handled automatically: `community` and `neighbors` rank candidates
against the entity index, so a node sitting on a real definition always wins.
Each line is tagged `[def]`, `[ref]` or `[stub]`, and hidden stubs are counted:

```
ReconstructLayerProxy   src/app-logic/ReconstructLayerProxy.h:80   [def] -> community 65
# 10 stub/reference node(s) hidden - they carry no definition
```

If you ever see only `[stub]` rows, the name exists solely as a forward
declaration — look it up with `gpq decl` instead.

## Community names

By default communities are numbered (`Community 65`), because naming them needs
an LLM pass over all 1,747 clusters. `build_graph.py --label` runs it using
whatever backend graphify auto-detects. Numbered communities are still useful —
`top_dirs` usually identifies a cluster at a glance (community 65 is 72 nodes,
all in `src/app-logic`, centred on the reconstruct layer).

## Using graphify directly

The CLI in `.venv` offers traversals `gpq` does not wrap:

```bash
.venv/Scripts/graphify.exe explain "ReconstructLayerProxy" --graph data/graphify-out/graph.json
.venv/Scripts/graphify.exe path "LayerProxy" "ReconstructionTree" --graph data/graphify-out/graph.json
.venv/Scripts/graphify.exe affected "ApplicationState" --depth 1 --graph data/graphify-out/graph.json
.venv/Scripts/graphify.exe god-nodes --top 10 --graph data/graphify-out/graph.json
```

`explain`, `path` and `affected` on a **named symbol** are the reliable modes.
`query` with a natural-language question spends most of its budget on hub nodes;
prefer naming a concrete type and keep `--budget` small.

## Limits

- Communities come from graph structure, not meaning. They cluster code that is
  wired together, which usually but not always matches a concept.
- The graph is a snapshot. Rebuild after the source or the main index changes.
- Graphify's extraction is independent of the main index's, so node counts and
  entity counts do not line up: the graph has 52,594 nodes against 121k entities,
  because it does not record parameters or locals.
- 44 files still have partial extraction, mostly `#if`-heavy or Scribe export
  files. They contribute fewer nodes but are not otherwise special-cased.
- Clustering needs `graspologic` for the fast native Leiden backend, which has no
  wheel for Python 3.13 — hence `requires-python = ">=3.12,<3.13"` in
  `pyproject.toml`. Without it graphify silently falls back to single-core
  Louvain and takes tens of minutes; `build_graph.py` warns when that happens.
