# PythonWrapper

[Book TOC](../../../TOC.md) · [model](../../../components/model.md) · cluster Community 901 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/model/deprecated/PythonWrapper.cc` | C++ | 35 |

## Overview

This is a deprecated Boost.Python module wrapper for the legacy `_model` Python module. It exports `GPlatesModel` functionality to Python via the `BOOST_PYTHON_MODULE` macro. This module predates the modern GPlates Python API found in `src/api/`. Do not use this; it exists only for backward compatibility and is no longer maintained.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `BOOST_PYTHON_MODULE(_model)` | function | `None` | — |

## Notes

Deprecated. Use the Python API in `src/api/` instead. This module is not actively maintained and is kept only for backward compatibility with legacy scripts.

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/deprecated/PythonWrapper.cc
```
