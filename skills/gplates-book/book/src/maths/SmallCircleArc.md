# SmallCircleArc

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 645 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/SmallCircleArc.h` | C++ | 181 |
| `src/maths/SmallCircleArc.cc` | C++ | 85 |

## Overview

`SmallCircleArc` is the bounded counterpart to `SmallCircle`: instead of a colatitude, it is defined by a rotation axis, a start point, and an angular extent, with `end_point()` computed on demand by applying `Rotation::create(d_axis, d_angular_extent)` to the start point rather than being stored. The angular extent is constrained to `[0, 2*PI]` as an anti-clockwise rotation about the axis — `0` collapses the arc to a point, `2*PI` makes it a full small circle. As with `SmallCircle`, a degenerate arc (start point coincident with the axis or its antipode) and an arc whose colatitude is exactly pi (technically a great circle arc) are both valid, not error cases.

The free `tessellate()` function subdivides an arc into a uniform sequence of points, each segment spanning an equal angle bounded by the caller's maximum, for callers such as renderers that need to draw a small circle arc as a sequence of straight segments.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::SmallCircleArc`](#gplatesmathssmallcirclearc) | class | — | — | 0 | A small circle arc on the surface of a sphere. |

## Members

### `GPlatesMaths::SmallCircleArc`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( const UnitVector3D &axis_, const PointOnSphere &start_point_, const double &angular_extent_)` | method | `SmallCircleArc` | public | Create a small circle arc, given its axis, starting point and angular extent. |
| `end_point()` | method | `PointOnSphere` | public | Return the end-point of the arc. |
| `colatitude()` | method | `real_t` | public | The colatitude angle (angle from the axis vector to a point on the small circle arc). |
| `cos_colatitude()` | method | `real_t` | public | The cosine of the colatitude angle. |
| `AssertInvariantHolds()` | method | `void` | protected | Assert the class invariant: that the cosine of the colatitude lies within the range \[-1, 1\]. |
| `d_axis` | field | `UnitVector3D` | private | — |
| `d_start_point` | field | `PointOnSphere` | private | — |
| `d_angular_extent` | field | `real_t` | private | — |
| `SmallCircleArc( const UnitVector3D &axis_, const PointOnSphere &start_point_, const double &angular_extent_)` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_SMALLCIRCLEARC_H` | macro | `None` | — |
| `tessellate( std::vector<PointOnSphere> &tessellation_points, const SmallCircleArc &small_circle_arc, const real_t &max_segment_angular_extent)` | function | `void` | Uniformly subdivides a small circle arc into smaller segments and appends the sequence of subdivided points to tessellation\_points. |

## Notes

Class invariant: the cosine of the colatitude (the dot product of the axis and the start point) must lie in `[-1, 1]`; the private constructor calls `AssertInvariantHolds()` and throws `ViolatedClassInvariantException` if it does not. Unlike `SmallCircle`, `colatitude()` here recomputes `acos()` on every call rather than caching it.

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/DateLineWrapper](DateLineWrapper.md) | maths | 37 |
| [maths/GreatCircleArc](GreatCircleArc.md) | maths | 23 |
| [canvas-tools/MeasureDistance](../canvas-tools/MeasureDistance.md) | canvas-tools | 7 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 4 |
| [maths/GeometryInterpolation](GeometryInterpolation.md) | maths | 4 |
| [view-operations/RenderedSmallCircleArc](../view-operations/RenderedSmallCircleArc.md) | view-operations | 4 |
| [app-logic/ResolvedSubSegmentRangeInSection](../app-logic/ResolvedSubSegmentRangeInSection.md) | app-logic | 3 |
| [maths/PointInPolygon](PointInPolygon.md) | maths | 3 |
| [maths/SphericalArea](SphericalArea.md) | maths | 3 |
| [opengl/GLScalarField3D](../opengl/GLScalarField3D.md) | opengl | 3 |
| [view-operations/RenderedGeometryFactory](../view-operations/RenderedGeometryFactory.md) | view-operations | 3 |
| [gui/FeatureTableModel](../gui/FeatureTableModel.md) | gui | 2 |
| [maths/Centroid](Centroid.md) | maths | 2 |
| [maths/GeometryIntersect](GeometryIntersect.md) | maths | 2 |
| [maths/PolygonOnSphere](PolygonOnSphere.md) | maths | 2 |
| [maths/PolylineOnSphere](PolylineOnSphere.md) | maths | 2 |
| [opengl/GLRasterCoRegistration](../opengl/GLRasterCoRegistration.md) | opengl | 2 |
| [app-logic/ResolvedTopologicalSubSegmentImpl](../app-logic/ResolvedTopologicalSubSegmentImpl.md) | app-logic | 1 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 1 |
| [maths/FiniteRotation](FiniteRotation.md) | maths | 1 |

*... and 1 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/SmallCircleArc.h
python scripts/gpq.py def GPlatesMaths::SmallCircleArc --body
python scripts/gpq.py uses SmallCircleArc --kind class
python scripts/gpq.py hier SmallCircleArc
```
