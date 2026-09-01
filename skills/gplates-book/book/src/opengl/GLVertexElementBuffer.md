# GLVertexElementBuffer

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 1497 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLVertexElementBuffer.h` | C++ | 178 |
| `src/opengl/GLVertexElementBuffer.cc` | C++ | 60 |

## Overview

`GLVertexElementBuffer` is a pure abstract interface for a `GLBuffer`
interpreted as index (vertex element) data, the counterpart to
`GLVertexBuffer` for attribute data. As with `GLVertexBuffer`, the same
underlying `GLBuffer` can be attached to both a `GLVertexBuffer` and a
`GLVertexElementBuffer` so vertices and indices share one allocation.
Concrete work — binding and `glDrawRangeElements` — is left to subclasses
(`GLVertexElementBufferImpl` and `GLVertexElementBufferObject`); this class
only fixes the shared interface and the `create` factory.

The `GLVertexElementTraits<VertexElementType>` specialisations (for
`GLubyte`, `GLushort`, `GLuint`) map an index storage type to its OpenGL enum
(`GL_UNSIGNED_BYTE`/`_SHORT`/`_INT`) and to `MAX_INDEXABLE_VERTEX`, the
largest vertex count that type can index — callers use this to choose the
smallest index type that still fits a given mesh.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLVertexElementTraits<GLubyte>`](#gplatesopenglglvertexelementtraitsglubyte) | struct | — | `<>` | 0 | — |
| [`GPlatesOpenGL::GLVertexElementTraits<GLushort>`](#gplatesopenglglvertexelementtraitsglushort) | struct | — | `<>` | 0 | — |
| [`GPlatesOpenGL::GLVertexElementTraits<GLuint>`](#gplatesopenglglvertexelementtraitsgluint) | struct | — | `<>` | 0 | — |
| [`GPlatesOpenGL::GLVertexElementBuffer`](#gplatesopenglglvertexelementbuffer) | class | `boost::enable_shared_from_this<GLVertexElementBuffer>` | — | 2 | An abstraction of the OpenGL buffer objects extension as used for vertex element buffers containing vertex element (index) data and \*not\* vertex attribute (vertices) data. |

## Members

### `GPlatesOpenGL::GLVertexElementTraits<GLubyte>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `type` | field | `GLenum` | public | GL\_UNSIGNED\_BYTE |
| `MAX_INDEXABLE_VERTEX` | field | `unsigned int` | public | The maximum number of vertices that can be indexed. |
| `const_max` | field | `unsigned int` | public | The maximum number of vertices that can be indexed. |

### `GPlatesOpenGL::GLVertexElementTraits<GLushort>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `type` | field | `GLenum` | public | GL\_UNSIGNED\_SHORT |
| `MAX_INDEXABLE_VERTEX` | field | `unsigned int` | public | The maximum number of vertices that can be indexed. |
| `const_max` | field | `unsigned int` | public | The maximum number of vertices that can be indexed. |

### `GPlatesOpenGL::GLVertexElementTraits<GLuint>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `type` | field | `GLenum` | public | GL\_UNSIGNED\_INT |
| `MAX_INDEXABLE_VERTEX` | field | `unsigned int` | public | The maximum number of vertices that can be indexed. |
| `const_max` | field | `unsigned int` | public | The maximum number of vertices that can be indexed. |

### `GPlatesOpenGL::GLVertexElementBuffer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_type` | typedef | `boost::shared_ptr<GLVertexElementBuffer>` | public | A convenience typedef for a shared pointer to a non-const GLVertexElementBuffer. |
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const GLVertexElementBuffer>` | public | — |
| `weak_ptr_type` | typedef | `boost::weak_ptr<GLVertexElementBuffer>` | public | A convenience typedef for a weak pointer to a GLVertexElementBuffer. |
| `weak_ptr_to_const_type` | typedef | `boost::weak_ptr<const GLVertexElementBuffer>` | public | — |
| `create( GLRenderer &renderer, const GLBuffer::shared_ptr_type &buffer)` | method | `shared_ptr_type` | public | Creates a GLVertexElementBuffer object attached to the specified buffer. |
| `create_as_unique_ptr( GLRenderer &renderer, const GLBuffer::shared_ptr_type &buffer)` | method | `std::unique_ptr<GLVertexElementBuffer>` | public | Same as create but returns a std::unique\_ptr - to guarantee only one owner. |
| `~GLVertexElementBuffer()` | destructor | `None` | public | — |
| `get_buffer()` | method | `GLBuffer::shared_ptr_type` | public | Returns the 'non-const' buffer used to store vertex element data (indices). |
| `gl_bind( GLRenderer &renderer)` | method | `void` | public | Binds this vertex element buffer so that vertex element data is sourced from it. |
| `gl_draw_range_elements( GLRenderer &renderer, GLenum mode, GLuint start, GLuint end, GLsizei count, GLenum type, GLint indices_offset)` | method | `void` | public | Performs the equivalent of the OpenGL command 'glDrawRangeElements'. indices\_offset is a byte offset from the start of 'this' indices array. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `type` | variable | `GLenum` | — |
| `GPLATES_OPENGL_GLVERTEXELEMENTBUFFER_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLScalarField3D](GLScalarField3D.md) | opengl | 15 |
| [opengl/GLMultiResolutionRaster](GLMultiResolutionRaster.md) | opengl | 9 |
| [gui/Stars](../gui/Stars.md) | gui | 7 |
| [opengl/GLFilledPolygonsGlobeView](GLFilledPolygonsGlobeView.md) | opengl | 7 |
| [opengl/GLFilledPolygonsMapView](GLFilledPolygonsMapView.md) | opengl | 7 |
| [gui/LayerPainter](../gui/LayerPainter.md) | gui | 5 |
| [opengl/GLVertexArray](GLVertexArray.md) | opengl | 5 |
| [gui/SphericalGrid](../gui/SphericalGrid.md) | gui | 4 |
| [opengl/GLRasterCoRegistration](GLRasterCoRegistration.md) | opengl | 4 |
| [opengl/GLVertexArrayImpl](GLVertexArrayImpl.md) | opengl | 3 |
| [opengl/GLVertexArrayObject](GLVertexArrayObject.md) | opengl | 3 |
| [gui/MapBackground](../gui/MapBackground.md) | gui | 2 |
| [gui/MapGrid](../gui/MapGrid.md) | gui | 2 |
| [gui/OpaqueSphere](../gui/OpaqueSphere.md) | gui | 2 |
| [opengl/GLStateSets](GLStateSets.md) | opengl | 2 |
| [opengl/GLStreamPrimitives](GLStreamPrimitives.md) | opengl | 2 |
| [opengl/GLVertexElementBufferImpl](GLVertexElementBufferImpl.md) | opengl | 2 |
| [opengl/GLVertexElementBufferObject](GLVertexElementBufferObject.md) | opengl | 2 |
| [opengl/GLMultiResolutionCubeMesh](GLMultiResolutionCubeMesh.md) | opengl | 1 |
| [opengl/GLMultiResolutionMapCubeMesh](GLMultiResolutionMapCubeMesh.md) | opengl | 1 |

*... and 2 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLVertexElementBuffer.h
python scripts/gpq.py def GPlatesOpenGL::GLVertexElementBuffer --body
python scripts/gpq.py uses GLVertexElementBuffer --kind class
python scripts/gpq.py hier GLVertexElementBuffer
```
