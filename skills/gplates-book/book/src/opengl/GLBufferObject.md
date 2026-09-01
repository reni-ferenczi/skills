# GLBufferObject

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 530 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLBufferObject.h` | C++ | 339 |
| `src/opengl/GLBufferObject.cc` | C++ | 739 |

## Overview

[[[PROSE overview unit=opengl/GLBufferObject tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLBufferObject`](#gplatesopenglglbufferobject) | class | [`GLBuffer`](GLBuffer.md)<br>[`GLObject`](GLObject.md) | — | 0 | An OpenGL object that supports the buffer object OpenGL extension - well it's actually the GL\_ARB\_vertex\_buffer\_object extension because its first use was for vertex buffers but it has since been extended to other objects (such as pixel ... |

## Members

### `GPlatesOpenGL::GLBufferObject`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_type` | typedef | `boost::shared_ptr<GLBufferObject>` | public | A convenience typedef for a shared pointer to a GLBufferObject. |
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const GLBufferObject>` | public | — |
| `weak_ptr_type` | typedef | `boost::weak_ptr<GLBufferObject>` | public | A convenience typedef for a weak pointer to a GLBufferObject. |
| `weak_ptr_to_const_type` | typedef | `boost::weak_ptr<const GLBufferObject>` | public | — |
| `resource_handle_type` | typedef | `GLuint` | public | Typedef for a resource handle. |
| `Allocator` | class | `None` | public | Policy class to allocate and deallocate OpenGL buffer objects. |
| `resource_type` | typedef | `GLObjectResource<resource_handle_type, Allocator>` | public | Typedef for a resource. |
| `resource_manager_type` | typedef | `GLObjectResourceManager<resource_handle_type, Allocator>` | public | Typedef for a resource manager. |
| `create( GLRenderer &renderer, const buffers_type &buffer_types)` | method | `shared_ptr_type` | public | Creates a GLBufferObject object with no array data. |
| `create_as_unique_ptr( GLRenderer &renderer, const buffers_type &buffer_types)` | method | `std::unique_ptr<GLBufferObject>` | public | Same as create but returns a std::unique\_ptr - to guarantee only one owner. |
| `get_buffer_size()` | method | `unsigned int` | public | Returns the size, in bytes, of the current buffer as allocated by gl\_buffer\_data. |
| `gl_buffer_data( GLRenderer &renderer, target_type target, unsigned int size, const void* data, usage_type usage)` | method | `void` | public | Specifies a new buffer of data. |
| `gl_buffer_sub_data( GLRenderer &renderer, target_type target, unsigned int offset, unsigned int size, const void* data)` | method | `void` | public | Specifies a new sub-section of data in the existing array. |
| `gl_get_buffer_sub_data( GLRenderer &renderer, target_type target, unsigned int offset, unsigned int size, void* data)` | method | `void` | public | Retrieves a sub-section of data from the existing array and copies it into. |
| `gl_map_buffer_static( GLRenderer &renderer, target_type target, access_type access)` | method | `GLvoid` | public | Maps the buffer for the specified access. |
| `asynchronous_map_buffer_dynamic_supported( GLRenderer &renderer)` | method | `bool` | public | Returns true if gl\_map\_buffer\_dynamic can be called without blocking. |
| `gl_map_buffer_dynamic( GLRenderer &renderer, target_type target)` | method | `GLvoid` | public | Maps the buffer for dynamic \*write\* access. |
| `gl_flush_buffer_dynamic( GLRenderer &renderer, target_type target, unsigned int offset, unsigned int length/*in bytes*/)` | method | `void` | public | Flushes a range of a currently mapped buffer (mapped via gl\_map\_buffer\_dynamic). |
| `asynchronous_map_buffer_stream_supported( GLRenderer &renderer)` | method | `bool` | public | Returns true if gl\_map\_buffer\_stream has fine-grained asynchronous support. |
| `gl_map_buffer_stream( GLRenderer &renderer, target_type target, unsigned int minimum_bytes_to_stream, unsigned int stream_alignment, unsigned int &stream_offset, unsigned int &stream_bytes_available)` | method | `GLvoid` | public | Maps the buffer for streaming \*write\* access. |
| `gl_flush_buffer_stream( GLRenderer &renderer, target_type target, unsigned int bytes_written)` | method | `void` | public | Specifies the number of bytes streamed after calling gl\_map\_buffer\_stream and writing data into the region mapped for streaming. |
| `gl_unmap_buffer( GLRenderer &renderer, target_type target)` | method | `GLboolean` | public | Unmaps the buffer mapped with gl\_map\_buffer\_static, gl\_map\_buffer\_dynamic or gl\_map\_buffer\_stream. |
| `get_buffer_resource_handle()` | method | `resource_handle_type` | public | Returns the buffer resource handle. |
| `GLBufferObject( GLRenderer &renderer, const buffers_type &buffer_types)` | constructor | `None` | protected | Constructor. |
| `d_buffer_types` | field | `buffers_type` | private | The buffer types that this buffer object is limited to targeting. |
| `d_resource` | field | `resource_type::non_null_ptr_to_const_type` | private | — |
| `d_size` | field | `unsigned int` | private | — |
| `d_usage` | field | `boost::optional<usage_type>` | private | — |
| `d_uninitialised_offset` | field | `unsigned int` | private | Current offset into buffer where uninitialised memory is (memory that hasn't been yet been written to by the client). |
| `is_target_type_supported( target_type target)` | method | `bool` | private | Returns true if target type corresponds to one of our buffer types. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLBUFFEROBJECT_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLBufferObject tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLContext](GLContext.md) | opengl | 31 |
| [opengl/GLPixelBufferObject](GLPixelBufferObject.md) | opengl | 30 |
| [opengl/GLPixelBufferImpl](GLPixelBufferImpl.md) | opengl | 23 |
| [opengl/GLStateSets](GLStateSets.md) | opengl | 22 |
| [opengl/GLState](GLState.md) | opengl | 19 |
| [opengl/GLRenderer](GLRenderer.md) | opengl | 16 |
| [opengl/GLProgramObject](GLProgramObject.md) | opengl | 10 |
| [opengl/GLShaderObject](GLShaderObject.md) | opengl | 9 |
| [opengl/GLVertexArrayObject](GLVertexArrayObject.md) | opengl | 7 |
| [opengl/GLVertexBufferObject](GLVertexBufferObject.md) | opengl | 7 |
| [opengl/GLVertexElementBufferObject](GLVertexElementBufferObject.md) | opengl | 7 |
| [opengl/GLMultiResolutionCubeMesh](GLMultiResolutionCubeMesh.md) | opengl | 6 |
| [opengl/GLOffScreenContext](GLOffScreenContext.md) | opengl | 6 |
| [opengl/GLMultiResolutionMapCubeMesh](GLMultiResolutionMapCubeMesh.md) | opengl | 5 |
| [opengl/GLRenderBufferObject](GLRenderBufferObject.md) | opengl | 5 |
| [opengl/GLRenderTarget](GLRenderTarget.md) | opengl | 5 |
| [opengl/GLFrameBufferObject](GLFrameBufferObject.md) | opengl | 4 |
| [opengl/GLReconstructedStaticPolygonMeshes](GLReconstructedStaticPolygonMeshes.md) | opengl | 3 |
| [opengl/GLPixelBuffer](GLPixelBuffer.md) | opengl | 2 |
| [opengl/GLTexture](GLTexture.md) | opengl | 2 |

*... and 4 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLBufferObject.h
python scripts/gpq.py def GPlatesOpenGL::GLBufferObject --body
python scripts/gpq.py uses GLBufferObject --kind class
python scripts/gpq.py hier GLBufferObject
```
