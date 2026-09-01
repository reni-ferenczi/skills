# GLProjectionUtils

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 3 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLProjectionUtils.h` | C++ | 139 |
| `src/opengl/GLProjectionUtils.cc` | C++ | 284 |

## Overview

[[[PROSE overview unit=opengl/GLProjectionUtils tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `project_window_coords_onto_unit_sphere( const GLViewport &viewport, const GLMatrix &model_view_transform, const GLMatrix &projection_transform, const double &window_x, const double &window_y)` | function | `boost::optional<GPlatesMaths::UnitVector3D>` | Projects a windows coordinate onto the unit sphere in model space using the specified model-view and projection transforms and the specified viewport. |
| `GPLATES_OPENGL_GLPROJECTIONUTILS_H` | macro | `None` | — |
| `glu_project( const GLViewport &viewport, const GLMatrix &model_view_transform, const GLMatrix &projection_transform, double objx, double objy, double objz, GLdouble *winx, GLdouble *winy, GLdouble *winz)` | function | `int` | Convenience function performs same as similarly named OpenGL function. |
| `glu_un_project( const GLViewport &viewport, const GLMatrix &model_view_transform, const GLMatrix &projection_transform, double winx, double winy, double winz, GLdouble *objx, GLdouble *objy, GLdouble *objz)` | function | `int` | Convenience function performs same as similarly named OpenGL function. |
| `get_min_max_pixel_size_on_unit_sphere( const GLViewport &viewport, const GLMatrix &model_view_transform, const GLMatrix &projection_transform)` | function | `std::pair<double/*min*/, double/*max*/>` | Returns an estimate of the minimum and maximum sizes of viewport pixels projected onto the unit sphere using the specified model-view and projection transforms. |
| `get_min_pixel_size_on_unit_sphere( const GLViewport &viewport, const GLMatrix &model_view_transform, const GLMatrix &projection_transform)` | function | `double` | Returns the minimum value of get\_min\_max\_pixel\_size\_on\_unit\_sphere. |
| `get_max_pixel_size_on_unit_sphere( const GLViewport &viewport, const GLMatrix &model_view_transform, const GLMatrix &projection_transform)` | function | `double` | Returns the maximum value of get\_min\_max\_pixel\_size\_on\_unit\_sphere. |

## Notes

[[[PROSE notes unit=opengl/GLProjectionUtils tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLMultiResolutionRasterMapView](GLMultiResolutionRasterMapView.md) | opengl | 5 |
| [gui/VelocityLegendOverlay](../gui/VelocityLegendOverlay.md) | gui | 3 |
| [opengl/GLFilledPolygonsGlobeView](GLFilledPolygonsGlobeView.md) | opengl | 3 |
| [opengl/GLMultiResolutionRaster](GLMultiResolutionRaster.md) | opengl | 3 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 3 |
| [opengl/GLText](GLText.md) | opengl | 3 |
| [opengl/GLMultiResolutionCubeRaster](GLMultiResolutionCubeRaster.md) | opengl | 1 |
| [opengl/GLMultiResolutionCubeReconstructedRaster](GLMultiResolutionCubeReconstructedRaster.md) | opengl | 1 |
| [opengl/GLReconstructedStaticPolygonMeshes](GLReconstructedStaticPolygonMeshes.md) | opengl | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLProjectionUtils.h
```
