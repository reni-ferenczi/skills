# EditTimeSequenceWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 268 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditTimeSequenceWidget.h` | C++ | 286 |
| `src/qt-widgets/EditTimeSequenceWidget.cc` | C++ | 952 |
| `src/qt-widgets/EditTimeSequenceWidgetUi.ui` | Qt form | 429 |

## Overview

An editor widget for `GpmlArray` property values containing time periods, displayed and edited as a flat sequence of time samples. The widget presents times in a table with spinbox-editable cells and action buttons for row insertion and deletion. Times can be added singly via a spinbox and button, or in batches via a range-fill interface (from/to/step values). When committing, the widget automatically sorts times, removes duplicates, and converts the flat list back into the structured `GpmlArray` of `GmlTimePeriod` objects. A custom spinbox delegate (`EditTimeSequenceSpinBoxDelegate`) renders and validates the time column. The widget monitors the current reconstruction time and provides buttons to populate fields from it.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::ColumnLayout`](#anonymouscolumnlayout) | enum | — | — | 0 | — |
| [`GPlatesQtWidgets::EditTimeSequenceSpinBoxDelegate`](#gplatesqtwidgetsedittimesequencespinboxdelegate) | class | `QItemDelegate` | — | 0 | The SpinBoxDelegate class This lets us customise the spinbox behaviour in the TableView. |
| [`GPlatesQtWidgets::EditTimeSequenceWidget`](#gplatesqtwidgetsedittimesequencewidget) | class | [`AbstractEditWidget`](AbstractEditWidget.md)<br>[`EditTableWidget`](EditTableWidget.md)<br>`Ui_EditTimeSequenceWidget` | — | 0 | — |

## Members

### `(anonymous)::ColumnLayout`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `COLUMN_TIME` | enumerator | `None` | — | — |
| `COLUMN_ACTION` | enumerator | `None` | — | — |

### `GPlatesQtWidgets::EditTimeSequenceSpinBoxDelegate`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `editing_finished()` | method | `void` | public | — |
| `EditTimeSequenceSpinBoxDelegate(QObject *parent = 0)` | constructor | `None` | public | — |
| `createEditor( QWidget *parent, const QStyleOptionViewItem &option, const QModelIndex &index)` | method | `QWidget` | public | — |
| `setEditorData( QWidget *editor, const QModelIndex &index)` | method | `void` | public | — |
| `setModelData( QWidget *editor, QAbstractItemModel *model, const QModelIndex &index)` | method | `void` | public | — |
| `updateEditorGeometry( QWidget *editor, const QStyleOptionViewItem &option, const QModelIndex &index)` | method | `void` | public | — |
| `paint( QPainter *painter, const QStyleOptionViewItem &option, const QModelIndex &index)` | method | `void` | public | — |

### `GPlatesQtWidgets::EditTimeSequenceWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EditTimeSequenceWidget( GPlatesAppLogic::ApplicationState &app_state_, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `reset_widget_to_default_values()` | method | `void` | public | — |
| `update_widget_from_time_period_array( GPlatesPropertyValues::GpmlArray &gpml_array)` | method | `void` | public | gpml\_array must have a value type of 'gml:TimePeriod'. |
| `create_property_value_from_widget()` | method | `GPlatesModel::PropertyValue::non_null_ptr_type` | public | — |
| `update_property_value_from_widget()` | method | `bool` | public | — |
| `handle_insert_row_above( const EditTableActionWidget *action_widget)` | method | `void` | public | — |
| `handle_insert_row_below( const EditTableActionWidget *action_widget)` | method | `void` | public | — |
| `handle_delete_row( const EditTableActionWidget *action_widget)` | method | `void` | public | — |
| `insert_single( double time)` | method | `void` | public | Adds a new time to the table. |
| `insert_multiple()` | method | `void` | public | Fill the table with values determined by the "Fill with times" group box. |
| `handle_spinbox_editing_finished()` | method | `void` | private | — |
| `handle_remove_all()` | method | `void` | private | — |
| `handle_remove()` | method | `void` | private | — |
| `handle_insert_single()` | method | `void` | private | — |
| `handle_insert_multiple()` | method | `void` | private | — |
| `handle_current_cell_changed( int currentRow, int currentColumn, int previousRow, int previousColumn)` | method | `void` | private | Creates an EditTableActionWidget item in the current row. |
| `handle_use_main_single()` | method | `void` | private | Use main window time for the insert-single-time time-value |
| `handle_use_main_from()` | method | `void` | private | Use main window time for the insert-multiple-times from-value |
| `handle_use_main_to()` | method | `void` | private | Use main window time for the insert-multiple-times to-value |
| `handle_single_time_entered()` | method | `void` | private | Listen for the time spinbox having had a value entered. |
| `get_row_for_action_widget( const EditTableActionWidget *action_widget)` | method | `int` | private | Finds the current table row associated with the EditTableActionWidget. |
| `insert_blank_time_into_table( int row)` | method | `void` | private | Adds a new blank point to the current geometry in the table. |
| `delete_time_from_table( int row)` | method | `void` | private | Removes a single point from the current geometry in the table. |
| `sort_and_commit()` | method | `void` | private | Sorts the table, removes duplicates, and emits commit signal. |
| `update_time_array_from_widget()` | method | `void` | private | Updates the time samples in the GpmlIrregularSampling. |
| `update_buttons()` | method | `void` | private | — |
| `setup_connections()` | method | `void` | private | — |
| `d_array_ptr` | field | `boost::intrusive_ptr<GPlatesPropertyValues::GpmlArray>` | private | This boost::intrusive\_ptr is used to remember the property value which was last loaded into this editing widget. |
| `d_current_reconstruction_time` | field | `double` | private | — |
| `d_spin_box_delegate` | field | `EditTimeSequenceSpinBoxDelegate` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `DEMAND_ZERO_TIME_VALUE_IN_TABLE` | variable | `bool` | TODO: check control flow so that sorting/removing-duplicates isn't happening multiple times. |
| `row_contains_zero(int row, QTableWidget *table)` | function | `bool` | — |
| `get_action_widget_for_row( QTableWidget &table, int row)` | function | `GPlatesQtWidgets::EditTableActionWidget` | Fetches the appropriate action widget given a row number. |
| `attempt_to_populate_table_row_from_time( GPlatesQtWidgets::EditTimeSequenceWidget &time_sequence_widget, QTableWidget &table, double time)` | function | `bool` | Allocates QTableWidgetItems and populates a QTableWidget from a time. |
| `populate_table_row_with_blank_time( GPlatesQtWidgets::EditTimeSequenceWidget &time_sequence_widget, QTableWidget &table, int row)` | function | `void` | Allocates QTableWidgetItems and populates a QTableWidget from a GPlatesMaths::PointOnSphere. |
| `work_around_table_graphical_glitch( GPlatesQtWidgets::EditTimeSequenceWidget &edit_time_sequence_widget, QTableWidget &table)` | function | `void` | Work around a graphical glitch, where the EditTableActionWidgets around the recently scrolled-to row appear to be misaligned. |
| `get_valid_time( QTableWidget &table_widget, int row)` | function | `boost::optional<double>` | — |
| `remove_row( int row, QTableWidget *table_widget)` | function | `void` | — |
| `remove_rows( QTableWidget *table_widget)` | function | `void` | This removes contiguous rows from a QTableWidget specified by the the table widget's selectedRanges() function. |
| `sort_and_remove_duplicates_from_table( QTableWidget *table)` | function | `void` | — |
| `GPLATES_QTWIDGETS_EDITTIMESEQUENCE_H` | macro | `None` | — |

## Notes

Calling `update_property_value_from_widget()` before loading a time period array with `update_widget_from_time_period_array()` throws `UninitialisedEditWidgetException`. Creating a property value requires at least two time samples (one complete period); an exception is thrown if fewer than two valid times are in the table. Negative time values are silently rejected when inserting. The table is pre-populated with time 0.0 on reset (configurable by DEMAND_ZERO_TIME_VALUE_IN_TABLE). Time duplication and sorting are handled automatically during commit; neither sorting nor duplicate removal is performed when edits are made.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/EditWidgetGroupBox](EditWidgetGroupBox.md) | qt-widgets | 3 |
| [app-logic/ReconstructMethodByPlateId](../app-logic/ReconstructMethodByPlateId.md) | app-logic | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `EditTimeSequenceWidget` | `QWidget` | Form | 23 |

**Qt signal/slot connections** (9 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_insert_single` | `clicked()` | `this` | `handle_insert_single()` |
| `button_remove_all` | `clicked()` | `this` | `handle_remove_all()` |
| `button_remove` | `clicked()` | `this` | `handle_remove()` |
| `button_insert_multiple` | `clicked()` | `this` | `handle_insert_multiple()` |
| `table_times` | `currentCellChanged(int,int,int,int)` | `this` | `handle_current_cell_changed(int,int,int,int)` |
| `button_use_main_single` | `clicked()` | `this` | `handle_use_main_single()` |
| `button_use_main_from` | `clicked()` | `this` | `handle_use_main_from()` |
| `button_use_main_to` | `clicked()` | `this` | `handle_use_main_to()` |
| `d_spin_box_delegate` | `editing_finished()` | `this` | `handle_spinbox_editing_finished()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/EditTimeSequenceWidget.h
python scripts/gpq.py def GPlatesQtWidgets::EditTimeSequenceWidget --body
python scripts/gpq.py uses EditTimeSequenceWidget --kind class
python scripts/gpq.py hier EditTimeSequenceWidget
```
