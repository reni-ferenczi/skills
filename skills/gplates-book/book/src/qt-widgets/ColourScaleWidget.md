# ColourScaleWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 651 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ColourScaleWidget.h` | C++ | 155 |
| `src/qt-widgets/ColourScaleWidget.cc` | C++ | 224 |

## Overview

A custom widget that renders a visual colour scale bar with annotations on a canvas. After populating it with a `GPlatesGui::RasterColourPalette`, the widget draws the scale and labels at minimum height of 200 pixels. It supports optional logarithmic scaling of the colour range and handles redraws on resize. The context menu allows saving the scale as an image.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ColourScaleWidget`](#gplatesqtwidgetscolourscalewidget) | class | `QWidget` | — | 0 | ColourScaleWidget displays an annotated colour scale on screen. |

## Members

### `GPlatesQtWidgets::ColourScaleWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LEFT_MARGIN` | field | `int` | public | Distance from left border of widget to the colour scale. |
| `COLOUR_SCALE_WIDTH` | field | `int` | public | Width of the colour scale. |
| `INTERNAL_SPACING` | field | `int` | public | Distance from colour scale to annotation text. |
| `ANNOTATION_LINE_SPACING` | field | `int` | public | Minimum spacing in pixels between each line of annotation. |
| `TICK_LENGTH` | field | `int` | public | Length of tick marks that accompany annotations. |
| `ColourScaleWidget( GPlatesPresentation::ViewState &view_state, ViewportWindow *viewport_window, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `populate( const GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type &colour_palette, boost::optional<double> use_log_scale = boost::none)` | method | `bool` | public | Causes this widget to render scales for the given colour\_palette. |
| `paintEvent( QPaintEvent *ev)` | method | `void` | protected | — |
| `resizeEvent( QResizeEvent *ev)` | method | `void` | protected | — |
| `contextMenuEvent( QContextMenuEvent *ev)` | method | `void` | protected | — |
| `regenerate_contents()` | method | `bool` | private | Returns true if we were able to extract the right info out of d\_curr\_colour\_palette. |
| `MINIMUM_HEIGHT` | field | `int` | private | — |
| `d_viewport_window` | field | `ViewportWindow` | private | — |
| `d_curr_colour_palette` | field | `GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type` | private | — |
| `d_colour_scale_pixmap` | field | `QPixmap` | private | — |
| `d_disabled_colour_scale_pixmap` | field | `QPixmap` | private | — |
| `d_annotations` | field | `GPlatesGui::ColourScale::annotations_seq_type` | private | — |
| `d_use_log_scale` | field | `boost::optional<double>` | private | — |
| `d_right_click_actions` | field | `QList<QAction *>` | private | — |
| `d_save_file_dialog` | field | `SaveFileDialog` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_file_dialog_filters()` | function | `GPlatesQtWidgets::SaveFileDialog::filter_list_type` | — |
| `GPLATES_QTWIDGETS_COLOURSCALEWIDGET_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 14 |
| [qt-widgets/RemappedColourPaletteWidget](RemappedColourPaletteWidget.md) | qt-widgets | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ColourScaleWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ColourScaleWidget --body
python scripts/gpq.py uses ColourScaleWidget --kind class
python scripts/gpq.py hier ColourScaleWidget
```
