# PyTopologyTools

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 4 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/api/PyTopologyTools.cc` | C++ | 78 |

## Overview

[[[PROSE overview unit=api/PyTopologyTools tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesApi::TopologyTools`](#gplatesapitopologytools) | class | — | — | 0 | — |

## Members

### `GPlatesApi::TopologyTools`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `sections_info(Feature feaure)` | method | `bp::list` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `export_topology_tools()` | function | `void` | — |

## Notes

[[[PROSE notes unit=api/PyTopologyTools tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

**Python bindings**

| Python name | Kind | Owner | C++ |
|---|---|---|---|
| `TopologyTools` | class | — | `TopologyTools` |
| `sections_info` | method | `TopologyTools` | `&TopologyTools::sections_info` |
| `sections_info` | staticmethod | `TopologyTools` | — |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/api/PyTopologyTools.cc
python scripts/gpq.py def GPlatesApi::TopologyTools --body
python scripts/gpq.py uses TopologyTools --kind class
python scripts/gpq.py hier TopologyTools
```
