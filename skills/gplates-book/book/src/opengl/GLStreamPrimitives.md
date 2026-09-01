# GLStreamPrimitives

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 13 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLStreamPrimitives.h` | C++ | 2308 |

## Overview

This header gives the painters a `glBegin`/`glEnd`-shaped interface that actually writes into vertex-buffer memory. GPlates generates its geometry per frame from reconstructed features, so the painters in `gui` — `GlobeRenderedGeometryLayerPainter`, `MapRenderedGeometryLayerPainter`, `LayerPainter` and the decorations like `Stars`, `MapGrid` and `SphericalGrid` — cannot pre-build static meshes; they need to emit vertices one at a time into a mapped buffer and draw when it fills. `GLStreamPrimitives` is that machine, and it is header-only and templated on the vertex type, the index type (`GLuint`, `GLushort` or `GLubyte`) and a stream-writer policy, so each painter streams its own vertex layout without a virtual call per vertex.

The pieces divide cleanly. `GLStreamPrimitives` itself holds the two output streams — vertices and indices — and exposes the primitive assembly only through nested adapter classes, each of which turns a primitive topology into indexed output. That output is always `GL_POINTS`, `GL_LINES` or `GL_TRIANGLES`: strips, fans, loops and quads are unrolled at stream time, so the topology is a property of the adapter you used, not of the draw call. `StreamTarget` is the RAII pairing that binds a stream to concrete buffers, and it is deliberately separate from the adapters so that a single logical primitive can span more than one buffer: when an `add_vertex` returns `false` the caller stops streaming, draws, remaps, restarts streaming, and re-submits only the vertex that failed — the adapter's own state (the strip's shared vertices, the loop's start vertex) survives the interruption. `Primitives` is the escape hatch for hot loops: it checks capacity once per primitive via `begin_primitive` and then writes vertices and explicit indices with no per-vertex bounds check at all.

The free functions at the bottom package the common case of streaming into real GL buffers. `begin_vertex_array_streaming` maps a vertex buffer and a vertex element buffer through `GLBuffer::MapBufferScope::gl_map_buffer_stream`, converts the byte offsets the mapping returns into vertex and index counts, and seeds the stream writers with those as their initial counts so the emitted indices are already correct for the buffer region. `end_vertex_array_streaming` flushes and unmaps, `render_vertex_array_stream` issues one `gl_draw_range_elements` over exactly what was streamed, and `suspend_render_resume_vertex_array_streaming` is the three composed — which is what a painter calls when a buffer fills mid-geometry.

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

**Never draw with the mode you streamed with.** `Quads` streams quads but emits `GL_TRIANGLES`; the strip and fan adapters likewise emit `GL_TRIANGLES`, and `Lines`, `LineStrips` and `LineLoops` all emit `GL_LINES`. Passing `GL_QUADS` or `GL_TRIANGLE_STRIP` to the draw call because that is what you fed the stream produces garbage.

**A `false` return is not an error, it is backpressure.** `add_vertex` returning `false` means the vertex or index stream is full and *nothing was written* for that call — capacity is checked before any write. The recovery is fixed: `stop_streaming`, draw, remap, `start_streaming`, then re-submit the same vertex. Treating `false` as fatal, or forgetting to re-submit, silently drops geometry. `LineLoops::end_line_loop` can also return `false` and must be called again after the same recovery.

**Incomplete primitives are dropped silently.** An odd number of vertices in a `Lines` block loses the trailing one; a one-vertex line strip or loop produces nothing. These are documented behaviours, not assertion failures.

**Streaming must be inside a `start_streaming`/`stop_streaming` pair.** Every `add_*` asserts on `d_vertex_stream` and `d_vertex_element_stream` being valid and throws `PreconditionViolationError` otherwise. The reverse ordering is fine and expected: an adapter's `begin_*`/`end_*` pair may span several streaming pairs.

**Adapters hold a reference to the stream, not ownership.** `Points` stores a pointer and the rest store references to the `GLStreamPrimitives`, and `StreamTarget` does too; all of them must not outlive it. Adapters are cheap and are normally constructed on the stack per drawing pass.

**`Primitives` does not bounds-check.** After `begin_primitive` returns `true` you must not exceed the vertex and index counts you asked for — `add_vertex` and `add_vertex_element` write unconditionally. Its indices are also relative to the primitive's base, added to `d_base_vertex_element` on write, whereas the other adapters emit absolute indices.

**Index reuse is deliberately shallow.** Only the sharing inherent in strips, fans and loops is exploited. The header is explicit that a complex mesh is better served by hand-built vertex and index buffers, since the post-transform vertex cache can only help when reuse is close together in the index stream.

**Interaction with the renderer's queueing.** These streams write into a buffer that is reused across draws, which is exactly the situation `GLRenderer::begin_render_queue_block` warns about: if the draw calls are queued rather than issued, they all end up reading the buffer's final contents. Stream and draw in the same immediate pass.

**Unmap failure is a warning, not an exception.** `end_vertex_array_streaming` checks both `gl_unmap_buffer` results and emits a `qWarning` if the mapped data was corrupted; the frame carries on regardless, so a corrupted stream shows up as visual garbage plus a log line.

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
