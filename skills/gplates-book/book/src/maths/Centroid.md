# Centroid

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 5 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/Centroid.h` | C++ | 403 |
| `src/maths/Centroid.cc` | C++ | 233 |

## Overview

[[[PROSE overview unit=maths/Centroid tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `calculate_sum_area_weighted_centroids_in_polygon_ring( const PointOnSphere &polygon_centroid, const PolygonOnSphere::ring_const_iterator &ring_begin, const PolygonOnSphere::ring_const_iterator &ring_end)` | function | `Vector3D` | Calculate the sum of centroids of a sequence of spherical triangles formed by GreatCircleArc objects and a polygon centroid using an approximate area weighting of the spherical triangles. |
| `GPLATES_MATHS_CENTROID_H` | macro | `None` | — |
| `calculate_sum_points( PointForwardIter begin, PointForwardIter end)` | function | `Vector3D` | Returns the sum of the sequence of PointOnSphere objects. |
| `calculate_sum_vertices( UnitVector3DForwardIter begin, UnitVector3DForwardIter end)` | function | `Vector3D` | Returns the sum of the sequence of UnitVector3D objects. |
| `calculate_vertices_centroid( UnitVector3DForwardIter begin, UnitVector3DForwardIter end)` | function | `UnitVector3D` | Calculates the centroid of the sequence of UnitVector3D objects. |
| `calculate_points_centroid( PointForwardIter begin, PointForwardIter end)` | function | `UnitVector3D` | Calculates the centroid of the sequence of PointOnSphere objects. |
| `calculate_points_centroid( const PointOnSphere &point)` | function | `UnitVector3D` | Calculates the centroid of point - which is just point. |
| `calculate_points_centroid( const MultiPointOnSphere &multi_point)` | function | `UnitVector3D` | Calculates the centroid of the points in multi\_point. |
| `calculate_points_centroid( const PolylineOnSphere &polyline)` | function | `UnitVector3D` | Calculates the centroid of the points in polyline. |
| `calculate_points_centroid( const PolygonOnSphere &polygon, bool include_interior_rings = true)` | function | `UnitVector3D` | Calculates the centroid of the points in polygon. |
| `calculate_outline_centroid( EdgeForwardIter begin, EdgeForwardIter end)` | function | `UnitVector3D` | Calculates the centroid of a sequence of GreatCircleArc objects using an approximate arc-length weighted average of the arc centroids. |
| `calculate_outline_centroid( const PolylineOnSphere &polyline)` | function | `UnitVector3D` | Calculates the centroid of the great circle arc edges in polyline. |
| `calculate_outline_centroid( const PolygonOnSphere &polygon, bool use_interior_rings = true)` | function | `UnitVector3D` | Calculates the centroid of the great circle arc edges in polygon. |
| `calculate_interior_centroid( const PolygonOnSphere &polygon, bool use_interior_rings = true)` | function | `UnitVector3D` | Calculates the centroid of polygon using spherical area weighting. |
| `get_normalised_centroid_or_placeholder_centroid( const Vector3D &centroid, const UnitVector3D &placeholder_centroid)` | function | `UnitVector3D` | — |
| `calculate_sum_arc_length_weighted_centroids( EdgeForwardIter edges_begin, EdgeForwardIter edges_end)` | function | `Vector3D` | Calculate the sum of centroids of a sequence of GreatCircleArc objects using an approximate arc-length weighting of the arc centroids. |
| `calculate_sum_points( PointForwardIter points_begin, PointForwardIter points_end)` | function | `Vector3D` | — |
| `calculate_sum_vertices( UnitVector3DForwardIter points_begin, UnitVector3DForwardIter points_end)` | function | `Vector3D` | — |
| `calculate_vertices_centroid( UnitVector3DForwardIter points_begin, UnitVector3DForwardIter points_end)` | function | `UnitVector3D` | — |
| `calculate_points_centroid( PointForwardIter points_begin, PointForwardIter points_end)` | function | `UnitVector3D` | — |
| `calculate_outline_centroid( EdgeForwardIter edges_begin, EdgeForwardIter edges_end)` | function | `UnitVector3D` | — |

## Notes

[[[PROSE notes unit=maths/Centroid tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLFilledPolygonsGlobeView](../opengl/GLFilledPolygonsGlobeView.md) | opengl | 18 |
| [maths/PolygonOnSphere](PolygonOnSphere.md) | maths | 7 |
| [app-logic/ResolvedTriangulationDelaunay2](../app-logic/ResolvedTriangulationDelaunay2.md) | app-logic | 3 |
| [maths/MultiPointOnSphere](MultiPointOnSphere.md) | maths | 3 |
| [maths/PolyGreatCircleArcBoundingTree](PolyGreatCircleArcBoundingTree.md) | maths | 3 |
| [maths/PolylineOnSphere](PolylineOnSphere.md) | maths | 3 |
| [maths/PointInPolygon](PointInPolygon.md) | maths | 1 |
| [maths/PolygonFan](PolygonFan.md) | maths | 1 |
| [maths/PolygonMesh](PolygonMesh.md) | maths | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/Centroid.h
```
