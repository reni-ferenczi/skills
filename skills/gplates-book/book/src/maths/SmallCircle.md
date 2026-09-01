# SmallCircle

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 677 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/SmallCircle.h` | C++ | 243 |
| `src/maths/SmallCircle.cc` | C++ | 141 |

## Overview

[[[PROSE overview unit=maths/SmallCircle tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::SmallCircle`](#gplatesmathssmallcircle) | class | — | — | 0 | A small circle of a unit sphere. |

## Members

### `GPlatesMaths::SmallCircle`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( const UnitVector3D &axis, const PointOnSphere &p)` | method | `SmallCircle` | public | Create a small circle, given its axis and a point. |
| `create_colatitude( const UnitVector3D &axis, const real_t &colat)` | method | `SmallCircle` | public | Create a small circle, given its axis and the "colatitude" of the small circle around the "North Pole" of its axis. @image html fig\_small\_circle.png @image latex fig\_small\_circle.eps width=2.3in ViolatedClassInvariantException if ... |
| `create_cosine_colatitude( const UnitVector3D &axis, const real_t &cos_colat)` | method | `SmallCircle` | public | Create a small circle, given its axis and the cosine of the "colatitude" of the small circle around the "North Pole" of its axis. axis and circumference (aka the "colatitude"). |
| `colatitude()` | method | `real_t` | public | — |
| `contains( const PointOnSphere &pt)` | method | `bool` | public | Evaluate whether the point pt lies on this small circle. |
| `intersection( const GreatCircle &other, std::vector<PointOnSphere> &points)` | method | `unsigned int` | public | Find the intersection points (if any) of this SmallCircle and the given GreatCircle. |
| `AssertInvariantHolds()` | method | `void` | protected | Assert the class invariant: that the cosine of the colatitude lies within the range \[-1, 1\]. |
| `d_axis` | field | `UnitVector3D` | private | — |
| `d_cos_colat` | field | `real_t` | private | The cosine of the colatitude. |
| `d_colat` | field | `boost::optional<real_t>` | private | The colatitude in radians. |
| `SmallCircle( const UnitVector3D &axis, const real_t &cos_colat, boost::optional<real_t> colat = boost::none)` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_MATHS_SMALLCIRCLE_H_` | macro | `None` | — |
| `tessellate( std::vector<PointOnSphere> &tessellation_points, const SmallCircle &small_circle, const real_t &max_segment_angular_extent)` | function | `void` | Uniformly subdivides a small circle into smaller segments and appends the sequence of subdivided points to tessellation\_points. |

## Notes

[[[PROSE notes unit=maths/SmallCircle tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [canvas-tools/CreateSmallCircle](../canvas-tools/CreateSmallCircle.md) | canvas-tools | 9 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 6 |
| [maths/deprecated/GridOnSphere](deprecated/GridOnSphere.md) | maths | 6 |
| [qt-widgets/deprecated/SmallCircleManager](../qt-widgets/deprecated/SmallCircleManager.md) | qt-widgets | 6 |
| [qt-widgets/SmallCircleWidget](../qt-widgets/SmallCircleWidget.md) | qt-widgets | 5 |
| [view-operations/RenderedSmallCircle](../view-operations/RenderedSmallCircle.md) | view-operations | 5 |
| [gui/SphericalGrid](../gui/SphericalGrid.md) | gui | 4 |
| [qt-widgets/CreateSmallCircleDialog](../qt-widgets/CreateSmallCircleDialog.md) | qt-widgets | 4 |
| [qt-widgets/CreateSmallCircleFeatureDialog](../qt-widgets/CreateSmallCircleFeatureDialog.md) | qt-widgets | 4 |
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 2 |
| [maths/FiniteRotation](FiniteRotation.md) | maths | 2 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 2 |
| [view-operations/RenderedGeometryFactory](../view-operations/RenderedGeometryFactory.md) | view-operations | 2 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 1 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 1 |
| [maths/ConstGeometryOnSphereVisitor](ConstGeometryOnSphereVisitor.md) | maths | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/SmallCircle.h
python scripts/gpq.py def GPlatesMaths::SmallCircle --body
python scripts/gpq.py uses SmallCircle --kind class
python scripts/gpq.py hier SmallCircle
```
