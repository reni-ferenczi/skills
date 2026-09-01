# RasterLayerOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 487 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/RasterLayerOptionsWidget.h` | C++ | 178 |
| `src/qt-widgets/RasterLayerOptionsWidget.cc` | C++ | 662 |
| `src/qt-widgets/RasterLayerOptionsWidgetUi.ui` | Qt form | 183 |

## Overview

[[[PROSE overview unit=qt-widgets/RasterLayerOptionsWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::RasterLayerOptionsWidget`](#gplatesqtwidgetsrasterlayeroptionswidget) | class | [`LayerOptionsWidget`](LayerOptionsWidget.md)<br>`Ui_RasterLayerOptionsWidget` | — | 0 | RasterLayerOptionsWidget is used to show additional options for raster layers in the visual layers widget. |

## Members

### `GPlatesQtWidgets::RasterLayerOptionsWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, ViewportWindow *viewport_window, QWidget *parent_)` | method | `LayerOptionsWidget` | public | — |
| `set_data( const boost::weak_ptr<GPlatesPresentation::VisualLayer> &visual_layer)` | method | `void` | public | — |
| `get_title` | field | `QString` | public | — |
| `handle_band_combobox_activated( const QString &text)` | method | `void` | private | — |
| `handle_select_palette_filename_button_clicked()` | method | `void` | private | — |
| `handle_use_default_palette_button_clicked()` | method | `void` | private | — |
| `handle_builtin_colour_palette_selected( const GPlatesGui::BuiltinColourPaletteType &builtin_colour_palette_type)` | method | `void` | private | — |
| `handle_builtin_parameters_changed( const GPlatesGui::BuiltinColourPaletteType::Parameters &builtin_parameters)` | method | `void` | private | — |
| `handle_palette_range_check_box_changed( int state)` | method | `void` | private | — |
| `handle_palette_min_line_editing_finished( double value)` | method | `void` | private | — |
| `handle_palette_max_line_editing_finished( double value)` | method | `void` | private | — |
| `handle_palette_range_restore_min_max_button_clicked()` | method | `void` | private | — |
| `handle_palette_range_restore_mean_deviation_button_clicked()` | method | `void` | private | — |
| `handle_palette_range_restore_mean_deviation_spinbox_changed( double value)` | method | `void` | private | — |
| `handle_opacity_spinbox_changed( double value)` | method | `void` | private | — |
| `handle_intensity_spinbox_changed( double value)` | method | `void` | private | — |
| `handle_surface_relief_scale_spinbox_changed( double value)` | method | `void` | private | — |
| `RasterLayerOptionsWidget( GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, ViewportWindow *viewport_window, QWidget *parent_)` | constructor | `None` | private | — |
| `get_raster_scalar_min_max( GPlatesAppLogic::Layer &layer)` | method | `std::pair<double, double>` | private | — |
| `get_raster_scalar_mean_std_dev( GPlatesAppLogic::Layer &layer)` | method | `std::pair<double, double>` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_viewport_window` | field | `ViewportWindow` | private | — |
| `d_open_file_dialog` | field | `OpenFileDialog` | private | — |
| `d_colour_palette_widget` | field | `RemappedColourPaletteWidget` | private | — |
| `d_current_visual_layer` | field | `boost::weak_ptr<GPlatesPresentation::VisualLayer>` | private | The visual layer for which we are currently displaying options. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_RASTERLAYEROPTIONSWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/RasterLayerOptionsWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/VisualLayerWidget](VisualLayerWidget.md) | qt-widgets | 11 |
| [presentation/VisualLayerRegistry](../presentation/VisualLayerRegistry.md) | presentation | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `RasterLayerOptionsWidget` | `QWidget` | Layers | 11 |

**Qt signal/slot connections** (17 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `band_combobox` | `activated(const QString &)` | `this` | `handle_band_combobox_activated(const QString &)` |
| `opacity_spinbox` | `valueChanged(double)` | `this` | `handle_opacity_spinbox_changed(double)` |
| `intensity_spinbox` | `valueChanged(double)` | `this` | `handle_intensity_spinbox_changed(double)` |
| `surface_relief_scale_spinbox` | `valueChanged(double)` | `this` | `handle_surface_relief_scale_spinbox_changed(double)` |
| `d_colour_palette_widget` | `select_palette_filename_button_clicked()` | `this` | `handle_select_palette_filename_button_clicked()` |
| `d_colour_palette_widget` | `use_default_palette_button_clicked()` | `this` | `handle_use_default_palette_button_clicked()` |
| `d_colour_palette_widget` | `builtin_colour_palette_selected(const GPlatesGui::BuiltinColourPaletteType &)` | `this` | `handle_builtin_colour_palette_selected(const GPlatesGui::BuiltinColourPaletteType &)` |
| `d_colour_palette_widget` | `builtin_parameters_changed(const GPlatesGui::BuiltinColourPaletteType::Parameters &)` | `this` | `handle_builtin_parameters_changed(const GPlatesGui::BuiltinColourPaletteType::Parameters &)` |
| `d_colour_palette_widget` | `range_check_box_changed(int)` | `this` | `handle_palette_range_check_box_changed(int)` |
| `d_colour_palette_widget` | `min_line_editing_finished(double)` | `this` | `handle_palette_min_line_editing_finished(double)` |
| `d_colour_palette_widget` | `max_line_editing_finished(double)` | `this` | `handle_palette_max_line_editing_finished(double)` |
| `d_colour_palette_widget` | `range_restore_min_max_button_clicked()` | `this` | `handle_palette_range_restore_min_max_button_clicked()` |
| `d_colour_palette_widget` | `range_restore_mean_deviation_button_clicked()` | `this` | `handle_palette_range_restore_mean_deviation_button_clicked()` |
| `d_colour_palette_widget` | `range_restore_mean_deviation_spinbox_changed(double)` | `this` | `handle_palette_range_restore_mean_deviation_spinbox_changed(double)` |
| `opacity_spinbox` | `valueChanged(double)` | `this` | `handle_opacity_spinbox_changed(double)` |

*... and 2 more connections.*


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/RasterLayerOptionsWidget.h
python scripts/gpq.py def GPlatesQtWidgets::RasterLayerOptionsWidget --body
python scripts/gpq.py uses RasterLayerOptionsWidget --kind class
python scripts/gpq.py hier RasterLayerOptionsWidget
```
