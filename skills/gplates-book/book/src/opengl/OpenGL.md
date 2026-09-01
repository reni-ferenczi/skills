# OpenGL

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 3 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/OpenGL.h` | C++ | 95 |

## Overview

[[[PROSE overview unit=opengl/OpenGL tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_OPENGL_H` | macro | `None` | — |
| `__CONVENTION__` | macro | `None` | Assume compilation on Mac OS X. \*/ |
| `GPLATES_OPENGL_BOOL` | macro_function | `((b) != 0)` | — |
| `GPLATES_OPENGL_BUFFER_OFFSET` | macro_function | `(reinterpret_cast<GLubyte *>(0) + (bytes))` | — |

## Notes

[[[PROSE notes unit=opengl/OpenGL tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLCapabilities](GLCapabilities.md) | opengl | 19 |
| [opengl/GLPixelBufferObject](GLPixelBufferObject.md) | opengl | 7 |
| [opengl/GLRenderer](GLRenderer.md) | opengl | 5 |
| [opengl/GLStateSets](GLStateSets.md) | opengl | 3 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 2 |
| [opengl/GLBufferObject](GLBufferObject.md) | opengl | 2 |
| [opengl/GLContext](GLContext.md) | opengl | 2 |
| [opengl/GLCubeSubdivision](GLCubeSubdivision.md) | opengl | 2 |
| [opengl/GLFilledPolygonsGlobeView](GLFilledPolygonsGlobeView.md) | opengl | 2 |
| [opengl/GLFilledPolygonsMapView](GLFilledPolygonsMapView.md) | opengl | 2 |
| [opengl/GLFrameBufferObject](GLFrameBufferObject.md) | opengl | 2 |
| [opengl/GLPixelBufferImpl](GLPixelBufferImpl.md) | opengl | 2 |
| [opengl/GLProgramObject](GLProgramObject.md) | opengl | 2 |
| [opengl/GLProjectionUtils](GLProjectionUtils.md) | opengl | 2 |
| [opengl/GLRenderTargetImpl](GLRenderTargetImpl.md) | opengl | 2 |
| [opengl/GLSaveRestoreFrameBuffer](GLSaveRestoreFrameBuffer.md) | opengl | 2 |
| [opengl/GLScalarField3D](GLScalarField3D.md) | opengl | 2 |
| [opengl/GLShaderObject](GLShaderObject.md) | opengl | 2 |
| [opengl/GLState](GLState.md) | opengl | 2 |
| [opengl/GLStateSetKeys](GLStateSetKeys.md) | opengl | 2 |

*... and 63 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/OpenGL.h
```
