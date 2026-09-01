# GLMultiResolutionMapCubeMesh

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 154 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLMultiResolutionMapCubeMesh.h` | C++ | 482 |
| `src/opengl/GLMultiResolutionMapCubeMesh.cc` | C++ | 905 |

## Overview

[[[PROSE overview unit=opengl/GLMultiResolutionMapCubeMesh tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLMultiResolutionMapCubeMesh`](#gplatesopenglglmultiresolutionmapcubemesh) | class | [`GPlatesUtils::ReferenceCount<GLMultiResolutionMapCubeMesh>`](../utils/ReferenceCount.md) | — | 0 | A mesh, projected on a 2D map, that is gridded along the cube subdivision tiles. |

## Members

### `GPlatesOpenGL::GLMultiResolutionMapCubeMesh`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AABB` | struct | `None` | private | A 2D axis-aligned bounding box to bound the map-projected coordinates. |
| `MeshDrawable` | struct | `None` | private | Information needed to render a quad tree node mesh. |
| `MeshQuadTreeNode` | struct | `None` | private | Stores mesh information for a cube quad tree node. |
| `mesh_cube_quad_tree_type` | typedef | `GPlatesMaths::CubeQuadTree<MeshQuadTreeNode>` | private | Typedef for a cube quad tree with nodes containing the type MeshQuadTreeNode. |
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLMultiResolutionMapCubeMesh>` | public | A convenience typedef for a shared pointer to a non-const GLMultiResolutionMapCubeMesh. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLMultiResolutionMapCubeMesh>` | public | A convenience typedef for a shared pointer to a const GLMultiResolutionMapCubeMesh. |
| `QuadTreeNode` | class | `None` | public | Used during traversal of the mesh cube quad tree to obtain quad tree node meshes. |
| `quad_tree_node_type` | typedef | `QuadTreeNode` | public | Typedef for a quad tree node. |
| `create( GLRenderer &renderer, const GPlatesGui::MapProjection &map_projection)` | method | `non_null_ptr_type` | public | Creates a GLMultiResolutionMapCubeMesh object. |
| `update_map_projection( GLRenderer &renderer, const GPlatesGui::MapProjection &map_projection)` | method | `bool` | public | Updates the internal mesh if the specified map projection differs from the previous one. |
| `get_quad_tree_root_node( GPlatesMaths::CubeCoordinateFrame::CubeFaceType cube_face)` | method | `QuadTreeNode` | public | Returns the quad tree root node. |
| `get_child_node( const QuadTreeNode &parent_node, unsigned int child_x_offset, unsigned int child_y_offset)` | method | `QuadTreeNode` | public | Returns the child node of specified parent node. |
| `get_clip_texture()` | method | `GLTexture::shared_ptr_type` | public | Returns the clip texture to use for texture clipping when needed. |
| `get_clip_texture_clip_space_to_texture_space_transform()` | method | `GLMatrix` | public | Returns the matrix that transforms clip-space \[-1, 1\] to the appropriate texture coordinates in the clip texture \[0.25, 0.75\]. |
| `get_tile_texture_clip_space_to_texture_space_transform()` | method | `GLMatrix` | public | Returns the matrix that transforms clip-space \[-1, 1\] to the appropriate texture coordinates in the tile texture \[0, 1\]. |
| `vertex_element_type` | typedef | `GLuint` | private | Typedef for the vertex indices - 32-bit since we're likely to exceed 65536 vertices (16-bit). |
| `MESH_CUBE_QUAD_TREE_MAXIMUM_DEPTH` | field | `unsigned int` | private | The maximum depth of the meshes cube quad tree. |
| `CUBE_FACE_DIMENSION` | field | `unsigned int` | private | The dimension of a cube face in terms of vertex spacings. |
| `NUM_MESH_VERTICES_PER_CUBE_FACE_SIDE` | field | `unsigned int` | private | The number of mesh vertices across the length of a cube face. |
| `CUBE_FACE_QUADRANT_DIMENSION` | field | `unsigned int` | private | The dimension of a cube face \*quadrant\* in terms of vertex spacings. |
| `NUM_MESH_VERTICES_PER_CUBE_FACE_QUADRANT_SIDE` | field | `unsigned int` | private | The number of mesh vertices across the length of a cube face \*quadrant\*. |
| `d_xy_clip_texture` | field | `GLTexture::shared_ptr_type` | private | Texture used to clip parts of a mesh that hang over a tile (in the cube face x/y plane). |
| `d_meshes_vertex_array` | field | `GLVertexArray::shared_ptr_type` | private | All mesh drawables within a cube face share a single vertex array. |
| `d_mesh_cube_quad_tree` | field | `mesh_cube_quad_tree_type::non_null_ptr_type` | private | The cube quad tree containing mesh drawables for the quad tree node tiles. |
| `d_map_projection_settings` | field | `GPlatesGui::MapProjectionSettings` | private | The settings of the most recent map projection (used to generate internal mesh). |
| `GLMultiResolutionMapCubeMesh( GLRenderer &renderer, const GPlatesGui::MapProjection &map_projection)` | constructor | `None` | private | Constructor. |
| `create_mesh( GLRenderer &renderer, const GPlatesGui::MapProjection &map_projection)` | method | `void` | private | — |
| `create_cube_face_mesh( GLRenderer &renderer, GPlatesMaths::CubeCoordinateFrame::CubeFaceType cube_face, const GLMapCubeMeshGenerator &map_cube_mesh_generator)` | method | `mesh_cube_quad_tree_type::node_type::ptr_type` | private | — |
| `create_cube_face_quad_tree_mesh( std::vector<GLTexture3DVertex> &mesh_vertices, std::vector<vertex_element_type> &mesh_indices, AABB &parent_node_bounding_box, double &parent_max_quad_size_in_map_projection, const std::vector<GLMapCubeMeshGenerator::Point> &cube_face_quadrant_mesh_vertices, const unsigned int cube_face ...` | method | `mesh_cube_quad_tree_type::node_type::ptr_type` | private | — |
| `create_cube_face_quad_tree_mesh_vertices( std::vector<GLTexture3DVertex> &mesh_vertices, std::vector<vertex_element_type> &mesh_indices, AABB &node_bounding_box, double &max_quad_size_in_map_projection, const std::vector<GLMapCubeMeshGenerator::Point> &cube_face_quadrant_mesh_vertices, const unsigned int cube_face_quad ...` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `DISABLE_GCC_WARNING` | variable | `PUSH_GCC_WARNINGS` | for boost assert |
| `GPLATES_OPENGL_GLMULTIRESOLUTIONMAPCUBEMESH_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLMultiResolutionMapCubeMesh tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLMultiResolutionRasterMapView](GLMultiResolutionRasterMapView.md) | opengl | 10 |
| [opengl/GLVisualLayers](GLVisualLayers.md) | opengl | 9 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 6 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLMultiResolutionMapCubeMesh.h
python scripts/gpq.py def GPlatesOpenGL::GLMultiResolutionMapCubeMesh --body
python scripts/gpq.py uses GLMultiResolutionMapCubeMesh --kind class
python scripts/gpq.py hier GLMultiResolutionMapCubeMesh
```
