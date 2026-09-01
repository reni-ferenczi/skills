# GLBufferObject

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 530 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLBufferObject.h` | C++ | 339 |
| `src/opengl/GLBufferObject.cc` | C++ | 739 |

## Overview

`GLBufferObject` is the real implementation behind `GLBuffer` — the one chosen
whenever `GLCapabilities` reports `GL_ARB_vertex_buffer_object` (and, for pixel
targets, `GL_ARB_pixel_buffer_object`). Its second base, `GLObject`, is an empty
marker: it adds only `boost::shared_ptr`/`weak_ptr` typedefs and a virtual
destructor, and its own comment explains that `boost::shared_ptr` is used rather
than `non_null_intrusive_ptr` so instances can go into a
`GPlatesUtils::ObjectCache`. The GL name comes from `GLObjectResource` with the
nested `Allocator` policy supplying `glGenBuffersARB`/`glDeleteBuffersARB`, and
the resource manager it allocates from belongs to the shared state of the
`GLContext` (`get_buffer_object_resource_manager`). That indirection is what
makes destruction safe from anywhere: the resource is only *queued* for
deallocation, and `GLContext` drains the queue at a point where the right
context is current — or, if the context is already gone, drops the handle
silently because the driver destroyed it along with the context.

No method here assumes anything about the current GL binding, and none leaves a
binding behind. Every method that issues GL opens with a
`GLRenderer::BindBufferObjectAndApply` scope, which records the renderer's
current binding for the target, applies this buffer's binding to real OpenGL
immediately (rather than deferring it as the renderer normally would), and
restores the previous one on exit. The direct `glBufferDataARB`,
`glMapBufferARB` and friends inside then operate on a binding the renderer knows
about, so the shadowed state in `GLState` never diverges from the driver's.

The substance of the file is `d_uninitialised_offset` and the streaming path
built on it. The offset is the first byte of the current allocation that the
client has not yet written since the buffer was last orphaned, and therefore the
first byte the GPU cannot still be reading. `gl_map_buffer_stream` rounds it up
to the requested alignment, then either maps just that tail without
synchronisation, or — if the tail can no longer satisfy `minimum_bytes_to_stream`
— orphans the whole allocation, resets the offset to zero and maps from the
start. Each of the three capability paths implements that same policy with a
different mechanism: `GL_ARB_map_buffer_range` with explicit range flags,
`GL_APPLE_flush_buffer_range` with `glBufferParameteriAPPLE` plus a full-buffer
map, and, with neither extension, a re-`gl_buffer_data` of the same size and a
NULL pointer, which is the classic orphaning idiom. `GLStreamPrimitives`
(`begin_vertex_array_streaming`) is the client this exists for: it maps the
vertex and vertex-element buffers this way so painters can keep appending
geometry and issuing draw calls without waiting on the GPU.

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

The GL name in `d_resource` is allocated once in the constructor and never
replaced; orphaning swaps the *storage* behind that name, not the name itself.
Deallocation is queued on the context's resource manager, so a `GLBufferObject`
may be destroyed on a path where no context is current, but the queue must
eventually be drained by `GLContext` for the driver-side names to be freed.

`d_uninitialised_offset` is the invariant to keep straight when editing
anything here. It is set to zero by `gl_buffer_data` with a NULL data pointer
and to the full size when data is supplied; advanced by `gl_buffer_sub_data`,
`gl_flush_buffer_dynamic` and `gl_flush_buffer_stream` to the end of the range
touched; and forced to the full size by `gl_map_buffer_static`, which has to
assume the whole buffer was written. The practical consequence is that mixing a
static map, or a sub-data write near the end, into a streaming buffer costs a
full orphan on the very next `gl_map_buffer_stream`. Note also that the offset
only ever moves forward past written ranges — uninitialised gaps *before* a
flushed range are deliberately counted as initialised.

The two streaming flush paths use different offset conventions and it is easy to
get wrong: the `GL_ARB_map_buffer_range` path flushes from offset zero because
it mapped only the tail, while the `GL_APPLE_flush_buffer_range` path flushes
from `d_uninitialised_offset` because it had to map the whole buffer. The ARB
streaming path also deliberately does **not** combine
`GL_MAP_UNSYNCHRONIZED_BIT` with `GL_MAP_INVALIDATE_BUFFER_BIT`: the in-code
comment records that doing so made an nVidia 780Ti (driver 364.96) hand back the
same allocation, overwriting data the GPU had not consumed, which showed up as
flickering cross-sections and surface masks in the 3D scalar field rendering.

A stream discard calls `allocated_buffer()` even though no `glBufferData`
happened, so that `GLStateSets` re-submits vertex attribute pointers — the same
ATI workaround that motivates the observer on the base class. If you add another
path that orphans, it needs the same notification.

Every entry point asserts `is_target_type_supported`, so using a buffer with a
target outside the `buffers_type` set passed to `create` is a
`PreconditionViolationError`, not a GL error; an unrecognised target aborts
outright. The constructor and `Allocator::allocate` both assert
`gl_ARB_vertex_buffer_object`, which is the contract that only
`GLBuffer::create` may decide to instantiate this class. Mapping failures call
`GLUtils::check_gl_errors` (which throws on any pending GL error) and then, in
debug builds, abort; in release builds they throw `OpenGLException`, so a
mapping call never returns NULL. `gl_unmap_buffer` is the exception: a GL_FALSE
result means the contents were lost rather than that the call was misused, so it
is warned about and returned to the caller.

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
