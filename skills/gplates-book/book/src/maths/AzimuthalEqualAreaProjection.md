# AzimuthalEqualAreaProjection

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 1146 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/AzimuthalEqualAreaProjection.h` | C++ | 162 |
| `src/maths/AzimuthalEqualAreaProjection.cc` | C++ | 158 |

## Overview

Implements the Lambert azimuthal equal-area map projection, centred on an
arbitrary `LatLonPoint` (or `PointOnSphere`) rather than a pole. It converts
between spherical (lon, lat) or Cartesian (x, y, z) coordinates and a flat
(x, y) plane tangent at the centre of projection, in both directions.

The forward projection (`project_from_lat_lon`, `project_from_point_on_sphere`)
follows the standard closed-form formulas for the spherical Lambert azimuthal
equal-area projection, using the trigonometric identities for the centre
latitude cached in the constructor. The inverse (`unproject_to_lat_lon`,
`unproject_to_point_on_sphere`) special-cases the point exactly at the centre
of projection to avoid a division by zero, and special-cases a centre at
either pole to avoid the same problem in the longitude recovery. `projection_scale`
scales the projected plane coordinates on the way out and is undone on the way
back in, so a caller can work in whatever plane units it needs (for example
pixels) without affecting the unprojected result. Each direction is also
exposed as a template overload that constructs an arbitrary 2D point type from
the projected `QPointF`, letting callers avoid a Qt dependency in their own
point types.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::AzimuthalEqualAreaProjection`](#gplatesmathsazimuthalequalareaprojection) | class | — | — | 0 | Lambert Equal Area Projection http://mathworld.wolfram.com/LambertAzimuthalEqual-AreaProjection.html |

## Members

### `GPlatesMaths::AzimuthalEqualAreaProjection`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AzimuthalEqualAreaProjection( const LatLonPoint &center_of_projection, const double &projection_scale = 1.0)` | constructor | `None` | public | projection\_scale is a scale factor for the projected coordinates. |
| `AzimuthalEqualAreaProjection( const PointOnSphere &center_of_projection, const double &projection_scale = 1.0)` | constructor | `None` | public | projection\_scale is a scale factor for the projected coordinates. |
| `project_from_lat_lon( const LatLonPoint &point)` | method | `Point2Type` | public | Convenient overload to return a template 2D point type. |
| `project_from_point_on_sphere( const PointOnSphere &point)` | method | `Point2Type` | public | Convenient overload to return a template 2D point type. |
| `unproject_to_lat_lon( const QPointF &point)` | method | `LatLonPoint` | public | Project a point in Azimuthal Equal Area (x,y) space to Spherical (lon,lat) space. |
| `unproject_to_lat_lon( const Point2Type &point)` | method | `LatLonPoint` | public | Convenient overload to accept a template 2D point type. |
| `unproject_to_point_on_sphere( const QPointF &point)` | method | `PointOnSphere` | public | Project a point in Azimuthal Equal Area (x,y) space to Cartesian (x,y,z) space. |
| `unproject_to_point_on_sphere( const Point2Type &point)` | method | `PointOnSphere` | public | Convenient overload to accept a template 2D point type. |
| `d_center_of_projection` | field | `LatLonPoint` | private | — |
| `d_sin_center_of_projection_latitude` | field | `double` | private | — |
| `d_cos_center_of_projection_latitude` | field | `double` | private | — |
| `d_projection_scale` | field | `double` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_AZIMUTHALEQUALAREAPROJECTION_H` | macro | `None` | — |

## Notes

The object is immutable once constructed: the centre of projection, its cached
sine/cosine, and the projection scale are all `const` fields set in the
constructor.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ResolvedTriangulationDelaunay2](../app-logic/ResolvedTriangulationDelaunay2.md) | app-logic | 39 |
| [app-logic/ResolvedTriangulationNetwork](../app-logic/ResolvedTriangulationNetwork.md) | app-logic | 28 |
| [app-logic/GeometryCookieCutter](../app-logic/GeometryCookieCutter.md) | app-logic | 16 |
| [gui/ExportStageRotationAnimationStrategy](../gui/ExportStageRotationAnimationStrategy.md) | gui | 10 |
| [qt-widgets/CreateSmallCircleDialog](../qt-widgets/CreateSmallCircleDialog.md) | qt-widgets | 10 |
| [app-logic/AssignPlateIds](../app-logic/AssignPlateIds.md) | app-logic | 2 |
| [app-logic/Reconstruction](../app-logic/Reconstruction.md) | app-logic | 1 |
| [app-logic/ResolvedTopologicalNetwork](../app-logic/ResolvedTopologicalNetwork.md) | app-logic | 1 |
| [app-logic/TopologyUtils](../app-logic/TopologyUtils.md) | app-logic | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/AzimuthalEqualAreaProjection.h
python scripts/gpq.py def GPlatesMaths::AzimuthalEqualAreaProjection --body
python scripts/gpq.py uses AzimuthalEqualAreaProjection --kind class
python scripts/gpq.py hier AzimuthalEqualAreaProjection
```
