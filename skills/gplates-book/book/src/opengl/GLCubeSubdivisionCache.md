# GLCubeSubdivisionCache

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 716 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLCubeSubdivisionCache.h` | C++ | 652 |

## Overview

`GLCubeSubdivisionCache` memoises the per-tile queries of a `GLCubeSubdivision` (projection transforms, frustums, bounding polygons, oriented bounding boxes) against nodes of a `GPlatesMaths::CubeQuadTree`, so that repeated visits to the same quad-tree tile — e.g. while traversing a raster pyramid and its reconstructed polygon mesh in lockstep — don't recompute the same view/projection maths each time. `get_quad_tree_root_node` and `get_child_node` lazily create quad-tree nodes as they are visited, returning a `NodeReference` that carries the node's cube face, level of detail and tile offsets; each `get_*` accessor looks up (or lazily computes and caches) the corresponding value on that node.

Which queries are actually cached is controlled entirely by eight boolean template parameters (`CacheProjectionTransform`, `CacheLooseProjectionTransform`, `CacheFrustum`, `CacheLooseFrustum`, `CacheBoundingPolygon`, `CacheLooseBoundingPolygon`, `CacheBounds`, `CacheLooseBounds`), each selecting between an empty `Implementation::No*` policy struct and one holding a `boost::optional` result, mixed together via `boost::mpl::if_c` into a single `Element` type. This means a caller enables only the caches it actually needs, and the corresponding `get_*` method on `GLCubeSubdivisionCache` will fail to compile if its cache flag was left `false` — there is no runtime fallback for an uncached query. The view transform is the one exception: since it depends only on the cube face, it is stored unconditionally as one of six precomputed transforms rather than through the cache.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::Implementation::NoProjectionTransform`](#gplatesopenglimplementationnoprojectiontransform) | struct | — | — | 0 | — |
| [`GPlatesOpenGL::Implementation::ProjectionTransform`](#gplatesopenglimplementationprojectiontransform) | struct | — | — | 0 | — |
| [`GPlatesOpenGL::Implementation::NoLooseProjectionTransform`](#gplatesopenglimplementationnolooseprojectiontransform) | struct | — | — | 0 | — |
| [`GPlatesOpenGL::Implementation::LooseProjectionTransform`](#gplatesopenglimplementationlooseprojectiontransform) | struct | — | — | 0 | — |
| [`GPlatesOpenGL::Implementation::NoFrustum`](#gplatesopenglimplementationnofrustum) | struct | — | — | 0 | — |
| [`GPlatesOpenGL::Implementation::Frustum`](#gplatesopenglimplementationfrustum) | struct | — | — | 0 | — |
| [`GPlatesOpenGL::Implementation::NoLooseFrustum`](#gplatesopenglimplementationnoloosefrustum) | struct | — | — | 0 | — |
| [`GPlatesOpenGL::Implementation::LooseFrustum`](#gplatesopenglimplementationloosefrustum) | struct | — | — | 0 | — |
| [`GPlatesOpenGL::Implementation::NoBoundingPolygon`](#gplatesopenglimplementationnoboundingpolygon) | struct | — | — | 0 | — |
| [`GPlatesOpenGL::Implementation::BoundingPolygon`](#gplatesopenglimplementationboundingpolygon) | struct | — | — | 0 | — |
| [`GPlatesOpenGL::Implementation::NoLooseBoundingPolygon`](#gplatesopenglimplementationnolooseboundingpolygon) | struct | — | — | 0 | — |
| [`GPlatesOpenGL::Implementation::LooseBoundingPolygon`](#gplatesopenglimplementationlooseboundingpolygon) | struct | — | — | 0 | — |
| [`GPlatesOpenGL::Implementation::NoOrientedBoundingBox`](#gplatesopenglimplementationnoorientedboundingbox) | struct | — | — | 0 | — |
| [`GPlatesOpenGL::Implementation::OrientedBoundingBox`](#gplatesopenglimplementationorientedboundingbox) | struct | — | — | 0 | — |
| [`GPlatesOpenGL::Implementation::NoLooseOrientedBoundingBox`](#gplatesopenglimplementationnolooseorientedboundingbox) | struct | — | — | 0 | — |
| [`GPlatesOpenGL::Implementation::LooseOrientedBoundingBox`](#gplatesopenglimplementationlooseorientedboundingbox) | struct | — | — | 0 | — |
| [`GPlatesOpenGL::GLCubeSubdivisionCache`](#gplatesopenglglcubesubdivisioncache) | class | [`GPlatesUtils::ReferenceCount< GLCubeSubdivisionCache< CacheProjectionTransform, CacheLooseProjectionTransform, CacheFrustum, CacheLooseFrustum, CacheBoundingPolygon, CacheLooseBoundingPolygon, CacheBounds, CacheLooseBounds> >`](../utils/ReferenceCount.md) | `< bool CacheProjectionTransform = false, bool CacheLooseProjectionTransform = false, bool CacheFrustum = false, bool CacheLooseFrustum = false, bool CacheBoundingPolygon = false, bool CacheLooseBoundingPolygon = false, bool CacheBounds = false, bool CacheLooseBounds = false>` | 0 | — |

## Members

### `GPlatesOpenGL::Implementation::NoProjectionTransform`

*None.*

### `GPlatesOpenGL::Implementation::ProjectionTransform`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `projection_transform` | field | `boost::optional<GLTransform::non_null_ptr_to_const_type>` | public | — |

### `GPlatesOpenGL::Implementation::NoLooseProjectionTransform`

*None.*

### `GPlatesOpenGL::Implementation::LooseProjectionTransform`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `loose_projection_transform` | field | `boost::optional<GLTransform::non_null_ptr_to_const_type>` | public | — |

### `GPlatesOpenGL::Implementation::NoFrustum`

*None.*

### `GPlatesOpenGL::Implementation::Frustum`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `frustum` | field | `boost::optional<GLFrustum>` | public | — |

### `GPlatesOpenGL::Implementation::NoLooseFrustum`

*None.*

### `GPlatesOpenGL::Implementation::LooseFrustum`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `loose_frustum` | field | `boost::optional<GLFrustum>` | public | — |

### `GPlatesOpenGL::Implementation::NoBoundingPolygon`

*None.*

### `GPlatesOpenGL::Implementation::BoundingPolygon`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `bounding_polygon` | field | `boost::optional<GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type>` | public | — |

### `GPlatesOpenGL::Implementation::NoLooseBoundingPolygon`

*None.*

### `GPlatesOpenGL::Implementation::LooseBoundingPolygon`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `loose_bounding_polygon` | field | `boost::optional<GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type>` | public | — |

### `GPlatesOpenGL::Implementation::NoOrientedBoundingBox`

*None.*

### `GPlatesOpenGL::Implementation::OrientedBoundingBox`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `oriented_bounding_box` | field | `boost::optional<GLIntersect::OrientedBoundingBox>` | public | — |

### `GPlatesOpenGL::Implementation::NoLooseOrientedBoundingBox`

*None.*

### `GPlatesOpenGL::Implementation::LooseOrientedBoundingBox`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `loose_oriented_bounding_box` | field | `boost::optional<GLIntersect::OrientedBoundingBox>` | public | — |

### `GPlatesOpenGL::GLCubeSubdivisionCache`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `subdivision_cache_type` | typedef | `GLCubeSubdivisionCache< CacheProjectionTransform, CacheLooseProjectionTransform, CacheFrustum, CacheLooseFrustum, CacheBoundingPolygon, CacheLooseBoundingPolygon, CacheBounds, Cach ...` | public | Typedef for this class type. |
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<subdivision_cache_type>` | public | A convenience typedef for a shared pointer to a non-const GLCubeSubdivisionCache. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const subdivision_cache_type>` | public | A convenience typedef for a shared pointer to a const GLCubeSubdivisionCache. |
| `create( const GLCubeSubdivision::non_null_ptr_to_const_type &cube_subdivision, unsigned int max_num_cached_elements = 1)` | method | `non_null_ptr_type` | public | Creates a GLCubeSubdivisionCache object that caches the queries obtained from cube\_subdivision. |
| `Element` | class | `None` | private | — |
| `element_type` | typedef | `Element< typename boost::mpl::if_c<CacheProjectionTransform, Implementation::ProjectionTransform, Implementation::NoProjectionTransform>::type, typename boost::mpl::if_c<CacheLoose ...` | private | Typedef for cached element of cube subdivision. |
| `element_cache_type` | typedef | `GPlatesUtils::ObjectCache<element_type>` | private | Typedef for an object cache of element\_type. |
| `volatile_element_type` | typedef | `typename element_cache_type::volatile_object_type` | private | Typedef for an object cache volatile object referencing an element. |
| `volatile_element_ptr_type` | typedef | `typename element_cache_type::volatile_object_ptr_type` | private | Typedef for an object cache volatile pointer to an element. |
| `cube_quad_tree_type` | typedef | `GPlatesMaths::CubeQuadTree<volatile_element_ptr_type>` | private | Typedef for a cube quad tree of volatile element pointers. |
| `cube_quad_tree_node_type` | typedef | `typename cube_quad_tree_type::node_type` | private | Typedef for a node of the cube quad tree of volatile element pointers. |
| `NodeReference` | class | `None` | public | A reference, or handle, to a node of this cube subdivision. |
| `node_reference_type` | typedef | `NodeReference` | public | Typedef for a reference to a cube quad tree node. |
| `get_quad_tree_root_node( GPlatesMaths::CubeCoordinateFrame::CubeFaceType cube_face)` | method | `node_reference_type` | public | Returns the root node of the specified cube face quad tree (creates a root node if it doesn't exist). |
| `get_child_node( const node_reference_type &node, unsigned int child_u_offset, unsigned int child_v_offset)` | method | `node_reference_type` | public | Returns a reference to the specified child node (creates a child node if it doesn't exist). |
| `get_view_transform( const node_reference_type &node)` | method | `GLTransform::non_null_ptr_to_const_type` | public | Returns the view transform of this cached element. |
| `get_projection_transform( const node_reference_type &node)` | method | `GLTransform::non_null_ptr_to_const_type` | public | Returns the projection transform of this cached element. |
| `get_loose_projection_transform( const node_reference_type &node)` | method | `GLTransform::non_null_ptr_to_const_type` | public | Returns the loose projection transform of this cached element. |
| `get_frustum( const node_reference_type &node)` | method | `GLFrustum` | public | Returns the view frustum of this cached element. |
| `get_loose_frustum( const node_reference_type &node)` | method | `GLFrustum` | public | Returns the loose view frustum of this cached element. |
| `get_bounding_polygon( const node_reference_type &node)` | method | `GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type` | public | Returns the polygon boundary of this cached element. |
| `get_loose_bounding_polygon( const node_reference_type &node)` | method | `GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type` | public | Returns the loose polygon boundary of this cached element. |
| `get_oriented_bounding_box( const node_reference_type &node)` | method | `GLIntersect::OrientedBoundingBox` | public | Returns the oriented bounding box of this cached element. |
| `get_loose_oriented_bounding_box( const node_reference_type &node)` | method | `GLIntersect::OrientedBoundingBox` | public | Returns the loose oriented bounding box of this cached element. |
| `d_cube_subdivision` | field | `GLCubeSubdivision::non_null_ptr_to_const_type` | private | The cube subdivision whose queries we're caching. |
| `d_element_cache` | field | `typename element_cache_type::shared_ptr_type` | private | The cached elements. |
| `d_cube_quad_tree` | field | `typename cube_quad_tree_type::non_null_ptr_type` | private | The cube quad tree referencing the cached elements. |
| `d_view_transforms` | field | `std::vector<GLTransform::non_null_ptr_to_const_type>` | private | The view transform for each cube face. |
| `GLCubeSubdivisionCache( const GLCubeSubdivision::non_null_ptr_to_const_type &cube_subdivision, unsigned int max_num_cached_elements)` | constructor | `None` | private | — |
| `get_cached_element( const node_reference_type &node)` | method | `boost::shared_ptr<element_type>` | private | Returns the cached element for the specified cube quad tree node reference. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLCUBESUBDIVISIONCACHE_H` | macro | `None` | — |

## Notes

- Each `get_*` accessor only compiles when its corresponding `Cache*` template parameter is `true`; passing `false` (the default for all eight) and calling the accessor anyway is a compile error, not a runtime one.
- `max_num_cached_elements` passed to `create` bounds the underlying `GPlatesUtils::ObjectCache`; the default of `1` effectively disables caching and turns the class into a plain traverser of `GLCubeSubdivision`, useful when each quad-tree node is visited only once.
- A value returned by `get_cached_element` (indirectly, via the public accessors) cannot be recycled by the cache until every `shared_ptr` referencing it is released, so holding onto a returned element longer than necessary can defeat the cache's recycling.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLMultiResolutionRasterMapView](GLMultiResolutionRasterMapView.md) | opengl | 29 |
| [opengl/GLMultiResolutionCubeRaster](GLMultiResolutionCubeRaster.md) | opengl | 19 |
| [opengl/GLMatrix](GLMatrix.md) | opengl | 17 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 12 |
| [opengl/GLFilledPolygonsGlobeView](GLFilledPolygonsGlobeView.md) | opengl | 8 |
| [opengl/GLReconstructedStaticPolygonMeshes](GLReconstructedStaticPolygonMeshes.md) | opengl | 7 |
| [opengl/GLRasterCoRegistration](GLRasterCoRegistration.md) | opengl | 4 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 3 |
| [opengl/GLVisualLayers](GLVisualLayers.md) | opengl | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLCubeSubdivisionCache.h
python scripts/gpq.py def GPlatesOpenGL::GLCubeSubdivisionCache --body
python scripts/gpq.py uses GLCubeSubdivisionCache --kind class
python scripts/gpq.py hier GLCubeSubdivisionCache
```
