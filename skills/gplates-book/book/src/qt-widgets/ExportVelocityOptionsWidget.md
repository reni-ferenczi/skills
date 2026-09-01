# ExportVelocityOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 266 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ExportVelocityOptionsWidget.h` | C++ | 140 |
| `src/qt-widgets/ExportVelocityOptionsWidget.cc` | C++ | 760 |
| `src/qt-widgets/ExportVelocityOptionsWidgetUi.ui` | Qt form | 506 |

## Overview

Provides the user interface for configuring velocity export options across multiple file formats: GPML, GMT, Terra text, and CitcomS global. The widget inherits from `ExportOptionsWidget` and acts as a container that delegates velocity calculation parameters to `ExportVelocityCalculationOptionsWidget` and file format options to `ExportFileOptionsWidget`.

For GMT export, the widget exposes many velocity-specific controls: velocity vector format (3D, colatitude-longitude, angle-magnitude, or azimuth-magnitude), velocity scaling, velocity sampling stride, coordinate order, and optional metadata inclusion (plate ID, domain points, domain metadata). For Terra text and CitcomS global formats, the widget provides filename template controls to match grid file naming conventions. The widget dynamically hides or shows controls based on the selected file format and updates the output description label whenever options change.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ExportVelocityOptionsWidget`](#gplatesqtwidgetsexportvelocityoptionswidget) | class | [`ExportOptionsWidget`](ExportOptionsWidget.md)<br>`Ui_ExportVelocityOptionsWidget` | — | 0 | General (non-CitcomS-specific) resolved topology export options. |

## Members

### `GPlatesQtWidgets::ExportVelocityOptionsWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( QWidget *parent, GPlatesGui::ExportAnimationContext &export_animation_context, const GPlatesGui::ExportVelocityAnimationStrategy::const_configuration_ptr &export_configuration)` | method | `ExportOptionsWidget` | public | Creates a ExportVelocityOptionsWidget containing default export options. |
| `create_export_animation_strategy_configuration( const QString &filename_template)` | method | `GPlatesGui::ExportAnimationStrategy::const_configuration_base_ptr` | public | Collects the options specified by the user and returns them as an export animation strategy configuration. |
| `react_gmt_velocity_vector_format_radio_button_toggled( bool checked)` | method | `void` | private | — |
| `react_gmt_velocity_scale_spin_box_value_changed( double value)` | method | `void` | private | — |
| `react_gmt_velocity_stride_spin_box_value_changed( int value)` | method | `void` | private | — |
| `react_gmt_domain_point_format_radio_button_toggled( bool checked)` | method | `void` | private | — |
| `react_gmt_include_plate_id_check_box_clicked()` | method | `void` | private | — |
| `react_gmt_include_domain_point_check_box_clicked()` | method | `void` | private | — |
| `react_gmt_include_domain_meta_data_check_box_clicked()` | method | `void` | private | — |
| `handle_terra_grid_filename_template_changed()` | method | `void` | private | — |
| `handle_citcoms_grid_filename_template_changed()` | method | `void` | private | — |
| `react_citcoms_gmt_format_check_box_clicked()` | method | `void` | private | — |
| `react_citcoms_gmt_velocity_scale_spin_box_value_changed( double value)` | method | `void` | private | — |
| `react_citcoms_gmt_velocity_stride_spin_box_value_changed( int value)` | method | `void` | private | — |
| `ExportVelocityOptionsWidget( QWidget *parent_, const GPlatesGui::ExportVelocityAnimationStrategy::const_configuration_ptr &export_configuration)` | constructor | `None` | private | — |
| `make_signal_slot_connections()` | method | `void` | private | — |
| `update_output_description_label()` | method | `void` | private | — |
| `d_export_configuration` | field | `GPlatesGui::ExportVelocityAnimationStrategy::configuration_ptr` | private | — |
| `d_export_velocity_calculation_options_widget` | field | `ExportVelocityCalculationOptionsWidget` | private | — |
| `d_export_file_options_widget` | field | `ExportFileOptionsWidget` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QT_WIDGETS_EXPORTVELOCITYOPTIONSWIDGET_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportAnimationRegistry](../gui/ExportAnimationRegistry.md) | gui | 5 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ExportVelocityOptionsWidget` | `QWidget` | Form | 39 |

**Qt signal/slot connections** (16 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `velocity_vector_3D_radio_button` | `toggled(bool)` | `this` | `react_gmt_velocity_vector_format_radio_button_toggled(bool)` |
| `velocity_vector_colat_lon_radio_button` | `toggled(bool)` | `this` | `react_gmt_velocity_vector_format_radio_button_toggled(bool)` |
| `velocity_vector_angle_magnitude_radio_button` | `toggled(bool)` | `this` | `react_gmt_velocity_vector_format_radio_button_toggled(bool)` |
| `velocity_vector_azimuth_magnitude_radio_button` | `toggled(bool)` | `this` | `react_gmt_velocity_vector_format_radio_button_toggled(bool)` |
| `velocity_scale_spin_box` | `valueChanged(double)` | `this` | `react_gmt_velocity_scale_spin_box_value_changed(double)` |
| `velocity_stride_spin_box` | `valueChanged(int)` | `this` | `react_gmt_velocity_stride_spin_box_value_changed(int)` |
| `lon_lat_radio_button` | `toggled(bool)` | `this` | `react_gmt_domain_point_format_radio_button_toggled(bool)` |
| `lat_lon_radio_button` | `toggled(bool)` | `this` | `react_gmt_domain_point_format_radio_button_toggled(bool)` |
| `include_plate_id_check_box` | `stateChanged(int)` | `this` | `react_gmt_include_plate_id_check_box_clicked()` |
| `include_domain_point_check_box` | `stateChanged(int)` | `this` | `react_gmt_include_domain_point_check_box_clicked()` |
| `include_domain_meta_data_check_box` | `stateChanged(int)` | `this` | `react_gmt_include_domain_meta_data_check_box_clicked()` |
| `terra_grid_filename_template_line_edit` | `editingFinished()` | `this` | `handle_terra_grid_filename_template_changed()` |
| `citcoms_grid_filename_template_line_edit` | `editingFinished()` | `this` | `handle_citcoms_grid_filename_template_changed()` |
| `citcoms_gmt_format_check_box` | `stateChanged(int)` | `this` | `react_citcoms_gmt_format_check_box_clicked()` |
| `citcoms_gmt_velocity_scale_spin_box` | `valueChanged(double)` | `this` | `react_citcoms_gmt_velocity_scale_spin_box_value_changed(double)` |

*... and 1 more connections.*


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ExportVelocityOptionsWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ExportVelocityOptionsWidget --body
python scripts/gpq.py uses ExportVelocityOptionsWidget --kind class
python scripts/gpq.py hier ExportVelocityOptionsWidget
```
