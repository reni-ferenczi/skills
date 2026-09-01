# VisualLayersWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 789 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/VisualLayersWidget.h` | C++ | 105 |
| `src/qt-widgets/VisualLayersWidget.cc` | C++ | 141 |
| `src/qt-widgets/VisualLayersWidgetUi.ui` | Qt form | 254 |

## Overview

[[[PROSE overview unit=qt-widgets/VisualLayersWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::VisualLayersWidget`](#gplatesqtwidgetsvisuallayerswidget) | class | `QWidget`<br>`Ui_VisualLayersWidget` | — | 0 | VisualLayersWidget displays the contents of VisualLayers. |

## Members

### `GPlatesQtWidgets::VisualLayersWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `VisualLayersWidget( GPlatesPresentation::VisualLayers &visual_layers, GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, ViewportWindow *viewport_window, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~VisualLayersWidget()` | destructor | `None` | public | — |
| `handle_add_new_layer_button_clicked()` | method | `void` | private | — |
| `handle_colouring_button_clicked()` | method | `void` | private | — |
| `handle_show_all_button_clicked()` | method | `void` | private | — |
| `handle_hide_all_button_clicked()` | method | `void` | private | — |
| `d_visual_layers` | field | `GPlatesGui::VisualLayersProxy` | private | A wrapper around VisualLayers to invert the ordering for the user interface. |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_viewport_window` | field | `ViewportWindow` | private | — |
| `d_add_new_layer_dialog` | field | `boost::scoped_ptr<AddNewLayerDialog>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_VISUALLAYERSWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/VisualLayersWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/VisualLayersDialog](VisualLayersDialog.md) | qt-widgets | 3 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `VisualLayersWidget` | `QWidget` | Layers | 12 |

**Qt signal/slot connections** (5 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `add_new_layer_button` | `clicked()` | `this` | `handle_add_new_layer_button_clicked()` |
| `colouring_button` | `clicked()` | `&d_viewport_window->dialogs()` | `pop_up_draw_style_dialog()` |
| `colouring_button` | `clicked()` | `this` | `handle_colouring_button_clicked()` |
| `button_show_all` | `clicked()` | `this` | `handle_show_all_button_clicked()` |
| `button_hide_all` | `clicked()` | `this` | `handle_hide_all_button_clicked()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/VisualLayersWidget.h
python scripts/gpq.py def GPlatesQtWidgets::VisualLayersWidget --body
python scripts/gpq.py uses VisualLayersWidget --kind class
python scripts/gpq.py hier VisualLayersWidget
```
