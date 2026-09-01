# GLMatrix

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 1508 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLMatrix.h` | C++ | 303 |
| `src/opengl/GLMatrix.cc` | C++ | 477 |

## Overview

[[[PROSE overview unit=opengl/GLMatrix tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLMatrix`](#gplatesopenglglmatrix) | class | `boost::equality_comparable<GLMatrix>` | — | 0 | A 4x4 matrix in OpenGL column-major format. |

## Members

### `GPlatesOpenGL::GLMatrix`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `IDENTITY` | field | `GLMatrix` | public | The identity matrix. |
| `GLMatrix()` | constructor | `None` | public | Constructor - creates identity matrix. |
| `GLMatrix( const GLdouble *matrix)` | constructor | `None` | public | Constructs an arbitrary 4x4 matrix. |
| `GLMatrix( const GPlatesMaths::UnitQuaternion3D &quaternion)` | constructor | `None` | public | Constructs 4x4 matrix from specified unit quaternion (note only the 3x3 rotation part of the matrix is initialised - the rest is set to zero). |
| `gl_load_identity` | field | `GLMatrix` | public | Performs function of similarly named OpenGL function. |
| `gl_load_matrix` | field | `GLMatrix` | public | Loads an arbitrary 4x4 matrix. |
| `gl_mult_matrix` | field | `GLMatrix` | public | Post-multiplies matrix matrix with the current internal matrix. |
| `gl_translate` | field | `GLMatrix` | public | Performs function of similarly named OpenGL function (including post-multiplication). |
| `gl_rotate` | field | `GLMatrix` | public | Performs function of similarly named OpenGL function (including post-multiplication). |
| `gl_scale` | field | `GLMatrix` | public | Performs function of similarly named OpenGL function (including post-multiplication). |
| `gl_ortho` | field | `GLMatrix` | public | Performs function of similarly named OpenGL function (including post-multiplication). |
| `gl_frustum` | field | `GLMatrix` | public | Performs function of similarly named OpenGL function (including post-multiplication). |
| `glu_look_at` | field | `GLMatrix` | public | Performs function of similarly named OpenGL function (including post-multiplication). |
| `glu_perspective` | field | `GLMatrix` | public | Performs function of similarly named OpenGL function (including post-multiplication). |
| `get_matrix()` | method | `GLdouble` | public | Returns internal matrix in OpenGL column-major format. |
| `matrix_type` | typedef | `GLdouble` | private | Typedef for a contiguous array of 16 doubles (in 4x4 format). |
| `d_matrix` | field | `matrix_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `IDENTITY` | variable | `GPlatesOpenGL::GLMatrix` | — |
| `GPLATES_OPENGL_GLMATRIX_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLMatrix tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/GlobeCanvas](../qt-widgets/GlobeCanvas.md) | qt-widgets | 55 |
| [qt-widgets/MapCanvas](../qt-widgets/MapCanvas.md) | qt-widgets | 37 |
| [gui/Globe](../gui/Globe.md) | gui | 34 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 30 |
| [opengl/GLRenderer](GLRenderer.md) | opengl | 30 |
| [opengl/GLUtils](GLUtils.md) | opengl | 30 |
| [opengl/GLStateSets](GLStateSets.md) | opengl | 29 |
| [opengl/GLProjectionUtils](GLProjectionUtils.md) | opengl | 23 |
| [opengl/GLFilledPolygonsGlobeView](GLFilledPolygonsGlobeView.md) | opengl | 21 |
| [opengl/GLLight](GLLight.md) | opengl | 15 |
| [opengl/GLMultiResolutionCubeRaster](GLMultiResolutionCubeRaster.md) | opengl | 14 |
| [opengl/GLProgramObject](GLProgramObject.md) | opengl | 14 |
| [gui/SceneLightingParameters](../gui/SceneLightingParameters.md) | gui | 13 |
| [gui/LayerPainter](../gui/LayerPainter.md) | gui | 12 |
| [opengl/GLScalarField3DGenerator](GLScalarField3DGenerator.md) | opengl | 12 |
| [opengl/GLMultiResolutionRasterMapView](GLMultiResolutionRasterMapView.md) | opengl | 11 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 10 |
| [gui/OpaqueSphere](../gui/OpaqueSphere.md) | gui | 10 |
| [opengl/GLRasterCoRegistration](GLRasterCoRegistration.md) | opengl | 10 |
| [opengl/GLCubeSubdivision](GLCubeSubdivision.md) | opengl | 8 |

*... and 22 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLMatrix.h
python scripts/gpq.py def GPlatesOpenGL::GLMatrix --body
python scripts/gpq.py uses GLMatrix --kind class
python scripts/gpq.py hier GLMatrix
```
