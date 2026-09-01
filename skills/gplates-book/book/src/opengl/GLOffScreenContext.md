# GLOffScreenContext

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 518 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLOffScreenContext.h` | C++ | 292 |
| `src/opengl/GLOffScreenContext.cc` | C++ | 450 |

## Overview

`GLOffScreenContext` exists so rendering code can target a genuine off-screen framebuffer instead of the *main* framebuffer of a `QGLWidget`, which cannot be safely modified outside its own paint event even though its OpenGL context can be used elsewhere. It tries, in order of preference, an off-screen `QGLPixelBuffer` ('pbuffer') context — sharing textures with a given `QGLWidgetContext` when one is supplied — or a `GL_EXT_framebuffer_object`-backed `GLScreenRenderTarget`, falling back only as a last resort to rendering into the QGLWidget's main framebuffer with save/restore (`GLSaveRestoreFrameBuffer`) around it to avoid corrupting prior contents. `create` has two overloads: one builds a standalone pbuffer context from a `QGLFormat`, the other attempts to reuse an existing `QGLWidget`'s context and its resources.

Rendering is bracketed by `begin_off_screen_render`/`end_off_screen_render`, which hand out and retire a `GLRenderer` scoped to this context and framebuffer; `RenderScope` wraps that pair as an RAII guard. `is_valid` reports whether any of the strategies above succeeded (always true when a `QGLWidgetContext` was given, since the main-framebuffer fallback always works), and `is_off_screen` distinguishes a genuine off-screen target from the main-framebuffer emulation.

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

- `begin_off_screen_render` assumes the full OpenGL state is already at its default when called, and both it and `end_off_screen_render` throw if `is_valid()` is false — callers must check validity before using the context.
- The requested frame buffer dimensions are honoured only for genuine off-screen rendering; when it falls back to the QGLWidget's main framebuffer, the actual dimensions are the widget's own and must be read back via `GLRenderer::get_current_frame_buffer_dimensions()`.
- The `GLRenderer` returned by `begin_off_screen_render` (or `RenderScope::get_renderer`) becomes invalid once `end_off_screen_render` is called and must not be used afterward.

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
