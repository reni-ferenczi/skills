# VelocityFieldCalculatorLayerOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 623 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/VelocityFieldCalculatorLayerOptionsWidget.h` | C++ | 143 |
| `src/qt-widgets/VelocityFieldCalculatorLayerOptionsWidget.cc` | C++ | 672 |
| `src/qt-widgets/VelocityFieldCalculatorLayerOptionsWidgetUi.ui` | Qt form | 556 |

## Overview

Options panel for `VelocityFieldCalculatorLayer`, controlling how velocities are calculated and displayed. It allows users to select the velocity calculation method (velocities of surfaces versus velocities of domain points), configure arrow rendering density and scale, and set up smoothing of velocities across plate boundaries. The widget manages its own state through slots that respond to spinbox and combobox changes, reading and writing layer parameters from the current `VisualLayer`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::VelocityFieldCalculatorLayerOptionsWidget`](#gplatesqtwidgetsvelocityfieldcalculatorlayeroptionswidget) | class | [`LayerOptionsWidget`](LayerOptionsWidget.md)<br>`Ui_VelocityFieldCalculatorLayerOptionsWidget` | — | 0 | VelocityFieldCalculatorLayerOptionsWidget is used to show additional options for topology network layers in the visual layers widget. |

## Members

### `GPlatesQtWidgets::VelocityFieldCalculatorLayerOptionsWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, ViewportWindow *viewport_window, QWidget *parent_)` | method | `LayerOptionsWidget` | public | — |
| `set_data( const boost::weak_ptr<GPlatesPresentation::VisualLayer> &visual_layer)` | method | `void` | public | — |
| `get_title` | field | `QString` | public | — |
| `handle_solve_velocity_method_combobox_activated( int index)` | method | `void` | private | — |
| `handle_arrow_spacing_value_changed( double arrow_spacing)` | method | `void` | private | — |
| `handle_unlimited_arrow_spacing_clicked()` | method | `void` | private | — |
| `handle_arrow_body_scale_value_changed( double arrow_body_scale_log10)` | method | `void` | private | — |
| `handle_arrowhead_scale_value_changed( double arrowhead_scale_log10)` | method | `void` | private | — |
| `handle_velocity_delta_time_type_button( bool checked)` | method | `void` | private | — |
| `handle_velocity_delta_time_value_changed( double value)` | method | `void` | private | — |
| `handle_velocity_smoothing_check_box_changed()` | method | `void` | private | — |
| `handle_velocity_smoothing_distance_spinbox_changed( double value)` | method | `void` | private | — |
| `handle_exclude_smoothing_in_deforming_regions_check_box_changed()` | method | `void` | private | — |
| `VelocityFieldCalculatorLayerOptionsWidget( GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, ViewportWindow *viewport_window, QWidget *parent_)` | constructor | `None` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_viewport_window` | field | `ViewportWindow` | private | — |
| `d_current_visual_layer` | field | `boost::weak_ptr<GPlatesPresentation::VisualLayer>` | private | The visual layer for which we are currently displaying options. |
| `d_help_solve_velocities_method_dialog` | field | `GPlatesQtWidgets::InformationDialog` | private | — |
| `d_help_arrow_spacing_dialog` | field | `GPlatesQtWidgets::InformationDialog` | private | — |
| `d_help_arrow_scale_dialog` | field | `GPlatesQtWidgets::InformationDialog` | private | — |
| `d_help_velocity_smoothing_dialog` | field | `GPlatesQtWidgets::InformationDialog` | private | — |
| `d_help_velocity_time_delta_dialog` | field | `GPlatesQtWidgets::InformationDialog` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `HELP_SOLVE_VELOCITIES_METHOD_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_SOLVE_VELOCITIES_METHOD_DIALOG_TEXT` | variable | `QString` | — |
| `HELP_ARROW_SPACING_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_ARROW_SPACING_DIALOG_TEXT` | variable | `QString` | — |
| `HELP_ARROW_SCALE_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_ARROW_SCALE_DIALOG_TEXT` | variable | `QString` | — |
| `HELP_VELOCITY_SMOOTHING_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_VELOCITY_SMOOTHING_DIALOG_TEXT` | variable | `QString` | — |
| `HELP_VELOCITY_TIME_DELTA_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_VELOCITY_TIME_DELTA_DIALOG_TEXT` | variable | `QString` | — |
| `GPLATES_QTWIDGETS_VelocityFieldCalculatorLayerOptionsWidget_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/VisualLayerRegistry](../presentation/VisualLayerRegistry.md) | presentation | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `VelocityFieldCalculatorLayerOptionsWidget` | `QWidget` | Layers | 28 |

**Qt signal/slot connections** (27 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `solve_velocities_method_combobox` | `activated(int)` | `this` | `handle_solve_velocity_method_combobox_activated(int)` |
| `arrow_spacing_spinbox` | `valueChanged(double)` | `this` | `handle_arrow_spacing_value_changed(double)` |
| `push_button_unlimited_arrow_spacing` | `clicked()` | `this` | `handle_unlimited_arrow_spacing_clicked()` |
| `arrow_body_scale_spinbox` | `valueChanged(double)` | `this` | `handle_arrow_body_scale_value_changed(double)` |
| `arrowhead_scale_spinbox` | `valueChanged(double)` | `this` | `handle_arrowhead_scale_value_changed(double)` |
| `velocity_delta_time_spinbox` | `valueChanged(double)` | `this` | `handle_velocity_delta_time_value_changed(double)` |
| `radio_t_plus_dt_to_t` | `toggled(bool)` | `this` | `handle_velocity_delta_time_type_button(bool)` |
| `radio_t_to_t_minus_dt` | `toggled(bool)` | `this` | `handle_velocity_delta_time_type_button(bool)` |
| `radio_t_plus_dt_2_to_t_minus_dt_2` | `toggled(bool)` | `this` | `handle_velocity_delta_time_type_button(bool)` |
| `velocity_smoothing_check_box` | `stateChanged(int)` | `this` | `handle_velocity_smoothing_check_box_changed()` |
| `velocity_smoothing_distance_spinbox` | `valueChanged(double)` | `this` | `handle_velocity_smoothing_distance_spinbox_changed(double)` |
| `exclude_smoothing_in_deforming_regions_check_box` | `stateChanged(int)` | `this` | `handle_exclude_smoothing_in_deforming_regions_check_box_changed()` |
| `push_button_help_solve_velocities_method` | `clicked()` | `d_help_solve_velocities_method_dialog` | `show()` |
| `push_button_help_arrow_spacing` | `clicked()` | `d_help_arrow_spacing_dialog` | `show()` |
| `push_button_help_arrow_scale` | `clicked()` | `d_help_arrow_scale_dialog` | `show()` |

*... and 12 more connections.*


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/VelocityFieldCalculatorLayerOptionsWidget.h
python scripts/gpq.py def GPlatesQtWidgets::VelocityFieldCalculatorLayerOptionsWidget --body
python scripts/gpq.py uses VelocityFieldCalculatorLayerOptionsWidget --kind class
python scripts/gpq.py hier VelocityFieldCalculatorLayerOptionsWidget
```
