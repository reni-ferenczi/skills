# GLRasterCoRegistration

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 53 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLRasterCoRegistration.h` | C++ | 1705 |
| `src/opengl/GLRasterCoRegistration.cc` | C++ | 6114 |

## Overview

[[[PROSE overview unit=opengl/GLRasterCoRegistration tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLRasterCoRegistration`](#gplatesopenglglrastercoregistration) | class | [`GPlatesUtils::ReferenceCount<GLRasterCoRegistration>`](../utils/ReferenceCount.md) | — | 0 | Co-registers the seed (geometry) features with a (possibly reconstructed) floating-point raster. |

## Members

### `GPlatesOpenGL::GLRasterCoRegistration`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TEXTURE_DIMENSION` | field | `unsigned int` | private | The power-of-two square texture dimension to use when creating floating-point textures to render the target raster to and to render the seed geometries into. |
| `NUM_REDUCE_STAGES` | field | `unsigned int` | private | The number of reduce stages depends on the texture dimension since each texture is reduced by a (dimension) factor of two (hence the dependence on log2). |
| `ReduceStageListTag` | struct | `None` | private | Used to declare different lists types. |
| `PointListTag` | struct | `None` | private | — |
| `MultiPointListTag` | struct | `None` | private | — |
| `PolylineListTag` | struct | `None` | private | — |
| `PolygonListTag` | struct | `None` | private | — |
| `SeedCoRegistration` | struct | `None` | private | Associates a reconstructed geometry of a seed feature with the feature and an operation. |
| `seed_co_registration_reduce_stage_list_type` | typedef | `GPlatesUtils::IntrusiveSinglyLinkedList<SeedCoRegistration, ReduceStageListTag>` | private | Typedef for a list of seed co-registrations used for a reduce stage. |
| `seed_co_registration_points_list_type` | typedef | `GPlatesUtils::IntrusiveSinglyLinkedList<SeedCoRegistration, PointListTag>` | private | Typedef for a list of \*point\* seed co-registrations. |
| `seed_co_registration_multi_points_list_type` | typedef | `GPlatesUtils::IntrusiveSinglyLinkedList<SeedCoRegistration, MultiPointListTag>` | private | Typedef for a list of \*multipoint\* seed co-registrations. |
| `seed_co_registration_polylines_list_type` | typedef | `GPlatesUtils::IntrusiveSinglyLinkedList<SeedCoRegistration, PolylineListTag>` | private | Typedef for a list of \*polyline\* seed co-registrations. |
| `seed_co_registration_polygons_list_type` | typedef | `GPlatesUtils::IntrusiveSinglyLinkedList<SeedCoRegistration, PolygonListTag>` | private | Typedef for a list of \*polygon\* seed co-registrations. |
| `SeedCoRegistrationReduceStageLists` | struct | `None` | private | Used when distributing SeedCoRegistration's among reduce stages. |
| `SeedCoRegistrationGeometryLists` | struct | `None` | private | Each seed geometry can be rendered as points \[and outlines \[and fills\]\] depending on whether it's a point (or multipoint), polyline or polygon geometry. |
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLRasterCoRegistration>` | public | A convenience typedef for a shared pointer to a non-const GLRasterCoRegistration. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLRasterCoRegistration>` | public | A convenience typedef for a shared pointer to a const GLRasterCoRegistration. |
| `OperationType` | enum | `None` | public | How the raster pixels in the region-of-interest of geometries are combined into a single value. |
| `Operation` | class | `None` | public | Specifies the type of operation and region-of-interest and contains co-registration results. |
| `is_supported( GLRenderer &renderer)` | method | `bool` | public | Returns true if raster co-registration is supported on the runtime system. |
| `create( GLRenderer &renderer)` | method | `boost::optional<non_null_ptr_type>` | public | Creates a GLRasterCoRegistration that co-registers the specified seed (geometry) features with the specified (possibly reconstructed) floating-point raster. raster\_level\_of\_detail is the level-of-detail at which to process the target ... |
| `co_register( GLRenderer &renderer, std::vector<Operation> &operations, const std::vector<GPlatesAppLogic::ReconstructContext::ReconstructedFeature> &reconstructed_seed_features, const GLMultiResolutionRasterInterface::non_null_ptr_type &reconstructed_target_raster, unsigned int raster_level_of_detail)` | method | `void` | public | For each specified operation the specified (reconstructed) seed features and (possibly reconstructed) floating-point target raster are co-registered. |
| `MINIMUM_SEED_GEOMETRIES_VIEWPORT_DIMENSION` | field | `unsigned int` | private | The minimum viewport size to render seed geometries into. |
| `NUM_REDUCE_VERTEX_ARRAY_QUADS_ACROSS_TEXTURE` | field | `unsigned int` | private | The number of quad primitives (in the reduce vertex array) lined up along either horizontal or vertical side of texture. |
| `NUM_BYTES_IN_STREAMING_VERTEX_BUFFER` | field | `unsigned int` | private | The number of bytes in the vertex buffer used to stream. |
| `MINIMUM_BYTES_TO_STREAM_IN_VERTEX_BUFFER` | field | `unsigned int` | private | The minimum number of bytes to stream in the vertex buffer. |
| `NUM_BYTES_IN_STREAMING_VERTEX_ELEMENT_BUFFER` | field | `unsigned int` | private | The number of bytes in the vertex element (indices) buffer used to stream. |
| `MINIMUM_BYTES_TO_STREAM_IN_VERTEX_ELEMENT_BUFFER` | field | `unsigned int` | private | The minimum number of bytes to stream in the vertex element buffer. |
| `cube_subdivision_cache_type` | typedef | `GLCubeSubdivisionCache< true/*CacheProjectionTransform*/, true/*CacheLooseProjectionTransform*/, false/*CacheFrustum*/, false/*CacheLooseFrustum*/, false/*CacheBoundingPolygon*/, f ...` | private | Typedef for a GLCubeSubvision cache. |
| `seed_geometries_spatial_partition_type` | typedef | `GPlatesMaths::CubeQuadTreePartition<SeedCoRegistration>` | private | Typedef for a spatial partition of reconstructed seed co-registrations whose geometry bounding small circle have been expanded by a region-of-interest radius. |
| `seed_geometries_intersecting_nodes_type` | typedef | `GPlatesMaths::CubeQuadTreePartitionUtils::CubeQuadTreeIntersectingNodes< SeedCoRegistration, GPlatesMaths::CubeQuadTreePartition<SeedCoRegistration> /*non-const*/ >` | private | Typedef for a structure that determines which nodes of a seed spatial partition intersect a regular cube quad tree. |
| `reduction_vertex_element_type` | typedef | `GLuint` | private | Typedef for vertex elements (indices) used in reduction vertex array. |
| `streaming_vertex_element_type` | typedef | `GLuint` | private | Typedef for vertex elements (indices) used for streaming vertex array. |
| `PointRegionOfInterestVertex` | struct | `None` | private | A vertex of the region-of-interest geometry around a point. |
| `point_region_of_interest_stream_primitives_type` | typedef | `GLStaticStreamPrimitives<PointRegionOfInterestVertex, streaming_vertex_element_type>` | private | Typedef for a static stream of seed geometry point vertices. |
| `LineRegionOfInterestVertex` | struct | `None` | private | A vertex of the region-of-interest geometry around a line (great circle arc). |
| `line_region_of_interest_stream_primitives_type` | typedef | `GLStaticStreamPrimitives<LineRegionOfInterestVertex, streaming_vertex_element_type>` | private | Typedef for a static stream of seed geometry line (GCA) vertices. |
| `FillRegionOfInterestVertex` | struct | `None` | private | A vertex of the region-of-interest geometry of a fill (polygon interior). |
| `fill_region_of_interest_stream_primitives_type` | typedef | `GLStaticStreamPrimitives<FillRegionOfInterestVertex, streaming_vertex_element_type>` | private | Typedef for a static stream of seed geometry fill (polygon) vertices. |
| `MaskRegionOfInterestVertex` | struct | `None` | private | A vertex of a quad used to mask target raster with region-of-interest texture. |
| `mask_region_of_interest_stream_primitives_type` | typedef | `GLStaticStreamPrimitives<MaskRegionOfInterestVertex, streaming_vertex_element_type>` | private | Typedef for a static stream of quads used to mask target raster with region-of-interest texture. |
| `SeedGeometriesNodeListNode` | struct | `None` | private | A linked list node that references a spatial partition node of reconstructed seed geometries. |
| `seed_geometries_spatial_partition_node_list_type` | typedef | `GPlatesUtils::IntrusiveSinglyLinkedList<SeedGeometriesNodeListNode>` | private | Typedef for a list of spatial partition nodes referencing reconstructed seed geometries. |
| `AddSeedCoRegistrationToGeometryLists` | class | `None` | private | Adds a SeedCoRegistration object to a list depending on associated its GeometryOnSphere type. |
| `ResultPixel` | struct | `None` | private | A single 'GL\_RGBA32F\_ARB' pixel containing the result of an operation. |
| `SeedCoRegistrationPartialResult` | struct | `None` | private | Contains a single co-registration result. |
| `seed_co_registration_partial_result_list_type` | typedef | `GPlatesUtils::IntrusiveSinglyLinkedList<SeedCoRegistrationPartialResult>` | private | Typedef for a list of SeedCoRegistrationPartialResult objects. |
| `OperationSeedFeaturePartialResults` | struct | `None` | private | Stores (potentially partial) seed co-registration results for seed features (for an operation). |
| `ReduceQuadTreeNode` | class | `None` | private | Base class for a node in a quad tree used during the reduce stage to track a seed geometry co-registration as it gets reduced across reduce textures to eventually become a single scalar value. |
| `ReduceQuadTreeLeafNode` | class | `None` | private | A leaf reduce quad tree node. |
| `ReduceQuadTreeInternalNode` | class | `None` | private | An internal reduce quad tree node. |
| `ReduceQuadTree` | class | `None` | private | A quad tree used during the reduce stage to track seed geometry co-registrations as they get reduced across reduce textures to eventually become single scalar values. |
| `ResultsQueue` | class | `None` | private | Manages queuing and asynchronous read back of result texture data from GPU to CPU. |
| `RenderSeedCoRegistrationParameters` | struct | `None` | private | Parameters used when rendering seed co-registrations during reduce quad tree traversal. |
| `CoRegistrationParameters` | struct | `None` | private | Parameters used when co-registering a raster with reconstructed seed geometries. |
| `d_framebuffer_object` | field | `GLFrameBufferObject::shared_ptr_type` | private | Used to render to floating-point textures. |
| `d_streaming_vertex_element_buffer` | field | `GLVertexElementBuffer::shared_ptr_type` | private | Used to stream indices (vertex elements) such as region-of-interest geometries. |
| `d_streaming_vertex_buffer` | field | `GLVertexBuffer::shared_ptr_type` | private | Used to stream vertices such as region-of-interest geometries. |
| `d_point_region_of_interest_vertex_array` | field | `GLVertexArray::shared_ptr_type` | private | Used to contain \*point\* region-of-interest geometries. |
| `d_line_region_of_interest_vertex_array` | field | `GLVertexArray::shared_ptr_type` | private | Used to contain \*line\* (great circle arc) region-of-interest geometries. |
| `d_fill_region_of_interest_vertex_array` | field | `GLVertexArray::shared_ptr_type` | private | Used to contain \*fill\* (polygon-interior) region-of-interest geometries. |
| `d_mask_region_of_interest_vertex_array` | field | `GLVertexArray::shared_ptr_type` | private | Contains quads used to mask target raster with region-of-interest texture. |
| `d_reduction_vertex_array` | field | `GLVertexArray::shared_ptr_type` | private | Used to reduce (by 2x2 -\> 1x1) region-of-interest filter results. |
| `d_render_points_of_seed_geometries_with_small_roi_angle_program_object` | field | `GLProgramObject::shared_ptr_type` | private | Shader program to render point regions-of-interest for seed geometries with small region-of-interest angles. |
| `d_render_points_of_seed_geometries_with_large_roi_angle_program_object` | field | `GLProgramObject::shared_ptr_type` | private | Shader program to render point regions-of-interest for seed geometries with large region-of-interest angles. |
| `d_render_lines_of_seed_geometries_with_small_roi_angle_program_object` | field | `GLProgramObject::shared_ptr_type` | private | Shader program to render line (great circle arc) regions-of-interest for seed geometries with small region-of-interest angles. |
| `d_render_lines_of_seed_geometries_with_large_roi_angle_program_object` | field | `GLProgramObject::shared_ptr_type` | private | Shader program to render line (great circle arc) regions-of-interest for seed geometries with large region-of-interest angles. |
| `d_render_fill_of_seed_geometries_program_object` | field | `GLProgramObject::shared_ptr_type` | private | Shader program to render fill (polygon-interior) regions-of-interest. |
| `d_mask_region_of_interest_moments_program_object` | field | `GLProgramObject::shared_ptr_type` | private | Shader program to copy target raster into seed sub-viewport with region-of-interest masking. |
| `d_mask_region_of_interest_minmax_program_object` | field | `GLProgramObject::shared_ptr_type` | private | Shader program to copy target raster into seed sub-viewport with region-of-interest masking. |
| `d_reduction_sum_program_object` | field | `GLProgramObject::shared_ptr_type` | private | Shader program to reduce by calculating \*sum\* of regions-of-interest filter results. |
| `d_reduction_min_program_object` | field | `GLProgramObject::shared_ptr_type` | private | Shader program to reduce by calculating \*minimum\* of regions-of-interest filter results. |
| `d_reduction_max_program_object` | field | `GLProgramObject::shared_ptr_type` | private | Shader program to reduce by calculating \*maximum\* of regions-of-interest filter results. |
| `d_identity_quaternion` | field | `GPlatesMaths::UnitQuaternion3D` | private | Simplifies some code since seed geometry can reference identity quaternion if has no finite rotation. |
| `d_debug_pixel_buffer` | field | `GLPixelBuffer::shared_ptr_type` | private | — |
| `GLRasterCoRegistration( GLRenderer &renderer)` | constructor | `None` | private | — |
| `initialise_vertex_arrays_and_shader_programs( GLRenderer &renderer)` | method | `void` | private | — |
| `initialise_point_region_of_interest_shader_programs( GLRenderer &renderer)` | method | `void` | private | — |
| `initialise_line_region_of_interest_shader_program( GLRenderer &renderer)` | method | `void` | private | — |
| `initialise_fill_region_of_interest_shader_program( GLRenderer &renderer)` | method | `void` | private | — |
| `initialise_mask_region_of_interest_shader_program( GLRenderer &renderer)` | method | `void` | private | — |
| `create_region_of_interest_shader_program( GLRenderer &renderer, const char *vertex_shader_defines, const char *fragment_shader_defines)` | method | `GLProgramObject::shared_ptr_type` | private | — |
| `initialise_reduction_of_region_of_interest_shader_programs( GLRenderer &renderer)` | method | `void` | private | — |
| `initialise_reduction_of_region_of_interest_vertex_array( GLRenderer &renderer)` | method | `void` | private | — |
| `initialise_reduction_vertex_array_in_quad_tree_traversal_order( std::vector<GLTextureVertex> &vertices, std::vector<reduction_vertex_element_type> &vertex_elements, unsigned int x_quad_offset, unsigned int y_quad_offset, unsigned int width_in_quads)` | method | `void` | private | — |
| `initialise_texture_level_of_detail_parameters( GLRenderer &renderer, const GLMultiResolutionRasterInterface::non_null_ptr_type &target_raster, const unsigned int raster_level_of_detail, unsigned int &raster_texture_cube_quad_tree_depth, unsigned int &seed_geometries_spatial_partition_depth)` | method | `void` | private | — |
| `create_reconstructed_seed_geometries_spatial_partition( std::vector<Operation> &operations, const std::vector<GPlatesAppLogic::ReconstructContext::ReconstructedFeature> &seed_features, const unsigned int seed_geometries_spatial_partition_depth)` | method | `seed_geometries_spatial_partition_type::non_null_ptr_type` | private | — |
| `filter_reduce_seed_geometries_spatial_partition( GLRenderer &renderer, const CoRegistrationParameters &co_registration_parameters)` | method | `void` | private | — |
| `filter_reduce_seed_geometries( GLRenderer &renderer, const CoRegistrationParameters &co_registration_parameters, seed_geometries_spatial_partition_type::node_reference_type seed_geometries_spatial_partition_node, const seed_geometries_spatial_partition_node_list_type &parent_seed_geometries_intersecting_node_list, cons ...` | method | `void` | private | — |
| `co_register_seed_geometries( GLRenderer &renderer, const CoRegistrationParameters &co_registration_parameters, seed_geometries_spatial_partition_type::node_reference_type seed_geometries_spatial_partition_node, const seed_geometries_spatial_partition_node_list_type &parent_seed_geometries_intersecting_node_list, const ...` | method | `void` | private | — |
| `co_register_seed_geometries_with_target_raster( GLRenderer &renderer, const CoRegistrationParameters &co_registration_parameters, const seed_geometries_spatial_partition_node_list_type &parent_seed_geometries_intersecting_node_list, const seed_geometries_intersecting_nodes_type &seed_geometries_intersecting_nodes, cube ...` | method | `void` | private | — |
| `co_register_seed_geometries_with_target_raster( GLRenderer &renderer, const CoRegistrationParameters &co_registration_parameters, const seed_geometries_spatial_partition_node_list_type &seed_geometries_intersecting_node_list, const GPlatesMaths::UnitVector3D &cube_face_centre, const GLTransform::non_null_ptr_to_const_t ...` | method | `void` | private | — |
| `group_seed_co_registrations_by_operation_to_reduce_stage_zero( std::vector<SeedCoRegistrationReduceStageLists> &operations_reduce_stage_lists, seed_geometries_spatial_partition_type &seed_geometries_spatial_partition, const seed_geometries_spatial_partition_node_list_type &seed_geometries_intersecting_node_list)` | method | `void` | private | — |
| `co_register_seed_geometries_with_loose_target_raster( GLRenderer &renderer, const CoRegistrationParameters &co_registration_parameters, seed_geometries_spatial_partition_type::node_reference_type seed_geometries_spatial_partition_node, cube_subdivision_cache_type &cube_subdivision_cache, const cube_subdivision_cache_ty ...` | method | `void` | private | — |
| `group_seed_co_registrations_by_operation( const CoRegistrationParameters &co_registration_parameters, std::vector<SeedCoRegistrationReduceStageLists> &operations_reduce_stage_lists, seed_geometries_spatial_partition_type::node_reference_type seed_geometries_spatial_partition_node, const GLUtils::QuadTreeClipSpaceTransf ...` | method | `void` | private | — |
| `render_seed_geometries_to_reduce_pyramids( GLRenderer &renderer, const CoRegistrationParameters &co_registration_parameters, unsigned int operation_index, const GPlatesMaths::UnitVector3D &cube_face_centre, const GLTexture::shared_ptr_type &target_raster_texture, const GLTransform::non_null_ptr_to_const_type &target_ra ...` | method | `void` | private | — |
| `render_seed_geometries_to_reduce_quad_tree_internal_node( GLRenderer &renderer, RenderSeedCoRegistrationParameters &render_params, ReduceQuadTreeInternalNode &reduce_quad_tree_internal_node)` | method | `unsigned int` | private | — |
| `render_seed_geometries_in_reduce_stage_render_list( GLRenderer &renderer, const GLTexture::shared_ptr_type &reduce_stage_texture, bool clear_reduce_stage_texture, const Operation &operation, const GPlatesMaths::UnitVector3D &cube_face_centre, const GLTexture::shared_ptr_type &target_raster_texture, const GLTransform::n ...` | method | `void` | private | — |
| `render_bounded_point_region_of_interest_geometries( GLRenderer &renderer, GLBuffer::MapBufferScope &map_vertex_element_buffer_scope, GLBuffer::MapBufferScope &map_vertex_buffer_scope, const SeedCoRegistrationGeometryLists &geometry_lists, const double &region_of_interest_radius)` | method | `void` | private | — |
| `render_bounded_point_region_of_interest_geometry( GLRenderer &renderer, GLBuffer::MapBufferScope &map_vertex_element_buffer_scope, GLBuffer::MapBufferScope &map_vertex_buffer_scope, point_region_of_interest_stream_primitives_type::StreamTarget &point_stream_target, point_region_of_interest_stream_primitives_type::Primi ...` | method | `void` | private | — |
| `render_unbounded_point_region_of_interest_geometries( GLRenderer &renderer, GLBuffer::MapBufferScope &map_vertex_element_buffer_scope, GLBuffer::MapBufferScope &map_vertex_buffer_scope, const SeedCoRegistrationGeometryLists &geometry_lists, const double &region_of_interest_radius)` | method | `void` | private | — |
| `render_unbounded_point_region_of_interest_geometry( GLRenderer &renderer, GLBuffer::MapBufferScope &map_vertex_element_buffer_scope, GLBuffer::MapBufferScope &map_vertex_buffer_scope, point_region_of_interest_stream_primitives_type::StreamTarget &point_stream_target, point_region_of_interest_stream_primitives_type::Pri ...` | method | `void` | private | — |
| `render_bounded_line_region_of_interest_geometries( GLRenderer &renderer, GLBuffer::MapBufferScope &map_vertex_element_buffer_scope, GLBuffer::MapBufferScope &map_vertex_buffer_scope, const SeedCoRegistrationGeometryLists &geometry_lists, const double &region_of_interest_radius)` | method | `void` | private | — |
| `render_bounded_line_region_of_interest_geometry( GLRenderer &renderer, GLBuffer::MapBufferScope &map_vertex_element_buffer_scope, GLBuffer::MapBufferScope &map_vertex_buffer_scope, line_region_of_interest_stream_primitives_type::StreamTarget &line_stream_target, line_region_of_interest_stream_primitives_type::Primitive ...` | method | `void` | private | — |
| `render_unbounded_line_region_of_interest_geometries( GLRenderer &renderer, GLBuffer::MapBufferScope &map_vertex_element_buffer_scope, GLBuffer::MapBufferScope &map_vertex_buffer_scope, const SeedCoRegistrationGeometryLists &geometry_lists, const double &region_of_interest_radius)` | method | `void` | private | — |
| `render_unbounded_line_region_of_interest_geometry( GLRenderer &renderer, GLBuffer::MapBufferScope &map_vertex_element_buffer_scope, GLBuffer::MapBufferScope &map_vertex_buffer_scope, line_region_of_interest_stream_primitives_type::StreamTarget &line_stream_target, line_region_of_interest_stream_primitives_type::Primiti ...` | method | `void` | private | — |
| `render_single_pixel_size_point_region_of_interest_geometries( GLRenderer &renderer, GLBuffer::MapBufferScope &map_vertex_element_buffer_scope, GLBuffer::MapBufferScope &map_vertex_buffer_scope, const SeedCoRegistrationGeometryLists &geometry_lists)` | method | `void` | private | — |
| `render_single_pixel_wide_line_region_of_interest_geometries( GLRenderer &renderer, GLBuffer::MapBufferScope &map_vertex_element_buffer_scope, GLBuffer::MapBufferScope &map_vertex_buffer_scope, const SeedCoRegistrationGeometryLists &geometry_lists)` | method | `void` | private | — |
| `render_fill_region_of_interest_geometries( GLRenderer &renderer, GLBuffer::MapBufferScope &map_vertex_element_buffer_scope, GLBuffer::MapBufferScope &map_vertex_buffer_scope, const SeedCoRegistrationGeometryLists &geometry_lists)` | method | `void` | private | — |
| `mask_target_raster_with_regions_of_interest( GLRenderer &renderer, const Operation &operation, const GPlatesMaths::UnitVector3D &cube_face_centre, const GLTexture::shared_ptr_type &target_raster_texture, const GLTexture::shared_ptr_type &region_of_interest_mask_texture, GLBuffer::MapBufferScope &map_vertex_element_buff ...` | method | `void` | private | — |
| `mask_target_raster_with_region_of_interest( GLRenderer &renderer, GLBuffer::MapBufferScope &map_vertex_element_buffer_scope, GLBuffer::MapBufferScope &map_vertex_buffer_scope, mask_region_of_interest_stream_primitives_type::StreamTarget &mask_stream_target, mask_region_of_interest_stream_primitives_type::Primitives &ma ...` | method | `void` | private | — |
| `render_reduction_of_reduce_stage( GLRenderer &renderer, const Operation &operation, const ReduceQuadTreeInternalNode &dst_reduce_quad_tree_node, unsigned int src_child_x_offset, unsigned int src_child_y_offset, bool clear_dst_reduce_stage_texture, const GLTexture::shared_ptr_type &dst_reduce_stage_texture, const GLText ...` | method | `void` | private | — |
| `find_number_reduce_vertex_array_quads_spanned_by_child_reduce_quad_tree_node( const ReduceQuadTreeInternalNode &parent_reduce_quad_tree_node, unsigned int child_x_offset, unsigned int child_y_offset, unsigned int child_quad_tree_node_width_in_quads)` | method | `unsigned int` | private | — |
| `render_target_raster( GLRenderer &renderer, const CoRegistrationParameters &co_registration_parameters, const GLTexture::shared_ptr_type &target_raster_texture, const GLTransform &view_transform, const GLTransform &projection_transform)` | method | `bool` | private | Renders target raster into render texture and returns true if there was any rendering into the view frustum (determined by view\_transform and projection\_transform). |
| `acquire_rgba_float_texture( GLRenderer &renderer)` | method | `GLTexture::shared_ptr_type` | private | — |
| `acquire_rgba_fixed_texture( GLRenderer &renderer)` | method | `GLTexture::shared_ptr_type` | private | — |
| `return_co_registration_results_to_caller( const CoRegistrationParameters &co_registration_parameters)` | method | `void` | private | — |
| `debug_fixed_point_render_target( GLRenderer &renderer, const QString &image_file_basename)` | method | `void` | private | — |
| `debug_floating_point_render_target( GLRenderer &renderer, const QString &image_file_basename, bool coverage_is_in_green_channel)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `RENDER_REGION_OF_INTEREST_GEOMETRIES_FRAGMENT_SHADER_SOURCE_FILE_NAME` | variable | `QString` | Fragment shader source to render region-of-interest geometries. |
| `RENDER_REGION_OF_INTEREST_GEOMETRIES_VERTEX_SHADER_SOURCE_FILE_NAME` | variable | `QString` | Vertex shader source to render region-of-interest geometries. |
| `MASK_REGION_OF_INTEREST_FRAGMENT_SHADER_SOURCE_FILE_NAME` | variable | `QString` | Fragment shader source to extract target raster in region-of-interest in preparation for reduction operations. |
| `MASK_REGION_OF_INTEREST_VERTEX_SHADER_SOURCE_FILE_NAME` | variable | `QString` | Vertex shader source to extract target raster in region-of-interest in preparation for reduction operations. |
| `REDUCTION_OF_REGION_OF_INTEREST_FRAGMENT_SHADER_SOURCE_FILE_NAME` | variable | `QString` | Fragment shader source to reduce region-of-interest filter results. |
| `REDUCTION_OF_REGION_OF_INTEREST_VERTEX_SHADER_SOURCE_FILE_NAME` | variable | `QString` | Vertex shader source to reduce region-of-interest filter results. |
| `GPLATES_OPENGL_GLRASTERCOREGISTRATION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLRasterCoRegistration tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [data-mining/DataSelector](../data-mining/DataSelector.md) | data-mining | 15 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 2 |
| [app-logic/CoRegistrationLayerProxy](../app-logic/CoRegistrationLayerProxy.md) | app-logic | 1 |

## Related

**Shader programs compiled by this unit**

| Shader unit | Component |
|---|---|
| [shaders/raster_co_registration](../qt-resources/opengl/raster_co_registration.md) | shaders |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLRasterCoRegistration.h
python scripts/gpq.py def GPlatesOpenGL::GLRasterCoRegistration --body
python scripts/gpq.py uses GLRasterCoRegistration --kind class
python scripts/gpq.py hier GLRasterCoRegistration
```
