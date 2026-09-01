# GnomonicProjection

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 644 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/GnomonicProjection.h` | C++ | 259 |
| `src/maths/GnomonicProjection.cc` | C++ | 150 |

## Overview

[[[PROSE overview unit=maths/GnomonicProjection tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::GnomonicProjection`](#gplatesmathsgnomonicprojection) | class | — | — | 0 | A projection from 3D points on unit sphere to a 2D tangent plane. |

## Members

### `GPlatesMaths::GnomonicProjection`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GnomonicProjection( const PointOnSphere &tangent_point, const AngularDistance &maximum_projection_angle)` | constructor | `None` | public | The tangent plane touches the unit sphere at position tangent\_point (which is also the direction of the tangent plane normal). |
| `GnomonicProjection( const UnitVector3D &tangent_plane_normal, const UnitVector3D &tangent_plane_x_axis, const UnitVector3D &tangent_plane_y_axis, const AngularDistance &maximum_projection_angle)` | constructor | `None` | public | The tangent plane touches the unit sphere at position PointOnSphere(tangent\_plane\_normal). |
| `get_tangent_point()` | method | `PointOnSphere` | public | Returns the point where the tangent plane touches the unit sphere. |
| `project_from_point_on_sphere( const PointOnSphere &point)` | method | `boost::optional<Point2Type>` | public | Convenient overload to return a template 2D point type. |
| `project_from_lat_lon( const LatLonPoint &point)` | method | `boost::optional<QPointF>` | public | Project a 3D point in Spherical (lon,lat) space to the tangent plane (x,y) space. |
| `unproject_to_point_on_sphere( const QPointF &point)` | method | `PointOnSphere` | public | Project a point in the tangent plane (x,y) space to Cartesian (x,y,z) space. |
| `unproject_to_point_on_sphere( const Point2Type &point)` | method | `PointOnSphere` | public | Convenient overload to accept a template 2D point type. |
| `unproject_to_lat_lon( const QPointF &point)` | method | `LatLonPoint` | public | Project a point in the tangent plane (x,y) space to Spherical (lon,lat) space. |
| `unproject_to_lat_lon( const Point2Type &point)` | method | `LatLonPoint` | public | Convenient overload to accept a template 2D point type. |
| `TangentPlaneFrame` | struct | `None` | private | The axes of the tangent plane. |
| `get_tangent_plane_frame( const UnitVector3D &tangent_plane_normal)` | method | `TangentPlaneFrame` | private | Calculate a tangent plane frame given only a tangent plane normal. |
| `d_tangent_plate_frame` | field | `TangentPlaneFrame` | private | — |
| `d_minimum_projection_cosine` | field | `double` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_orthonormal_vector( const UnitVector3D &point, const UnitVector3D &plane_normal)` | function | `UnitVector3D` | Projects a unit vector point onto the plane whose normal is plane\_normal and returns normalised version of projected point. |
| `GPLATES_MATHS_GNOMONICPROJECTION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=maths/GnomonicProjection tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/PolygonMesh](PolygonMesh.md) | maths | 7 |
| [maths/PolygonOrientation](PolygonOrientation.md) | maths | 7 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/GnomonicProjection.h
python scripts/gpq.py def GPlatesMaths::GnomonicProjection --body
python scripts/gpq.py uses GnomonicProjection --kind class
python scripts/gpq.py hier GnomonicProjection
```
