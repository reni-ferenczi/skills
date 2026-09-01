# EditStringListWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 427 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditStringListWidget.h` | C++ | 207 |
| `src/qt-widgets/EditStringListWidget.cc` | C++ | 526 |
| `src/qt-widgets/EditStringListWidgetUi.ui` | Qt form | 199 |

## Overview

An editor widget for `GpmlStringList` property values (ordered sequences of strings). The widget displays the list in a two-column table: the first column holds editable string values, and the second column holds action buttons. Rows can be inserted above or below the current row, or deleted, via these action buttons. Alternatively, strings can be appended via a text-edit field with an "Append Element" button. The widget also inherits from `EditTableWidget`, which provides the table-editing framework and action-button management.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::ColumnLayout`](#anonymouscolumnlayout) | enum | — | — | 0 | — |
| [`GPlatesQtWidgets::EditStringListWidget`](#gplatesqtwidgetseditstringlistwidget) | class | [`AbstractEditWidget`](AbstractEditWidget.md)<br>[`EditTableWidget`](EditTableWidget.md)<br>`Ui_EditStringListWidget` | — | 0 | — |

## Members

### `(anonymous)::ColumnLayout`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `COLUMN_ELEMENT` | enumerator | `None` | — | — |
| `COLUMN_ACTION` | enumerator | `None` | — | — |

### `GPlatesQtWidgets::EditStringListWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EditStringListWidget( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `reset_widget_to_default_values()` | method | `void` | public | Clear the widget contents and any data structures. |
| `update_widget_from_string_list( GPlatesPropertyValues::GpmlStringList &gpml_string_list)` | method | `void` | public | Update the widget contents from gpml\_string\_list. |
| `create_property_value_from_widget()` | method | `GPlatesModel::PropertyValue::non_null_ptr_type` | public | Create a new instance of a property-value derivation, based upon the widget contents. |
| `update_property_value_from_widget()` | method | `bool` | public | Update the property-value instance from which this widget was populated, with the values currently in this widget. |
| `handle_insert_row_above( const EditTableActionWidget *action_widget)` | method | `void` | public | — |
| `handle_insert_row_below( const EditTableActionWidget *action_widget)` | method | `void` | public | — |
| `handle_delete_row( const EditTableActionWidget *action_widget)` | method | `void` | public | — |
| `append_string_element( const QString &str)` | method | `void` | public | Append a new string element to the table. |
| `handle_cell_changed( int row, int column)` | method | `void` | private | Handle a change to the data contained in a cell. |
| `handle_append_element_button_clicked()` | method | `void` | private | — |
| `handle_current_cell_changed( int currentRow, int currentColumn, int previousRow, int previousColumn)` | method | `void` | private | Handle a change to which cell has the focus. |
| `handle_cell_activated(int row, int column)` | method | `void` | private | Handle when a cell is activated. |
| `get_row_for_action_widget( const EditTableActionWidget *action_widget)` | method | `int` | private | Finds the current table row associated with the EditTableActionWidget. |
| `insert_empty_string_element_into_table( int row)` | method | `void` | private | Insert a new empty string to the table. |
| `delete_row( int row)` | method | `void` | private | Removes a single row from the table. |
| `commit_changes()` | method | `void` | private | Commit changes, by emitting the commit signal. |
| `d_string_list_ptr` | field | `boost::intrusive_ptr<GPlatesPropertyValues::GpmlStringList>` | private | This boost::intrusive\_ptr is used to remember the property value which was last loaded into this editing widget. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_action_widget_for_row( QTableWidget &table, int row)` | function | `GPlatesQtWidgets::EditTableActionWidget` | Fetches the appropriate action widget given a row number. |
| `ensure_table_size( QTableWidget &table, int rows)` | function | `int` | Uses rowCount() and setRowCount() to ensure the table has at least rows rows available. |
| `append_string_to_table( QTableWidget &table, const QString &str)` | function | `void` | Append the string str to table. |
| `populate_table_row_with_empty_string_element( GPlatesQtWidgets::EditStringListWidget &string_list_widget, QTableWidget &table, int which_row)` | function | `void` | Insert an empty string element at already-inserted row which\_row of table. |
| `work_around_table_graphical_glitch( GPlatesQtWidgets::EditStringListWidget &edit_string_list_widget, QTableWidget &table)` | function | `void` | Work around a graphical glitch, where the EditTableActionWidgets around the recently scrolled-to row appear to be misaligned. |
| `get_element_string( QTableWidget &table_widget, int row)` | function | `boost::optional<QString>` | — |
| `populate_element_vector_from_table( std::vector<GPlatesPropertyValues::TextContent> &elements, QTableWidget &table_elements)` | function | `void` | — |
| `GPLATES_QTWIDGETS_EDITSTRINGLIST_H` | macro | `None` | — |

## Notes

Calling `update_property_value_from_widget()` before loading a list with `update_widget_from_string_list()` throws `UninitialisedEditWidgetException`. Empty strings are valid list elements and are preserved. The widget listens to the `cellActivated` signal (not `cellChanged`) to detect edits; `cellChanged` fires during table population, so a different signal is used to distinguish user edits from programmatic updates.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/EditWidgetGroupBox](EditWidgetGroupBox.md) | qt-widgets | 3 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `EditStringListWidget` | `QWidget` | Form | 5 |

**Qt signal/slot connections** (4 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_append_element` | `clicked()` | `this` | `handle_append_element_button_clicked()` |
| `table_elements` | `cellActivated(int, int)` | `this` | `handle_cell_changed(int, int)` |
| `table_elements` | `cellChanged(int, int)` | `this` | `handle_cell_changed(int, int)` |
| `table_elements` | `currentCellChanged(int,int,int,int)` | `this` | `handle_current_cell_changed(int,int,int,int)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/EditStringListWidget.h
python scripts/gpq.py def GPlatesQtWidgets::EditStringListWidget --body
python scripts/gpq.py uses EditStringListWidget --kind class
python scripts/gpq.py hier EditStringListWidget
```
