# PythonWrapper

[Book TOC](../../../TOC.md) · [maths](../../../components/maths.md) · cluster Community 2 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/deprecated/PythonWrapper.cc` | C++ | 43 |

## Overview

A deprecated Boost.Python module entry point that wraps core maths types (`PointOnSphere`, `PolylineOnSphere`, `Real`, `UnitVector3D`, `Vector3D`) for Python access. The `BOOST_PYTHON_MODULE(_maths)` macro builds a Python extension module by delegating to export functions defined in the respective type headers. This was part of an early Python binding strategy that has since evolved.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `BOOST_PYTHON_MODULE(_maths)` | function | `None` | — |

## Notes

*None.*

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/deprecated/PythonWrapper.cc
```
