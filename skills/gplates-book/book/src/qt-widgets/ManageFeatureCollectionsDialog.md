# ManageFeatureCollectionsDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 357 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ManageFeatureCollectionsDialog.h` | C++ | 389 |
| `src/qt-widgets/ManageFeatureCollectionsDialog.cc` | C++ | 1050 |
| `src/qt-widgets/ManageFeatureCollectionsDialogUi.ui` | Qt form | 307 |

## Overview

[[[PROSE overview unit=qt-widgets/ManageFeatureCollectionsDialog tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::ColumnNames::ColumnName`](#anonymouscolumnnamescolumnname) | enum | — | — | 0 | These should match the columns set up in the designer. |
| [`GPlatesQtWidgets::ManageFeatureCollectionsDialog`](#gplatesqtwidgetsmanagefeaturecollectionsdialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_ManageFeatureCollectionsDialog` | — | 0 | — |

## Members

### `(anonymous)::ColumnNames::ColumnName`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FILENAME` | enumerator | `None` | — | — |
| `FORMAT` | enumerator | `None` | — | — |
| `ACTIONS` | enumerator | `None` | — | — |

### `GPlatesQtWidgets::ManageFeatureCollectionsDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ManageFeatureCollectionsDialog( GPlatesAppLogic::FeatureCollectionFileState &file_state, GPlatesAppLogic::FeatureCollectionFileIO &feature_collection_file_io, GPlatesGui::FileIOFeedback &gui_file_io_feedback, GPlatesAppLogic::ReconstructGraph &reconstruct_graph, GPlatesPresentation::ViewState& d_view_state, QWidget *pa ...` | constructor | `None` | public | — |
| `register_edit_configuration( GPlatesFileIO::FeatureCollectionFileFormat::Format file_format, const boost::shared_ptr<ManageFeatureCollections::EditConfiguration> &edit_configuration_ptr)` | method | `void` | public | Registers an edit configuration for the specified file format. |
| `edit_configuration( ManageFeatureCollectionsActionWidget *action_widget_ptr)` | method | `void` | public | Initiates editing of the file configuration. |
| `save_file( ManageFeatureCollectionsActionWidget *action_widget_ptr)` | method | `void` | public | Causes the file referenced by the action widget to be saved with its current name. |
| `save_file_as( ManageFeatureCollectionsActionWidget *action_widget_ptr)` | method | `void` | public | Causes the file referenced by the action widget to be saved with a new name. |
| `save_file_copy( ManageFeatureCollectionsActionWidget *action_widget_ptr)` | method | `void` | public | Causes a copy of the file referenced by the action widget to be saved using different name. |
| `reload_file( ManageFeatureCollectionsActionWidget *action_widget_ptr)` | method | `void` | public | Unloads and re-loads the file referenced by the action widget. |
| `unload_file( ManageFeatureCollectionsActionWidget *action_widget_ptr)` | method | `void` | public | Causes the file referenced by the action widget to be unloaded, and removed from the table. |
| `highlight_unsaved_changes()` | method | `void` | public | Recolours table rows' background colours based on saved/unsaved state. |
| `save_all_named_changes()` | method | `void` | public | Saves-in-place all files with unsaved changes, except for those which have not yet been given filenames. |
| `handle_file_state_files_added( GPlatesAppLogic::FeatureCollectionFileState &file_state, const std::vector<GPlatesAppLogic::FeatureCollectionFileState::file_reference> &new_files)` | method | `void` | private | NOTE: all signals/slots should use namespace scope for all arguments otherwise differences between signals and slots will cause Qt to not be able to connect them at runtime. |
| `handle_file_state_file_about_to_be_removed( GPlatesAppLogic::FeatureCollectionFileState &file_state, GPlatesAppLogic::FeatureCollectionFileState::file_reference file)` | method | `void` | private | — |
| `handle_file_state_file_info_changed( GPlatesAppLogic::FeatureCollectionFileState &file_state, GPlatesAppLogic::FeatureCollectionFileState::file_reference file)` | method | `void` | private | — |
| `header_section_clicked( int section_index)` | method | `void` | private | — |
| `handle_selection_changed()` | method | `void` | private | — |
| `save_selected()` | method | `void` | private | — |
| `reload_selected()` | method | `void` | private | — |
| `unload_selected()` | method | `void` | private | — |
| `clear_selection()` | method | `void` | private | — |
| `clear_rows()` | method | `void` | protected | Deletes items and completely removes all rows from the table. |
| `add_row( GPlatesAppLogic::FeatureCollectionFileState::file_reference file_it, bool should_highlight_unsaved_changes = true)` | method | `void` | protected | Adds a row to the table, creating a ManageFeatureCollectionsActionWidget to store the FileInfo and the buttons used to interact with the file. should\_highlight\_unsaved\_changes might be false if you're adding many rows and you want to ... |
| `update_row( int row, GPlatesAppLogic::FeatureCollectionFileState::file_reference file, bool should_highlight_unsaved_changes = true)` | method | `void` | protected | Updates the specified row in the table to a new filename (FileInfo) and default file configuration if one is required for the file's format. should\_highlight\_unsaved\_changes might be false if you're updatin many rows and you want to ... |
| `find_row( ManageFeatureCollectionsActionWidget *action_widget_ptr)` | method | `int` | protected | Locates the current row of the table used by the given action widget. |
| `find_row( GPlatesAppLogic::FeatureCollectionFileState::file_reference file_it)` | method | `int` | protected | Locates the current row of the table used by the given file info iterator. |
| `remove_row( ManageFeatureCollectionsActionWidget *action_widget_ptr)` | method | `void` | protected | Removes the row indicated by the given action widget. |
| `remove_row( int row)` | method | `void` | protected | Removes the row indicated indexed by row. |
| `save_all( bool include_unnamed_files, bool only_unsaved_changes)` | method | `void` | protected | Goes through each loaded file and saves-in-place. |
| `set_row_background_colour( int row)` | method | `void` | protected | Recolours a single row's background based on saved/unsaved state. |
| `dragEnterEvent( QDragEnterEvent *ev)` | method | `void` | protected | Reimplementation of drag/drop events so we can handle users dragging files onto Manage Feature Collections Dialog. |
| `dropEvent( QDropEvent *ev)` | method | `void` | protected | Reimplementation of drag/drop events so we can handle users dragging files onto Manage Feature Collections Dialog. |
| `edit_configuration_map_type` | typedef | `std::map< GPlatesFileIO::FeatureCollectionFileFormat::Format, boost::shared_ptr<ManageFeatureCollections::EditConfiguration> >` | private | Typedef for a mapping of file formats to registered edit configurations. |
| `ColumnSort` | struct | `None` | private | Identifies which column (if any) is sorted and whether it's sorted ascending or descending. |
| `d_file_format_registry` | field | `GPlatesFileIO::FeatureCollectionFileFormat::Registry` | private | Registry of file formats. |
| `d_file_state` | field | `GPlatesAppLogic::FeatureCollectionFileState` | private | The loaded feature collection files. |
| `d_feature_collection_file_io` | field | `GPlatesAppLogic::FeatureCollectionFileIO` | private | Handles loading/unloading of feature collections. |
| `d_gui_file_io_feedback_ptr` | field | `QPointer<GPlatesGui::FileIOFeedback>` | private | GUI wrapper around saving/loading to handle feedback dialogs, progress bars, etc. |
| `d_reconstruct_graph` | field | `GPlatesAppLogic::ReconstructGraph` | private | As an optimisation, group a sequence of file unloads into a single remove layers group. |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_edit_configurations` | field | `edit_configuration_map_type` | private | The registered edit configurations (mapped to file formats). |
| `d_column_sort` | field | `boost::optional<ColumnSort>` | private | The column (and sort order) currently used for sorting, if sorting enabled. |
| `connect_to_file_state_signals()` | method | `void` | private | Connect to signals from a FeatureCollectionFileState object. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `bg_colour_normal(Qt::white)` | function | `QColor` | The colours to be used for row backgrounds and icon colours. |
| `bg_colour_unsaved` | variable | `QColor` | — |
| `bg_colour_new_feature_collection` | variable | `QColor` | — |
| `get_format_for_file( GPlatesAppLogic::FeatureCollectionFileState::file_reference file, const GPlatesFileIO::FeatureCollectionFileFormat::Registry &file_format_registry)` | function | `boost::optional<GPlatesFileIO::FeatureCollectionFileFormat::Format>` | Returns the file format for a file if it was identified, otherwise returns boost::none. |
| `get_format_description_for_file( boost::optional<GPlatesFileIO::FeatureCollectionFileFormat::Format> file_format, const GPlatesFileIO::FeatureCollectionFileFormat::Registry &file_format_registry)` | function | `QString` | Returns the file format for a file. |
| `get_action_widget( QTableWidget *qtable_widget, int row)` | function | `GPlatesQtWidgets::ManageFeatureCollectionsActionWidget` | — |
| `get_selected_action_widgets( QTableWidget *qtable_widget)` | function | `std::vector<GPlatesQtWidgets::ManageFeatureCollectionsActionWidget *>` | Returns a list of selected files (rows) by returning the action widget in each selected row. |
| `get_selected_files( QTableWidget *qtable_widget)` | function | `std::vector<GPlatesAppLogic::FeatureCollectionFileState::file_reference>` | Returns a list of selected files (rows) by returning the file reference in each selected row. |
| `set_row_background( QTableWidget *qtable_widget, int row, const QBrush &bg_colour)` | function | `void` | Convenience function to change the background for all table cells on a given row. |
| `create_pixmap_from_colour( const QColor &colour, int size = 16)` | function | `QPixmap` | Creates a colour 'swatch' pixmap consisting of the given colour. |
| `GPLATES_GUI_MANAGEFEATURECOLLECTIONSDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ManageFeatureCollectionsDialog tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ManageFeatureCollectionsEditConfigurations](ManageFeatureCollectionsEditConfigurations.md) | qt-widgets | 10 |
| [qt-widgets/ManageFeatureCollectionsActionWidget](ManageFeatureCollectionsActionWidget.md) | qt-widgets | 7 |
| [gui/UnsavedChangesTracker](../gui/UnsavedChangesTracker.md) | gui | 2 |
| [gui/Dialogs](../gui/Dialogs.md) | gui | 1 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 1 |
| [qt-widgets/ViewportWindow](ViewportWindow.md) | qt-widgets | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ManageFeatureCollectionsDialog` | `QDialog` | Manage Feature Collections | 15 |

**Qt signal/slot connections** (11 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_open_file` | `clicked()` | `d_gui_file_io_feedback_ptr` | `open_files()` |
| `button_save_all_changes` | `clicked()` | `this` | `save_all_named_changes()` |
| `button_save_selected` | `clicked()` | `this` | `save_selected()` |
| `button_reload_selected` | `clicked()` | `this` | `reload_selected()` |
| `button_unload_selected` | `clicked()` | `this` | `unload_selected()` |
| `button_clear_selection` | `clicked()` | `this` | `clear_selection()` |
| `table_feature_collections` | `itemSelectionChanged()` | `this` | `handle_selection_changed()` |
| `table_feature_collections->horizontalHeader()` | `sectionClicked(int)` | `this` | `header_section_clicked(int)` |
| `&d_file_state` | `file_state_files_added( GPlatesAppLogic::FeatureCollectionFileState &, const std::vector<GPlatesAppLogic::FeatureCollectionFileState::file_reference> &)` | `this` | `handle_file_state_files_added( GPlatesAppLogic::FeatureCollectionFileState &, const std::vector<GPlatesAppLogic::FeatureCollectionFileState::file_reference> &)` |
| `&d_file_state` | `file_state_file_about_to_be_removed( GPlatesAppLogic::FeatureCollectionFileState &, GPlatesAppLogic::FeatureCollectionFileState::file_reference)` | `this` | `handle_file_state_file_about_to_be_removed( GPlatesAppLogic::FeatureCollectionFileState &, GPlatesAppLogic::FeatureCollectionFileState::file_reference)` |
| `&d_file_state` | `file_state_file_info_changed( GPlatesAppLogic::FeatureCollectionFileState &, GPlatesAppLogic::FeatureCollectionFileState::file_reference)` | `this` | `handle_file_state_file_info_changed( GPlatesAppLogic::FeatureCollectionFileState &, GPlatesAppLogic::FeatureCollectionFileState::file_reference)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ManageFeatureCollectionsDialog.h
python scripts/gpq.py def GPlatesQtWidgets::ManageFeatureCollectionsDialog --body
python scripts/gpq.py uses ManageFeatureCollectionsDialog --kind class
python scripts/gpq.py hier ManageFeatureCollectionsDialog
```
