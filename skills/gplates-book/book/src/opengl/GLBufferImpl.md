# GLBufferImpl

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 600 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLBufferImpl.h` | C++ | 309 |
| `src/opengl/GLBufferImpl.cc` | C++ | 92 |

## Overview

`GLBufferImpl` is the fallback half of the `GLBuffer` abstraction: the
implementation chosen by `GLBuffer::create` when `GLCapabilities` reports that
the driver lacks the buffer-object extension the caller needs. It holds the
"buffer" as a plain `boost::shared_array<GLubyte>` in system memory and lets
OpenGL read it the pre-1.5 way, as a client-side array pointer handed straight
to the draw call. That keeps the whole rendering backend able to run on a
context that has no vertex or pixel buffer objects at all, without any client of
`GLBuffer` knowing which representation it got.

Because the data never leaves system memory, the entire synchronisation half of
the `GLBuffer` contract collapses to nothing here. All three mapping entry
points simply return the array pointer, both flush operations and the unmap are
no-ops, and both `asynchronous_*_supported` predicates return true — OpenGL
copies out of a client array while dereferencing it during the draw call, so
there is no GPU-side reader to race with. `gl_map_buffer_stream` likewise
reports the whole array as available from offset zero, since no part of it needs
to be treated as still in flight.

The counterpart to that design is `get_buffer_resource`, the escape hatch the
render framework uses to obtain the raw client pointer. `GLRenderer`'s
`DrawElementsDrawable`, `DrawRangeElementsDrawable`, `ReadPixelsDrawable` and
`DrawPixelsDrawable`, the `gl_tex_image_*` and `gl_tex_sub_image_*` paths of
`GLPixelBufferImpl`, and `Implementation::GLVertexAttributeBuffer` in
`GLStateSets` all add their byte offset to it and pass the result to OpenGL where
a buffer-object offset would otherwise go. Touch this class when adding a new
kind of buffer usage: whatever `GLBufferObject` does with a bound handle, the
equivalent here has to be expressible as a pointer into this array.

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

`gl_buffer_data` always allocates a *new* array and drops the old one; it never
resizes in place and never preserves the previous contents. Any raw pointer
previously obtained from `get_buffer_resource` or from a mapping call therefore
dangles afterwards, which is exactly why the base class publishes
`has_buffer_been_allocated_since` and why `GLStateSets` re-reads the pointer
whenever that observer fires. Do not cache the pointer across a
`gl_buffer_data`.

Handing out a raw pointer is only safe because the renderer keeps a shared
reference to the `GLBufferImpl` itself until the queued drawable has been
submitted to the GPU — the comment on `get_buffer_resource` states this
explicitly. If you introduce a path that takes the pointer without the renderer
holding the object, that guarantee is gone.

The `target` and `usage` arguments are ignored entirely, as is the `GLRenderer &`
passed to the constructor; they exist only so the signatures match
`GLBufferObject`. Note also the asymmetry in NULL handling: `gl_buffer_data`
explicitly leaves the array uninitialised when `data` is NULL, mirroring
`glBufferData`, while `gl_buffer_sub_data` and `gl_get_buffer_sub_data` `memcpy`
unconditionally after only a range assertion — the base class's `std::vector`
overloads pass NULL with a zero size for an empty vector.

This is the slow path by construction. Every draw re-reads the array through the
driver instead of using GPU-resident storage, and each `gl_buffer_data` is a
fresh heap allocation and copy, so it is not something to select deliberately —
it is what you get when the extension is missing.

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
