# ExternalResourceFailureException

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 541 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/global/ExternalResourceFailureException.h` | C++ | 58 |

## Overview

[[[PROSE overview unit=global/ExternalResourceFailureException tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGlobal::ExternalResourceFailureException`](#gplatesglobalexternalresourcefailureexception) | class | [`Exception`](GPlatesException.md) | — | 2 | This is the base class of all exceptions in GPlates which are due to the failure of some external resource. |

## Members

### `GPlatesGlobal::ExternalResourceFailureException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ExternalResourceFailureException( const GPlatesUtils::CallStack::Trace &exception_source)` | constructor | `None` | public | An alternative constructor that adds the location at which exception is thrown to the call stack trace. |
| `~ExternalResourceFailureException()` | destructor | `None` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GLOBAL_EXTERNALRESOURCEFAILUREEXCEPTION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=global/ExternalResourceFailureException tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/TrailingLatLonCoordinateException](../maths/TrailingLatLonCoordinateException.md) | maths | 5 |
| [maths/InvalidLatLonCoordinateException](../maths/InvalidLatLonCoordinateException.md) | maths | 4 |
| [opengl/GLCubeSubdivision](../opengl/GLCubeSubdivision.md) | opengl | 4 |
| [view-operations/RenderedGeometryFactory](../view-operations/RenderedGeometryFactory.md) | view-operations | 3 |
| [maths/SphericalArea](../maths/SphericalArea.md) | maths | 2 |
| [opengl/GLIntersectPrimitives](../opengl/GLIntersectPrimitives.md) | opengl | 2 |
| [view-operations/RenderedColouredPolygonOnSphere](../view-operations/RenderedColouredPolygonOnSphere.md) | view-operations | 2 |
| [view-operations/RenderedColouredPolylineOnSphere](../view-operations/RenderedColouredPolylineOnSphere.md) | view-operations | 2 |
| [view-operations/RenderedColouredTriangleSurfaceMesh](../view-operations/RenderedColouredTriangleSurfaceMesh.md) | view-operations | 2 |
| [maths/Rotation](../maths/Rotation.md) | maths | 1 |
| [maths/deprecated/GridOnSphere](../maths/deprecated/GridOnSphere.md) | maths | 1 |
| [maths/deprecated/PolylineIntersections_test](../maths/deprecated/PolylineIntersections_test.md) | maths | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/ExternalResourceFailureException.h
python scripts/gpq.py def GPlatesGlobal::ExternalResourceFailureException --body
python scripts/gpq.py uses ExternalResourceFailureException --kind class
python scripts/gpq.py hier ExternalResourceFailureException
```
