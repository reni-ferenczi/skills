# GLBufferImpl

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 600 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLBufferImpl.h` | C++ | 309 |
| `src/opengl/GLBufferImpl.cc` | C++ | 92 |

## Overview

[[[PROSE overview unit=opengl/GLBufferImpl tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLBufferImpl`](#gplatesopenglglbufferimpl) | class | [`GLBuffer`](GLBuffer.md) | — | 0 | An implementation of the OpenGL object that supports the buffer object OpenGL extension - well it's actually the GL\_ARB\_vertex\_buffer\_object extension because its first use was for vertex buffers but it has since been extended to other ... |

## Members

### `GPlatesOpenGL::GLBufferImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_type` | typedef | `boost::shared_ptr<GLBufferImpl>` | public | A convenience typedef for a shared pointer to a GLBufferImpl. |
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const GLBufferImpl>` | public | — |
| `create( GLRenderer &renderer)` | method | `shared_ptr_type` | public | Creates a GLBufferImpl object with no array data. |
| `create_as_unique_ptr( GLRenderer &renderer)` | method | `std::unique_ptr<GLBufferImpl>` | public | Same as create but returns a std::unique\_ptr - to guarantee only one owner. |
| `get_buffer_size()` | method | `unsigned int` | public | Returns the size, in bytes, of the current buffer as allocated by gl\_buffer\_data. |
| `gl_buffer_data( GLRenderer &renderer, target_type target, unsigned int size, const void *data, usage_type usage)` | method | `void` | public | Specifies a new buffer of data. |
| `gl_buffer_sub_data( GLRenderer &renderer, target_type target, unsigned int offset, unsigned int size, const void* data)` | method | `void` | public | Specifies a new sub-section of data in the existing array. |
| `gl_get_buffer_sub_data( GLRenderer &renderer, target_type target, unsigned int offset, unsigned int size, void* data)` | method | `void` | public | Retrieves a sub-section of data from the existing array and copies it into. |
| `gl_map_buffer_static( GLRenderer &renderer, target_type target, access_type access)` | method | `GLvoid` | public | Maps the buffer for static access. |
| `asynchronous_map_buffer_dynamic_supported( GLRenderer &renderer)` | method | `bool` | public | Returns true if gl\_map\_buffer\_dynamic can be called without blocking. |
| `gl_map_buffer_dynamic( GLRenderer &renderer, target_type target)` | method | `GLvoid` | public | Maps the buffer for dynamic \*write\* access. |
| `gl_flush_buffer_dynamic( GLRenderer &renderer, target_type target, unsigned int offset, unsigned int length/*in bytes*/)` | method | `void` | public | Flushes a range of a currently mapped buffer (mapped via gl\_map\_buffer\_dynamic). |
| `asynchronous_map_buffer_stream_supported( GLRenderer &renderer)` | method | `bool` | public | Returns true if gl\_map\_buffer\_stream has fine-grained asynchronous support. |
| `gl_map_buffer_stream( GLRenderer &renderer, target_type target, unsigned int minimum_bytes_to_stream, unsigned int stream_alignment, unsigned int &stream_offset, unsigned int &stream_bytes_available)` | method | `GLvoid` | public | Maps the buffer for streaming \*write\* access. |
| `gl_flush_buffer_stream( GLRenderer &renderer, target_type target, unsigned int bytes_written)` | method | `void` | public | Specifies the number of bytes streamed after calling gl\_map\_buffer\_stream and writing data into the region mapped for streaming. |
| `gl_unmap_buffer( GLRenderer &renderer, target_type target)` | method | `GLboolean` | public | Unmaps the buffer mapped with gl\_map\_buffer\_static, gl\_map\_buffer\_dynamic or gl\_map\_buffer\_stream. |
| `get_buffer_resource()` | method | `GLubyte` | public | Implementation function accessed by buffer implementation target types. |
| `GLBufferImpl( GLRenderer &renderer)` | constructor | `None` | protected | — |
| `d_data` | field | `boost::shared_array<GLubyte>` | protected | — |
| `d_size` | field | `unsigned int` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLBUFFERIMPL_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLBufferImpl tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLRenderer](GLRenderer.md) | opengl | 175 |
| [opengl/GLStateSets](GLStateSets.md) | opengl | 55 |
| [opengl/GLReconstructedStaticPolygonMeshes](GLReconstructedStaticPolygonMeshes.md) | opengl | 31 |
| [opengl/GLPixelBufferImpl](GLPixelBufferImpl.md) | opengl | 27 |
| [opengl/GLMultiResolutionMapCubeMesh](GLMultiResolutionMapCubeMesh.md) | opengl | 21 |
| [opengl/GLRendererImpl](GLRendererImpl.md) | opengl | 21 |
| [opengl/GLOffScreenContext](GLOffScreenContext.md) | opengl | 18 |
| [opengl/GLPixelBufferObject](GLPixelBufferObject.md) | opengl | 17 |
| [opengl/GLBufferObject](GLBufferObject.md) | opengl | 14 |
| [opengl/GLMultiResolutionCubeMesh](GLMultiResolutionCubeMesh.md) | opengl | 13 |
| [opengl/GLVertexBufferImpl](GLVertexBufferImpl.md) | opengl | 13 |
| [opengl/GLRenderTarget](GLRenderTarget.md) | opengl | 10 |
| [opengl/GLState](GLState.md) | opengl | 8 |
| [opengl/GLVertexElementBufferImpl](GLVertexElementBufferImpl.md) | opengl | 6 |
| [opengl/GLBuffer](GLBuffer.md) | opengl | 3 |
| [opengl/GLContext](GLContext.md) | opengl | 3 |
| [opengl/GLCompiledDrawState](GLCompiledDrawState.md) | opengl | 2 |
| [opengl/GLMultiResolutionRasterInterface](GLMultiResolutionRasterInterface.md) | opengl | 2 |
| [opengl/GLPixelBuffer](GLPixelBuffer.md) | opengl | 2 |
| [opengl/GLVertexBuffer](GLVertexBuffer.md) | opengl | 2 |

*... and 2 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLBufferImpl.h
python scripts/gpq.py def GPlatesOpenGL::GLBufferImpl --body
python scripts/gpq.py uses GLBufferImpl --kind class
python scripts/gpq.py hier GLBufferImpl
```
