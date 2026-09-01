# GLVertexElementBufferImpl

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 659 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLVertexElementBufferImpl.h` | C++ | 125 |
| `src/opengl/GLVertexElementBufferImpl.cc` | C++ | 83 |

## Overview

`GLVertexElementBufferImpl` provides fallback element buffer (index buffer) support for OpenGL implementations that lack the vertex buffer object extension. It wraps a `GLBufferImpl` and delegates bind and draw operations to the `GLRenderer`, which implements them using client-side memory arrays via base OpenGL 1.1.

Like `GLVertexBufferImpl`, this is a compatibility layer maintaining a uniform interface across platforms that may or may not have native hardware vertex buffer support.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLVertexElementBufferImpl`](#gplatesopenglglvertexelementbufferimpl) | class | [`GLVertexElementBuffer`](GLVertexElementBuffer.md) | — | 0 | An implementation of the OpenGL buffer objects extension as used for vertex buffers containing vertex element (indices) data and \*not\* vertex attribute (vertices) data. |

## Members

### `GPlatesOpenGL::GLVertexElementBufferImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_type` | typedef | `boost::shared_ptr<GLVertexElementBufferImpl>` | public | A convenience typedef for a shared pointer to a GLVertexElementBufferImpl. |
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const GLVertexElementBufferImpl>` | public | — |
| `create( GLRenderer &renderer, const GLBufferImpl::shared_ptr_type &buffer)` | method | `shared_ptr_type` | public | Creates a GLVertexElementBufferImpl object attached to the specified buffer. |
| `create_as_unique_ptr( GLRenderer &renderer, const GLBufferImpl::shared_ptr_type &buffer)` | method | `std::unique_ptr<GLVertexElementBufferImpl>` | public | Same as create but returns a std::unique\_ptr - to guarantee only one owner. |
| `get_buffer()` | method | `GLBuffer::shared_ptr_to_const_type` | public | Returns the buffer used to store vertex element data (indices). |
| `gl_bind( GLRenderer &renderer)` | method | `void` | public | Binds this vertex element buffer so that vertex element data is sourced from it. |
| `gl_draw_range_elements( GLRenderer &renderer, GLenum mode, GLuint start, GLuint end, GLsizei count, GLenum type, GLint indices_offset)` | method | `void` | public | Performs the equivalent of the OpenGL command 'glDrawRangeElements'. indices\_offset is a byte offset from the start of 'this' indices array. |
| `d_buffer` | field | `GLBufferImpl::shared_ptr_type` | private | The buffer being targeted by this vertex element buffer. |
| `GLVertexElementBufferImpl( GLRenderer &renderer, const GLBufferImpl::shared_ptr_type &buffer)` | constructor | `None` | private | Constructor. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLVERTEXELEMENTBUFFERIMPL_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLVertexElementBuffer](GLVertexElementBuffer.md) | opengl | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLVertexElementBufferImpl.h
python scripts/gpq.py def GPlatesOpenGL::GLVertexElementBufferImpl --body
python scripts/gpq.py uses GLVertexElementBufferImpl --kind class
python scripts/gpq.py hier GLVertexElementBufferImpl
```
