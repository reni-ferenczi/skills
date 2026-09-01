# ExportVelocityCalculationOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 85 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ExportVelocityCalculationOptionsWidget.h` | C++ | 208 |
| `src/qt-widgets/ExportVelocityCalculationOptionsWidgetUi.ui` | Qt form | 321 |

## Overview

Provides the user interface for configuring velocity calculation parameters. Like `ExportVelocityCalculationOptionsWidget`, this widget does not inherit from `ExportOptionsWidget`; it is designed to be embedded in another export options widget as a sub-component.

The widget allows users to control three aspects of velocity export: the velocity delta-time type (three options for computing velocity over different time intervals), the delta-time value, and velocity smoothing near plate boundaries. Users can enable or disable boundary smoothing and adjust the angular half-extent of the smoothing region. There is also an option to exclude deforming regions from smoothing. When any control changes, the widget updates its internal configuration object, which can be retrieved via `get_export_velocity_calculation_options()`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ExportVelocityCalculationOptionsWidget`](#gplatesqtwidgetsexportvelocitycalculationoptionswidget) | class | `QWidget`<br>`Ui_ExportVelocityCalculationOptionsWidget` | — | 0 | ExportVelocityCalculationOptionsWidget is used to allow the user to change the velocity delta-time interval and type, and also enable smoothing of velocities near plate boundaries (and to adjust any smoothing options). |

## Members

### `GPlatesQtWidgets::ExportVelocityCalculationOptionsWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( QWidget *parent, const GPlatesGui::ExportOptionsUtils::ExportVelocityCalculationOptions & default_export_velocity_calculation_options)` | method | `ExportVelocityCalculationOptionsWidget` | public | Creates a ExportVelocityCalculationOptionsWidget using default options. |
| `handle_velocity_delta_time_type_button( bool checked)` | method | `void` | private | — |
| `handle_velocity_delta_time_value_changed( double value)` | method | `void` | private | — |
| `react_velocity_smoothing_check_box_changed()` | method | `void` | private | — |
| `react_velocity_smoothing_distance_spinbox_changed( double value)` | method | `void` | private | — |
| `react_exclude_smoothing_in_deforming_regions_check_box_changed()` | method | `void` | private | — |
| `ExportVelocityCalculationOptionsWidget( QWidget *parent_, const GPlatesGui::ExportOptionsUtils::ExportVelocityCalculationOptions &export_velocity_calculation_options_)` | constructor | `None` | private | — |
| `make_signal_slot_connections()` | method | `void` | private | — |
| `d_export_velocity_calculation_options` | field | `GPlatesGui::ExportOptionsUtils::ExportVelocityCalculationOptions` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QT_WIDGETS_EXPORTVELOCITYCALCULATIONOPTIONSWIDGET_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ExportVelocityOptionsWidget](ExportVelocityOptionsWidget.md) | qt-widgets | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ExportVelocityCalculationOptionsWidget` | `QWidget` | Form | 15 |

**Qt signal/slot connections** (7 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `radio_t_plus_dt_to_t` | `toggled(bool)` | `this` | `handle_velocity_delta_time_type_button(bool)` |
| `radio_t_to_t_minus_dt` | `toggled(bool)` | `this` | `handle_velocity_delta_time_type_button(bool)` |
| `radio_t_plus_dt_2_to_t_minus_dt_2` | `toggled(bool)` | `this` | `handle_velocity_delta_time_type_button(bool)` |
| `velocity_delta_time_spinbox` | `valueChanged(double)` | `this` | `handle_velocity_delta_time_value_changed(double)` |
| `velocity_smoothing_check_box` | `stateChanged(int)` | `this` | `react_velocity_smoothing_check_box_changed()` |
| `velocity_smoothing_distance_spinbox` | `valueChanged(double)` | `this` | `react_velocity_smoothing_distance_spinbox_changed(double)` |
| `exclude_smoothing_in_deforming_regions_check_box` | `stateChanged(int)` | `this` | `react_exclude_smoothing_in_deforming_regions_check_box_changed()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ExportVelocityCalculationOptionsWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ExportVelocityCalculationOptionsWidget --body
python scripts/gpq.py uses ExportVelocityCalculationOptionsWidget --kind class
python scripts/gpq.py hier ExportVelocityCalculationOptionsWidget
```
