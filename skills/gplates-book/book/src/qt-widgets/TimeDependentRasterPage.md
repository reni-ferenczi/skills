# TimeDependentRasterPage

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 393 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/TimeDependentRasterPage.h` | C++ | 163 |
| `src/qt-widgets/TimeDependentRasterPage.cc` | C++ | 1173 |
| `src/qt-widgets/TimeDependentRasterPageUi.ui` | Qt form | 221 |

## Overview

A wizard page for assembling time-dependent raster sequences during import. It presents a table where users can add raster files from disk, assign or edit time values for each raster, and sort the sequence by time or filename. Time values can be deduced from filenames automatically, or entered manually. Drag-and-drop is supported for adding files. The page tracks whether the sequence is complete and validates time entries; it also supports toggling between short and full file paths for readability. It coordinates with a `TimeDependentRasterSequence` object to build the actual raster sequence, and with a callback function to notify the import workflow of the final band count.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::TimeLineEdit`](#anonymoustimelineedit) | class | [`FriendlyLineEdit`](FriendlyLineEdit.md) | — | 0 | — |
| [`(anonymous)::TimeDelegate`](#anonymoustimedelegate) | class | `QItemDelegate` | — | 0 | — |
| [`(anonymous)::TimeValidator`](#anonymoustimevalidator) | class | `QDoubleValidator` | — | 0 | — |
| [`(anonymous)::DeleteKeyEventFilter`](#anonymousdeletekeyeventfilter) | class | `QObject` | — | 0 | — |
| [`GPlatesQtWidgets::TimeDependentRasterPage`](#gplatesqtwidgetstimedependentrasterpage) | class | `QWizardPage`<br>`Ui_TimeDependentRasterPage` | — | 0 | — |

## Members

### `(anonymous)::TimeLineEdit`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `index_to_editor_map_type` | typedef | `GPlatesQtWidgets::TimeDependentRasterPage::index_to_editor_map_type` | public | — |
| `TimeLineEdit( const QString &contents, const QString &message_on_empty_string, QTableWidget *table, const boost::weak_ptr<index_to_editor_map_type> &index_to_editor_map, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~TimeLineEdit()` | destructor | `None` | public | — |
| `set_model_index( const QModelIndex &index)` | method | `void` | public | — |
| `erase_index_mapping()` | method | `void` | private | — |
| `focusInEvent( QFocusEvent *event_)` | method | `void` | protected | — |
| `handle_text_edited( const QString &text_)` | method | `void` | protected | — |
| `d_table` | field | `QTableWidget` | private | — |
| `d_model_index` | field | `QModelIndex` | private | — |
| `d_index_to_editor_map` | field | `boost::weak_ptr<index_to_editor_map_type>` | private | — |

### `(anonymous)::TimeDelegate`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `index_to_editor_map_type` | typedef | `GPlatesQtWidgets::TimeDependentRasterPage::index_to_editor_map_type` | public | — |
| `TimeDelegate( QValidator *validator, const boost::weak_ptr<index_to_editor_map_type> index_to_editor_map, QTableWidget *parent_)` | constructor | `None` | public | — |
| `createEditor( QWidget *parent_, const QStyleOptionViewItem &option, const QModelIndex &index)` | method | `QWidget` | public | — |
| `setEditorData( QWidget *editor, const QModelIndex &index)` | method | `void` | public | — |
| `setModelData( QWidget *editor, QAbstractItemModel *model, const QModelIndex &index)` | method | `void` | public | — |
| `d_validator` | field | `QValidator` | private | — |
| `d_index_to_editor_map` | field | `boost::weak_ptr<index_to_editor_map_type>` | private | — |
| `d_table` | field | `QTableWidget` | private | — |

### `(anonymous)::TimeValidator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TimeValidator( QObject *parent_)` | constructor | `None` | public | — |
| `validate( QString &input, int &pos)` | method | `State` | public | — |

### `(anonymous)::DeleteKeyEventFilter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DeleteKeyEventFilter( const boost::function<void ()> &remove_rows_function, QObject *parent_)` | constructor | `None` | public | — |
| `eventFilter( QObject *obj, QEvent *event_)` | method | `bool` | protected | — |
| `d_remove_rows_function` | field | `boost::function<void ()>` | private | — |

### `GPlatesQtWidgets::TimeDependentRasterPage`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `index_to_editor_map_type` | typedef | `std::map<QModelIndex, QWidget *>` | public | Assists with finding out which editor is editing which index. |
| `TimeDependentRasterPage( GPlatesPresentation::ViewState &view_state, unsigned int &raster_width, unsigned int &raster_height, TimeDependentRasterSequence &raster_sequence, const boost::function<void (unsigned int)> &set_number_of_bands_function, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `isComplete()` | method | `bool` | public | — |
| `dragEnterEvent( QDragEnterEvent *ev)` | method | `void` | protected | — |
| `dropEvent( QDropEvent *ev)` | method | `void` | protected | — |
| `handle_add_directory_button_clicked()` | method | `void` | private | — |
| `handle_add_files_button_clicked()` | method | `void` | private | — |
| `handle_remove_selected_button_clicked()` | method | `void` | private | — |
| `handle_sort_by_time_button_clicked()` | method | `void` | private | — |
| `handle_sort_by_file_name_button_clicked()` | method | `void` | private | — |
| `handle_show_full_paths_button_toggled( bool checked)` | method | `void` | private | — |
| `handle_table_selection_changed()` | method | `void` | private | — |
| `handle_table_cell_changed( int row, int column)` | method | `void` | private | — |
| `make_signal_slot_connections()` | method | `void` | private | — |
| `check_if_complete()` | method | `void` | private | — |
| `populate_table()` | method | `void` | private | — |
| `remove_selected_from_table()` | method | `void` | private | — |
| `add_files_to_sequence( QFileInfoList file_infos)` | method | `void` | private | — |
| `deduce_times( std::vector< boost::optional<double> > &times, const QFileInfoList &file_infos)` | method | `void` | private | — |
| `d_raster_width` | field | `unsigned int` | private | — |
| `d_raster_height` | field | `unsigned int` | private | — |
| `d_raster_sequence` | field | `TimeDependentRasterSequence` | private | — |
| `d_set_number_of_bands_function` | field | `boost::function<void (unsigned int)>` | private | — |
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
| `MINIMUM_TIME` | variable | `double` | — |
| `MAXIMUM_TIME` | variable | `double` | — |
| `DECIMAL_PLACES` | variable | `int` | — |
| `custom_round( double d)` | function | `double` | — |
| `round_to_dp( double d)` | function | `double` | — |
| `GPLATES_QTWIDGETS_TIMEDEPENDENTRASTERPAGE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ImportRasterDialog](ImportRasterDialog.md) | qt-widgets | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `TimeDependentRasterPage` | `QWizardPage` | WizardPage | 13 |

**Qt signal/slot connections** (8 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `add_directory_button` | `clicked()` | `this` | `handle_add_directory_button_clicked()` |
| `add_files_button` | `clicked()` | `this` | `handle_add_files_button_clicked()` |
| `remove_selected_button` | `clicked()` | `this` | `handle_remove_selected_button_clicked()` |
| `sort_by_time_button` | `clicked()` | `this` | `handle_sort_by_time_button_clicked()` |
| `sort_by_file_name_button` | `clicked()` | `this` | `handle_sort_by_file_name_button_clicked()` |
| `show_full_paths_button` | `toggled(bool)` | `this` | `handle_show_full_paths_button_toggled(bool)` |
| `files_table` | `itemSelectionChanged()` | `this` | `handle_table_selection_changed()` |
| `files_table` | `cellChanged(int, int)` | `this` | `handle_table_cell_changed(int, int)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/TimeDependentRasterPage.h
python scripts/gpq.py def GPlatesQtWidgets::TimeDependentRasterPage --body
python scripts/gpq.py uses TimeDependentRasterPage --kind class
python scripts/gpq.py hier TimeDependentRasterPage
```
