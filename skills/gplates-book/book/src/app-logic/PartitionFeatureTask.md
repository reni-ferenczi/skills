# PartitionFeatureTask

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 1820 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/PartitionFeatureTask.h` | C++ | 112 |
| `src/app-logic/PartitionFeatureTask.cc` | C++ | 58 |

## Overview

[[[PROSE overview unit=app-logic/PartitionFeatureTask tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::partition_feature_task_ptr_type`](#gplatesapplogicpartition_feature_task_ptr_type) | typedef | — | — | 0 | Typedef for a shared pointer to a task. |
| [`GPlatesAppLogic::partition_feature_task_ptr_seq_type`](#gplatesapplogicpartition_feature_task_ptr_seq_type) | typedef | — | — | 0 | Typedef for a sequence of shared pointers to tasks. |
| [`GPlatesAppLogic::PartitionFeatureTask`](#gplatesapplogicpartitionfeaturetask) | class | — | — | 2 | Interface for a task that can be queried to see if it can assign a plate id to a specific feature and asked to assign the plate id. |

## Members

### `GPlatesAppLogic::partition_feature_task_ptr_type`

*None.*

### `GPlatesAppLogic::partition_feature_task_ptr_seq_type`

*None.*

### `GPlatesAppLogic::PartitionFeatureTask`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~PartitionFeatureTask()` | destructor | `None` | public | — |
| `can_partition_feature( const GPlatesModel::FeatureHandle::const_weak_ref &feature_ref)` | method | `bool` | public | Return true if can partition feature\_ref. |
| `partition_feature( const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection_ref, const GeometryCookieCutter &geometry_cookie_cutter, const ReconstructMethodInterface::Context &reconstruct_method_context, const double &reconstruction_time, bool r ...` | method | `void` | public | Assigns properties of the partitioning polygons to feature\_ref and any clones of it that hold partitioned geometry. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_PARTITIONFEATURETASK_H` | macro | `None` | — |
| `get_partition_feature_tasks( GPlatesAppLogic::AssignPlateIds::AssignPlateIdMethodType assign_plate_id_method, const GPlatesAppLogic::AssignPlateIds::feature_property_flags_type &feature_property_types_to_assign, bool verify_information_model)` | function | `partition_feature_task_ptr_seq_type` | Creates and returns all PartitionFeatureTask tasks in the order in which they should be processed. |

## Notes

[[[PROSE notes unit=app-logic/PartitionFeatureTask tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/AssignPlateIds](AssignPlateIds.md) | app-logic | 8 |
| [app-logic/deprecated/PropertyValuePropogator](deprecated/PropertyValuePropogator.md) | app-logic | 7 |
| [app-logic/GenericPartitionFeatureTask](GenericPartitionFeatureTask.md) | app-logic | 1 |
| [app-logic/PartitionFeatureUtils](PartitionFeatureUtils.md) | app-logic | 1 |
| [app-logic/VgpPartitionFeatureTask](VgpPartitionFeatureTask.md) | app-logic | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/PartitionFeatureTask.h
python scripts/gpq.py def GPlatesAppLogic::PartitionFeatureTask --body
python scripts/gpq.py uses PartitionFeatureTask --kind class
python scripts/gpq.py hier PartitionFeatureTask
```
