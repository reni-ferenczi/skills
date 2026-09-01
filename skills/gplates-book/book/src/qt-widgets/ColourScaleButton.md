# ColourScaleButton

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 30 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ColourScaleButton.h` | C++ | 142 |
| `src/qt-widgets/ColourScaleButton.cc` | C++ | 242 |

## Overview

[[[PROSE overview unit=qt-widgets/ColourScaleButton tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ColourScaleButton`](#gplatesqtwidgetscolourscalebutton) | class | `QToolButton` | — | 0 | ColourScaleButton displays a colour scale image (without annotations) in a QToolButton. |

## Members

### `GPlatesQtWidgets::ColourScaleButton`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ColourScaleButton( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `populate( const GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type &colour_palette, boost::optional<double> use_log_scale = boost::none)` | method | `bool` | public | Causes this widget to render scales for the given colour\_palette. |
| `paintEvent( QPaintEvent *ev)` | method | `void` | protected | — |
| `resizeEvent( QResizeEvent *ev)` | method | `void` | protected | — |
| `enterEvent( QEvent *ev)` | method | `void` | protected | — |
| `leaveEvent( QEvent *ev)` | method | `void` | protected | — |
| `sizeHint()` | method | `QSize` | protected | — |
| `minimumSizeHint()` | method | `QSize` | protected | — |
| `handle_pressed()` | method | `void` | private | — |
| `handle_released()` | method | `void` | private | — |
| `regenerate_contents()` | method | `bool` | private | Returns true if we were able to extract the right info out of d\_curr\_colour\_palette. |
| `MINIMUM_PIXMAP_WIDTH` | field | `int` | private | Pixmap size. |
| `MINIMUM_PIXMAP_HEIGHT` | field | `int` | private | — |
| `MINIMUM_WIDTH` | field | `int` | private | Button size (including border size of 1). |
| `MINIMUM_HEIGHT` | field | `int` | private | — |
| `d_curr_colour_palette` | field | `GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type` | private | — |
| `d_use_log_scale` | field | `boost::optional<double>` | private | — |
| `d_colour_scale_pixmap` | field | `QPixmap` | private | — |
| `d_disabled_colour_scale_pixmap` | field | `QPixmap` | private | — |
| `d_mouse_inside_button` | field | `bool` | private | — |
| `d_mouse_pressed` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QT_WIDGETS_COLOURSCALEBUTTON_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ColourScaleButton tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ChooseBuiltinPaletteDialog](ChooseBuiltinPaletteDialog.md) | qt-widgets | 155 |
| [qt-widgets/RemappedColourPaletteWidget](RemappedColourPaletteWidget.md) | qt-widgets | 1 |

## Related

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `this` | `pressed()` | `this` | `handle_pressed()` |
| `this` | `released()` | `this` | `handle_released()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ColourScaleButton.h
python scripts/gpq.py def GPlatesQtWidgets::ColourScaleButton --body
python scripts/gpq.py uses ColourScaleButton --kind class
python scripts/gpq.py hier ColourScaleButton
```
