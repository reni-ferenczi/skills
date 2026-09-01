# ScalarField3DDepthLayersPage

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 106 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ScalarField3DDepthLayersPage.h` | C++ | 161 |
| `src/qt-widgets/ScalarField3DDepthLayersPage.cc` | C++ | 1159 |
| `src/qt-widgets/ScalarField3DDepthLayersPageUi.ui` | Qt form | 219 |

## Overview

[[[PROSE overview unit=qt-widgets/ScalarField3DDepthLayersPage tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::DepthLineEdit`](#anonymousdepthlineedit) | class | [`FriendlyLineEdit`](FriendlyLineEdit.md) | — | 0 | — |
| [`(anonymous)::DepthDelegate`](#anonymousdepthdelegate) | class | `QItemDelegate` | — | 0 | — |
| [`(anonymous)::DepthValidator`](#anonymousdepthvalidator) | class | `QDoubleValidator` | — | 0 | — |
| [`(anonymous)::DeleteKeyEventFilter`](#anonymousdeletekeyeventfilter) | class | `QObject` | — | 0 | — |
| [`GPlatesQtWidgets::ScalarField3DDepthLayersPage`](#gplatesqtwidgetsscalarfield3ddepthlayerspage) | class | `QWizardPage`<br>`Ui_ScalarField3DDepthLayersPage` | — | 0 | — |

## Members

### `(anonymous)::DepthLineEdit`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `index_to_editor_map_type` | typedef | `GPlatesQtWidgets::ScalarField3DDepthLayersPage::index_to_editor_map_type` | public | — |
| `DepthLineEdit( const QString &contents, const QString &message_on_empty_string, QTableWidget *table, const boost::weak_ptr<index_to_editor_map_type> &index_to_editor_map, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~DepthLineEdit()` | destructor | `None` | public | — |
| `set_model_index( const QModelIndex &index)` | method | `void` | public | — |
| `erase_index_mapping()` | method | `void` | private | — |
| `focusInEvent( QFocusEvent *event_)` | method | `void` | protected | — |
| `handle_text_edited( const QString &text_)` | method | `void` | protected | — |
| `d_table` | field | `QTableWidget` | private | — |
| `d_model_index` | field | `QModelIndex` | private | — |
| `d_index_to_editor_map` | field | `boost::weak_ptr<index_to_editor_map_type>` | private | — |

### `(anonymous)::DepthDelegate`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `index_to_editor_map_type` | typedef | `GPlatesQtWidgets::ScalarField3DDepthLayersPage::index_to_editor_map_type` | public | — |
| `DepthDelegate( QValidator *validator, const boost::weak_ptr<index_to_editor_map_type> index_to_editor_map, QTableWidget *parent_)` | constructor | `None` | public | — |
| `createEditor( QWidget *parent_, const QStyleOptionViewItem &option, const QModelIndex &index)` | method | `QWidget` | public | — |
| `setEditorData( QWidget *editor, const QModelIndex &index)` | method | `void` | public | — |
| `setModelData( QWidget *editor, QAbstractItemModel *model, const QModelIndex &index)` | method | `void` | public | — |
| `d_validator` | field | `QValidator` | private | — |
| `d_index_to_editor_map` | field | `boost::weak_ptr<index_to_editor_map_type>` | private | — |
| `d_table` | field | `QTableWidget` | private | — |

### `(anonymous)::DepthValidator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DepthValidator( QObject *parent_)` | constructor | `None` | public | — |
| `validate( QString &input, int &pos)` | method | `State` | public | — |

### `(anonymous)::DeleteKeyEventFilter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DeleteKeyEventFilter( const boost::function<void ()> &remove_rows_function, QObject *parent_)` | constructor | `None` | public | — |
| `eventFilter( QObject *obj, QEvent *event_)` | method | `bool` | protected | — |
| `d_remove_rows_function` | field | `boost::function<void ()>` | private | — |

### `GPlatesQtWidgets::ScalarField3DDepthLayersPage`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `index_to_editor_map_type` | typedef | `std::map<QModelIndex, QWidget *>` | public | Assists with finding out which editor is editing which index. |
| `ScalarField3DDepthLayersPage( GPlatesPresentation::ViewState &view_state, unsigned int &raster_width, unsigned int &raster_height, ScalarField3DDepthLayersSequence &depth_layers_sequence, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `isComplete()` | method | `bool` | public | — |
| `dragEnterEvent( QDragEnterEvent *ev)` | method | `void` | protected | — |
| `dropEvent( QDropEvent *ev)` | method | `void` | protected | — |
| `handle_add_directory_button_clicked()` | method | `void` | private | — |
| `handle_add_files_button_clicked()` | method | `void` | private | — |
| `handle_remove_selected_button_clicked()` | method | `void` | private | — |
| `handle_sort_by_depth_button_clicked()` | method | `void` | private | — |
| `handle_sort_by_file_name_button_clicked()` | method | `void` | private | — |
| `handle_show_full_paths_button_toggled( bool checked)` | method | `void` | private | — |
| `handle_table_selection_changed()` | method | `void` | private | — |
| `handle_table_cell_changed( int row, int column)` | method | `void` | private | — |
| `make_signal_slot_connections()` | method | `void` | private | — |
| `check_if_complete()` | method | `void` | private | — |
| `populate_table()` | method | `void` | private | — |
| `remove_selected_from_table()` | method | `void` | private | — |
| `add_files_to_sequence( QFileInfoList file_infos)` | method | `void` | private | — |
| `deduce_depths( std::vector< boost::optional<double> > &depths, const QFileInfoList &file_infos)` | method | `void` | private | — |
| `d_raster_width` | field | `unsigned int` | private | — |
| `d_raster_height` | field | `unsigned int` | private | — |
| `d_depth_layers_sequence` | field | `ScalarField3DDepthLayersSequence` | private | — |
| `d_validator` | field | `QValidator` | private | — |
| `d_is_complete` | field | `bool` | private | — |
| `d_show_full_paths` | field | `bool` | private | — |
| `d_index_to_editor_map` | field | `boost::shared_ptr<index_to_editor_map_type>` | private | — |
| `d_widget_to_focus` | field | `QWidget` | private | — |
| `d_open_directory_dialog` | field | `OpenDirectoryDialog` | private | — |
| `d_open_files_dialog` | field | `OpenFileDialog` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `MINIMUM_DEPTH` | variable | `double` | — |
| `MAXIMUM_DEPTH` | variable | `double` | — |
| `DECIMAL_PLACES` | variable | `int` | — |
| `custom_round( double d)` | function | `double` | — |
| `round_to_dp( double d)` | function | `double` | — |
| `GPLATES_QTWIDGETS_SCALARFIELD3DDEPTHLAYERSPAGE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ScalarField3DDepthLayersPage tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ImportScalarField3DDialog](ImportScalarField3DDialog.md) | qt-widgets | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ScalarField3DDepthLayersPage` | `QWizardPage` | WizardPage | 13 |

**Qt signal/slot connections** (8 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `add_directory_button` | `clicked()` | `this` | `handle_add_directory_button_clicked()` |
| `add_files_button` | `clicked()` | `this` | `handle_add_files_button_clicked()` |
| `remove_selected_button` | `clicked()` | `this` | `handle_remove_selected_button_clicked()` |
| `sort_by_depth_button` | `clicked()` | `this` | `handle_sort_by_depth_button_clicked()` |
| `sort_by_file_name_button` | `clicked()` | `this` | `handle_sort_by_file_name_button_clicked()` |
| `show_full_paths_button` | `toggled(bool)` | `this` | `handle_show_full_paths_button_toggled(bool)` |
| `files_table` | `itemSelectionChanged()` | `this` | `handle_table_selection_changed()` |
| `files_table` | `cellChanged(int, int)` | `this` | `handle_table_cell_changed(int, int)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ScalarField3DDepthLayersPage.h
python scripts/gpq.py def GPlatesQtWidgets::ScalarField3DDepthLayersPage --body
python scripts/gpq.py uses ScalarField3DDepthLayersPage --kind class
python scripts/gpq.py hier ScalarField3DDepthLayersPage
```
