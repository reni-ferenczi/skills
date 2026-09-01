# GLBuffer

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 178 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLBuffer.h` | C++ | 612 |
| `src/opengl/GLBuffer.cc` | C++ | 229 |

## Overview

[[[PROSE overview unit=opengl/GLBuffer tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLBuffer`](#gplatesopenglglbuffer) | class | `boost::enable_shared_from_this<GLBuffer>` | — | 2 | An abstraction based on an OpenGL object that supports the buffer object OpenGL extension - well it's actually the GL\_ARB\_vertex\_buffer\_object extension because its first use was for vertex buffers but it has since been extended to other ... |

## Members

### `GPlatesOpenGL::GLBuffer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_type` | typedef | `boost::shared_ptr<GLBuffer>` | public | A convenience typedef for a shared pointer to a non-const GLBuffer. |
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const GLBuffer>` | public | — |
| `weak_ptr_type` | typedef | `boost::weak_ptr<GLBuffer>` | public | A convenience typedef for a weak pointer to a GLBuffer. |
| `weak_ptr_to_const_type` | typedef | `boost::weak_ptr<const GLBuffer>` | public | — |
| `BufferType` | enum | `None` | public | The buffer types that a buffer can be used for. |
| `buffers_type` | typedef | `std::bitset<NUM_BUFFER_TYPES>` | public | A std::bitset for setting which buffer types a buffer will be used for. |
| `BUFFER_TYPE_VERTEX` | field | `buffers_type` | public | The supported buffer types. |
| `BUFFER_TYPE_PIXEL` | field | `buffers_type` | public | — |
| `target_type` | typedef | `unsigned int` | public | Typedef for a target of this buffer. |
| `TARGET_ARRAY_BUFFER` | field | `target_type` | public | The supported targets. |
| `TARGET_ELEMENT_ARRAY_BUFFER` | field | `target_type` | public | — |
| `TARGET_PIXEL_UNPACK_BUFFER` | field | `target_type` | public | — |
| `TARGET_PIXEL_PACK_BUFFER` | field | `target_type` | public | — |
| `usage_type` | typedef | `unsigned int` | public | Typedef for the usage of the buffer. |
| `USAGE_STATIC_DRAW` | field | `usage_type` | public | STATIC - You will specify the data only once (or possibly very rarely), then use it many times without modifying it. |
| `USAGE_STATIC_READ` | field | `usage_type` | public | — |
| `USAGE_STATIC_COPY` | field | `usage_type` | public | — |
| `USAGE_DYNAMIC_DRAW` | field | `usage_type` | public | DYNAMIC - You will specify or modify the data repeatedly, and use it repeatedly after each time you do this. |
| `USAGE_DYNAMIC_READ` | field | `usage_type` | public | — |
| `USAGE_DYNAMIC_COPY` | field | `usage_type` | public | — |
| `USAGE_STREAM_DRAW` | field | `usage_type` | public | STREAM - You will modify the data once, then use it once, and repeat this process many times. |
| `USAGE_STREAM_READ` | field | `usage_type` | public | — |
| `USAGE_STREAM_COPY` | field | `usage_type` | public | — |
| `access_type` | typedef | `unsigned int` | public | Typedef for regular mapped access to the buffer. |
| `ACCESS_READ_ONLY` | field | `access_type` | public | — |
| `ACCESS_WRITE_ONLY` | field | `access_type` | public | — |
| `ACCESS_READ_WRITE` | field | `access_type` | public | — |
| `create( GLRenderer &renderer, const buffers_type &buffer_types)` | method | `shared_ptr_type` | public | Creates a GLBuffer object with no array data. buffer\_types specifies the types of buffer that will be used. |
| `create_as_unique_ptr( GLRenderer &renderer, const buffers_type &buffer_types)` | method | `std::unique_ptr<GLBuffer>` | public | Same as create but returns a std::unique\_ptr - to guarantee only one owner. |
| `~GLBuffer()` | destructor | `None` | public | — |
| `get_buffer_size()` | method | `unsigned int` | public | Returns the size, in bytes, of the current buffer as allocated by gl\_buffer\_data. |
| `gl_buffer_data( GLRenderer &renderer, target_type target, unsigned int size, const void *data, usage_type usage)` | method | `void` | public | Specifies a new buffer of data. |
| `gl_buffer_data( GLRenderer &renderer, target_type target, const std::vector<ElementType> &data, usage_type usage)` | method | `void` | public | Similar to the other overload of gl\_buffer\_data but using a std::vector. |
| `gl_buffer_sub_data( GLRenderer &renderer, target_type target, unsigned int offset, unsigned int size, const void* data)` | method | `void` | public | Specifies a new sub-section of data in the existing array. |
| `gl_buffer_sub_data( GLRenderer &renderer, target_type target, unsigned int offset, const std::vector<ElementType> &data)` | method | `void` | public | Similar to the other overload of gl\_buffer\_sub\_data but using a std::vector. |
| `gl_get_buffer_sub_data( GLRenderer &renderer, target_type target, unsigned int offset, unsigned int size, void* data)` | method | `void` | public | Retrieves a sub-section of data from the existing array and copies it into data. |
| `gl_map_buffer_static( GLRenderer &renderer, target_type target, access_type access)` | method | `GLvoid` | public | Maps the buffer for static access. |
| `asynchronous_map_buffer_dynamic_supported( GLRenderer &renderer)` | method | `bool` | public | Returns true if gl\_map\_buffer\_dynamic can be called without blocking. |
| `gl_map_buffer_dynamic( GLRenderer &renderer, target_type target)` | method | `GLvoid` | public | Maps the buffer for dynamic \*write\* access. |
| `gl_flush_buffer_dynamic( GLRenderer &renderer, target_type target, unsigned int offset, unsigned int length/*in bytes*/)` | method | `void` | public | Flushes a range of a currently mapped buffer (mapped via gl\_map\_buffer\_dynamic). |
| `asynchronous_map_buffer_stream_supported( GLRenderer &renderer)` | method | `bool` | public | Returns true if gl\_map\_buffer\_stream has fine-grained asynchronous support. |
| `gl_map_buffer_stream( GLRenderer &renderer, target_type target, unsigned int minimum_bytes_to_stream, unsigned int stream_alignment, unsigned int &stream_offset, unsigned int &stream_bytes_available)` | method | `GLvoid` | public | Maps the buffer for streaming \*write\* access. |
| `gl_flush_buffer_stream( GLRenderer &renderer, target_type target, unsigned int bytes_written)` | method | `void` | public | Specifies the number of bytes streamed after calling gl\_map\_buffer\_stream and writing data into the region mapped for streaming. bytes\_written is the number of bytes streamed into the region mapped by gl\_map\_buffer\_stream. |
| `gl_unmap_buffer( GLRenderer &renderer, target_type target)` | method | `GLboolean` | public | Unmaps the buffer mapped with gl\_map\_buffer\_static, gl\_map\_buffer\_dynamic or gl\_map\_buffer\_stream. |
| `MapBufferScope` | class | `None` | public | RAII class to call gl\_map\_buffer\_static and gl\_unmap\_buffer over a scope. |
| `buffer_allocation_observer_type` | typedef | `GPlatesUtils::ObserverToken` | public | Typedef for an observer of buffer allocations. |
| `has_buffer_been_allocated_since( const buffer_allocation_observer_type &buffer_allocation_observer)` | method | `bool` | public | Returns true if a buffer has been allocated (ie, is gl\_buffer\_data has been called) since buffer\_allocation\_observer was last passed to this method. |
| `update_buffer_allocation_observer( buffer_allocation_observer_type &buffer_allocation_observer)` | method | `void` | public | Updates the specified buffer allocation observer so that a call to has\_buffer\_been\_allocated\_since will subsequently return false. |
| `allocated_buffer()` | method | `void` | protected | Derived classes can notify clients that a buffer allocation has occurred. |
| `buffer_allocation_subject_type` | typedef | `GPlatesUtils::SubjectToken` | private | Typedef for a subject of buffer allocations. |
| `d_buffer_allocation_subject` | field | `buffer_allocation_subject_type` | private | Keeps track of buffer allocations (ie, calls to 'gl\_buffer\_data'). |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `BUFFER_TYPE_VERTEX` | variable | `GPlatesOpenGL::GLBuffer::buffers_type` | — |
| `BUFFER_TYPE_PIXEL` | variable | `GPlatesOpenGL::GLBuffer::buffers_type` | — |
| `TARGET_ARRAY_BUFFER` | variable | `GPlatesOpenGL::GLBuffer::target_type` | — |
| `TARGET_ELEMENT_ARRAY_BUFFER` | variable | `GPlatesOpenGL::GLBuffer::target_type` | — |
| `TARGET_PIXEL_UNPACK_BUFFER` | variable | `GPlatesOpenGL::GLBuffer::target_type` | — |
| `TARGET_PIXEL_PACK_BUFFER` | variable | `GPlatesOpenGL::GLBuffer::target_type` | — |
| `USAGE_STATIC_DRAW` | variable | `GPlatesOpenGL::GLBuffer::usage_type` | — |
| `USAGE_STATIC_READ` | variable | `GPlatesOpenGL::GLBuffer::usage_type` | — |
| `USAGE_STATIC_COPY` | variable | `GPlatesOpenGL::GLBuffer::usage_type` | — |
| `USAGE_DYNAMIC_DRAW` | variable | `GPlatesOpenGL::GLBuffer::usage_type` | — |
| `USAGE_DYNAMIC_READ` | variable | `GPlatesOpenGL::GLBuffer::usage_type` | — |
| `USAGE_DYNAMIC_COPY` | variable | `GPlatesOpenGL::GLBuffer::usage_type` | — |
| `USAGE_STREAM_DRAW` | variable | `GPlatesOpenGL::GLBuffer::usage_type` | — |
| `USAGE_STREAM_READ` | variable | `GPlatesOpenGL::GLBuffer::usage_type` | — |
| `USAGE_STREAM_COPY` | variable | `GPlatesOpenGL::GLBuffer::usage_type` | — |
| `ACCESS_READ_ONLY` | variable | `GPlatesOpenGL::GLBuffer::access_type` | — |
| `ACCESS_WRITE_ONLY` | variable | `GPlatesOpenGL::GLBuffer::access_type` | — |
| `ACCESS_READ_WRITE` | variable | `GPlatesOpenGL::GLBuffer::access_type` | — |
| `GPLATES_OPENGL_GLBUFFER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLBuffer tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLRasterCoRegistration](GLRasterCoRegistration.md) | opengl | 303 |
| [opengl/GLScalarField3D](GLScalarField3D.md) | opengl | 241 |
| [opengl/GLContext](GLContext.md) | opengl | 178 |
| [opengl/GLProgramObject](GLProgramObject.md) | opengl | 150 |
| [opengl/GLStateSets](GLStateSets.md) | opengl | 113 |
| [opengl/GLBufferObject](GLBufferObject.md) | opengl | 78 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 67 |
| [opengl/GLTextureUtils](GLTextureUtils.md) | opengl | 65 |
| [opengl/GLMultiResolutionRaster](GLMultiResolutionRaster.md) | opengl | 62 |
| [gui/LayerPainter](../gui/LayerPainter.md) | gui | 56 |
| [opengl/GLFilledPolygonsGlobeView](GLFilledPolygonsGlobeView.md) | opengl | 55 |
| [opengl/GLRenderer](GLRenderer.md) | opengl | 55 |
| [opengl/GLShaderProgramUtils](GLShaderProgramUtils.md) | opengl | 55 |
| [opengl/GLVertexArrayObject](GLVertexArrayObject.md) | opengl | 52 |
| [opengl/GLVertexArrayImpl](GLVertexArrayImpl.md) | opengl | 49 |
| [opengl/GLTexture](GLTexture.md) | opengl | 45 |
| [opengl/GLFrameBufferObject](GLFrameBufferObject.md) | opengl | 44 |
| [opengl/GLFilledPolygonsMapView](GLFilledPolygonsMapView.md) | opengl | 43 |
| [opengl/GLBufferImpl](GLBufferImpl.md) | opengl | 42 |
| [opengl/GLScalarField3DGenerator](GLScalarField3DGenerator.md) | opengl | 42 |

*... and 41 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLBuffer.h
python scripts/gpq.py def GPlatesOpenGL::GLBuffer --body
python scripts/gpq.py uses GLBuffer --kind class
python scripts/gpq.py hier GLBuffer
```
