# GLVertexBuffer

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 448 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLVertexBuffer.h` | C++ | 226 |
| `src/opengl/GLVertexBuffer.cc` | C++ | 55 |

## Overview

`GLVertexBuffer` is a thin, extension-agnostic wrapper around a `GLBuffer`
that interprets its contents as vertex attribute data — as opposed to
`GLVertexElementBuffer`, which interprets a `GLBuffer` as index data. It does
not own storage itself; `create` attaches it to an existing `GLBuffer`, and
the same underlying buffer can be attached to both a `GLVertexBuffer` and a
`GLVertexElementBuffer` at once so vertices and indices can share one
allocation.

Its `gl_*_pointer` methods (`gl_vertex_pointer`, `gl_color_pointer`,
`gl_normal_pointer`, `gl_tex_coord_pointer`, and the generic
`gl_vertex_attrib_pointer`/`_i_pointer`/`_l_pointer` family) mirror the
fixed-function and shader-attribute pointer calls that `GLVertexArrayImpl`
and `GLVertexArrayObject` record when a `GLVertexArray` client calls their
equivalent `set_*` methods, letting those two vertex-array implementations
share one buffer abstraction regardless of whether a real vertex array object
is backing them.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLVertexBuffer`](#gplatesopenglglvertexbuffer) | class | `boost::enable_shared_from_this<GLVertexBuffer>` | — | 2 | An abstraction of the OpenGL buffer objects extension as used for vertex buffers containing vertex (attribute) data and \*not\* vertex element (indices) data. |

## Members

### `GPlatesOpenGL::GLVertexBuffer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_type` | typedef | `boost::shared_ptr<GLVertexBuffer>` | public | A convenience typedef for a shared pointer to a non-const GLVertexBuffer. |
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const GLVertexBuffer>` | public | — |
| `weak_ptr_type` | typedef | `boost::weak_ptr<GLVertexBuffer>` | public | A convenience typedef for a weak pointer to a GLVertexBuffer. |
| `weak_ptr_to_const_type` | typedef | `boost::weak_ptr<const GLVertexBuffer>` | public | — |
| `create( GLRenderer &renderer, const GLBuffer::shared_ptr_type &buffer)` | method | `shared_ptr_type` | public | Creates a GLVertexBuffer object attached to the specified buffer. |
| `create_as_unique_ptr( GLRenderer &renderer, const GLBuffer::shared_ptr_type &buffer)` | method | `std::unique_ptr<GLVertexBuffer>` | public | Same as create but returns a std::unique\_ptr - to guarantee only one owner. |
| `~GLVertexBuffer()` | destructor | `None` | public | — |
| `get_buffer()` | method | `GLBuffer::shared_ptr_type` | public | Returns the 'non-const' buffer used to store vertex attribute data (vertices). |
| `gl_vertex_pointer( GLRenderer &renderer, GLint size, GLenum type, GLsizei stride, GLint offset)` | method | `void` | public | Binds the vertex position data ('glVertexPointer') to 'this' vertex buffer. |
| `gl_color_pointer( GLRenderer &renderer, GLint size, GLenum type, GLsizei stride, GLint offset)` | method | `void` | public | Binds the vertex color data ('glColorPointer') to 'this' vertex buffer. |
| `gl_normal_pointer( GLRenderer &renderer, GLenum type, GLsizei stride, GLint offset)` | method | `void` | public | Binds the vertex normal data ('glNormalPointer') to 'this' vertex buffer. |
| `gl_tex_coord_pointer( GLRenderer &renderer, GLenum texture_unit, GLint size, GLenum type, GLsizei stride, GLint offset)` | method | `void` | public | Binds the vertex texture coordinate data ('glTexCoordPointer') to 'this' vertex buffer. |
| `gl_vertex_attrib_pointer( GLRenderer &renderer, GLuint attribute_index, GLint size, GLenum type, GLboolean normalized, GLsizei stride, GLint offset)` | method | `void` | public | Binds the specified \*generic\* vertex attribute data at attribute index attribute\_index to 'this' vertex buffer. |
| `gl_vertex_attrib_i_pointer( GLRenderer &renderer, GLuint attribute_index, GLint size, GLenum type, GLsizei stride, GLint offset)` | method | `void` | public | Same as gl\_vertex\_attrib\_pointer except used to specify attributes mapping to \*integer\* shader variables. |
| `gl_vertex_attrib_l_pointer( GLRenderer &renderer, GLuint attribute_index, GLint size, GLenum type, GLsizei stride, GLint offset)` | method | `void` | public | Same as gl\_vertex\_attrib\_pointer except used to specify attributes mapping to \*double\* shader variables. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLVERTEXBUFFER_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLScalarField3D](GLScalarField3D.md) | opengl | 15 |
| [opengl/GLVertexArrayObject](GLVertexArrayObject.md) | opengl | 15 |
| [opengl/GLVertex](GLVertex.md) | opengl | 14 |
| [opengl/GLVertexArrayImpl](GLVertexArrayImpl.md) | opengl | 14 |
| [opengl/GLVertexArray](GLVertexArray.md) | opengl | 9 |
| [gui/LayerPainter](../gui/LayerPainter.md) | gui | 3 |
| [opengl/GLFilledPolygonsGlobeView](GLFilledPolygonsGlobeView.md) | opengl | 3 |
| [opengl/GLFilledPolygonsMapView](GLFilledPolygonsMapView.md) | opengl | 3 |
| [opengl/GLMultiResolutionRaster](GLMultiResolutionRaster.md) | opengl | 3 |
| [opengl/GLRasterCoRegistration](GLRasterCoRegistration.md) | opengl | 3 |
| [opengl/GLVertexBufferImpl](GLVertexBufferImpl.md) | opengl | 2 |
| [opengl/GLVertexBufferObject](GLVertexBufferObject.md) | opengl | 2 |
| [gui/Stars](../gui/Stars.md) | gui | 1 |
| [opengl/GLReconstructedStaticPolygonMeshes](GLReconstructedStaticPolygonMeshes.md) | opengl | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLVertexBuffer.h
python scripts/gpq.py def GPlatesOpenGL::GLVertexBuffer --body
python scripts/gpq.py uses GLVertexBuffer --kind class
python scripts/gpq.py hier GLVertexBuffer
```
