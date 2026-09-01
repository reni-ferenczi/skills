# GLStreamPrimitives

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 13 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLStreamPrimitives.h` | C++ | 2308 |

## Overview

[[[PROSE overview unit=opengl/GLStreamPrimitives tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLStreamPrimitives`](#gplatesopenglglstreamprimitives) | class | `boost::noncopyable` | `<class VertexType, typename VertexElementType, template <class> class StreamWriterType>` | 2 | So the 'mode' parameter of glDrawRangeElements, for example, is always one of: - GL\_POINTS, - GL\_LINES, or - GL\_TRIANGLES. |
| [`GPlatesOpenGL::GLStaticStreamPrimitives`](#gplatesopenglglstaticstreamprimitives) | class | [`GLStreamPrimitives<VertexType, VertexElementType, GLStaticBufferStreamWriter>`](GLStreamPrimitives.md) | `<class VertexType, typename VertexElementType>` | 0 | A type of GLStreamPrimitives that writes to static (fixed size) vertex/index buffers. |
| [`GPlatesOpenGL::GLDynamicStreamPrimitives`](#gplatesopenglgldynamicstreamprimitives) | class | [`GLStreamPrimitives<VertexType, VertexElementType, GLDynamicBufferStreamWriter>`](GLStreamPrimitives.md) | `<class VertexType, typename VertexElementType>` | 0 | A type of GLStreamPrimitives that writes to dynamic (std::vector) vertex/index buffers. |

## Members

### `GPlatesOpenGL::GLStreamPrimitives`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `stream_primitives_type` | typedef | `GLStreamPrimitives<VertexType, VertexElementType, StreamWriterType>` | public | Typedef for this class. |
| `vertex_element_type` | typedef | `VertexElementType` | public | Typedef for a vertex index. |
| `vertex_type` | typedef | `VertexType` | public | Typedef for the vertex type. |
| `GLStreamPrimitives()` | constructor | `None` | public | Constructor. |
| `Points` | class | `None` | public | Attach to GLStreamPrimitives to stream point primitives. |
| `Lines` | class | `None` | public | Attach to GLStreamPrimitives to stream line primitives. |
| `LineStrips` | class | `None` | public | Attach to GLStreamPrimitives to stream line strip primitives. |
| `LineLoops` | class | `None` | public | Attach to GLStreamPrimitives to stream line loop primitives. |
| `Triangles` | class | `None` | public | Attach to GLStreamPrimitives to stream triangle primitives. |
| `TriangleStrips` | class | `None` | public | Attach to GLStreamPrimitives to stream triangle strip primitives. |
| `TriangleFans` | class | `None` | public | Attach to GLStreamPrimitives to stream triangle fan primitives. |
| `TriangleMeshes` | class | `None` | public | Attach to GLStreamPrimitives to stream individual vertex-indexed triangle meshes. |
| `Quads` | class | `None` | public | Attach to GLStreamPrimitives to stream quad primitives. |
| `Primitives` | class | `None` | public | Attach to GLStreamPrimitives to stream arbitrary primitives where the stream overflow check is done at the beginning of the primitive instead of checking at each vertex. |
| `StreamTarget` | class | `None` | public | RAII class to start and stop streaming over a scope and also to temporarily interrupt streaming when the vertex buffer or vertex element buffer is full (or when client decides to render the stream contents). |
| `vertex_stream_writer_type` | typedef | `StreamWriterType<vertex_type>` | private | Typedef for a vertex stream writer. |
| `vertex_element_stream_writer_type` | typedef | `StreamWriterType<vertex_element_type>` | private | Typedef for a vertex element stream writer. |
| `d_vertex_stream` | field | `boost::optional<vertex_stream_writer_type>` | private | Where the output vertices are written (a write-only wrapper around vertex buffer memory). |
| `d_begin_vertex_stream_count` | field | `unsigned int` | private | The vertex stream count at the most recent call to begin\_streaming. |
| `d_vertex_element_stream` | field | `boost::optional<vertex_element_stream_writer_type>` | private | Where the output vertex elements are written (a write-only wrapper around vertex element buffer memory). |
| `d_begin_vertex_element_stream_count` | field | `unsigned int` | private | The vertex element stream count at the most recent call to begin\_streaming. |
| `begin_streaming( const VertexStreamWriterConstructorArgs &vertex_stream_writer_constructor_args, const VertexElementStreamWriterConstructorArgs &vertex_element_stream_writer_constructor_args, unsigned int &begin_streaming_vertex_count, unsigned int &begin_streaming_vertex_element_count)` | method | `void` | private | Starts a target for streaming primitives (a vertex buffer and vertex element buffer). |
| `get_base_vertex_element()` | method | `unsigned int` | private | Returns the number of vertices currently in the vertex stream writer. |
| `get_num_streamed_vertices()` | method | `unsigned int` | private | Returns the number of vertices streamed since the last call to begin\_streaming. |
| `get_num_streamed_vertex_elements()` | method | `unsigned int` | private | Returns the number of vertex elements streamed since the last call to begin\_streaming. |
| `end_streaming( unsigned int &num_streamed_vertices, unsigned int &num_streamed_vertex_elements)` | method | `void` | private | Stops a target for streaming primitives and returned the number of vertices/indices streamed since the last call to begin\_streaming. |
| `add_point( const vertex_type &vertex)` | method | `bool` | private | Adds a point primitive. |
| `add_line( const vertex_type &start_vertex, const vertex_type &end_vertex)` | method | `bool` | private | Adds a line primitive with the specified start and end vertices. |
| `add_line( const vertex_type &end_vertex)` | method | `bool` | private | Adds a line primitive whose start vertex is the end of the last line added. |
| `add_triangle( const vertex_type &first_vertex, const vertex_type &second_vertex, const vertex_type &third_vertex)` | method | `bool` | private | Adds a triangle primitive with the specified vertices. |
| `add_triangle_reversed( const vertex_type &first_vertex, const vertex_type &second_vertex, const vertex_type &third_vertex)` | method | `bool` | private | Adds a triangle primitive with the specified vertices. |
| `add_triangle( const vertex_type &third_vertex)` | method | `bool` | private | Adds a triangle primitive whose third vertex is third\_vertex. |
| `add_triangle_reversed( const vertex_type &third_vertex)` | method | `bool` | private | Adds a triangle primitive whose third vertex is third\_vertex. |
| `add_triangle( const vertex_type &first_vertex, const vertex_type &third_vertex)` | method | `bool` | private | Adds a triangle primitive whose first and third vertices are first\_vertex and third\_vertex. |
| `add_vertex( const vertex_type &vertex)` | method | `bool` | private | Adds a vertex only (no vertex elements are added). |
| `add_triangle( vertex_element_type first_vertex_element, vertex_element_type second_vertex_element, vertex_element_type third_vertex_element)` | method | `bool` | private | Adds a triangle primitive by indexing the specified vertices (and added with add\_vertex). |

### `GPlatesOpenGL::GLStaticStreamPrimitives`

*None.*

### `GPlatesOpenGL::GLDynamicStreamPrimitives`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLSTREAMPRIMITIVES_H` | macro | `None` | — |
| `begin_vertex_array_streaming( GLRenderer &renderer, typename GLStaticStreamPrimitives<VertexType, VertexElementType>::StreamTarget &stream_target, GLBuffer::MapBufferScope &map_vertex_element_buffer_scope, unsigned int min_bytes_to_stream_in_vertex_element_buffer, GLBuffer::MapBufferScope &map_vertex_buffer_scope, unsi ...` | function | `void` | — |
| `end_vertex_array_streaming( GLRenderer &renderer, typename GLStaticStreamPrimitives<VertexType, VertexElementType>::StreamTarget &stream_target, GLBuffer::MapBufferScope &map_vertex_element_buffer_scope, GLBuffer::MapBufferScope &map_vertex_buffer_scope)` | function | `void` | — |
| `render_vertex_array_stream( GLRenderer &renderer, typename GLStaticStreamPrimitives<VertexType, VertexElementType>::StreamTarget &stream_target, const GLVertexArray::shared_ptr_type &vertex_array, GLenum primitive_mode)` | function | `void` | — |
| `suspend_render_resume_vertex_array_streaming( GLRenderer &renderer, typename GLStaticStreamPrimitives<VertexType, VertexElementType>::StreamTarget &stream_target, GLBuffer::MapBufferScope &map_vertex_element_buffer_scope, unsigned int min_bytes_to_stream_in_vertex_element_buffer, GLBuffer::MapBufferScope &map_vertex_bu ...` | function | `void` | — |

## Notes

[[[PROSE notes unit=opengl/GLStreamPrimitives tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLRasterCoRegistration](GLRasterCoRegistration.md) | opengl | 201 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 182 |
| [opengl/GLScalarField3D](GLScalarField3D.md) | opengl | 78 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 48 |
| [gui/SphericalGrid](../gui/SphericalGrid.md) | gui | 16 |
| [gui/MapBackground](../gui/MapBackground.md) | gui | 15 |
| [gui/Stars](../gui/Stars.md) | gui | 15 |
| [gui/MapGrid](../gui/MapGrid.md) | gui | 13 |
| [gui/LayerPainter](../gui/LayerPainter.md) | gui | 11 |
| [gui/OpaqueSphere](../gui/OpaqueSphere.md) | gui | 10 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLStreamPrimitives.h
python scripts/gpq.py def GPlatesOpenGL::GLStreamPrimitives --body
python scripts/gpq.py uses GLStreamPrimitives --kind class
python scripts/gpq.py hier GLStreamPrimitives
```
