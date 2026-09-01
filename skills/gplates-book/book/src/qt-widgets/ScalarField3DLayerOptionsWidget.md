# ScalarField3DLayerOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 126 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ScalarField3DLayerOptionsWidget.h` | C++ | 306 |
| `src/qt-widgets/ScalarField3DLayerOptionsWidget.cc` | C++ | 3381 |
| `src/qt-widgets/ScalarField3DLayerOptionsWidgetUi.ui` | Qt form | 2274 |

## Overview

A `LayerOptionsWidget` that lets users adjust rendering parameters for 3D scalar field layers in the visual layers dock. Controls include choosing between isosurface and cross-section render modes, setting deviation windows and color schemes, adjusting opacity and depth restrictions, and configuring quality–performance trade-offs. The widget manages scalar-value and gradient-magnitude color palettes with custom range scaling, and updates itself when switching between layers via `set_data()`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ScalarField3DLayerOptionsWidget`](#gplatesqtwidgetsscalarfield3dlayeroptionswidget) | class | [`LayerOptionsWidget`](LayerOptionsWidget.md)<br>`Ui_ScalarField3DLayerOptionsWidget` | — | 0 | ScalarField3DLayerOptionsWidget is used to show additional options for 3D scalar field layers in the visual layers widget. |

## Members

### `GPlatesQtWidgets::ScalarField3DLayerOptionsWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, ViewportWindow *viewport_window, QWidget *parent_)` | method | `LayerOptionsWidget` | public | — |
| `set_data( const boost::weak_ptr<GPlatesPresentation::VisualLayer> &visual_layer)` | method | `void` | public | — |
| `get_title` | field | `QString` | public | — |
| `~ScalarField3DLayerOptionsWidget()` | destructor | `None` | public | — |
| `handle_render_mode_button( bool checked)` | method | `void` | private | — |
| `handle_isosurface_deviation_window_mode_button( bool checked)` | method | `void` | private | — |
| `handle_isosurface_colour_mode_button( bool checked)` | method | `void` | private | — |
| `handle_cross_sections_colour_mode_button( bool checked)` | method | `void` | private | — |
| `handle_select_scalar_palette_filename_button_clicked()` | method | `void` | private | — |
| `handle_use_default_scalar_palette_button_clicked()` | method | `void` | private | — |
| `handle_builtin_scalar_colour_palette_selected( const GPlatesGui::BuiltinColourPaletteType &builtin_scalar_colour_palette_type)` | method | `void` | private | — |
| `handle_builtin_scalar_parameters_changed( const GPlatesGui::BuiltinColourPaletteType::Parameters &builtin_scalar_parameters)` | method | `void` | private | — |
| `handle_scalar_palette_range_check_box_changed( int state)` | method | `void` | private | — |
| `handle_scalar_palette_min_line_editing_finished( double value)` | method | `void` | private | — |
| `handle_scalar_palette_max_line_editing_finished( double value)` | method | `void` | private | — |
| `handle_scalar_palette_range_restore_min_max_button_clicked()` | method | `void` | private | — |
| `handle_scalar_palette_range_restore_mean_deviation_button_clicked()` | method | `void` | private | — |
| `handle_scalar_palette_range_restore_mean_deviation_spinbox_changed( double value)` | method | `void` | private | — |
| `handle_select_gradient_palette_filename_button_clicked()` | method | `void` | private | — |
| `handle_use_default_gradient_palette_button_clicked()` | method | `void` | private | — |
| `handle_builtin_gradient_colour_palette_selected( const GPlatesGui::BuiltinColourPaletteType &builtin_gradient_colour_palette_type)` | method | `void` | private | — |
| `handle_builtin_gradient_parameters_changed( const GPlatesGui::BuiltinColourPaletteType::Parameters &builtin_gradient_parameters)` | method | `void` | private | — |
| `handle_gradient_palette_range_check_box_changed( int state)` | method | `void` | private | — |
| `handle_gradient_palette_min_line_editing_finished( double value)` | method | `void` | private | — |
| `handle_gradient_palette_max_line_editing_finished( double value)` | method | `void` | private | — |
| `handle_gradient_palette_range_restore_min_max_button_clicked()` | method | `void` | private | — |
| `handle_gradient_palette_range_restore_mean_deviation_button_clicked()` | method | `void` | private | — |
| `handle_gradient_palette_range_restore_mean_deviation_spinbox_changed( double value)` | method | `void` | private | — |
| `handle_isovalue_spinbox_changed( double isovalue)` | method | `void` | private | — |
| `handle_isovalue_slider_changed( int value)` | method | `void` | private | — |
| `handle_deviation_spinbox_changed( double deviation)` | method | `void` | private | — |
| `handle_symmetric_deviation_spinbox_changed( double symmetric_deviation)` | method | `void` | private | — |
| `handle_symmetric_deviation_check_box_changed()` | method | `void` | private | — |
| `handle_opacity_deviation_surfaces_spinbox_changed( double opacity)` | method | `void` | private | — |
| `handle_volume_render_deviation_window_check_box_changed()` | method | `void` | private | — |
| `handle_opacity_deviation_volume_rendering_spinbox_changed( double opacity)` | method | `void` | private | — |
| `handle_surface_deviation_window_check_box_changed()` | method | `void` | private | — |
| `handle_isoline_frequency_spinbox_changed( int frequency)` | method | `void` | private | — |
| `handle_surface_polygons_mask_check_box_changed()` | method | `void` | private | — |
| `handle_depth_restriction_spinbox_changed( double value)` | method | `void` | private | — |
| `handle_restore_actual_depth_range_button_clicked()` | method | `void` | private | — |
| `handle_quality_performance_spinbox_changed( int value)` | method | `void` | private | — |
| `handle_improve_performance_during_globe_rotation_check_box_changed()` | method | `void` | private | — |
| `handle_test_variable_spinbox_changed( double value)` | method | `void` | private | — |
| `ScalarField3DLayerOptionsWidget( GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, ViewportWindow *viewport_window, QWidget *parent_)` | constructor | `None` | private | — |
| `enable_disable_options_for_visual_layer_params( const GPlatesViewOperations::ScalarField3DRenderParameters &scalar_field_render_parameters)` | method | `void` | private | — |
| `get_scalar_value_min_max( GPlatesAppLogic::Layer &layer)` | method | `std::pair<double, double>` | private | — |
| `get_scalar_value_mean_std_dev( GPlatesAppLogic::Layer &layer)` | method | `std::pair<double, double>` | private | — |
| `get_gradient_magnitude_min_max( GPlatesAppLogic::Layer &layer)` | method | `std::pair<double, double>` | private | — |
| `get_gradient_magnitude_mean_std_dev( GPlatesAppLogic::Layer &layer)` | method | `std::pair<double, double>` | private | — |
| `get_slider_isovalue( const double &iso_value, GPlatesAppLogic::Layer &layer, QSlider *isovalue_slider)` | method | `int` | private | — |
| `get_depth_min_max( GPlatesAppLogic::Layer &layer)` | method | `std::pair<double, double>` | private | — |
| `NUM_SHADER_TEST_VARIABLES` | field | `unsigned int` | private | The number of QDoubleSpinBox's used for shader test variables. |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_viewport_window` | field | `ViewportWindow` | private | — |
| `d_open_file_dialog` | field | `OpenFileDialog` | private | — |
| `d_scalar_colour_palette_widget` | field | `RemappedColourPaletteWidget` | private | — |
| `d_gradient_colour_palette_widget` | field | `RemappedColourPaletteWidget` | private | — |
| `d_shader_test_variables` | field | `std::vector<float>` | private | — |
| `d_current_visual_layer` | field | `boost::weak_ptr<GPlatesPresentation::VisualLayer>` | private | The visual layer for which we are currently displaying options. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `HIDE_SHADER_TEST_VARIABLE_CONTROLS` | macro | `None` | Define this to hide the GUI controls that change the shader test variables. |
| `GPLATES_QTWIDGETS_SCALARFIELD3DLAYEROPTIONSWIDGET_H` | macro | `None` | — |

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
| `ScalarField3DLayerOptionsWidget` | `QWidget` | — | 134 |

