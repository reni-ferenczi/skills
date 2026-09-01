# GLObjectResourceManager

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 1300 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLObjectResourceManager.h` | C++ | 123 |

## Overview

[[[PROSE overview unit=opengl/GLObjectResourceManager tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=opengl/GLObjectResourceManager tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
