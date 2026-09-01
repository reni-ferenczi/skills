# PolylineIntersections

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 418 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/PolylineIntersections.h` | C++ | 326 |
| `src/maths/PolylineIntersections.cc` | C++ | 607 |

## Overview

[[[PROSE overview unit=maths/PolylineIntersections tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::PolylineIntersections::PartitionedPolyline`](#gplatesmathspolylineintersectionspartitionedpolyline) | class | [`GPlatesUtils::ReferenceCount<PartitionedPolyline>`](../utils/ReferenceCount.md) | — | 0 | A section of one of the two original intersected geometries. |
| [`GPlatesMaths::PolylineIntersections::partitioned_polyline_ptr_to_const_seq_type`](#gplatesmathspolylineintersectionspartitioned_polyline_ptr_to_const_seq_type) | typedef | — | — | 0 | Typedef for sequence of pointers to const PartitionedPolyline. |
| [`GPlatesMaths::PolylineIntersections::Intersection`](#gplatesmathspolylineintersectionsintersection) | class | [`GPlatesUtils::ReferenceCount<Intersection>`](../utils/ReferenceCount.md) | — | 0 | A point of intersection of the two original intersected geometries; |
| [`GPlatesMaths::PolylineIntersections::intersection_ptr_to_const_seq_type`](#gplatesmathspolylineintersectionsintersection_ptr_to_const_seq_type) | typedef | — | — | 0 | Typedef for sequence of pointers to const Intersection. |
| [`GPlatesMaths::PolylineIntersections::Graph`](#gplatesmathspolylineintersectionsgraph) | class | — | — | 0 | Contains the results of intersecting two geometries in a form where the resulting partitioned polylines from each geometry can be traversed and queried. |

## Members

### `GPlatesMaths::PolylineIntersections::PartitionedPolyline`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<PartitionedPolyline>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const PartitionedPolyline>` | public | — |
| `create( PolylineOnSphere::non_null_ptr_to_const_type polyline_)` | method | `non_null_ptr_type` | public | — |
| `polyline` | field | `PolylineOnSphere::non_null_ptr_to_const_type` | public | The actual partitioned polyline geometry. |
| `prev_intersection` | field | `Intersection` | public | The previous intersection if there is one. |
| `next_intersection` | field | `Intersection` | public | The next intersection if there is one. |
| `PartitionedPolyline( PolylineOnSphere::non_null_ptr_to_const_type polyline_)` | constructor | `None` | private | — |

### `GPlatesMaths::PolylineIntersections::partitioned_polyline_ptr_to_const_seq_type`

*None.*

### `GPlatesMaths::PolylineIntersections::Intersection`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<Intersection>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const Intersection>` | public | — |
| `create( const PointOnSphere &intersection_point_)` | method | `non_null_ptr_type` | public | — |
| `intersection_point` | field | `PointOnSphere` | public | The point of intersection. |
| `prev_partitioned_polyline1` | field | `PartitionedPolyline` | public | The previous partitioned polyline from the first original geometry. |
| `next_partitioned_polyline1` | field | `PartitionedPolyline` | public | The next partitioned polyline from the first original geometry. |
| `prev_partitioned_polyline2` | field | `PartitionedPolyline` | public | The previous partitioned polyline from the second original geometry. |
| `next_partitioned_polyline2` | field | `PartitionedPolyline` | public | The next partitioned polyline from the second original geometry. |
| `Intersection( const PointOnSphere &intersection_point_)` | constructor | `None` | private | — |

### `GPlatesMaths::PolylineIntersections::intersection_ptr_to_const_seq_type`

*None.*

### `GPlatesMaths::PolylineIntersections::Graph`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `unordered_intersections` | field | `intersection_ptr_to_const_seq_type` | public | The \*unordered\* intersection points. |
| `geometry1_ordered_intersections` | field | `intersection_ptr_to_const_seq_type` | public | The intersections \*ordered\* along the first original geometry (from its start to end). |
| `geometry2_ordered_intersections` | field | `intersection_ptr_to_const_seq_type` | public | The intersections \*ordered\* along the second original geometry (from its start to end). |
| `partitioned_polylines1` | field | `partitioned_polyline_ptr_to_const_seq_type` | public | The partitioned polylines belonging to the first original geometry. |
| `partitioned_polylines2` | field | `partitioned_polyline_ptr_to_const_seq_type` | public | The partitioned polylines belonging to the second original geometry. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `clear( Graph &graph)` | function | `void` | Clear the graph. |
| `add_intersections( Graph &graph, const GeometryIntersect::Graph &intersection_graph)` | function | `void` | Create and add intersections using the intersection graph. |
| `create_partitioned_polyline( const VertexIteratorType vertices_begin, const VertexIteratorType vertices_end, const unsigned int num_segments, const unsigned int GeometryIntersect::Intersection::*segment_index_ptr, const AngularDistance GeometryIntersect::Intersection::*angle_in_segment_ptr, // This is either SEGMENT1_S ...` | function | `PolylineOnSphere::non_null_ptr_to_const_type` | Create a polyline partitioned between two intersections, or between start of geometry and the end intersection (if no start intersection), or between the start intersection and end of geometry (if no end intersection). |
| `add_partitioned_polylines( const VertexIteratorType vertices_begin, const VertexIteratorType vertices_end, const unsigned int num_segments, Graph &graph, partitioned_polyline_ptr_to_const_seq_type Graph::*partitioned_polylines_ptr, const PartitionedPolyline * Intersection::*prev_partitioned_polyline_ptr, const Partitio ...` | function | `void` | Create and add partitioned polylines, for one of the two geometries, using the intersection graph. |
| `partition_geometries( Graph &graph, const GeometryIntersect::Graph &intersection_graph, const VertexIterator1Type vertices1_begin, const VertexIterator1Type vertices1_end, const unsigned int num_segments1, const VertexIterator2Type vertices2_begin, const VertexIterator2Type vertices2_end, const unsigned int num_segment ...` | function | `void` | Partition two polyline/polygon geometries. |
| `GPLATES_MATHS_POLYLINEINTERSECTIONS_H` | macro | `None` | — |
| `partition( Graph &partition_graph, const PolylineOnSphere &polyline1, const PolylineOnSphere &polyline2)` | function | `bool` | Find all points of intersection of polyline1 and polyline2, and store them in the returned Graph object; partition polyline1 and polyline2 at these points of intersection, and store these new, polylines in 'partitioned\_polylines1' and ... |
| `partition( Graph &partition_graph, const PolygonOnSphere &polygon1, const PolygonOnSphere &polygon2)` | function | `bool` | Another overload of partition; intersects two polygons. |
| `partition( Graph &partition_graph, const PolylineOnSphere &polyline, const PolygonOnSphere &polygon)` | function | `bool` | Another overload of partition; intersects a polyline and a polygon. |
| `partition( Graph &partition_graph, const PolygonOnSphere &polygon, const PolylineOnSphere &polyline)` | function | `bool` | Another overload of partition; intersects a polygon and a polyline. |

## Notes

[[[PROSE notes unit=maths/PolylineIntersections tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/PolygonPartitioner](PolygonPartitioner.md) | maths | 30 |
| [app-logic/GenerateVelocityDomainCitcoms](../app-logic/GenerateVelocityDomainCitcoms.md) | app-logic | 7 |
| [maths/deprecated/PolylineIntersections_test](deprecated/PolylineIntersections_test.md) | maths | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/PolylineIntersections.h
python scripts/gpq.py def GPlatesMaths::PolylineIntersections::Intersection --body
python scripts/gpq.py uses Intersection --kind class
python scripts/gpq.py hier Intersection
```
