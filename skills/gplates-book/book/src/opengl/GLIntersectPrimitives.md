# GLIntersectPrimitives

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 717 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLIntersectPrimitives.h` | C++ | 633 |
| `src/opengl/GLIntersectPrimitives.cc` | C++ | 510 |

## Overview

`GLIntersectPrimitives` supplies the geometric primitive types — `Plane`, `Ray`, `Sphere`, `OrientedBoundingBox` — that `GLIntersect`'s intersection and culling routines (`intersect_ray_sphere`, `intersect_sphere_frustum`, `intersect_OBB_frustum`) operate on. `Plane` distinguishes between a cheap "unnormalised" form (`signed_distance_unnormalised`, `get_normal_unnormalised`, `get_signed_distance_to_origin_unnormalised`, all working directly with a possibly non-unit normal) and a slower "true" form (`signed_distance`, `get_normal`, `get_signed_distance_to_origin`) that scales by the inverse normal magnitude, so hot culling paths can stay in the unnormalised form and only pay the extra cost when an exact distance or normal is actually needed. `OrientedBoundingBox` has no such pair: it simply stores its three axes as non-unit vectors already scaled by their half-lengths.

`OrientedBoundingBoxBuilder` incrementally grows an `OrientedBoundingBox` around a fixed set of axes by tracking, per axis, the min/max projection of every point, arc, polygon or nested OBB added to it (`add`/`add_filled_polygon`); `get_oriented_bounding_box()` turns that running projection range into the final box. The free `create_oriented_bounding_box_builder` overloads pick a starting axis frame — from an explicit z-axis, from a z-axis plus an approximate y-axis, or from a `GPlatesMaths::BoundingSmallCircle` — when the caller does not already have an orthonormal basis to hand.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLIntersect::Plane`](#gplatesopenglglintersectplane) | class | — | — | 0 | A 3D infinite plane defined by a normal vector and any point on the plane. |
| [`GPlatesOpenGL::GLIntersect::Ray`](#gplatesopenglglintersectray) | class | — | — | 0 | A ray with an origin point and a unit vector direction. |
| [`GPlatesOpenGL::GLIntersect::Sphere`](#gplatesopenglglintersectsphere) | class | — | — | 0 | A sphere with a centre point and a radius. |
| [`GPlatesOpenGL::GLIntersect::OrientedBoundingBox`](#gplatesopenglglintersectorientedboundingbox) | class | — | — | 0 | A bounding box whose axes are orthogonal but not necessarily aligned with the coordinate axes. |
| [`GPlatesOpenGL::GLIntersect::OrientedBoundingBoxBuilder`](#gplatesopenglglintersectorientedboundingboxbuilder) | class | — | — | 0 | Used to incrementally build an OrientedBoundingBox. |

## Members

### `GPlatesOpenGL::GLIntersect::Plane`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `HalfSpaceType` | enum | `None` | public | The half space result when testing a point against a plane. |
| `Plane( const GPlatesMaths::Vector3D &normal, const GPlatesMaths::Vector3D &point_on_plane)` | constructor | `None` | public | Define a plane with a normal vector and any point on the plane. |
| `Plane( const GPlatesMaths::UnitVector3D &normal, const GPlatesMaths::Vector3D &point_on_plane)` | constructor | `None` | public | Define a plane with a normal vector and any point on the plane. |
| `Plane( const double &a, const double &b, const double &c, const double &d)` | constructor | `None` | public | Define a plane using plane coefficients (a,b,c,d). |
| `classify_point( const GPlatesMaths::Vector3D &point)` | method | `HalfSpaceType` | public | Returns whether point is in negative or positive half space or on the plane. |
| `classify_point( const GPlatesMaths::UnitVector3D &point)` | method | `HalfSpaceType` | public | Same as the other overloaded method but for unit vector points. |
| `signed_distance_unnormalised( const GPlatesMaths::Vector3D &point)` | method | `double` | public | Returns the signed distance of point to 'this' plane \*multiplied\* by the magnitude of 'this' plane's normal vector. |
| `signed_distance_unnormalised( const GPlatesMaths::UnitVector3D &point)` | method | `double` | public | Same as the other overloaded method but for unit vector points. |
| `signed_distance( const GPlatesMaths::Vector3D &point)` | method | `double` | public | Returns the 'true' signed distance of point to 'this' plane. |
| `signed_distance( const GPlatesMaths::UnitVector3D &point)` | method | `double` | public | Same as the other overloaded method but for unit vector points. |
| `get_normal()` | method | `GPlatesMaths::UnitVector3D` | public | Returns the (normalised) plane normal vector. |
| `get_signed_distance_to_origin()` | method | `double` | public | Returns the 'true' signed distance of the plane \*to\* the origin. |
| `d_normal` | field | `GPlatesMaths::Vector3D` | private | — |
| `d_signed_distance_to_origin_unnormalised` | field | `GPlatesMaths::real_t` | private | The signed distance \*from\* the plane \*to\* the origin multiplied. by the magnitude of the plane's normal vector. |
| `d_inv_magnitude_normal` | field | `boost::optional<GPlatesMaths::real_t>` | private | Inverse of the normal's magnitude. |

### `GPlatesOpenGL::GLIntersect::Ray`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Ray( const GPlatesMaths::Vector3D &ray_origin, const GPlatesMaths::UnitVector3D &ray_direction)` | constructor | `None` | public | — |
| `get_point_on_ray( const GPlatesMaths::real_t &t)` | method | `GPlatesMaths::Vector3D` | public | Returns position along ray that is t distance from ray's origin. |
| `d_origin` | field | `GPlatesMaths::Vector3D` | private | — |
| `d_direction` | field | `GPlatesMaths::UnitVector3D` | private | — |

### `GPlatesOpenGL::GLIntersect::Sphere`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Sphere( const GPlatesMaths::Vector3D &sphere_centre, const GPlatesMaths::real_t &sphere_radius)` | constructor | `None` | public | — |
| `d_centre` | field | `GPlatesMaths::Vector3D` | private | — |
| `d_radius` | field | `GPlatesMaths::real_t` | private | — |

### `GPlatesOpenGL::GLIntersect::OrientedBoundingBox`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `OrientedBoundingBox( const GPlatesMaths::Vector3D &centre, const GPlatesMaths::Vector3D &half_length_x_axis, const GPlatesMaths::Vector3D &half_length_y_axis, const GPlatesMaths::Vector3D &half_length_z_axis)` | constructor | `None` | public | Constructs a bounding box using the orthogonal axes and centre point. |
| `d_centre` | field | `GPlatesMaths::Vector3D` | private | The centre of the bounding box. |
| `d_half_length_x_axis` | field | `GPlatesMaths::Vector3D` | private | The orthogonal (not orthonormal) axes of the oriented bounding box. |
| `d_half_length_y_axis` | field | `GPlatesMaths::Vector3D` | private | — |
| `d_half_length_z_axis` | field | `GPlatesMaths::Vector3D` | private | — |

### `GPlatesOpenGL::GLIntersect::OrientedBoundingBoxBuilder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `OrientedBoundingBoxBuilder( const GPlatesMaths::UnitVector3D &obb_x_axis, const GPlatesMaths::UnitVector3D &obb_y_axis, const GPlatesMaths::UnitVector3D &obb_z_axis)` | constructor | `None` | public | Builds a bounding box that will be aligned with the specified axes. |
| `OrientedBoundingBoxBuilder( const GPlatesMaths::BoundingSmallCircle &bounding_small_circle, const GPlatesMaths::UnitVector3D &obb_x_axis, const GPlatesMaths::UnitVector3D &obb_y_axis)` | constructor | `None` | public | Creates a oriented bounding box builder that bounds a small circle - the OBB z-axis will be the small circle centre. |
| `add( const GPlatesMaths::UnitVector3D &point)` | method | `void` | public | Expand the current bounding box (if necessary) to include point. |
| `add( const GPlatesMaths::PointOnSphere &point)` | method | `void` | public | Expand the current bounding box (if necessary) to include point. |
| `add( const GPlatesMaths::GreatCircleArc &gca)` | method | `void` | public | Expand the current bounding box (if necessary) to include a great circle arc. |
| `add( GreatCircleArcForwardIter great_circle_arc_begin, GreatCircleArcForwardIter great_circle_arc_end)` | method | `void` | public | Expand the current bounding box (if necessary) to include a sequence of great circle arcs. |
| `add( const GPlatesMaths::MultiPointOnSphere &multi_point)` | method | `void` | public | Expand the current bounding box (if necessary) to include a multi-point. |
| `add( const GPlatesMaths::PolylineOnSphere &polyline)` | method | `void` | public | Expand the current bounding box (if necessary) to include a polyline. |
| `add( const GPlatesMaths::PolygonOnSphere &polygon)` | method | `void` | public | Expand the current bounding box (if necessary) to include a polygon. |
| `add_filled_polygon( const GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type &polygon)` | method | `void` | public | Expand the current bounding box (if necessary) to include a filled polygon. |
| `add( const OrientedBoundingBox &obb)` | method | `void` | public | Expand the current bounding box (if necessary) to include another oriented bounding box obb (that may have different axes). |
| `get_oriented_bounding_box()` | method | `OrientedBoundingBox` | public | Returns the oriented box bounding of all points added so far. |
| `d_x_axis` | field | `GPlatesMaths::UnitVector3D` | private | OBB axes |
| `d_y_axis` | field | `GPlatesMaths::UnitVector3D` | private | — |
| `d_z_axis` | field | `GPlatesMaths::UnitVector3D` | private | — |
| `d_min_dot_x_axis` | field | `double` | private | Min/max projection of bounded points onto OBB x-axis |
| `d_max_dot_x_axis` | field | `double` | private | — |
| `d_min_dot_y_axis` | field | `double` | private | Min/max projection of bounded points onto OBB y-axis |
| `d_max_dot_y_axis` | field | `double` | private | — |
| `d_min_dot_z_axis` | field | `double` | private | Min/max projection of bounded points onto OBB z-axis |
| `d_max_dot_z_axis` | field | `double` | private | — |
| `DEGENERATE_HALF_LENGTH_THRESHOLD` | field | `double` | private | The half-length for a degenerate dimension of the bounding box. |
| `add_projection( const OrientedBoundingBox &obb, GPlatesMaths::UnitVector3D &axis, double &min_dot_axis, double &max_dot_axis)` | method | `void` | private | Project obb along one of our axes and expand as necessary. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `DEGENERATE_HALF_LENGTH_THRESHOLD` | variable | `double` | This is the equivalent of about 6 metres (since globe has radius of ~6e+6 Kms). |
| `GPLATES_OPENGL_GLINTERSECTPRIMITIVES_H` | macro | `None` | — |
| `create_oriented_bounding_box_builder( const GPlatesMaths::Vector3D &obb_y_axis, const GPlatesMaths::UnitVector3D &obb_z_axis)` | function | `OrientedBoundingBoxBuilder` | Creates a oriented bounding box builder when you have the OBB z-axis and a y-axis direction that is not necessarily orthogonal to the z-axis. |
| `create_oriented_bounding_box_builder( const GPlatesMaths::UnitVector3D &obb_z_axis)` | function | `OrientedBoundingBoxBuilder` | Creates a oriented bounding box builder when you only have the OBB z-axis. |
| `create_oriented_bounding_box_builder( const GPlatesMaths::BoundingSmallCircle &bounding_small_circle)` | function | `OrientedBoundingBoxBuilder` | Creates a oriented bounding box builder that bounds a small circle - the OBB z-axis will be the small circle centre. |

## Notes

- Prefer the `_unnormalised` methods on `Plane` unless a true distance or normal is required; the normalised forms are documented as slower because they force a `1/magnitude` computation, which `Plane` lazily caches in `d_inv_magnitude_normal` on first use.
- `OrientedBoundingBox`'s half-length axis vectors and `OrientedBoundingBoxBuilder`'s input axes are expected to be orthogonal/orthonormal but this is not checked; near-orthogonal input still yields a convex (if slightly trapezoidal) volume rather than failing.
- `OrientedBoundingBoxBuilder::get_oriented_bounding_box()` throws `PreconditionViolationError` if no points were ever added, and clamps degenerate axes (all projected points coincide) to `DEGENERATE_HALF_LENGTH_THRESHOLD` rather than producing a zero-length axis.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLFrustum](GLFrustum.md) | opengl | 47 |
| [opengl/GLCubeSubdivision](GLCubeSubdivision.md) | opengl | 18 |
| [opengl/GLMultiResolutionRaster](GLMultiResolutionRaster.md) | opengl | 15 |
| [opengl/GLMultiResolutionMapCubeMesh](GLMultiResolutionMapCubeMesh.md) | opengl | 10 |
| [opengl/GLCubeSubdivisionCache](GLCubeSubdivisionCache.md) | opengl | 6 |
| [opengl/GLIntersect](GLIntersect.md) | opengl | 3 |
| [opengl/GLProjectionUtils](GLProjectionUtils.md) | opengl | 2 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLIntersectPrimitives.h
python scripts/gpq.py def GPlatesOpenGL::GLIntersect::Plane --body
python scripts/gpq.py uses Plane --kind class
python scripts/gpq.py hier Plane
```
