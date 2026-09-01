# PartitionFeatureTask

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 1820 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/PartitionFeatureTask.h` | C++ | 112 |
| `src/app-logic/PartitionFeatureTask.cc` | C++ | 58 |

## Overview

`PartitionFeatureTask` is the strategy interface behind cookie-cutter plate-id assignment: given a feature and the `GeometryCookieCutter` that has already partitioned its geometry against a set of polygons, a task decides (`can_partition_feature`) whether it applies to that feature, and if so assigns the partitioning polygon's properties (`partition_feature`) to the feature and to any clones created to hold the other partitioned pieces of its geometry.

`get_partition_feature_tasks` builds the fixed, ordered pipeline of tasks that `AssignPlateIds` runs a feature through: a `VgpPartitionFeatureTask` for virtual-geomagnetic-pole features first, then a `GenericPartitionFeatureTask` last as the catch-all, since it can process any feature type. Tasks are tried front-to-back and the caller stops at the first one whose `can_partition_feature` returns true, so ordering from most specific to least specific is load-bearing.

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

- The `GenericPartitionFeatureTask` entry must stay last in `get_partition_feature_tasks`'s returned sequence, since it accepts any feature type and would otherwise shadow the more specific `VgpPartitionFeatureTask`.
- `respect_feature_time_period` defaults to true but some derived tasks (noted on `partition_feature`: `VgpPartitionFeatureTask`) ignore it.
- `partition_feature` can both modify `feature_ref` in place and create clones of it to hold other pieces of the partitioned geometry; callers should not assume `feature_ref` alone captures the full result.

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
