# DigitisationWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 556 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/DigitisationWidget.h` | C++ | 214 |
| `src/qt-widgets/DigitisationWidget.cc` | C++ | 294 |
| `src/qt-widgets/DigitisationWidgetUi.ui` | Qt form | 205 |

## Overview

A task panel widget for digitizing geometric features on the map. Wraps a `GeometryBuilder` and `LatLonCoordinatesTable` to display coordinates as the user draws. Lets users export digitized coordinates, create features from them, or use them in WFS requests. Responds to canvas tool geometry changes and provides actions for clearing and undoing the digitized geometry.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::DigitisationWidget`](#gplatesqtwidgetsdigitisationwidget) | class | [`TaskPanelWidget`](TaskPanelWidget.md)<br>`Ui_DigitisationWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::DigitisationWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DigitisationWidget( GPlatesViewOperations::GeometryBuilder &digitise_geometry_builder, GPlatesCanvasTools::GeometryOperationState &geometry_operation_state, GPlatesPresentation::ViewState &view_state_, ViewportWindow &viewport_window_, QAction *clear_action, QAction *undo_action, GPlatesGui::CanvasToolWorkflows &canvas ...` | constructor | `None` | public | — |
| `~DigitisationWidget()` | destructor | `None` | public | — |
| `reload_coordinates_table_if_necessary()` | method | `void` | public | — |
| `handle_activation()` | method | `void` | public | — |
| `get_clear_action_text()` | method | `QString` | public | — |
| `clear_action_enabled()` | method | `bool` | public | — |
| `handle_clear_action_triggered()` | method | `void` | public | — |
| `handle_create()` | method | `void` | private | The slot that gets called when the user clicks "Create". |
| `handle_export()` | method | `void` | private | Feeds the ExportCoordinatesDialog a GeometryOnSphere, and then displays it. |
| `handle_use_in_wfs()` | method | `void` | private | Feeds the ExportCoordinatesDialog a GeometryOnSphere, and then displays it. |
| `handle_geometry_changed()` | method | `void` | private | The slot that gets called when the geometry inside the geometry builder is changed. |
| `d_viewport_window` | field | `ViewportWindow` | private | The almighty Viewport Window , holder of all dialogs! |
| `d_export_coordinates_dialog` | field | `ExportCoordinatesDialog` | private | The dialog the user sees when they hit the Export button. |
| `d_create_feature_dialog` | field | `CreateFeatureDialog` | private | The dialog the user sees when they hit the Create button. |
| `d_new_geom_builder` | field | `GPlatesViewOperations::GeometryBuilder` | private | The new geometry GeometryBuilder we use when we need to create new feature geometry. |
| `d_canvas_tool_workflows` | field | `GPlatesGui::CanvasToolWorkflows` | private | Used by clear geometry undo operation. |
| `d_lat_lon_coordinates_table` | field | `boost::scoped_ptr<LatLonCoordinatesTable>` | private | A wrapper around coordinates table that listens to a GeometryBuilder and fills in the table accordingly. |
| `make_signal_slot_connections()` | method | `void` | private | — |
| `coordinates_table()` | method | `QTreeWidget` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_DIGITISATIONWIDGET_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/TaskPanel](TaskPanel.md) | qt-widgets | 4 |
| [presentation/Application](../presentation/Application.md) | presentation | 1 |
| [qt-widgets/ViewportWindow](ViewportWindow.md) | qt-widgets | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `DigitisationWidget` | `QWidget` | Form | 8 |

**Qt signal/slot connections** (4 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_export_coordinates` | `clicked()` | `this` | `handle_export()` |
| `button_use_in_wfs` | `clicked()` | `this` | `handle_use_in_wfs()` |
| `button_create_feature` | `clicked()` | `this` | `handle_create()` |
| `d_new_geom_builder` | `stopped_updating_geometry()` | `this` | `handle_geometry_changed()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/DigitisationWidget.h
python scripts/gpq.py def GPlatesQtWidgets::DigitisationWidget --body
python scripts/gpq.py uses DigitisationWidget --kind class
python scripts/gpq.py hier DigitisationWidget
```
