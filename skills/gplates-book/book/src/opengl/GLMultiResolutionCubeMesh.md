# GLMultiResolutionCubeMesh

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 171 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLMultiResolutionCubeMesh.h` | C++ | 357 |
| `src/opengl/GLMultiResolutionCubeMesh.cc` | C++ | 387 |

## Overview

`GLMultiResolutionCubeMesh` pre-generates the vertex meshes used to draw the tiles of a cube-map quad tree (the same subdivision scheme used by `GLMultiResolutionCubeRaster` and the reconstructed-raster pipeline). Rather than tessellating each tile's geometry on the fly, it builds a `mesh_cube_quad_tree_type` (a `GPlatesMaths::CubeQuadTree` of `MeshQuadTreeNode`) down to `MESH_CUBE_QUAD_TREE_MAXIMUM_DEPTH`, and callers walk it with `QuadTreeNode` handles obtained from `get_quad_tree_root_node()` and `get_child_node()`.

The mesh depth is capped well below what a 16-bit vertex index could address (depth 5 rather than the theoretical maximum of 7) to keep the pre-built vertex arrays small. Below that depth a `QuadTreeNode` maps exactly onto a tile; once traversal goes deeper than the pre-generated tree, the same coarsest mesh is reused for every descendant tile and a clip texture (`get_clip_texture()`, `get_clip_texture_clip_space_transform()`) masks the mesh down to the requested tile's sub-area instead of generating new geometry.

The header notes that mesh drawables were previously captured as `GLCompiledDrawState` objects, but that consumed too much memory (~150Mb at depth 6, since each `GLState` costs a few Kb and there can be ~32,000 of them); the current design stores the raw draw parameters in `MeshDrawable` and issues the draw call directly in `QuadTreeNode::render_mesh_drawable()`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLMultiResolutionCubeMesh`](#gplatesopenglglmultiresolutioncubemesh) | class | [`GPlatesUtils::ReferenceCount<GLMultiResolutionCubeMesh>`](../utils/ReferenceCount.md) | — | 0 | A mesh that is gridded along the cube subdivision tiles. |

## Members

### `GPlatesOpenGL::GLMultiResolutionCubeMesh`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MeshDrawable` | struct | `None` | private | Information needed to render a quad tree node mesh. |
| `MeshQuadTreeNode` | struct | `None` | private | Stores mesh information for a cube quad tree node. |
| `mesh_cube_quad_tree_type` | typedef | `GPlatesMaths::CubeQuadTree<MeshQuadTreeNode>` | private | Typedef for a cube quad tree with nodes containing the type MeshQuadTreeNode. |
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLMultiResolutionCubeMesh>` | public | A convenience typedef for a shared pointer to a non-const GLMultiResolutionCubeMesh. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLMultiResolutionCubeMesh>` | public | A convenience typedef for a shared pointer to a const GLMultiResolutionCubeMesh. |
| `QuadTreeNode` | class | `None` | public | Used during traversal of the mesh cube quad tree to obtain quad tree node meshes. |
| `quad_tree_node_type` | typedef | `QuadTreeNode` | public | Typedef for a quad tree node. |
| `create( GLRenderer &renderer)` | method | `non_null_ptr_type` | public | Creates a GLMultiResolutionCubeMesh object. |
| `get_quad_tree_root_node( GPlatesMaths::CubeCoordinateFrame::CubeFaceType cube_face)` | method | `QuadTreeNode` | public | Returns the quad tree root node. |
| `get_child_node( const QuadTreeNode &parent_node, unsigned int child_x_offset, unsigned int child_y_offset)` | method | `QuadTreeNode` | public | Returns the child node of specified parent node. |
| `get_clip_texture()` | method | `GLTexture::shared_ptr_type` | public | Returns the clip texture to use for texture clipping when needed. |
| `get_clip_texture_clip_space_to_texture_space_transform()` | method | `GLMatrix` | public | Returns the matrix that transforms clip-space \[-1, 1\] to the appropriate texture coordinates in the clip texture \[0.25, 0.75\]. |
| `get_tile_texture_clip_space_to_texture_space_transform()` | method | `GLMatrix` | public | Returns the matrix that transforms clip-space \[-1, 1\] to the appropriate texture coordinates in the tile texture \[0, 1\]. |
| `vertex_element_type` | typedef | `GLushort` | private | Typedef for the vertex indices. |
| `MESH_CUBE_QUAD_TREE_MAXIMUM_DEPTH` | field | `unsigned int` | private | The maximum depth of the meshes cube quad tree. |
| `MESH_MAXIMUM_TILES_PER_CUBE_FACE_SIDE` | field | `unsigned int` | private | The maximum number of mesh tiles across the length of a cube face. |
| `MESH_MAXIMUM_VERTICES_PER_CUBE_FACE_SIDE` | field | `unsigned int` | private | The maximum number of mesh vertices across the length of a cube face. |
| `d_xy_clip_texture` | field | `GLTexture::shared_ptr_type` | private | Texture used to clip parts of a mesh that hang over a tile (in the cube face x/y plane). |
| `d_meshes_vertex_array` | field | `GLVertexArray::shared_ptr_type` | private | All mesh drawables within a cube face share a single vertex array. |
| `d_mesh_cube_quad_tree` | field | `mesh_cube_quad_tree_type::non_null_ptr_type` | private | The cube quad tree containing mesh drawables for the quad tree node tiles. |
| `GLMultiResolutionCubeMesh( GLRenderer &renderer)` | constructor | `None` | private | Constructor. |
| `create_mesh_drawables( GLRenderer &renderer)` | method | `void` | private | — |
| `create_cube_face_vertex_and_index_array( GLRenderer &renderer, GPlatesMaths::CubeCoordinateFrame::CubeFaceType cube_face, const std::vector<GPlatesMaths::UnitVector3D> &unique_cube_face_mesh_vertices)` | method | `void` | private | — |
| `create_cube_face_vertex_and_index_array( std::vector<GLVertex> &mesh_vertices, std::vector<vertex_element_type> &mesh_indices, const std::vector<GPlatesMaths::UnitVector3D> &unique_cube_face_mesh_vertices, const GPlatesMaths::CubeQuadTreeLocation &quad_tree_node_location)` | method | `void` | private | — |
| `create_quad_tree_mesh_drawables( GLRenderer &renderer, GPlatesMaths::CubeCoordinateFrame::CubeFaceType cube_face)` | method | `void` | private | — |
| `create_quad_tree_mesh_drawables( GLRenderer &renderer, unsigned int &vertex_index, unsigned int &vertex_element_index, GPlatesMaths::CubeCoordinateFrame::CubeFaceType cube_face, unsigned int depth)` | method | `mesh_cube_quad_tree_type::node_type::ptr_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `DISABLE_GCC_WARNING` | variable | `PUSH_GCC_WARNINGS` | for boost assert |
| `GPLATES_OPENGL_GLMULTIRESOLUTIONCUBEMESH_H` | macro | `None` | — |

## Notes

All mesh drawables for a cube face share a single vertex array (`d_meshes_vertex_array`, one per cube face), so `QuadTreeNode`s only ever hold offsets into it rather than owning geometry. A `QuadTreeNode` stores a raw pointer into the underlying `mesh_cube_quad_tree_type` node (or, past the pre-generated depth, a raw pointer to the coarsest `MeshDrawable`), so it is only valid as long as the owning `GLMultiResolutionCubeMesh` is alive.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 16 |
| [opengl/GLFilledPolygonsGlobeView](GLFilledPolygonsGlobeView.md) | opengl | 10 |
| [opengl/GLVisualLayers](GLVisualLayers.md) | opengl | 9 |
| [app-logic/RasterLayerProxy](../app-logic/RasterLayerProxy.md) | app-logic | 3 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 3 |
| [gui/CommandServer](../gui/CommandServer.md) | gui | 1 |
| [opengl/GLMultiResolutionCubeReconstructedRaster](GLMultiResolutionCubeReconstructedRaster.md) | opengl | 1 |
| [qt-widgets/ImportRasterDialog](../qt-widgets/ImportRasterDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLMultiResolutionCubeMesh.h
python scripts/gpq.py def GPlatesOpenGL::GLMultiResolutionCubeMesh --body
python scripts/gpq.py uses GLMultiResolutionCubeMesh --kind class
python scripts/gpq.py hier GLMultiResolutionCubeMesh
```
