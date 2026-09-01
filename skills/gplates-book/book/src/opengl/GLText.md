# GLText

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 3 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLText.h` | C++ | 110 |
| `src/opengl/GLText.cc` | C++ | 200 |

## Overview

`GLText` renders text over the OpenGL scene by handing off to Qt rather than
drawing glyphs itself. `render_text_3D` projects a 3D world position through
`GLRenderer`'s current model-view, projection and viewport state to a window
coordinate, then uses `GLRenderer::QPainterBlockScope` to suspend OpenGL
rendering and obtain the `QPainter` that was attached when rendering began
(`GLRenderer::begin_render` must have been given one, or the call asserts),
draws the string with `QPainter::drawText`, and resumes OpenGL rendering when
the scope exits. `render_text_2D` is the `world_z = 0` convenience case for
the 2D map views, called from `gui/LayerPainter` and `gui/TextOverlay`.

The function takes care of the coordinate-system and device-pixel mismatches
between OpenGL and Qt: it inverts the y-axis (OpenGL's origin is bottom-left,
Qt's is top-left), converts device pixels to the device-independent pixels
`QPainter` expects, and — when OpenGL scissoring is enabled — translates the
scissor rectangle into an equivalent `QPainter` clip rectangle so text outside
the OpenGL-clipped region isn't drawn either.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `scale_font( const QFont &font, float scale)` | function | `QFont` | Returns a scaled version of the specified font. |
| `render_text( GLRenderer &renderer, float x, float y, const QString &string, const GPlatesGui::Colour &colour, const QFont &font, float scale)` | function | `void` | Renders text by delegating to the QPainter passed into GLRenderer. |
| `GPLATES_OPENGL_GLTEXT2DDRAWABLE_H` | macro | `None` | — |
| `render_text_3D( GLRenderer &renderer, double world_x, double world_y, double world_z, const QString &string, const GPlatesGui::Colour &colour, int x_offset, int y_offset, const QFont &font = QFont(), float scale = 1.0f)` | function | `void` | Renders text at a 3D position. |
| `render_text_2D( GLRenderer &renderer, const double &world_x, const double &world_y, const QString &string, const GPlatesGui::Colour &colour, int x_offset, int y_offset, const QFont &font, float scale = 1.0f)` | function | `void` | Renders text at a 2D position specified in the OpenGL coordinate frame (origin is bottom-left). |

## Notes

- `render_text_3D` throws `OpenGLException` if the `GLRenderer` it is given
  was not started with a `QPainter` attached.
- The `x_offset`/`y_offset`/`scale` parameters are in device-independent
  pixels regardless of the device pixel ratio; the conversion to and from
  OpenGL's device pixels happens internally.
- `y` is the text baseline, and glyphs are drawn above it.
- Text is skipped entirely (not clipped) when its projected depth falls
  outside the `[0, 1]` near/far range; x/y clipping is left to window or
  scissor clipping rather than handled here.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/LayerPainter](../gui/LayerPainter.md) | gui | 9 |
| [gui/TextOverlay](../gui/TextOverlay.md) | gui | 5 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLText.h
```
