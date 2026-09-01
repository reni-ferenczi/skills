# GLIntersect

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 3 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLIntersect.h` | C++ | 137 |
| `src/opengl/GLIntersect.cc` | C++ | 206 |

## Overview

`GLIntersect` is a free-function namespace of intersection routines used for two purposes: view-frustum culling, and screen-space-to-world-space pixel/texel projection for level-of-detail selection. `intersect_ray_sphere` supports the latter; `intersect_sphere_frustum` and `intersect_OBB_frustum` support the former, testing a `Sphere` or `OrientedBoundingBox` against an array of `Plane`s that bound a (possibly open, but convex) frustum region.

Both frustum tests share a hierarchical-culling optimisation: `frustum_plane_mask` marks which planes are still active, and on a possible intersection the function returns a narrower mask that drops any plane the whole bounding volume was found entirely inside. Callers pass that narrowed mask down when testing children of a bounding-volume hierarchy, so a node need only be tested against the parent's still-relevant planes rather than the whole frustum every time.

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

- The frustum planes must define a convex region (their positive half-spaces intersected); a concave arrangement gives undefined results.
- `frustum_plane_mask` supports at most 31 planes; passing 32 or more throws `PreconditionViolationError`. A zero mask means "no planes active" and both functions return true unconditionally in that case.
- Plane normals must point toward the inside of the frustum, matching the convention used by `GLFrustum`.

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
