# GLVertexArray

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 312 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLVertexArray.h` | C++ | 510 |
| `src/opengl/GLVertexArray.cc` | C++ | 91 |

## Overview

[[[PROSE overview unit=opengl/GLVertexArray tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLVertexArray`](#gplatesopenglglvertexarray) | class | `boost::enable_shared_from_this<GLVertexArray>` | — | 2 | An abstraction based on OpenGL vertex array objects (GL\_ARB\_vertex\_array\_object extension) that behaves like vertex array objects even if the extension is not supported. |

## Members

### `GPlatesOpenGL::GLVertexArray`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_type` | typedef | `boost::shared_ptr<GLVertexArray>` | public | A convenience typedef for a shared pointer to a non-const GLVertexArray. |
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const GLVertexArray>` | public | — |
| `weak_ptr_type` | typedef | `boost::weak_ptr<GLVertexArray>` | public | A convenience typedef for a weak pointer to a GLVertexArray. |
| `weak_ptr_to_const_type` | typedef | `boost::weak_ptr<const GLVertexArray>` | public | — |
| `create( GLRenderer &renderer)` | method | `shared_ptr_type` | public | Creates a GLVertexArray object with no array data. |
| `create_as_unique_ptr( GLRenderer &renderer)` | method | `std::unique_ptr<GLVertexArray>` | public | Same as create but returns a std::unique\_ptr - to guarantee only one owner. |
| `~GLVertexArray()` | destructor | `None` | public | — |
| `gl_bind( GLRenderer &renderer)` | method | `void` | public | Binds this vertex array so that all vertex data is sourced from the vertex buffers, specified in this interface, and vertex element data is sourced from the vertex element buffer. |
| `gl_draw_range_elements( GLRenderer &renderer, GLenum mode, GLuint start, GLuint end, GLsizei count, GLenum type, GLint indices_offset)` | method | `void` | public | Performs the equivalent of the OpenGL command 'glDrawRangeElements'. |
| `clear( GLRenderer &renderer)` | method | `void` | public | Clears this vertex array. |
| `set_vertex_element_buffer( GLRenderer &renderer, const GLVertexElementBuffer::shared_ptr_to_const_type &vertex_element_buffer)` | method | `void` | public | Specify the source of vertex element (vertex indices) data. |
| `set_enable_client_state( GLRenderer &renderer, GLenum array, bool enable)` | method | `void` | public | Enables the specified (array) vertex array (in the fixed-function pipeline). |
| `set_enable_client_texture_state( GLRenderer &renderer, GLenum texture_unit, bool enable)` | method | `void` | public | Enables the vertex attribute array GL\_TEXTURE\_COORD\_ARRAY (in the fixed-function pipeline) on the specified texture unit. |
| `set_vertex_pointer( GLRenderer &renderer, const GLVertexBuffer::shared_ptr_to_const_type &vertex_buffer, GLint size, GLenum type, GLsizei stride, GLint offset)` | method | `void` | public | Specify the source of vertex position data. |
| `set_color_pointer( GLRenderer &renderer, const GLVertexBuffer::shared_ptr_to_const_type &vertex_buffer, GLint size, GLenum type, GLsizei stride, GLint offset)` | method | `void` | public | Specify the source of vertex colour data. |
| `set_normal_pointer( GLRenderer &renderer, const GLVertexBuffer::shared_ptr_to_const_type &vertex_buffer, GLenum type, GLsizei stride, GLint offset)` | method | `void` | public | Specify the source of vertex normal data. |
| `set_tex_coord_pointer( GLRenderer &renderer, const GLVertexBuffer::shared_ptr_to_const_type &vertex_buffer, GLenum texture_unit, GLint size, GLenum type, GLsizei stride, GLint offset)` | method | `void` | public | Specify the source of vertex texture coordinate data. |
| `set_enable_vertex_attrib_array( GLRenderer &renderer, GLuint attribute_index, bool enable)` | method | `void` | public | Enables the specified \*generic\* vertex attribute data at attribute index attribute\_index. |
| `set_vertex_attrib_pointer( GLRenderer &renderer, const GLVertexBuffer::shared_ptr_to_const_type &vertex_buffer, GLuint attribute_index, GLint size, GLenum type, GLboolean normalized, GLsizei stride, GLint offset)` | method | `void` | public | Specify the source of \*generic\* vertex attribute data at attribute index attribute\_index. |
| `set_vertex_attrib_i_pointer( GLRenderer &renderer, const GLVertexBuffer::shared_ptr_to_const_type &vertex_buffer, GLuint attribute_index, GLint size, GLenum type, GLsizei stride, GLint offset)` | method | `void` | public | Same as set\_vertex\_attrib\_pointer except used to specify attributes mapping to \*integer\* shader variables. |
| `set_vertex_attrib_l_pointer( GLRenderer &renderer, const GLVertexBuffer::shared_ptr_to_const_type &vertex_buffer, GLuint attribute_index, GLint size, GLenum type, GLsizei stride, GLint offset)` | method | `void` | public | Same as set\_vertex\_attrib\_pointer except used to specify attributes mapping to \*double\* shader variables. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLVERTEXARRAY_H` | macro | `None` | — |
| `compile_vertex_array_draw_state( GLRenderer &renderer, GLVertexArray &vertex_array, GLenum mode, GLuint start, GLuint end, GLsizei count, GLenum type, GLint indices_offset = 0)` | function | `GLCompiledDrawState::non_null_ptr_type` | Compiles a draw state that, whenever applied to a renderer, will bind and draw the vertex array. |
| `set_vertex_array_data( GLRenderer &renderer, GLVertexArray &vertex_array, const std::vector<VertexType> &vertices, const std::vector<VertexElementType> &vertex_elements)` | function | `void` | — |
| `compile_vertex_array_draw_state( GLRenderer &renderer, GLVertexArray &vertex_array, const std::vector<VertexType> &vertices, const std::vector<VertexElementType> &vertex_elements, GLenum mode)` | function | `GLCompiledDrawState::non_null_ptr_type` | — |

## Notes

[[[PROSE notes unit=opengl/GLVertexArray tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLRasterCoRegistration](GLRasterCoRegistration.md) | opengl | 15 |
| [opengl/GLScalarField3D](GLScalarField3D.md) | opengl | 9 |
| [gui/LayerPainter](../gui/LayerPainter.md) | gui | 6 |
| [gui/SphericalGrid](../gui/SphericalGrid.md) | gui | 6 |
| [gui/Stars](../gui/Stars.md) | gui | 5 |
| [opengl/GLReconstructedStaticPolygonMeshes](GLReconstructedStaticPolygonMeshes.md) | opengl | 5 |
| [gui/MapBackground](../gui/MapBackground.md) | gui | 4 |
| [gui/MapGrid](../gui/MapGrid.md) | gui | 4 |
| [gui/OpaqueSphere](../gui/OpaqueSphere.md) | gui | 4 |
| [opengl/GLMultiResolutionRaster](GLMultiResolutionRaster.md) | opengl | 4 |
| [opengl/GLFilledPolygonsGlobeView](GLFilledPolygonsGlobeView.md) | opengl | 3 |
| [opengl/GLFilledPolygonsMapView](GLFilledPolygonsMapView.md) | opengl | 3 |
| [opengl/GLMultiResolutionCubeMesh](GLMultiResolutionCubeMesh.md) | opengl | 3 |
| [opengl/GLMultiResolutionMapCubeMesh](GLMultiResolutionMapCubeMesh.md) | opengl | 3 |
| [opengl/GLStreamPrimitives](GLStreamPrimitives.md) | opengl | 3 |
| [opengl/GLUtils](GLUtils.md) | opengl | 3 |
| [opengl/GLContext](GLContext.md) | opengl | 1 |
| [opengl/GLVertex](GLVertex.md) | opengl | 1 |
| [opengl/GLVertexArrayImpl](GLVertexArrayImpl.md) | opengl | 1 |
| [opengl/GLVertexArrayObject](GLVertexArrayObject.md) | opengl | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLVertexArray.h
python scripts/gpq.py def GPlatesOpenGL::GLVertexArray --body
python scripts/gpq.py uses GLVertexArray --kind class
python scripts/gpq.py hier GLVertexArray
```
