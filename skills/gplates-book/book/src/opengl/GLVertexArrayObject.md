# GLVertexArrayObject

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 552 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLVertexArrayObject.h` | C++ | 451 |
| `src/opengl/GLVertexArrayObject.cc` | C++ | 331 |

## Overview

[[[PROSE overview unit=opengl/GLVertexArrayObject tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLVertexArrayObject`](#gplatesopenglglvertexarrayobject) | class | [`GLVertexArray`](GLVertexArray.md)<br>[`GLObject`](GLObject.md) | — | 0 | An OpenGL object that encapsulates vertex array state. |

## Members

### `GPlatesOpenGL::GLVertexArrayObject`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_type` | typedef | `boost::shared_ptr<GLVertexArrayObject>` | public | A convenience typedef for a shared pointer to a GLVertexArrayObject. |
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const GLVertexArrayObject>` | public | — |
| `weak_ptr_type` | typedef | `boost::weak_ptr<GLVertexArrayObject>` | public | A convenience typedef for a weak pointer to a GLVertexArrayObject. |
| `weak_ptr_to_const_type` | typedef | `boost::weak_ptr<const GLVertexArrayObject>` | public | — |
| `resource_handle_type` | typedef | `GLuint` | public | Typedef for a resource handle. |
| `Allocator` | class | `None` | public | Policy class to allocate and deallocate OpenGL vertex array objects. |
| `resource_type` | typedef | `GLObjectResource<resource_handle_type, Allocator>` | public | Typedef for a resource. |
| `resource_manager_type` | typedef | `GLObjectResourceManager<resource_handle_type, Allocator>` | public | Typedef for a resource manager. |
| `create( GLRenderer &renderer)` | method | `shared_ptr_type` | public | Creates a shared pointer to a GLVertexArrayObject object. |
| `create_as_unique_ptr( GLRenderer &renderer)` | method | `std::unique_ptr<GLVertexArrayObject>` | public | Same as create but returns a std::unique\_ptr - to guarantee only one owner. |
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
| `get_vertex_array_resource( GLRenderer &renderer, resource_handle_type &resource_handle, boost::shared_ptr<GLState> &current_resource_state, boost::shared_ptr<const GLState> &target_resource_state)` | method | `void` | public | Returns the vertex array resource handle (and current resource state) associated with the specified context. |
| `ContextObjectState` | struct | `None` | private | The vertex array object state as currently set in each OpenGL context. |
| `context_object_state_seq_type` | typedef | `std::vector<ContextObjectState>` | private | Typedef for a sequence of context object states. |
| `d_context_object_states` | field | `context_object_state_seq_type` | private | The vertex array object state for each context that we've encountered. |
| `d_object_state` | field | `GLVertexArrayImpl::shared_ptr_type` | private | Object state as last set for the OpenGL context that resource was created in. |
| `GLVertexArrayObject( GLRenderer &renderer)` | constructor | `None` | private | Constructor. |
| `get_object_state_for_current_context` | field | `ContextObjectState` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLVERTEXARRAYOBJECT_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLVertexArrayObject tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLRenderer](GLRenderer.md) | opengl | 15 |
| [opengl/GLState](GLState.md) | opengl | 7 |
| [opengl/GLStateSets](GLStateSets.md) | opengl | 5 |
| [opengl/GLContext](GLContext.md) | opengl | 4 |
| [opengl/GLVertexArray](GLVertexArray.md) | opengl | 2 |
| [opengl/GLObjectResourceManager](GLObjectResourceManager.md) | opengl | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLVertexArrayObject.h
python scripts/gpq.py def GPlatesOpenGL::GLVertexArrayObject --body
python scripts/gpq.py uses GLVertexArrayObject --kind class
python scripts/gpq.py hier GLVertexArrayObject
```
