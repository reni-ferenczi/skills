# GLMultiResolutionCubeReconstructedRaster

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 175 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLMultiResolutionCubeReconstructedRaster.h` | C++ | 455 |
| `src/opengl/GLMultiResolutionCubeReconstructedRaster.cc` | C++ | 531 |

## Overview

[[[PROSE overview unit=opengl/GLMultiResolutionCubeReconstructedRaster tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLMultiResolutionCubeReconstructedRaster`](#gplatesopenglglmultiresolutioncubereconstructedraster) | class | [`GLMultiResolutionCubeRasterInterface`](GLMultiResolutionCubeRasterInterface.md) | — | 0 | A reconstructed raster rendered into a multi-resolution cube map. |

## Members

### `GPlatesOpenGL::GLMultiResolutionCubeReconstructedRaster`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TileTexture` | struct | `None` | private | Maintains a tile's texture and source tile cache handle. |
| `tile_texture_cache_type` | typedef | `GPlatesUtils::ObjectCache<TileTexture>` | private | Typedef for a cache of tile textures. |
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLMultiResolutionCubeReconstructedRaster>` | public | A convenience typedef for a shared pointer to a non-const GLMultiResolutionCubeReconstructedRaster. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLMultiResolutionCubeReconstructedRaster>` | public | A convenience typedef for a shared pointer to a const GLMultiResolutionCubeReconstructedRaster. |
| `cache_handle_type` | typedef | `GLMultiResolutionCubeRasterInterface::cache_handle_type` | public | Typedef for an opaque object that caches a particular tile of this raster. |
| `quad_tree_node_type` | typedef | `GLMultiResolutionCubeRasterInterface::quad_tree_node_type` | public | Typedef for a quad tree node. |
| `create( GLRenderer &renderer, const GLMultiResolutionStaticPolygonReconstructedRaster::non_null_ptr_type &source_reconstructed_raster, bool cache_tile_textures = true)` | method | `non_null_ptr_type` | public | Creates a GLMultiResolutionCubeReconstructedRaster object. |
| `set_world_transform( const GLMatrix &world_transform)` | method | `void` | public | Sets the transform to apply to raster/geometries when rendering into the cube map. |
| `get_subject_token` | field | `GPlatesUtils::SubjectToken` | public | Returns a subject token that clients can observe to see if they need to update themselves (such as any cached data we render for them) by getting us to re-render. |
| `get_quad_tree_root_node( GPlatesMaths::CubeCoordinateFrame::CubeFaceType cube_face)` | method | `boost::optional<quad_tree_node_type>` | public | Returns the quad tree root node of the specified cube face. |
| `get_child_node( const quad_tree_node_type &parent_node, unsigned int child_x_offset, unsigned int child_y_offset)` | method | `boost::optional<quad_tree_node_type>` | public | Returns the specified child cube quad tree node of specified parent node. |
| `get_tile_texel_dimension()` | method | `unsigned int` | public | Returns the tile texel dimension. |
| `get_tile_texture_internal_format()` | method | `GLint` | public | Returns the texture internal format that can be used if rendering to a texture as opposed to the main framebuffer. |
| `ClientCacheTile` | struct | `None` | private | Used to cache information, specific to a tile, to return to the client for caching. |
| `CubeQuadTreeNode` | struct | `None` | private | A node in the quad tree of a cube face. |
| `cube_quad_tree_type` | typedef | `GPlatesMaths::CubeQuadTree<CubeQuadTreeNode>` | private | Typedef for a cube quad tree with nodes containing the type CubeQuadTreeNode. |
| `QuadTreeNodeImpl` | struct | `None` | private | Implementation of base class node to return to the client. |
| `MIN_TILE_TEXEL_DIMENSION` | field | `unsigned int` | private | Minimum tile texel dimension. |
| `d_reconstructed_raster` | field | `GLMultiResolutionStaticPolygonReconstructedRaster::non_null_ptr_type` | private | The reconstructed raster we are rendering into our cube map. |
| `d_reconstructed_raster_observer_token` | field | `GPlatesUtils::ObserverToken` | private | Keep track of changes to d\_reconstructed\_raster. |
| `d_level_of_detail_offset_for_scaled_tile_dimension` | field | `int` | private | If we increased the tile texel dimension then we need to adjust LOD correspondingly. |
| `d_tile_texel_dimension` | field | `unsigned int` | private | The number of texels along a tiles edge (horizontal or vertical since it's square). |
| `d_texture_cache` | field | `tile_texture_cache_type::shared_ptr_type` | private | Cache of tile textures. |
| `d_cache_tile_textures` | field | `bool` | private | If true then we cache the tile textures. |
| `d_cube_subdivision` | field | `GLCubeSubdivision::non_null_ptr_to_const_type` | private | Used to calculate projection transforms for the cube quad tree. |
| `d_cube_quad_tree` | field | `cube_quad_tree_type::non_null_ptr_type` | private | The cube quad tree. |
| `d_world_transform` | field | `GLMatrix` | private | The transform to use when rendering into the cube quad tree tiles. |
| `d_subject_token` | field | `GPlatesUtils::SubjectToken` | private | Used to inform clients that we have been updated. |
| `GLMultiResolutionCubeReconstructedRaster( GLRenderer &renderer, const GLMultiResolutionStaticPolygonReconstructedRaster::non_null_ptr_type &source_reconstructed_raster, bool cache_tile_textures)` | constructor | `None` | private | Constructor. |
| `update_tile_texel_dimension( GLRenderer &renderer, unsigned int tile_texel_dimension)` | method | `unsigned int` | private | — |
| `get_tile_texture( GLRenderer &renderer, const CubeQuadTreeNode &tile, cache_handle_type &cache_handle)` | method | `boost::optional<GLTexture::shared_ptr_to_const_type>` | private | — |
| `render_raster_data_into_tile_texture( GLRenderer &renderer, const CubeQuadTreeNode &tile, TileTexture &tile_texture)` | method | `bool` | private | — |
| `get_level_of_detail( unsigned int quad_tree_depth)` | method | `float` | private | — |
| `create_tile_texture( GLRenderer &renderer, const GLTexture::shared_ptr_type &tile_texture)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `MIN_TILE_TEXEL_DIMENSION` | variable | `unsigned int` | — |
| `GPLATES_OPENGL_GLMULTIRESOLUTIONCUBERECONSTRUCTEDRASTER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLMultiResolutionCubeReconstructedRaster tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLVisualLayers](GLVisualLayers.md) | opengl | 22 |
| [app-logic/RasterLayerProxy](../app-logic/RasterLayerProxy.md) | app-logic | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLMultiResolutionCubeReconstructedRaster.h
python scripts/gpq.py def GPlatesOpenGL::GLMultiResolutionCubeReconstructedRaster --body
python scripts/gpq.py uses GLMultiResolutionCubeReconstructedRaster --kind class
python scripts/gpq.py hier GLMultiResolutionCubeReconstructedRaster
```
