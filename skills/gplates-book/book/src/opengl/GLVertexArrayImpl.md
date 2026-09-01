# GLVertexArrayImpl

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 946 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLVertexArrayImpl.h` | C++ | 333 |
| `src/opengl/GLVertexArrayImpl.cc` | C++ | 278 |

## Overview

[[[PROSE overview unit=opengl/GLVertexArrayImpl tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLVertexArrayImpl`](#gplatesopenglglvertexarrayimpl) | class | [`GLVertexArray`](GLVertexArray.md) | — | 0 | An implementation of the OpenGL vertex array objects (GL\_ARB\_vertex\_array\_object extension) to simulate equivalent behaviour when the extension is not supported. |

## Members

### `GPlatesOpenGL::GLVertexArrayImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_type` | typedef | `boost::shared_ptr<GLVertexArrayImpl>` | public | A convenience typedef for a shared pointer to a GLVertexArrayImpl. |
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const GLVertexArrayImpl>` | public | — |
| `create( GLRenderer &renderer)` | method | `shared_ptr_type` | public | Creates a GLVertexArrayImpl object with no array data. |
| `create_as_unique_ptr( GLRenderer &renderer)` | method | `std::unique_ptr<GLVertexArrayImpl>` | public | Same as create but returns a std::unique\_ptr - to guarantee only one owner. |
| `gl_bind( GLRenderer &renderer)` | method | `void` | public | Binds this vertex array so that all vertex data is sourced from the vertex buffers, specified in this interface, and vertex element data is sourced from the vertex element buffer. |
| `gl_draw_range_elements( GLRenderer &renderer, GLenum mode, GLuint start, GLuint end, GLsizei count, GLenum type, GLint indices_offset)` | method | `void` | public | Performs the equivalent of the OpenGL command 'glDrawRangeElements'. |
| `clear( GLRenderer &renderer)` | method | `void` | public | Clears this vertex array. |
| `set_vertex_element_buffer( GLRenderer &renderer, const GLVertexElementBuffer::shared_ptr_to_const_type &vertex_element_buffer)` | method | `void` | public | Specify the source of vertex element (vertex indices) data. |
| `set_enable_client_state( GLRenderer &renderer, GLenum array, bool enable = true)` | method | `void` | public | Enables the specified (array) vertex array (in the fixed-function pipeline). |
| `set_enable_client_texture_state( GLRenderer &renderer, GLenum texture_unit, bool enable = true)` | method | `void` | public | Enables the vertex attribute array GL\_TEXTURE\_COORD\_ARRAY (in the fixed-function pipeline) on the specified texture unit. |
| `set_vertex_pointer( GLRenderer &renderer, const GLVertexBuffer::shared_ptr_to_const_type &vertex_buffer, GLint size, GLenum type, GLsizei stride, GLint offset)` | method | `void` | public | Specify the source of vertex position data. |
| `set_color_pointer( GLRenderer &renderer, const GLVertexBuffer::shared_ptr_to_const_type &vertex_buffer, GLint size, GLenum type, GLsizei stride, GLint offset)` | method | `void` | public | Specify the source of vertex colour data. |
| `set_normal_pointer( GLRenderer &renderer, const GLVertexBuffer::shared_ptr_to_const_type &vertex_buffer, GLenum type, GLsizei stride, GLint offset)` | method | `void` | public | Specify the source of vertex normal data. |
| `set_tex_coord_pointer( GLRenderer &renderer, const GLVertexBuffer::shared_ptr_to_const_type &vertex_buffer, GLenum texture_unit, GLint size, GLenum type, GLsizei stride, GLint offset)` | method | `void` | public | Specify the source of vertex texture coordinate data. |
| `set_enable_vertex_attrib_array( GLRenderer &renderer, GLuint attribute_index, bool enable)` | method | `void` | public | Enables the specified \*generic\* vertex attribute data at attribute index attribute\_index. |
| `set_vertex_attrib_pointer( GLRenderer &renderer, const GLVertexBuffer::shared_ptr_to_const_type &vertex_buffer, GLuint attribute_index, GLint size, GLenum type, GLboolean normalized, GLsizei stride, GLint offset)` | method | `void` | public | Specify the source of \*generic\* vertex attribute data at attribute index attribute\_index. |
| `set_vertex_attrib_i_pointer( GLRenderer &renderer, const GLVertexBuffer::shared_ptr_to_const_type &vertex_buffer, GLuint attribute_index, GLint size, GLenum type, GLsizei stride, GLint offset)` | method | `void` | public | Same as set\_vertex\_attrib\_pointer except used to specify attributes mapping to \*integer\* shader variables. |
| `set_vertex_attrib_l_pointer( GLRenderer &renderer, const GLVertexBuffer::shared_ptr_to_const_type &vertex_buffer, GLuint attribute_index, GLint size, GLenum type, GLsizei stride, GLint offset)` | method | `void` | public | Same as set\_vertex\_attrib\_pointer except used to specify attributes mapping to \*double\* shader variables. |
| `get_compiled_bind_state()` | method | `boost::shared_ptr<const GLState>` | public | Returns the compiled bind state for this vertex array. |
| `d_vertex_element_buffer` | field | `boost::optional<GLVertexElementBuffer::shared_ptr_to_const_type>` | private | The sole vertex element buffer containing vertex indices. |
| `d_compiled_bind_state` | field | `GLCompiledDrawState::non_null_ptr_type` | private | Maintains all the binding/enabling state for this vertex array. |
| `GLVertexArrayImpl( GLRenderer &renderer)` | constructor | `None` | private | Constructor. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLVERTEXARRAYIMPL_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLVertexArrayImpl tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLVertexArrayObject](GLVertexArrayObject.md) | opengl | 4 |
| [opengl/GLVertexArray](GLVertexArray.md) | opengl | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLVertexArrayImpl.h
python scripts/gpq.py def GPlatesOpenGL::GLVertexArrayImpl --body
python scripts/gpq.py uses GLVertexArrayImpl --kind class
python scripts/gpq.py hier GLVertexArrayImpl
```
