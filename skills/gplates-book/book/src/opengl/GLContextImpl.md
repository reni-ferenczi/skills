# GLContextImpl

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 1073 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLContextImpl.h` | C++ | 149 |

## Overview

`GLContextImpl` supplies the two concrete `GLContext::Impl` backends that adapt Qt's OpenGL context types to the `GLContext` abstraction: `QGLWidgetImpl` wraps a `QGLWidget` (the on-screen canvas used by `GlobeCanvas` and `MapCanvas`/`MapView`), and `QGLPixelBufferImpl` wraps a `QGLPixelBuffer` (used for off-screen rendering, notably by `GLOffScreenContext`). Both simply forward `make_current`, `get_qgl_format`, `get_width` and `get_height` to the wrapped Qt object, converting widget/pixel-buffer dimensions to device pixels by multiplying by `devicePixelRatio` since OpenGL dimensions are expected in device pixels rather than logical ones.

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

- `QGLWidgetImpl` binds to its `QGLWidget` for life via a reference, but `QGLPixelBufferImpl` holds its `QGLPixelBuffer` by pointer and exposes `set_pixel_buffer` to repoint it — the two wrappers are not interchangeable in this respect, since only the pixel-buffer variant supports being retargeted after construction.
- Neither wrapper takes ownership of the Qt object it wraps; the caller must keep the `QGLWidget` or `QGLPixelBuffer` alive for as long as the `GLContextImpl` is in use.

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
