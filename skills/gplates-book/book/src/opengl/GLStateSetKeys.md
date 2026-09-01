# GLStateSetKeys

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 604 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLStateSetKeys.h` | C++ | 328 |
| `src/opengl/GLStateSetKeys.cc` | C++ | 563 |

## Overview

`GLStateSetKeys` maps every distinct piece of OpenGL state that GPlates tracks
(a `glEnable` capability, a bound buffer target, a texture-unit parameter, a
generic vertex attribute, and so on) onto a small dense integer, `key_type`.
That key is what `GLState` uses to index its array of current `GLStateSet`
values, so setting or querying a piece of state is an array lookup rather than
a map lookup or a chain of comparisons.

State that exists regardless of the GPU (like `glEnable(GL_BLEND)` or
`glDepthFunc`) gets a fixed key from the anonymous enum. State whose extent
depends on the driver's reported limits — the number of texture image units,
texture coordinate sets, or generic vertex attributes — cannot be enumerated
at compile time, so `GLStateSetKeys` allocates a base key for each such
category after the fixed keys and computes per-unit keys by adding a
fixed per-unit offset (`TextureImageUnitKeyOffsetType`,
`TextureCoordKeyOffsetType`, `GenericVertexAttributeKeyOffsetType`) multiplied
by the unit or attribute index onto that base. `create` builds one instance
from the queried `GLCapabilities`, after which `get_num_state_set_keys`
reports the total the caller must size its state array to.

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

- The instance is immutable once created (`create` returns a
  `non_null_ptr_to_const_type`), and its key layout is fixed for the lifetime
  of the `GLCapabilities` it was built from — the number and offsets of keys
  depend on driver-reported limits, so a `GLStateSetKeys` built for one
  context is not valid for another with different capabilities.
- `get_polygon_mode_key` requires the caller to split `GL_FRONT_AND_BACK`
  into separate `GL_FRONT` and `GL_BACK` requests; passing it directly is not
  handled.
- Unsupported enum values passed to the `get_*_key` methods trigger
  `GPlatesGlobal::Abort` rather than returning an error code.

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
