# GLStateSetStore

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 188 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLStateSetStore.h` | C++ | 118 |

## Overview

`GLStateSetStore` is a plain aggregate of `GPlatesUtils::ObjectPool` instances,
one per concrete `GLStateSet` subclass declared in `GLStateSets.h` (bind
targets, `glEnable` flags, matrix loads, vertex pointers, and so on). Each
`GLState` change constructs one of these small immutable state-set objects,
and rather than `new`/`delete` per change, it draws and returns instances from
the matching pool here — a fixed, type-safe alternative to a single
heterogeneous allocator for the very high churn of per-frame state objects.

`GLContext::SharedState::get_state_store` creates one lazily, together with a
`GLStateSetKeys`, and hands both to `GLStateStore`; callers reach it through
that shared state rather than constructing it directly, since the constructor
is private and only invoked via `create`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLStateSetStore`](#gplatesopenglglstatesetstore) | class | [`GPlatesUtils::ReferenceCount<GLStateSetStore>`](../utils/ReferenceCount.md) | — | 0 | Manages allocation of derived GLStateSet classes using a separate object pool for each type. |

## Members

### `GPlatesOpenGL::GLStateSetStore`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLStateSetStore>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLStateSetStore>` | public | — |
| `create()` | method | `non_null_ptr_type` | public | Creates a GLStateSetStore object. |
| `active_texture_state_sets` | field | `GPlatesUtils::ObjectPool<GLActiveTextureStateSet>` | public | Alphabetically ordered... |
| `alpha_func_state_sets` | field | `GPlatesUtils::ObjectPool<GLAlphaFuncStateSet>` | public | — |
| `bind_buffer_object_state_sets` | field | `GPlatesUtils::ObjectPool<GLBindBufferObjectStateSet>` | public | — |
| `bind_frame_buffer_object_state_sets` | field | `GPlatesUtils::ObjectPool<GLBindFrameBufferObjectStateSet>` | public | — |
| `bind_program_object_state_sets` | field | `GPlatesUtils::ObjectPool<GLBindProgramObjectStateSet>` | public | — |
| `bind_texture_state_sets` | field | `GPlatesUtils::ObjectPool<GLBindTextureStateSet>` | public | — |
| `bind_vertex_array_object_state_sets` | field | `GPlatesUtils::ObjectPool<GLBindVertexArrayObjectStateSet>` | public | — |
| `blend_equation_state_sets` | field | `GPlatesUtils::ObjectPool<GLBlendEquationStateSet>` | public | — |
| `blend_func_state_sets` | field | `GPlatesUtils::ObjectPool<GLBlendFuncStateSet>` | public | — |
| `clear_color_state_sets` | field | `GPlatesUtils::ObjectPool<GLClearColorStateSet>` | public | — |
| `clear_depth_state_sets` | field | `GPlatesUtils::ObjectPool<GLClearDepthStateSet>` | public | — |
| `clear_stencil_state_sets` | field | `GPlatesUtils::ObjectPool<GLClearStencilStateSet>` | public | — |
| `client_active_texture_state_sets` | field | `GPlatesUtils::ObjectPool<GLClientActiveTextureStateSet>` | public | — |
| `color_mask_state_sets` | field | `GPlatesUtils::ObjectPool<GLColorMaskStateSet>` | public | — |
| `color_pointer_state_sets` | field | `GPlatesUtils::ObjectPool<GLColorPointerStateSet>` | public | — |
| `cull_face_state_sets` | field | `GPlatesUtils::ObjectPool<GLCullFaceStateSet>` | public | — |
| `depth_func_state_sets` | field | `GPlatesUtils::ObjectPool<GLDepthFuncStateSet>` | public | — |
| `depth_mask_state_sets` | field | `GPlatesUtils::ObjectPool<GLDepthMaskStateSet>` | public | — |
| `depth_range_state_sets` | field | `GPlatesUtils::ObjectPool<GLDepthRangeStateSet>` | public | — |
| `enable_client_state_state_sets` | field | `GPlatesUtils::ObjectPool<GLEnableClientStateStateSet>` | public | — |
| `enable_client_texture_state_state_sets` | field | `GPlatesUtils::ObjectPool<GLEnableClientTextureStateStateSet>` | public | — |
| `enable_state_sets` | field | `GPlatesUtils::ObjectPool<GLEnableStateSet>` | public | — |
| `enable_texture_state_sets` | field | `GPlatesUtils::ObjectPool<GLEnableTextureStateSet>` | public | — |
| `enable_vertex_attrib_array_state_sets` | field | `GPlatesUtils::ObjectPool<GLEnableVertexAttribArrayStateSet>` | public | — |
| `front_face_state_sets` | field | `GPlatesUtils::ObjectPool<GLFrontFaceStateSet>` | public | — |
| `hint_state_sets` | field | `GPlatesUtils::ObjectPool<GLHintStateSet>` | public | — |
| `line_width_state_sets` | field | `GPlatesUtils::ObjectPool<GLLineWidthStateSet>` | public | — |
| `load_matrix_state_sets` | field | `GPlatesUtils::ObjectPool<GLLoadMatrixStateSet>` | public | — |
| `load_texture_matrix_state_sets` | field | `GPlatesUtils::ObjectPool<GLLoadTextureMatrixStateSet>` | public | — |
| `matrix_mode_state_sets` | field | `GPlatesUtils::ObjectPool<GLMatrixModeStateSet>` | public | — |
| `point_size_state_sets` | field | `GPlatesUtils::ObjectPool<GLPointSizeStateSet>` | public | — |
| `polygon_mode_state_sets` | field | `GPlatesUtils::ObjectPool<GLPolygonModeStateSet>` | public | — |
| `polygon_offset_state_sets` | field | `GPlatesUtils::ObjectPool<GLPolygonOffsetStateSet>` | public | — |
| `normal_pointer_state_sets` | field | `GPlatesUtils::ObjectPool<GLNormalPointerStateSet>` | public | — |
| `scissor_state_sets` | field | `GPlatesUtils::ObjectPool<GLScissorStateSet>` | public | — |
| `stencil_func_state_sets` | field | `GPlatesUtils::ObjectPool<GLStencilFuncStateSet>` | public | — |
| `stencil_mask_state_sets` | field | `GPlatesUtils::ObjectPool<GLStencilMaskStateSet>` | public | — |
| `stencil_op_state_sets` | field | `GPlatesUtils::ObjectPool<GLStencilOpStateSet>` | public | — |
| `tex_coord_pointer_state_sets` | field | `GPlatesUtils::ObjectPool<GLTexCoordPointerStateSet>` | public | — |
| `tex_gen_state_sets` | field | `GPlatesUtils::ObjectPool<GLTexGenStateSet>` | public | — |
| `tex_env_state_sets` | field | `GPlatesUtils::ObjectPool<GLTexEnvStateSet>` | public | — |
| `vertex_attrib_array_state_sets` | field | `GPlatesUtils::ObjectPool<GLVertexAttribPointerStateSet>` | public | — |
| `vertex_pointer_state_sets` | field | `GPlatesUtils::ObjectPool<GLVertexPointerStateSet>` | public | — |
| `viewport_state_sets` | field | `GPlatesUtils::ObjectPool<GLViewportStateSet>` | public | — |
| `GLStateSetStore()` | constructor | `None` | private | Constructor. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLSTATESETSTORE_H` | macro | `None` | — |

## Notes

Adding a new `GLStateSet` subclass requires adding a matching `ObjectPool`
field here as well — nothing enforces the pairing at compile time.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLState](GLState.md) | opengl | 79 |
| [opengl/GLStateStore](GLStateStore.md) | opengl | 5 |
| [opengl/GLContext](GLContext.md) | opengl | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLStateSetStore.h
python scripts/gpq.py def GPlatesOpenGL::GLStateSetStore --body
python scripts/gpq.py uses GLStateSetStore --kind class
python scripts/gpq.py hier GLStateSetStore
```
