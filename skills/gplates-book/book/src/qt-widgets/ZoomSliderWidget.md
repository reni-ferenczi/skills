# ZoomSliderWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 774 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ZoomSliderWidget.h` | C++ | 176 |
| `src/qt-widgets/ZoomSliderWidget.cc` | C++ | 135 |

## Overview

A vertical slider widget with zoom-in and zoom-out icon buttons (shown as clickable labels at the top and bottom). The slider provides a bidirectional interface to the viewport zoom: when dragged, it changes the zoom level through `ViewportZoom`; when the zoom changes from other sources (spinbox, keyboard, mouse wheel), the slider updates to match. The widget is implemented in code rather than using Designer because it must be positioned carefully between other code-generated widgets to achieve proper layout of a resize grip between the globe view and task panel.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ZoomSliderWidget`](#gplatesqtwidgetszoomsliderwidget) | class | `QWidget` | — | 0 | Trivial widget with a slider and two icons that responds to and changes the viewport zoom. |

## Members

### `GPlatesQtWidgets::ZoomSliderWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ZoomSliderWidget( GPlatesGui::ViewportZoom &vzoom, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `handle_slider_moved( int slider_position)` | method | `void` | private | — |
| `handle_zoom_changed()` | method | `void` | private | — |
| `ZoomSlider` | class | `None` | private | — |
| `ZoomIcon` | class | `None` | private | — |
| `set_up_ui()` | method | `void` | private | — |
| `set_up_signals_and_slots()` | method | `void` | private | — |
| `d_viewport_zoom_ptr` | field | `GPlatesGui::ViewportZoom` | private | This is a pointer to the viewport zoom we are using to control the current zoom level (and react to zoom events not caused by us so we can update our slider). |
| `d_slider_zoom` | field | `ZoomSlider` | private | This is our slider widget that we get events from. |
| `d_suppress_zoom_change_event` | field | `bool` | private | A necessary work-around to using QSlider::setValue() while tracking is enabled; we don't want the programmatic modification of the slider to cause zoom level changes, because the slider ticks by zoom level, which may not be exactly the ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `NUM_STEPS_PER_LEVEL` | variable | `int` | — |
| `GPLATES_QTWIDGETS_ZOOMSLIDERWIDGET_H` | macro | `None` | — |

## Notes

The `d_suppress_zoom_change_event` flag prevents feedback loops in the signal/slot chain: when handle_zoom_changed() sets the slider value programmatically, the flag is set to suppress the resulting valueChanged signal, preventing propagation back to ViewportZoom. This is necessary because slider ticks are coarser than zoom percentages, so an arbitrary zoom value may map to a different slider position, creating a mismatch if both directions are active.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ReconstructionViewWidget](ReconstructionViewWidget.md) | qt-widgets | 3 |

## Related

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_slider_zoom` | `valueChanged(int)` | `this` | `handle_slider_moved(int)` |
| `d_viewport_zoom_ptr` | `zoom_changed()` | `this` | `handle_zoom_changed()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ZoomSliderWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ZoomSliderWidget --body
python scripts/gpq.py uses ZoomSliderWidget --kind class
python scripts/gpq.py hier ZoomSliderWidget
```
