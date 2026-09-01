# GLRenderTargetImpl

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 532 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLRenderTargetImpl.h` | C++ | 248 |
| `src/opengl/GLRenderTargetImpl.cc` | C++ | 425 |

## Overview

Holds the actual OpenGL resources and framebuffer logic shared by
`GLRenderTarget` (fixed-size) and `GLScreenRenderTarget` (screen-size), which
each own one by value and forward `begin_render`/`end_render`/`get_texture`
to it. `set_render_target_dimensions` (re)allocates the texture's and any
depth/stencil `GLRenderBufferObject`'s storage; it must be called at least
once before the first `begin_render`, and cannot be called while rendering is
in progress.

The core problem it solves is that native framebuffer objects cannot be
shared across OpenGL contexts, while the texture and renderbuffer resources
they wrap around can. `GLRenderTargetImpl` resolves this by keeping one
`ContextObjectState` — its own `GLFrameBufferObject` plus an
attached-or-not flag — per `GLContext` it has been used from, recreating a
framebuffer object for each newly encountered context but reusing the same
underlying texture and renderbuffers everywhere. This lets a single instance,
and hence a single `GLRenderTarget`, be shared freely across contexts without
its owner needing to special-case the framebuffer object itself.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLRenderTargetImpl`](#gplatesopenglglrendertargetimpl) | class | `boost::noncopyable` | — | 0 | Implementation used to render to both fixed-size and screen-size textures (with optional associated hardware depth/stencil buffer). |

## Members

### `GPlatesOpenGL::GLRenderTargetImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `is_supported( GLRenderer &renderer, GLint texture_internalformat, bool include_depth_buffer, bool include_stencil_buffer)` | method | `bool` | public | Returns true if the texture internal format and optional depth/stencil buffer combination are supported by the runtime system (also requires support for GL\_EXT\_framebuffer\_object). |
| `GLRenderTargetImpl( GLRenderer &renderer, GLint texture_internalformat, bool include_depth_buffer, bool include_stencil_buffer)` | constructor | `None` | public | — |
| `set_render_target_dimensions( GLRenderer &renderer, unsigned int render_target_width, unsigned int render_target_height)` | method | `void` | public | Ensures internal texture (and optional depth/stencil buffer) have a storage allocation of the specified dimensions. |
| `begin_render( GLRenderer &renderer)` | method | `void` | public | Binds the internal framebuffer object for rendering to the internal texture and optional depth buffer. |
| `end_render( GLRenderer &renderer)` | method | `void` | public | Binds the framebuffer object that was bound when begin\_render was called, or the main framebuffer if no framebuffer object was bound. |
| `get_texture()` | method | `GLTexture::shared_ptr_to_const_type` | public | Returns the render texture. |
| `ContextObjectState` | struct | `None` | private | The framebuffer object state as currently set in each OpenGL context. |
| `context_object_state_seq_type` | typedef | `std::vector<ContextObjectState>` | private | Typedef for a sequence of context object states. |
| `RenderInfo` | struct | `None` | private | Information kept during a begin\_render / end\_render pair. |
| `RenderBuffer` | struct | `None` | private | Information for a depth/stencil render buffer. |
| `d_context_object_states` | field | `context_object_state_seq_type` | private | The vertex array object state for each context that we've encountered. |
| `d_texture` | field | `GLTexture::shared_ptr_type` | private | — |
| `d_texture_internalformat` | field | `GLint` | private | — |
| `d_depth_buffer` | field | `boost::optional<RenderBuffer>` | private | — |
| `d_stencil_buffer` | field | `boost::optional<RenderBuffer>` | private | — |
| `d_allocated_storage` | field | `bool` | private | Is false if we've not yet allocated storage for the texture and depth buffer. |
| `d_current_render_info` | field | `boost::optional<RenderInfo>` | private | Render information kept between begin\_render and end\_render. |
| `get_frame_buffer_object( GLRenderer &renderer)` | method | `GLFrameBufferObject::shared_ptr_type` | private | Returns the framebuffer associated with the OpenGL context used by the specified renderer. |
| `get_object_state_for_current_context` | field | `ContextObjectState` | private | — |
| `is_currently_rendering()` | method | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLRENDERTARGETIMPL_H` | macro | `None` | — |

## Notes

`end_render` restores whatever framebuffer object (or the main framebuffer)
was bound at the matching `begin_render`, recorded in `d_current_render_info`,
so callers do not need to save and restore bindings themselves. `get_texture`
throws if called between `begin_render` and `end_render`, since the texture
cannot be read while it is still a render target. `ContextObjectState`
deliberately stores its `GLContext` as a raw pointer rather than a shared
pointer to avoid a reference cycle. Requiring a stencil buffer additionally
requires `GL_EXT_packed_depth_stencil`, since most consumer hardware only
supports a stencil attachment packed together with depth.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLVertexArrayObject](GLVertexArrayObject.md) | opengl | 10 |
| [opengl/GLRenderTarget](GLRenderTarget.md) | opengl | 4 |
| [opengl/GLScreenRenderTarget](GLScreenRenderTarget.md) | opengl | 4 |
| [opengl/GLContextImpl](GLContextImpl.md) | opengl | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLRenderTargetImpl.h
python scripts/gpq.py def GPlatesOpenGL::GLRenderTargetImpl --body
python scripts/gpq.py uses GLRenderTargetImpl --kind class
python scripts/gpq.py hier GLRenderTargetImpl
```
