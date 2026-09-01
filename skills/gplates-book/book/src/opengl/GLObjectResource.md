# GLObjectResource

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 1352 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLObjectResource.h` | C++ | 118 |

## Overview

[[[PROSE overview unit=opengl/GLObjectResource tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLObjectResource`](#gplatesopenglglobjectresource) | class | [`GPlatesUtils::ReferenceCount<GLObjectResource<ResourceHandleType,ResourceAllocatorType> >`](../utils/ReferenceCount.md) | `<typename ResourceHandleType, class ResourceAllocatorType>` | 0 | An RAII wrapper around an OpenGL object resource (such as a texture object) that schedules the resource to be deallocated when its destructor is called. |

## Members

### `GPlatesOpenGL::GLObjectResource`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `this_type` | typedef | `GLObjectResource<ResourceHandleType,ResourceAllocatorType>` | public | Typedef for this class type. |
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<this_type>` | public | A convenience typedef for a shared pointer to a non-const GLObjectResource. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const this_type>` | public | A convenience typedef for a shared pointer to a const GLObjectResource. |
| `resource_manager_type` | typedef | `GLObjectResourceManager<ResourceHandleType, ResourceAllocatorType>` | public | Typedef for the manager of this resource type. |
| `create( const GLCapabilities &capabilities, const typename resource_manager_type::shared_ptr_type &resource_manager)` | method | `non_null_ptr_type` | public | Creates a GLObjectResource from a resource manager. |
| `~GLObjectResource()` | destructor | `None` | public | — |
| `get_resource_handle()` | method | `ResourceHandleType` | public | Returns the resource handle held internally. |
| `d_resource_handle` | field | `ResourceHandleType` | private | — |
| `d_resource_manager` | field | `boost::weak_ptr<resource_manager_type>` | private | — |
| `GLObjectResource( ResourceHandleType resource_handle, const boost::weak_ptr<resource_manager_type> &resource_manager)` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLOBJECTRESOURCE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLObjectResource tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLState](GLState.md) | opengl | 8 |
| [opengl/GLStateStore](GLStateStore.md) | opengl | 8 |
| [opengl/GLStateSets](GLStateSets.md) | opengl | 7 |
| [opengl/GLBufferObject](GLBufferObject.md) | opengl | 5 |
| [opengl/GLProgramObject](GLProgramObject.md) | opengl | 5 |
| [opengl/GLRenderBufferObject](GLRenderBufferObject.md) | opengl | 5 |
| [opengl/GLShaderObject](GLShaderObject.md) | opengl | 5 |
| [opengl/GLTexture](GLTexture.md) | opengl | 5 |
| [opengl/GLFrameBufferObject](GLFrameBufferObject.md) | opengl | 4 |
| [opengl/GLVertexArrayObject](GLVertexArrayObject.md) | opengl | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLObjectResource.h
python scripts/gpq.py def GPlatesOpenGL::GLObjectResource --body
python scripts/gpq.py uses GLObjectResource --kind class
python scripts/gpq.py hier GLObjectResource
```
