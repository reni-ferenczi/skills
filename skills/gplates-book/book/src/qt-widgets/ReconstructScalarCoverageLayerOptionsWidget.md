# ReconstructScalarCoverageLayerOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 655 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ReconstructScalarCoverageLayerOptionsWidget.h` | C++ | 160 |
| `src/qt-widgets/ReconstructScalarCoverageLayerOptionsWidget.cc` | C++ | 553 |
| `src/qt-widgets/ReconstructScalarCoverageLayerOptionsWidgetUi.ui` | Qt form | 63 |

## Overview

[[[PROSE overview unit=qt-widgets/ReconstructScalarCoverageLayerOptionsWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ReconstructScalarCoverageLayerOptionsWidget`](#gplatesqtwidgetsreconstructscalarcoveragelayeroptionswidget) | class | [`LayerOptionsWidget`](LayerOptionsWidget.md)<br>`Ui_ReconstructScalarCoverageLayerOptionsWidget` | — | 0 | ReconstructScalarCoverageLayerOptionsWidget is used to show additional options for reconstructing scalar coverages (geometries with scalars) in the visual layers widget. |

## Members

### `GPlatesQtWidgets::ReconstructScalarCoverageLayerOptionsWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, ViewportWindow *viewport_window, QWidget *parent_)` | method | `LayerOptionsWidget` | public | — |
| `set_data( const boost::weak_ptr<GPlatesPresentation::VisualLayer> &visual_layer)` | method | `void` | public | — |
| `get_title` | field | `QString` | public | — |
| `handle_scalar_type_combobox_activated( const QString &text)` | method | `void` | private | — |
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
| `ReconstructScalarCoverageLayerOptionsWidget( GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, ViewportWindow *viewport_window, QWidget *parent_)` | constructor | `None` | private | — |
| `get_scalar_min_max( GPlatesAppLogic::Layer &layer)` | method | `std::pair<double, double>` | private | — |
| `get_scalar_mean_std_dev( GPlatesAppLogic::Layer &layer)` | method | `std::pair<double, double>` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_viewport_window` | field | `ViewportWindow` | private | — |
| `d_open_file_dialog` | field | `OpenFileDialog` | private | — |
| `d_colour_palette_widget` | field | `RemappedColourPaletteWidget` | private | — |
| `d_current_visual_layer` | field | `boost::weak_ptr<GPlatesPresentation::VisualLayer>` | private | The visual layer for which we are currently displaying options. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QT_WIDGETS_RECONSTRUCTSCALARCOVERAGELAYEROPTIONSWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ReconstructScalarCoverageLayerOptionsWidget tier=3]]]
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
| `ReconstructScalarCoverageLayerOptionsWidget` | `QWidget` | Layers | 5 |

**Qt signal/slot connections** (11 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `scalar_type_combobox` | `activated(const QString &)` | `this` | `handle_scalar_type_combobox_activated(const QString &)` |
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


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ReconstructScalarCoverageLayerOptionsWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ReconstructScalarCoverageLayerOptionsWidget --body
python scripts/gpq.py uses ReconstructScalarCoverageLayerOptionsWidget --kind class
python scripts/gpq.py hier ReconstructScalarCoverageLayerOptionsWidget
```
