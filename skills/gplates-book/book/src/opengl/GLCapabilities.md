# GLCapabilities

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 508 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLCapabilities.h` | C++ | 429 |
| `src/opengl/GLCapabilities.cc` | C++ | 644 |

## Overview

[[[PROSE overview unit=opengl/GLCapabilities tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLCapabilities`](#gplatesopenglglcapabilities) | class | `boost::noncopyable` | — | 0 | Various OpenGL implementation-dependent capabilities and parameters. |

## Members

### `GPlatesOpenGL::GLCapabilities`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Viewport` | struct | `None` | public | Parameters related to viewports. |
| `Framebuffer` | struct | `None` | public | Parameters related to the framebuffers. |
| `Shader` | struct | `None` | public | — |
| `Texture` | struct | `None` | public | Parameters related to textures. |
| `Vertex` | struct | `None` | public | Parameters related to geometry data. |
| `Buffer` | struct | `None` | public | Parameters related to buffer objects. |
| `gl_version_1_2` | field | `bool` | public | Is OpenGL version 1.2 supported ? |
| `gl_version_1_4` | field | `bool` | public | Is OpenGL version 1.4 supported ? |
| `viewport` | field | `Viewport` | public | OpenGL extension queries. |
| `framebuffer` | field | `Framebuffer` | public | — |
| `shader` | field | `Shader` | public | — |
| `texture` | field | `Texture` | public | — |
| `vertex` | field | `Vertex` | public | — |
| `buffer` | field | `Buffer` | public | — |
| `GLCapabilities()` | constructor | `None` | private | — |
| `initialise()` | method | `void` | private | — |
| `initialise_viewport()` | method | `void` | private | — |
| `initialise_framebuffer()` | method | `void` | private | — |
| `initialise_shader()` | method | `void` | private | — |
| `initialise_texture()` | method | `void` | private | — |
| `initialise_vertex()` | method | `void` | private | — |
| `initialise_buffer()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `gl_COLOR_ATTACHMENT0` | variable | `GLenum` | Set the GL\_COLOR\_ATTACHMENT0\_EXT constant. |
| `gl_TEXTURE0` | variable | `GLenum` | Set the GL\_TEXTURE0 constant. |
| `GPLATES_OPENGL_GLCAPABILITIES_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLCapabilities tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLStateSets](GLStateSets.md) | opengl | 252 |
| [opengl/GLScalarField3D](GLScalarField3D.md) | opengl | 87 |
| [opengl/GLState](GLState.md) | opengl | 79 |
| [opengl/GLRenderer](GLRenderer.md) | opengl | 70 |
| [opengl/GLContext](GLContext.md) | opengl | 66 |
| [opengl/GLProgramObject](GLProgramObject.md) | opengl | 64 |
| [opengl/GLStateSetKeys](GLStateSetKeys.md) | opengl | 55 |
| [opengl/GLFrameBufferObject](GLFrameBufferObject.md) | opengl | 49 |
| [opengl/GLBufferObject](GLBufferObject.md) | opengl | 41 |
| [opengl/GLDataRasterSource](GLDataRasterSource.md) | opengl | 35 |
| [opengl/GLNormalMapSource](GLNormalMapSource.md) | opengl | 34 |
| [opengl/GLRenderTargetImpl](GLRenderTargetImpl.md) | opengl | 33 |
| [opengl/GLMultiResolutionCubeRaster](GLMultiResolutionCubeRaster.md) | opengl | 26 |
| [opengl/GLFilledPolygonsGlobeView](GLFilledPolygonsGlobeView.md) | opengl | 21 |
| [opengl/GLRasterCoRegistration](GLRasterCoRegistration.md) | opengl | 21 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 19 |
| [opengl/GLTextureUtils](GLTextureUtils.md) | opengl | 18 |
| [app-logic/ResolvedTriangulationDelaunay2](../app-logic/ResolvedTriangulationDelaunay2.md) | app-logic | 17 |
| [opengl/GLVisualRasterSource](GLVisualRasterSource.md) | opengl | 17 |
| [opengl/GLMultiResolutionCubeReconstructedRaster](GLMultiResolutionCubeReconstructedRaster.md) | opengl | 16 |

*... and 48 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLCapabilities.h
python scripts/gpq.py def GPlatesOpenGL::GLCapabilities --body
python scripts/gpq.py uses GLCapabilities --kind class
python scripts/gpq.py hier GLCapabilities
```
