# GLFrustum

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 1387 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLFrustum.h` | C++ | 154 |
| `src/opengl/GLFrustum.cc` | C++ | 225 |

## Overview

[[[PROSE overview unit=opengl/GLFrustum tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLFrustum`](#gplatesopenglglfrustum) | class | — | — | 0 | An array of the six frustum planes that bound a viewing volume. |

## Members

### `GPlatesOpenGL::GLFrustum`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PlaneType` | enum | `None` | public | The specific frustum planes. |
| `ALL_PLANES_ACTIVE_MASK` | field | `boost::uint32_t` | public | Bitmask to indicate all frustum planes are active. |
| `GLFrustum()` | constructor | `None` | public | Default constructor initialises planes using identity model-view and projection matrices. |
| `GLFrustum( const GLMatrix &model_view_matrix, const GLMatrix &projection_matrix)` | constructor | `None` | public | Initialises planes using the specified model-view and projection matrices. |
| `set_identity_model_view_projection()` | method | `void` | public | Initialises planes using the identity model-view and projection matrices. |
| `set_model_view_projection( const GLMatrix &model_view_matrix, const GLMatrix &projection_matrix)` | method | `void` | public | Initialises planes using the specified model-view and projection matrices. |
| `get_planes()` | method | `GLIntersect::Plane` | public | Returns the frustum planes. |
| `IDENTITY_FRUSTUM_PLANES` | field | `GLIntersect::Plane` | private | The frustum planes for the identify model-view-projection. |
| `d_planes` | field | `std::vector<GLIntersect::Plane>` | private | The left, right, bottom, top, near and far frustum planes. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_left_plane( const GLMatrix &mvp)` | function | `GLIntersect::Plane` | Returns the left clip plane - mvp is model-view-projection matrix. |
| `get_right_plane( const GLMatrix &mvp)` | function | `GLIntersect::Plane` | Returns the right clip plane - mvp is model-view-projection matrix. |
| `get_bottom_plane( const GLMatrix &mvp)` | function | `GLIntersect::Plane` | Returns the bottom clip plane - mvp is model-view-projection matrix. |
| `get_top_plane( const GLMatrix &mvp)` | function | `GLIntersect::Plane` | Returns the top clip plane - mvp is model-view-projection matrix. |
| `get_near_plane( const GLMatrix &mvp)` | function | `GLIntersect::Plane` | Returns the near clip plane - mvp is model-view-projection matrix. |
| `get_far_plane( const GLMatrix &mvp)` | function | `GLIntersect::Plane` | Returns the far clip plane - mvp is model-view-projection matrix. |
| `IDENTITY_FRUSTUM_PLANES` | variable | `GPlatesOpenGL::GLIntersect::Plane` | NOTE: These should be in the same order as specified by the 'PlaneType' enum. |
| `GPLATES_OPENGL_GLFRUSTUM_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLFrustum tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 16 |
| [qt-widgets/GlobeCanvas](../qt-widgets/GlobeCanvas.md) | qt-widgets | 16 |
| [opengl/GLMultiResolutionRasterMapView](GLMultiResolutionRasterMapView.md) | opengl | 14 |
| [opengl/GLMultiResolutionRaster](GLMultiResolutionRaster.md) | opengl | 12 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 10 |
| [opengl/GLCubeSubdivision](GLCubeSubdivision.md) | opengl | 7 |
| [opengl/GLCubeSubdivisionCache](GLCubeSubdivisionCache.md) | opengl | 6 |
| [opengl/GLReconstructedStaticPolygonMeshes](GLReconstructedStaticPolygonMeshes.md) | opengl | 6 |
| [opengl/GLFilledPolygonsGlobeView](GLFilledPolygonsGlobeView.md) | opengl | 5 |
| [qt-widgets/MapCanvas](../qt-widgets/MapCanvas.md) | qt-widgets | 4 |
| [opengl/GLMultiResolutionCubeRaster](GLMultiResolutionCubeRaster.md) | opengl | 3 |
| [opengl/GLMultiResolutionCubeReconstructedRaster](GLMultiResolutionCubeReconstructedRaster.md) | opengl | 3 |
| [opengl/GLScalarField3DGenerator](GLScalarField3DGenerator.md) | opengl | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLFrustum.h
python scripts/gpq.py def GPlatesOpenGL::GLFrustum --body
python scripts/gpq.py uses GLFrustum --kind class
python scripts/gpq.py hier GLFrustum
```
