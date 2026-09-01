# GeometryCookieCutter

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 109 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/GeometryCookieCutter.h` | C++ | 402 |
| `src/app-logic/GeometryCookieCutter.cc` | C++ | 748 |

## Overview

[[[PROSE overview unit=app-logic/GeometryCookieCutter tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::(anonymous)::FeatureOrderVisitor`](#gplatesapplogicanonymousfeatureordervisitor) | class | [`GPlatesModel::FeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | — |
| [`GPlatesAppLogic::GeometryCookieCutter`](#gplatesapplogicgeometrycookiecutter) | class | `boost::noncopyable` | — | 0 | Partitions geometry using dynamic resolved topological boundaries and/or static reconstructed feature polygons. |

## Members

### `GPlatesAppLogic::(anonymous)::FeatureOrderVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `feature_order_map_type` | typedef | `std::map<GPlatesModel::FeatureHandle::weak_ref, unsigned int>` | public | — |
| `FeatureOrderVisitor( feature_order_map_type &feature_order_map)` | constructor | `None` | public | — |
| `initialise_pre_feature_properties( GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | protected | — |
| `d_feature_order_map` | field | `feature_order_map_type` | private | — |
| `d_feature_count` | field | `unsigned int` | private | — |

### `GPlatesAppLogic::GeometryCookieCutter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `partitioned_geometry_seq_type` | typedef | `GPlatesMaths::PolygonPartitioner::partitioned_geometry_seq_type` | public | Typedef for a sequence of geometries resulting from partitioning a single geometry. |
| `Partition` | class | `None` | public | Typedef for a partitioning polygon and the geometries partitioned inside it. |
| `partition_seq_type` | typedef | `std::list<Partition>` | public | Typedef for a sequence of inside partitions. |
| `SortPlates` | enum | `None` | public | Enumerated ways to sort plates. |
| `GeometryCookieCutter( const double &reconstruction_time, boost::optional<const std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &> reconstructed_static_polygons, boost::optional<const std::vector<ResolvedTopologicalBoundary::non_null_ptr_type> &> resolved_topological_boundaries, boost::optional<const std::v ...` | constructor | `None` | public | Finds reconstructed polygon geometries to partition other geometry with. |
| `GeometryCookieCutter( const double &reconstruction_time, const std::vector<ReconstructionGeometry::non_null_ptr_type> &reconstruction_geometries, bool group_networks_then_boundaries_then_static_polygons = true, boost::optional<SortPlates> sort_plates = SORT_BY_PLATE_ID, GPlatesMaths::PolygonOnSphere::PointInPolygonSpee ...` | constructor | `None` | public | Finds reconstructed polygon geometries to partition other geometry with. |
| `GeometryCookieCutter( const double &reconstruction_time, const ReconstructMethodRegistry &reconstruct_method_registry, const std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref> &feature_collections, const ReconstructionTreeCreator &reconstruction_tree_creator, bool group_networks_then_boundaries_then_static_po ...` | constructor | `None` | public | Finds reconstructed polygon geometries to partition other geometry with. |
| `has_partitioning_polygons()` | method | `bool` | public | Returns true if we have partitioning polygons. |
| `partition_geometry( const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &geometry, boost::optional<partition_seq_type &> partitioned_inside_geometries = boost::none, boost::optional<partitioned_geometry_seq_type &> partitioned_outside_geometries = boost::none)` | method | `bool` | public | Partition geometry using the partitioning polygons found in the constructor. |
| `partition_geometries( const std::vector<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type> &geometries, boost::optional<partition_seq_type &> partitioned_inside_geometries = boost::none, boost::optional<partitioned_geometry_seq_type &> partitioned_outside_geometries = boost::none)` | method | `bool` | public | Same as partition\_geometry except partitions multiple input geometries (instead of one). |
| `partition_point( const GPlatesMaths::PointOnSphere &point)` | method | `boost::optional<const ReconstructionGeometry *>` | public | Finds which partitioning polygon boundary contains point. |
| `get_reconstruction_time()` | method | `double` | public | Returns the reconstruction time of the reconstructed partitioning polygons used to partition geometry with. |
| `PartitioningGeometry` | class | `None` | private | Associates a ReconstructionGeometry with its polygon structure for geometry partitioning. |
| `partitioning_geometry_seq_type` | typedef | `std::vector<PartitioningGeometry>` | private | Typedef for a sequence of partitioning geometries. |
| `AddPartitioningReconstructionGeometry` | class | `None` | private | Visits reconstruction geometries to add as partitioning geometries. |
| `d_partitioning_geometries` | field | `partitioning_geometry_seq_type` | private | The partitioning geometries. |
| `d_reconstruction_time` | field | `double` | private | — |
| `d_partition_point_speed_and_memory` | field | `GPlatesMaths::PolygonOnSphere::PointInPolygonSpeedAndMemory` | private | — |
| `add_partitioning_reconstruction_geometries( const std::vector<ReconstructionGeometry::non_null_ptr_type> &reconstruction_geometries, boost::optional<SortPlates> sort_plates)` | method | `void` | private | Adds ReconstructionGeometry objects, unsorted by type, as partitioning geometries. |
| `add_partitioning_resolved_topological_networks( const std::vector<ResolvedTopologicalNetwork::non_null_ptr_type> &resolved_topological_networks, boost::optional<SortPlates> sort_plates)` | method | `void` | private | Adds ResolvedTopologicalNetwork objects as partitioning geometries. |
| `add_partitioning_resolved_topological_network( const ResolvedTopologicalNetwork::non_null_ptr_type &resolved_topological_network)` | method | `void` | private | Add a ResolvedTopologicalNetwork as a partitioning geometry. |
| `add_partitioning_resolved_topological_boundaries( const std::vector<ResolvedTopologicalBoundary::non_null_ptr_type> &resolved_topological_boundaries, boost::optional<SortPlates> sort_plates)` | method | `void` | private | Adds ResolvedTopologicalBoundary objects as partitioning geometries. |
| `add_partitioning_resolved_topological_boundary( const ResolvedTopologicalBoundary::non_null_ptr_type &resolved_topological_boundary)` | method | `void` | private | Add a ResolvedTopologicalBoundary as a partitioning geometry. |
| `add_partitioning_reconstructed_feature_polygons( const std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &reconstructed_feature_geometries, boost::optional<SortPlates> sort_plates)` | method | `void` | private | Adds ReconstructedFeatureGeometry objects as partitioning geometries. |
| `add_partitioning_reconstructed_feature_polygon( const ReconstructedFeatureGeometry::non_null_ptr_type &reconstructed_feature_geometry)` | method | `void` | private | Add a ReconstructedFeatureGeometry as a partitioning geometry, if it has a \*polygon\* geometry. |
| `sort_plates_in_partitioning_group( const partitioning_geometry_seq_type::iterator &partitioning_group_begin, const partitioning_geometry_seq_type::iterator &partitioning_group_end, SortPlates sort_plates)` | method | `void` | private | Sort plates within a partitioning group. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `operator()( const PartitioningGeometry &lhs, const PartitioningGeometry &rhs)` | operator | `bool` | — |
| `operator()( const PartitioningGeometry &lhs, const PartitioningGeometry &rhs)` | operator | `bool` | — |
| `GPLATES_APP_LOGIC_GEOMETRYCOOKIECUTTER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/GeometryCookieCutter tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/PartitionFeatureUtils](PartitionFeatureUtils.md) | app-logic | 48 |
| [app-logic/AssignPlateIds](AssignPlateIds.md) | app-logic | 15 |
| [app-logic/PlateVelocityUtils](PlateVelocityUtils.md) | app-logic | 15 |
| [app-logic/VgpPartitionFeatureTask](VgpPartitionFeatureTask.md) | app-logic | 4 |
| [app-logic/GenericPartitionFeatureTask](GenericPartitionFeatureTask.md) | app-logic | 3 |
| [app-logic/deprecated/PropertyValuePropogator](deprecated/PropertyValuePropogator.md) | app-logic | 2 |
| [cli/CliAssignPlateIdsCommand](../cli/CliAssignPlateIdsCommand.md) | cli | 1 |
| [qt-widgets/AssignReconstructionPlateIdsDialog](../qt-widgets/AssignReconstructionPlateIdsDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/GeometryCookieCutter.h
python scripts/gpq.py def GPlatesAppLogic::GeometryCookieCutter --body
python scripts/gpq.py uses GeometryCookieCutter --kind class
python scripts/gpq.py hier GeometryCookieCutter
```
