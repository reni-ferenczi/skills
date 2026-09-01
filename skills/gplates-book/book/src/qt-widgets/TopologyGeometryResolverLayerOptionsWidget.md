# TopologyGeometryResolverLayerOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1016 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/TopologyGeometryResolverLayerOptionsWidget.h` | C++ | 114 |
| `src/qt-widgets/TopologyGeometryResolverLayerOptionsWidget.cc` | C++ | 216 |
| `src/qt-widgets/TopologyGeometryResolverLayerOptionsWidgetUi.ui` | Qt form | 107 |

## Overview

[[[PROSE overview unit=qt-widgets/TopologyGeometryResolverLayerOptionsWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::TopologyGeometryResolverLayerOptionsWidget`](#gplatesqtwidgetstopologygeometryresolverlayeroptionswidget) | class | [`LayerOptionsWidget`](LayerOptionsWidget.md)<br>`Ui_TopologyGeometryResolverLayerOptionsWidget` | — | 0 | TopologyGeometryResolverLayerOptionsWidget is used to show additional options for topology geometry layers in the visual layers widget. |

## Members

### `GPlatesQtWidgets::TopologyGeometryResolverLayerOptionsWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, ViewportWindow *viewport_window, QWidget *parent_)` | method | `LayerOptionsWidget` | public | — |
| `set_data( const boost::weak_ptr<GPlatesPresentation::VisualLayer> &visual_layer)` | method | `void` | public | — |
| `get_title` | field | `QString` | public | — |
| `open_draw_style_setting_dlg()` | method | `void` | private | — |
| `handle_fill_polygons_clicked()` | method | `void` | private | — |
| `handle_fill_opacity_spinbox_changed( double value)` | method | `void` | private | — |
| `handle_fill_intensity_spinbox_changed( double value)` | method | `void` | private | — |
| `TopologyGeometryResolverLayerOptionsWidget( GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, ViewportWindow *viewport_window, QWidget *parent_)` | constructor | `None` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_viewport_window` | field | `ViewportWindow` | private | — |
| `d_draw_style_dialog_ptr` | field | `DrawStyleDialog` | private | — |
| `d_current_visual_layer` | field | `boost::weak_ptr<GPlatesPresentation::VisualLayer>` | private | The visual layer for which we are currently displaying options. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QT_WIDGETS_TOPOLOGYGEOMETRYRESOLVERLAYEROPTIONSWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/TopologyGeometryResolverLayerOptionsWidget tier=3]]]
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
| `TopologyGeometryResolverLayerOptionsWidget` | `QWidget` | — | 7 |

**Qt signal/slot connections** (6 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `draw_style_link` | `link_activated()` | `this` | `open_draw_style_setting_dlg()` |
| `fill_polygons` | `clicked()` | `this` | `handle_fill_polygons_clicked()` |
| `fill_opacity_spinbox` | `valueChanged(double)` | `this` | `handle_fill_opacity_spinbox_changed(double)` |
| `fill_intensity_spinbox` | `valueChanged(double)` | `this` | `handle_fill_intensity_spinbox_changed(double)` |
| `fill_opacity_spinbox` | `valueChanged(double)` | `this` | `handle_fill_opacity_spinbox_changed(double)` |
| `fill_intensity_spinbox` | `valueChanged(double)` | `this` | `handle_fill_intensity_spinbox_changed(double)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/TopologyGeometryResolverLayerOptionsWidget.h
python scripts/gpq.py def GPlatesQtWidgets::TopologyGeometryResolverLayerOptionsWidget --body
python scripts/gpq.py uses TopologyGeometryResolverLayerOptionsWidget --kind class
python scripts/gpq.py hier TopologyGeometryResolverLayerOptionsWidget
```
