# FeatureCollectionFileState

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 767 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/FeatureCollectionFileState.h` | C++ | 561 |
| `src/app-logic/FeatureCollectionFileState.cc` | C++ | 545 |

## Overview

[[[PROSE overview unit=app-logic/FeatureCollectionFileState tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::FeatureCollectionFileState`](#gplatesapplogicfeaturecollectionfilestate) | class | `QObject`<br>`boost::noncopyable` | — | 0 | Holds information associated with the currently loaded and active feature collection files. |

## Members

### `GPlatesAppLogic::FeatureCollectionFileState`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `file_handle_type` | typedef | `std::size_t` | private | Typedef for a file handle. |
| `file_index_type` | typedef | `std::size_t` | public | Typedef for an index defining the order of currently loaded files. |
| `FileReference` | class | `None` | public | A reference to a file loaded into FeatureCollectionFileState. 'FileStateQualifiedType' can be either 'FeatureCollectionFileState' or 'const FeatureCollectionFileState'. |
| `const_file_reference` | typedef | `FileReference<const FeatureCollectionFileState>` | public | Typedef for a 'const' reference to a loaded file. |
| `file_reference` | typedef | `FileReference<FeatureCollectionFileState>` | public | Typedef for a 'non-const' reference to a loaded file. |
| `FeatureCollectionFileState( GPlatesModel::ModelInterface &model)` | constructor | `None` | public | Constructor. |
| `~FeatureCollectionFileState()` | destructor | `None` | public | Destructor. |
| `get_loaded_files()` | method | `std::vector<const_file_reference>` | public | Returns a sequence of 'const' file references to all currently loaded files. |
| `add_files( const std::vector<GPlatesFileIO::File::non_null_ptr_type> &files)` | method | `std::vector<file_reference>` | public | Adds multiple feature collection files and activates them. |
| `add_file( const GPlatesFileIO::File::non_null_ptr_type &file)` | method | `file_reference` | public | Adds a file and activates it. |
| `remove_file( file_reference file_ref)` | method | `void` | public | Remove file from the collection of currently loaded files. |
| `emit_file_reloaded()` | method | `void` | public | — |
| `file_state_files_added( GPlatesAppLogic::FeatureCollectionFileState &file_state, const std::vector<GPlatesAppLogic::FeatureCollectionFileState::file_reference> &new_files)` | method | `void` | public | The following signals only occur at the end (and in some cases also the beginning) of a public method of this class. |
| `file_state_file_about_to_be_removed( GPlatesAppLogic::FeatureCollectionFileState &file_state, GPlatesAppLogic::FeatureCollectionFileState::file_reference file)` | method | `void` | public | NOTE: Do not dereference the internal feature collection of file as it might be invalid (if this signal was generated when "undo"ing a file add). |
| `file_state_file_info_changed( GPlatesAppLogic::FeatureCollectionFileState &file_state, GPlatesAppLogic::FeatureCollectionFileState::file_reference file)` | method | `void` | public | — |
| `file_state_changed( GPlatesAppLogic::FeatureCollectionFileState &file_state)` | method | `void` | public | This signal is emitted \*after\* any file state has changed. |
| `file_reloaded( GPlatesAppLogic::FeatureCollectionFileState &file_state)` | method | `void` | public | — |
| `FileSlotExtra` | class | `None` | private | Contains a loaded file's shared reference and less frequently accessed information or information that is more expensive to copy. |
| `FileSlot` | class | `None` | private | A slot to store information about a file in a sequence of loaded files. |
| `file_slot_seq_type` | typedef | `std::vector<FileSlot>` | private | Typedef for a sequence of FileSlot objects. |
| `file_handles_seq_type` | typedef | `std::vector<file_handle_type>` | private | Typedef for a sequence of file handles. |
| `file_indices_seq_type` | typedef | `std::vector<file_index_type>` | private | Typedef for a sequence of indices indicating the order in which files were added. |
| `d_model` | field | `GPlatesModel::ModelInterface` | private | Used to add the feature collections of new files to the model. |
| `d_num_currently_loaded_files` | field | `std::size_t` | private | The number of loaded files (includes files that were deactivated in the \*model\* and subsequently reactivated). |
| `d_file_slots` | field | `file_slot_seq_type` | private | The sequence of all currently loaded files (includes those that have been conceptually deleted in the model - ie, deactivated in the model). |
| `d_free_file_handles` | field | `file_handles_seq_type` | private | A sequence of file handles that have been released and can be reused. |
| `d_file_indices` | field | `file_indices_seq_type` | private | The sequence of file indices. |
| `add_file_internal( const GPlatesFileIO::File::non_null_ptr_type &file)` | method | `file_handle_type` | private | — |
| `get_file` | field | `GPlatesFileIO::File::Reference` | private | — |
| `get_file_index( file_handle_type file_handle)` | method | `file_index_type` | private | — |
| `set_file_info( file_handle_type file_handle, const GPlatesFileIO::FileInfo &new_file_info, boost::optional<GPlatesFileIO::FeatureCollectionFileFormat::Configuration::shared_ptr_to_const_type> new_file_configuration)` | method | `void` | private | — |
| `deactivated_feature_collection( file_handle_type file_handle)` | method | `void` | private | — |
| `reactivated_feature_collection( file_handle_type file_handle)` | method | `void` | private | — |
| `destroying_feature_collection( file_handle_type file_handle)` | method | `void` | private | — |
| `FeatureCollectionUnloadCallback` | class | `None` | private | Keeps track of feature collections as they are deactivated and reactivated in the \*model\*. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `feature_collection_contains_feature( const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection_ref, const GPlatesModel::FeatureHandle::weak_ref &feature_ref)` | function | `bool` | — |
| `GPLATES_APP_LOGIC_FEATURECOLLECTIONFILESTATE_H` | macro | `None` | — |
| `get_file_reference_containing_feature( GPlatesAppLogic::FeatureCollectionFileState &file_state_ref, GPlatesModel::FeatureHandle::weak_ref feature_ref)` | function | `boost::optional<GPlatesAppLogic::FeatureCollectionFileState::file_reference>` | — |

## Notes

[[[PROSE notes unit=app-logic/FeatureCollectionFileState tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 96 |
| [qt-widgets/ManageFeatureCollectionsDialog](../qt-widgets/ManageFeatureCollectionsDialog.md) | qt-widgets | 79 |
| [qt-widgets/ManageFeatureCollectionsEditConfigurations](../qt-widgets/ManageFeatureCollectionsEditConfigurations.md) | qt-widgets | 59 |
| [app-logic/ReconstructGraphImpl](ReconstructGraphImpl.md) | app-logic | 54 |
| [app-logic/Layer](Layer.md) | app-logic | 48 |
| [app-logic/FeatureCollectionFileIO](FeatureCollectionFileIO.md) | app-logic | 37 |
| [qt-widgets/ChooseFeatureCollectionWidget](../qt-widgets/ChooseFeatureCollectionWidget.md) | qt-widgets | 37 |
| [app-logic/ReconstructGraph](ReconstructGraph.md) | app-logic | 34 |
| [qt-widgets/ScalarField3DLayerOptionsWidget](../qt-widgets/ScalarField3DLayerOptionsWidget.md) | qt-widgets | 31 |
| [app-logic/ApplicationState](ApplicationState.md) | app-logic | 29 |
| [gui/UnsavedChangesTracker](../gui/UnsavedChangesTracker.md) | gui | 28 |
| [qt-widgets/ColouringDialog](../qt-widgets/ColouringDialog.md) | qt-widgets | 27 |
| [qt-widgets/ChooseFeatureCollectionDialog](../qt-widgets/ChooseFeatureCollectionDialog.md) | qt-widgets | 26 |
| [qt-widgets/ShapefileAttributeViewerDialog](../qt-widgets/ShapefileAttributeViewerDialog.md) | qt-widgets | 21 |
| [qt-widgets/FeatureSummaryWidget](../qt-widgets/FeatureSummaryWidget.md) | qt-widgets | 20 |
| [qt-widgets/ManageFeatureCollectionsActionWidget](../qt-widgets/ManageFeatureCollectionsActionWidget.md) | qt-widgets | 20 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 18 |
| [qt-widgets/RasterLayerOptionsWidget](../qt-widgets/RasterLayerOptionsWidget.md) | qt-widgets | 17 |
| [app-logic/deprecated/PaleomagWorkflow](deprecated/PaleomagWorkflow.md) | app-logic | 16 |
| [app-logic/deprecated/PlateVelocityWorkflow](deprecated/PlateVelocityWorkflow.md) | app-logic | 16 |

*... and 46 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/FeatureCollectionFileState.h
python scripts/gpq.py def GPlatesAppLogic::FeatureCollectionFileState --body
python scripts/gpq.py uses FeatureCollectionFileState --kind class
python scripts/gpq.py hier FeatureCollectionFileState
```
