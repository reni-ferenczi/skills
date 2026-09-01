# EditTotalReconstructionSequenceWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 369 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditTotalReconstructionSequenceWidget.h` | C++ | 244 |
| `src/qt-widgets/EditTotalReconstructionSequenceWidget.cc` | C++ | 1050 |
| `src/qt-widgets/EditTotalReconstructionSequenceWidgetUi.ui` | Qt form | 326 |

## Overview

[[[PROSE overview unit=qt-widgets/EditTotalReconstructionSequenceWidget tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`ColumnNames::ColumnName`](#columnnamescolumnname) | enum | — | — | 0 | — |
| [`(anonymous)::TableUpdateGuard`](#anonymoustableupdateguard) | struct | `boost::noncopyable` | — | 0 | Borrowed from the TopologySectionsTable. |
| [`GPlatesQtWidgets::EditPoleActionWidget`](#gplatesqtwidgetseditpoleactionwidget) | class | [`EditTableActionWidget`](EditTableActionWidget.md) | — | 0 | — |
| [`GPlatesQtWidgets::EditTotalReconstructionSequenceWidget`](#gplatesqtwidgetsedittotalreconstructionsequencewidget) | class | `QWidget`<br>[`EditTableWidget`](EditTableWidget.md)<br>`Ui_EditTotalReconstructionSequenceWidget` | — | 0 | This widget displays, and allows editing of, the irregular sampling property of a TotalReconstructionSequence feature. |

## Members

### `ColumnNames::ColumnName`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TIME` | enumerator | `None` | — | — |
| `LATITUDE` | enumerator | `None` | — | — |
| `LONGITUDE` | enumerator | `None` | — | — |
| `ANGLE` | enumerator | `None` | — | — |
| `COMMENT` | enumerator | `None` | — | — |
| `ACTIONS` | enumerator | `None` | — | — |
| `NUMCOLS` | enumerator | `None` | — | — |

### `(anonymous)::TableUpdateGuard`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TableUpdateGuard( bool &guard_flag_ref)` | constructor | `None` | public | — |
| `~TableUpdateGuard()` | destructor | `None` | public | — |
| `d_guard_flag_ptr` | field | `bool` | public | — |

### `GPlatesQtWidgets::EditPoleActionWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EditPoleActionWidget( EditTableWidget *table_widget, bool enable_is_on = true, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `set_enable_flag( bool flag)` | method | `void` | public | — |
| `refresh_buttons()` | method | `void` | protected | — |
| `enable_pole()` | method | `void` | private | — |
| `disable_pole()` | method | `void` | private | — |
| `disable_button` | field | `QPushButton` | private | — |
| `enable_button` | field | `QPushButton` | private | — |
| `d_enable_is_on` | field | `bool` | private | — |

### `GPlatesQtWidgets::EditTotalReconstructionSequenceWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EditTotalReconstructionSequenceWidget( QWidget *parent = 0)` | constructor | `None` | public | — |
| `update_table_widget_from_property( GPlatesPropertyValues::GpmlIrregularSampling::non_null_ptr_type irregular_sampling)` | method | `void` | public | Fill table with data from TRS feature. |
| `get_irregular_sampling_property_value_from_table_widget()` | method | `GPlatesModel::TopLevelProperty::non_null_ptr_type` | public | — |
| `moving_plate_id()` | method | `GPlatesModel::integer_plate_id_type` | public | — |
| `fixed_plate_id()` | method | `GPlatesModel::integer_plate_id_type` | public | — |
| `set_moving_plate_id( const GPlatesModel::integer_plate_id_type &moving_plate_id)` | method | `void` | public | — |
| `set_fixed_plate_id( const GPlatesModel::integer_plate_id_type &fixed_plate_id)` | method | `void` | public | — |
| `sort_table_by_time()` | method | `void` | public | — |
| `validate()` | method | `bool` | public | Validate the table of sequences. |
| `initialise()` | method | `void` | public | Set up an "empty" widget - but with an initial (zero-valued) row entry. |
| `set_action_widget_in_row( int row)` | method | `void` | public | — |
| `handle_disable_pole( EditPoleActionWidget*, bool)` | method | `void` | public | — |
| `table_validity_changed( bool)` | method | `void` | public | — |
| `plate_ids_have_changed()` | method | `void` | public | — |
| `make_irregular_sampling_from_table()` | method | `GPlatesModel::TopLevelProperty::non_null_ptr_type` | protected | Creates an irregular sampling property from the values in table. |
| `handle_insert_row_above( const EditTableActionWidget *)` | method | `void` | private | — |
| `handle_insert_row_below( const EditTableActionWidget *)` | method | `void` | private | — |
| `handle_delete_row( const EditTableActionWidget *)` | method | `void` | private | — |
| `handle_insert_new_pole()` | method | `void` | private | — |
| `handle_item_changed( QTableWidgetItem* item)` | method | `void` | private | — |
| `handle_current_cell_changed( int,int,int,int)` | method | `void` | private | — |
| `handle_editing_finished()` | method | `void` | private | Handle the editFinished() signal from the spinbox in the active cell. |
| `handle_plate_ids_changed()` | method | `void` | private | — |
| `get_row_for_action_widget( const EditTableActionWidget *)` | method | `int` | private | — |
| `insert_blank_row( int row)` | method | `void` | private | — |
| `delete_row( int row)` | method | `void` | private | — |
| `d_suppress_update_notification_guard` | field | `bool` | private | Borrowed from TopologySectionsTable - used to prevent update and related methods from triggering the itemChanged signal. |
| `d_spinbox_row` | field | `int` | private | The row and column at which the spinbox is located. |
| `d_spinbox_column` | field | `int` | private | — |
| `d_moving_plate_changed` | field | `bool` | private | — |
| `d_fixed_plate_changed` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `fill_table_with_comment( QTableWidget *table, unsigned int row_count, const QString &comment)` | function | `void` | — |
| `fill_table_with_finite_rotation( QTableWidget *table, unsigned int row_count, const GPlatesPropertyValues::GpmlFiniteRotation &finite_rotation, const QLocale &locale_)` | function | `void` | — |
| `fill_table_with_pole( QTableWidget *table, unsigned int row_count, const GPlatesModel::PropertyValue::non_null_ptr_to_const_type &time_sample_value, const QLocale &locale_)` | function | `void` | — |
| `fill_table_with_time_instant( QTableWidget *table, unsigned int row_count, const GPlatesPropertyValues::GeoTimeInstant &geo_time_instant, const QLocale &locale_)` | function | `void` | — |
| `insert_table_row( QTableWidget *table, unsigned int row_count, const GPlatesPropertyValues::GpmlTimeSample &time_sample, const QLocale &locale_)` | function | `void` | Fill row row\_count in the QTableWidget table with the time,lat,lon,angle and comment from the GpmlTimeSample time\_sample. |
| `set_spinbox_properties( QDoubleSpinBox *spinbox, int column)` | function | `void` | Set appropriate limits for the spinbox according to its column - e.g. -90 to 90 for latitude. |
| `update_table_from_last_active_cell( QTableWidget *table)` | function | `void` | Commit any spinbox widget value from the most recently spinbox-ified cell to the table. |
| `fill_row_with_defaults( QTableWidget *table, int row)` | function | `void` | — |
| `table_times_are_valid( QTableWidget *table, QString& msg)` | function | `bool` | Returns true if the time values (i.e. values in ColumnNames::Time of table): 1) are not empty AND 2) do not contain duplicate times. |
| `set_indeterminate_fields_for_row( QTableWidget *table, int row)` | function | `void` | Changes any of the lat/lon fields in row row to "indet" if their corresponding angle field is zero. |
| `set_indeterminate_fields_for_table( QTableWidget *table)` | function | `void` | Changes any of the lat/lon fields in table to "indet" if their corresponding angle fields are zero. |
| `GPLATES_QTWIDGETS_EDITTOTALRECONSTRUCTIONSEQUENCEWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/EditTotalReconstructionSequenceWidget tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/EditTotalReconstructionSequenceDialog](EditTotalReconstructionSequenceDialog.md) | qt-widgets | 9 |
| [qt-widgets/CreateTotalReconstructionSequenceDialog](CreateTotalReconstructionSequenceDialog.md) | qt-widgets | 5 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `EditTotalReconstructionSequenceWidget` | `QWidget` | Form | 19 |

**Qt signal/slot connections** (8 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `enable_button` | `clicked()` | `this` | `enable_pole()` |
| `disable_button` | `clicked()` | `this` | `disable_pole()` |
| `table_sequences` | `itemChanged(QTableWidgetItem*)` | `this` | `handle_item_changed(QTableWidgetItem*)` |
| `button_insert` | `pressed()` | `this` | `handle_insert_new_pole()` |
| `table_sequences` | `currentCellChanged(int,int,int,int)` | `this` | `handle_current_cell_changed(int,int,int,int)` |
| `spinbox_moving` | `valueChanged(int)` | `this` | `handle_plate_ids_changed()` |
| `spinbox_fixed` | `valueChanged(int)` | `this` | `handle_plate_ids_changed()` |
| `spinbox` | `editingFinished()` | `this` | `handle_editing_finished()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/EditTotalReconstructionSequenceWidget.h
python scripts/gpq.py def GPlatesQtWidgets::EditTotalReconstructionSequenceWidget --body
python scripts/gpq.py uses EditTotalReconstructionSequenceWidget --kind class
python scripts/gpq.py hier EditTotalReconstructionSequenceWidget
```
