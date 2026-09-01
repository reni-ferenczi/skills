# Python

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 740 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/api/Python.cc` | C++ | 80 |

## Overview

[[[PROSE overview unit=api/Python tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `export_console_reader()` | function | `void` | api directory. |
| `export_console_writer()` | function | `void` | — |
| `export_feature_collection()` | function | `void` | — |
| `export_instance()` | function | `void` | presentation directory. |
| `export_style()` | function | `void` | — |
| `export_main_window()` | function | `void` | qt-widgets directory. |
| `export_co_registration()` | function | `void` | — |
| `export_functions()` | function | `void` | — |
| `export_colour()` | function | `void` | — |
| `export_feature()` | function | `void` | — |
| `export_topology_tools()` | function | `void` | — |
| `export_coregistration_layer_proxy()` | function | `void` | — |
| `BOOST_PYTHON_MODULE(pygplates)` | function | `None` | — |

## Notes

[[[PROSE notes unit=api/Python tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/api/Python.cc
```