**Qt signal/slot connections** (131 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `isosurface_render_mode_button` | `toggled(bool)` | `this` | `handle_render_mode_button(bool)` |
| `cross_sections_render_mode_button` | `toggled(bool)` | `this` | `handle_render_mode_button(bool)` |
| `no_deviation_window_mode_button` | `toggled(bool)` | `this` | `handle_isosurface_deviation_window_mode_button(bool)` |
| `single_deviation_window_mode_button` | `toggled(bool)` | `this` | `handle_isosurface_deviation_window_mode_button(bool)` |
| `double_deviation_window_mode_button` | `toggled(bool)` | `this` | `handle_isosurface_deviation_window_mode_button(bool)` |
| `isosurface_depth_colour_mode_button` | `toggled(bool)` | `this` | `handle_isosurface_colour_mode_button(bool)` |
| `isosurface_scalar_colour_mode_button` | `toggled(bool)` | `this` | `handle_isosurface_colour_mode_button(bool)` |
| `isosurface_gradient_colour_mode_button` | `toggled(bool)` | `this` | `handle_isosurface_colour_mode_button(bool)` |
| `cross_sections_scalar_colour_mode_button` | `toggled(bool)` | `this` | `handle_cross_sections_colour_mode_button(bool)` |
| `cross_sections_gradient_colour_mode_button` | `toggled(bool)` | `this` | `handle_cross_sections_colour_mode_button(bool)` |
| `d_scalar_colour_palette_widget` | `select_palette_filename_button_clicked()` | `this` | `handle_select_scalar_palette_filename_button_clicked()` |
| `d_scalar_colour_palette_widget` | `use_default_palette_button_clicked()` | `this` | `handle_use_default_scalar_palette_button_clicked()` |
| `d_scalar_colour_palette_widget` | `builtin_colour_palette_selected(const GPlatesGui::BuiltinColourPaletteType &)` | `this` | `handle_builtin_scalar_colour_palette_selected(const GPlatesGui::BuiltinColourPaletteType &)` |
| `d_scalar_colour_palette_widget` | `builtin_parameters_changed(const GPlatesGui::BuiltinColourPaletteType::Parameters &)` | `this` | `handle_builtin_scalar_parameters_changed(const GPlatesGui::BuiltinColourPaletteType::Parameters &)` |
| `d_scalar_colour_palette_widget` | `range_check_box_changed(int)` | `this` | `handle_scalar_palette_range_check_box_changed(int)` |

*... and 116 more connections.*


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ScalarField3DLayerOptionsWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ScalarField3DLayerOptionsWidget --body
python scripts/gpq.py uses ScalarField3DLayerOptionsWidget --kind class
python scripts/gpq.py hier ScalarField3DLayerOptionsWidget
```
