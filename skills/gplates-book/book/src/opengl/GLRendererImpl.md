# GLRendererImpl

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 300 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLRendererImpl.h` | C++ | 397 |

## Overview

[[[PROSE overview unit=opengl/GLRendererImpl tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLRendererImpl::StateBlock`](#gplatesopenglglrendererimplstateblock) | class | — | — | 0 | Keeps track of all state sets within a state block scope. |
| [`GPlatesOpenGL::GLRendererImpl::state_block_stack_type`](#gplatesopenglglrendererimplstate_block_stack_type) | typedef | — | — | 0 | Typedef for a stack of state blocks. |
| [`GPlatesOpenGL::GLRendererImpl::Drawable`](#gplatesopenglglrendererimpldrawable) | struct | [`GPlatesUtils::ReferenceCount<Drawable>`](../utils/ReferenceCount.md) | — | 0 | Interface for the various draw calls - so we can wrap them up for a render queue is requested. |
| [`GPlatesOpenGL::GLRendererImpl::RenderOperation`](#gplatesopenglglrendererimplrenderoperation) | struct | — | — | 0 | Used when drawables are added to a render queue instead of being rendered immediately. |
| [`GPlatesOpenGL::GLRendererImpl::RenderQueue`](#gplatesopenglglrendererimplrenderqueue) | struct | [`GPlatesUtils::ReferenceCount<RenderQueue>`](../utils/ReferenceCount.md) | — | 0 | A sequence of RenderOperation objects batched up in a queue for later rendering. |
| [`GPlatesOpenGL::GLRendererImpl::render_queue_stack_type`](#gplatesopenglglrendererimplrender_queue_stack_type) | typedef | — | — | 0 | Typedef for a stack of render queues. |
| [`GPlatesOpenGL::GLRendererImpl::frame_buffer_draw_count_type`](#gplatesopenglglrendererimplframe_buffer_draw_count_type) | typedef | — | — | 0 | Typedef for a counter for the number of draws to any framebuffer. |
| [`GPlatesOpenGL::GLRendererImpl::RenderTextureTarget`](#gplatesopenglglrendererimplrendertexturetarget) | struct | — | — | 0 | Contains information for a render-to-texture target. |
| [`GPlatesOpenGL::GLRendererImpl::RenderTargetBlock`](#gplatesopenglglrendererimplrendertargetblock) | struct | — | — | 0 | Contains information for a render target block. |
| [`GPlatesOpenGL::GLRendererImpl::render_target_block_stack_type`](#gplatesopenglglrendererimplrender_target_block_stack_type) | typedef | — | — | 0 | Typedef for a stack of render targets. |

## Members

### `GPlatesOpenGL::GLRendererImpl::StateBlock`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `StateBlock( const GLState::shared_ptr_type &current_state)` | constructor | `None` | public | Constructor when current\_state is the \*full\* state. |
| `StateBlock( const GLState::shared_ptr_type &current_state, const GLState::shared_ptr_to_const_type &begin_state_to_apply)` | constructor | `None` | public | Constructor when current\_state is a state \*change\* compared to begin\_state\_to\_apply. |
| `StateBlock( const GLCompiledDrawState::non_null_ptr_type &compiled_draw_state, const GLState::shared_ptr_to_const_type &begin_state_to_apply)` | constructor | `None` | public | Constructor when compiled\_draw\_state is a state \*change\* compared to begin\_state\_to\_apply. |
| `get_state_to_apply()` | method | `GLState::shared_ptr_type` | public | Returns the current state that can be applied to OpenGL (the full state). |
| `get_cloned_state_to_apply()` | method | `GLState::shared_ptr_type` | public | Same as get\_state\_to\_apply but makes sure a copy/clone is returned. |
| `d_current_state` | field | `GLState::shared_ptr_type` | private | The snapshot of the current OpenGL state for this state block. |
| `d_begin_state_to_apply` | field | `boost::optional<GLState::shared_ptr_to_const_type>` | private | If compiling draw state in this state block... |
| `d_compiled_draw_state` | field | `boost::optional<GLCompiledDrawState::non_null_ptr_type>` | private | If compiling draw state in this state block... |
| `get_state_to_apply_from_state_change()` | method | `GLState::shared_ptr_type` | private | Returns state to apply using the compiled draw state. |

### `GPlatesOpenGL::GLRendererImpl::state_block_stack_type`

*None.*

### `GPlatesOpenGL::GLRendererImpl::Drawable`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<Drawable>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const Drawable>` | public | — |
| `~Drawable()` | destructor | `None` | public | — |
| `draw( const GLCapabilities &capabilities, const GLState &state_to_apply, GLState &last_applied_state)` | method | `void` | public | Applies that part of the state in state\_to\_apply (to OpenGL) that is used by this (derived) draw command. |

### `GPlatesOpenGL::GLRendererImpl::RenderOperation`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderOperation( GLState::shared_ptr_type state_, Drawable::non_null_ptr_to_const_type drawable_, bool modifies_frame_buffer_ = true)` | constructor | `None` | public | — |
| `state` | field | `GLState::shared_ptr_type` | public | — |
| `drawable` | field | `Drawable::non_null_ptr_to_const_type` | public | — |
| `modifies_frame_buffer` | field | `bool` | public | — |

### `GPlatesOpenGL::GLRendererImpl::RenderQueue`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<RenderQueue>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const RenderQueue>` | public | — |
| `create()` | method | `non_null_ptr_type` | public | — |
| `render_operations` | field | `std::vector<RenderOperation>` | public | — |
| `RenderQueue()` | constructor | `None` | private | — |

### `GPlatesOpenGL::GLRendererImpl::render_queue_stack_type`

*None.*

### `GPlatesOpenGL::GLRendererImpl::frame_buffer_draw_count_type`

*None.*

### `GPlatesOpenGL::GLRendererImpl::RenderTextureTarget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderTextureTarget( const GLViewport &texture_viewport_, const GLTexture::shared_ptr_to_const_type &texture_, GLint level_, bool depth_buffer_, bool stencil_buffer_)` | constructor | `None` | public | — |
| `texture_viewport` | field | `GLViewport` | public | — |
| `texture` | field | `GLTexture::shared_ptr_to_const_type` | public | — |
| `level` | field | `GLint` | public | — |
| `depth_buffer` | field | `bool` | public | — |
| `stencil_buffer` | field | `bool` | public | — |
| `tile_save_restore_state` | field | `bool` | public | Is true if should save/restore state within the current begin/end tile in render target. |
| `FrameBufferObject` | struct | `None` | public | When using framebuffer object as a render target (when GL\_EXT\_framebuffer\_object is supported). |
| `MainFrameBuffer` | struct | `None` | public | When using main framebuffer as a render target (when GL\_EXT\_framebuffer\_object is not supported). |
| `main_frame_buffer` | field | `boost::optional<MainFrameBuffer>` | public | When using main framebuffer as a render target (when GL\_EXT\_framebuffer\_object is not supported). |
| `frame_buffer_object` | field | `boost::optional<FrameBufferObject>` | public | The framebuffer object to use for render targets (when GL\_EXT\_framebuff\_object is supported). |

### `GPlatesOpenGL::GLRendererImpl::RenderTargetBlock`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderTargetBlock( const boost::optional<RenderTextureTarget> &render_texture_target_)` | constructor | `None` | public | Constructor. |
| `render_texture_target` | field | `boost::optional<RenderTextureTarget>` | public | The render-to-texture target, unless this block represents the main framebuffer. |
| `state_block_stack` | field | `state_block_stack_type` | public | Stack of currently pushed state blocks. |
| `compile_draw_state_nest_count` | field | `unsigned int` | public | The number of state blocks that are compiling/recording draw state. |
| `render_queue_stack` | field | `render_queue_stack_type` | public | Stack of currently pushed render queues. |

### `GPlatesOpenGL::GLRendererImpl::render_target_block_stack_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLRENDERERIMPL_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLRendererImpl tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLRenderer](GLRenderer.md) | opengl | 180 |
| [gui/LayerPainter](../gui/LayerPainter.md) | gui | 6 |
| [opengl/GLAgeGridMaskSource](GLAgeGridMaskSource.md) | opengl | 4 |
| [opengl/GLVisualRasterSource](GLVisualRasterSource.md) | opengl | 4 |
| [gui/CommandServer](../gui/CommandServer.md) | gui | 1 |
| [opengl/GLCompiledDrawState](GLCompiledDrawState.md) | opengl | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLRendererImpl.h
python scripts/gpq.py def GPlatesOpenGL::GLRendererImpl::StateBlock --body
python scripts/gpq.py uses StateBlock --kind class
python scripts/gpq.py hier StateBlock
```
