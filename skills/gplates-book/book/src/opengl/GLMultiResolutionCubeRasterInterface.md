# GLMultiResolutionCubeRasterInterface

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 843 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLMultiResolutionCubeRasterInterface.h` | C++ | 253 |

## Overview

`GLMultiResolutionCubeRasterInterface` is the common interface for anything that presents raster data as a cube-map quad tree of texture tiles, so that consumers of a cube raster (map view, reconstructed-raster rendering, `GLVisualLayers`) do not need to know whether the tiles come from a plain `GLMultiResolutionCubeRaster` or from a reconstructed source such as `GLMultiResolutionCubeReconstructedRaster`. Traversal happens through the nested `QuadTreeNode`, a value type that forwards to a polymorphic `ImplInterface` supplied by whichever concrete raster created it — `is_leaf_node()` reports whether the requested resolution has been reached, and `get_tile_texture()` returns the tile's texture, rendering it on demand if it is not already cached.

`set_world_transform()` repositions the raster within the cube map — its main use is aligning the cube map to the central meridian of a 2D map projection — and invalidates any cached tile textures and, for some implementations, the previously obtained quad tree nodes themselves; callers are expected to restart traversal from `get_quad_tree_root_node()` after calling it rather than continuing an in-progress walk.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLMultiResolutionCubeRasterInterface`](#gplatesopenglglmultiresolutioncuberasterinterface) | class | [`GPlatesUtils::ReferenceCount<GLMultiResolutionCubeRasterInterface>`](../utils/ReferenceCount.md) | — | 2 | Interface for any raster data in a multi-resolution cube map. |

## Members

### `GPlatesOpenGL::GLMultiResolutionCubeRasterInterface`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLMultiResolutionCubeRasterInterface>` | public | A convenience typedef for a shared pointer to a non-const GLMultiResolutionCubeRasterInterface. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLMultiResolutionCubeRasterInterface>` | public | A convenience typedef for a shared pointer to a const GLMultiResolutionCubeRasterInterface. |
| `cache_handle_type` | typedef | `boost::shared_ptr<void>` | public | Typedef for an opaque object that caches a particular tile of this raster. |
| `QuadTreeNode` | class | `None` | public | Used during traversal of the raster cube quad tree to obtain quad tree node texture tiles. |
| `quad_tree_node_type` | typedef | `QuadTreeNode` | public | Typedef for a quad tree node. |
| `~GLMultiResolutionCubeRasterInterface()` | destructor | `None` | public | — |
| `get_world_transform` | field | `GLMatrix` | public | Gets the transform that is applied to raster/geometries when rendering into the cube map. |
| `set_world_transform( const GLMatrix &world_transform)` | method | `void` | public | Sets the transform to apply to raster/geometries when rendering into the cube map. |
| `get_subject_token` | field | `GPlatesUtils::SubjectToken` | public | Returns a subject token that clients can observe to see if they need to update themselves (such as any cached data we render for them) by getting us to re-render. |
| `get_quad_tree_root_node( GPlatesMaths::CubeCoordinateFrame::CubeFaceType cube_face)` | method | `boost::optional<quad_tree_node_type>` | public | Returns the quad tree root node of the specified cube face. |
| `get_child_node( const quad_tree_node_type &parent_node, unsigned int child_x_offset, unsigned int child_y_offset)` | method | `boost::optional<quad_tree_node_type>` | public | Returns the specified child cube quad tree node of specified parent node. |
| `get_tile_texel_dimension()` | method | `unsigned int` | public | Returns the tile texel dimension passed into constructor. |
| `get_tile_texture_internal_format()` | method | `GLint` | public | Returns the texture internal format that can be used if rendering to a texture as opposed to the main framebuffer. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLMULTIRESOLUTIONCUBERASTERINTERFACE_H` | macro | `None` | — |

## Notes

A texture returned by `get_tile_texture()` uses nearest-neighbour filtering when it is a floating-point texture, because older hardware that supports floating-point textures cannot filter them in fixed-function sampling; callers needing smooth sampling must emulate bilinear filtering themselves in a fragment shader. Calling `set_world_transform()` mid-traversal is unsafe for implementations (such as `GLMultiResolutionCubeRaster`) that invalidate outstanding `QuadTreeNode`s on a transform change; restart traversal from the root afterwards. Some derived classes have no leaf nodes and `is_leaf_node()` always returns `false` for them.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLMultiResolutionRasterMapView](GLMultiResolutionRasterMapView.md) | opengl | 22 |
| [opengl/GLMultiResolutionCubeRaster](GLMultiResolutionCubeRaster.md) | opengl | 9 |
| [app-logic/RasterLayerProxy](../app-logic/RasterLayerProxy.md) | app-logic | 8 |
| [opengl/GLMultiResolutionCubeReconstructedRaster](GLMultiResolutionCubeReconstructedRaster.md) | opengl | 4 |
| [opengl/GLVisualLayers](GLVisualLayers.md) | opengl | 3 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLMultiResolutionCubeRasterInterface.h
python scripts/gpq.py def GPlatesOpenGL::GLMultiResolutionCubeRasterInterface --body
python scripts/gpq.py uses GLMultiResolutionCubeRasterInterface --kind class
python scripts/gpq.py hier GLMultiResolutionCubeRasterInterface
```
