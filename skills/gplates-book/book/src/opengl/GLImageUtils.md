# GLImageUtils

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 3 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLImageUtils.h` | C++ | 77 |
| `src/opengl/GLImageUtils.cc` | C++ | 159 |

## Overview

[[[PROSE overview unit=opengl/GLImageUtils tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLIMAGEUTILS_H` | macro | `None` | — |
| `copy_rgba8_frame_buffer_into_argb32_qimage( GLRenderer &renderer, QImage &image, const GLViewport &source_viewport, const GLViewport &destination_viewport)` | function | `void` | Copies the specified source rectangle of the currently bound frame buffer into the specified destination rectangle of the QImage. |
| `draw_text_into_qimage( const QString &text, unsigned int image_width, unsigned int image_height, const float text_scale = 1.0f, const QColor &text_colour = QColor(255, 255, 255, 255)/*white*/, const QColor &background_colour = QColor(0, 0, 0, 255)/*black*/)` | function | `QImage` | Draws the specified text into a QImage the specified size. |

## Notes

[[[PROSE notes unit=opengl/GLImageUtils tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/FeedbackOpenGLToQPainter](../gui/FeedbackOpenGLToQPainter.md) | gui | 3 |
| [opengl/GLMultiResolutionRasterMapView](GLMultiResolutionRasterMapView.md) | opengl | 3 |
| [opengl/GLVisualRasterSource](GLVisualRasterSource.md) | opengl | 3 |
| [qt-widgets/GlobeCanvas](../qt-widgets/GlobeCanvas.md) | qt-widgets | 3 |
| [qt-widgets/MapCanvas](../qt-widgets/MapCanvas.md) | qt-widgets | 3 |
| [opengl/GLMultiResolutionCubeRaster](GLMultiResolutionCubeRaster.md) | opengl | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLImageUtils.h
```
