# GLMultiResolutionCubeRaster

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 208 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLMultiResolutionCubeRaster.h` | C++ | 671 |
| `src/opengl/GLMultiResolutionCubeRaster.cc` | C++ | 875 |

## Overview

[[[PROSE overview unit=opengl/GLMultiResolutionCubeRaster tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLMultiResolutionCubeRaster`](#gplatesopenglglmultiresolutioncuberaster) | class | [`GLMultiResolutionCubeRasterInterface`](GLMultiResolutionCubeRasterInterface.md) | — | 0 | A raster that is re-sampled into a multi-resolution cube map. |

## Members

### `GPlatesOpenGL::GLMultiResolutionCubeRaster`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TileTexture` | struct | `None` | private | Maintains a tile's texture and source tile cache handle. |
| `tile_texture_cache_type` | typedef | `GPlatesUtils::ObjectCache<TileTexture>` | private | Typedef for a cache of tile textures. |
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLMultiResolutionCubeRaster>` | public | A convenience typedef for a shared pointer to a non-const GLMultiResolutionCubeRaster. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLMultiResolutionCubeRaster>` | public | A convenience typedef for a shared pointer to a const GLMultiResolutionCubeRaster. |
| `cache_handle_type` | typedef | `GLMultiResolutionCubeRasterInterface::cache_handle_type` | public | Typedef for an opaque object that caches a particular tile of this raster. |
| `quad_tree_node_type` | typedef | `GLMultiResolutionCubeRasterInterface::quad_tree_node_type` | public | Typedef for a quad tree node. |
| `FixedPointTextureFilterType` | enum | `None` | public | The texture filter types to use for fixed-point textures. |
| `DEFAULT_FIXED_POINT_TEXTURE_FILTER` | field | `FixedPointTextureFilterType` | public | The default fixed-point texture filtering mode for the textures returned by get\_tile\_texture is bilinear (with anisotropic) filtering. |
| `FIXED_POINT_TEXTURE_FILTER_MAG_LINEAR_ANISOTROPIC` | field | `FixedPointTextureFilterType` | public | The default fixed-point texture filtering mode for the textures returned by get\_tile\_texture is bilinear (with anisotropic) filtering. |
| `CacheTileTexturesType` | enum | `None` | public | Determines the granularity of caching to be used for GLMultiResolutionCubeRaster tile textures... |
| `DEFAULT_CACHE_TILE_TEXTURES` | field | `CacheTileTexturesType` | public | The default granularity of tile texture caching. |
| `CACHE_TILE_TEXTURES_INDIVIDUAL_TILES` | field | `CacheTileTexturesType` | public | The default granularity of tile texture caching. |
| `DEFAULT_TILE_TEXEL_DIMENSION` | field | `unsigned int` | public | The default tile dimension is 256. |
| `supports_floating_point_source_raster( GLRenderer &renderer)` | method | `bool` | public | Returns true if floating-point source raster is supported. |
| `create( GLRenderer &renderer, const GLMultiResolutionRaster::non_null_ptr_type &source_multi_resolution_raster, unsigned int tile_texel_dimension = DEFAULT_TILE_TEXEL_DIMENSION, bool adapt_tile_dimension_to_source_resolution = true, FixedPointTextureFilterType fixed_point_texture_filter = DEFAULT_FIXED_POINT_TEXTURE_FI ...` | method | `non_null_ptr_type` | public | Creates a GLMultiResolutionCubeRaster object. tile\_texel\_dimension is the (possibly unadapted) dimension of each square tile texture (returned by get\_tile\_texture). |
| `set_world_transform( const GLMatrix &world_transform)` | method | `void` | public | Sets the transform to apply to raster/geometries when rendering into the cube map. |
| `get_subject_token` | field | `GPlatesUtils::SubjectToken` | public | Returns a subject token that clients can observe to see if they need to update themselves (such as any cached data we render for them) by getting us to re-render. |
| `get_quad_tree_root_node( GPlatesMaths::CubeCoordinateFrame::CubeFaceType cube_face)` | method | `boost::optional<quad_tree_node_type>` | public | Returns the quad tree root node of the specified cube face. |
| `get_child_node( const quad_tree_node_type &parent_node, unsigned int child_x_offset, unsigned int child_y_offset)` | method | `boost::optional<quad_tree_node_type>` | public | Returns the specified child cube quad tree node of specified parent node. |
| `get_tile_texel_dimension()` | method | `unsigned int` | public | Returns the tile texel dimension passed into constructor. |
| `get_tile_texture_internal_format()` | method | `GLint` | public | Returns the texture internal format that can be used if rendering to a texture as opposed to the main framebuffer. |
| `get_fixed_point_texture_filter()` | method | `FixedPointTextureFilterType` | public | Returns the filter for fixed-point textures (selected in create). |
| `create_tile_texture( GLRenderer &renderer, const GLTexture::shared_ptr_type &tile_texture, const quad_tree_node_type &tile)` | method | `void` | public | Initialises the specified tile texture to reserve memory for its (uninitialised) image and sets its various filtering options. |
| `update_tile_texture( GLRenderer &renderer, const GLTexture::shared_ptr_type &tile_texture, const quad_tree_node_type &tile)` | method | `void` | public | Updates the specified tile texture, created with create\_tile\_texture, so that its filtering options correspond to whether it belongs to a leaf node tile or not. |
| `get_num_levels_of_detail()` | method | `unsigned int` | public | Returns the number of levels of detail. |
| `ClientCacheTile` | struct | `None` | private | Used to cache information, specific to a tile, to return to the client for caching. |
| `CubeQuadTreeNode` | struct | `None` | private | A node in the quad tree of a cube face. |
| `cube_quad_tree_type` | typedef | `GPlatesMaths::CubeQuadTree<CubeQuadTreeNode>` | private | Typedef for a cube quad tree with nodes containing the type CubeQuadTreeNode. |
| `QuadTreeNodeImpl` | struct | `None` | private | Implementation of base class node to return to the client. |
| `cube_subdivision_cache_type` | typedef | `GLCubeSubdivisionCache< true/*CacheProjectionTransform*/>` | private | Typedef for a GLCubeSubvision cache. |
| `d_multi_resolution_raster` | field | `GLMultiResolutionRaster::non_null_ptr_type` | private | The raster we are re-sampling into our cube map. |
| `d_multi_resolution_raster_observer_token` | field | `GPlatesUtils::ObserverToken` | private | Keep track of changes to d\_multi\_resolution\_raster. |
| `d_tile_texel_dimension` | field | `unsigned int` | private | The number of texels along a tiles edge (horizontal or vertical since it's square). |
| `d_fixed_point_texture_filter` | field | `FixedPointTextureFilterType` | private | The texture filtering mode (for fixed-point textures) returned by get\_tile\_texture. |
| `d_texture_cache` | field | `tile_texture_cache_type::shared_ptr_type` | private | Cache of tile textures. |
| `d_cache_tile_textures` | field | `CacheTileTexturesType` | private | Determines granularity of caching of \*our\* tile textures (from get\_tile\_texture). |
| `d_cube_quad_tree` | field | `cube_quad_tree_type::non_null_ptr_type` | private | The cube quad tree. |
| `d_num_source_levels_of_detail_used` | field | `unsigned int` | private | The number of levels of detail of the source raster that we use. |
| `d_world_transform` | field | `GLMatrix` | private | The transform to use when rendering into the cube quad tree tiles. |
| `d_subject_token` | field | `GPlatesUtils::SubjectToken` | private | Used to inform clients that we have been updated. |
| `GLMultiResolutionCubeRaster( GLRenderer &renderer, const GLMultiResolutionRaster::non_null_ptr_type &multi_resolution_raster, unsigned int initial_tile_texel_dimension, bool adapt_tile_dimension_to_source_resolution, FixedPointTextureFilterType fixed_point_texture_filter, CacheTileTexturesType cache_tile_textures)` | constructor | `None` | private | Constructor. |
| `adjust_tile_texel_dimension( bool adapt_tile_dimension_to_source_resolution, const GLCapabilities &capabilities)` | method | `void` | private | Adjusts d\_tile\_texel\_dimension and determines the number of LODs of source raster used by this cube map raster. |
| `initialise_cube_quad_trees()` | method | `void` | private | — |
| `create_quad_tree_node( const GLViewport &viewport, cube_subdivision_cache_type &cube_subdivision_cache, const cube_subdivision_cache_type::node_reference_type &cube_subdivision_cache_node, const unsigned int source_level_of_detail)` | method | `boost::optional<cube_quad_tree_type::node_type::ptr_type>` | private | Creates a quad tree node if it is covered by the source raster. |
| `get_tile_texture( GLRenderer &renderer, const CubeQuadTreeNode &tile, cache_handle_type &cache_handle)` | method | `GLTexture::shared_ptr_to_const_type` | private | — |
| `render_raster_data_into_tile_texture( GLRenderer &renderer, const CubeQuadTreeNode &tile, TileTexture &tile_texture)` | method | `void` | private | — |
| `create_tile_texture( GLRenderer &renderer, const GLTexture::shared_ptr_type &tile_texture, const CubeQuadTreeNode &tile)` | method | `void` | private | — |
| `update_tile_texture( GLRenderer &renderer, const GLTexture::shared_ptr_type &tile_texture, const CubeQuadTreeNode &tile)` | method | `void` | private | — |
| `update_fixed_point_tile_texture_mag_filter( GLRenderer &renderer, const GLTexture::shared_ptr_type &tile_texture, const CubeQuadTreeNode &tile)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLMULTIRESOLUTIONCUBERASTER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLMultiResolutionCubeRaster tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 61 |
| [opengl/GLVisualLayers](GLVisualLayers.md) | opengl | 45 |
| [app-logic/RasterLayerProxy](../app-logic/RasterLayerProxy.md) | app-logic | 21 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 12 |
| [qt-widgets/MapCanvas](../qt-widgets/MapCanvas.md) | qt-widgets | 5 |
| [data-mining/DataSelector](../data-mining/DataSelector.md) | data-mining | 1 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLMultiResolutionCubeRaster.h
python scripts/gpq.py def GPlatesOpenGL::GLMultiResolutionCubeRaster --body
python scripts/gpq.py uses GLMultiResolutionCubeRaster --kind class
python scripts/gpq.py hier GLMultiResolutionCubeRaster
```
