# SphericalArea

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 945 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/SphericalArea.h` | C++ | 186 |
| `src/maths/SphericalArea.cc` | C++ | 406 |

## Overview

[[[PROSE overview unit=maths/SphericalArea tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=maths/SphericalArea tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
