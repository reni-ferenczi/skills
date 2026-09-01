# TopologyNetworkResolverLayerOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 86 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/TopologyNetworkResolverLayerOptionsWidget.h` | C++ | 276 |
| `src/qt-widgets/TopologyNetworkResolverLayerOptionsWidget.cc` | C++ | 1748 |
| `src/qt-widgets/TopologyNetworkResolverLayerOptionsWidgetUi.ui` | Qt form | 1259 |

## Overview

[[[PROSE overview unit=qt-widgets/TopologyNetworkResolverLayerOptionsWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::TopologyNetworkResolverLayerOptionsWidget`](#gplatesqtwidgetstopologynetworkresolverlayeroptionswidget) | class | [`LayerOptionsWidget`](LayerOptionsWidget.md)<br>`Ui_TopologyNetworkResolverLayerOptionsWidget` | — | 0 | TopologyNetworkResolverLayerOptionsWidget is used to show additional options for topology network layers in the visual layers widget. |

## Members

### `GPlatesQtWidgets::TopologyNetworkResolverLayerOptionsWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, ViewportWindow *viewport_window, QWidget *parent_)` | method | `LayerOptionsWidget` | public | — |
| `set_data( const boost::weak_ptr<GPlatesPresentation::VisualLayer> &visual_layer)` | method | `void` | public | — |
| `get_title` | field | `QString` | public | — |
| `handle_strain_rate_smoothing_button( bool checked)` | method | `void` | private | — |
| `handle_strain_rate_clamping_clicked()` | method | `void` | private | — |
| `handle_strain_rate_clamping_line_editing_finished()` | method | `void` | private | — |
| `handle_rift_exponential_stretching_constant_line_editing_finished()` | method | `void` | private | — |
| `handle_rift_strain_rate_resolution_line_editing_finished()` | method | `void` | private | — |
| `handle_rift_edge_length_threshold_line_editing_finished()` | method | `void` | private | — |
| `handle_fill_rigid_blocks_clicked()` | method | `void` | private | — |
| `handle_segment_velocity_clicked()` | method | `void` | private | — |
| `handle_colour_mode_button( bool checked)` | method | `void` | private | — |
| `handle_draw_mode_button( bool checked)` | method | `void` | private | — |
| `handle_min_abs_dilatation_spinbox_changed( double min_abs_dilatation)` | method | `void` | private | — |
| `handle_max_abs_dilatation_spinbox_changed( double max_abs_dilatation)` | method | `void` | private | — |
| `handle_select_dilatation_palette_filename_button_clicked()` | method | `void` | private | — |
| `handle_use_default_dilatation_palette_button_clicked()` | method | `void` | private | — |
| `handle_min_abs_second_invariant_spinbox_changed( double min_abs_second_invariant)` | method | `void` | private | — |
| `handle_max_abs_second_invariant_spinbox_changed( double max_abs_second_invariant)` | method | `void` | private | — |
| `handle_select_second_invariant_palette_filename_button_clicked()` | method | `void` | private | — |
| `handle_use_default_second_invariant_palette_button_clicked()` | method | `void` | private | — |
| `handle_min_strain_rate_style_spinbox_changed( double min_strain_rate_style)` | method | `void` | private | — |
| `handle_max_strain_rate_style_spinbox_changed( double max_strain_rate_style)` | method | `void` | private | — |
| `handle_select_strain_rate_style_palette_filename_button_clicked()` | method | `void` | private | — |
| `handle_use_default_strain_rate_style_palette_button_clicked()` | method | `void` | private | — |
| `handle_fill_opacity_spinbox_changed( double value)` | method | `void` | private | — |
| `handle_fill_intensity_spinbox_changed( double value)` | method | `void` | private | — |
| `open_draw_style_setting_dlg()` | method | `void` | private | — |
| `DoubleValidator` | class | `None` | private | Fixes up any QValidator::Intermediate input (only when user editing has finished) so that we always get a valid result (when user editing has finished) and hence always get an 'editingFinished()' signal to process/finalise the user input ... |
| `TopologyNetworkResolverLayerOptionsWidget( GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, ViewportWindow *viewport_window, QWidget *parent_)` | constructor | `None` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_viewport_window` | field | `ViewportWindow` | private | — |
| `d_draw_style_dialog_ptr` | field | `DrawStyleDialog` | private | — |
| `d_open_file_dialog` | field | `OpenFileDialog` | private | — |
| `d_clamp_strain_rate_line_edit_double_validator` | field | `QDoubleValidator` | private | — |
| `d_rift_strain_rate_resolution_line_edit_double_validator` | field | `QDoubleValidator` | private | — |
| `d_rift_exponential_stretching_constant_line_edit_double_validator` | field | `QDoubleValidator` | private | — |
| `d_rift_edge_length_threshold_line_edit_double_validator` | field | `QDoubleValidator` | private | — |
| `d_dilatation_palette_filename_lineedit` | field | `FriendlyLineEdit` | private | — |
| `d_dilatation_colour_scale_widget` | field | `ColourScaleWidget` | private | — |
| `d_second_invariant_palette_filename_lineedit` | field | `FriendlyLineEdit` | private | — |
| `d_second_invariant_colour_scale_widget` | field | `ColourScaleWidget` | private | — |
| `d_strain_rate_style_palette_filename_lineedit` | field | `FriendlyLineEdit` | private | — |
| `d_strain_rate_style_colour_scale_widget` | field | `ColourScaleWidget` | private | — |
| `d_current_visual_layer` | field | `boost::weak_ptr<GPlatesPresentation::VisualLayer>` | private | The visual layer for which we are currently displaying options. |
| `d_help_strain_rate_smoothing_dialog` | field | `GPlatesQtWidgets::InformationDialog` | private | — |
| `d_help_strain_rate_clamping_dialog` | field | `GPlatesQtWidgets::InformationDialog` | private | — |
| `d_help_rift_exponential_stretching_constant_dialog` | field | `GPlatesQtWidgets::InformationDialog` | private | — |
| `d_help_rift_strain_rate_resolution_dialog` | field | `GPlatesQtWidgets::InformationDialog` | private | — |
| `d_help_rift_edge_length_threshold_dialog` | field | `GPlatesQtWidgets::InformationDialog` | private | — |
| `d_help_triangulation_colour_mode_dialog` | field | `GPlatesQtWidgets::InformationDialog` | private | — |
| `d_help_triangulation_draw_mode_dialog` | field | `GPlatesQtWidgets::InformationDialog` | private | — |
| `STRAIN_RATE_SCALE` | field | `double` | private | Used to scale min/max strain rate values into their spinboxes. |
| `SCALED_STRAIN_RATE_MIN` | field | `double` | private | Min/max range for scaled strain rate values. |
| `SCALED_STRAIN_RATE_MAX` | field | `double` | private | — |
| `SCALED_STRAIN_RATE_DECIMAL_PLACES` | field | `int` | private | Number of decimal places for scaled strain rate values. |
| `RIFT_EXPONENTIAL_STRETCHING_CONSTANT_DECIMAL_PLACES` | field | `int` | private | Number of decimal places for rift exponential stretching constant values. |
| `RIFT_EDGE_LENGTH_THRESHOLD_DECIMAL_PLACES` | field | `int` | private | Number of decimal places for rift edge length threshold values. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `HELP_STRAIN_RATE_SMOOTHING_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_STRAIN_RATE_SMOOTHING_DIALOG_TEXT` | variable | `QString` | — |
| `HELP_STRAIN_RATE_CLAMPING_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_STRAIN_RATE_CLAMPING_DIALOG_TEXT` | variable | `QString` | — |
| `HELP_RIFT_EXPONENTIAL_STRETCHING_CONSTANT_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_RIFT_EXPONENTIAL_STRETCHING_CONSTANT_DIALOG_TEXT` | variable | `QString` | — |
| `HELP_RIFT_STRAIN_RATE_RESOLUTION_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_RIFT_STRAIN_RATE_RESOLUTION_DIALOG_TEXT` | variable | `QString` | — |
| `HELP_RIFT_EDGE_LENGTH_THRESHOLD_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_RIFT_EDGE_LENGTH_THRESHOLD_DIALOG_TEXT` | variable | `QString` | — |
| `HELP_TRIANGULATION_COLOUR_MODE_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_TRIANGULATION_COLOUR_MODE_DIALOG_TEXT` | variable | `QString` | — |
| `HELP_TRIANGULATION_DRAW_MODE_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_TRIANGULATION_DRAW_MODE_DIALOG_TEXT` | variable | `QString` | — |
| `STRAIN_RATE_SCALE` | variable | `double` | — |
| `SCALED_STRAIN_RATE_MIN` | variable | `double` | — |
| `SCALED_STRAIN_RATE_MAX` | variable | `double` | — |
| `SCALED_STRAIN_RATE_DECIMAL_PLACES` | variable | `int` | — |
| `RIFT_EXPONENTIAL_STRETCHING_CONSTANT_DECIMAL_PLACES` | variable | `int` | — |
| `RIFT_EDGE_LENGTH_THRESHOLD_DECIMAL_PLACES` | variable | `int` | — |
| `GPLATES_QTWIDGETS_TOPOLOGYNETWORKRESOLVERLAYEROPTIONSWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/TopologyNetworkResolverLayerOptionsWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/VisualLayerRegistry](../presentation/VisualLayerRegistry.md) | presentation | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `TopologyNetworkResolverLayerOptionsWidget` | `QWidget` | Layers | 82 |

**Qt signal/slot connections** (61 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `no_smoothing_radio_button` | `toggled(bool)` | `this` | `handle_strain_rate_smoothing_button(bool)` |
| `barycentric_radio_button` | `toggled(bool)` | `this` | `handle_strain_rate_smoothing_button(bool)` |
| `natural_neighbour_radio_button` | `toggled(bool)` | `this` | `handle_strain_rate_smoothing_button(bool)` |
| `push_button_help_strain_rate_smoothing` | `clicked()` | `d_help_strain_rate_smoothing_dialog` | `show()` |
| `enable_clamping_checkbox` | `clicked()` | `this` | `handle_strain_rate_clamping_clicked()` |
| `clamp_strain_rate_line_edit` | `editingFinished()` | `this` | `handle_strain_rate_clamping_line_editing_finished()` |
| `push_button_help_strain_rate_clamping` | `clicked()` | `d_help_strain_rate_clamping_dialog` | `show()` |
| `rift_exponential_stretching_constant_line_edit` | `editingFinished()` | `this` | `handle_rift_exponential_stretching_constant_line_editing_finished()` |
| `push_button_help_rift_exponential_stretching_constant` | `clicked()` | `d_help_rift_exponential_stretching_constant_dialog` | `show()` |
| `rift_strain_rate_resolution_line_edit` | `editingFinished()` | `this` | `handle_rift_strain_rate_resolution_line_editing_finished()` |
| `push_button_help_rift_strain_rate_resolution` | `clicked()` | `d_help_rift_strain_rate_resolution_dialog` | `show()` |
| `rift_edge_length_threshold_line_edit` | `editingFinished()` | `this` | `handle_rift_edge_length_threshold_line_editing_finished()` |
| `push_button_help_rift_edge_length_threshold` | `clicked()` | `d_help_rift_edge_length_threshold_dialog` | `show()` |
| `dilatation_radio_button` | `toggled(bool)` | `this` | `handle_colour_mode_button(bool)` |
| `second_invariant_radio_button` | `toggled(bool)` | `this` | `handle_colour_mode_button(bool)` |

*... and 46 more connections.*


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/TopologyNetworkResolverLayerOptionsWidget.h
python scripts/gpq.py def GPlatesQtWidgets::TopologyNetworkResolverLayerOptionsWidget --body
python scripts/gpq.py uses TopologyNetworkResolverLayerOptionsWidget --kind class
python scripts/gpq.py hier TopologyNetworkResolverLayerOptionsWidget
```
