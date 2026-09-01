# SphericalArea

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 945 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/SphericalArea.h` | C++ | 186 |
| `src/maths/SphericalArea.cc` | C++ | 406 |

## Overview

A free-function namespace for computing signed spherical areas, on a unit-radius sphere, of `PolygonOnSphere` rings and of triangles bounded by points and `GreatCircleArc` edges. `calculate_polygon_signed_area()` (and the exterior/interior ring variants) triangulate by fanning from `polygon.get_boundary_centroid()`: for each boundary edge it forms a spherical triangle centroid-to-edge-start-to-edge-end-back-to-centroid and sums `calculate_spherical_triangle_signed_area()` over the edges. Each triangle's signed area is the spherical excess — the sum of its three internal angles minus pi for a counter-clockwise triangle, or plus pi for clockwise — computed via the internal `calculate_angle_between_adjacent_non_zero_length_edges()` helper.

Interior rings are not required to carry the opposite winding to the exterior ring (unlike some other libraries); `calculate_polygon_signed_area()` instead forces each interior ring's contribution to oppose the exterior ring's sign, so holes always reduce the exterior area regardless of how they were wound. Every `..._area()` function is a thin `abs()` wrapper around its `..._signed_area()` counterpart. Callers who already have both a point and its bounding `GreatCircleArc` should prefer the two-argument `calculate_spherical_triangle_signed_area()` overload over building points and calling the three-point overload, since the header calls it out as more efficient. To convert any of these unit-sphere areas to Earth's actual surface area, multiply by the square of `GPlatesUtils::Earth`'s radius.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `calculate_angle_between_adjacent_non_zero_length_edges( const GreatCircleArc &first_edge, const GreatCircleArc &second_edge)` | function | `double` | Calculates the angle, in radians, between two adjacent great circle arcs. |
| `calculate_spherical_triangle_signed_area( const GreatCircleArc &first_edge, const GreatCircleArc &second_edge, const GreatCircleArc &third_edge)` | function | `real_t` | Calculates the \*signed\* spherical area of the spherical triangle bounded by the specified edges. |
| `GPLATES_MATHS_SPHERICALAREA_H` | macro | `None` | — |
| `calculate_polygon_signed_area( const PolygonOnSphere &polygon)` | function | `real_t` | Calculates the \*signed\* spherical area of a polygon-on-sphere. |
| `calculate_polygon_area( const PolygonOnSphere &polygon)` | function | `real_t` | Same as calculate\_polygon\_signed\_area but returns the absolute value of the area. |
| `calculate_polygon_exterior_ring_signed_area( const PolygonOnSphere &polygon)` | function | `real_t` | Calculates the \*signed\* spherical area of the exterior ring of a polygon. |
| `calculate_polygon_exterior_ring_area( const PolygonOnSphere &polygon)` | function | `real_t` | Same as calculate\_polygon\_exterior\_ring\_signed\_area but returns the absolute value of the area. |
| `calculate_polygon_interior_ring_signed_area( const PolygonOnSphere &polygon, unsigned int interior_ring_index)` | function | `real_t` | Calculates the \*signed\* spherical area of the interior ring at the specified interior ring index of a polygon. |
| `calculate_polygon_interior_ring_area( const PolygonOnSphere &polygon, unsigned int interior_ring_index)` | function | `real_t` | Same as calculate\_polygon\_interior\_ring\_signed\_area but returns the absolute value of the area. |
| `calculate_spherical_triangle_signed_area( const PointOnSphere &point, const GreatCircleArc &edge)` | function | `real_t` | Calculates the \*signed\* spherical area of the spherical triangle bounded by the specified point and edge. |
| `calculate_spherical_triangle_signed_area( const PointOnSphere &first_point, const PointOnSphere &second_point, const PointOnSphere &third_point)` | function | `real_t` | Calculates the \*signed\* spherical area of the spherical triangle bounded by the specified points. |
| `calculate_spherical_triangle_area( const PointOnSphere &point, const GreatCircleArc &edge)` | function | `real_t` | Same as calculate\_spherical\_triangle\_signed\_area but returns the absolute value of the area. |
| `calculate_spherical_triangle_area( const PointOnSphere &first_point, const PointOnSphere &second_point, const PointOnSphere &third_point)` | function | `real_t` | Same as calculate\_spherical\_triangle\_signed\_area but returns the absolute value of the area. |

## Notes

`calculate_polygon_area()` is guaranteed less than `2 * PI` (a hemisphere): a polygon's boundary always bounds two areas on the sphere (the small "inside" and the large "outside"), and which one a *signed* calculation actually lands on depends on the polygon's orientation, but `calculate_polygon_area()` always reports the smaller of the two, making it orientation-agnostic.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 7 |
| [maths/PolygonOrientation](PolygonOrientation.md) | maths | 5 |
| [maths/Centroid](Centroid.md) | maths | 3 |
| [maths/PolygonOnSphere](PolygonOnSphere.md) | maths | 3 |
| [canvas-tools/MeasureDistanceState](../canvas-tools/MeasureDistanceState.md) | canvas-tools | 1 |
| [data-mining/DataSelector](../data-mining/DataSelector.md) | data-mining | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/SphericalArea.h
```
