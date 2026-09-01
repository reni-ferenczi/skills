# ColouringDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 119 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ColouringDialog.h` | C++ | 399 |
| `src/qt-widgets/ColouringDialog.cc` | C++ | 1180 |
| `src/qt-widgets/ColouringDialogUi.ui` | Qt form | 260 |

## Overview

[[[PROSE overview unit=qt-widgets/ColouringDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::FeatureCollectionRemover`](#anonymousfeaturecollectionremover) | class | [`GPlatesModel::WeakReferenceCallback<const GPlatesModel::FeatureCollectionHandle>`](../model/WeakReferenceCallback.md) | — | 0 | Automagically removes a feature collection from the combobox when it gets deactivated. |
| [`GPlatesQtWidgets::ColouringDialog`](#gplatesqtwidgetscolouringdialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_ColouringDialog` | — | 0 | — |

## Members

### `(anonymous)::FeatureCollectionRemover`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FeatureCollectionRemover( QComboBox *combobox)` | constructor | `None` | public | — |
| `publisher_deactivated( const GPlatesModel::WeakReference<const GPlatesModel::FeatureCollectionHandle> &reference, const deactivated_event_type &event)` | method | `void` | public | — |
| `d_combobox` | field | `QComboBox` | private | — |

### `GPlatesQtWidgets::ColouringDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ColouringDialog( GPlatesPresentation::ViewState &view_state, const GlobeAndMapWidget &existing_globe_and_map_widget, ReadErrorAccumulationDialog &read_error_accumulation_dialog, QWidget* parent_ = NULL)` | constructor | `None` | public | Constructs a ColouringDialog. |
| `handle_close_button_clicked( bool checked)` | method | `void` | private | — |
| `handle_open_button_clicked( bool checked)` | method | `void` | private | — |
| `handle_add_button_clicked( bool checked)` | method | `void` | private | — |
| `handle_remove_button_clicked( bool checked)` | method | `void` | private | — |
| `handle_categories_table_cell_changed( int current_row, int current_column, int previous_row, int previous_column)` | method | `void` | private | — |
| `handle_main_repaint( bool mouse_down)` | method | `void` | private | — |
| `handle_repaint( bool mouse_down)` | method | `void` | private | — |
| `handle_colour_schemes_list_selection_changed()` | method | `void` | private | — |
| `handle_show_thumbnails_changed( int state)` | method | `void` | private | — |
| `handle_feature_collections_combobox_index_changed( int index)` | method | `void` | private | — |
| `handle_use_global_changed( int state)` | method | `void` | private | — |
| `edit_current_colour_scheme()` | method | `void` | private | — |
| `handle_files_added( GPlatesAppLogic::FeatureCollectionFileState &file_state, const std::vector<GPlatesAppLogic::FeatureCollectionFileState::file_reference> &new_files)` | method | `void` | private | — |
| `handle_file_info_changed( GPlatesAppLogic::FeatureCollectionFileState &file_state, GPlatesAppLogic::FeatureCollectionFileState::file_reference file)` | method | `void` | private | — |
| `PreviewColourScheme` | class | `None` | private | This is a special colour scheme that wraps around the ViewState's copy of ColourSchemeDelegator (i.e. the one used by the main window), and allows the colour scheme for a particular feature collection (or globally) to be changed in order ... |
| `reposition()` | method | `void` | private | — |
| `make_signal_slot_connections()` | method | `void` | private | — |
| `populate_colour_scheme_categories()` | method | `void` | private | — |
| `populate_feature_collections()` | method | `void` | private | — |
| `load_category( GPlatesGui::ColourSchemeCategory::Type category, int id_to_select = -1)` | method | `void` | private | — |
| `start_rendering_from( int list_index)` | method | `void` | private | Kicks off the rendering loop. |
| `load_colour_scheme_from( QListWidgetItem *item)` | method | `void` | private | Modifies d\_preview\_colour\_scheme based on the colour scheme index stored associated with the item. |
| `open_cpt_files( const QStringList &file_list)` | method | `void` | private | — |
| `open_cpt_files( const QStringList &file_list, const PropertyExtractorType &property_extractor)` | method | `void` | private | — |
| `add_single_colour()` | method | `void` | private | — |
| `insert_list_widget_item( const GPlatesGui::ColourSchemeInfo &colour_scheme_info, GPlatesGui::ColourSchemeContainer::id_type id)` | method | `void` | private | — |
| `dragEnterEvent( QDragEnterEvent *ev)` | method | `void` | private | Reimplementation of drag/drop events so we can handle users dragging files onto colouring dialog. |
| `dropEvent( QDropEvent *ev)` | method | `void` | private | Reimplementation of drag/drop events so we can handle users dragging files onto colouring dialog. |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | Used for creating feature-age colour schemes. |
| `d_existing_globe_and_map_widget_ptr` | field | `GlobeAndMapWidget` | private | An existing GlobeAndMapWidget from which we'll clone our own GlobeAndMapWidget. |
| `d_read_error_accumulation_dialog_ptr` | field | `ReadErrorAccumulationDialog` | private | The dialog that shows file read errors. |
| `d_colour_scheme_container` | field | `GPlatesGui::ColourSchemeContainer` | private | Contains all loaded colour schemes, sorted by category. |
| `d_view_state_colour_scheme_delegator` | field | `GPlatesGui::ColourSchemeDelegator::non_null_ptr_type` | private | The colour scheme delegator in the ViewState used to control colouring in the main window. |
| `d_preview_colour_scheme` | field | `PreviewColourScheme::non_null_ptr_type` | private | The colour scheme used to control the colour of our previewing GlobeAndMapWidget. |
| `d_globe_and_map_widget_ptr` | field | `GlobeAndMapWidget` | private | The widget that does the rendering of the colour scheme previews. |
| `d_feature_store_root` | field | `GPlatesModel::FeatureStoreRootHandle::const_weak_ref` | private | A weak-ref to the feature store root, so we can find out about new feature collections. |
| `d_blank_icon` | field | `QIcon` | private | A blank icon for use as a placeholder icon. |
| `d_current_colour_scheme_category` | field | `GPlatesGui::ColourSchemeCategory::Type` | private | Stores the current colour scheme category displayed. |
| `d_next_icon_to_render` | field | `int` | private | Stores the index of the next icon in the colour schemes list to render, so that handle\_repaint() can keep track of where it got up to (it does one icon in one pass). |
| `d_show_thumbnails` | field | `bool` | private | If true, this dialog will show thumbnail previews of colour schemes. |
| `d_suppress_next_repaint` | field | `bool` | private | A hack to prevent unwanted refreshes from happening. |
| `d_current_feature_collection` | field | `GPlatesModel::FeatureCollectionHandle::const_weak_ref` | private | A weak reference to the feature collection for which we are currently viewing the colour scheme. |
| `d_last_single_colour` | field | `QColor` | private | The last colour added to the Single Colour category. |
| `d_open_regular_cpt_files_dialog` | field | `OpenFileDialog` | private | — |
| `d_open_categorical_cpt_files_dialog` | field | `OpenFileDialog` | private | — |
| `d_open_any_cpt_files_dialog` | field | `OpenFileDialog` | private | — |
| `ICON_SIZE` | field | `int` | private | The height and width of a preview icon. |
| `SPACING` | field | `int` | private | The space between items in the colour schemes list widget. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `NEW_FEATURE_COLLECTION` | variable | `QString` | — |
| `insert_separator( QComboBox *combobox)` | function | `void` | — |
| `remove_separator( QComboBox *combobox)` | function | `void` | — |
| `add_file_reference_to_combobox( const GPlatesAppLogic::FeatureCollectionFileState::file_reference &file_reference, QComboBox *combobox)` | function | `void` | — |
| `extract_colour_palette_pathnames_from_file_urls( const QList<QUrl> &urls)` | function | `QStringList` | Transforms a list of file:// urls into a list of pathnames in string form. |
| `OPEN_DIALOG_TITLE` | variable | `char` | — |
| `GPLATES_QTWIDGETS_COLOURINGDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ColouringDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Dialogs](../gui/Dialogs.md) | gui | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ColouringDialog` | `QDialog` | Manage Colouring | 16 |

**Qt signal/slot connections** (16 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `categories_table` | `currentCellChanged(int, int, int, int)` | `this` | `handle_categories_table_cell_changed(int, int, int, int)` |
| `close_button` | `clicked(bool)` | `this` | `handle_close_button_clicked(bool)` |
| `open_button` | `clicked(bool)` | `this` | `handle_open_button_clicked(bool)` |
| `add_button` | `clicked(bool)` | `this` | `handle_add_button_clicked(bool)` |
| `edit_button` | `clicked(bool)` | `this` | `edit_current_colour_scheme()` |
| `remove_button` | `clicked(bool)` | `this` | `handle_remove_button_clicked(bool)` |
| `d_existing_globe_and_map_widget_ptr` | `repainted(bool)` | `this` | `handle_main_repaint(bool)` |
| `d_globe_and_map_widget_ptr` | `repainted(bool)` | `this` | `handle_repaint(bool)` |
| `categories_table` | `currentCellChanged(int, int, int, int)` | `this` | `handle_categories_table_cell_changed(int, int, int, int)` |
| `colour_schemes_list` | `itemSelectionChanged()` | `this` | `handle_colour_schemes_list_selection_changed()` |
| `colour_schemes_list` | `itemDoubleClicked(QListWidgetItem *)` | `this` | `edit_current_colour_scheme()` |
| `show_thumbnails_checkbox` | `stateChanged(int)` | `this` | `handle_show_thumbnails_changed(int)` |
| `feature_collections_combobox` | `currentIndexChanged(int)` | `this` | `handle_feature_collections_combobox_index_changed(int)` |
| `use_global_checkbox` | `stateChanged(int)` | `this` | `handle_use_global_changed(int)` |
| `&d_application_state.get_feature_collection_file_state()` | `file_state_file_info_changed( GPlatesAppLogic::FeatureCollectionFileState &, GPlatesAppLogic::FeatureCollectionFileState::file_reference)` | `this` | `handle_file_info_changed( GPlatesAppLogic::FeatureCollectionFileState &, GPlatesAppLogic::FeatureCollectionFileState::file_reference)` |

*... and 1 more connections.*


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ColouringDialog.h
python scripts/gpq.py def GPlatesQtWidgets::ColouringDialog --body
python scripts/gpq.py uses ColouringDialog --kind class
python scripts/gpq.py hier ColouringDialog
```
