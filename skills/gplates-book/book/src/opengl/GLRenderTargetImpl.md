# GLRenderTargetImpl

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 532 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLRenderTargetImpl.h` | C++ | 248 |
| `src/opengl/GLRenderTargetImpl.cc` | C++ | 425 |

## Overview

[[[PROSE overview unit=opengl/GLRenderTargetImpl tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=opengl/GLRenderTargetImpl tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
