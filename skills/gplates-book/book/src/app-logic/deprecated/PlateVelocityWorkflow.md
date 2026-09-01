# PlateVelocityWorkflow

[Book TOC](../../../TOC.md) · [app-logic](../../../components/app-logic.md) · cluster Community 548 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/deprecated/PlateVelocityWorkflow.h` | C++ | 231 |
| `src/app-logic/deprecated/PlateVelocityWorkflow.cc` | C++ | 207 |

## Overview

A workflow for managing plate velocity feature collections within the application's file-based workflow system. It handles feature collection loading, unloading, and velocity calculations by tracking associations between velocity field feature collections and their corresponding mesh node data. The workflow solves velocities at specific reconstruction times with a specified anchored plate ID and renders results to target layers.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::PlateVelocityWorkflow`](#gplatesapplogicplatevelocityworkflow) | class | `FeatureCollectionWorkflow` | — | 0 | Class to handle velocity feature collection loading/unloading and calculations. |

## Members

### `GPlatesAppLogic::PlateVelocityWorkflow`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PlateVelocityWorkflow( ApplicationState &application_state, GPlatesViewOperations::RenderedGeometryCollection::child_layer_owner_ptr_type comp_mesh_point_layer, GPlatesViewOperations::RenderedGeometryCollection::child_layer_owner_ptr_type comp_mesh_arrow_layer)` | constructor | `None` | public | FIXME: Presentation code should not be in here (this is app logic code). |
| `get_tag()` | method | `tag_type` | public | — |
| `get_priority()` | method | `priority_type` | public | Priority of this FeatureCollectionFileState workflow. |
| `add_file( FeatureCollectionFileState::file_reference file_iter, const ClassifyFeatureCollection::classifications_type &classification, bool used_by_higher_priority_workflow)` | method | `bool` | public | Callback method notifying of new file (called from FeatureCollectionFileState). |
| `remove_file( FeatureCollectionFileState::file_reference file_iter)` | method | `void` | public | Callback method notifying about to remove file (called from FeatureCollectionFileState). |
| `changed_file( FeatureCollectionFileState::file_reference file_iter, GPlatesFileIO::File &old_file, const ClassifyFeatureCollection::classifications_type &new_classification)` | method | `bool` | public | Callback method notifying file has changed (called from FeatureCollectionFileState). |
| `set_file_active( FeatureCollectionFileState::file_reference file_iter, bool active)` | method | `void` | public | — |
| `get_num_velocity_feature_collections()` | method | `unsigned int` | public | Returns the number of velocity feature collections currently being calculated. |
| `get_velocity_feature_collection( unsigned int index)` | method | `GPlatesModel::FeatureCollectionHandle::weak_ref` | public | Returns the feature collection at index index. |
| `solve_velocities( Reconstruction &reconstruction, const double &reconstruction_time, GPlatesModel::integer_plate_id_type reconstruction_anchored_plate_id, const std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref> & reconstruction_features_collection)` | method | `void` | public | Solves velocities for all loaded velocity feature collections. |
| `VelocityFieldFeatureCollectionInfo` | struct | `None` | private | Used to associate a mesh node feature collection with a velocity field feature collection so that when the former is deleted we can stop calculating velocities for the latter. |
| `velocity_field_feature_collection_info_seq_type` | typedef | `std::vector<VelocityFieldFeatureCollectionInfo>` | private | Typedef for a sequence of associations between mesh node velocity feature collections and corresponding velocity field feature collections. |
| `d_model` | field | `GPlatesModel::ModelInterface` | private | — |
| `d_velocity_field_feature_collection_infos` | field | `velocity_field_feature_collection_info_seq_type` | private | — |
| `d_comp_mesh_point_layer` | field | `GPlatesViewOperations::RenderedGeometryCollection::child_layer_owner_ptr_type` | private | FIXME: Presentation code should not be in here (this is app logic code). |
| `d_comp_mesh_arrow_layer` | field | `GPlatesViewOperations::RenderedGeometryCollection::child_layer_owner_ptr_type` | private | — |
| `s_instance_number` | field | `int` | private | FIXME: Find a better way to uniquely identify workflow instances |
| `d_instance_number` | field | `int` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `s_instance_number` | variable | `int` | — |
| `GPLATES_APP_LOGIC_PLATEVELOCITYWORKFLOW_H` | macro | `None` | — |

## Notes

*None.*

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/deprecated/PlateVelocityWorkflow.h
python scripts/gpq.py def GPlatesAppLogic::PlateVelocityWorkflow --body
python scripts/gpq.py uses PlateVelocityWorkflow --kind class
python scripts/gpq.py hier PlateVelocityWorkflow
```
