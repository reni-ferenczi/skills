# AzimuthalEqualAreaProjection

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 1146 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/AzimuthalEqualAreaProjection.h` | C++ | 162 |
| `src/maths/AzimuthalEqualAreaProjection.cc` | C++ | 158 |

## Overview

[[[PROSE overview unit=maths/AzimuthalEqualAreaProjection tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=maths/AzimuthalEqualAreaProjection tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
