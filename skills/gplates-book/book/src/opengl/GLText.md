# GLText

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 3 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLText.h` | C++ | 110 |
| `src/opengl/GLText.cc` | C++ | 200 |

## Overview

[[[PROSE overview unit=opengl/GLText tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=opengl/GLText tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
