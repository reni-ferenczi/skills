# VelocityMethodWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 336 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/VelocityMethodWidget.h` | C++ | 207 |
| `src/qt-widgets/VelocityMethodWidget.cc` | C++ | 118 |
| `src/qt-widgets/VelocityMethodWidgetUi.ui` | Qt form | 150 |

## Overview

[[[PROSE overview unit=qt-widgets/VelocityMethodWidget tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::VelocityMethodWidget`](#gplatesqtwidgetsvelocitymethodwidget) | class | `QWidget`<br>`Ui_VelocityMethodWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::VelocityMethodWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MapValueEquals` | class | `None` | public | — |
| `VelocityMethod` | enum | `None` | public | — |
| `velocity_method_description_map_type` | typedef | `QMap<VelocityMethod,QString>` | public | — |
| `VelocityMethodWidget(bool show_threshold_spinboxes = true, QWidget *parent = 0)` | constructor | `None` | public | — |
| `~VelocityMethodWidget()` | destructor | `None` | public | — |
| `delta_time_spinbox()` | method | `QDoubleSpinBox` | public | — |
| `velocity_yellow_spinbox()` | method | `QDoubleSpinBox` | public | — |
| `velocity_red_spinbox()` | method | `QDoubleSpinBox` | public | — |
| `velocity_method_button_group()` | method | `QButtonGroup` | public | — |
| `delta_time()` | method | `double` | public | — |
| `set_delta_time( double delta_time_)` | method | `void` | public | — |
| `yellow_velocity_threshold()` | method | `double` | public | — |
| `set_yellow_velocity_threshold( double yellow)` | method | `void` | public | — |
| `red_velocity_threshold()` | method | `double` | public | — |
| `set_red_velocity_threshold( double red)` | method | `void` | public | — |
| `velocity_method()` | method | `VelocityMethod` | public | — |
| `set_velocity_method( const VelocityMethod &method)` | method | `void` | public | — |
| `configuration_changed( bool valid)` | method | `void` | public | configuration\_changed - emitted when the dt spinbox has changed. |
| `handle_velocity_method_changed()` | method | `void` | private | — |
| `handle_delta_time_changed()` | method | `void` | private | — |
| `handle_velocity_yellow_changed()` | method | `void` | private | — |
| `handle_velocity_red_changed()` | method | `void` | private | — |
| `d_velocity_method` | field | `VelocityMethod` | private | — |
| `d_spin_box_palette` | field | `QPalette` | private | d\_spin\_box\_palette - the palette used in the delta\_time spinboxe. |
| `d_show_threshold_spinboxes` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_VELOCITYMETHODWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/VelocityMethodWidget tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportNetRotationAnimationStrategy](../gui/ExportNetRotationAnimationStrategy.md) | gui | 9 |
| [gui/ExportOptionsUtils](../gui/ExportOptionsUtils.md) | gui | 7 |
| [qt-widgets/ExportNetRotationOptionsWidget](ExportNetRotationOptionsWidget.md) | qt-widgets | 5 |
| [gui/ExportAnimationRegistry](../gui/ExportAnimationRegistry.md) | gui | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `VelocityMethodWidget` | `QWidget` | Form | 11 |

**Qt signal/slot connections** (6 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `radio_t_to_t_minus_dt` | `clicked()` | `this` | `handle_velocity_method_changed()` |
| `radio_t_plus_dt_to_t` | `clicked()` | `this` | `handle_velocity_method_changed()` |
| `radio_t_plus_dt_to_t_minus_dt` | `clicked()` | `this` | `handle_velocity_method_changed()` |
| `spinbox_dt` | `valueChanged(double)` | `this` | `handle_delta_time_changed()` |
| `spinbox_yellow` | `valueChanged(double)` | `this` | `handle_velocity_yellow_changed()` |
| `spinbox_red` | `valueChanged(double)` | `this` | `handle_velocity_red_changed()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/VelocityMethodWidget.h
python scripts/gpq.py def GPlatesQtWidgets::VelocityMethodWidget --body
python scripts/gpq.py uses VelocityMethodWidget --kind class
python scripts/gpq.py hier VelocityMethodWidget
```
