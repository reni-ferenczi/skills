# ExportRasterOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 334 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ExportRasterOptionsWidget.h` | C++ | 125 |
| `src/qt-widgets/ExportRasterOptionsWidget.cc` | C++ | 388 |
| `src/qt-widgets/ExportRasterOptionsWidgetUi.ui` | Qt form | 547 |

## Overview

A form-based widget for configuring raster (colour or numerical) export options. Users specify resolution (in degrees), geographic extents (top, bottom, left, right latitude/longitude), choice of pixel or grid-line registration, and optional compression. The widget automatically updates displayed raster dimensions as extents and resolution change, using the `get_export_raster_parameters()` helper to compute width and height. Collected options are packaged as `ExportRasterAnimationStrategy::Configuration`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ExportRasterOptionsWidget`](#gplatesqtwidgetsexportrasteroptionswidget) | class | [`ExportOptionsWidget`](ExportOptionsWidget.md)<br>`Ui_ExportRasterOptionsWidget` | — | 0 | Raster (colour or numerical) export options. |

## Members

### `GPlatesQtWidgets::ExportRasterOptionsWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( QWidget *parent, GPlatesGui::ExportAnimationContext &export_animation_context, const GPlatesGui::ExportRasterAnimationStrategy::const_configuration_ptr & export_configuration)` | method | `ExportOptionsWidget` | public | Creates a ExportRasterOptionsWidget containing default export options. |
| `create_export_animation_strategy_configuration( const QString &filename_template)` | method | `GPlatesGui::ExportAnimationStrategy::const_configuration_base_ptr` | public | Collects the options specified by the user and returns them as an export animation strategy configuration. |
| `react_resolution_spin_box_value_changed( double value)` | method | `void` | private | — |
| `react_top_extents_spin_box_value_changed( double value)` | method | `void` | private | — |
| `react_bottom_extents_spin_box_value_changed( double value)` | method | `void` | private | — |
| `react_left_extents_spin_box_value_changed( double value)` | method | `void` | private | — |
| `react_right_extents_spin_box_value_changed( double value)` | method | `void` | private | — |
| `handle_grid_line_registration_checkbox_state_changed( int state)` | method | `void` | private | — |
| `react_use_global_extents_button_clicked()` | method | `void` | private | — |
| `react_enable_compression_check_box_clicked()` | method | `void` | private | — |
| `ExportRasterOptionsWidget( QWidget *parent_, const GPlatesGui::ExportRasterAnimationStrategy::const_configuration_ptr & export_configuration)` | constructor | `None` | private | — |
| `make_signal_slot_connections()` | method | `void` | private | — |
| `update_raster_dimensions()` | method | `void` | private | — |
| `d_export_configuration` | field | `GPlatesGui::ExportRasterAnimationStrategy::Configuration` | private | — |
| `d_help_grid_line_registration_dialog` | field | `GPlatesQtWidgets::InformationDialog` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `HELP_GRID_LINE_REGISTRATION_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_GRID_LINE_REGISTRATION_DIALOG_TEXT` | variable | `QString` | — |
| `get_export_raster_parameters( const double &top_extents, const double &bottom_extents, const double &left_extents, const double &right_extents, const double &raster_resolution_in_degrees, bool use_grid_line_registration)` | function | `std::pair<unsigned int/*raster_width*/, unsigned int/*raster_height*/>` | Calculates the export raster dimensions from resolution and lat/lon extents. |
| `GPLATES_QT_WIDGETS_EXPORTRASTEROPTIONSWIDGET_H` | macro | `None` | — |

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
| `ExportRasterOptionsWidget` | `QWidget` | Form | 33 |

**Qt signal/slot connections** (13 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `push_button_help_grid_line_registration` | `clicked()` | `d_help_grid_line_registration_dialog` | `show()` |
| `resolution_spin_box` | `valueChanged(double)` | `this` | `react_resolution_spin_box_value_changed(double)` |
| `top_extents_spinbox` | `valueChanged(double)` | `this` | `react_top_extents_spin_box_value_changed(double)` |
| `bottom_extents_spinbox` | `valueChanged(double)` | `this` | `react_bottom_extents_spin_box_value_changed(double)` |
| `left_extents_spinbox` | `valueChanged(double)` | `this` | `react_left_extents_spin_box_value_changed(double)` |
| `right_extents_spinbox` | `valueChanged(double)` | `this` | `react_right_extents_spin_box_value_changed(double)` |
| `grid_line_registration_checkbox` | `stateChanged(int)` | `this` | `handle_grid_line_registration_checkbox_state_changed(int)` |
| `use_global_extents_button` | `clicked()` | `this` | `react_use_global_extents_button_clicked()` |
| `enable_compression_checkbox` | `stateChanged(int)` | `this` | `react_enable_compression_check_box_clicked()` |
| `right_extents_spinbox` | `valueChanged(double)` | `this` | `react_right_extents_spin_box_value_changed(double)` |
| `right_extents_spinbox` | `valueChanged(double)` | `this` | `react_right_extents_spin_box_value_changed(double)` |
| `left_extents_spinbox` | `valueChanged(double)` | `this` | `react_left_extents_spin_box_value_changed(double)` |
| `left_extents_spinbox` | `valueChanged(double)` | `this` | `react_left_extents_spin_box_value_changed(double)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ExportRasterOptionsWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ExportRasterOptionsWidget --body
python scripts/gpq.py uses ExportRasterOptionsWidget --kind class
python scripts/gpq.py hier ExportRasterOptionsWidget
```
