# GLMultiResolutionRasterMapView

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 802 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLMultiResolutionRasterMapView.h` | C++ | 238 |
| `src/opengl/GLMultiResolutionRasterMapView.cc` | C++ | 810 |

## Overview

`GLMultiResolutionRasterMapView` renders a `GLMultiResolutionCubeRasterInterface` (any cube-map-tiled raster, reconstructed or not) drawn onto the 2D map projection defined by a `GLMultiResolutionMapCubeMesh`. It is the counterpart, for the flat map view, of drawing a cube raster straight onto the sphere in the globe view: instead of textured cube tiles being placed directly in 3D, `render()` walks the raster's cube quad tree and the mesh's cube quad tree together (`render_quad_tree()`) and renders each raster tile onto its corresponding map-projected mesh tile (`render_tile_to_scene()`), selecting resolution from `get_viewport_pixel_size_in_map_projection()` rather than from a 3D frustum.

`create()` re-orients the given cube raster's world transform to the map projection's central meridian longitude so cube-map texel space lines up with the mesh, meaning the caller's cube raster is mutated as a side effect of construction. Rendering prefers a `GLProgramObject` shader pair (`d_render_tile_to_scene_program_object`/`..._with_clipping`) built by `create_shader_programs()` from the `multi_resolution_raster_map_view` shader sources; where shader programs are unsupported the code falls back to the fixed-function pipeline, but then loses the clipping variant, so at high zoom tile-boundary artefacts can appear.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLMultiResolutionRasterMapView`](#gplatesopenglglmultiresolutionrastermapview) | class | [`GPlatesUtils::ReferenceCount<GLMultiResolutionRasterMapView>`](../utils/ReferenceCount.md) | — | 0 | Used to view multi-resolution cube raster in a 2D map projection of the globe. |

## Members

### `GPlatesOpenGL::GLMultiResolutionRasterMapView`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLMultiResolutionRasterMapView>` | public | A convenience typedef for a shared pointer to a non-const GLMultiResolutionRasterMapView. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLMultiResolutionRasterMapView>` | public | A convenience typedef for a shared pointer to a const GLMultiResolutionMapView. |
| `cache_handle_type` | typedef | `boost::shared_ptr<void>` | public | Typedef for an opaque object that caches a particular render of this map view. |
| `create( GLRenderer &renderer, const GLMultiResolutionCubeRasterInterface::non_null_ptr_type &multi_resolution_cube_raster, const GLMultiResolutionMapCubeMesh::non_null_ptr_to_const_type &multi_resolution_map_cube_mesh)` | method | `non_null_ptr_type` | public | Creates a GLMultiResolutionRasterMapView object. |
| `render( GLRenderer &renderer, cache_handle_type &cache_handle)` | method | `bool` | public | Renders the source raster, as a map projection, visible in the view frustum (determined by the current viewport and model-view/projection transforms of renderer). cache\_handle can be stored by the client to keep textures (and vertices), ... |
| `cube_subdivision_cache_type` | typedef | `GLCubeSubdivisionCache< true/*CacheProjectionTransform*/, false/*CacheLooseProjectionTransform*/, false/*CacheFrustum*/, false/*CacheLooseFrustum*/, false/*CacheBoundingPolygon*/, ...` | private | Typedef for a GLCubeSubvision cache. |
| `clip_cube_subdivision_cache_type` | typedef | `GLCubeSubdivisionCache< true/*CacheProjectionTransform*/, false/*CacheLooseProjectionTransform*/, false/*CacheFrustum*/, false/*CacheLooseFrustum*/, false/*CacheBoundingPolygon*/, ...` | private | Typedef for a GLCubeSubvision cache. |
| `mesh_quad_tree_node_type` | typedef | `GLMultiResolutionMapCubeMesh::quad_tree_node_type` | private | Typedef for a quad tree node of a multi-resolution cube mesh. |
| `raster_quad_tree_node_type` | typedef | `GLMultiResolutionCubeRasterInterface::quad_tree_node_type` | private | Typedef for the source raster cube quad tree node. |
| `ERROR_VIEWPORT_PIXEL_SIZE_IN_MAP_PROJECTION` | field | `double` | private | The viewport pixel size (in map projection coordinates) to use when there's an error. |
| `d_multi_resolution_cube_raster` | field | `GLMultiResolutionCubeRasterInterface::non_null_ptr_type` | private | — |
| `d_multi_resolution_map_cube_mesh` | field | `GLMultiResolutionMapCubeMesh::non_null_ptr_to_const_type` | private | — |
| `d_tile_texel_dimension` | field | `unsigned int` | private | The texture dimension of a cube quad tree tile. |
| `d_inverse_tile_texel_dimension` | field | `float` | private | 1.0 / 'd\_tile\_texel\_dimension'. |
| `d_map_projection_central_meridian_longitude` | field | `double` | private | The map projection's central meridian longitude is used as a transform when rendering the source raster (to align it with the map cube mesh). |
| `d_world_transform` | field | `GLMatrix` | private | The transform used for the map projection's central meridian longitude. |
| `d_render_tile_to_scene_program_object` | field | `boost::optional<GLProgramObject::shared_ptr_type>` | private | Shader program to render tiles to the scene. |
| `d_render_tile_to_scene_with_clipping_program_object` | field | `boost::optional<GLProgramObject::shared_ptr_type>` | private | Shader program to render tiles to the scene with clipping. |
| `GLMultiResolutionRasterMapView( GLRenderer &renderer, const GLMultiResolutionCubeRasterInterface::non_null_ptr_type &multi_resolution_cube_raster, const GLMultiResolutionMapCubeMesh::non_null_ptr_to_const_type &multi_resolution_map_cube_mesh)` | constructor | `None` | private | — |
| `render_quad_tree( GLRenderer &renderer, const raster_quad_tree_node_type &source_raster_quad_tree_node, const mesh_quad_tree_node_type &mesh_quad_tree_node, cube_subdivision_cache_type &cube_subdivision_cache, const cube_subdivision_cache_type::node_reference_type &cube_subdivision_cache_node, clip_cube_subdivision_cac ...` | method | `void` | private | — |
| `render_tile_to_scene( GLRenderer &renderer, const raster_quad_tree_node_type &source_raster_quad_tree_node, const mesh_quad_tree_node_type &mesh_quad_tree_node, cube_subdivision_cache_type &cube_subdivision_cache, const cube_subdivision_cache_type::node_reference_type &cube_subdivision_cache_node, clip_cube_subdivision ...` | method | `void` | private | — |
| `set_tile_state( GLRenderer &renderer, const GLTexture::shared_ptr_to_const_type &tile_texture, const GLTransform &projection_transform, const GLTransform &clip_projection_transform, const GLTransform &view_transform, bool clip_to_tile_frustum)` | method | `void` | private | — |
| `get_viewport_pixel_size_in_map_projection( const GLViewport &viewport, const GLMatrix &model_view_transform, const GLMatrix &projection_transform)` | method | `double` | private | — |
| `create_shader_programs( GLRenderer &renderer)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `RENDER_TILE_TO_SCENE_VERTEX_SHADER_SOURCE_FILE_NAME` | variable | `QString` | Vertex shader source code to render a tile to the scene. |
| `RENDER_TILE_TO_SCENE_FRAGMENT_SHADER_SOURCE_FILE_NAME` | variable | `QString` | Fragment shader source code to render a tile to the scene. |
| `visualise_level_of_detail_in_texture( GLRenderer &renderer, const GLTexture::shared_ptr_to_const_type &tile_texture, unsigned int level_of_detail)` | function | `void` | — |
| `ERROR_VIEWPORT_PIXEL_SIZE_IN_MAP_PROJECTION` | variable | `double` | — |
| `GPLATES_OPENGL_GLMULTIRESOLUTIONRASTERMAPVIEW_H` | macro | `None` | — |

## Notes

Creating a view mutates the passed-in `multi_resolution_cube_raster`'s world transform to align it with the map projection's central meridian, so the same cube raster instance should not simultaneously be relied on to render un-transformed (e.g. for the globe view) elsewhere. `render()` returns `false` without rendering anything when the source raster does not intersect the view frustum at all (for example, a non-global raster scrolled out of view), which is a valid, non-error outcome. When shader programs are unavailable, the fixed-function fallback omits tile clipping, so visual artefacts at tile boundaries are expected at high zoom on such hardware rather than indicating a bug.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLVisualLayers](GLVisualLayers.md) | opengl | 24 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 4 |

## Related

**Shader programs compiled by this unit**

| Shader unit | Component |
|---|---|
| [shaders/multi_resolution_raster_map_view](../qt-resources/opengl/multi_resolution_raster_map_view.md) | shaders |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLMultiResolutionRasterMapView.h
python scripts/gpq.py def GPlatesOpenGL::GLMultiResolutionRasterMapView --body
python scripts/gpq.py uses GLMultiResolutionRasterMapView --kind class
python scripts/gpq.py hier GLMultiResolutionRasterMapView
```
