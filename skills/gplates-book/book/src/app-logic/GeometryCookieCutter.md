# GeometryCookieCutter

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 109 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/GeometryCookieCutter.h` | C++ | 402 |
| `src/app-logic/GeometryCookieCutter.cc` | C++ | 748 |

## Overview

`GeometryCookieCutter` answers "which plate does this point or line fall inside?" by turning a set of reconstructed polygon geometries into a `GPlatesMaths::PolygonPartitioner` per polygon and testing arbitrary geometry against them. It accepts static reconstructed polygons (`ReconstructedFeatureGeometry`), `ResolvedTopologicalBoundary` and `ResolvedTopologicalNetwork` geometries either pre-separated, combined in one `ReconstructionGeometry` list, or resolved on the fly from feature collections via a `ReconstructMethodRegistry` and `ReconstructionTreeCreator`.

Priority order matters because polygons can overlap: topological networks (and their interior static polygons) partition first, then topological boundaries, then plain static polygons, since the closed plate polygons currently leave holes where deforming networks exist. Within each group the polygons are optionally sorted by plate ID or by area (highest first) so that, when boundaries overlap, the more specific (further from the anchor, or smaller) plate wins the assignment. When grouping is turned off, the internal `FeatureOrderVisitor` instead walks the source feature collections to recover the original feature order and preserves it via a `std::multimap` keyed by that order, rather than by plate ID or area.

Callers such as `PartitionFeatureUtils` and `AssignPlateIds` use `partition_geometry`/`partition_geometries` to split arbitrary geometry into inside/outside pieces per polygon, or `partition_point` for a single point-in-polygon query.

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

- If overlapping partitioning polygons are passed in, results depend on the final ordering established by the constructor (grouping, then plate-ID/area sort, then feature order): a point inside two polygons is assigned to whichever comes first in that order, not to some notion of best fit.
- Ideally partitioning polygons should not overlap, but the class tolerates it rather than asserting; the sort options exist specifically to make the overlap behaviour predictable.
- The object is `boost::noncopyable` and immutable after construction — it captures a single reconstruction time and one fixed set of partitioning polygons, so a new instance is needed per reconstruction time.

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
