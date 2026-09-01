# GLMultiResolutionCubeRasterInterface

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 843 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLMultiResolutionCubeRasterInterface.h` | C++ | 253 |

## Overview

[[[PROSE overview unit=opengl/GLMultiResolutionCubeRasterInterface tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=opengl/GLMultiResolutionCubeRasterInterface tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
