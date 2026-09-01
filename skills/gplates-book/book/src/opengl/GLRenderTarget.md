# GLRenderTarget

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 1040 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLRenderTarget.h` | C++ | 215 |
| `src/opengl/GLRenderTarget.cc` | C++ | 154 |

## Overview

A fixed-size off-screen render target: a texture plus an optional
depth/stencil buffer, rendered into between `begin_render` and `end_render`
(or, more conveniently, over the lifetime of a `RenderScope`). It delegates
its actual OpenGL framebuffer-object work to `GLRenderTargetImpl`, which it
owns by value.

The design point is context portability: a native OpenGL framebuffer object
cannot be shared between rendering contexts, but `GLRenderTarget` can be used
freely across contexts because `GLRenderTargetImpl` creates a framebuffer
object per context internally, while its texture and renderbuffer resources
(which are natively shareable) stay shared. `end_render` restores whichever
framebuffer object (or the main framebuffer) was bound before `begin_render`,
so nesting or interleaving render targets does not require callers to track
prior bindings themselves. As with the other `GL*Object` wrappers,
`boost::shared_ptr` rather than `non_null_intrusive_ptr` is used deliberately,
so instances can be held in a `GPlatesUtils::ObjectCache`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLRenderTarget`](#gplatesopenglglrendertarget) | class | `boost::noncopyable` | — | 0 | Used to render to a fixed-dimension texture (with optional associated hardware depth/stencil buffer). |

## Members

### `GPlatesOpenGL::GLRenderTarget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_type` | typedef | `boost::shared_ptr<GLRenderTarget>` | public | A convenience typedef for a shared pointer to a GLRenderTarget. |
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const GLRenderTarget>` | public | — |
| `is_supported( GLRenderer &renderer, GLint texture_internalformat, bool include_depth_buffer, bool include_stencil_buffer, unsigned int render_target_width, unsigned int render_target_height)` | method | `bool` | public | Returns true if the texture internal format and optional depth/stencil buffer combination are supported by the runtime system (also requires support for GL\_EXT\_framebuffer\_object). |
| `create( GLRenderer &renderer, GLint texture_internalformat, bool include_depth_buffer, bool include_stencil_buffer, unsigned int render_target_width, unsigned int render_target_height)` | method | `shared_ptr_type` | public | Creates a shared pointer to a GLRenderTarget object. |
| `create_as_unique_ptr( GLRenderer &renderer, GLint texture_internalformat, bool include_depth_buffer, bool include_stencil_buffer, unsigned int render_target_width, unsigned int render_target_height)` | method | `std::unique_ptr<GLRenderTarget>` | public | Same as create but returns a std::unique\_ptr - to guarantee only one owner. |
| `begin_render( GLRenderer &renderer)` | method | `void` | public | Binds the internal framebuffer object for rendering to the internal texture and optional depth buffer. |
| `end_render( GLRenderer &renderer)` | method | `void` | public | Binds the framebuffer object that was bound when begin\_render was called, or the main framebuffer if no framebuffer object was bound. |
| `RenderScope` | class | `None` | public | RAII class to call begin\_render and end\_render over a scope. |
| `get_texture()` | method | `GLTexture::shared_ptr_to_const_type` | public | Returns the render texture. |
| `d_impl` | field | `GLRenderTargetImpl` | private | The render target implementation. |
| `GLRenderTarget( GLRenderer &renderer, GLint texture_internalformat, bool include_depth_buffer, bool include_stencil_buffer, unsigned int render_target_width, unsigned int render_target_height)` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLRENDERTARGET_H` | macro | `None` | — |

## Notes

`get_texture` throws if called while rendering is in progress (between
`begin_render` and `end_render`), since the texture cannot be safely sampled
until rendering to it has finished. `is_supported` must be checked before
`create`: besides `GL_EXT_framebuffer_object`, a stencil buffer additionally
requires `GL_EXT_packed_depth_stencil` (most consumer hardware only supports a
stencil attachment packed together with depth), and non-power-of-two
dimensions require non-power-of-two texture support.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLScreenRenderTarget](GLScreenRenderTarget.md) | opengl | 13 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 9 |
| [opengl/GLContext](GLContext.md) | opengl | 8 |
| [opengl/GLScalarField3DGenerator](GLScalarField3DGenerator.md) | opengl | 6 |
| [opengl/GLScalarField3D](GLScalarField3D.md) | opengl | 4 |
| [gui/CommandServer](../gui/CommandServer.md) | gui | 2 |
| [gui/Globe](../gui/Globe.md) | gui | 2 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 2 |
| [qt-widgets/ImportScalarField3DDialog](../qt-widgets/ImportScalarField3DDialog.md) | qt-widgets | 2 |
| [api/PyCoregistrationLayerProxy](../api/PyCoregistrationLayerProxy.md) | api | 1 |
| [gui/ExportCoRegistrationAnimationStrategy](../gui/ExportCoRegistrationAnimationStrategy.md) | gui | 1 |
| [presentation/ScalarField3DVisualLayerParams](../presentation/ScalarField3DVisualLayerParams.md) | presentation | 1 |
| [qt-widgets/CoRegistrationResultTableDialog](../qt-widgets/CoRegistrationResultTableDialog.md) | qt-widgets | 1 |
| [qt-widgets/MapCanvas](../qt-widgets/MapCanvas.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLRenderTarget.h
python scripts/gpq.py def GPlatesOpenGL::GLRenderTarget --body
python scripts/gpq.py uses GLRenderTarget --kind class
python scripts/gpq.py hier GLRenderTarget
```
