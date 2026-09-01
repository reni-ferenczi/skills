# ReconstructLayerOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 593 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ReconstructLayerOptionsWidget.h` | C++ | 139 |
| `src/qt-widgets/ReconstructLayerOptionsWidget.cc` | C++ | 488 |
| `src/qt-widgets/ReconstructLayerOptionsWidgetUi.ui` | Qt form | 220 |

## Overview

[[[PROSE overview unit=qt-widgets/ReconstructLayerOptionsWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ReconstructLayerOptionsWidget`](#gplatesqtwidgetsreconstructlayeroptionswidget) | class | [`LayerOptionsWidget`](LayerOptionsWidget.md)<br>`Ui_ReconstructLayerOptionsWidget` | — | 0 | ReconstructLayerOptionsWidget is used to show additional options for reconstructed geometry layers in the visual layers widget. |

## Members

### `GPlatesQtWidgets::ReconstructLayerOptionsWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, ViewportWindow *viewport_window, QWidget *parent_)` | method | `LayerOptionsWidget` | public | — |
| `~ReconstructLayerOptionsWidget()` | destructor | `None` | public | — |
| `set_data( const boost::weak_ptr<GPlatesPresentation::VisualLayer> &visual_layer)` | method | `void` | public | — |
| `get_title` | field | `QString` | public | — |
| `open_vgp_visibility_dialog()` | method | `void` | private | — |
| `open_topology_reconstruction_parameters_dialog()` | method | `bool` | private | — |
| `open_draw_style_setting_dlg()` | method | `void` | private | — |
| `handle_use_topologies_button( bool checked)` | method | `void` | private | — |
| `handle_prompt_set_topology_reconstruction_parameters_clicked()` | method | `void` | private | — |
| `handle_fill_polygons_clicked()` | method | `void` | private | — |
| `handle_fill_polylines_clicked()` | method | `void` | private | — |
| `handle_fill_opacity_spinbox_changed( double value)` | method | `void` | private | — |
| `handle_fill_intensity_spinbox_changed( double value)` | method | `void` | private | — |
| `ReconstructLayerOptionsWidget( GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, ViewportWindow *viewport_window, QWidget *parent_)` | constructor | `None` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_viewport_window` | field | `ViewportWindow` | private | — |
| `d_set_vgp_visibility_dialog` | field | `SetVGPVisibilityDialog` | private | — |
| `d_set_topology_reconstruction_parameters_dialog` | field | `SetTopologyReconstructionParametersDialog` | private | — |
| `d_draw_style_dialog_ptr` | field | `DrawStyleDialog` | private | — |
| `d_current_visual_layer` | field | `boost::weak_ptr<GPlatesPresentation::VisualLayer>` | private | The visual layer for which we are currently displaying options. |
| `d_help_reconstruct_using_topologies_dialog` | field | `GPlatesQtWidgets::InformationDialog` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `HELP_RECONSTRUCT_USING_TOPOLOGIES_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_RECONSTRUCT_USING_TOPOLOGIES_DIALOG_TEXT` | variable | `QString` | — |
| `GPLATES_QTWIDGETS_RECONSTRUCTLAYEROPTIONSWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ReconstructLayerOptionsWidget tier=3]]]
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
| `ReconstructLayerOptionsWidget` | `QWidget` | — | 15 |

**Qt signal/slot connections** (15 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `set_vgp_visibility_link` | `link_activated()` | `this` | `open_vgp_visibility_dialog()` |
| `set_topology_reconstruction_parameters_link` | `link_activated()` | `this` | `open_topology_reconstruction_parameters_dialog()` |
| `draw_style_link` | `link_activated()` | `this` | `open_draw_style_setting_dlg()` |
| `dont_use_topologies_radio_button` | `toggled(bool)` | `this` | `handle_use_topologies_button(bool)` |
| `use_topologies_radio_button` | `toggled(bool)` | `this` | `handle_use_topologies_button(bool)` |
| `prompt_set_topology_reconstruction_parameters_check_box` | `clicked()` | `this` | `handle_prompt_set_topology_reconstruction_parameters_clicked()` |
| `push_button_help_reconstruct_using_topologies` | `clicked()` | `d_help_reconstruct_using_topologies_dialog` | `show()` |
| `fill_polygons` | `clicked()` | `this` | `handle_fill_polygons_clicked()` |
| `fill_polylines` | `clicked()` | `this` | `handle_fill_polylines_clicked()` |
| `fill_opacity_spinbox` | `valueChanged(double)` | `this` | `handle_fill_opacity_spinbox_changed(double)` |
| `fill_intensity_spinbox` | `valueChanged(double)` | `this` | `handle_fill_intensity_spinbox_changed(double)` |
| `dont_use_topologies_radio_button` | `toggled(bool)` | `this` | `handle_use_topologies_button(bool)` |
| `use_topologies_radio_button` | `toggled(bool)` | `this` | `handle_use_topologies_button(bool)` |
| `fill_opacity_spinbox` | `valueChanged(double)` | `this` | `handle_fill_opacity_spinbox_changed(double)` |
| `fill_intensity_spinbox` | `valueChanged(double)` | `this` | `handle_fill_intensity_spinbox_changed(double)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ReconstructLayerOptionsWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ReconstructLayerOptionsWidget --body
python scripts/gpq.py uses ReconstructLayerOptionsWidget --kind class
python scripts/gpq.py hier ReconstructLayerOptionsWidget
```
