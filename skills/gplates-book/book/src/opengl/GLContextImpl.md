# GLContextImpl

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 1073 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLContextImpl.h` | C++ | 149 |

## Overview

[[[PROSE overview unit=opengl/GLContextImpl tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLContextImpl::QGLWidgetImpl`](#gplatesopenglglcontextimplqglwidgetimpl) | class | [`GLContext::Impl`](GLContext.md) | — | 0 | A derivation of GLContext::Impl for QGLWidget. |
| [`GPlatesOpenGL::GLContextImpl::QGLPixelBufferImpl`](#gplatesopenglglcontextimplqglpixelbufferimpl) | class | [`GLContext::Impl`](GLContext.md) | — | 0 | A derivation of GLContext::Impl for QGLPixelBuffer. |

## Members

### `GPlatesOpenGL::GLContextImpl::QGLWidgetImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `QGLWidgetImpl( QGLWidget &qgl_widget)` | constructor | `None` | public | — |
| `make_current()` | method | `void` | public | — |
| `get_qgl_format()` | method | `QGLFormat` | public | — |
| `get_width()` | method | `unsigned int` | public | — |
| `get_height()` | method | `unsigned int` | public | — |
| `d_qgl_widget` | field | `QGLWidget` | private | — |

### `GPlatesOpenGL::GLContextImpl::QGLPixelBufferImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `QGLPixelBufferImpl( QGLPixelBuffer &qgl_pixel_buffer)` | constructor | `None` | public | — |
| `set_pixel_buffer( QGLPixelBuffer &qgl_pixel_buffer)` | method | `void` | public | — |
| `make_current()` | method | `void` | public | — |
| `get_qgl_format()` | method | `QGLFormat` | public | — |
| `get_width()` | method | `unsigned int` | public | — |
| `get_height()` | method | `unsigned int` | public | — |
| `d_qgl_pixel_buffer` | field | `QGLPixelBuffer` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLCONTEXTIMPL_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLContextImpl tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLOffScreenContext](GLOffScreenContext.md) | opengl | 14 |
| [qt-widgets/GlobeCanvas](../qt-widgets/GlobeCanvas.md) | qt-widgets | 7 |
| [qt-widgets/MapView](../qt-widgets/MapView.md) | qt-widgets | 5 |
| [qt-widgets/MapCanvas](../qt-widgets/MapCanvas.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLContextImpl.h
python scripts/gpq.py def GPlatesOpenGL::GLContextImpl::QGLPixelBufferImpl --body
python scripts/gpq.py uses QGLPixelBufferImpl --kind class
python scripts/gpq.py hier QGLPixelBufferImpl
```
