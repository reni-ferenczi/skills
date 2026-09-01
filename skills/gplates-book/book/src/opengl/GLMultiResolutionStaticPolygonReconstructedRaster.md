# GLMultiResolutionStaticPolygonReconstructedRaster

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 71 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLMultiResolutionStaticPolygonReconstructedRaster.h` | C++ | 1007 |
| `src/opengl/GLMultiResolutionStaticPolygonReconstructedRaster.cc` | C++ | 3122 |

## Overview

[[[PROSE overview unit=opengl/GLMultiResolutionStaticPolygonReconstructedRaster tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLMultiResolutionStaticPolygonReconstructedRaster`](#gplatesopenglglmultiresolutionstaticpolygonreconstructedraster) | class | [`GLMultiResolutionRasterInterface`](GLMultiResolutionRasterInterface.md) | — | 0 | A raster that is reconstructed by mapping it onto a set of present-day static polygons and reconstructing the polygons (and hence partitioned pieces of the raster). |

## Members

### `GPlatesOpenGL::GLMultiResolutionStaticPolygonReconstructedRaster`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLMultiResolutionStaticPolygonReconstructedRaster>` | public | A convenience typedef for a shared pointer to a non-const GLMultiResolutionStaticPolygonReconstructedRaster. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLMultiResolutionStaticPolygonReconstructedRaster>` | public | A convenience typedef for a shared pointer to a const GLMultiResolutionStaticPolygonReconstructedRaster. |
| `cache_handle_type` | typedef | `GLMultiResolutionRasterInterface::cache_handle_type` | public | Typedef for an opaque object that caches a particular render of this raster. |
| `is_supported( GLRenderer &renderer)` | method | `bool` | public | Returns true if \*reconstructed\* rasters are supported on the runtime system. |
| `supports_floating_point_source_raster( GLRenderer &renderer)` | method | `bool` | public | Returns true if floating-point source raster is supported. |
| `supports_age_mask_generation( GLRenderer &renderer)` | method | `bool` | public | Returns true if age masks can be generated on the runtime system. |
| `supports_normal_map( GLRenderer &renderer)` | method | `bool` | public | Returns true if a normal map can be used on the runtime system to accentuate surface lighting. |
| `create( GLRenderer &renderer, const double &reconstruction_time, const GLMultiResolutionCubeRaster::non_null_ptr_type &source_raster, const std::vector<GLReconstructedStaticPolygonMeshes::non_null_ptr_type> &reconstructed_static_polygon_meshes, boost::optional<GLMultiResolutionCubeRaster::non_null_ptr_type> age_grid_ra ...` | method | `non_null_ptr_type` | public | Creates a GLMultiResolutionStaticPolygonReconstructedRaster object that is reconstructed using static polygon meshes. |
| `create( GLRenderer &renderer, const double &reconstruction_time, const GLMultiResolutionCubeRaster::non_null_ptr_type &source_raster, const GLMultiResolutionCubeMesh::non_null_ptr_to_const_type &multi_resolution_cube_mesh, boost::optional<GLMultiResolutionCubeRaster::non_null_ptr_type> age_grid_raster = boost::none, bo ...` | method | `non_null_ptr_type` | public | Same as the other overload of create but creates a GLMultiResolutionStaticPolygonReconstructedRaster object that is not reconstructed. |
| `update( const double &reconstruction_time)` | method | `void` | public | Updates the current reconstruction time. |
| `get_subject_token` | field | `GPlatesUtils::SubjectToken` | public | Returns a subject token that clients can observe to see if they need to update themselves (such as any cached data we render for them) by getting us to re-render. |
| `get_num_levels_of_detail()` | method | `unsigned int` | public | Returns the number of levels of detail. |
| `get_level_of_detail( const GLMatrix &model_view_transform, const GLMatrix &projection_transform, const GLViewport &viewport, float level_of_detail_bias = 0.0f)` | method | `float` | public | Returns the unclamped exact floating-point level-of-detail that theoretically represents the exact level-of-detail that would be required to fulfill the resolution needs of a render target (as defined by the specified viewport and ... |
| `clamp_level_of_detail( float level_of_detail)` | method | `float` | public | Takes an unclamped level-of-detail (see get\_level\_of\_detail) and clamps it to lie within the range \[-Infinity, get\_num\_levels\_of\_detail - 1\]. |
| `render( GLRenderer &renderer, float level_of_detail, cache_handle_type &cache_handle)` | method | `bool` | public | Renders all tiles visible in the view frustum (determined by the current model-view/projection transforms of renderer) and returns true if any tiles were rendered. |
| `get_tile_texel_dimension()` | method | `unsigned int` | public | Returns the tile texel dimension of this raster which is also the tile texel dimension of the source cube raster. |
| `get_target_texture_internal_format()` | method | `GLint` | public | Returns the texture internal format that can be used if rendering to a texture, when calling render, as opposed to the main framebuffer. |
| `source_raster_cube_subdivision_cache_type` | typedef | `GLCubeSubdivisionCache< true/*CacheProjectionTransform*/, false/*CacheLooseProjectionTransform*/, false/*CacheFrustum*/, false/*CacheLooseFrustum*/, false/*CacheBoundingPolygon*/, ...` | private | Typedef for the source raster GLCubeSubvision cache. |
| `age_grid_cube_subdivision_cache_type` | typedef | `GLCubeSubdivisionCache< true/*CacheProjectionTransform*/, false/*CacheLooseProjectionTransform*/, false/*CacheFrustum*/, false/*CacheLooseFrustum*/, false/*CacheBoundingPolygon*/, ...` | private | Typedef for the age grid GLCubeSubvision cache. |
| `normal_map_cube_subdivision_cache_type` | typedef | `GLCubeSubdivisionCache< true/*CacheProjectionTransform*/, false/*CacheLooseProjectionTransform*/, false/*CacheFrustum*/, false/*CacheLooseFrustum*/, false/*CacheBoundingPolygon*/, ...` | private | Typedef for the normal map GLCubeSubvision cache. |
| `clip_cube_subdivision_cache_type` | typedef | `GLCubeSubdivisionCache< true/*CacheProjectionTransform*/, false/*CacheLooseProjectionTransform*/, false/*CacheFrustum*/, false/*CacheLooseFrustum*/, false/*CacheBoundingPolygon*/, ...` | private | Typedef for clip GLCubeSubvision cache. |
| `AgeGridCubeRaster` | struct | `None` | private | Age grid cube raster. |
| `NormalMapCubeRaster` | struct | `None` | private | Normal map cube raster. |
| `ProgramObject` | struct | `None` | private | A GLProgramObject and the uniform variables it uses. |
| `RenderQuadTreeNode` | struct | `None` | private | Used to cache information, specific to a quad tree node, \*during\* traversal of the source raster. |
| `render_traversal_cube_quad_tree_type` | typedef | `GPlatesMaths::CubeQuadTree<RenderQuadTreeNode>` | private | Typedef for a cube quad tree used during traversal of the source raster. |
| `ClientCacheQuadTreeNode` | struct | `None` | private | Used to cache information, specific to a quad tree node, to return to the client for caching. |
| `client_cache_cube_quad_tree_type` | typedef | `GPlatesMaths::CubeQuadTree<ClientCacheQuadTreeNode>` | private | Typedef for a cube quad tree to return to the client, at each 'render' call, containing cached state that should be kept alive to prevent prematurely recycling our objects. |
| `QuadTreeNode` | struct | `None` | private | Used to cache information, specific to a quad tree node, \*across\* render traversals (across frames). |
| `cube_quad_tree_type` | typedef | `GPlatesMaths::CubeQuadTree<QuadTreeNode>` | private | Typedef for a cube quad tree that persists from one render call to the next. |
| `source_raster_quad_tree_node_type` | typedef | `GLMultiResolutionCubeRaster::quad_tree_node_type` | private | Typedef for a raster cube quad tree node. |
| `age_grid_mask_quad_tree_node_type` | typedef | `GLMultiResolutionCubeRaster::quad_tree_node_type` | private | Typedef for a cube quad tree of age grid mask tiles. |
| `normal_map_quad_tree_node_type` | typedef | `GLMultiResolutionCubeRaster::quad_tree_node_type` | private | Typedef for a cube quad tree of normal map tiles. |
| `present_day_polygon_mesh_drawables_seq_type` | typedef | `GLReconstructedStaticPolygonMeshes::present_day_polygon_mesh_drawables_seq_type` | private | Typedef for a sequence of present day polygon mesh drawables. |
| `present_day_polygon_meshes_node_intersections_type` | typedef | `GLReconstructedStaticPolygonMeshes::PresentDayPolygonMeshesNodeIntersections` | private | Typedef for a cube quad tree representing possible intersections of present day polygon meshes with each cube quad tree node. |
| `present_day_polygon_meshes_intersection_partition_type` | typedef | `present_day_polygon_meshes_node_intersections_type::intersection_partition_type` | private | — |
| `present_day_polygon_mesh_membership_type` | typedef | `GLReconstructedStaticPolygonMeshes::PresentDayPolygonMeshMembership` | private | Typedef for membership of present day polygon meshes. |
| `reconstructed_polygon_mesh_transform_group_seq_type` | typedef | `GLReconstructedStaticPolygonMeshes::reconstructed_polygon_mesh_transform_group_seq_type` | private | Typedef for a sequence of transform groups (of reconstructed polygon meshes). |
| `reconstructed_polygon_mesh_transform_group_type` | typedef | `GLReconstructedStaticPolygonMeshes::ReconstructedPolygonMeshTransformGroup` | private | Typedef for a transform group (of reconstructed polygon meshes). |
| `reconstructed_polygon_mesh_transform_groups_type` | typedef | `GLReconstructedStaticPolygonMeshes::ReconstructedPolygonMeshTransformsGroups` | private | Typedef for a sequences of transform groups (of reconstructed polygon meshes). |
| `cube_mesh_quad_tree_node_type` | typedef | `GLMultiResolutionCubeMesh::quad_tree_node_type` | private | Typedef for a quad tree node of a multi-resolution cube mesh. |
| `drawable_seq_type` | typedef | `std::vector<GLCompiledDrawState::non_null_ptr_to_const_type>` | private | Typedef for a sequence of drawables. |
| `ViewType` | enum | `None` | private | Classify the view projection as either a 3D globe view or 2D map view. |
| `d_reconstruction_time` | field | `double` | private | The current reconstruction time (used for age comparisons with age grid). |
| `d_source_raster` | field | `GLMultiResolutionCubeRaster::non_null_ptr_type` | private | The re-sampled source raster we are reconstructing. |
| `d_source_raster_texture_observer_token` | field | `GPlatesUtils::ObserverToken` | private | Keep track of changes to d\_source\_raster. |
| `d_reconstructed_static_polygon_meshes` | field | `std::vector<GLReconstructedStaticPolygonMeshes::non_null_ptr_type>` | private | The reconstructed present day static polygon meshes. |
| `d_reconstructed_static_polygon_meshes_observer_tokens` | field | `std::vector<GPlatesUtils::ObserverToken>` | private | Keep track of changes to d\_reconstructed\_static\_polygon\_meshes. |
| `d_multi_resolution_cube_mesh` | field | `boost::optional<GLMultiResolutionCubeMesh::non_null_ptr_to_const_type>` | private | The multi-resolution mesh used when the raster is not reconstructed. |
| `d_age_grid_cube_raster` | field | `boost::optional<AgeGridCubeRaster>` | private | Optional age grid raster. |
| `d_normal_map_cube_raster` | field | `boost::optional<NormalMapCubeRaster>` | private | Optional normal map raster. |
| `d_source_raster_tile_texel_dimension` | field | `unsigned int` | private | The source raster tile texture dimension. |
| `d_source_raster_inverse_tile_texel_dimension` | field | `float` | private | 1.0 / 'd\_source\_raster\_tile\_texel\_dimension'. |
| `d_source_raster_tile_root_uv_transform` | field | `GLUtils::QuadTreeUVTransform` | private | Source raster tile UV scaling/translating starts with this root UV transform (has texel overlap built in). |
| `d_xy_clip_texture` | field | `GLTexture::shared_ptr_type` | private | Texture used to clip parts of a mesh that hang over a tile (in the cube face x/y plane). |
| `d_z_clip_texture` | field | `GLTexture::shared_ptr_type` | private | Texture used to clip parts of a mesh that are inside a tile's frustum but on the opposite side of the globe (in the cube face z axis). |
| `d_xy_clip_texture_transform` | field | `GLMatrix` | private | Matrix to convert texture coordinates from range \[0,1\] to range \[0.25, 0.75\] to map to the interior 2x2 texel region of the 4x4 clip texture. |
| `d_full_screen_quad_drawable` | field | `GLCompiledDrawState::non_null_ptr_to_const_type` | private | Used to draw a textured full-screen quad into render texture. |
| `d_render_floating_point_program_object` | field | `boost::optional<ProgramObject>` | private | Render a floating-point source raster. |
| `d_render_floating_point_with_age_grid_with_active_polygons_program_object` | field | `boost::optional<ProgramObject>` | private | Render a floating-point source raster using an age grid with active polygons. |
| `d_render_floating_point_with_age_grid_with_inactive_polygons_program_object` | field | `boost::optional<ProgramObject>` | private | Render a floating-point source raster using an age grid with inactive polygons. |
| `d_render_fixed_point_program_object` | field | `boost::optional<ProgramObject>` | private | Render a fixed-point source raster. |
| `d_render_fixed_point_with_age_grid_with_active_polygons_program_object` | field | `boost::optional<ProgramObject>` | private | Render a fixed-point source raster using an age grid with active polygons. |
| `d_render_fixed_point_with_age_grid_with_inactive_polygons_program_object` | field | `boost::optional<ProgramObject>` | private | Render a fixed-point source raster using an age grid with inactive polygons. |
| `d_render_fixed_point_with_age_grid_with_active_polygons_with_surface_lighting_program_object` | field | `boost::optional<ProgramObject>` | private | Render a fixed-point source raster using an age grid with active polygons with surface lighting. |
| `d_render_fixed_point_with_age_grid_with_inactive_polygons_with_surface_lighting_program_object` | field | `boost::optional<ProgramObject>` | private | Render a fixed-point source raster using an age grid with inactive polygons with surface lighting. |
| `d_render_fixed_point_with_surface_lighting_program_object` | field | `boost::optional<ProgramObject>` | private | Render a fixed-point source raster with surface lighting. |
| `d_render_fixed_point_with_normal_map_program_object` | field | `boost::optional<ProgramObject>` | private | Render a fixed-point source raster with with a normal map. |
| `d_render_fixed_point_with_normal_map_with_surface_lighting_program_object` | field | `boost::optional<ProgramObject>` | private | Render a fixed-point source raster with a normal map with surface lighting. |
| `d_render_fixed_point_with_age_grid_with_active_polygons_with_normal_map_program_object` | field | `boost::optional<ProgramObject>` | private | Render a fixed-point source raster using an age grid with active polygons with a normal map with surface lighting. |
| `d_render_fixed_point_with_age_grid_with_inactive_polygons_with_normal_map_program_object` | field | `boost::optional<ProgramObject>` | private | Render a fixed-point source raster using an age grid with inactive polygons with a normal map. |
| `d_render_fixed_point_with_age_grid_with_active_polygons_with_normal_map_with_surface_lighting_program_object` | field | `boost::optional<ProgramObject>` | private | Render a fixed-point source raster using an age grid with active polygons with a normal map with surface lighting. |
| `d_render_fixed_point_with_age_grid_with_inactive_polygons_with_normal_map_with_surface_lighting_program_object` | field | `boost::optional<ProgramObject>` | private | Render a fixed-point source raster using an age grid with inactive polygons with a normal map with surface lighting. |
| `d_light` | field | `boost::optional<GLLight::non_null_ptr_type>` | private | The light (direction) used during surface lighting. |
| `d_light_observer_token` | field | `GPlatesUtils::ObserverToken` | private | Keep track of changes to d\_light. |
| `d_cube_quad_tree` | field | `cube_quad_tree_type::non_null_ptr_type` | private | Caches age-masked render textures for the cube quad tree tiles for re-use over multiple frames. |
| `d_subject_token` | field | `GPlatesUtils::SubjectToken` | private | Used to inform clients that we have been updated. |
| `GLMultiResolutionStaticPolygonReconstructedRaster( GLRenderer &renderer, const double &reconstruction_time, const GLMultiResolutionCubeRaster::non_null_ptr_type &source_raster, const std::vector<GLReconstructedStaticPolygonMeshes::non_null_ptr_type> &reconstructed_static_polygon_meshes, boost::optional<GLMultiResolutio ...` | constructor | `None` | private | Constructor. |
| `reconstructing_raster()` | method | `bool` | private | Returns true if reconstructing raster (using reconstructed static polygon meshes), otherwise \*not\* reconstructing raster (instead using GLMultiResolutionCubeMesh). |
| `render_transform_group( GLRenderer &renderer, render_traversal_cube_quad_tree_type &render_traversal_cube_quad_tree, client_cache_cube_quad_tree_type &client_cache_cube_quad_tree, boost::optional<const reconstructed_polygon_mesh_transform_group_type &> reconstructed_polygon_mesh_transform_group, boost::optional<const p ...` | method | `void` | private | — |
| `render_quad_tree( GLRenderer &renderer, boost::object_pool<GLUtils::QuadTreeUVTransform> &pool_quad_tree_uv_transforms, render_traversal_cube_quad_tree_type &render_traversal_cube_quad_tree, render_traversal_cube_quad_tree_type::node_type &render_traversal_cube_quad_tree_node, client_cache_cube_quad_tree_type &client_c ...` | method | `void` | private | — |
| `render_tile_to_scene( GLRenderer &renderer, render_traversal_cube_quad_tree_type::node_type &render_traversal_cube_quad_tree_node, client_cache_cube_quad_tree_type::node_type &client_cache_cube_quad_tree_node, const source_raster_quad_tree_node_type &source_raster_quad_tree_node, const GLUtils::QuadTreeUVTransform &sou ...` | method | `void` | private | — |
| `get_tile_textures( GLRenderer &renderer, boost::optional<GLTexture::shared_ptr_to_const_type> &source_raster_texture, boost::optional<GLTexture::shared_ptr_to_const_type> &age_grid_mask_texture, boost::optional<GLTexture::shared_ptr_to_const_type> &normal_map_texture, client_cache_cube_quad_tree_type::node_type &client ...` | method | `bool` | private | — |
| `get_shader_program_for_tile( bool source_raster_is_floating_point, bool using_age_grid_tile, bool using_normal_map_tile, bool active_polygons)` | method | `boost::optional<ProgramObject>` | private | — |
| `create_scene_tile_draw_state( GLRenderer &renderer, boost::optional<ProgramObject> render_tile_to_scene_program_object, const GLTexture::shared_ptr_to_const_type &source_raster_tile_texture, const GLUtils::QuadTreeUVTransform &source_raster_uv_transform, boost::optional<GLTexture::shared_ptr_to_const_type> age_grid_til ...` | method | `RenderQuadTreeNode::TileDrawState` | private | — |
| `render_tile_polygon_drawables( GLRenderer &renderer, const RenderQuadTreeNode::TileDrawState &render_scene_tile_draw_state, const GPlatesMaths::UnitQuaternion3D &reconstructed_polygon_mesh_rotation, const present_day_polygon_mesh_membership_type &reconstructed_polygon_mesh_membership, const present_day_polygon_meshes_n ...` | method | `void` | private | — |
| `apply_tile_state( GLRenderer &renderer, const RenderQuadTreeNode::TileDrawState &tile_draw_state, const GPlatesMaths::UnitQuaternion3D &plate_rotation)` | method | `void` | private | — |
| `apply_tile_shader_program_state( GLRenderer &renderer, const RenderQuadTreeNode::TileDrawState &tile_draw_state)` | method | `void` | private | — |
| `create_shader_programs( GLRenderer &renderer)` | method | `void` | private | — |
| `create_shader_program( GLRenderer &renderer, bool define_source_raster_is_floating_point, bool define_using_age_grid, bool define_generate_age_mask, bool define_active_polygons, bool define_surface_lighting, bool define_using_normal_map, bool define_no_directional_light_for_normal_maps, bool define_map_view)` | method | `boost::optional<ProgramObject>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `TEMPORARY_HACK_NO_DIRECTIONAL_LIGHT_FOR_NORMAL_MAPS` | macro | `None` | Temporarily remove directional lighting for normal maps until GPlates 1.4 (when introduce light canvas tool)... |
| `INVERSE_LOG2` | variable | `float` | The inverse of log(2.0). |
| `RENDER_TILE_TO_SCENE_VERTEX_SHADER_SOURCE_FILE_NAME` | variable | `QString` | Vertex shader source code to render raster tiles to the scene. |
| `RENDER_TILE_TO_SCENE_FRAGMENT_SHADER_SOURCE_FILE_NAME` | variable | `QString` | Fragment shader source code to render raster tiles to the scene. |
| `create_dot3_extract_red_channel()` | function | `std::vector<GLfloat>` | A 4-component texture environment colour used to extract red channel when used with GL\_ARB\_texture\_env\_dot3. |
| `GPLATES_OPENGL_GLMULTIRESOLUTIONSTATICPOLYGONRECONSTRUCTEDRASTER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLMultiResolutionStaticPolygonReconstructedRaster tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLVisualLayers](GLVisualLayers.md) | opengl | 19 |
| [app-logic/RasterLayerProxy](../app-logic/RasterLayerProxy.md) | app-logic | 15 |
| [opengl/GLMultiResolutionCubeReconstructedRaster](GLMultiResolutionCubeReconstructedRaster.md) | opengl | 11 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 4 |
| [opengl/GLRenderer](GLRenderer.md) | opengl | 2 |
| [qt-widgets/MapCanvas](../qt-widgets/MapCanvas.md) | qt-widgets | 1 |

## Related

**Shader programs compiled by this unit**

| Shader unit | Component |
|---|---|
| [shaders/multi_resolution_static_polygon_reconstructed_raster](../qt-resources/opengl/multi_resolution_static_polygon_reconstructed_raster.md) | shaders |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLMultiResolutionStaticPolygonReconstructedRaster.h
python scripts/gpq.py def GPlatesOpenGL::GLMultiResolutionStaticPolygonReconstructedRaster --body
python scripts/gpq.py uses GLMultiResolutionStaticPolygonReconstructedRaster --kind class
python scripts/gpq.py hier GLMultiResolutionStaticPolygonReconstructedRaster
```
