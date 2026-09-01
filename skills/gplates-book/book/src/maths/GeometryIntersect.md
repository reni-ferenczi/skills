# GeometryIntersect

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 414 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/GeometryIntersect.h` | C++ | 410 |
| `src/maths/GeometryIntersect.cc` | C++ | 1438 |

## Overview

[[[PROSE overview unit=maths/GeometryIntersect tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::GeometryIntersect::SortGeometryIntersection`](#gplatesmathsgeometryintersectsortgeometryintersection) | class | — | — | 0 | Predicate to sort intersections from beginning of the geometry to end. |
| [`GPlatesMaths::GeometryIntersect::Intersection`](#gplatesmathsgeometryintersectintersection) | class | — | — | 0 | Location of an intersection between two geometries. |
| [`GPlatesMaths::GeometryIntersect::intersection_seq_type`](#gplatesmathsgeometryintersectintersection_seq_type) | typedef | — | — | 0 | Typedef for a sequence of Intersection. |
| [`GPlatesMaths::GeometryIntersect::Graph`](#gplatesmathsgeometryintersectgraph) | class | — | — | 0 | Contains the results of intersecting two geometries. |

## Members

### `GPlatesMaths::GeometryIntersect::SortGeometryIntersection`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SortGeometryIntersection( const intersection_seq_type &intersections, const unsigned int Intersection::*segment_index_ptr, const AngularDistance Intersection::*angle_in_segment_ptr)` | constructor | `None` | public | — |
| `operator()( unsigned int lhs, unsigned int rhs)` | operator | `bool` | public | — |
| `d_intersections` | field | `intersection_seq_type` | private | — |
| `Intersection` | field | `unsigned int` | private | — |

### `GPlatesMaths::GeometryIntersect::Intersection`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Type` | enum | `None` | public | Type of intersection, whether two great circle arc segments cross or touch. |
| `get_on_segment_start_threshold_cosine()` | method | `double` | public | Return the cosine (dot product of two points) of maximum angular distance used for "on segment start". |
| `get_on_segment_start_threshold_sine()` | method | `double` | public | Return the sine (dot product of point and GCA plane) of maximum angular distance used for "on segment start". |
| `Intersection( Type type_, const PointOnSphere &position_, unsigned int segment_index1_, unsigned int segment_index2_, const AngularDistance &angle_in_segment1_ = AngularDistance::ZERO, const AngularDistance &angle_in_segment2_ = AngularDistance::ZERO)` | constructor | `None` | public | — |
| `is_on_segment1_start()` | method | `bool` | public | Is this intersection \*on\* the start point of segment1 ? |
| `is_on_segment2_start()` | method | `bool` | public | Is this intersection \*on\* the start point of segment2 ? |
| `type` | field | `Type` | public | — |
| `position` | field | `PointOnSphere` | public | — |
| `segment_index1` | field | `unsigned int` | public | Segment index within the first geometry. |
| `segment_index2` | field | `unsigned int` | public | Segment index within the second geometry. |
| `angle_in_segment1` | field | `AngularDistance` | public | Angle (radians) from segment start point to intersection along segment in first geometry. |
| `angle_in_segment2` | field | `AngularDistance` | public | Angle (radians) from segment start point to intersection along segment in second geometry. |

### `GPlatesMaths::GeometryIntersect::intersection_seq_type`

*None.*

### `GPlatesMaths::GeometryIntersect::Graph`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `empty()` | method | `bool` | public | Returns true if graph is empty. |
| `clear()` | method | `void` | public | Empties the graph. |
| `unordered_intersections` | field | `intersection_seq_type` | public | The \*unordered\* intersections. |
| `geometry1_ordered_intersections` | field | `std::vector<unsigned int>` | public | The intersections \*ordered\* along each original geometry. |
| `geometry2_ordered_intersections` | field | `std::vector<unsigned int>` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `THICKNESS_THRESHOLD_COSINE` | variable | `double` | Thickness threshold used for a dot product between two points. |
| `THICKNESS_THRESHOLD_SINE` | variable | `double` | Thickness threshold used for a dot product between a point and a plane (GCA normal vector). |
| `POLYGON_NEEDS_NO_LAST_SEGMENT_INDEX` | variable | `unsigned int` | We don't need any special handling of the last segment in a polygon ring, so for polygons we just specify the maximum unsigned integer (so that no segment indices will compare equal with it and activate the special handling). |
| `sort_geometry_intersections( Graph &graph)` | function | `void` | For each of the two geometries, sort its intersection list such that intersections are ordered from the geometries start to end. |
| `add_intersection( Graph &graph, Intersection::Type intersection_type, const UnitVector3D &intersection_position, const UnitVector3D &segment1_start_point, const UnitVector3D &segment2_start_point, unsigned int segment1_index, unsigned int segment2_index)` | function | `void` | Add an Intersection to the graph. |
| `add_segments_crossing_intersection( Graph &graph, const UnitVector3D &segment1_start_point, const UnitVector3D &segment1_end_point, const UnitVector3D &segment1_plane, const UnitVector3D &segment2_start_point, const UnitVector3D &segment2_end_point, const UnitVector3D &segment2_plane, bool segment1_start_point_on_posit ...` | function | `void` | Two non-zero-length segments cross each other's \*thick\* plane - find and add the intersection. |
| `point_is_in_segment_lune( const UnitVector3D &point, const UnitVector3D &segment_plane, const UnitVector3D &segment_start_point, const UnitVector3D &segment_end_point)` | function | `bool` | Returns true if the specified point lies within the lune of the specified segment. |
| `intersect_segments( Graph &graph, const GreatCircleArc &segment1, const GreatCircleArc &segment2, unsigned int segment1_index, unsigned int segment2_index, unsigned int last_segment1_index, unsigned int last_segment2_index)` | function | `void` | See if two segments cross or touch each other's \*thick\* plane - if so, find and add the intersection(s). |
| `intersect_bounding_tree_nodes( Graph &graph, const PolyGreatCircleArcBoundingTree<GreatCircleArcConstIterator1Type> &geometry1_bounding_tree, const typename PolyGreatCircleArcBoundingTree<GreatCircleArcConstIterator1Type>::node_type &geometry1_sub_tree_node, const unsigned int last_segment1_index, const PolyGreatCircle ...` | function | `void` | Find any intersections between a bounding tree node (of segments) of one polyline or polygon, and the bounding tree node (of segments) of another polyline or polygon. |
| `intersect_geometries( Graph &graph, const PolyGeometryBoundingTree1Type &poly_geometry1_bounding_tree, const unsigned int last_segment1_index, const PolyGeometryBoundingTree2Type &poly_geometry2_bounding_tree, const unsigned int last_segment2_index)` | function | `bool` | Find any intersections between two polyline/polygon geometries. |
| `GPLATES_MATHS_GEOMETRYINTERSECT_H` | macro | `None` | — |
| `intersect( Graph &intersection_graph, const PolylineOnSphere &polyline1, const PolylineOnSphere &polyline2)` | function | `bool` | Find all points of intersection of polyline1 and polyline2, and store them in the returned Graph object. |
| `intersect( Graph &intersection_graph, const PolygonOnSphere &polygon1, const PolygonOnSphere &polygon2, bool include_polygon1_interior_rings = true, bool include_polygon2_interior_rings = true)` | function | `bool` | Find all points of intersection of polygon1 and polygon2, and store them in the returned Graph object. |
| `intersect( Graph &intersection_graph, const PolylineOnSphere &polyline, const PolygonOnSphere &polygon, bool include_polygon_interior_rings = true)` | function | `bool` | Find all points of intersection of polyline and polygon, and store them in the returned Graph object. |
| `intersect( Graph &intersection_graph, const PolygonOnSphere &polygon, const PolylineOnSphere &polyline, bool include_polygon_interior_rings = true)` | function | `bool` | Find all points of intersection of polygon and polyline, and store them in the returned Graph object. |

## Notes

[[[PROSE notes unit=maths/GeometryIntersect tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/PolylineIntersections](PolylineIntersections.md) | maths | 144 |
| [maths/GeometryCrossing](GeometryCrossing.md) | maths | 49 |
| [app-logic/TopologyIntersections](../app-logic/TopologyIntersections.md) | app-logic | 43 |
| [app-logic/ResolvedSubSegmentRangeInSection](../app-logic/ResolvedSubSegmentRangeInSection.md) | app-logic | 13 |
| [app-logic/TopologyGeometryResolverLayerProxy](../app-logic/TopologyGeometryResolverLayerProxy.md) | app-logic | 6 |
| [maths/SmallCircleBounds](SmallCircleBounds.md) | maths | 4 |
| [app-logic/TopologyNetworkResolver](../app-logic/TopologyNetworkResolver.md) | app-logic | 3 |
| [app-logic/TopologyNetworkResolverLayerProxy](../app-logic/TopologyNetworkResolverLayerProxy.md) | app-logic | 3 |
| [app-logic/TopologyReconstruct](../app-logic/TopologyReconstruct.md) | app-logic | 3 |
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 2 |
| [app-logic/TopologyGeometryResolver](../app-logic/TopologyGeometryResolver.md) | app-logic | 1 |
| [app-logic/TopologyUtils](../app-logic/TopologyUtils.md) | app-logic | 1 |
| [app-logic/VelocityFieldCalculatorLayerProxy](../app-logic/VelocityFieldCalculatorLayerProxy.md) | app-logic | 1 |
| [file-io/CitcomsResolvedTopologicalBoundaryExport](../file-io/CitcomsResolvedTopologicalBoundaryExport.md) | file-io | 1 |
| [file-io/GMTFormatResolvedTopologicalGeometryExport](../file-io/GMTFormatResolvedTopologicalGeometryExport.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/GeometryIntersect.h
python scripts/gpq.py def GPlatesMaths::GeometryIntersect::Intersection --body
python scripts/gpq.py uses Intersection --kind class
python scripts/gpq.py hier Intersection
```
