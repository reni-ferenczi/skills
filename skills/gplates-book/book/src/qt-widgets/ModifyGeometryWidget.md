# ModifyGeometryWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 0 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ModifyGeometryWidget.h` | C++ | 98 |
| `src/qt-widgets/ModifyGeometryWidget.cc` | C++ | 64 |
| `src/qt-widgets/ModifyGeometryWidgetUi.ui` | Qt form | 70 |

## Overview

A task panel widget that displays the latitude/longitude coordinates of a geometry as it is being modified by an interactive canvas tool. When a user modifies geometry on the globe or map, this widget reflects those changes in real-time by displaying each vertex's coordinates.

The widget uses a `LatLonCoordinatesTable` to wrap around the underlying `QTreeWidget` and automatically listens to the `GeometryBuilder` state of the canvas tool. As vertices are added, moved, or removed, the coordinates table is kept in sync and refreshed on demand via `reload_coordinates_table_if_necessary()`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ModifyGeometryWidget`](#gplatesqtwidgetsmodifygeometrywidget) | class | [`TaskPanelWidget`](TaskPanelWidget.md)<br>`Ui_ModifyGeometryWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ModifyGeometryWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ModifyGeometryWidget( GPlatesCanvasTools::GeometryOperationState &geometry_operation_state, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~ModifyGeometryWidget()` | destructor | `None` | public | — |
| `reload_coordinates_table_if_necessary()` | method | `void` | public | — |
| `handle_activation()` | method | `void` | public | — |
| `coordinates_table()` | method | `QTreeWidget` | private | — |
| `d_lat_lon_coordinates_table` | field | `boost::scoped_ptr<LatLonCoordinatesTable>` | private | A wrapper around coordinates table that listens to a GeometryBuilder and fills in the table accordingly. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_MODIFYGEOMETRYWIDGET_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/TaskPanel](TaskPanel.md) | qt-widgets | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ModifyGeometryWidget` | `QWidget` | Form | 3 |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ModifyGeometryWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ModifyGeometryWidget --body
python scripts/gpq.py uses ModifyGeometryWidget --kind class
python scripts/gpq.py hier ModifyGeometryWidget
```
