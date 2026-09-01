# LightingWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 591 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/LightingWidget.h` | C++ | 102 |
| `src/qt-widgets/LightingWidget.cc` | C++ | 225 |
| `src/qt-widgets/LightingWidgetUi.ui` | Qt form | 121 |

## Overview

[[[PROSE overview unit=qt-widgets/LightingWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::LightingWidget`](#gplatesqtwidgetslightingwidget) | class | [`TaskPanelWidget`](TaskPanelWidget.md)<br>`Ui_LightingWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::LightingWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LightingWidget( ViewportWindow &viewport_window_, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~LightingWidget()` | destructor | `None` | public | — |
| `handle_activation()` | method | `void` | public | — |
| `react_enable_lighting_geometry_on_sphere_check_box_changed()` | method | `void` | private | — |
| `react_enable_lighting_filled_geometry_on_sphere_check_box_changed()` | method | `void` | private | — |
| `react_enable_lighting_arrow_check_box_changed()` | method | `void` | private | — |
| `react_enable_lighting_raster_check_box_changed()` | method | `void` | private | — |
| `react_enable_lighting_scalar_field_check_box_changed()` | method | `void` | private | — |
| `react_ambient_lighting_spinbox_changed( double value)` | method | `void` | private | — |
| `react_light_direction_attached_to_view_frame_check_box_changed()` | method | `void` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_globe_and_map_widget` | field | `GlobeAndMapWidget` | private | — |
| `apply_lighting()` | method | `void` | private | — |
| `make_signal_slot_connections()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QT_WIDGETS_LIGHTINGWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/LightingWidget tier=3]]]
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
| `LightingWidget` | `QWidget` | Form | 10 |

**Qt signal/slot connections** (7 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `enable_lighting_geometry_on_sphere` | `stateChanged(int)` | `this` | `react_enable_lighting_geometry_on_sphere_check_box_changed()` |
| `enable_lighting_arrow` | `stateChanged(int)` | `this` | `react_enable_lighting_arrow_check_box_changed()` |
| `enable_lighting_filled_geometry_on_sphere` | `stateChanged(int)` | `this` | `react_enable_lighting_filled_geometry_on_sphere_check_box_changed()` |
| `enable_lighting_raster` | `stateChanged(int)` | `this` | `react_enable_lighting_raster_check_box_changed()` |
| `enable_lighting_scalar_field` | `stateChanged(int)` | `this` | `react_enable_lighting_scalar_field_check_box_changed()` |
| `ambient_lighting_spin_box` | `valueChanged(double)` | `this` | `react_ambient_lighting_spinbox_changed(double)` |
| `light_direction_attached_to_view_frame_check_box` | `stateChanged(int)` | `this` | `react_light_direction_attached_to_view_frame_check_box_changed()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/LightingWidget.h
python scripts/gpq.py def GPlatesQtWidgets::LightingWidget --body
python scripts/gpq.py uses LightingWidget --kind class
python scripts/gpq.py hier LightingWidget
```
