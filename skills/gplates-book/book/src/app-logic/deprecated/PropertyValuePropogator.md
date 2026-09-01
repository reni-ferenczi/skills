# PropertyValuePropogator

[Book TOC](../../../TOC.md) · [app-logic](../../../components/app-logic.md) · cluster Community 892 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/deprecated/PropertyValuePropogator.h` | C++ | 355 |
| `src/app-logic/deprecated/PropertyValuePropogator.cc` | C++ | 156 |

## Overview

[[[PROSE overview unit=app-logic/deprecated/PropertyValuePropogator tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::PropertyValuePropogator`](#gplatesapplogicpropertyvaluepropogator) | class | — | — | 0 | Assigns reconstruction plate ids to feature(s) using resolved topological boundaries (reconstructions of TopologicalClosedPlateBoundary features). |

## Members

### `GPlatesAppLogic::PropertyValuePropogator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `boost::shared_ptr<PropertyValuePropogator>` | public | Typedef for shared pointer to AssignPlateIds. |
| `FeaturePropertyType` | enum | `None` | public | The feature property types we can assign. |
| `feature_property_flags_type` | typedef | `std::bitset<NUM_FEATURE_PROPERTY_TYPES>` | public | A std::bitset for specifying which feature properties to assign. |
| `RECONSTRUCTION_PLATE_ID_PROPERTY_FLAG` | field | `feature_property_flags_type` | public | Specifies only the reconstruction plate id property is assigned. |
| `create( GPlatesAppLogic::AssignPlateIds::AssignPlateIdMethodType assign_plate_id_method, const std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref> & partitioning_feature_collections, const std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref> & reconstruction_feature_collections, const double &reconstru ...` | method | `non_null_ptr_type` | public | Create an internal Reconstruction using partitioning\_feature\_collections, reconstruction\_feature\_collections, reconstruction\_time and anchor\_plate\_id to create a new set of partitioning polygons to be used for cookie-cutting. ... |
| `has_partitioning_polygons()` | method | `bool` | public | Returns true if we have partitioning polygons. |
| `assign_reconstruction_plate_ids( const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection_ref)` | method | `void` | public | Assign reconstruction plate ids to all features in the feature collection. |
| `assign_reconstruction_plate_ids( const std::vector<GPlatesModel::FeatureHandle::weak_ref> &feature_refs, const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection_ref)` | method | `void` | public | Assign reconstruction plate ids to all features in a list of features. |
| `assign_reconstruction_plate_id( const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection_ref)` | method | `void` | public | Assign a reconstruction plate id to a feature. feature\_ref should be contained by feature\_collection\_ref. |
| `propogate_property_value( const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection_ref, PartitionFeatureUtils::SimplePropertyValueAssigner::PropertyNameFeatureCollectionMap& property_feature_collection_map)` | method | `void` | public | — |
| `d_assign_plate_id_method` | field | `GPlatesAppLogic::AssignPlateIds::AssignPlateIdMethodType` | private | The method used to assign plate ids to features. |
| `d_feature_property_types_to_assign` | field | `feature_property_flags_type` | private | The types of feature properties to assign. |
| `d_reconstruction` | field | `GPlatesAppLogic::Reconstruction::non_null_ptr_type` | private | Contains the reconstructed polygons used for cookie-cutting. |
| `d_geometry_cookie_cutter` | field | `GeometryCookieCutter` | private | Used to cookie cut geometries to find partitioning polygons. |
| `d_partition_feature_tasks` | field | `std::vector< boost::shared_ptr<PartitionFeatureTask> >` | private | Tasks that do the actual assigning of properties like plate id. |
| `PropertyValuePropogator( GPlatesAppLogic::AssignPlateIds::AssignPlateIdMethodType assign_plate_id_method, const std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref> & partitioning_feature_collections, const std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref> & reconstruction_feature_collections, const ...` | constructor | `None` | private | Create an internal Reconstruction using partitioning\_feature\_collections, reconstruction\_feature\_collections, reconstruction\_time and anchor\_plate\_id to create a new set of partitioning polygons to be used for cookie-cutting. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `RECONSTRUCTION_PLATE_ID_PROPERTY_FLAG` | variable | `GPlatesAppLogic::PropertyValuePropogator::feature_property_flags_type` | — |
| `GPLATES_APP_LOGIC_PROPERTYVALUEPROPOGATOR_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/deprecated/PropertyValuePropogator tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/deprecated/PropertyValuePropogator.h
python scripts/gpq.py def GPlatesAppLogic::PropertyValuePropogator --body
python scripts/gpq.py uses PropertyValuePropogator --kind class
python scripts/gpq.py hier PropertyValuePropogator
```
