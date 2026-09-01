# GeometryForwardDeclarations

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 1765 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/GeometryForwardDeclarations.h` | C++ | 51 |

## Overview

Forward declarations for the spherical geometry classes (`PointOnSphere`, `PolylineOnSphere`, `PolygonOnSphere`, `MultiPointOnSphere`). These declarations support lightweight headers that need only type names and can use `intrusive_ptr` without full class definitions, reducing compilation dependencies. Use this header instead of including the full geometry headers when only a pointer or reference to a geometry type is needed.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_GEOMETRYFORWARDDECLARATIONS_H` | macro | `None` | — |

## Notes

*None.*

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/GeometryForwardDeclarations.h
```
