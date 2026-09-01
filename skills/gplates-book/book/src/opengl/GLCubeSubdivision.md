# GLCubeSubdivision

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 801 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLCubeSubdivision.h` | C++ | 442 |
| `src/opengl/GLCubeSubdivision.cc` | C++ | 267 |

## Overview

`GLCubeSubdivision` computes the view/projection transforms, frustums, spherical bounding polygons and oriented bounding boxes for a quad-tree subdivision of a cube face, at any `level_of_detail`/`tile_u_offset`/`tile_v_offset` address. Because the cube is a gnomonic projection of the sphere (great circles project to straight lines), each tile's frustum, when projected onto the sphere, is bounded by exactly four great-circle arcs — which is what `get_bounding_polygon` and `get_oriented_bounding_box` exploit to build cheap spatial bounds for culling and raster look-up.

Every query has a "loose" counterpart (`get_loose_projection_transform`, `get_loose_frustum`, `get_loose_bounding_polygon`, `get_loose_oriented_bounding_box`) that doubles the tile's extent about its own centre rather than the true tile size; see `CubeQuadTreePartition` for why loose bounds are needed. `get_expand_frustum_ratio` and the `expand_frustum_ratio` passed to `create` let a frustum be widened slightly so that a tile's border texel centres land exactly on the frustum planes, which is required to avoid seams when bilinearly-filtered tile textures are stitched together; this expansion is unnecessary for nearest-texel filtering.

The `zNear`/`zFar` passed to `create` are chosen close to the sphere's surface (`zNear` near zero) specifically to keep large, untessellated geometry arcs from being clipped by the near plane, at the cost of depth-buffer precision — acceptable because most cube-based rendering has no real depth complexity.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLCubeSubdivision`](#gplatesopenglglcubesubdivision) | class | [`GPlatesUtils::ReferenceCount<GLCubeSubdivision>`](../utils/ReferenceCount.md) | — | 0 | Defines a quad-tree subdivision of each face of a cube with optional overlapping extents. |

## Members

### `GPlatesOpenGL::GLCubeSubdivision`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLCubeSubdivision>` | public | A convenience typedef for a shared pointer to a non-const GLCubeSubdivision. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLCubeSubdivision>` | public | A convenience typedef for a shared pointer to a const GLCubeSubdivision. |
| `get_expand_frustum_ratio( unsigned int tile_texel_dimension, const double &frustum_border_overlap_in_texels)` | method | `double` | public | Calculates a frustum expand ratio (for use in create) for a tile of the specified texel dimension and the desired overlap in units of texels. |
| `create( const double &expand_frustum_ratio = 1.0, GLdouble zNear = 1e-3, GLdouble zFar = 2.0)` | method | `non_null_ptr_type` | public | Since a texel has a centre sample point but is also a square area this means that the tile textures overlap slightly (by one texel). |
| `get_view_transform( GPlatesMaths::CubeCoordinateFrame::CubeFaceType cube_face)` | method | `GLTransform::non_null_ptr_to_const_type` | public | Returns the view matrix used to render a scene into a subdivision tile. must be in the range \[0, 2^level\_of\_detail). must be in the range \[0, 2^level\_of\_detail). |
| `get_projection_transform( unsigned int level_of_detail, unsigned int tile_u_offset, unsigned int tile_v_offset)` | method | `GLTransform::non_null_ptr_to_const_type` | public | Returns the projection matrix used to render a scene into a subdivision tile. must be in the range \[0, 2^level\_of\_detail). must be in the range \[0, 2^level\_of\_detail). |
| `get_loose_projection_transform( unsigned int level_of_detail, unsigned int tile_u_offset, unsigned int tile_v_offset)` | method | `GLTransform::non_null_ptr_to_const_type` | public | Returns the loose projection matrix used to render a scene into a subdivision tile, but with the tile doubled in size (about the tile centre) on the plane of the cube face. |
| `get_frustum( GPlatesMaths::CubeCoordinateFrame::CubeFaceType cube_face, unsigned int level_of_detail, unsigned int tile_u_offset, unsigned int tile_v_offset)` | method | `GLFrustum` | public | Returns the six-plane frustum from the view-projection transform obtained from get\_view\_transform and get\_projection\_transform. |
| `get_loose_frustum( GPlatesMaths::CubeCoordinateFrame::CubeFaceType cube_face, unsigned int level_of_detail, unsigned int tile_u_offset, unsigned int tile_v_offset)` | method | `GLFrustum` | public | Returns the six-plane loose frustum from the view-projection transform obtained from get\_view\_transform and get\_loose\_projection\_transform. |
| `get_bounding_polygon( GPlatesMaths::CubeCoordinateFrame::CubeFaceType cube_face, unsigned int level_of_detail, unsigned int tile_u_offset, unsigned int tile_v_offset)` | method | `GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type` | public | Returns the polygon (on sphere) containing four great circle arcs that bound the specified subdivision tile. |
| `get_loose_bounding_polygon( GPlatesMaths::CubeCoordinateFrame::CubeFaceType cube_face, unsigned int level_of_detail, unsigned int tile_u_offset, unsigned int tile_v_offset)` | method | `GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type` | public | Returns the polygon (on sphere) containing four great circle arcs that form the 'loose' bounds the specified subdivision tile. |
| `get_oriented_bounding_box( GPlatesMaths::CubeCoordinateFrame::CubeFaceType cube_face, unsigned int level_of_detail, unsigned int tile_u_offset, unsigned int tile_v_offset)` | method | `GLIntersect::OrientedBoundingBox` | public | Returns the oriented bounding box (OBB) containing four great circle arcs that bound the specified subdivision tile and the area inside them on the surface of the globe. |
| `get_loose_oriented_bounding_box( GPlatesMaths::CubeCoordinateFrame::CubeFaceType cube_face, unsigned int level_of_detail, unsigned int tile_u_offset, unsigned int tile_v_offset)` | method | `GLIntersect::OrientedBoundingBox` | public | Returns the loose oriented bounding box (OBB) formed from the specified tile, but with the tile doubled in size (about the tile centre) on the plane of the cube face. |
| `FrustumCornerPoints` | struct | `None` | private | Calculates and contains the four (unnormalised) corner points of a frustum. |
| `d_expand_frustum_ratio` | field | `double` | private | Factor by which to expand the frustum around the tile border. |
| `d_expanded_projection_scale` | field | `double` | private | Scale factor used when/if expanding a projection transform around a frustum border. |
| `d_near` | field | `GLdouble` | private | Frustum near plane distance. |
| `d_far` | field | `GLdouble` | private | Frustum far plane distance. |
| `GLCubeSubdivision( const double &expand_frustum_ratio, GLdouble zNear, GLdouble zFar)` | constructor | `None` | private | Constructor. |
| `create_projection_transform( unsigned int level_of_detail, unsigned int tile_u_offset, unsigned int tile_v_offset, const double &expanded_projection_scale)` | method | `GLTransform::non_null_ptr_to_const_type` | private | — |
| `create_bounding_polygon( const FrustumCornerPoints &frustum_corner_points)` | method | `GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type` | private | — |
| `create_oriented_bounding_box( const FrustumCornerPoints &frustum_corner_points)` | method | `GLIntersect::OrientedBoundingBox` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLCUBESUBDIVISION_H` | macro | `None` | — |

## Notes

- `zNear` cannot be zero (a zero-distance frustum has no valid projection matrix) and is deliberately kept small but not vanishingly so, to balance near-plane clipping avoidance against numerical precision in the projection matrix.
- `tile_u_offset` and `tile_v_offset` must lie in `[0, 2^level_of_detail)`; this is documented but not asserted in the header.
- Loose-tile methods double `expand_frustum_ratio` (`2 * d_expand_frustum_ratio`) rather than recomputing it, relying on the fact that the same ratio works for both loose and non-loose tiles when loose texels are twice the size of non-loose ones.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLScalarField3DGenerator](GLScalarField3DGenerator.md) | opengl | 11 |
| [opengl/GLRasterCoRegistration](GLRasterCoRegistration.md) | opengl | 10 |
| [opengl/GLMultiResolutionCubeReconstructedRaster](GLMultiResolutionCubeReconstructedRaster.md) | opengl | 9 |
| [opengl/GLScalarField3D](GLScalarField3D.md) | opengl | 7 |
| [opengl/GLCubeSubdivisionCache](GLCubeSubdivisionCache.md) | opengl | 4 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 3 |
| [opengl/GLFilledPolygonsGlobeView](GLFilledPolygonsGlobeView.md) | opengl | 1 |
| [opengl/GLMultiResolutionCubeRaster](GLMultiResolutionCubeRaster.md) | opengl | 1 |
| [opengl/GLMultiResolutionRasterMapView](GLMultiResolutionRasterMapView.md) | opengl | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLCubeSubdivision.h
python scripts/gpq.py def GPlatesOpenGL::GLCubeSubdivision --body
python scripts/gpq.py uses GLCubeSubdivision --kind class
python scripts/gpq.py hier GLCubeSubdivision
```
