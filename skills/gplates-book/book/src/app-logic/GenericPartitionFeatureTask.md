# GenericPartitionFeatureTask

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 930 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/GenericPartitionFeatureTask.h` | C++ | 113 |
| `src/app-logic/GenericPartitionFeatureTask.cc` | C++ | 235 |

## Overview

[[[PROSE overview unit=app-logic/GenericPartitionFeatureTask tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::GenericPartitionFeatureTask`](#gplatesapplogicgenericpartitionfeaturetask) | class | [`PartitionFeatureTask`](PartitionFeatureTask.md) | — | 0 | Generic task for assigning properties to a feature. |

## Members

### `GPlatesAppLogic::GenericPartitionFeatureTask`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GenericPartitionFeatureTask( GPlatesAppLogic::AssignPlateIds::AssignPlateIdMethodType assign_plate_id_method, const GPlatesAppLogic::AssignPlateIds::feature_property_flags_type &feature_property_types_to_assign, bool verify_information_model)` | constructor | `None` | public | If 'verify\_information\_model' is true then feature property types are only added if they don't not violate the GPGIM. |
| `can_partition_feature( const GPlatesModel::FeatureHandle::const_weak_ref &feature_ref)` | method | `bool` | public | — |
| `partition_feature( const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection_ref, const GeometryCookieCutter &geometry_cookie_cutter, const ReconstructMethodInterface::Context &reconstruct_method_context, const double &reconstruction_time, bool r ...` | method | `void` | public | — |
| `d_verify_information_model` | field | `bool` | private | — |
| `d_assign_plate_id_method` | field | `GPlatesAppLogic::AssignPlateIds::AssignPlateIdMethodType` | private | — |
| `d_feature_property_types_to_assign` | field | `GPlatesAppLogic::AssignPlateIds::feature_property_flags_type` | private | — |
| `partition_feature( const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const boost::shared_ptr<const PartitionFeatureUtils::PartitionedFeature> &partitioned_feature, PartitionFeatureUtils::PartitionedFeatureManager &partitioned_feature_manager, const ReconstructMethodInterface::Context &reconstruct_method_context ...` | method | `void` | private | — |
| `assign_feature_to_plate_it_overlaps_the_most( const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const boost::shared_ptr<const PartitionFeatureUtils::PartitionedFeature> &partitioned_feature, PartitionFeatureUtils::PartitionedFeatureManager &partitioned_feature_manager, const ReconstructMethodInterface::Context ...` | method | `void` | private | — |
| `partition_feature_into_plates( const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const boost::shared_ptr<const PartitionFeatureUtils::PartitionedFeature> &partitioned_feature, PartitionFeatureUtils::PartitionedFeatureManager &partitioned_feature_manager, const ReconstructMethodInterface::Context &reconstruct_me ...` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_GENERICPARTITIONFEATURETASK_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/GenericPartitionFeatureTask tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/PartitionFeatureTask](PartitionFeatureTask.md) | app-logic | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/GenericPartitionFeatureTask.h
python scripts/gpq.py def GPlatesAppLogic::GenericPartitionFeatureTask --body
python scripts/gpq.py uses GenericPartitionFeatureTask --kind class
python scripts/gpq.py hier GenericPartitionFeatureTask
```
