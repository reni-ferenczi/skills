# TopologySectionsTable

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 21 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/TopologySectionsTable.h` | C++ | 375 |
| `src/gui/TopologySectionsTable.cc` | C++ | 990 |

## Overview

[[[PROSE overview unit=gui/TopologySectionsTable tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::TableUpdateGuard`](#anonymoustableupdateguard) | struct | `boost::noncopyable` | — | 0 | Tiny convenience class to help suppress the QTableWidget::cellChanged() notification in situations where we are updating the table data programatically. |
| [`GPlatesGui::TopologySectionsTable`](#gplatesguitopologysectionstable) | class | `QObject` | — | 0 | Class to manage a QTableWidget plus the items within, to display the sections of topology the user is currently building up via the plate polygon tool. |

## Members

### `(anonymous)::TableUpdateGuard`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TableUpdateGuard( bool &guard_flag_ref)` | constructor | `None` | public | — |
| `~TableUpdateGuard()` | destructor | `None` | public | — |
| `d_guard_flag_ptr` | field | `bool` | public | — |

### `GPlatesGui::TopologySectionsTable`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TopologySectionsTable( QTableWidget &table, TopologySectionsContainer &boundary_container, TopologySectionsContainer &interior_container, GPlatesPresentation::ViewState &view_state)` | constructor | `None` | public | — |
| `~TopologySectionsTable()` | destructor | `None` | public | — |
| `update_table()` | method | `void` | public | Updates the table rows from the data vector. |
| `focus_feature_at_row( int row)` | method | `void` | public | — |
| `react_focus_feature_at_index( GPlatesGui::TopologySectionsContainer::size_type index)` | method | `void` | public | — |
| `react_container_change(GPlatesGui::TopologySectionsContainer*)` | method | `void` | public | — |
| `react_cell_entered( int row, int col)` | method | `void` | private | — |
| `react_cell_clicked( int row, int col)` | method | `void` | private | — |
| `react_cell_changed( int row, int col)` | method | `void` | private | — |
| `react_remove_clicked()` | method | `void` | private | — |
| `react_insert_above_clicked()` | method | `void` | private | — |
| `react_insert_below_clicked()` | method | `void` | private | — |
| `react_cancel_insertion_point_clicked()` | method | `void` | private | — |
| `clear_table()` | method | `void` | private | Removes and deletes QTableWidgetItems from the table. |
| `topology_section_modified( GPlatesGui::TopologySectionsContainer::size_type topology_sections_container_index)` | method | `void` | private | A table row in the topology sections container was modified. |
| `get_current_action_box_row()` | method | `int` | private | Returns the current table row associated with the ActionButtonBox. |
| `move_action_box( int row)` | method | `void` | private | — |
| `remove_action_box()` | method | `void` | private | — |
| `set_action_box_widget( int row)` | method | `void` | private | — |
| `get_current_insertion_point_row()` | method | `int` | private | Returns the visual row associated with the Insertion Point. |
| `set_insertion_point_widget( int row)` | method | `void` | private | — |
| `remove_insertion_point_widget( int row)` | method | `void` | private | — |
| `convert_data_index_to_table_row( TopologySectionsContainer::size_type index)` | method | `int` | private | Convert between items of data in the vector and rows on the QTableWidget, accounting for the presence of an 'insertion point' row. |
| `convert_table_row_to_data_index( int row)` | method | `TopologySectionsContainer::size_type` | private | Convert between items of data in the vector and rows on the QTableWidget, accounting for the presence of an 'insertion point' row. |
| `set_up_actions()` | method | `void` | private | Configures and connects up our QActions. |
| `set_up_connections_to_container(TopologySectionsContainer *ptr)` | method | `void` | private | Configures and connects up our QActions. |
| `create_new_action_box()` | method | `GPlatesQtWidgets::ActionButtonBox` | private | Assigns our custom actions to a newly created ActionButtonBox, and returns said box. |
| `set_up_table()` | method | `void` | private | Sets columns and other properties of the QTableWidget. |
| `update_table_row_count()` | method | `void` | private | Updates the number of visual rows in the table. |
| `update_table_row( int row)` | method | `void` | private | Updates data in table cells for one visual row. |
| `render_valid_row( int row, const TopologySectionsContainer::TableRow &row_data, QColor bg = Qt::white)` | method | `void` | private | Updates data in table cells for one visual row so that it matches the given TableRow struct. |
| `render_insertion_point_row( int row)` | method | `void` | private | Updates data in table cells for one visual row to draw the special 'insertion point' row. |
| `render_invalid_row( int row, QString reason)` | method | `void` | private | Updates data in table cells for one visual row so that it displays a warning about the data for this row being invalid. |
| `update_data_from_table( int row)` | method | `void` | private | The inverse of update\_table\_row(); Called after the user has edited the table, it checks each column of the given row to see if a suitable function is defined, and calls it to convert the QTableWidgetItem cell back into the back-end data. |
| `install_table_widget_item( int row, int column, const TopologySectionsContainer::TableRow &row_data, QColor bg)` | method | `void` | private | Install a QTableWidgetItem for the cell at row and column. |
| `install_edit_cell_widget( int row, int column)` | method | `void` | private | Create and install a widget to edit the cell at row and column (as opposed to using a QTableWidgetItem). |
| `remove_cell( int row, int column)` | method | `void` | private | Removes cell (either widget or QTableWidgetItem) at row and column. |
| `remove_cells( int row)` | method | `void` | private | Removes all cells in row. |
| `reset_row( int row)` | method | `void` | private | Reset row to the default state so we can render a new row. |
| `d_table` | field | `QPointer<QTableWidget>` | private | The QTableWidget we are managing. |
| `d_container_ptr` | field | `TopologySectionsContainer` | private | The underlying data. |
| `d_boundary_container_ptr` | field | `TopologySectionsContainer` | private | — |
| `d_interior_container_ptr` | field | `TopologySectionsContainer` | private | — |
| `d_column_heading_infos` | field | `std::vector<TopologySectionsTableColumns::ColumnHeadingInfo>` | private | Column information for setting up the table columns and converting data to/from the topology sections container. |
| `d_action_box_row` | field | `int` | private | The row that the ActionButtonBox we display is in. |
| `d_remove_action` | field | `QAction` | private | Remove Action. |
| `d_insert_above_action` | field | `QAction` | private | Insert Above Action. |
| `d_insert_below_action` | field | `QAction` | private | Insert Below Action. |
| `d_cancel_insertion_point_action` | field | `QAction` | private | Cancel Insertion Point Action. |
| `d_suppress_update_notification_guard` | field | `bool` | private | This flag is set by instantiating a TableUpdateGuard (in the .cc file) at any scope where we are directly modifying table cells programmatically. |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | Application state used to retrieve the current reconstruction. |
| `d_feature_focus_ptr` | field | `FeatureFocus` | private | Feature focus, so that the user can click on entries in the table and adjust the focus from there. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `is_row_prev_neighbor_of_insert( int r, int i, int table_count )` | function | `bool` | — |
| `is_row_next_neighbor_of_insert( int r, int i, int table_count )` | function | `bool` | — |
| `check_row_validity( const GPlatesGui::TopologySectionsContainer::TableRow &entry)` | function | `bool` | — |
| `check_row_validity_geom( const GPlatesGui::TopologySectionsContainer::TableRow &entry)` | function | `bool` | — |
| `check_row_validity_reconstructed_geometry( const GPlatesGui::TopologySectionsContainer::TableRow &entry, const GPlatesAppLogic::Reconstruction &reconstruction)` | function | `bool` | — |
| `get_invalid_row_message( const GPlatesGui::TopologySectionsContainer::TableRow &entry)` | function | `QString` | — |
| `GPLATES_GUI_TOPOLOGYSECTIONSTABLE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/TopologySectionsTable tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/SearchResultsDockWidget](../qt-widgets/SearchResultsDockWidget.md) | qt-widgets | 2 |

## Related

**Qt signal/slot connections** (15 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_table` | `cellEntered(int, int)` | `this` | `react_cell_entered(int, int)` |
| `d_table` | `cellChanged(int, int)` | `this` | `react_cell_changed(int, int)` |
| `d_table` | `cellClicked(int, int)` | `this` | `react_cell_clicked(int, int)` |
| `container_ptr` | `do_update()` | `this` | `update_table()` |
| `container_ptr` | `cleared()` | `this` | `clear_table()` |
| `container_ptr` | `insertion_point_moved(GPlatesGui::TopologySectionsContainer::size_type)` | `this` | `update_table()` |
| `container_ptr` | `entry_removed(GPlatesGui::TopologySectionsContainer::size_type)` | `this` | `update_table()` |
| `container_ptr` | `entries_inserted( GPlatesGui::TopologySectionsContainer::size_type, GPlatesGui::TopologySectionsContainer::size_type, GPlatesGui::TopologySectionsContainer::const_iterator, GPlatesGui::TopologySection` | `this` | `update_table()` |
| `container_ptr` | `entry_modified(GPlatesGui::TopologySectionsContainer::size_type)` | `this` | `topology_section_modified(GPlatesGui::TopologySectionsContainer::size_type)` |
| `container_ptr` | `focus_feature_at_index( GPlatesGui::TopologySectionsContainer::size_type)` | `this` | `react_focus_feature_at_index(GPlatesGui::TopologySectionsContainer::size_type)` |
| `container_ptr` | `container_change(GPlatesGui::TopologySectionsContainer *)` | `this` | `react_container_change(GPlatesGui::TopologySectionsContainer *)` |
| `d_remove_action` | `triggered()` | `this` | `react_remove_clicked()` |
| `d_insert_above_action` | `triggered()` | `this` | `react_insert_above_clicked()` |
| `d_insert_below_action` | `triggered()` | `this` | `react_insert_below_clicked()` |
| `d_cancel_insertion_point_action` | `triggered()` | `this` | `react_cancel_insertion_point_clicked()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/TopologySectionsTable.h
python scripts/gpq.py def GPlatesGui::TopologySectionsTable --body
python scripts/gpq.py uses TopologySectionsTable --kind class
python scripts/gpq.py hier TopologySectionsTable
```
