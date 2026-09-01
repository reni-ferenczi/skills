# GLObject

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 531 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLObject.h` | C++ | 68 |

## Overview

`GLObject` is the common, non-copyable root for every wrapped OpenGL resource type — texture, buffer, framebuffer, shader and program objects, and the rest of the `GL*Object` family. It contributes nothing but a virtual destructor and the pointer typedefs those subclasses share.

It exposes `boost::shared_ptr`/`weak_ptr` typedefs rather than the `non_null_intrusive_ptr` used elsewhere in `opengl`, specifically so that instances can be managed by `GPlatesUtils::ObjectCache`, which needs ordinary shared/weak pointer semantics (including the ability to have no live owner) to recycle GL resources.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLObject`](#gplatesopenglglobject) | class | `boost::noncopyable` | — | 10 | Base class for any OpenGL object such as texture object, texture buffer object, vertex buffer object, pixel buffer object, framebuffer object, etc. |

## Members

### `GPlatesOpenGL::GLObject`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_type` | typedef | `boost::shared_ptr<GLObject>` | public | A convenience typedef for a shared pointer to a GLObject. |
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const GLObject>` | public | — |
| `weak_ptr_type` | typedef | `boost::weak_ptr<GLObject>` | public | A convenience typedef for a weak pointer to a GLObject. |
| `weak_ptr_to_const_type` | typedef | `boost::weak_ptr<const GLObject>` | public | — |
| `~GLObject()` | destructor | `None` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLOBJECT_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLAgeGridMaskSource](GLAgeGridMaskSource.md) | opengl | 16 |
| [opengl/GLShaderProgramUtils](GLShaderProgramUtils.md) | opengl | 15 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 10 |
| [opengl/GLMultiResolutionCubeRaster](GLMultiResolutionCubeRaster.md) | opengl | 9 |
| [opengl/GLNormalMapSource](GLNormalMapSource.md) | opengl | 7 |
| [opengl/GLMultiResolutionCubeReconstructedRaster](GLMultiResolutionCubeReconstructedRaster.md) | opengl | 5 |
| [opengl/GLMultiResolutionMapCubeMesh](GLMultiResolutionMapCubeMesh.md) | opengl | 5 |
| [opengl/GLLight](GLLight.md) | opengl | 4 |
| [opengl/GLMultiResolutionCubeMesh](GLMultiResolutionCubeMesh.md) | opengl | 4 |
| [opengl/GLMultiResolutionRasterMapView](GLMultiResolutionRasterMapView.md) | opengl | 3 |
| [opengl/GLScalarFieldDepthLayersSource](GLScalarFieldDepthLayersSource.md) | opengl | 3 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 2 |
| [opengl/GLBufferObject](GLBufferObject.md) | opengl | 2 |
| [opengl/GLFrameBufferObject](GLFrameBufferObject.md) | opengl | 2 |
| [opengl/GLMultiResolutionCubeRasterInterface](GLMultiResolutionCubeRasterInterface.md) | opengl | 2 |
| [opengl/GLPixelBufferObject](GLPixelBufferObject.md) | opengl | 2 |
| [opengl/GLProgramObject](GLProgramObject.md) | opengl | 2 |
| [opengl/GLRenderBufferObject](GLRenderBufferObject.md) | opengl | 2 |
| [opengl/GLShaderObject](GLShaderObject.md) | opengl | 2 |
| [opengl/GLTexture](GLTexture.md) | opengl | 2 |

*... and 4 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLObject.h
python scripts/gpq.py def GPlatesOpenGL::GLObject --body
python scripts/gpq.py uses GLObject --kind class
python scripts/gpq.py hier GLObject
```
