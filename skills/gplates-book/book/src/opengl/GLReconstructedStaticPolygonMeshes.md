# GLReconstructedStaticPolygonMeshes

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 125 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLReconstructedStaticPolygonMeshes.h` | C++ | 825 |
| `src/opengl/GLReconstructedStaticPolygonMeshes.cc` | C++ | 1195 |

## Overview

Bridges the app-logic reconstruction of static polygons to the GPU: it turns a
present-day set of polygon geometries into GPU-ready `PolygonMeshDrawable`s once,
then, on each `update`, re-groups the already-reconstructed
`ReconstructContext::Reconstruction`s (from a
`reconstructions_spatial_partition_type` cube quad tree partition) by their
`GPlatesMaths::UnitQuaternion3D` finite rotation into
`ReconstructedPolygonMeshTransformGroup`s. `GLMultiResolutionStaticPolygonReconstructedRaster`
and other raster-reconstruction consumers call `get_reconstructed_polygon_meshes`
each frame to get those groups back, filtered to the polygons visible in the
current view frustum via `PresentDayPolygonMeshMembership` bitsets, so a whole
transform group can be drawn with a single model-view transform instead of one
draw call per polygon.

Because polygon interiors need to be tested against raster tiles cube-face by
cube-face, the class precomputes `PresentDayPolygonMeshesNodeIntersections`: a
conservative (may include false positives, never false negatives) cube quad tree
recording which present-day polygon meshes can possibly intersect each node,
built once from the present-day geometries and reused for the lifetime of the
object. The present-day drawables and this intersection tree are both constant
for the object's lifetime; only the per-transform-group membership changes as
`update` is called with a new reconstruction time and spatial partition. A
separate `active_or_inactive_reconstructions_spatial_partition` argument lets
`update` also track polygons that are reconstructed but inactive at the current
time, which raster reconstruction needs when an age grid — rather than the
polygons' own begin time — decides where to mask off oceanic crust.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLReconstructedStaticPolygonMeshes`](#gplatesopenglglreconstructedstaticpolygonmeshes) | class | [`GPlatesUtils::ReferenceCount<GLReconstructedStaticPolygonMeshes>`](../utils/ReferenceCount.md) | — | 0 | Reconstructed static polygons used to reconstruct a raster. |

## Members

### `GPlatesOpenGL::GLReconstructedStaticPolygonMeshes`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLReconstructedStaticPolygonMeshes>` | public | A convenience typedef for a shared pointer to a non-const GLReconstructedStaticPolygonMeshes. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLReconstructedStaticPolygonMeshes>` | public | A convenience typedef for a shared pointer to a const GLReconstructedStaticPolygonMeshes. |
| `polygon_mesh_seq_type` | typedef | `std::vector<boost::optional<GPlatesMaths::PolygonMesh::non_null_ptr_to_const_type> >` | public | Typedef for a sequence of PolygonMesh objects. |
| `geometries_seq_type` | typedef | `std::vector<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | public | Typedef for a sequence of geometries. |
| `present_day_polygon_mesh_handle_type` | typedef | `unsigned int` | public | Typedef for a handle (index) into a sequence of present day polygon meshes. |
| `reconstructions_spatial_partition_type` | typedef | `GPlatesMaths::CubeQuadTreePartition<GPlatesAppLogic::ReconstructContext::Reconstruction>` | public | Typedef for a spatial partition of reconstructed feature geometries. |
| `PolygonMeshDrawable` | struct | `None` | public | A polygon mesh consisting of triangles within the interior region of the polygon if the polygon was successfully meshed, otherwise simply a triangle fan mesh (with centroid as apex). |
| `present_day_polygon_mesh_drawables_seq_type` | typedef | `std::vector<boost::optional<PolygonMeshDrawable> >` | public | Typedef for a sequence of OpenGL drawables representing the present day polygon meshes. |
| `PresentDayPolygonMeshMembership` | class | `None` | public | Represents the boolean membership state of present day polygon meshes. |
| `PresentDayPolygonMeshesNodeIntersections` | class | `None` | public | Keeps track of which present day polygon meshes intersect which cube quad tree nodes. |
| `ReconstructedPolygonMeshTransformGroup` | class | `None` | public | Contains all reconstructed polygon meshes that have the same transform. |
| `reconstructed_polygon_mesh_transform_group_seq_type` | typedef | `std::vector<ReconstructedPolygonMeshTransformGroup>` | public | Typedef for a sequence of reconstructed polygon mesh transform groups. |
| `ReconstructedPolygonMeshTransformsGroups` | class | `None` | public | Contains all reconstructed polygon meshes for all transforms. |
| `create( GLRenderer &renderer, const polygon_mesh_seq_type &polygon_meshes, const geometries_seq_type &present_day_geometries, const double &reconstruction_time, const reconstructions_spatial_partition_type::non_null_ptr_to_const_type &initial_reconstructions_spatial_partition)` | method | `non_null_ptr_type` | public | Creates a GLReconstructedStaticPolygonMeshes object. |
| `update( const double &reconstruction_time, const reconstructions_spatial_partition_type::non_null_ptr_to_const_type &reconstructions_spatial_partition, boost::optional<reconstructions_spatial_partition_type::non_null_ptr_to_const_type> active_or_inactive_reconstructions_spatial_partition = boost::none)` | method | `void` | public | Updates the reconstructed static polygons corresponding to the present day polygons passed into the constructor. |
| `get_reconstructed_polygon_meshes( GLRenderer &renderer)` | method | `ReconstructedPolygonMeshTransformsGroups::non_null_ptr_to_const_type` | public | Returns the reconstructed feature geometries grouped by finite rotation transforms along with the present day OpenGL polygon meshes. |
| `cube_subdivision_cache_type` | typedef | `GPlatesOpenGL::GLCubeSubdivisionCache< true/*CacheProjectionTransform*/, false/*CacheLooseProjectionTransform*/, true/*CacheFrustum*/, false/*CacheLooseFrustum*/, true/*CacheBoundi ...` | private | Typedef for a GLCubeSubvision cache. |
| `ReconstructedPolygonMeshTransformGroupBuilder` | struct | `None` | private | Contains all reconstructed polygon meshes that have the same transform. |
| `reconstructed_polygon_mesh_transform_group_builder_seq_type` | typedef | `std::vector<ReconstructedPolygonMeshTransformGroupBuilder>` | private | Typedef for a sequence of reconstructed polygon mesh transform group builders. |
| `reconstructed_polygon_mesh_transform_group_builder_map_type` | typedef | `std::map< boost::reference_wrapper<const GPlatesAppLogic::ReconstructMethodFiniteRotation>, reconstructed_polygon_mesh_transform_group_builder_seq_type::size_type>` | private | Typedef for mapping finite rotations to a group of reconstructed polygon meshes. |
| `d_polygon_meshes_vertex_array` | field | `GLVertexArray::shared_ptr_type` | private | All polygon mesh drawables share a single vertex array. |
| `d_present_day_polygon_mesh_drawables` | field | `present_day_polygon_mesh_drawables_seq_type` | private | The OpenGL drawables representing each present day polygon mesh. |
| `d_present_day_polygon_meshes_node_intersections` | field | `PresentDayPolygonMeshesNodeIntersections` | private | Boolean state of intersection of present day polygon meshes with cube quad tree nodes. |
| `d_reconstruction_time` | field | `double` | private | The current reconstruction time. |
| `d_reconstructions_spatial_partition` | field | `reconstructions_spatial_partition_type::non_null_ptr_to_const_type` | private | The reconstructed feature geometries for the current reconstruction time. |
| `d_active_or_inactive_reconstructions_spatial_partition` | field | `boost::optional<reconstructions_spatial_partition_type::non_null_ptr_to_const_type>` | private | The reconstructed feature geometries for the current reconstruction time even if the features (that they were reconstructed from) are not active (or not defined) at the reconstruction time. |
| `d_subject_token` | field | `GPlatesUtils::SubjectToken` | private | Used to inform clients that we have been updated. |
| `GLReconstructedStaticPolygonMeshes( GLRenderer &renderer, const polygon_mesh_seq_type &polygon_meshes, const geometries_seq_type &present_day_geometries, const double &reconstruction_time, const reconstructions_spatial_partition_type::non_null_ptr_to_const_type &initial_reconstructions_spatial_partition)` | constructor | `None` | private | Constructor. |
| `get_reconstructed_polygon_meshes_from_quad_tree( reconstructed_polygon_mesh_transform_group_builder_seq_type &reconstructed_polygon_mesh_transform_groups, reconstructed_polygon_mesh_transform_group_builder_map_type &reconstructed_polygon_mesh_transform_group_map, unsigned int num_polygon_meshes, const reconstructions_s ...` | method | `void` | private | Get the reconstructions for the specified spatial partition node. |
| `add_reconstructed_polygon_meshes( reconstructed_polygon_mesh_transform_group_builder_seq_type &reconstructed_polygon_mesh_transform_groups, reconstructed_polygon_mesh_transform_group_builder_map_type &reconstructed_polygon_mesh_transform_group_map, unsigned int num_polygon_meshes, const reconstructions_spatial_partitio ...` | method | `void` | private | Adds a sequence of polygon meshes belonging to the cube root or to a quad tree node. |
| `create_polygon_mesh_drawables( GLRenderer &renderer, const geometries_seq_type &present_day_geometries, const polygon_mesh_seq_type &polygon_meshes)` | method | `void` | private | Creates the vertex array of the polygon meshes and wraps each individual polygon mesh in a drawable. |
| `find_present_day_polygon_mesh_node_intersections( const geometries_seq_type &present_day_geometries)` | method | `void` | private | For each present day polygon mesh determines, and records, which nodes of the cube quad tree node it possibly intersects. |
| `find_present_day_polygon_mesh_node_intersections( present_day_polygon_mesh_handle_type polygon_mesh_handle, const GPlatesMaths::PolygonMesh &polygon_mesh, cube_subdivision_cache_type &cube_subdivision_cache)` | method | `void` | private | — |
| `find_present_day_polygon_mesh_node_intersections( const present_day_polygon_mesh_handle_type present_day_polygon_mesh_handle, const GPlatesMaths::PolygonMesh &polygon_mesh, const std::vector<unsigned int> &polygon_mesh_parent_triangle_indices, PresentDayPolygonMeshesNodeIntersections::intersection_partition_type::node_ ...` | method | `void` | private | — |
| `find_present_day_polygon_mesh_node_intersections( present_day_polygon_mesh_handle_type polygon_mesh_handle, const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &present_day_geometry, cube_subdivision_cache_type &cube_subdivision_cache)` | method | `void` | private | — |
| `find_present_day_polygon_mesh_node_intersections( const present_day_polygon_mesh_handle_type present_day_polygon_mesh_handle, const GPlatesMaths::PolygonPartitioner &polygon_partitioner, PresentDayPolygonMeshesNodeIntersections::intersection_partition_type::node_type &intersections_quad_tree_node, cube_subdivision_cach ...` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLRECONSTRUCTEDSTATICPOLYGONMESHES_H` | macro | `None` | — |

## Notes

If the present-day polygons themselves change, the header is explicit that
callers must create a new `GLReconstructedStaticPolygonMeshes` rather than
continue using an existing one — `update` only re-reconstructs against the
polygon meshes fixed at construction. The "inactive" and "active-or-inactive"
membership accessors on `ReconstructedPolygonMeshTransformGroup` and
`ReconstructedPolygonMeshTransformsGroups` return empty memberships whenever
`update` was last called without an `active_or_inactive_reconstructions_spatial_partition`,
so a caller must check which overload of `update` was used before relying on
those results. `get_subject_token` lets dependents (such as cached rasters)
detect that they need to re-fetch reconstructed polygon meshes after an
`update`, rather than polling.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 23 |
| [app-logic/ReconstructLayerProxy](../app-logic/ReconstructLayerProxy.md) | app-logic | 16 |
| [opengl/GLVisualLayers](GLVisualLayers.md) | opengl | 6 |
| [app-logic/RasterLayerProxy](../app-logic/RasterLayerProxy.md) | app-logic | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLReconstructedStaticPolygonMeshes.h
python scripts/gpq.py def GPlatesOpenGL::GLReconstructedStaticPolygonMeshes --body
python scripts/gpq.py uses GLReconstructedStaticPolygonMeshes --kind class
python scripts/gpq.py hier GLReconstructedStaticPolygonMeshes
```
