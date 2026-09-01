# GLScreenRenderTarget

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 1042 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLScreenRenderTarget.h` | C++ | 201 |
| `src/opengl/GLScreenRenderTarget.cc` | C++ | 130 |

## Overview

`GLScreenRenderTarget` wraps an off-screen `GLTexture` (with an optional depth and/or stencil buffer) sized to the viewport, for render passes that need to draw to a texture rather than the main framebuffer — for example the intermediate surface-fill-mask and volume-fill passes in `GLScalarField3D`. `begin_render()`/`end_render()` bracket the pass, resizing the underlying storage to the requested dimensions and rebinding whatever framebuffer object was active beforehand when the scope ends; `RenderScope` is an RAII wrapper around that pair for exception-safe use. Unlike a raw OpenGL framebuffer object, which cannot be shared across contexts, `GLScreenRenderTarget` creates one underlying FBO per context it is used from internally, so a single instance — and the texture/renderbuffer it wraps — can be reused freely across multiple `GLRenderer` contexts.

`is_supported()` gates the requested texture-internal-format/depth/stencil combination against `GL_EXT_framebuffer_object`, non-power-of-two texture support (since the target tracks the viewport size), and `GL_EXT_packed_depth_stencil` when a stencil buffer is requested.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLScreenRenderTarget`](#gplatesopenglglscreenrendertarget) | class | `boost::noncopyable` | — | 0 | Used to render to a screen-size texture (with optional associated hardware depth buffer). |

## Members

### `GPlatesOpenGL::GLScreenRenderTarget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_type` | typedef | `boost::shared_ptr<GLScreenRenderTarget>` | public | A convenience typedef for a shared pointer to a GLScreenRenderTarget. |
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const GLScreenRenderTarget>` | public | — |
| `is_supported( GLRenderer &renderer, GLint texture_internalformat, bool include_depth_buffer, bool include_stencil_buffer)` | method | `bool` | public | Returns true if the texture internal format and optional depth/stencil buffer combination are supported by the runtime system (also requires support for GL\_EXT\_framebuffer\_object). |
| `create( GLRenderer &renderer, GLint texture_internalformat, bool include_depth_buffer, bool include_stencil_buffer)` | method | `shared_ptr_type` | public | Creates a shared pointer to a GLScreenRenderTarget object. |
| `create_as_unique_ptr( GLRenderer &renderer, GLint texture_internalformat, bool include_depth_buffer, bool include_stencil_buffer)` | method | `std::unique_ptr<GLScreenRenderTarget>` | public | Same as create but returns a std::unique\_ptr - to guarantee only one owner. |
| `begin_render( GLRenderer &renderer, unsigned int render_target_width, unsigned int render_target_height)` | method | `void` | public | Ensures internal texture (and optional depth buffer) have a storage allocation of the specified dimensions and binds the internal framebuffer object for rendering to them. |
| `end_render( GLRenderer &renderer)` | method | `void` | public | Binds the framebuffer object that was bound when begin\_render was called, or the main framebuffer if no framebuffer object was bound. |
| `RenderScope` | class | `None` | public | RAII class to call begin\_render and end\_render over a scope. |
| `get_texture()` | method | `GLTexture::shared_ptr_to_const_type` | public | Returns the render texture. |
| `d_impl` | field | `GLRenderTargetImpl` | private | The render target implementation. |
| `GLScreenRenderTarget( GLRenderer &renderer, GLint texture_internalformat, bool include_depth_buffer, bool include_stencil_buffer)` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLSCREENRENDERTARGET_H` | macro | `None` | — |

## Notes

- `get_texture()` throws if called between `begin_render()` and `end_render()` — the texture cannot be read while it is still the active render target.
- Instances are held by `boost::shared_ptr` rather than the usual `non_null_intrusive_ptr` specifically so they can live in a `GPlatesUtils::ObjectCache`; use `create_as_unique_ptr()` instead when single ownership must be guaranteed.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLScalarField3D](GLScalarField3D.md) | opengl | 11 |
| [opengl/GLContext](GLContext.md) | opengl | 8 |
| [opengl/GLOffScreenContext](GLOffScreenContext.md) | opengl | 4 |
| [gui/Globe](../gui/Globe.md) | gui | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLScreenRenderTarget.h
python scripts/gpq.py def GPlatesOpenGL::GLScreenRenderTarget --body
python scripts/gpq.py uses GLScreenRenderTarget --kind class
python scripts/gpq.py hier GLScreenRenderTarget
```
