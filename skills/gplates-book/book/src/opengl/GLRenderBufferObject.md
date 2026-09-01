# GLRenderBufferObject

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 595 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLRenderBufferObject.h` | C++ | 193 |
| `src/opengl/GLRenderBufferObject.cc` | C++ | 108 |

## Overview

[[[PROSE overview unit=opengl/GLRenderBufferObject tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLRenderBufferObject`](#gplatesopenglglrenderbufferobject) | class | [`GLObject`](GLObject.md)<br>`boost::enable_shared_from_this<GLRenderBufferObject>` | — | 0 | A render buffer object to be used with GLFrameBufferObject. |

## Members

### `GPlatesOpenGL::GLRenderBufferObject`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_type` | typedef | `boost::shared_ptr<GLRenderBufferObject>` | public | A convenience typedef for a shared pointer to a GLRenderBufferObject. |
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const GLRenderBufferObject>` | public | — |
| `weak_ptr_type` | typedef | `boost::weak_ptr<GLRenderBufferObject>` | public | A convenience typedef for a weak pointer to a GLRenderBufferObject. |
| `weak_ptr_to_const_type` | typedef | `boost::weak_ptr<const GLRenderBufferObject>` | public | — |
| `resource_handle_type` | typedef | `GLuint` | public | Typedef for a resource handle. |
| `Allocator` | class | `None` | public | Policy class to allocate and deallocate OpenGL render buffer objects. |
| `resource_type` | typedef | `GLObjectResource<resource_handle_type, Allocator>` | public | Typedef for a resource. |
| `resource_manager_type` | typedef | `GLObjectResourceManager<resource_handle_type, Allocator>` | public | Typedef for a resource manager. |
| `create( GLRenderer &renderer)` | method | `shared_ptr_type` | public | Creates a shared pointer to a GLRenderBufferObject object. |
| `create_as_unique_ptr( GLRenderer &renderer)` | method | `std::unique_ptr<GLRenderBufferObject>` | public | Same as create but returns a std::unique\_ptr - to guarantee only one owner. |
| `gl_render_buffer_storage( GLRenderer &renderer, GLint internalformat, GLsizei width, GLsizei height)` | method | `void` | public | Performs same function as the glRenderBufferStorage OpenGL function. |
| `get_internal_format()` | method | `boost::optional<GLint>` | public | Returns the internal format of the texture. |
| `get_render_buffer_resource_handle()` | method | `resource_handle_type` | public | Returns the render buffer resource handle. |
| `d_resource` | field | `resource_type::non_null_ptr_to_const_type` | private | — |
| `d_dimensions` | field | `boost::optional< std::pair<GLuint/*width*/, GLuint/*height*/> >` | private | — |
| `d_internal_format` | field | `boost::optional<GLint>` | private | — |
| `GLRenderBufferObject( GLRenderer &renderer)` | constructor | `None` | private | Constructor. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLRENDERBUFFEROBJECT_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLRenderBufferObject tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLContext](GLContext.md) | opengl | 14 |
| [opengl/GLRenderTargetImpl](GLRenderTargetImpl.md) | opengl | 10 |
| [opengl/GLTexture](GLTexture.md) | opengl | 8 |
| [opengl/GLFrameBufferObject](GLFrameBufferObject.md) | opengl | 7 |
| [opengl/GLRendererImpl](GLRendererImpl.md) | opengl | 5 |
| [opengl/GLScalarField3D](GLScalarField3D.md) | opengl | 3 |
| [opengl/GLLight](GLLight.md) | opengl | 2 |
| [opengl/GLMultiResolutionCubeRaster](GLMultiResolutionCubeRaster.md) | opengl | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLRenderBufferObject.h
python scripts/gpq.py def GPlatesOpenGL::GLRenderBufferObject --body
python scripts/gpq.py uses GLRenderBufferObject --kind class
python scripts/gpq.py hier GLRenderBufferObject
```
