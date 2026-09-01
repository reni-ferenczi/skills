# GenericVectorOps3D

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 261 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/GenericVectorOps3D.h` | C++ | 111 |

## Overview

[[[PROSE overview unit=maths/GenericVectorOps3D tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::GenericVectorOps3D::ReturnType`](#gplatesmathsgenericvectorops3dreturntype) | struct | — | `< typename R >` | 0 | — |

## Members

### `GPlatesMaths::GenericVectorOps3D::ReturnType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `cross( const V1 &v1, const V2 &v2)` | method | `R` | public | — |
| `scale( const real_t s, const V v)` | method | `R` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_GENERICVECTOROPS3D_H` | macro | `None` | — |
| `dot( const V1 &v1, const V2 &v2)` | function | `real_t` | — |
| `negate( const V &v)` | function | `V` | — |
| `perpendicular( const V1 &v1, const V2 &v2)` | function | `bool` | — |

## Notes

[[[PROSE notes unit=maths/GenericVectorOps3D tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/GeometryInterpolation](GeometryInterpolation.md) | maths | 56 |
| [qt-widgets/FiniteRotationCalculatorDialog](../qt-widgets/FiniteRotationCalculatorDialog.md) | qt-widgets | 45 |
| [maths/PointInPolygon](PointInPolygon.md) | maths | 43 |
| [maths/GreatCircleArc](GreatCircleArc.md) | maths | 41 |
| [maths/SmallCircleBounds](SmallCircleBounds.md) | maths | 33 |
| [opengl/GLMatrix](../opengl/GLMatrix.md) | opengl | 28 |
| [maths/UnitVector3D](UnitVector3D.md) | maths | 27 |
| [view-operations/ChangeLightDirectionOperation](../view-operations/ChangeLightDirectionOperation.md) | view-operations | 22 |
| [gui/SimpleGlobeOrientation](../gui/SimpleGlobeOrientation.md) | gui | 20 |
| [opengl/GLVertex](../opengl/GLVertex.md) | opengl | 18 |
| [app-logic/ResolvedTriangulationNetwork](../app-logic/ResolvedTriangulationNetwork.md) | app-logic | 17 |
| [opengl/GLIntersectPrimitives](../opengl/GLIntersectPrimitives.md) | opengl | 17 |
| [gui/SceneLightingParameters](../gui/SceneLightingParameters.md) | gui | 16 |
| [maths/Vector3D](Vector3D.md) | maths | 16 |
| [view-operations/RenderedEllipse](../view-operations/RenderedEllipse.md) | view-operations | 14 |
| [opengl/GLProgramObject](../opengl/GLProgramObject.md) | opengl | 10 |
| [opengl/GLStateSets](../opengl/GLStateSets.md) | opengl | 10 |
| [view-operations/MovePoleOperation](../view-operations/MovePoleOperation.md) | view-operations | 10 |
| [app-logic/NetRotationUtils](../app-logic/NetRotationUtils.md) | app-logic | 9 |
| [maths/FiniteRotation](FiniteRotation.md) | maths | 9 |

*... and 55 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/GenericVectorOps3D.h
python scripts/gpq.py def GPlatesMaths::GenericVectorOps3D::ReturnType --body
python scripts/gpq.py uses ReturnType --kind struct
python scripts/gpq.py hier ReturnType
```
