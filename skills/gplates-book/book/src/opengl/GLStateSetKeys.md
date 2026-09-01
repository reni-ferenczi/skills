# GLStateSetKeys

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 604 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLStateSetKeys.h` | C++ | 328 |
| `src/opengl/GLStateSetKeys.cc` | C++ | 563 |

## Overview

[[[PROSE overview unit=opengl/GLStateSetKeys tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLStateSetKeys`](#gplatesopenglglstatesetkeys) | class | [`GPlatesUtils::ReferenceCount<GLStateSetKeys>`](../utils/ReferenceCount.md) | — | 0 | Used to assign a separate slot for each GLStateSet derived state. |

## Members

### `GPlatesOpenGL::GLStateSetKeys`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLStateSetKeys>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLStateSetKeys>` | public | — |
| `key_type` | typedef | `unsigned int` | public | Typedef for a state set key. |
| `create( const GLCapabilities &capabilities)` | method | `non_null_ptr_to_const_type` | public | Creates an immutable GLStateSetKeys object. |
| `get_num_state_set_keys()` | method | `unsigned int` | public | Returns the total number of state set keys. |
| `(anonymous enum)` | enum | `None` | public | These keys can be used directly. |
| `get_bind_buffer_object_key( GLenum target)` | method | `key_type` | public | For binding buffer objects (objects that target GL\_ARB\_vertex\_buffer\_object extension). |
| `get_enable_key( GLenum cap)` | method | `key_type` | public | For glEnable with non-texture targets. |
| `get_polygon_mode_key( GLenum face)` | method | `key_type` | public | For glPolygonMode. |
| `get_hint_key( GLenum target)` | method | `key_type` | public | For glHint. |
| `get_texture_enable_key( GLenum texture_unit, GLenum texture_target)` | method | `key_type` | public | For glEnable with texture targets. |
| `get_bind_texture_key( GLenum texture_unit, GLenum texture_target)` | method | `key_type` | public | — |
| `get_tex_env_key( GLenum texture_unit, GLenum target, GLenum pname)` | method | `key_type` | public | — |
| `get_tex_gen_key( GLenum texture_unit, GLenum coord, GLenum pname)` | method | `key_type` | public | — |
| `get_enable_client_texture_state_key( GLenum texture_unit)` | method | `key_type` | public | — |
| `get_tex_coord_pointer_state_key( GLenum texture_unit)` | method | `key_type` | public | — |
| `get_enable_client_state_key( GLenum array)` | method | `key_type` | public | — |
| `get_enable_vertex_attrib_array_key( GLuint attribute_index)` | method | `key_type` | public | — |
| `get_vertex_attrib_array_key( GLuint attribute_index)` | method | `key_type` | public | — |
| `get_load_matrix_key( GLenum mode)` | method | `key_type` | public | — |
| `get_load_texture_matrix_key( GLenum texture_unit)` | method | `key_type` | public | — |
| `GenericVertexAttributeKeyOffsetType` | enum | `None` | private | Key offsets within a particular generic vertex attribute index - offsets repeat for each subsequent index. |
| `TextureImageUnitKeyOffsetType` | enum | `None` | private | Key offsets within a particular texture \*image\* unit - offsets repeat for each subsequent texture unit. |
| `TextureCoordKeyOffsetType` | enum | `None` | private | Key offsets within a particular texture \*coordinate\* set - offsets repeat for each subsequent texture unit. |
| `d_capabilities` | field | `GLCapabilities` | private | — |
| `d_generic_vertex_attribute_index_zero_base_key` | field | `key_type` | private | — |
| `d_texture_image_unit_zero_base_key` | field | `key_type` | private | — |
| `d_texture_coord_zero_base_key` | field | `key_type` | private | — |
| `d_num_state_set_keys` | field | `unsigned int` | private | — |
| `GLStateSetKeys( const GLCapabilities &capabilities)` | constructor | `None` | private | Default constructor can only be called by create. |
| `get_texture_image_unit_key_from_key_offset( GLenum texture_unit, TextureImageUnitKeyOffsetType key_offset)` | method | `key_type` | private | Calculate a key for a texture parameter in the specified texture \*image\* unit. |
| `get_texture_coord_key_from_key_offset( GLenum texture_unit, TextureCoordKeyOffsetType key_offset)` | method | `key_type` | private | Calculate a key for a texture parameter for the specified texture \*coordinate\* set. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLSTATESETKEYS_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLStateSetKeys tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLState](GLState.md) | opengl | 247 |
| [opengl/GLStateStore](GLStateStore.md) | opengl | 5 |
| [opengl/GLContext](GLContext.md) | opengl | 2 |
| [opengl/GLMultiResolutionRaster](GLMultiResolutionRaster.md) | opengl | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLStateSetKeys.h
python scripts/gpq.py def GPlatesOpenGL::GLStateSetKeys --body
python scripts/gpq.py uses GLStateSetKeys --kind class
python scripts/gpq.py hier GLStateSetKeys
```
