# GLViewport

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 1290 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLViewport.h` | C++ | 148 |

## Overview

[[[PROSE overview unit=opengl/GLViewport tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLViewport`](#gplatesopenglglviewport) | class | `boost::equality_comparable<GLViewport>` | — | 0 | OpenGL viewport parameters. |

## Members

### `GPlatesOpenGL::GLViewport`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLViewport()` | constructor | `None` | public | Default constructor. |
| `GLViewport( GLint x_, GLint y_, GLsizei width_, GLsizei height_)` | constructor | `None` | public | Constructor. |
| `set_viewport( GLint x_, GLint y_, GLsizei width_, GLsizei height_)` | method | `void` | public | Sets the viewport parameters. |
| `x()` | method | `GLint` | public | — |
| `y()` | method | `GLint` | public | — |
| `width()` | method | `GLsizei` | public | — |
| `height()` | method | `GLsizei` | public | — |
| `viewport_type` | typedef | `GLint` | public | Typedef for an array of four integers representing the viewport parameters. |
| `operator==( const GLViewport &other)` | operator | `bool` | public | Equality operator - and operator!= provided by boost::equality\_comparable. |
| `Viewport` | struct | `None` | private | — |
| `d_viewport` | field | `Viewport` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLVIEWPORT_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLViewport tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/GlobeCanvas](../qt-widgets/GlobeCanvas.md) | qt-widgets | 56 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 50 |
| [opengl/GLStateSets](GLStateSets.md) | opengl | 49 |
| [opengl/GLProjectionUtils](GLProjectionUtils.md) | opengl | 40 |
| [opengl/GLTileRender](GLTileRender.md) | opengl | 39 |
| [opengl/GLRenderer](GLRenderer.md) | opengl | 38 |
| [qt-widgets/MapCanvas](../qt-widgets/MapCanvas.md) | qt-widgets | 35 |
| [gui/FeedbackOpenGLToQPainter](../gui/FeedbackOpenGLToQPainter.md) | gui | 21 |
| [opengl/GLScalarField3D](GLScalarField3D.md) | opengl | 15 |
| [opengl/GLState](GLState.md) | opengl | 15 |
| [opengl/GLImageUtils](GLImageUtils.md) | opengl | 13 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 12 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 12 |
| [gui/VelocityLegendOverlay](../gui/VelocityLegendOverlay.md) | gui | 11 |
| [opengl/GLSaveRestoreFrameBuffer](GLSaveRestoreFrameBuffer.md) | opengl | 11 |
| [gui/Globe](../gui/Globe.md) | gui | 9 |
| [opengl/GLText](GLText.md) | opengl | 8 |
| [gui/LayerPainter](../gui/LayerPainter.md) | gui | 6 |
| [opengl/GLMultiResolutionRaster](GLMultiResolutionRaster.md) | opengl | 4 |
| [opengl/GLMultiResolutionRasterInterface](GLMultiResolutionRasterInterface.md) | opengl | 4 |

*... and 16 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLViewport.h
python scripts/gpq.py def GPlatesOpenGL::GLViewport --body
python scripts/gpq.py uses GLViewport --kind class
python scripts/gpq.py hier GLViewport
```
