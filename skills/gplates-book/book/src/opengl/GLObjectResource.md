# GLObjectResource

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 1352 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLObjectResource.h` | C++ | 118 |

## Overview

`GLObjectResource` is an RAII wrapper, templated on a raw OpenGL handle type and an allocator policy, that ties a single OpenGL object handle (a texture name, buffer name, etc.) to the resource manager (`GLObjectResourceManager`) that allocated it. `create` asks the manager to allocate a handle; the destructor asks the same manager, reached through a `boost::weak_ptr`, to queue that handle for deallocation.

Deallocation is deferred to a queue rather than performed immediately because releasing an OpenGL object requires a current OpenGL context, and a `GLObjectResource`'s destructor can run at a point where the right context is not current. The weak pointer to the manager also lets this class distinguish "manager is still alive, please recycle this handle" from "the whole OpenGL context (and every resource in it) has already been destroyed, so there is nothing to release" — the latter is a silent no-op in the destructor.

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

- The destructor deliberately does nothing if the resource manager has already been destroyed (weak pointer expired): that only happens when the owning OpenGL context itself was torn down, which already frees every resource in it, so re-releasing the handle would be meaningless or unsafe.

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
