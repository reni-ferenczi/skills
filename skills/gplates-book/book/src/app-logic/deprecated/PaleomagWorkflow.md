# PaleomagWorkflow

[Book TOC](../../../TOC.md) · [app-logic](../../../components/app-logic.md) · cluster Community 664 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/deprecated/PaleomagWorkflow.h` | C++ | 220 |
| `src/app-logic/deprecated/PaleomagWorkflow.cc` | C++ | 245 |

## Overview

[[[PROSE overview unit=app-logic/deprecated/PaleomagWorkflow tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::PaleomagWorkflow`](#gplatesapplogicpaleomagworkflow) | class | `FeatureCollectionWorkflow` | — | 0 | Class to handle velocity feature collection loading/unloading and calculations. |

## Members

### `GPlatesAppLogic::PaleomagWorkflow`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PaleomagWorkflow( ApplicationState &application_state, GPlatesPresentation::ViewState *view_state_ptr, GPlatesViewOperations::RenderedGeometryCollection::child_layer_owner_ptr_type paleomag_layer)` | constructor | `None` | public | FIXME: Presentation code should not be in here (this is app logic code). |
| `get_tag()` | method | `tag_type` | public | — |
| `get_priority()` | method | `priority_type` | public | Priority of this FeatureCollectionFileState workflow. |
| `add_file( FeatureCollectionFileState::file_reference file_iter, const ClassifyFeatureCollection::classifications_type &classification, bool used_by_higher_priority_workflow)` | method | `bool` | public | Callback method notifying of new file (called from FeatureCollectionFileState). |
| `remove_file( FeatureCollectionFileState::file_reference file_iter)` | method | `void` | public | Callback method notifying about to remove file (called from FeatureCollectionFileState). |
| `changed_file( FeatureCollectionFileState::file_reference file_iter, GPlatesFileIO::File &old_file, const ClassifyFeatureCollection::classifications_type &new_classification)` | method | `bool` | public | Callback method notifying file has changed (called from FeatureCollectionFileState). |
| `set_file_active( FeatureCollectionFileState::file_reference file_iter, bool active)` | method | `void` | public | — |
| `get_num_paleomag_feature_collections()` | method | `unsigned int` | public | Returns the number of velocity feature collections currently being calculated. |
| `draw_paleomag_features( Reconstruction &reconstruction, const double &reconstruction_time)` | method | `void` | public | — |
| `PaleomagFeatureCollectionInfo` | struct | `None` | private | Used to associate a mesh node feature collection with a velocity field feature collection so that when the former is deleted we can stop calculating velocities for the latter. |
| `paleomag_feature_collection_info_seq_type` | typedef | `std::vector<PaleomagFeatureCollectionInfo>` | private | Typedef for a sequence of associations between mesh node velocity feature collections and corresponding velocity field feature collections. |
| `d_model` | field | `GPlatesModel::ModelInterface` | private | — |
| `d_paleomag_feature_collection_infos` | field | `paleomag_feature_collection_info_seq_type` | private | — |
| `d_paleomag_layer` | field | `GPlatesViewOperations::RenderedGeometryCollection::child_layer_owner_ptr_type` | private | FIXME: Presentation code should not be in here (this is app logic code). |
| `d_view_state_ptr` | field | `GPlatesPresentation::ViewState` | private | For accessing the VGPVisibilitySettings |
| `s_instance_number` | field | `int` | private | FIXME: Find a better way to uniquely identify workflow instances |
| `d_instance_number` | field | `int` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_colour_from_feature( const GPlatesModel::FeatureCollectionHandle::iterator feature_iterator)` | function | `GPlatesGui::ColourProxy` | — |
| `s_instance_number` | variable | `int` | — |
| `GPLATES_APP_LOGIC_PALEOMAGWORKFLOW_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/deprecated/PaleomagWorkflow tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/deprecated/PaleomagWorkflow.h
python scripts/gpq.py def GPlatesAppLogic::PaleomagWorkflow --body
python scripts/gpq.py uses PaleomagWorkflow --kind class
python scripts/gpq.py hier PaleomagWorkflow
```
