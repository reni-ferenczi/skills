# ExportDeformationOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 370 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ExportDeformationOptionsWidget.h` | C++ | 122 |
| `src/qt-widgets/ExportDeformationOptionsWidget.cc` | C++ | 455 |
| `src/qt-widgets/ExportDeformationOptionsWidgetUi.ui` | Qt form | 260 |

## Overview

`ExportDeformationOptionsWidget` is the options panel for exporting deformation data (strain and strain rate) from the reconstruction. It presents checkboxes for controlling which deformation components are included in the export (principal strain stretch, dilatation strain, dilatation strain rate, second invariant of strain rate, strain rate style).

The widget also supports format-specific options: for GMT output, the user can choose between lon/lat and lat/lon coordinate order. An embedded `ExportFileOptionsWidget` handles file naming and format selection. As the user toggles options, `update_output_description_label()` dynamically shows what will be exported.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ExportDeformationOptionsWidget`](#gplatesqtwidgetsexportdeformationoptionswidget) | class | [`ExportOptionsWidget`](ExportOptionsWidget.md)<br>`Ui_ExportDeformationOptionsWidget` | — | 0 | ExportDeformationOptionsWidget is used to show export options for exporting deformation info (such as strain). |

## Members

### `GPlatesQtWidgets::ExportDeformationOptionsWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( QWidget *parent, GPlatesGui::ExportAnimationContext &export_animation_context, const GPlatesGui::ExportDeformationAnimationStrategy::const_configuration_ptr &export_configuration)` | method | `ExportOptionsWidget` | public | Creates a ExportDeformationOptionsWidget containing default export options. |
| `create_export_animation_strategy_configuration( const QString &filename_template)` | method | `GPlatesGui::ExportAnimationStrategy::const_configuration_base_ptr` | public | Collects the options specified by the user and returns them as an export animation strategy configuration. |
| `react_gmt_domain_point_format_radio_button_toggled( bool checked)` | method | `void` | private | — |
| `react_include_principal_strain_check_box_clicked()` | method | `void` | private | — |
| `react_principal_output_radio_button_toggled( bool checked)` | method | `void` | private | — |
| `react_principal_angle_radio_button_toggled( bool checked)` | method | `void` | private | — |
| `react_include_dilatation_strain_check_box_clicked()` | method | `void` | private | — |
| `react_include_dilatation_strain_rate_check_box_clicked()` | method | `void` | private | — |
| `react_include_second_invariant_strain_rate_check_box_clicked()` | method | `void` | private | — |
| `react_include_strain_rate_style_check_box_clicked()` | method | `void` | private | — |
| `ExportDeformationOptionsWidget( QWidget *parent_, const GPlatesGui::ExportDeformationAnimationStrategy::const_configuration_ptr &export_configuration)` | constructor | `None` | private | — |
| `make_signal_slot_connections()` | method | `void` | private | — |
| `update_output_description_label()` | method | `void` | private | — |
| `d_export_configuration` | field | `GPlatesGui::ExportDeformationAnimationStrategy::configuration_ptr` | private | — |
| `d_export_file_options_widget` | field | `ExportFileOptionsWidget` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QT_WIDGETS_EXPORTDEFORMATIONOPTIONSWIDGET_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportAnimationRegistry](../gui/ExportAnimationRegistry.md) | gui | 3 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ExportDeformationOptionsWidget` | `QWidget` | Form | 22 |

**Qt signal/slot connections** (11 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `include_principal_strain_stretch_check_box` | `stateChanged(int)` | `this` | `react_include_principal_strain_check_box_clicked()` |
| `include_dilatation_strain_check_box` | `stateChanged(int)` | `this` | `react_include_dilatation_strain_check_box_clicked()` |
| `include_dilatation_strain_rate_check_box` | `stateChanged(int)` | `this` | `react_include_dilatation_strain_rate_check_box_clicked()` |
| `include_second_invariant_strain_rate_check_box` | `stateChanged(int)` | `this` | `react_include_second_invariant_strain_rate_check_box_clicked()` |
| `include_strain_rate_style_check_box` | `stateChanged(int)` | `this` | `react_include_strain_rate_style_check_box_clicked()` |
| `principal_output_strain_radio_button` | `toggled(bool)` | `this` | `react_principal_output_radio_button_toggled(bool)` |
| `principal_output_stretch_radio_button` | `toggled(bool)` | `this` | `react_principal_output_radio_button_toggled(bool)` |
| `principal_angle_major_minor_radio_button` | `toggled(bool)` | `this` | `react_principal_angle_radio_button_toggled(bool)` |
| `principal_azimuth_major_minor_radio_button` | `toggled(bool)` | `this` | `react_principal_angle_radio_button_toggled(bool)` |
| `gmt_lon_lat_radio_button` | `toggled(bool)` | `this` | `react_gmt_domain_point_format_radio_button_toggled(bool)` |
| `gmt_lat_lon_radio_button` | `toggled(bool)` | `this` | `react_gmt_domain_point_format_radio_button_toggled(bool)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ExportDeformationOptionsWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ExportDeformationOptionsWidget --body
python scripts/gpq.py uses ExportDeformationOptionsWidget --kind class
python scripts/gpq.py hier ExportDeformationOptionsWidget
```
