# UnsavedChangesTracker

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 769 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/UnsavedChangesTracker.h` | C++ | 284 |
| `src/gui/UnsavedChangesTracker.cc` | C++ | 407 |

## Overview

[[[PROSE overview unit=gui/UnsavedChangesTracker tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::UnsavedChangesCallback`](#anonymousunsavedchangescallback) | class | [`GPlatesModel::WeakReferenceCallback<GPlatesModel::FeatureCollectionHandle>`](../model/WeakReferenceCallback.md) | — | 0 | Callback to receive notifications of changes to feature collections. |
| [`GPlatesGui::UnsavedChangesTracker`](#gplatesguiunsavedchangestracker) | class | `QObject` | — | 0 | This GUI class tracks changes to the saved/unsaved state of loaded files, and updates the GUI appropriately. |

## Members

### `(anonymous)::UnsavedChangesCallback`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UnsavedChangesCallback( GPlatesGui::UnsavedChangesTracker &tracker)` | constructor | `None` | public | — |
| `publisher_modified( const weak_reference_type &, const modified_event_type &)` | method | `void` | public | — |
| `publisher_deactivated( const weak_reference_type &, const deactivated_event_type &)` | method | `void` | public | — |
| `publisher_reactivated( const weak_reference_type &, const reactivated_event_type &)` | method | `void` | public | — |
| `publisher_about_to_be_destroyed( const weak_reference_type &, const about_to_be_destroyed_event_type &)` | method | `void` | public | — |
| `d_tracker_ptr` | field | `GPlatesGui::UnsavedChangesTracker` | private | Pointer to the Unsaved Changes Tracker, so we can actually do stuff to the rest of GPlates. |

### `GPlatesGui::UnsavedChangesTracker`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UnsavedChangesResult` | enum | `None` | public | The result of the close, clear, load previous session and load project event hooks. |
| `UnsavedChangesTracker( GPlatesQtWidgets::ViewportWindow &viewport_window_, GPlatesAppLogic::FeatureCollectionFileState &file_state_, GPlatesAppLogic::FeatureCollectionFileIO &feature_collection_file_io_, GPlatesPresentation::SessionManagement &session_management_, QObject *parent_ = NULL)` | constructor | `None` | public | — |
| `~UnsavedChangesTracker()` | destructor | `None` | public | — |
| `init()` | method | `void` | public | Connects buttons, adds menus, etc. |
| `has_unsaved_feature_collections()` | method | `bool` | public | True when there are any feature collections containing anything unsaved. |
| `list_unsaved_feature_collection_filenames()` | method | `QStringList` | public | List of file names of unsaved feature collections, for listing in the UnsavedChangesWarningDialog. |
| `close_event_hook()` | method | `UnsavedChangesResult` | public | Hook called when ViewportWindow is closing. |
| `clear_session_event_hook()` | method | `UnsavedChangesResult` | public | Called when the user wants to clear the session. |
| `load_previous_session_event_hook()` | method | `UnsavedChangesResult` | public | Called when the user wants to load a previous session. |
| `load_project_event_hook()` | method | `UnsavedChangesResult` | public | Called when the user wants to load a project. |
| `handle_model_has_changed()` | method | `void` | public | Slot called after some changes have been made to the Model. |
| `handle_file_state_files_added( GPlatesAppLogic::FeatureCollectionFileState &file_state, const std::vector<GPlatesAppLogic::FeatureCollectionFileState::file_reference> &new_files)` | method | `void` | private | — |
| `handle_file_state_file_about_to_be_removed( GPlatesAppLogic::FeatureCollectionFileState &file_state, GPlatesAppLogic::FeatureCollectionFileState::file_reference file)` | method | `void` | private | — |
| `manage_feature_collections_dialog` | field | `GPlatesQtWidgets::ManageFeatureCollectionsDialog` | private | Returns the ManageFeatureCollectionsDialog via ViewportWindow. |
| `file_io_feedback` | field | `GPlatesGui::FileIOFeedback` | private | Sneaky method to find the FileIOFeedback via ViewportWindow and the Qt object tree. |
| `connect_to_file_state_signals()` | method | `void` | private | Makes the signal/slot connections to FileState so we can maintain a bunch of weakrefs to loaded files and watch them for changes. |
| `LoadedFile` | class | `None` | private | Keeps track of a loaded file and its feature collection. |
| `loaded_files_container_type` | typedef | `std::vector<LoadedFile>` | private | — |
| `d_viewport_window_ptr` | field | `GPlatesQtWidgets::ViewportWindow` | private | Pointer to the main window to update with changes. |
| `d_warning_dialog_ptr` | field | `GPlatesQtWidgets::UnsavedChangesWarningDialog` | private | Pointer to the dialog we use to notify users on close. |
| `d_file_state_ptr` | field | `GPlatesAppLogic::FeatureCollectionFileState` | private | The loaded feature collection files. |
| `d_feature_collection_file_io_ptr` | field | `GPlatesAppLogic::FeatureCollectionFileIO` | private | Handles loading/unloading of feature collections. |
| `d_session_management_ptr` | field | `GPlatesPresentation::SessionManagement` | private | Detects unsaved changes in loaded projects. |
| `d_loaded_files` | field | `loaded_files_container_type` | private | We maintain a list of weak-refs to the currently loaded FeatureCollections. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_unsaved_changes_result( GPlatesQtWidgets::UnsavedChangesWarningDialog *warning_dialog_ptr, GPlatesQtWidgets::UnsavedChangesWarningDialog::ActionRequested action_requested, QStringList unsaved_feature_collection_filenames, bool has_unsaved_project_changes)` | function | `GPlatesGui::UnsavedChangesTracker::UnsavedChangesResult` | Returns true if user decides it's OK to discard the unsaved changes. |
| `GPLATES_GUI_UNSAVEDCHANGESTRACKER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/UnsavedChangesTracker tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/FileIOFeedback](FileIOFeedback.md) | gui | 25 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 7 |
| [qt-widgets/ImportRasterDialog](../qt-widgets/ImportRasterDialog.md) | qt-widgets | 1 |
| [qt-widgets/ImportScalarField3DDialog](../qt-widgets/ImportScalarField3DDialog.md) | qt-widgets | 1 |

## Related

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_file_state_ptr` | `file_state_files_added( GPlatesAppLogic::FeatureCollectionFileState &, const std::vector<GPlatesAppLogic::FeatureCollectionFileState::file_reference> &)` | `this` | `handle_file_state_files_added( GPlatesAppLogic::FeatureCollectionFileState &, const std::vector<GPlatesAppLogic::FeatureCollectionFileState::file_reference> &)` |
| `d_file_state_ptr` | `file_state_file_about_to_be_removed( GPlatesAppLogic::FeatureCollectionFileState &, GPlatesAppLogic::FeatureCollectionFileState::file_reference)` | `this` | `handle_file_state_file_about_to_be_removed( GPlatesAppLogic::FeatureCollectionFileState &, GPlatesAppLogic::FeatureCollectionFileState::file_reference)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/UnsavedChangesTracker.h
python scripts/gpq.py def GPlatesGui::UnsavedChangesTracker --body
python scripts/gpq.py uses UnsavedChangesTracker --kind class
python scripts/gpq.py hier UnsavedChangesTracker
```
