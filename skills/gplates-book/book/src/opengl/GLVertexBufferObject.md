# GLVertexBufferObject

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 531 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLVertexBufferObject.h` | C++ | 223 |
| `src/opengl/GLVertexBufferObject.cc` | C++ | 155 |

## Overview

`GLVertexBufferObject` is the `GLVertexBuffer` concrete implementation backed
by a real `GL_ARRAY_BUFFER_ARB` object, requiring the
`GL_ARB_vertex_buffer_object` extension. It wraps a `GLBufferObject` (held in
`d_buffer`), exposed both as the `GLBuffer::shared_ptr_to_const_type` seen
through the base `GLVertexBuffer::get_buffer` interface and as the concrete
`GLBufferObject` through `get_buffer_object` for callers that need the actual
resource. `get_target_type` reports the fixed `GL_ARRAY_BUFFER_ARB` binding
target that distinguishes it from a `GLVertexElementBuffer`'s
`GL_ELEMENT_ARRAY_BUFFER_ARB`.

Its `gl_*_pointer` methods implement the same interface as
`GLVertexBuffer`'s, forwarding to `renderer` to bind this buffer object and
issue the corresponding vertex/attribute pointer call, so higher-level code
that only knows about `GLVertexBuffer` works unchanged whether the underlying
storage is this hardware-backed buffer or a client-side fallback.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLVertexBufferObject`](#gplatesopenglglvertexbufferobject) | class | [`GLVertexBuffer`](GLVertexBuffer.md)<br>[`GLObject`](GLObject.md) | — | 0 | An OpenGL buffer object used to stored vertices (vertex attributes) but \*not\* vertex elements (indices). |

## Members

### `GPlatesOpenGL::GLVertexBufferObject`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_type` | typedef | `boost::shared_ptr<GLVertexBufferObject>` | public | A convenience typedef for a shared pointer to a GLVertexBufferObject. |
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const GLVertexBufferObject>` | public | — |
| `weak_ptr_type` | typedef | `boost::weak_ptr<GLVertexBufferObject>` | public | A convenience typedef for a weak pointer to a GLVertexBufferObject. |
| `weak_ptr_to_const_type` | typedef | `boost::weak_ptr<const GLVertexBufferObject>` | public | — |
| `get_target_type()` | method | `GLenum` | public | Returns the target GL\_ARRAY\_BUFFER\_ARB. |
| `create( GLRenderer &renderer, const GLBufferObject::shared_ptr_type &buffer)` | method | `shared_ptr_type` | public | Creates a shared pointer to a GLVertexBufferObject object. |
| `create_as_unique_ptr( GLRenderer &renderer, const GLBufferObject::shared_ptr_type &buffer)` | method | `std::unique_ptr<GLVertexBufferObject>` | public | Same as create but returns a std::unique\_ptr - to guarantee only one owner. |
| `get_buffer()` | method | `GLBuffer::shared_ptr_to_const_type` | public | Returns the buffer used to store vertex attribute data (vertices). |
| `gl_vertex_pointer( GLRenderer &renderer, GLint size, GLenum type, GLsizei stride, GLint offset)` | method | `void` | public | Binds the vertex position data ('glVertexPointer') to 'this' vertex buffer. |
| `gl_color_pointer( GLRenderer &renderer, GLint size, GLenum type, GLsizei stride, GLint offset)` | method | `void` | public | Binds the vertex color data ('glColorPointer') to 'this' vertex buffer. |
| `gl_normal_pointer( GLRenderer &renderer, GLenum type, GLsizei stride, GLint offset)` | method | `void` | public | Binds the vertex normal data ('glNormalPointer') to 'this' vertex buffer. |
| `gl_tex_coord_pointer( GLRenderer &renderer, GLenum texture_unit, GLint size, GLenum type, GLsizei stride, GLint offset)` | method | `void` | public | Binds the vertex texture coordinate data ('glTexCoordPointer') to 'this' vertex buffer. |
| `gl_vertex_attrib_pointer( GLRenderer &renderer, GLuint attribute_index, GLint size, GLenum type, GLboolean normalized, GLsizei stride, GLint offset)` | method | `void` | public | Binds the specified \*generic\* vertex attribute data at attribute index attribute\_index to 'this' vertex buffer. |
| `gl_vertex_attrib_i_pointer( GLRenderer &renderer, GLuint attribute_index, GLint size, GLenum type, GLsizei stride, GLint offset)` | method | `void` | public | Same as gl\_vertex\_attrib\_pointer except used to specify attributes mapping to \*integer\* shader variables. |
| `gl_vertex_attrib_l_pointer( GLRenderer &renderer, GLuint attribute_index, GLint size, GLenum type, GLsizei stride, GLint offset)` | method | `void` | public | Same as gl\_vertex\_attrib\_pointer except used to specify attributes mapping to \*double\* shader variables. |
| `get_buffer_object()` | method | `GLBufferObject::shared_ptr_to_const_type` | public | Returns the buffer object. |
| `d_buffer` | field | `GLBufferObject::shared_ptr_type` | private | — |
| `GLVertexBufferObject( GLRenderer &renderer, const GLBufferObject::shared_ptr_type &buffer)` | constructor | `None` | private | Constructor. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLVERTEXBUFFEROBJECT_H` | macro | `None` | — |

## Notes

Requires `GL_ARB_vertex_buffer_object`; use `GLVertexBufferImpl` when the
extension is unavailable.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLRenderer](GLRenderer.md) | opengl | 7 |
| [opengl/GLStateSets](GLStateSets.md) | opengl | 7 |
| [opengl/GLVertexBuffer](GLVertexBuffer.md) | opengl | 2 |
| [opengl/GLState](GLState.md) | opengl | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLVertexBufferObject.h
python scripts/gpq.py def GPlatesOpenGL::GLVertexBufferObject --body
python scripts/gpq.py uses GLVertexBufferObject --kind class
python scripts/gpq.py hier GLVertexBufferObject
```
