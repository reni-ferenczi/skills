# GLVertexBufferImpl

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 448 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLVertexBufferImpl.h` | C++ | 200 |
| `src/opengl/GLVertexBufferImpl.cc` | C++ | 183 |

## Overview

`GLVertexBufferImpl` provides fallback vertex buffer support for OpenGL implementations that lack the vertex buffer object extension. It wraps a `GLBufferImpl` and delegates vertex pointer calls (position, color, normal, texture coordinates, generic attributes) to the `GLRenderer`, which then implements them using client-side memory arrays via base OpenGL 1.1 functionality.

This is a compatibility layer: modern systems have hardware vertex buffer objects, but this implementation allows the rendering code to maintain a uniform interface across all platforms.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLVertexBufferImpl`](#gplatesopenglglvertexbufferimpl) | class | [`GLVertexBuffer`](GLVertexBuffer.md) | — | 0 | An implementation of the OpenGL buffer objects extension as used for vertex buffers containing vertex (attribute) data and \*not\* vertex element (indices) data. |

## Members

### `GPlatesOpenGL::GLVertexBufferImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_type` | typedef | `boost::shared_ptr<GLVertexBufferImpl>` | public | A convenience typedef for a shared pointer to a GLVertexBufferImpl. |
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const GLVertexBufferImpl>` | public | — |
| `create( GLRenderer &renderer, const GLBufferImpl::shared_ptr_type &buffer)` | method | `shared_ptr_type` | public | Creates a GLVertexBufferImpl object attached to the specified buffer. |
| `create_as_unique_ptr( GLRenderer &renderer, const GLBufferImpl::shared_ptr_type &buffer)` | method | `std::unique_ptr<GLVertexBufferImpl>` | public | Same as create but returns a std::unique\_ptr - to guarantee only one owner. |
| `get_buffer()` | method | `GLBuffer::shared_ptr_to_const_type` | public | Returns the buffer used to store vertex attribute data (vertices). |
| `gl_vertex_pointer( GLRenderer &renderer, GLint size, GLenum type, GLsizei stride, GLint offset)` | method | `void` | public | Binds the vertex position data ('glVertexPointer') to 'this' vertex buffer. |
| `gl_color_pointer( GLRenderer &renderer, GLint size, GLenum type, GLsizei stride, GLint offset)` | method | `void` | public | Binds the vertex color data ('glColorPointer') to 'this' vertex buffer. |
| `gl_normal_pointer( GLRenderer &renderer, GLenum type, GLsizei stride, GLint offset)` | method | `void` | public | Binds the vertex normal data ('glNormalPointer') to 'this' vertex buffer. |
| `gl_tex_coord_pointer( GLRenderer &renderer, GLenum texture_unit, GLint size, GLenum type, GLsizei stride, GLint offset)` | method | `void` | public | Binds the vertex texture coordinate data ('glTexCoordPointer') to 'this' vertex buffer. |
| `gl_vertex_attrib_pointer( GLRenderer &renderer, GLuint attribute_index, GLint size, GLenum type, GLboolean normalized, GLsizei stride, GLint offset)` | method | `void` | public | Binds the specified \*generic\* vertex attribute data at attribute index attribute\_index to 'this' vertex buffer. |
| `gl_vertex_attrib_i_pointer( GLRenderer &renderer, GLuint attribute_index, GLint size, GLenum type, GLsizei stride, GLint offset)` | method | `void` | public | Same as gl\_vertex\_attrib\_pointer except used to specify attributes mapping to \*integer\* shader variables. |
| `gl_vertex_attrib_l_pointer( GLRenderer &renderer, GLuint attribute_index, GLint size, GLenum type, GLsizei stride, GLint offset)` | method | `void` | public | Same as gl\_vertex\_attrib\_pointer except used to specify attributes mapping to \*double\* shader variables. |
| `d_buffer` | field | `GLBufferImpl::shared_ptr_type` | private | The buffer being targeted by this vertex buffer. |
| `GLVertexBufferImpl( GLRenderer &renderer, const GLBufferImpl::shared_ptr_type &buffer)` | constructor | `None` | private | Constructor. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLVERTEXBUFFERIMPL_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLVertexBuffer](GLVertexBuffer.md) | opengl | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLVertexBufferImpl.h
python scripts/gpq.py def GPlatesOpenGL::GLVertexBufferImpl --body
python scripts/gpq.py uses GLVertexBufferImpl --kind class
python scripts/gpq.py hier GLVertexBufferImpl
```
