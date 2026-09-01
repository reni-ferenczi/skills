# PolygonPartitioner

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 159 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/PolygonPartitioner.h` | C++ | 239 |
| `src/maths/PolygonPartitioner.cc` | C++ | 898 |

## Overview

[[[PROSE overview unit=maths/PolygonPartitioner tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::GeometryPartitioner`](#anonymousgeometrypartitioner) | class | [`GPlatesMaths::ConstGeometryOnSphereVisitor`](ConstGeometryOnSphereVisitor.md) | — | 0 | — |
| [`(anonymous)::InsidePartitionedPolylineMerger`](#anonymousinsidepartitionedpolylinemerger) | class | — | — | 0 | Sequential partitioned polylines that are inside and/or overlapping with the partitioning polygon's boundary can really be merged into a single polygon since we are classifying them all as inside; this class keeps track of this. |
| [`GPlatesMaths::PolygonPartitioner`](#gplatesmathspolygonpartitioner) | class | — | — | 0 | Partitions GeometryOnSphere derived types using a PolygonOnSphere into geometries that are inside or outside or both (they are clipped if they cross the polygon boundary). |

## Members

### `(anonymous)::GeometryPartitioner`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GeometryPartitioner( const GPlatesMaths::PolygonPartitioner &polygon_partitioner, boost::optional<GPlatesMaths::PolygonPartitioner::partitioned_geometry_seq_type &> partitioned_geometries_inside, boost::optional<GPlatesMaths::PolygonPartitioner::partitioned_geometry_seq_type &> partitioned_geometries_outside)` | constructor | `None` | public | — |
| `partition_geometry( const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &geometry_to_be_partitioned)` | method | `GPlatesMaths::PolygonPartitioner::Result` | public | — |
| `visit_multi_point_on_sphere( GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere)` | method | `void` | protected | — |
| `visit_point_on_sphere( GPlatesMaths::PointGeometryOnSphere::non_null_ptr_to_const_type point_on_sphere)` | method | `void` | protected | — |
| `visit_polygon_on_sphere( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere)` | method | `void` | protected | — |
| `visit_polyline_on_sphere( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere)` | method | `void` | protected | — |
| `d_polygon_partitioner` | field | `GPlatesMaths::PolygonPartitioner` | private | — |
| `d_result` | field | `GPlatesMaths::PolygonPartitioner::Result` | private | — |
| `d_partitioned_geometries_inside` | field | `boost::optional<GPlatesMaths::PolygonPartitioner::partitioned_geometry_seq_type &>` | private | — |
| `d_partitioned_geometries_outside` | field | `boost::optional<GPlatesMaths::PolygonPartitioner::partitioned_geometry_seq_type &>` | private | — |

### `(anonymous)::InsidePartitionedPolylineMerger`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InsidePartitionedPolylineMerger( GPlatesMaths::PolygonPartitioner::partitioned_polyline_seq_type &inside_list)` | constructor | `None` | public | Construct with the list of polylines that are inside the partitioning polygon. |
| `add_inside_polyline( const GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type &inside_polyline)` | method | `void` | public | Add a polyline that's inside (or overlapping the boundary) of the partitioning polygon. |
| `merge_inside_polylines_and_output()` | method | `void` | public | We've come to the end of a contiguous sequence of polylines that are inside (or overlapping the boundary) the partitioning polygon. |
| `inside_polyline_seq_type` | typedef | `std::vector<GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type>` | private | — |
| `d_inside_polylines` | field | `inside_polyline_seq_type` | private | — |
| `d_inside_polyline_list` | field | `GPlatesMaths::PolygonPartitioner::partitioned_polyline_seq_type` | private | — |

### `GPlatesMaths::PolygonPartitioner`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `boost::shared_ptr<PolygonPartitioner>` | public | Typedef for a shared pointer to PolygonPartitioner. |
| `create( const PolygonOnSphere::non_null_ptr_to_const_type &partitioning_polygon, PolygonOnSphere::PointInPolygonSpeedAndMemory partition_point_speed_and_memory = PolygonOnSphere::ADAPTIVE)` | method | `non_null_ptr_type` | public | Create with the polygon that will do the partitioning. partition\_point\_speed\_and\_memory determines the speed versus memory trade-off of the point-in-polygon tests in partition\_point. |
| `Result` | enum | `None` | public | The result of partitioning a geometry against the partitioning polygon. |
| `partitioned_geometry_seq_type` | typedef | `std::list<GeometryOnSphere::non_null_ptr_to_const_type>` | public | Typedef for a sequence of partitioned geometries. |
| `partitioned_polyline_seq_type` | typedef | `std::list<PolylineOnSphere::non_null_ptr_to_const_type>` | public | Typedef for a sequence of partitioned polylines. |
| `partitioned_point_seq_type` | typedef | `std::vector<PointOnSphere>` | public | Typedef for a sequence of partitioned points. |
| `partition_geometry( const GeometryOnSphere::non_null_ptr_to_const_type &geometry_to_be_partitioned, boost::optional<partitioned_geometry_seq_type &> partitioned_geometries_inside = boost::none, boost::optional<partitioned_geometry_seq_type &> partitioned_geometries_outside = boost::none)` | method | `Result` | public | Partition geometry\_to\_be\_partitioned into geometries inside and outside the partitioning polygon. |
| `partition_polyline( const PolylineOnSphere::non_null_ptr_to_const_type &polyline_to_be_partitioned, boost::optional<partitioned_polyline_seq_type &> partitioned_polylines_inside = boost::none, boost::optional<partitioned_polyline_seq_type &> partitioned_polylines_outside = boost::none)` | method | `Result` | public | Partition polyline\_to\_be\_partitioned into polylines inside and outside the partitioning polygon. |
| `partition_polygon( const PolygonOnSphere::non_null_ptr_to_const_type &polygon_to_be_partitioned, boost::optional<partitioned_polyline_seq_type &> partitioned_polylines_inside = boost::none, boost::optional<partitioned_polyline_seq_type &> partitioned_polylines_outside = boost::none)` | method | `Result` | public | Partition polygon\_to\_be\_partitioned into either polylines inside and outside the partitioning polygon or neither if it was fully outside or inside. |
| `partition_point( const PointOnSphere &point_to_be_partitioned)` | method | `Result` | public | Returns whether point\_to\_be\_partitioned is inside, outside or on the boundary of the partitioning polygon. |
| `partition_multipoint( const MultiPointOnSphere::non_null_ptr_to_const_type &multipoint_to_be_partitioned, boost::optional<partitioned_point_seq_type &> partitioned_points_inside = boost::none, boost::optional<partitioned_point_seq_type &> partitioned_points_outside = boost::none)` | method | `Result` | public | Partition multipoint\_to\_be\_partitioned into an optional multipoint inside and an optional multipoint outside the partitioning polygon. |
| `d_partitioning_polygon` | field | `PolygonOnSphere::non_null_ptr_to_const_type` | private | — |
| `d_partitioning_polygon_orientation` | field | `PolygonOrientation::Orientation` | private | — |
| `d_partition_point_speed_and_memory` | field | `PolygonOnSphere::PointInPolygonSpeedAndMemory` | private | — |
| `PolygonPartitioner( const PolygonOnSphere::non_null_ptr_to_const_type &partitioning_polygon, PolygonOnSphere::PointInPolygonSpeedAndMemory partition_point_speed_and_memory)` | constructor | `None` | private | Construct with the polygon that will do the partitioning. |
| `is_non_intersecting_polyline_or_polygon_fully_inside_partitioning_polygon( const PointOnSphere &arbitrary_point_on_geometry)` | method | `bool` | private | — |
| `partition_intersecting_geometry( const PolylineIntersections::Graph &partitioned_polylines_graph, boost::optional<partitioned_polyline_seq_type &> partitioned_polylines_inside, boost::optional<partitioned_polyline_seq_type &> partitioned_polylines_outside)` | method | `void` | private | Determines which partitioned polylines are inside/outside the partitioning polygon and appends to the appropriate partition list. |
| `is_partitioned_polyline_inside_partitioning_polygon( const PolylineIntersections::Graph &partitioned_polylines_graph, const PolylineIntersections::PartitionedPolyline &partitioned_poly)` | method | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_first_or_last_non_zero_great_circle_arc( const GPlatesMaths::PolylineOnSphere &polyline, bool get_first)` | function | `boost::optional<const GPlatesMaths::GreatCircleArc &>` | Get first (or last) non-zero length GCA of polyline. |
| `do_adjacent_great_circle_arcs_bend_left( const GPlatesMaths::GreatCircleArc &prev_gca, const GPlatesMaths::GreatCircleArc &next_gca, const GPlatesMaths::PointOnSphere &intersection_point)` | function | `bool` | Precondition: the GCA's are not zero length. |
| `GPLATES_MATHS_POLYGONINTERSECTIONS_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=maths/PolygonPartitioner tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLReconstructedStaticPolygonMeshes](../opengl/GLReconstructedStaticPolygonMeshes.md) | opengl | 7 |
| [app-logic/GeometryCookieCutter](../app-logic/GeometryCookieCutter.md) | app-logic | 6 |
| [app-logic/TopologyUtils](../app-logic/TopologyUtils.md) | app-logic | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/PolygonPartitioner.h
python scripts/gpq.py def GPlatesMaths::PolygonPartitioner --body
python scripts/gpq.py uses PolygonPartitioner --kind class
python scripts/gpq.py hier PolygonPartitioner
```
