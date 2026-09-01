# ZoomControlWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 714 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ZoomControlWidget.h` | C++ | 119 |
| `src/qt-widgets/ZoomControlWidget.cc` | C++ | 101 |
| `src/qt-widgets/ZoomControlWidgetUi.ui` | Qt form | 122 |

## Overview

[[[PROSE overview unit=qt-widgets/ZoomControlWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ZoomControlWidget`](#gplatesqtwidgetszoomcontrolwidget) | class | `QWidget`<br>`Ui_ZoomControlWidget` | — | 0 | Small widget with a spinbox and three buttons for controlling the zoom level. |

## Members

### `GPlatesQtWidgets::ZoomControlWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ZoomControlWidget( GPlatesGui::ViewportZoom &vzoom, QWidget *parent_)` | constructor | `None` | public | — |
| `editing_finished()` | method | `void` | public | Emitted when the user has entered a new zoom value in the spinbox. |
| `activate_zoom_spinbox()` | method | `void` | public | Focuses the spinbox and highlights text, ready to be replaced. |
| `show_buttons( bool show_)` | method | `void` | public | Sets whether you want the + / - / 1 buttons shown or hidden. |
| `show_label( bool show_)` | method | `void` | public | Sets whether you want the "Zoom:" label shown or hidden. |
| `handle_zoom_changed()` | method | `void` | private | In response to a zoom event, this will set the spinbox to reflect the new zoom level percentage. |
| `handle_spinbox_changed()` | method | `void` | private | In response to user spinning to a new zoom percent value and hitting 'enter'. |
| `d_viewport_zoom_ptr` | field | `GPlatesGui::ViewportZoom` | private | This is a pointer to the viewport zoom we are using to control the current zoom level (and react to zoom events not caused by us so we can update our spinbox). |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_ZOOMCONTROLWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ZoomControlWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ReconstructionViewWidget](ReconstructionViewWidget.md) | qt-widgets | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ZoomControlWidget` | `QWidget` | Form | 6 |

**Qt signal/slot connections** (5 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_zoom_in` | `clicked()` | `&vzoom` | `zoom_in()` |
| `button_zoom_out` | `clicked()` | `&vzoom` | `zoom_out()` |
| `button_zoom_reset` | `clicked()` | `&vzoom` | `reset_zoom()` |
| `spinbox_zoom_percent` | `editingFinished()` | `this` | `handle_spinbox_changed()` |
| `&vzoom` | `zoom_changed()` | `this` | `handle_zoom_changed()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ZoomControlWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ZoomControlWidget --body
python scripts/gpq.py uses ZoomControlWidget --kind class
python scripts/gpq.py hier ZoomControlWidget
```
