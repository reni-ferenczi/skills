# UnsavedChangesTracker

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 769 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/UnsavedChangesTracker.h` | C++ | 284 |
| `src/gui/UnsavedChangesTracker.cc` | C++ | 407 |

## Overview

`UnsavedChangesTracker` draws together, in one place, everything the GUI shows
the user about which loaded files have unsaved changes, so that closing the
window, clearing the session, or loading a previous session/project can warn
before data is lost. The actual saved/unsaved state lives in the app-logic
tier (`FeatureCollectionFileState`, `FeatureCollectionFileIO`); this class
only observes it and drives the presentation — status icons on
`ViewportWindow`, highlighted rows in `ManageFeatureCollectionsDialog`, and the
confirmation prompt in `UnsavedChangesWarningDialog`.

It tracks "unsaved" at the level of individual `FeatureCollectionHandle`s by
keeping a `LoadedFile` entry — a `file_reference` plus a
`FeatureCollectionHandle::weak_ref` — for every currently loaded file, and
attaching an `UnsavedChangesCallback` (a `WeakReferenceCallback<FeatureCollectionHandle>`)
to each one so `publisher_modified()` fires back into the tracker whenever
that collection's revision changes. `connect_to_file_state_signals()` keeps
`d_loaded_files` in sync as files are added and removed by
`FeatureCollectionFileState`. `close_event_hook()`,
`clear_session_event_hook()`, `load_previous_session_event_hook()` and
`load_project_event_hook()` are the four places `ViewportWindow` calls into it
before letting one of those actions proceed, each returning an
`UnsavedChangesResult` that tells the caller whether to go ahead, discard, or
abort.

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

- `init()` must be called after `ViewportWindow::setupUi()`, not from the
  constructor — it wires up buttons and menus that do not exist yet at
  construction time.
- `d_loaded_files` deliberately keeps its own `LoadedFile` entries (a
  `file_reference` plus a `FeatureCollectionHandle::weak_ref`) instead of
  iterating `FeatureCollectionFileState`'s own list directly, because
  `handle_file_state_file_about_to_be_removed()` fires *before* the file is
  removed, and iterating the file state's live list at that point would still
  include the file that is about to disappear.
- `d_loaded_files` cannot be a `std::set` of weak-refs: the `UnsavedChangesCallback`
  is attached to each weak-ref only after it is copied into the container, and
  callbacks are not copied — so the weak-ref must be modifiable in place after
  insertion, which a set does not allow.
- `d_warning_dialog_ptr` is parented to `ViewportWindow`, so its lifetime is
  managed by Qt's parent/child ownership rather than by this class.
- `file_io_feedback()` and `manage_feature_collections_dialog()` locate their
  target objects via `ViewportWindow`'s Qt object tree rather than being
  passed in, to avoid widening the constructor's parameter list further.

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
