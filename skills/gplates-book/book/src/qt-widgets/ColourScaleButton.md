# ColourScaleButton

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 30 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ColourScaleButton.h` | C++ | 142 |
| `src/qt-widgets/ColourScaleButton.cc` | C++ | 242 |

## Overview

`ColourScaleButton` renders an unannotated preview of a
`GPlatesGui::RasterColourPalette` as a clickable button, used as the
launching control for the full colour-scale/palette picker (see
`ChooseBuiltinPaletteDialog`, its dominant caller). It subclasses
`QToolButton` rather than `QPushButton` specifically because `QToolButton`
respects the widget's size hints, which matters for a button whose entire
purpose is displaying an image at a controlled aspect ratio.

`populate()` hands the palette (and an optional log-scale distribution
parameter) to `GPlatesGui::ColourScale::generate()`, which does the actual
pixmap rendering into `d_colour_scale_pixmap` and
`d_disabled_colour_scale_pixmap`; `regenerate_contents()` re-runs that
generation whenever the button is resized, since the pixmap must be
regenerated at the new pixel dimensions rather than simply scaled.
`paintEvent()` composites the appropriate pixmap over the button's palette
background and draws a hover/pressed highlight tracked by
`d_mouse_inside_button` and `d_mouse_pressed`.

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

`populate()` returns `false` if `ColourScale::generate()` cannot extract a
usable scale from the given palette — callers should check the return value
rather than assume the button always ends up showing something.
`enterEvent()` forces an explicit repaint on hover because, per a comment in
the source, Qt 4.8 needed this on Mac but not on Windows or Ubuntu to redraw
the highlight.

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
