# ReconstructionLayerOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 689 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ReconstructionLayerOptionsWidget.h` | C++ | 119 |
| `src/qt-widgets/ReconstructionLayerOptionsWidget.cc` | C++ | 228 |
| `src/qt-widgets/ReconstructionLayerOptionsWidgetUi.ui` | Qt form | 81 |

## Overview

This widget provides options for reconstruction layers, which contain the plate rotation data used to reconstruct geometries through time. It allows users to view the total reconstruction poles, merge multiple reconstruction layer trees, and control how rotation data is extrapolated beyond the time range covered by the input rotation file.

The widget offers a checkbox to mark a reconstruction layer as the default, which determines which rotation sequence is used when multiple reconstruction layers are available. It also provides an option to extend rotation poles to the distant past, preventing geometries from snapping back to present-day positions when the reconstruction time predates the oldest rotation data. A dialog is available to help users understand this extrapolation behavior and its effects on ancient reconstructions.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ReconstructionLayerOptionsWidget`](#gplatesqtwidgetsreconstructionlayeroptionswidget) | class | [`LayerOptionsWidget`](LayerOptionsWidget.md)<br>`Ui_ReconstructionLayerOptionsWidget` | — | 0 | ReconstructionLayerOptionsWidget is used to show additional options for reconstruction layers in the visual layers widget. |

## Members

### `GPlatesQtWidgets::ReconstructionLayerOptionsWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, ViewportWindow *viewport_window, QWidget *parent_)` | method | `LayerOptionsWidget` | public | — |
| `set_data( const boost::weak_ptr<GPlatesPresentation::VisualLayer> &visual_layer)` | method | `void` | public | — |
| `get_title` | field | `QString` | public | — |
| `handle_view_total_reconstruction_poles_link_activated()` | method | `void` | private | — |
| `handle_merge_reconstruction_tree_layers_link_activated()` | method | `void` | private | — |
| `handle_extend_total_reconstruction_poles_to_distant_past_clicked()` | method | `void` | private | — |
| `handle_keep_as_default_checkbox_clicked( bool checked)` | method | `void` | private | — |
| `ReconstructionLayerOptionsWidget( GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, ViewportWindow *viewport_window, QWidget *parent_)` | constructor | `None` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_viewport_window` | field | `ViewportWindow` | private | — |
| `d_merge_reconstruction_layers_dialog` | field | `MergeReconstructionLayersDialog` | private | — |
| `d_current_visual_layer` | field | `boost::weak_ptr<GPlatesPresentation::VisualLayer>` | private | The visual layer for which we are currently displaying options. |
| `d_help_extend_total_reconstruction_pole_to_distant_past_dialog` | field | `GPlatesQtWidgets::InformationDialog` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `HELP_EXTEND_TOTAL_RECONSTRUCTION_POLE_TO_DISTANT_PAST_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_EXTEND_TOTAL_RECONSTRUCTION_POLE_TO_DISTANT_PAST_DIALOG_TEXT` | variable | `QString` | — |
| `GPLATES_QTWIDGETS_RECONSTRUCTIONLAYEROPTIONSWIDGET_H` | macro | `None` | — |

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
| `ReconstructionLayerOptionsWidget` | `QWidget` | Layers | 6 |

**Qt signal/slot connections** (5 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `view_total_reconstruction_poles_link` | `link_activated()` | `this` | `handle_view_total_reconstruction_poles_link_activated()` |
| `merge_reconstruction_tree_layers_link` | `link_activated()` | `this` | `handle_merge_reconstruction_tree_layers_link_activated()` |
| `keep_as_default_checkbox` | `clicked(bool)` | `this` | `handle_keep_as_default_checkbox_clicked(bool)` |
| `extend_total_reconstruction_poles_to_distant_past_check_box` | `clicked()` | `this` | `handle_extend_total_reconstruction_poles_to_distant_past_clicked()` |
| `push_button_help_extend_total_reconstruction_poles_to_distant_past` | `clicked()` | `d_help_extend_total_reconstruction_pole_to_distant_past_dialog` | `show()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ReconstructionLayerOptionsWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ReconstructionLayerOptionsWidget --body
python scripts/gpq.py uses ReconstructionLayerOptionsWidget --kind class
python scripts/gpq.py hier ReconstructionLayerOptionsWidget
```
