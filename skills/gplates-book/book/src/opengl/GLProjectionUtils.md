# GLProjectionUtils

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 3 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLProjectionUtils.h` | C++ | 139 |
| `src/opengl/GLProjectionUtils.cc` | C++ | 284 |

## Overview

A free-function namespace of GLU-style helpers for converting between window
coordinates, model space and the projection frustum, built on top of `GLViewport`
and `GLMatrix`. `glu_project` and `glu_un_project` are thin wrappers around
`gluProject`/`gluUnProject` that take GPlates' own transform and viewport types
instead of raw OpenGL state.

`project_window_coords_onto_unit_sphere` composes `glu_un_project` with a ray-sphere
intersection: it unprojects a window coordinate onto the near clipping plane, then
intersects the ray from the eye through that point with the unit sphere centred at
the origin, returning `boost::none` when the ray misses the globe. `get_min_max_pixel_size_on_unit_sphere`
samples nine points across the view frustum's near face (the four corners, the four
edge midpoints and the centre), projects each pair of adjacent samples onto the unit
sphere and returns the smallest and largest resulting great-circle distances. This
gives callers a cheap way to estimate how finely a raster or mesh needs to be
tessellated to match screen resolution, without projecting every pixel.

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

`get_min_max_pixel_size_on_unit_sphere` is documented as reasonably expensive, but
acceptable because callers invoke it once per raster per render scene rather than
per pixel. Its returned range is `(0, Pi]`, the distance between the north and south
poles on the unit sphere; a caller that needs only one bound should use
`get_min_pixel_size_on_unit_sphere` or `get_max_pixel_size_on_unit_sphere` rather
than discarding half of the pair result itself, since both are computed from a
single call anyway.

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
