# ConfigureCanvasToolGeometryRenderParametersDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 879 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ConfigureCanvasToolGeometryRenderParametersDialog.h` | C++ | 118 |
| `src/qt-widgets/ConfigureCanvasToolGeometryRenderParametersDialog.cc` | C++ | 300 |
| `src/qt-widgets/ConfigureCanvasToolGeometryRenderParametersDialogUi.ui` | Qt form | 539 |

## Overview

Configures visual appearance of geometries rendered by interactive canvas tools. The dialog allows adjustment of point sizes, line widths, and colours for different geometry categories: focused/clicked features, topology network focus, topology sections, and reconstruction-layer geometries. It holds a reference to a `RenderedGeometryParameters` object and updates it when the user adjusts spinboxes or colour buttons, with two-way synchronization so external parameter changes update the UI.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ConfigureCanvasToolGeometryRenderParametersDialog`](#gplatesqtwidgetsconfigurecanvastoolgeometryrenderparametersdialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_ConfigureCanvasToolGeometryRenderParametersDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ConfigureCanvasToolGeometryRenderParametersDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ConfigureCanvasToolGeometryRenderParametersDialog( GPlatesViewOperations::RenderedGeometryParameters &rendered_geometry_parameters, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `react_focused_feature_clicked_geometry_colour_changed()` | method | `void` | private | — |
| `react_focused_feature_point_size_hint_spinbox_value_changed( double value)` | method | `void` | private | — |
| `react_focused_feature_line_width_hint_spinbox_value_changed( double value)` | method | `void` | private | — |
| `react_topology_focus_colour_changed()` | method | `void` | private | — |
| `react_topology_focus_point_size_hint_spinbox_value_changed( double value)` | method | `void` | private | — |
| `react_topology_focus_line_width_hint_spinbox_value_changed( double value)` | method | `void` | private | — |
| `react_topology_sections_colour_changed()` | method | `void` | private | — |
| `react_topology_sections_point_size_hint_spinbox_value_changed( double value)` | method | `void` | private | — |
| `react_topology_sections_line_width_hint_spinbox_value_changed( double value)` | method | `void` | private | — |
| `react_reconstruction_layer_point_size_hint_spinbox_value_changed( double value)` | method | `void` | private | — |
| `react_reconstruction_layer_line_width_hint_spinbox_value_changed( double value)` | method | `void` | private | — |
| `react_reconstruction_layer_topology_size_multiplier_spinbox_value_changed( double value)` | method | `void` | private | — |
| `handle_rendered_geometry_parameters_changed()` | method | `void` | private | — |
| `d_rendered_geometry_parameters` | field | `GPlatesViewOperations::RenderedGeometryParameters` | private | — |
| `d_focused_feature_clicked_geometry_colour_button` | field | `ChooseColourButton` | private | — |
| `d_topology_focus_colour_button` | field | `ChooseColourButton` | private | — |
| `d_topology_sections_colour_button` | field | `ChooseColourButton` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_CONFIGURECANVASTOOLGEOMETRYRENDERPARAMETERSDIALOG_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Dialogs](../gui/Dialogs.md) | gui | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ConfigureCanvasToolGeometryRenderParametersDialog` | `QDialog` | Configure Geometry Rendering | 34 |

**Qt signal/slot connections** (13 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_focused_feature_clicked_geometry_colour_button` | `colour_changed(GPlatesQtWidgets::ChooseColourButton &)` | `this` | `react_focused_feature_clicked_geometry_colour_changed()` |
| `focused_feature_point_size_hint_spinbox` | `valueChanged(double)` | `this` | `react_focused_feature_point_size_hint_spinbox_value_changed(double)` |
| `focused_feature_line_width_hint_spinbox` | `valueChanged(double)` | `this` | `react_focused_feature_line_width_hint_spinbox_value_changed(double)` |
| `d_topology_focus_colour_button` | `colour_changed(GPlatesQtWidgets::ChooseColourButton &)` | `this` | `react_topology_focus_colour_changed()` |
| `topology_focus_point_size_hint_spinbox` | `valueChanged(double)` | `this` | `react_topology_focus_point_size_hint_spinbox_value_changed(double)` |
| `topology_focus_line_width_hint_spinbox` | `valueChanged(double)` | `this` | `react_topology_focus_line_width_hint_spinbox_value_changed(double)` |
| `d_topology_sections_colour_button` | `colour_changed(GPlatesQtWidgets::ChooseColourButton &)` | `this` | `react_topology_sections_colour_changed()` |
| `topology_sections_point_size_hint_spinbox` | `valueChanged(double)` | `this` | `react_topology_sections_point_size_hint_spinbox_value_changed(double)` |
| `topology_sections_line_width_hint_spinbox` | `valueChanged(double)` | `this` | `react_topology_sections_line_width_hint_spinbox_value_changed(double)` |
| `reconstruction_layer_point_size_hint_spinbox` | `valueChanged(double)` | `this` | `react_reconstruction_layer_point_size_hint_spinbox_value_changed(double)` |
| `reconstruction_layer_line_width_hint_spinbox` | `valueChanged(double)` | `this` | `react_reconstruction_layer_line_width_hint_spinbox_value_changed(double)` |
| `reconstruction_layer_topology_size_multiplier_spinbox` | `valueChanged(double)` | `this` | `react_reconstruction_layer_topology_size_multiplier_spinbox_value_changed(double)` |
| `&d_rendered_geometry_parameters` | `parameters_changed(GPlatesViewOperations::RenderedGeometryParameters &)` | `this` | `handle_rendered_geometry_parameters_changed()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ConfigureCanvasToolGeometryRenderParametersDialog.h
python scripts/gpq.py def GPlatesQtWidgets::ConfigureCanvasToolGeometryRenderParametersDialog --body
python scripts/gpq.py uses ConfigureCanvasToolGeometryRenderParametersDialog --kind class
python scripts/gpq.py hier ConfigureCanvasToolGeometryRenderParametersDialog
```
