# GLObjectResourceManager

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 1300 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLObjectResourceManager.h` | C++ | 123 |

## Overview

`GLObjectResourceManager` is the allocation/deallocation half of the `GLObjectResource` pair: it holds a `ResourceAllocatorType` policy object that knows how to allocate and deallocate one kind of raw OpenGL handle (texture, buffer, shader, program, etc.), and each `GLObjectResourceManager<ResourceHandleType, ResourceAllocatorType>` instantiation manages exactly that one resource kind for one `GLContext`.

Deallocation is deliberately two-phase: `queue_resource_for_deallocation` only records a handle, and the actual `ResourceAllocatorType::deallocate` calls happen later, in a batch, from `deallocate_queued_resources`. This lets `GLObjectResource` destructors run at arbitrary times — including when no OpenGL context is current — without making OpenGL calls; the caller is expected to invoke `deallocate_queued_resources` periodically while the context *is* current, such as right after rendering a frame.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLObjectResourceManager`](#gplatesopenglglobjectresourcemanager) | class | — | `<typename ResourceHandleType, class ResourceAllocatorType>` | 0 | Allocates and deallocates OpenGL object resources (such as texture objects). |

## Members

### `GPlatesOpenGL::GLObjectResourceManager`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `this_type` | typedef | `GLObjectResourceManager<ResourceHandleType, ResourceAllocatorType>` | public | Typedef for this class. |
| `shared_ptr_type` | typedef | `boost::shared_ptr<this_type>` | public | Typedef for a shared pointer to GLObjectResourceManager. |
| `create( const ResourceAllocatorType &resource_allocator = ResourceAllocatorType())` | method | `shared_ptr_type` | public | Creates a GLObjectResourceManager object. |
| `allocate_resource( const GLCapabilities &capabilities)` | method | `ResourceHandleType` | public | Allocates an OpenGL resource using the 'ResourceAllocatorType' policy. |
| `queue_resource_for_deallocation( ResourceHandleType resource)` | method | `void` | public | Queues a resource for deallocation when deallocate\_queued\_resources is called. |
| `deallocate_queued_resources()` | method | `void` | public | Deallocates all resources queued up by queue\_resource\_for\_deallocation. |
| `resource_deallocation_queue_type` | typedef | `std::vector<ResourceHandleType>` | private | — |
| `d_resource_allocator` | field | `ResourceAllocatorType` | private | — |
| `d_resource_deallocation_queue` | field | `resource_deallocation_queue_type` | private | — |
| `GLObjectResourceManager( const ResourceAllocatorType &resource_allocator)` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLOBJECTRESOURCEMANAGER_H` | macro | `None` | — |

## Notes

- If `deallocate_queued_resources` is not called regularly while the context is current, released OpenGL resources accumulate in `d_resource_deallocation_queue` and are never actually freed on the GPU.
- `allocate_resource` and `deallocate_queued_resources` both make real OpenGL calls (through the allocator policy) and therefore require a current OpenGL context; only `queue_resource_for_deallocation` is safe to call without one.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLObjectResource](GLObjectResource.md) | opengl | 5 |
| [opengl/GLContext](GLContext.md) | opengl | 4 |
| [opengl/GLBufferObject](GLBufferObject.md) | opengl | 2 |
| [opengl/GLFrameBufferObject](GLFrameBufferObject.md) | opengl | 2 |
| [opengl/GLProgramObject](GLProgramObject.md) | opengl | 2 |
| [opengl/GLRenderBufferObject](GLRenderBufferObject.md) | opengl | 2 |
| [opengl/GLShaderObject](GLShaderObject.md) | opengl | 2 |
| [opengl/GLTexture](GLTexture.md) | opengl | 2 |
| [opengl/GLVertexArrayObject](GLVertexArrayObject.md) | opengl | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLObjectResourceManager.h
python scripts/gpq.py def GPlatesOpenGL::GLObjectResourceManager --body
python scripts/gpq.py uses GLObjectResourceManager --kind class
python scripts/gpq.py hier GLObjectResourceManager
```
