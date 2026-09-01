# HellingerSegmentDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 294 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/HellingerSegmentDialog.h` | C++ | 216 |
| `src/qt-widgets/HellingerSegmentDialog.cc` | C++ | 759 |
| `src/qt-widgets/HellingerSegmentDialogUi.ui` | Qt form | 240 |

## Overview

Dialog for creating or editing a Hellinger segment with its constituent picks (measured points). The dialog displays the segment's picks in a table with columns for plate index, latitude, longitude, uncertainty, and enabled status. Users can add or remove picks, enable or disable individual picks, reset a pick to its default state, or change the plate index for all picks in the segment at once. The `SpinBoxDelegate` provides custom spinbox editing for numeric fields, adapting to whether 3-way fitting is enabled in the parent tool.

The dialog can operate in two modes: creating a new segment or editing an existing one. In create mode, users may encounter a `HellingerNewSegmentWarning` if the segment number already exists. The dialog tracks the currently selected pick and can be updated by globe interactions via `update_pick_coords()`. When the user finishes, it calls `add_segment_to_model()` to persist the segment to the underlying `HellingerModel`, then emits `finished_editing()` to notify the parent dialog.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::SpinBoxDelegate`](#gplatesqtwidgetsspinboxdelegate) | class | `QItemDelegate` | — | 0 | The SpinBoxDelegate class This lets us customise the spinbox behaviour in the TableView. |
| [`GPlatesQtWidgets::HellingerSegmentDialog`](#gplatesqtwidgetshellingersegmentdialog) | class | `QDialog`<br>`Ui_HellingerSegmentDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::SpinBoxDelegate`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SpinBoxDelegate( bool three_way_fitting_is_enabled, QObject *parent = 0)` | constructor | `None` | public | — |
| `createEditor( QWidget *parent, const QStyleOptionViewItem &option, const QModelIndex &index)` | method | `QWidget` | public | — |
| `setEditorData( QWidget *editor, const QModelIndex &index)` | method | `void` | public | — |
| `setModelData( QWidget *editor, QAbstractItemModel *model, const QModelIndex &index)` | method | `void` | public | — |
| `updateEditorGeometry( QWidget *editor, const QStyleOptionViewItem &option, const QModelIndex &index)` | method | `void` | public | — |
| `paint( QPainter *painter, const QStyleOptionViewItem &option, const QModelIndex &index)` | method | `void` | public | — |
| `d_three_way_fitting_is_enabled` | field | `bool` | private | — |

### `GPlatesQtWidgets::HellingerSegmentDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ColumnType` | enum | `None` | public | — |
| `HellingerSegmentDialog( HellingerDialog *hellinger_dialog, HellingerModel *hellinger_model, bool create_new_segment = false)` | constructor | `None` | public | — |
| `initialise_with_segment( const int &segment_number)` | method | `void` | public | — |
| `initialise()` | method | `void` | public | — |
| `current_pick()` | method | `boost::optional<GPlatesQtWidgets::HellingerPick>` | public | — |
| `update_pick_coords( const GPlatesMaths::LatLonPoint &llp)` | method | `void` | public | — |
| `begin_segment_operation()` | method | `void` | public | — |
| `finished_editing()` | method | `void` | public | — |
| `handle_selection_changed(const QItemSelection &, const QItemSelection &)` | method | `void` | private | — |
| `handle_add_segment()` | method | `void` | private | — |
| `handle_add_line()` | method | `void` | private | — |
| `handle_remove_line()` | method | `void` | private | — |
| `add_segment_to_model()` | method | `void` | private | — |
| `change_pick_type_of_whole_table()` | method | `void` | private | — |
| `update_buttons()` | method | `void` | private | — |
| `handle_reset()` | method | `void` | private | — |
| `handle_enable()` | method | `void` | private | — |
| `handle_disable()` | method | `void` | private | — |
| `close()` | method | `void` | private | — |
| `reject()` | method | `void` | private | — |
| `fill_widgets()` | method | `void` | private | — |
| `handle_edited_segment()` | method | `void` | private | — |
| `handle_new_segment()` | method | `void` | private | — |
| `set_initial_row_values(const int &row)` | method | `void` | private | — |
| `set_row_values(const int &row, const GPlatesQtWidgets::HellingerPick &pick)` | method | `void` | private | — |
| `d_hellinger_dialog_ptr` | field | `HellingerDialog` | private | — |
| `d_table_model` | field | `QStandardItemModel` | private | — |
| `d_hellinger_model_ptr` | field | `HellingerModel` | private | — |
| `d_hellinger_new_segment_warning` | field | `HellingerNewSegmentWarning` | private | — |
| `d_spin_box_delegate` | field | `SpinBoxDelegate` | private | — |
| `d_creating_new_segment` | field | `bool` | private | — |
| `d_original_segment_number` | field | `boost::optional<int>` | private | — |
| `d_current_pick` | field | `boost::optional<HellingerPick>` | private | — |
| `d_current_row` | field | `unsigned int` | private | — |
| `d_three_way_fitting_is_enabled` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `DEFAULT_UNCERTAINTY` | variable | `double` | DEFAULT\_UNCERTAINTY - initial uncertainty (km) to use in new picks. |
| `translate_segment_type( GPlatesQtWidgets::HellingerPlateIndex type)` | function | `QString` | translate\_segment\_type Convert MOVING/DISABLED\_MOVING types to a QString form of MOVING; similarly for FIXED/DISABLED\_FIXED. |
| `update_entire_row(QTableView *table, const QModelIndex &index)` | function | `void` | — |
| `GPLATES_QTWIDGETS_HELLINGERSEGMENTDIALOG_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/HellingerDialog](HellingerDialog.md) | qt-widgets | 6 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `HellingerSegmentDialog` | `QDialog` | New Segment | 17 |

**Qt signal/slot connections** (14 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_add_segment` | `clicked()` | `this` | `handle_add_segment()` |
| `button_add_line` | `clicked()` | `this` | `handle_add_line()` |
| `button_remove_line` | `clicked()` | `this` | `handle_remove_line()` |
| `radio_plate_index_1` | `clicked()` | `this` | `change_pick_type_of_whole_table()` |
| `radio_plate_index_2` | `clicked()` | `this` | `change_pick_type_of_whole_table()` |
| `radio_plate_index_3` | `clicked()` | `this` | `change_pick_type_of_whole_table()` |
| `radio_custom` | `clicked()` | `this` | `change_pick_type_of_whole_table()` |
| `button_reset` | `clicked()` | `this` | `handle_reset()` |
| `button_enable` | `clicked()` | `this` | `handle_enable()` |
| `button_disable` | `clicked()` | `this` | `handle_disable()` |
| `button_cancel` | `clicked()` | `this` | `close()` |
| `table_new_segment->verticalHeader()` | `sectionClicked(int)` | `this` | `update_buttons()` |
| `table_new_segment` | `clicked(QModelIndex)` | `this` | `update_buttons()` |
| `table_new_segment->selectionModel()` | `selectionChanged(QItemSelection,QItemSelection)` | `this` | `handle_selection_changed(QItemSelection,QItemSelection)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/HellingerSegmentDialog.h
python scripts/gpq.py def GPlatesQtWidgets::HellingerSegmentDialog --body
python scripts/gpq.py uses HellingerSegmentDialog --kind class
python scripts/gpq.py hier HellingerSegmentDialog
```
