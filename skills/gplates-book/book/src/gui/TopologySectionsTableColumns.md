# TopologySectionsTableColumns

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 103 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/TopologySectionsTableColumns.h` | C++ | 192 |
| `src/gui/TopologySectionsTableColumns.cc` | C++ | 725 |

## Overview

This namespace defines how each column of the Topology Sections table (populated from `TopologySectionsContainer`) is displayed and edited by `TopologySectionsTable`. `ColumnHeadingInfo` bundles everything one column needs — its label, tooltip, width, resize mode, alignment, item flags, and four function pointers: an `accessor` to render a `TableRow` into a `QTableWidgetItem`, a `mutator` to write user-entered cell data back into a `TableRow`, a predicate deciding whether the cell needs an editing widget instead of plain text, and a factory that creates that widget. `get_column_heading_infos()` builds and returns the full `std::vector<ColumnHeadingInfo>` (backed by the file-scope `COLUMN_HEADING_INFO_TABLE`) that drives the table's setup; `COLUMN_ACTIONS` is the reserved index-0 column for the row action buttons, distinct from every data-bound column.

The concrete accessor/mutator functions (`get_data_time_of_appearance`, `get_data_reconstruction_plate_id`, `get_data_feature_name`, etc.) each know how to pull one piece of data — feature type, reconstruction plate ID, name, begin/end time — either from the `TableRow`'s own overrides or by falling back to the referenced feature's own property (via `GPlatesFeatureVisitors::get_property_value`). `get_time_of_appearance()`/`get_time_of_disappearance()` implement that fallback chain explicitly: the topological section's own begin/end time first, then the referenced feature's `gml:validTime`, then distant past/future as a last resort; `should_edit_time_period()` decides a row is independently time-editable only when both a begin and an end time are already set on the section itself.

`EditTimeWidget` is the cell-editing widget for those begin/end time columns: a `QDoubleSpinBox` for the numeric time in Ma paired with a "Distant Past"/"Distant Future" `QCheckBox` that disables the spinbox when checked. It must live in this header (rather than the `.cc`) so Qt's moc picks up its `Q_OBJECT` macro.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::TopologySectionsTableColumns::ColumnHeadingInfo`](#gplatesguitopologysectionstablecolumnscolumnheadinginfo) | struct | — | — | 0 | Defines characteristics of each column of the table. |
| [`GPlatesGui::TopologySectionsTableColumns::EditTimeWidget`](#gplatesguitopologysectionstablecolumnsedittimewidget) | class | `QWidget` | — | 0 | A widget to edit the begin/end times of a topological section independently of the begin/end times of the feature the topological section is referencing. |

## Members

### `GPlatesGui::TopologySectionsTableColumns::ColumnHeadingInfo`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `label` | field | `char` | public | — |
| `tooltip` | field | `char` | public | — |
| `width` | field | `int` | public | — |
| `resize_mode` | field | `QHeaderView::ResizeMode` | public | — |
| `data_alignment` | field | `QFlags<Qt::AlignmentFlag>` | public | — |
| `data_flags` | field | `QFlags<Qt::ItemFlag>` | public | — |
| `accessor` | field | `table_accessor_type` | public | — |
| `mutator` | field | `table_mutator_type` | public | — |
| `should_edit_cell_with_widget` | field | `should_install_edit_cell_widget_type` | public | — |
| `create_edit_cell_widget` | field | `create_edit_cell_widget_type` | public | — |

### `GPlatesGui::TopologySectionsTableColumns::EditTimeWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Time` | enum | `None` | public | Whether this widget is tracking begin or end time. |
| `EditTimeWidget( Time begin_or_end_time, GPlatesGui::TopologySectionsContainer &sections_container, GPlatesGui::TopologySectionsContainer::size_type sections_container_index, QWidget *parent_)` | constructor | `None` | public | — |
| `~EditTimeWidget()` | destructor | `None` | public | — |
| `focusInEvent( QFocusEvent *focus_event)` | method | `void` | public | — |
| `focusOutEvent( QFocusEvent *focus_event)` | method | `void` | public | — |
| `eventFilter( QObject *obj, QEvent *event)` | method | `bool` | public | — |
| `set_spinbox_time_in_topology_section( double time)` | method | `void` | private | — |
| `set_distant_time_checkstate( int)` | method | `void` | private | — |
| `d_begin_or_end_time` | field | `Time` | private | — |
| `d_sections_container` | field | `TopologySectionsContainer` | private | — |
| `d_sections_container_index` | field | `TopologySectionsContainer::size_type` | private | — |
| `d_table_row` | field | `TopologySectionsContainer::TableRow` | private | — |
| `d_time_spinbox` | field | `QDoubleSpinBox` | private | — |
| `d_distant_time_checkbox` | field | `QCheckBox` | private | — |
| `get_time_from_topology_section()` | method | `GPlatesPropertyValues::GeoTimeInstant` | private | Returns the begin or end time of the current topological section if exists or the begin/end time of the feature referenced by it. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_time_of_appearance( const GPlatesGui::TopologySectionsContainer::TableRow &table_row)` | function | `GPlatesPropertyValues::GeoTimeInstant` | Returns time of appearance using topological section first and if it's not set then returns time of appearance from feature referenced by topological section and if that's not set then returns distant past. |
| `get_time_of_disappearance( const GPlatesGui::TopologySectionsContainer::TableRow &table_row)` | function | `GPlatesPropertyValues::GeoTimeInstant` | Returns time of disappearance using topological section first and if it's not set then returns time of disappearance from feature referenced by topological section and if that's not set then returns distant future. |
| `should_edit_time_period( const GPlatesGui::TopologySectionsContainer::TableRow &row_data)` | function | `bool` | Returns true if the user should be able to edit the topological sections's time period. |
| `null_data_accessor( const GPlatesGui::TopologySectionsContainer::TableRow &, QTableWidgetItem &)` | function | `void` | Table accessor functions: These functions take the raw data and modify a QTableWidgetItem to display the data appropriately. |
| `display_time( const GPlatesPropertyValues::GeoTimeInstant &geo_time, QTableWidgetItem &cell)` | function | `void` | Displays a GeomTimeInstant in a QTableWidgetItem. |
| `get_data_time_edit_flag( const GPlatesGui::TopologySectionsContainer::TableRow &row_data, QTableWidgetItem &cell)` | function | `void` | — |
| `get_data_time_of_appearance( const GPlatesGui::TopologySectionsContainer::TableRow &row_data, QTableWidgetItem &cell)` | function | `void` | — |
| `get_data_time_of_disappearance( const GPlatesGui::TopologySectionsContainer::TableRow &row_data, QTableWidgetItem &cell)` | function | `void` | — |
| `get_data_feature_type( const GPlatesGui::TopologySectionsContainer::TableRow &row_data, QTableWidgetItem &cell)` | function | `void` | — |
| `get_data_reconstruction_plate_id( const GPlatesGui::TopologySectionsContainer::TableRow &row_data, QTableWidgetItem &cell)` | function | `void` | — |
| `get_data_feature_name( const GPlatesGui::TopologySectionsContainer::TableRow &row_data, QTableWidgetItem &cell)` | function | `void` | — |
| `null_data_mutator( GPlatesGui::TopologySectionsContainer::TableRow &, const QTableWidgetItem &)` | function | `void` | Table mutator functions: These functions take a QTableWidgetItem with user-entered values and update the raw data appropriately. |
| `set_data_time_edit_flag( GPlatesGui::TopologySectionsContainer::TableRow &row_data, const QTableWidgetItem &cell)` | function | `void` | — |
| `null_install_edit_cell_widget_query( const GPlatesGui::TopologySectionsContainer::TableRow &/*row_data*/)` | function | `bool` | Cell widget query functions: These functions query whether a cell widget should be created to allow the user to edit the raw data or whether a regular QTableWidgetItem should be created. |
| `install_edit_time_period_widget_query( const GPlatesGui::TopologySectionsContainer::TableRow &row_data)` | function | `bool` | — |
| `null_edit_cell_widget_creator( QTableWidget *, GPlatesGui::TopologySectionsContainer &, GPlatesGui::TopologySectionsContainer::size_type)` | function | `QWidget` | Cell widget creation functions: These functions create a cell widget that allows the user to edit the raw data. |
| `edit_begin_time_cell_widget_creator( QTableWidget *table_widget, GPlatesGui::TopologySectionsContainer &sections_container, GPlatesGui::TopologySectionsContainer::size_type sections_container_index)` | function | `QWidget` | — |
| `edit_end_time_cell_widget_creator( QTableWidget *table_widget, GPlatesGui::TopologySectionsContainer &sections_container, GPlatesGui::TopologySectionsContainer::size_type sections_container_index)` | function | `QWidget` | — |
| `COLUMN_HEADING_INFO_TABLE` | variable | `GPlatesGui::TopologySectionsTableColumns::ColumnHeadingInfo` | The column header information table. |
| `GPLATES_GUI_TOPOLOGYSECTIONSTABLECOLUMNS_H` | macro | `None` | — |
| `get_column_heading_infos()` | function | `std::vector<ColumnHeadingInfo>` | Returns the column header information table. |
| `COLUMN_ACTIONS` | variable | `int` | The "actions" column is the zero column. |

## Notes

`EditTimeWidget` edits a local copy of the row (`d_table_row`, taken at construction time via `sections_container.at(...)`), not the container directly. Its slots (`set_spinbox_time_in_topology_section()`, `set_distant_time_checkstate()`) only mutate that local copy — the only call to `d_sections_container.update_at()` that would commit it back lives in `focusOutEvent()`, which along with the destructor and `eventFilter()` is compiled out under `#if 0`. As the code currently stands, edits made through this widget's spinbox or checkbox are never written back to the `TopologySectionsContainer`.

`ColumnHeadingInfo`'s four members are raw C function pointers (not `std::function` or virtuals), so every accessor/mutator/predicate/factory must have C-linkage-compatible free-function signatures matching the `table_accessor_type` etc. typedefs exactly.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/TopologySectionsTable](TopologySectionsTable.md) | gui | 33 |
| [app-logic/deprecated/ReconstructedFeatureGeometryPopulator](../app-logic/deprecated/ReconstructedFeatureGeometryPopulator.md) | app-logic | 7 |
| [app-logic/ReconstructMethodHalfStageRotation](../app-logic/ReconstructMethodHalfStageRotation.md) | app-logic | 5 |
| [app-logic/TopologyGeometryResolver](../app-logic/TopologyGeometryResolver.md) | app-logic | 2 |
| [app-logic/ReconstructMethodByPlateId](../app-logic/ReconstructMethodByPlateId.md) | app-logic | 1 |
| [app-logic/ReconstructMethodFlowline](../app-logic/ReconstructMethodFlowline.md) | app-logic | 1 |
| [app-logic/ReconstructMethodInterface](../app-logic/ReconstructMethodInterface.md) | app-logic | 1 |
| [app-logic/ReconstructMethodVirtualGeomagneticPole](../app-logic/ReconstructMethodVirtualGeomagneticPole.md) | app-logic | 1 |
| [app-logic/TopologyNetworkResolver](../app-logic/TopologyNetworkResolver.md) | app-logic | 1 |

## Related

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_time_spinbox` | `valueChanged(double)` | `this` | `set_spinbox_time_in_topology_section(double)` |
| `d_distant_time_checkbox` | `stateChanged(int)` | `this` | `set_distant_time_checkstate(int)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/TopologySectionsTableColumns.h
python scripts/gpq.py def GPlatesGui::TopologySectionsTableColumns::EditTimeWidget --body
python scripts/gpq.py uses EditTimeWidget --kind class
python scripts/gpq.py hier EditTimeWidget
```
