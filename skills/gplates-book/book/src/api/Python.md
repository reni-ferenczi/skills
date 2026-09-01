# Python

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 740 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/api/Python.cc` | C++ | 80 |

## Overview

This file defines the module initialization for pygplates, the standalone Python extension module. It declares and calls export functions from across the api directory to register all Python bindings: feature collections, features, reconstruction functions, GUI controls, and utility functions. The `BOOST_PYTHON_MODULE(pygplates)` macro serves as the module entry point. Some exports are conditional on `GPLATES_PYTHON_EMBEDDING` to distinguish between the embedded Python console (inside GPlates) and the standalone module.

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

This file has no header; it is purely an initialization aggregate. The build configuration determines which exports are included via `GPLATES_PYTHON_EMBEDDING` to support both embedded and standalone use.

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/api/Python.cc
```
