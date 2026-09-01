# FileIOFeedback

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 193 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/FileIOFeedback.h` | C++ | 550 |
| `src/gui/FileIOFeedback.cc` | C++ | 1672 |

## Overview

`FileIOFeedback` wraps GPlates' app-logic file loading and saving (`GPlatesAppLogic::FeatureCollectionFileIO`, `SessionManagement`) with the GUI feedback users expect: it prompts for filenames via `SaveFileDialog`/`OpenFileDialog`, and turns app-logic exceptions into error dialogs rather than letting them propagate. It was factored out of `ManageFeatureCollectionsDialog` so the load/save logic can be reused from menu actions, drag-and-drop, session restore and project files alike. Every load or session-restore path funnels through `try_catch_file_or_session_load_with_feedback`, which takes a `boost::function<bool ()>` — one of the free `*_try_catch_function` adapters that bind a specific app-logic call (`open_files_try_catch_function`, `reload_file_try_catch_function`, `open_previous_session_try_catch_function`, `open_project_try_catch_function`) — so the same exception handling and error reporting is written once and shared by every entry point.

Saving is layered similarly: `save_file_as_appropriate` picks between `save_file_in_place`, `save_file_as` and `save_file_copy` depending on whether the file already has a name and format, `get_save_file_filters_for_file` builds the matching Save-dialog filters from the `FeatureCollectionFileFormat::Registry` and `ReconstructMethodRegistry`, and `file_is_unnamed` supplies the shared definition of "not yet saved anywhere" that `save_files`/`save_all` use to decide which loaded files to touch. `CollectLoadedFilesScope` is a small RAII helper, independent of the rest of the class, that listens to `FeatureCollectionFileState::file_state_files_added` for the lifetime of the scope and reports which files were newly loaded — used where a caller needs to know exactly which files a load operation added, such as project or session restore.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::FileIOFeedback`](#gplatesguifileiofeedback) | class | `QObject` | — | 0 | This GUI class is responsible for wrapping the saving and loading app-logic operations with a thin layer of GUI feedback for users - in particular, calls to the save methods of this class will prompt the user for filenames appropriately, ... |
| [`GPlatesGui::CollectLoadedFilesScope`](#gplatesguicollectloadedfilesscope) | class | `QObject` | — | 0 | Used to collect the files loaded during the lifetime of a CollectLoadFilesScope object. |

## Members

### `GPlatesGui::FileIOFeedback`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PROJECT_FILENAME_EXTENSION` | field | `QString` | public | Filename extension for project files. |
| `FileIOFeedback( GPlatesAppLogic::ApplicationState &app_state_, GPlatesPresentation::ViewState &view_state_, GPlatesQtWidgets::ViewportWindow &viewport_window_, FeatureFocus &feature_focus_, QObject *parent_ = NULL)` | constructor | `None` | public | — |
| `~FileIOFeedback()` | destructor | `None` | public | — |
| `open_files( const QStringList &filenames)` | method | `void` | public | Opens the specified files, handling any exceptions thrown by popping up appropriate error dialogs. |
| `reload_file( GPlatesAppLogic::FeatureCollectionFileState::file_reference file)` | method | `void` | public | Reloads the file given by FileState file\_reference file and handles any exceptions thrown by popping up appropriate error dialogs. |
| `open_project( const QString &project_filename)` | method | `void` | public | Opens the specified project file and restores to a previously saved GPlates session, handling any exceptions thrown by popping up appropriate error dialogs. |
| `save_project( const QString &project_filename)` | method | `bool` | public | Saves the current GPlates session state to the specified project file, handling any exceptions thrown by popping up appropriate error dialogs. |
| `save_file_as_appropriate( GPlatesAppLogic::FeatureCollectionFileState::file_reference file)` | method | `bool` | public | Save a file, given by FileState file\_reference file. |
| `save_file_in_place( GPlatesAppLogic::FeatureCollectionFileState::file_reference file)` | method | `bool` | public | Save a file, given by FileState file\_reference file. |
| `save_file_as( GPlatesAppLogic::FeatureCollectionFileState::file_reference file)` | method | `bool` | public | Save a file, given by FileState file\_reference file, and prompt the user with a Save As dialog to let them specify a new name for the loaded file. |
| `save_file_copy( GPlatesAppLogic::FeatureCollectionFileState::file_reference file)` | method | `bool` | public | Save a file, given by FileState file\_reference file, and prompt the user with a Save a Copy dialog to let them specify a new name for the loaded file. |
| `save_file( GPlatesAppLogic::FeatureCollectionFileState::file_reference file)` | method | `bool` | public | Save a file, given by FileState file\_reference file. |
| `save_files( const std::vector<GPlatesAppLogic::FeatureCollectionFileState::file_reference> &files, bool include_unnamed_files, bool only_unsaved_changes)` | method | `bool` | public | Save the specified files as though the 'save in place' button was used. |
| `save_all( bool include_unnamed_files, bool only_unsaved_changes)` | method | `bool` | public | Save all files as though the 'save in place' button was used. |
| `create_file( const GPlatesFileIO::File::non_null_ptr_type &file)` | method | `boost::optional<GPlatesAppLogic::FeatureCollectionFileState::file_reference>` | public | Creates, and saves, a file named filename and saves feature\_collection to the file, handling any exceptions thrown by popping up appropriate error dialogs (and returning false). |
| `extract_project_filenames_from_file_urls( const QList<QUrl> &urls)` | method | `QStringList` | public | Returns those URLs that are project files. |
| `extract_feature_collection_filenames_from_file_urls( const QList<QUrl> &urls)` | method | `QStringList` | public | Returns those URLs that are filenames with extensions registered as feature collection file formats. |
| `open_files()` | method | `void` | public | Opens an Open File dialog allowing the user to select zero or more files, then opens them. |
| `clear_session()` | method | `bool` | public | Clears the current session. |
| `open_previous_session( int session_slot_to_load = 0)` | method | `void` | public | Opens the set of files from the user's previous session. |
| `open_project()` | method | `void` | public | Opens an Open Project dialog allowing the user to select a project file to restore to a previously saved GPlates session. |
| `save_project()` | method | `bool` | public | Saves the current GPlates session state to the current project if the current session is a project, or calls save\_project\_as to first ask the user to select a project file to save to. |
| `save_project_as()` | method | `bool` | public | Opens an Save Project dialog allowing the user to select a project file to save the current GPlates session state to. |
| `save_file( GPlatesFileIO::File::Reference &file_ref, bool clear_unsaved_changes = true)` | method | `bool` | private | Saves the feature collection in file\_ref to the filename in file\_ref. |
| `open_project_internal( const QString &project_filename, bool save_current_session)` | method | `void` | private | Opens a project without first checking for unsaved changes. |
| `try_catch_file_or_session_load_with_feedback( boost::function<bool ()> file_or_session_load_func, boost::optional<QString> filename = boost::none)` | method | `bool` | private | Allows calling multiple functions that throw the same types of exceptions and handles those exceptions in one place. |
| `app_state` | field | `GPlatesAppLogic::ApplicationState` | private | Quick method to get at the ApplicationState from inside this class. |
| `view_state` | field | `GPlatesPresentation::ViewState` | private | Quick method to get at the ViewState from inside this class. |
| `manage_feature_collections_dialog` | field | `GPlatesQtWidgets::ManageFeatureCollectionsDialog` | private | Returns the ManageFeatureCollectionsDialog via ViewportWindow. |
| `unsaved_changes_tracker` | field | `GPlatesGui::UnsavedChangesTracker` | private | Sneaky method to find the UnsavedChangesTracker via ViewportWindow and the Qt object tree. |
| `d_app_state_ptr` | field | `GPlatesAppLogic::ApplicationState` | private | ApplicationState for getting access to important file-loading stuff. |
| `d_view_state_ptr` | field | `GPlatesPresentation::ViewState` | private | ViewState for getting access to session management. |
| `d_viewport_window_ptr` | field | `GPlatesQtWidgets::ViewportWindow` | private | Pointer to the main window, to pop up error dialogs from etc. |
| `d_file_state_ptr` | field | `GPlatesAppLogic::FeatureCollectionFileState` | private | The loaded feature collection files. |
| `d_feature_collection_file_io_ptr` | field | `GPlatesAppLogic::FeatureCollectionFileIO` | private | Handles loading/unloading of feature collections. |
| `d_file_format_registry_ptr` | field | `GPlatesFileIO::FeatureCollectionFileFormat::Registry` | private | The registry of file formats. |
| `d_feature_focus` | field | `FeatureFocus` | private | Stores the notion of which feature has the focus. |
| `d_save_file_as_dialog` | field | `GPlatesQtWidgets::SaveFileDialog` | private | The save file as dialog box. |
| `d_save_file_copy_dialog` | field | `GPlatesQtWidgets::SaveFileDialog` | private | The save file copy dialog box. |
| `d_save_project_dialog` | field | `GPlatesQtWidgets::SaveFileDialog` | private | The save project dialog box. |
| `d_open_files_dialog` | field | `GPlatesQtWidgets::OpenFileDialog` | private | The open files dialog box. |
| `d_open_project_dialog` | field | `GPlatesQtWidgets::OpenFileDialog` | private | The open project dialog box. |
| `d_open_project_relative_or_absolute_dialog_ptr` | field | `GPlatesQtWidgets::OpenProjectRelativeOrAbsoluteDialog` | private | Pointer to the dialog we use to ask users whether to load data files relative to the loaded project (or use absolute paths) when it's ambiguous. |
| `d_missing_session_files_dialog_ptr` | field | `GPlatesQtWidgets::MissingSessionFilesDialog` | private | Pointer to the dialog we use to ask users to locate the missing data files when a project/session is loaded. |
| `d_ogr_srs_write_option_dialog_ptr` | field | `GPlatesQtWidgets::OgrSrsWriteOptionDialog` | private | Pointer to the dialog we use to notify users of a non-WGS84 SRS associated an original file on disk, and to obtain the users SRS behaviour preference. |

### `GPlatesGui::CollectLoadedFilesScope`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CollectLoadedFilesScope( GPlatesAppLogic::FeatureCollectionFileState *feature_collection_file_state)` | constructor | `None` | public | — |
| `get_loaded_files` | field | `std::vector<GPlatesAppLogic::FeatureCollectionFileState::file_reference>` | public | Get the files loaded during the lifetime of 'this' object. |
| `handle_file_state_files_added( GPlatesAppLogic::FeatureCollectionFileState &file_state, const std::vector<GPlatesAppLogic::FeatureCollectionFileState::file_reference> &new_files)` | method | `void` | private | — |
| `d_loaded_files` | field | `std::vector<GPlatesAppLogic::FeatureCollectionFileState::file_reference>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `add_filename_extensions_to_file_dialog_filter( FileDialogFilter &filter, GPlatesFileIO::FeatureCollectionFileFormat::Format file_format, const GPlatesFileIO::FeatureCollectionFileFormat::Registry &file_format_registry)` | function | `void` | — |
| `create_file_dialog_filter( GPlatesFileIO::FeatureCollectionFileFormat::Format file_format, const GPlatesFileIO::FeatureCollectionFileFormat::Registry &file_format_registry)` | function | `FileDialogFilter` | — |
| `create_all_filter()` | function | `FileDialogFilter` | — |
| `get_load_file_filters( const GPlatesFileIO::FeatureCollectionFileFormat::Registry &file_format_registry)` | function | `GPlatesQtWidgets::OpenFileDialog::filter_list_type` | Builds a list of input filters for opening all types of feature collections. |
| `get_save_file_filters_for_file( GPlatesAppLogic::FeatureCollectionFileState::file_reference file_ref, const GPlatesAppLogic::ReconstructMethodRegistry &reconstruct_method_registry, const GPlatesFileIO::FeatureCollectionFileFormat::Registry &file_format_registry)` | function | `GPlatesQtWidgets::SaveFileDialog::filter_list_type` | Builds the specially-formatted list of suitable output filters given a file to be saved. |
| `get_load_save_project_filters()` | function | `GPlatesQtWidgets::OpenFileDialog::filter_list_type` | Builds a list of filters for loading/saving project files. |
| `file_is_unnamed( GPlatesAppLogic::FeatureCollectionFileState::file_reference file)` | function | `bool` | Here is the logic for determining if a file is considered 'unnamed', i.e. not yet having a name associated with it, no presence on disk. |
| `set_ogr_configuration_write_behaviour( boost::shared_ptr<GPlatesFileIO::FeatureCollectionFileFormat::OGRConfiguration> &ogr_config, const GPlatesQtWidgets::OgrSrsWriteOptionDialog::BehaviourRequested &behaviour)` | function | `void` | — |
| `show_ogr_srs_dialog_if_necessary( const std::vector<GPlatesAppLogic::FeatureCollectionFileState::file_reference> &files, GPlatesQtWidgets::OgrSrsWriteOptionDialog *ogr_srs_write_option_dialog)` | function | `bool` | — |
| `show_save_project_unsaved_feature_collections_message_box_if_necessary( QWidget *parent_widget, GPlatesGui::UnsavedChangesTracker &unsaved_changes_tracker)` | function | `bool` | Shows the unsaved feature collections message box, if necessary, to inform the user they need to first either save or discard any unsaved feature collections before they can save the current session as a project file. |
| `open_files_try_catch_function( GPlatesAppLogic::FeatureCollectionFileIO &file_io, const QStringList &filenames, std::vector<GPlatesAppLogic::FeatureCollectionFileState::file_reference> &loaded_files)` | function | `bool` | Helps convert FeatureCollectionFileIO::load\_files() to signature required by 'try\_catch\_file\_or\_session\_load\_with\_feedback()' by making return parameter an argument. |
| `reload_file_try_catch_function( GPlatesAppLogic::FeatureCollectionFileIO &file_io, const GPlatesAppLogic::FeatureCollectionFileState::file_reference &file)` | function | `bool` | Helps convert FeatureCollectionFileIO::reload\_file() to signature required by 'try\_catch\_file\_or\_session\_load\_with\_feedback()' which requires a boolean return value. |
| `open_previous_session_try_catch_function( GPlatesPresentation::SessionManagement &sm, int session_slot_to_load, bool save_current_session, GPlatesQtWidgets::MissingSessionFilesDialog *missing_session_files_dialog_ptr)` | function | `bool` | Helps convert SessionManagement::load\_previous\_session() to signature required by 'try\_catch\_file\_or\_session\_load\_with\_feedback()' which requires a boolean return value. |
| `open_project_try_catch_function( GPlatesPresentation::SessionManagement &sm, const QString &project_filename, bool save_current_session, GPlatesQtWidgets::OpenProjectRelativeOrAbsoluteDialog *open_project_relative_or_absolute_dialog_ptr, GPlatesQtWidgets::MissingSessionFilesDialog *missing_session_files_dialog_ptr)` | function | `bool` | Helps convert SessionManagement::load\_project() to signature required by 'try\_catch\_file\_or\_session\_load\_with\_feedback()' which requires a boolean return value. |
| `PROJECT_FILENAME_EXTENSION` | variable | `QString` | — |
| `GPLATES_GUI_FILEIOFEEDBACK_H` | macro | `None` | — |

## Notes

- `manage_feature_collections_dialog` and `unsaved_changes_tracker` are not owned here: both are looked up through `d_viewport_window_ptr` (the latter via the Qt object tree), so this class depends on `ViewportWindow` having already constructed those objects.
- `open_project_internal` and the raw `save_file(File::Reference &, ...)` overload skip the unsaved-changes prompt that the public `open_project`/`save_*` entry points perform — call them directly only when that check has already been handled (e.g. from inside `try_catch_file_or_session_load_with_feedback`).
- Every public load/save entry point is expected to route through `try_catch_file_or_session_load_with_feedback` so that app-logic exceptions are caught and reported once, in one place, instead of duplicating error-dialog logic at each call site.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ManageFeatureCollectionsDialog](../qt-widgets/ManageFeatureCollectionsDialog.md) | qt-widgets | 44 |
| [qt-widgets/ImportRasterDialog](../qt-widgets/ImportRasterDialog.md) | qt-widgets | 23 |
| [gui/UnsavedChangesTracker](UnsavedChangesTracker.md) | gui | 16 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 15 |
| [entry-points/gplates_main](../entry-points/gplates_main.md) | entry-points | 7 |
| [gui/GPlatesQApplication](GPlatesQApplication.md) | gui | 3 |
| [qt-widgets/ImportScalarField3DDialog](../qt-widgets/ImportScalarField3DDialog.md) | qt-widgets | 3 |
| [gui/SessionMenu](SessionMenu.md) | gui | 2 |
| [qt-widgets/GenerateVelocityDomainCitcomsDialog](../qt-widgets/GenerateVelocityDomainCitcomsDialog.md) | qt-widgets | 1 |
| [qt-widgets/GenerateVelocityDomainLatLonDialog](../qt-widgets/GenerateVelocityDomainLatLonDialog.md) | qt-widgets | 1 |
| [qt-widgets/GenerateVelocityDomainTerraDialog](../qt-widgets/GenerateVelocityDomainTerraDialog.md) | qt-widgets | 1 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `feature_collection_file_state` | `file_state_files_added( GPlatesAppLogic::FeatureCollectionFileState &, const std::vector<GPlatesAppLogic::FeatureCollectionFileState::file_reference> &)` | `this` | `handle_file_state_files_added( GPlatesAppLogic::FeatureCollectionFileState &, const std::vector<GPlatesAppLogic::FeatureCollectionFileState::file_reference> &)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/FileIOFeedback.h
python scripts/gpq.py def GPlatesGui::FileIOFeedback --body
python scripts/gpq.py uses FileIOFeedback --kind class
python scripts/gpq.py hier FileIOFeedback
```
