# GLBuffer

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 178 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLBuffer.h` | C++ | 612 |
| `src/opengl/GLBuffer.cc` | C++ | 229 |

## Overview

`GLBuffer` is the rendering backend's abstraction of an OpenGL buffer object — a
block of storage the GPU reads vertices, vertex indices or pixel data out of, or
writes pixel data into. The interface deliberately mirrors the ARB
buffer-object entry points (`glBufferData`, `glBufferSubData`,
`glGetBufferSubData`, `glMapBuffer`, `glUnmapBuffer`) so that client code reads
like OpenGL code, with one difference: every call takes a `GLRenderer &` rather
than depending on whatever is currently bound. The renderer owns binding state,
and the buffer-object implementation binds itself and restores the previous
binding around each direct GL call it makes.

The class exists because GPlates still supports drivers without
`GL_ARB_vertex_buffer_object` or `GL_ARB_pixel_buffer_object`, and `create` is
the single place that decision is made. It asks `GLCapabilities` (through
`GLRenderer::get_capabilities`) about each buffer type the caller named in the
`buffers_type` bitset, and returns a `GLBufferObject` only if every requested
type is supported; otherwise it returns a `GLBufferImpl`, which simulates the
buffer in client-side memory. This is why callers must declare their intended
buffer types up front instead of at first use: a buffer meant to be filled by a
pixel read and then drawn as vertices has to fall back if either extension is
missing, and by then it is too late to change representation. Everything layered
on top — `GLVertexBuffer`, `GLVertexElementBuffer`, `GLPixelBuffer` and their
`*Impl`/`*Object` pairs, and through them `GLRenderer` and the painters — is
written against this interface and never against the choice.

The three mapping families are the substance of the design, and they differ in
how they avoid stalling on the GPU rather than in what they write.
`gl_map_buffer_static` is always available and may block if the GPU is still
reading the buffer; `gl_map_buffer_dynamic` maps for write and lets the caller
declare, through `gl_flush_buffer_dynamic`, exactly which sub-ranges it touched;
`gl_map_buffer_stream` hands back only the still-unwritten tail of the buffer so
the caller can append and draw repeatedly, orphaning the whole allocation only
when the tail runs out. The two `asynchronous_*_supported` predicates report
whether the underlying extensions can actually deliver that behaviour — they
never gate the calls, they only tell the caller whether the fast path exists.
The buffer-allocation observer at the end of the header is render-framework
plumbing rather than a client feature: `Implementation::GLVertexAttributeBuffer`
in `GLStateSets` uses it to notice that `gl_buffer_data` has been called since
vertex attribute pointers were last submitted, because ATI drivers were observed
to need those pointers rebound after every `glBufferData`.

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

Ownership is `boost::shared_ptr` rather than the `non_null_intrusive_ptr` used
almost everywhere else in the tree, purely so buffers can be held by
`GPlatesUtils::ObjectCache`. The base also derives from
`boost::enable_shared_from_this`, and `GLBufferObject` calls `shared_from_this()`
on every data-path method in order to bind itself through the renderer — so an
instance must genuinely be owned by a `shared_ptr` before any of those methods
run. `create_as_unique_ptr` exists so the factory chain can compose without an
intermediate shared count; in this tree every one of those unique pointers is
immediately `release()`d into a `shared_ptr` by the matching `create`.

The size is zero until the first `gl_buffer_data`, and every sub-data, flush and
stream call asserts that its range fits within it — a violation is a
`PreconditionViolationError`, not a GL error. `gl_buffer_data` with a NULL data
pointer is meaningful: it allocates uninitialised storage, and it is the
orphaning idiom the mapping documentation refers to. `gl_buffer_data` is also
the only operation that counts as an allocation for
`has_buffer_been_allocated_since`; sub-data and mapping do not.

`MapBufferScope` does not map in its constructor — it only guarantees the
unmap. Its map and unmap calls must be matched and non-nested (it asserts that
no map is outstanding when you map, and that one is when you flush or unmap),
and its destructor unmaps only if one is still outstanding, swallowing any
exception and discarding the `GLboolean` result. If the "contents were
corrupted" return value matters to you — it reports events such as a video
memory loss across an ALT+TAB — call `gl_unmap_buffer` explicitly rather than
letting the scope do it.

Unlike `glMapBuffer`, the mapping methods throw on failure instead of returning
NULL, so callers must not test the returned pointer; they must be prepared for
an exception instead.

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
