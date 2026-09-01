# GLIntersect

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 3 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLIntersect.h` | C++ | 137 |
| `src/opengl/GLIntersect.cc` | C++ | 206 |

## Overview

[[[PROSE overview unit=opengl/GLIntersect tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLINTERSECT_H` | macro | `None` | — |
| `intersect_ray_sphere( const Ray &ray, const Sphere &sphere)` | function | `boost::optional<GPlatesMaths::real_t>` | Intersects a ray with a sphere and returns the closest distance from the ray's origin to the sphere's surface or false it doesn't intersect. |
| `intersect_sphere_frustum( const Sphere &sphere, const Plane frustum_planes[], boost::uint32_t frustum_plane_mask)` | function | `boost::optional<boost::uint32_t>` | Intersects a Sphere with the planes of a frustum. |
| `intersect_OBB_frustum( const OrientedBoundingBox &obb, const Plane frustum_planes[], boost::uint32_t frustum_plane_mask)` | function | `boost::optional<boost::uint32_t>` | Intersects an OrientedBoundingBox with the planes of a frustum. |

## Notes

[[[PROSE notes unit=opengl/GLIntersect tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 15 |
| [opengl/GLMultiResolutionRaster](GLMultiResolutionRaster.md) | opengl | 12 |
| [opengl/GLProjectionUtils](GLProjectionUtils.md) | opengl | 6 |
| [opengl/GLReconstructedStaticPolygonMeshes](GLReconstructedStaticPolygonMeshes.md) | opengl | 6 |
| [opengl/GLFilledPolygonsGlobeView](GLFilledPolygonsGlobeView.md) | opengl | 4 |
| [opengl/GLMultiResolutionRasterMapView](GLMultiResolutionRasterMapView.md) | opengl | 4 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLIntersect.h
```
