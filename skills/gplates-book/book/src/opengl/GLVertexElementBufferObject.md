# GLVertexElementBufferObject

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 531 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLVertexElementBufferObject.h` | C++ | 156 |
| `src/opengl/GLVertexElementBufferObject.cc` | C++ | 89 |

## Overview

[[[PROSE overview unit=opengl/GLVertexElementBufferObject tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLVertexElementBufferObject`](#gplatesopenglglvertexelementbufferobject) | class | [`GLVertexElementBuffer`](GLVertexElementBuffer.md)<br>[`GLObject`](GLObject.md) | — | 0 | An OpenGL buffer object used to stored vertex elements (vertex indices) but \*not\* vertex attributes (vertices). |

## Members

### `GPlatesOpenGL::GLVertexElementBufferObject`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_type` | typedef | `boost::shared_ptr<GLVertexElementBufferObject>` | public | A convenience typedef for a shared pointer to a GLVertexElementBufferObject. |
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const GLVertexElementBufferObject>` | public | — |
| `weak_ptr_type` | typedef | `boost::weak_ptr<GLVertexElementBufferObject>` | public | A convenience typedef for a weak pointer to a GLVertexElementBufferObject. |
| `weak_ptr_to_const_type` | typedef | `boost::weak_ptr<const GLVertexElementBufferObject>` | public | — |
| `get_target_type()` | method | `GLenum` | public | Returns the target GL\_ELEMENT\_ARRAY\_BUFFER\_ARB. |
| `create( GLRenderer &renderer, const GLBufferObject::shared_ptr_type &buffer)` | method | `shared_ptr_type` | public | Creates a shared pointer to a GLVertexElementBufferObject object. |
| `create_as_unique_ptr( GLRenderer &renderer, const GLBufferObject::shared_ptr_type &buffer)` | method | `std::unique_ptr<GLVertexElementBufferObject>` | public | Same as create but returns a std::unique\_ptr - to guarantee only one owner. |
| `get_buffer()` | method | `GLBuffer::shared_ptr_to_const_type` | public | Returns the buffer used to store vertex element data (indices). |
| `gl_bind( GLRenderer &renderer)` | method | `void` | public | Binds this vertex element buffer so that vertex element data is sourced from it. |
| `gl_draw_range_elements( GLRenderer &renderer, GLenum mode, GLuint start, GLuint end, GLsizei count, GLenum type, GLint indices_offset)` | method | `void` | public | Performs the equivalent of the OpenGL command 'glDrawRangeElements'. |
| `get_buffer_object()` | method | `GLBufferObject::shared_ptr_to_const_type` | public | Returns the buffer object. |
| `d_buffer` | field | `GLBufferObject::shared_ptr_type` | private | — |
| `GLVertexElementBufferObject( GLRenderer &renderer, const GLBufferObject::shared_ptr_type &buffer)` | constructor | `None` | private | Constructor. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLVERTEXELEMENTBUFFEROBJECT_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLVertexElementBufferObject tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLRenderer](GLRenderer.md) | opengl | 4 |
| [opengl/GLVertexElementBuffer](GLVertexElementBuffer.md) | opengl | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLVertexElementBufferObject.h
python scripts/gpq.py def GPlatesOpenGL::GLVertexElementBufferObject --body
python scripts/gpq.py uses GLVertexElementBufferObject --kind class
python scripts/gpq.py hier GLVertexElementBufferObject
```
