# GLViewport

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 1290 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLViewport.h` | C++ | 148 |

## Overview

A header-only value type wrapping the `(x, y, width, height)` integer rectangle
that OpenGL uses for both the viewport and the scissor box. It is tier 1 not
because it is complicated but because it is the currency for every screen-space
rectangle in the backend, and one of the most widely used types in `opengl`.

The one design decision worth knowing is the private `Viewport` union: the four
components are addressable both as named fields and as a `GLint[4]`. That is why
`get_viewport()` can hand its storage straight to `gluProject` and `gluUnProject`
in `GLProjectionUtils` with no repacking, while `GLStateSets` uses the named
accessors to feed `glViewport` and `glScissor`, and packs several `GLViewport`
objects into one contiguous array for the `glViewportArrayv` /
`glScissorArrayv` multi-viewport paths.

In the render path, `GLRenderer::gl_viewport` and `gl_scissor` store these into
the shadowed state and `gl_get_viewport` / `gl_get_scissor` read them back;
`GLViewportStateSet` and `GLScissorStateSet` hold them and use `operator==` to
skip redundant driver calls. `GLTileRender` produces a triple of them per tile
when rendering an image larger than the framebuffer, and the canvases
(`GPlatesQtWidgets::GlobeCanvas`, `GPlatesQtWidgets::MapCanvas`) supply the
window rectangle that everything downstream projects against.

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

- `operator==` is load-bearing, not decoration: `GLViewportStateSet` and
  `GLScissorStateSet` compare viewports to decide whether to issue `glViewport` /
  `glScissor` at all. If you ever add a field here, extend `operator==` too, or
  redundant-state elimination will silently start dropping real state changes.
- The union aliases `width` and `height`, declared `GLsizei`, onto elements of a
  `GLint[4]`. It works because the two are the same size on the supported
  platforms, and the anonymous struct inside the union is a compiler extension
  rather than standard C++. Both assumptions are worth remembering before
  changing the member types.
- Nothing is validated. The default constructor produces `(0, 0, 0, 0)` — a legal
  but empty rectangle, not an "unset" marker — and negative widths or heights are
  stored as given and only rejected later by OpenGL.
- `get_viewport()` returns a reference into the object's own storage; do not hold
  it past the `GLViewport`'s lifetime.
- The class itself is a plain copyable value with no GL resources, safe to
  construct and compare anywhere. `GLRenderer::gl_get_viewport` and
  `gl_get_scissor`, however, must be called between `begin_render` and
  `end_render`, and their `viewport_index` must be below
  `GLCapabilities::viewport::gl_max_viewports`.

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
