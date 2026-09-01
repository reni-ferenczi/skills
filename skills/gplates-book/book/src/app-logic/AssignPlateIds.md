# AssignPlateIds

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 894 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/AssignPlateIds.h` | C++ | 388 |
| `src/app-logic/AssignPlateIds.cc` | C++ | 293 |

## Overview

[[[PROSE overview unit=app-logic/AssignPlateIds tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::AssignPlateIds`](#gplatesapplogicassignplateids) | class | `boost::noncopyable` | — | 0 | Assigns reconstruction plate ids to feature(s) using resolved topological boundaries (reconstructions of TopologicalClosedPlateBoundary features). |

## Members

### `GPlatesAppLogic::AssignPlateIds`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `boost::shared_ptr<AssignPlateIds>` | public | Typedef for shared pointer to AssignPlateIds. |
| `AssignPlateIdMethodType` | enum | `None` | public | How plate ids are assigned to features. |
| `FeaturePropertyType` | enum | `None` | public | The feature property types we can assign. |
| `feature_property_flags_type` | typedef | `std::bitset<NUM_FEATURE_PROPERTY_TYPES>` | public | A std::bitset for specifying which feature properties to assign. |
| `RECONSTRUCTION_PLATE_ID_PROPERTY_FLAG` | field | `feature_property_flags_type` | public | Specifies only the reconstruction plate id property is assigned. |
| `create( AssignPlateIdMethodType assign_plate_id_method, const std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref> &partitioning_feature_collections, const ReconstructionTreeCreator &default_reconstruction_tree_creator, const double &reconstruction_time, const feature_property_flags_type &feature_property_types ...` | method | `non_null_ptr_type` | public | Create an internal Reconstruction using partitioning\_feature\_collections, reconstruction\_feature\_collections, reconstruction\_time and anchor\_plate\_id to create a new set of partitioning polygons to be used for cookie-cutting. ... |
| `create( AssignPlateIdMethodType assign_plate_id_method, const std::vector<LayerProxy::non_null_ptr_type> &partitioning_layer_proxies, const ReconstructionTreeCreator &default_reconstruction_tree_creator, const double &reconstruction_time, const feature_property_flags_type &feature_property_types_to_assign = RECONSTRUCT ...` | method | `non_null_ptr_type` | public | The partitioning static or dynamic polygons come from a layer output. |
| `~AssignPlateIds()` | destructor | `None` | public | — |
| `has_partitioning_polygons()` | method | `bool` | public | Returns true if we have partitioning polygons. |
| `assign_reconstruction_plate_ids( const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection_ref, boost::optional<const ReconstructMethodInterface::Context &> reconstruct_method_context = boost::none)` | method | `void` | public | Assign reconstruction plate ids to all features in the feature collection. |
| `assign_reconstruction_plate_ids( const std::vector<GPlatesModel::FeatureHandle::weak_ref> &feature_refs, const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection_ref, boost::optional<const ReconstructMethodInterface::Context &> reconstruct_method_context = boost::none)` | method | `void` | public | Assign reconstruction plate ids to all features in a list of features. |
| `assign_reconstruction_plate_id( const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection_ref, boost::optional<const ReconstructMethodInterface::Context &> reconstruct_method_context = boost::none)` | method | `void` | public | Assign a reconstruction plate id to a feature. feature\_ref should be contained by feature\_collection\_ref. |
| `d_assign_plate_id_method` | field | `AssignPlateIdMethodType` | private | The method used to assign plate ids to features. |
| `d_feature_property_types_to_assign` | field | `feature_property_flags_type` | private | The types of feature properties to assign. |
| `d_geometry_cookie_cutter` | field | `boost::scoped_ptr<GeometryCookieCutter>` | private | Used to cookie cut geometries to find partitioning polygons. |
| `d_partition_feature_tasks` | field | `std::vector< boost::shared_ptr<PartitionFeatureTask> >` | private | Tasks that do the actual assigning of properties like plate id. |
| `d_default_reconstruct_method_context` | field | `ReconstructMethodInterface::Context` | private | Default reconstruction used to reverse reconstruct partitioned geometries. |
| `d_reconstruction_time` | field | `double` | private | The time that the partitioned geometries are at, and that the partitioning polygons are reconstructed/resolve to. |
| `d_respect_feature_time_period` | field | `bool` | private | Determines if features are only partitioned if the reconstruction time is within the time period over which the features are defined. |
| `AssignPlateIds( AssignPlateIdMethodType assign_plate_id_method, const std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref> &partitioning_feature_collections, const ReconstructionTreeCreator &default_reconstruction_tree_creator, const double &reconstruction_time, const feature_property_flags_type &feature_proper ...` | constructor | `None` | private | Create an internal Reconstruction using partitioning\_feature\_collections, reconstruction\_feature\_collections, reconstruction\_time and anchor\_plate\_id to create a new set of partitioning polygons to be used for cookie-cutting. |
| `AssignPlateIds( AssignPlateIdMethodType assign_plate_id_method, const std::vector<LayerProxy::non_null_ptr_type> &partitioning_layer_proxies, const ReconstructionTreeCreator &default_reconstruction_tree_creator, const double &reconstruction_time, const feature_property_flags_type &feature_property_types_to_assign, bool ...` | constructor | `None` | private | The partitioning static or dynamic polygons come from layer outputs. |
| `assign_reconstruction_plate_id_internal( const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection_ref, const ReconstructMethodInterface::Context &reconstruct_method_context)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `RECONSTRUCTION_PLATE_ID_PROPERTY_FLAG` | variable | `GPlatesAppLogic::AssignPlateIds::feature_property_flags_type` | — |
| `GPLATES_APP_LOGIC_ASSIGNPLATEIDS_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/AssignPlateIds tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/PartitionFeatureUtils](PartitionFeatureUtils.md) | app-logic | 40 |
| [qt-widgets/AssignReconstructionPlateIdsDialog](../qt-widgets/AssignReconstructionPlateIdsDialog.md) | qt-widgets | 39 |
| [cli/CliAssignPlateIdsCommand](../cli/CliAssignPlateIdsCommand.md) | cli | 37 |
| [app-logic/deprecated/PropertyValuePropogator](deprecated/PropertyValuePropogator.md) | app-logic | 34 |
| [app-logic/PartitionFeatureTask](PartitionFeatureTask.md) | app-logic | 13 |
| [app-logic/GenericPartitionFeatureTask](GenericPartitionFeatureTask.md) | app-logic | 12 |
| [app-logic/VgpPartitionFeatureTask](VgpPartitionFeatureTask.md) | app-logic | 5 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/AssignPlateIds.h
python scripts/gpq.py def GPlatesAppLogic::AssignPlateIds --body
python scripts/gpq.py uses AssignPlateIds --kind class
python scripts/gpq.py hier AssignPlateIds
```
