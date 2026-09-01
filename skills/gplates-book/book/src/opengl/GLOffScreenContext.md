# GLOffScreenContext

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 518 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLOffScreenContext.h` | C++ | 292 |
| `src/opengl/GLOffScreenContext.cc` | C++ | 450 |

## Overview

[[[PROSE overview unit=opengl/GLOffScreenContext tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLOffScreenContext`](#gplatesopenglgloffscreencontext) | class | [`GPlatesUtils::ReferenceCount<GLOffScreenContext>`](../utils/ReferenceCount.md) | — | 0 | An off-screen OpenGL context (or fall back to emulation of off-screen using a QGLWidget frame buffer). |

## Members

### `GPlatesOpenGL::GLOffScreenContext`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLOffScreenContext>` | public | A convenience typedef for a shared pointer to a non-const GLOffScreenContext. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLOffScreenContext>` | public | A convenience typedef for a shared pointer to a const GLOffScreenContext. |
| `QGLWidgetContext` | struct | `None` | public | Associates a QGLWidget with its OpenGL context. |
| `create( const QGLFormat &qgl_format)` | method | `non_null_ptr_type` | public | Creates an off-screen OpenGL context and associated frame buffer using the specified format. |
| `create( const QGLWidgetContext &qgl_widget_context)` | method | `non_null_ptr_type` | public | Creates an off-screen render target that attempts to use the OpenGL context of the specified QGLWidget. |
| `is_valid()` | method | `bool` | public | Returns true if the off-screen context is valid. |
| `is_off_screen()` | method | `bool` | public | Returns true if the rendering will truly be off-screen. |
| `begin_off_screen_render( unsigned int frame_buffer_width, unsigned int frame_buffer_height, boost::optional<QPainter &> qpainter = boost::none, // Does the QPainter render to the framebuffer or some other paint device ? ... bool paint_device_is_framebuffer = true)` | method | `GPlatesGlobal::PointerTraits<GLRenderer>::non_null_ptr_type` | public | Begins an off-screen render scope that targets this off-screen context and associated frame buffer. |
| `end_off_screen_render()` | method | `void` | public | Ends the current off-screen render scope. |
| `RenderScope` | class | `None` | public | RAII class to call begin\_render and end\_render over a scope. |
| `d_qgl_widget_context` | field | `boost::optional<QGLWidgetContext>` | private | This is only valid if a QGLWidget context was provided. |
| `d_off_screen_context` | field | `boost::optional<GLContext::non_null_ptr_type>` | private | The OpenGL context used for off-screen rendering. |
| `d_screen_render_target` | field | `boost::optional<GLScreenRenderTarget::shared_ptr_type>` | private | Various options for implementing off-screen rendering. |
| `d_qgl_pixel_buffer` | field | `boost::optional<QGLPixelBuffer>` | private | — |
| `d_qgl_pixel_buffer_impl` | field | `boost::optional< boost::shared_ptr<GLContextImpl::QGLPixelBufferImpl> >` | private | — |
| `d_renderer` | field | `boost::optional< boost::shared_ptr<GLRenderer> >` | private | The renderer is only valid between begin\_off\_screen\_render and end\_off\_screen\_render. |
| `d_save_restore_framebuffer` | field | `boost::optional<GLSaveRestoreFrameBuffer>` | private | Used to save/restore the QGLWidget frame buffer when 'pbuffer' and frame buffer objects not supported. |
| `GLOffScreenContext( const QGLFormat &qgl_format)` | constructor | `None` | private | — |
| `GLOffScreenContext( const QGLWidgetContext &qgl_widget_context)` | constructor | `None` | private | — |
| `initialise( const QGLFormat &qgl_format)` | method | `void` | private | — |
| `initialise_screen_render_target()` | method | `bool` | private | — |
| `initialise_pbuffer_context( const QGLFormat &qgl_format, int initial_width, int initial_height)` | method | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLOFFSCREENCONTEXT_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLOffScreenContext tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/GlobeCanvas](../qt-widgets/GlobeCanvas.md) | qt-widgets | 13 |
| [qt-widgets/MapCanvas](../qt-widgets/MapCanvas.md) | qt-widgets | 13 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLOffScreenContext.h
python scripts/gpq.py def GPlatesOpenGL::GLOffScreenContext --body
python scripts/gpq.py uses GLOffScreenContext --kind class
python scripts/gpq.py hier GLOffScreenContext
```
