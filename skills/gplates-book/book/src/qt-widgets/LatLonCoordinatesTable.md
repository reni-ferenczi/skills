# LatLonCoordinatesTable

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 348 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/LatLonCoordinatesTable.h` | C++ | 207 |
| `src/qt-widgets/LatLonCoordinatesTable.cc` | C++ | 801 |

## Overview

A `QObject` wrapper around a `QTreeWidget` that displays the geometry(ies) and their latitude/longitude coordinates in a hierarchical tree. It listens to a `GeometryBuilder` and keeps the tree in sync as geometries and points are inserted, removed, or moved.

The tree is populated by `initialise_table_from_current_geometry_builder()`, which uses a `TreeWidgetBuilder` to construct the hierarchy. Each geometry is a top-level item with its type label, and points are children showing their lat/lon coordinates. The class also responds to highlighting signals from `GeometryOperation`, allowing points to be visually highlighted in the tree.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::LatLonColumnLayout`](#anonymouslatloncolumnlayout) | enum | — | — | 0 | The order that coordinates are displayed in the tree widget. |
| [`GPlatesQtWidgets::LatLonCoordinatesTable`](#gplatesqtwidgetslatloncoordinatestable) | class | `QObject` | — | 0 | — |

## Members

### `(anonymous)::LatLonColumnLayout`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `COLUMN_LAT` | enumerator | `None` | — | — |
| `COLUMN_LON` | enumerator | `None` | — | — |

### `GPlatesQtWidgets::LatLonCoordinatesTable`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LatLonCoordinatesTable( QTreeWidget *coordinates_table, GPlatesCanvasTools::GeometryOperationState &geometry_operation_state)` | constructor | `None` | public | — |
| `reload_if_necessary()` | method | `void` | public | — |
| `change_actual_geometry_type( GPlatesViewOperations::GeometryBuilder::GeometryIndex geometry_index, GPlatesMaths::GeometryType::Value geometry_type)` | method | `void` | private | NOTE: all signals/slots should use namespace scope for all arguments otherwise differences between signals and slots will cause Qt to not be able to connect them at runtime. |
| `insert_geometry( GPlatesViewOperations::GeometryBuilder::GeometryIndex geometry_index)` | method | `void` | private | — |
| `remove_geometry( GPlatesViewOperations::GeometryBuilder::GeometryIndex geometry_index)` | method | `void` | private | — |
| `insert_point_into_current_geometry( GPlatesViewOperations::GeometryBuilder::PointIndex point_index, const GPlatesMaths::PointOnSphere &oriented_pos_on_globe)` | method | `void` | private | — |
| `remove_point_from_current_geometry( GPlatesViewOperations::GeometryBuilder::PointIndex point_index)` | method | `void` | private | — |
| `move_point_in_current_geometry( GPlatesViewOperations::GeometryBuilder::PointIndex point_index, const GPlatesMaths::PointOnSphere &new_oriented_pos_on_globe)` | method | `void` | private | — |
| `switched_geometry_operation( GPlatesViewOperations::GeometryOperation *geometry_operation)` | method | `void` | private | The geometry operation emitting signals has changed. geometry\_operation is NULL if no GeometryOperation is currently activated. |
| `switched_geometry_builder( GPlatesViewOperations::GeometryBuilder *geometry_builder)` | method | `void` | private | The geometry builder emitting signals has changed. geometry\_builder is NULL if no GeometryBuilder is currently activated. |
| `highlight_point_in_geometry( GPlatesViewOperations::GeometryBuilder *geometry_builder, GPlatesViewOperations::GeometryBuilder::GeometryIndex geometry_index, GPlatesViewOperations::GeometryBuilder::PointIndex point_index, const GPlatesGui::Colour &highlight_colour)` | method | `void` | private | The point at index point\_index was in the geometry at index geometry\_index in the geometry builder geometry\_builder was highlighted by a geometry operation. |
| `unhighlight_point_in_geometry( GPlatesViewOperations::GeometryBuilder *geometry_builder, GPlatesViewOperations::GeometryBuilder::GeometryIndex geometry_index, GPlatesViewOperations::GeometryBuilder::PointIndex point_index)` | method | `void` | private | No points are highlighted by this geometry operation in the geometry builder geometry\_builder. |
| `d_coordinates_table` | field | `QTreeWidget` | private | The QTreeWidget that we fill in. |
| `d_tree_widget_builder` | field | `GPlatesGui::TreeWidgetBuilder` | private | Helps assemble our QTreeWidget. |
| `d_current_geometry_builder` | field | `GPlatesViewOperations::GeometryBuilder` | private | The GeometryBuilder we are listening to. |
| `d_current_geometry_operation` | field | `GPlatesViewOperations::GeometryOperation` | private | The GeometryOperation we are listening to. |
| `d_need_to_reload_data` | field | `bool` | private | A flag to indicate whether we need to reload data. |
| `connect_to_geometry_operation_state_signals( GPlatesCanvasTools::GeometryOperationState &geometry_operation_state)` | method | `void` | private | — |
| `connect_to_current_geometry_operation()` | method | `void` | private | — |
| `disconnect_from_current_geometry_operation()` | method | `void` | private | — |
| `connect_to_current_geometry_builder()` | method | `void` | private | — |
| `disconnect_from_current_geometry_builder()` | method | `void` | private | — |
| `initialise_table_from_current_geometry_builder()` | method | `void` | private | Fill in QTreeWidget using the current GeometryBuilder object. |
| `insert_point_into_geometry( GPlatesViewOperations::GeometryBuilder::GeometryIndex geometry_index, GPlatesViewOperations::GeometryBuilder::PointIndex point_index, const GPlatesMaths::PointOnSphere &oriented_pos_on_globe)` | method | `void` | private | — |
| `remove_point_from_geometry( GPlatesViewOperations::GeometryBuilder::GeometryIndex geometry_index, GPlatesViewOperations::GeometryBuilder::PointIndex point_index)` | method | `void` | private | — |
| `get_coord_item( GPlatesViewOperations::GeometryBuilder::GeometryIndex geometry_index, GPlatesViewOperations::GeometryBuilder::PointIndex point_index)` | method | `QTreeWidgetItem` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `create_geometry_item( GPlatesGui::TreeWidgetBuilder &tree_widget_builder, const QString &label = QString())` | function | `GPlatesGui::TreeWidgetBuilder::item_handle_type` | Creates a top-level QTreeWidgetItem used to distinguish between parts of multi-geometries and polygon innards. |
| `highlight_lat_lon( QTreeWidgetItem *coord_item, const GPlatesGui::Colour &highlight_colour)` | function | `void` | Sets the QTreeWidgetItem's foreground/background colour to the highlight colour. |
| `unhighlight_lat_lon( QTreeWidgetItem *coord_item)` | function | `void` | Sets the QTreeWidgetItem's foreground/background colour to the unhighlight colour. |
| `set_lat_lon( QTreeWidgetItem *coord_item, double lat, double lon)` | function | `void` | Modifies the lat/lon of an existing tree widget item. |
| `create_lat_lon_item( GPlatesGui::TreeWidgetBuilder &tree_widget_builder, double lat, double lon)` | function | `GPlatesGui::TreeWidgetBuilder::item_handle_type` | Turns a lat,lon pair into a tree widget item ready for insertion into the tree. |
| `get_geometry_type_text( GPlatesMaths::GeometryType::Value geom_type)` | function | `QString` | — |
| `GPLATES_QTWIDGETS_LATLONCOORDINATESTABLE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ModifyGeometryWidget](ModifyGeometryWidget.md) | qt-widgets | 9 |
| [qt-widgets/DigitisationWidget](DigitisationWidget.md) | qt-widgets | 3 |

## Related

**Qt signal/slot connections** (10 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&geometry_operation_state` | `switched_geometry_operation( GPlatesViewOperations::GeometryOperation *)` | `this` | `switched_geometry_operation( GPlatesViewOperations::GeometryOperation *)` |
| `&geometry_operation_state` | `switched_geometry_builder( GPlatesViewOperations::GeometryBuilder *)` | `this` | `switched_geometry_builder( GPlatesViewOperations::GeometryBuilder *)` |
| `d_current_geometry_operation` | `highlight_point_in_geometry( GPlatesViewOperations::GeometryBuilder *, GPlatesViewOperations::GeometryBuilder::GeometryIndex, GPlatesViewOperations::GeometryBuilder::PointIndex, const GPlatesGui::Colo` | `this` | `highlight_point_in_geometry( GPlatesViewOperations::GeometryBuilder *, GPlatesViewOperations::GeometryBuilder::GeometryIndex, GPlatesViewOperations::GeometryBuilder::PointIndex, const GPlatesGui::Colo` |
| `d_current_geometry_operation` | `unhighlight_point_in_geometry( GPlatesViewOperations::GeometryBuilder *, GPlatesViewOperations::GeometryBuilder::GeometryIndex, GPlatesViewOperations::GeometryBuilder::PointIndex)` | `this` | `unhighlight_point_in_geometry( GPlatesViewOperations::GeometryBuilder *, GPlatesViewOperations::GeometryBuilder::GeometryIndex, GPlatesViewOperations::GeometryBuilder::PointIndex)` |
| `d_current_geometry_builder` | `changed_actual_geometry_type( GPlatesViewOperations::GeometryBuilder::GeometryIndex, GPlatesMaths::GeometryType::Value)` | `this` | `change_actual_geometry_type( GPlatesViewOperations::GeometryBuilder::GeometryIndex, GPlatesMaths::GeometryType::Value)` |
| `d_current_geometry_builder` | `inserted_geometry( GPlatesViewOperations::GeometryBuilder::GeometryIndex)` | `this` | `insert_geometry( GPlatesViewOperations::GeometryBuilder::GeometryIndex)` |
| `d_current_geometry_builder` | `removed_geometry( GPlatesViewOperations::GeometryBuilder::GeometryIndex)` | `this` | `remove_geometry( GPlatesViewOperations::GeometryBuilder::GeometryIndex)` |
| `d_current_geometry_builder` | `inserted_point_into_current_geometry( GPlatesViewOperations::GeometryBuilder::PointIndex, const GPlatesMaths::PointOnSphere &)` | `this` | `insert_point_into_current_geometry( GPlatesViewOperations::GeometryBuilder::PointIndex, const GPlatesMaths::PointOnSphere &)` |
| `d_current_geometry_builder` | `removed_point_from_current_geometry( GPlatesViewOperations::GeometryBuilder::PointIndex)` | `this` | `remove_point_from_current_geometry( GPlatesViewOperations::GeometryBuilder::PointIndex)` |
| `d_current_geometry_builder` | `moved_point_in_current_geometry( GPlatesViewOperations::GeometryBuilder::PointIndex, const GPlatesMaths::PointOnSphere &, bool)` | `this` | `move_point_in_current_geometry( GPlatesViewOperations::GeometryBuilder::PointIndex, const GPlatesMaths::PointOnSphere &)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/LatLonCoordinatesTable.h
python scripts/gpq.py def GPlatesQtWidgets::LatLonCoordinatesTable --body
python scripts/gpq.py uses LatLonCoordinatesTable --kind class
python scripts/gpq.py hier LatLonCoordinatesTable
```
