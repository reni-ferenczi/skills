# AngularDistance

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 27 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/AngularDistance.h` | C++ | 208 |
| `src/maths/AngularDistance.cc` | C++ | 36 |

## Overview

[[[PROSE overview unit=maths/AngularDistance tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::AngularDistance`](#gplatesmathsangulardistance) | class | `boost::less_than_comparable<AngularDistance, boost::equivalent<AngularDistance, boost::equality_comparable<AngularDistance> > >` | — | 0 | An angular distance stored as cosine instead of the actual angle. |

## Members

### `GPlatesMaths::AngularDistance`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ZERO` | field | `AngularDistance` | public | Angular distance of zero (radians). |
| `HALF_PI` | field | `AngularDistance` | public | Angular distance of PI/2 radians (90 degrees). |
| `PI` | field | `AngularDistance` | public | Angular distance of PI radians (180 degrees). |
| `create_from_cosine( const real_t &cosine)` | method | `AngularDistance` | public | Create from the cosine of the angular distance. |
| `create_from_angle( const real_t &angle)` | method | `AngularDistance` | public | Create from an angular distance (radians) in the range \[0, PI\]. |
| `calculate_angle()` | method | `real_t` | public | Calculates the angular distance (radians) from the cosine of the angular distance. |
| `operator<( const AngularDistance &rhs)` | operator | `bool` | public | Less than operator - all other operators (\<=, \>, \>=, ==, !=) provided by boost::less\_than\_comparable, boost::equivalent and boost::equality\_comparable. |
| `is_precisely_less_than( const AngularExtentOrDistance &rhs)` | method | `bool` | public | Similar to 'operator\<' except does not have an epsilon test. |
| `is_precisely_greater_than( const AngularExtentOrDistance &rhs)` | method | `bool` | public | Similar to 'operator\>' except does not have an epsilon test. |
| `d_cosine` | field | `real_t` | private | — |
| `AngularDistance( const real_t &cosine)` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `ZERO` | variable | `GPlatesMaths::AngularDistance` | — |
| `HALF_PI` | variable | `GPlatesMaths::AngularDistance` | — |
| `PI` | variable | `GPlatesMaths::AngularDistance` | — |
| `GPLATES_MATHS_ANGULARDISTANCE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=maths/AngularDistance tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ResolvedTriangulationNetwork](../app-logic/ResolvedTriangulationNetwork.md) | app-logic | 236 |
| [maths/SmallCircleBounds](SmallCircleBounds.md) | maths | 194 |
| [opengl/GLRasterCoRegistration](../opengl/GLRasterCoRegistration.md) | opengl | 189 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 181 |
| [maths/GeometryDistance](GeometryDistance.md) | maths | 173 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 158 |
| [app-logic/TopologyReconstruct](../app-logic/TopologyReconstruct.md) | app-logic | 157 |
| [opengl/GLIntersectPrimitives](../opengl/GLIntersectPrimitives.md) | opengl | 131 |
| [app-logic/ResolvedSubSegmentRangeInSection](../app-logic/ResolvedSubSegmentRangeInSection.md) | app-logic | 110 |
| [app-logic/PlateVelocityUtils](../app-logic/PlateVelocityUtils.md) | app-logic | 98 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 88 |
| [opengl/GLScalarField3D](../opengl/GLScalarField3D.md) | opengl | 82 |
| [maths/GreatCircleArc](GreatCircleArc.md) | maths | 74 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 73 |
| [utils/GeometryCreationUtils](../utils/GeometryCreationUtils.md) | utils | 61 |
| [maths/PolygonPartitioner](PolygonPartitioner.md) | maths | 58 |
| [maths/FiniteRotation](FiniteRotation.md) | maths | 56 |
| [qt-widgets/EditGeometryWidget](../qt-widgets/EditGeometryWidget.md) | qt-widgets | 49 |
| [view-operations/InsertVertexGeometryOperation](../view-operations/InsertVertexGeometryOperation.md) | view-operations | 49 |
| [view-operations/GeometryBuilder](../view-operations/GeometryBuilder.md) | view-operations | 48 |

*... and 86 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/AngularDistance.h
python scripts/gpq.py def GPlatesMaths::AngularDistance --body
python scripts/gpq.py uses AngularDistance --kind class
python scripts/gpq.py hier AngularDistance
```
