# ModifyGeometryWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 0 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ModifyGeometryWidget.h` | C++ | 98 |
| `src/qt-widgets/ModifyGeometryWidget.cc` | C++ | 64 |
| `src/qt-widgets/ModifyGeometryWidgetUi.ui` | Qt form | 70 |

## Overview

[[[PROSE overview unit=qt-widgets/ModifyGeometryWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=qt-widgets/ModifyGeometryWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
