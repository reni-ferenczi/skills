# GLFilledPolygonsGlobeView

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 633 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLFilledPolygonsGlobeView.h` | C++ | 660 |
| `src/opengl/GLFilledPolygonsGlobeView.cc` | C++ | 1392 |

## Overview

[[[PROSE overview unit=opengl/GLFilledPolygonsGlobeView tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLFilledPolygonsGlobeView`](#gplatesopenglglfilledpolygonsglobeview) | class | [`GPlatesUtils::ReferenceCount<GLFilledPolygonsGlobeView>`](../utils/ReferenceCount.md) | — | 0 | A representation of (reconstructed) filled polygons (static or dynamic) that uses multi-resolution cube textures instead of polygons meshes. |

## Members

### `GPlatesOpenGL::GLFilledPolygonsGlobeView`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `drawable_vertex_element_type` | typedef | `GLuint` | private | Typedef for a vertex element (vertex index) of a drawable. |
| `drawable_vertex_type` | typedef | `GLColourVertex` | private | Typedef for a coloured vertex of a drawable. |
| `FilledDrawable` | struct | `None` | private | Contains information to render a filled drawable. |
| `filled_drawable_type` | typedef | `FilledDrawable` | private | Typedef for a filled drawable. |
| `filled_drawables_spatial_partition_type` | typedef | `GPlatesMaths::CubeQuadTreePartition<filled_drawable_type>` | private | Typedef for a spatial partition of filled drawables. |
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLFilledPolygonsGlobeView>` | public | A convenience typedef for a shared pointer to a non-const GLFilledPolygonsGlobeView. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLFilledPolygonsGlobeView>` | public | A convenience typedef for a shared pointer to a const GLFilledPolygonsGlobeView. |
| `FilledDrawables` | class | `None` | public | Used to accumulate filled drawables (optionally as a spatial partition) for rendering. |
| `filled_drawables_type` | typedef | `FilledDrawables` | public | Typedef for a group of filled drawables. |
| `create( GLRenderer &renderer, const GLMultiResolutionCubeMesh::non_null_ptr_to_const_type &multi_resolution_cube_mesh, boost::optional<GLLight::non_null_ptr_type> light = boost::none)` | method | `non_null_ptr_type` | public | Creates a GLFilledPolygonsGlobeView object. |
| `render( GLRenderer &renderer, const filled_drawables_type &filled_drawables)` | method | `void` | public | Renders the specified filled drawables (spatial partition). |
| `MAX_TILE_TEXEL_DIMENSION` | field | `int` | private | The maximum tile size for rendering filled drawables. |
| `MIN_TILE_TEXEL_DIMENSION` | field | `int` | private | The minimum tile size for rendering filled drawables. |
| `cube_subdivision_cache_type` | typedef | `GLCubeSubdivisionCache< true/*CacheProjectionTransform*/, false/*CacheLooseProjectionTransform*/, false/*CacheFrustum*/, false/*CacheLooseFrustum*/, false/*CacheBoundingPolygon*/, ...` | private | Typedef for a GLCubeSubvision cache. |
| `clip_cube_subdivision_cache_type` | typedef | `GLCubeSubdivisionCache< true/*CacheProjectionTransform*/, false/*CacheLooseProjectionTransform*/, false/*CacheFrustum*/, false/*CacheLooseFrustum*/, false/*CacheBoundingPolygon*/, ...` | private | Typedef for a GLCubeSubvision cache. |
| `mesh_quad_tree_node_type` | typedef | `GLMultiResolutionCubeMesh::quad_tree_node_type` | private | Typedef for a quad tree node of a multi-resolution cube mesh. |
| `filled_drawables_intersecting_nodes_type` | typedef | `GPlatesMaths::CubeQuadTreePartitionUtils::CubeQuadTreeIntersectingNodes< filled_drawable_type, const GPlatesMaths::CubeQuadTreePartition<filled_drawable_type> /*const*/>` | private | Typedef for a structure that determines which nodes of a spatial partition intersect a regular cube quad tree. |
| `FilledDrawablesListNode` | struct | `None` | private | A linked list node that references a spatial partition node of filled drawables. |
| `filled_drawables_spatial_partition_node_list_type` | typedef | `GPlatesUtils::IntrusiveSinglyLinkedList<FilledDrawablesListNode>` | private | Typedef for a list of spatial partition nodes referencing reconstructed filled drawables. |
| `filled_drawable_seq_type` | typedef | `std::vector<filled_drawable_type>` | private | Typedef for a sequence of filled drawables. |
| `d_max_tile_texel_dimension` | field | `unsigned int` | private | The maximum texture dimension of a cube quad tree tile. |
| `d_min_tile_texel_dimension` | field | `unsigned int` | private | The minimum texture dimension of a cube quad tree tile. |
| `d_drawables_vertex_buffer` | field | `GLVertexBuffer::shared_ptr_type` | private | The vertex buffer containing the vertices of all drawables of the current render call. |
| `d_drawables_vertex_element_buffer` | field | `GLVertexElementBuffer::shared_ptr_type` | private | The vertex buffer containing the vertex elements (indices) of all drawables of the current render call. |
| `d_drawables_vertex_array` | field | `GLVertexArray::shared_ptr_type` | private | The vertex array containing all drawables of the current render call. |
| `d_multi_resolution_cube_mesh` | field | `GLMultiResolutionCubeMesh::non_null_ptr_to_const_type` | private | Contains meshes for each cube quad tree node. |
| `d_light` | field | `boost::optional<GLLight::non_null_ptr_type>` | private | The light (direction) used during surface lighting. |
| `d_render_tile_to_scene_program_object` | field | `boost::optional<GLProgramObject::shared_ptr_type>` | private | Shader program to render tiles to the scene (the final stage). |
| `d_render_tile_to_scene_with_clipping_program_object` | field | `boost::optional<GLProgramObject::shared_ptr_type>` | private | Shader program to render tiles to the scene (the final stage) with clipping. |
| `d_render_tile_to_scene_with_lighting_program_object` | field | `boost::optional<GLProgramObject::shared_ptr_type>` | private | Shader program to render tiles to the scene (the final stage) with lighting. |
| `d_render_tile_to_scene_with_clipping_and_lighting_program_object` | field | `boost::optional<GLProgramObject::shared_ptr_type>` | private | Shader program to render tiles to the scene (the final stage) with clipping and lighting. |
| `GLFilledPolygonsGlobeView( GLRenderer &renderer, const GLMultiResolutionCubeMesh::non_null_ptr_to_const_type &multi_resolution_cube_mesh, boost::optional<GLLight::non_null_ptr_type> light)` | constructor | `None` | private | Constructor. |
| `get_level_of_detail( unsigned int &tile_texel_dimension, const GLViewport &viewport, const GLMatrix &model_view_transform, const GLMatrix &projection_transform)` | method | `unsigned int` | private | — |
| `render_quad_tree( GLRenderer &renderer, unsigned int tile_texel_dimension, const mesh_quad_tree_node_type &mesh_quad_tree_node, const filled_drawables_type &filled_drawables, const filled_drawables_spatial_partition_node_list_type &parent_filled_drawables_intersecting_node_list, const filled_drawables_intersecting_node ...` | method | `void` | private | — |
| `render_quad_tree_node( GLRenderer &renderer, unsigned int tile_texel_dimension, const mesh_quad_tree_node_type &mesh_quad_tree_node, const filled_drawables_type &filled_drawables, const filled_drawables_spatial_partition_node_list_type & parent_reconstructed_drawable_meshes_intersecting_node_list, const filled_drawable ...` | method | `void` | private | — |
| `get_filled_drawables_intersecting_nodes( const GPlatesMaths::CubeQuadTreeLocation &source_raster_tile_location, const GPlatesMaths::CubeQuadTreeLocation &intersecting_node_location, filled_drawables_spatial_partition_type::const_node_reference_type intersecting_node_reference, filled_drawables_spatial_partition_node_li ...` | method | `void` | private | — |
| `set_tile_state( GLRenderer &renderer, const GLTexture::shared_ptr_to_const_type &tile_texture, const GLTransform &projection_transform, const GLTransform &clip_projection_transform, const GLTransform &view_transform, bool clip_to_tile_frustum)` | method | `void` | private | — |
| `render_tile_to_scene( GLRenderer &renderer, unsigned int tile_texel_dimension, const mesh_quad_tree_node_type &mesh_quad_tree_node, const filled_drawables_type &filled_drawables, const filled_drawables_spatial_partition_node_list_type &filled_drawables_intersecting_node_list, cube_subdivision_cache_type &cube_subdivisi ...` | method | `void` | private | — |
| `render_filled_drawables_to_tile_texture( GLRenderer &renderer, const GLTexture::shared_ptr_to_const_type &tile_texture, const filled_drawable_seq_type &transformed_sorted_filled_drawables, const GLTransform &projection_transform, const GLTransform &view_transform)` | method | `void` | private | — |
| `get_filled_drawables( filled_drawable_seq_type &filled_drawables, filled_drawables_spatial_partition_type::element_const_iterator begin_root_filled_drawables, filled_drawables_spatial_partition_type::element_const_iterator end_root_filled_drawables, const filled_drawables_spatial_partition_node_list_type &filled_drawab ...` | method | `void` | private | — |
| `acquire_tile_texture( GLRenderer &renderer, unsigned int tile_texel_dimension)` | method | `GLTexture::shared_ptr_type` | private | — |
| `create_drawables_vertex_array( GLRenderer &renderer)` | method | `void` | private | — |
| `write_filled_drawables_to_vertex_array( GLRenderer &renderer, const filled_drawables_type &filled_drawables)` | method | `void` | private | — |
| `create_shader_programs( GLRenderer &renderer)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `INVERSE_LOG2` | variable | `float` | The inverse of log(2.0). |
| `RENDER_TILE_TO_SCENE_VERTEX_SHADER_SOURCE_FILE_NAME` | variable | `QString` | Vertex shader source code to render a tile to the scene. |
| `RENDER_TILE_TO_SCENE_FRAGMENT_SHADER_SOURCE_FILE_NAME` | variable | `QString` | Fragment shader source code to render a tile to the scene. |
| `GPLATES_OPENGL_GLFILLEDPOLYGONSGLOBEVIEW_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLFilledPolygonsGlobeView tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLVisualLayers](GLVisualLayers.md) | opengl | 32 |
| [gui/LayerPainter](../gui/LayerPainter.md) | gui | 19 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 12 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 1 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 1 |
| [qt-widgets/ProjectionControlWidget](../qt-widgets/ProjectionControlWidget.md) | qt-widgets | 1 |

## Related

**Shader programs compiled by this unit**

| Shader unit | Component |
|---|---|
| [shaders/multi_resolution_filled_polygons](../qt-resources/opengl/multi_resolution_filled_polygons.md) | shaders |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLFilledPolygonsGlobeView.h
python scripts/gpq.py def GPlatesOpenGL::GLFilledPolygonsGlobeView --body
python scripts/gpq.py uses GLFilledPolygonsGlobeView --kind class
python scripts/gpq.py hier GLFilledPolygonsGlobeView
```
