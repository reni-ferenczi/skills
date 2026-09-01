# ReconstructLayerProxy

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 139 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructLayerProxy.h` | C++ | 1332 |
| `src/app-logic/ReconstructLayerProxy.cc` | C++ | 1463 |

## Overview

[[[PROSE overview unit=app-logic/ReconstructLayerProxy tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructLayerProxy`](#gplatesapplogicreconstructlayerproxy) | class | [`LayerProxy`](LayerProxy.md) | — | 0 | A layer proxy for reconstructing regular (non-topological) features containing vector geometry. |

## Members

### `GPlatesAppLogic::ReconstructLayerProxy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ReconstructLayerProxy>` | public | A convenience typedef for a shared pointer to a non-const ReconstructLayerProxy. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ReconstructLayerProxy>` | public | A convenience typedef for a shared pointer to a const ReconstructLayerProxy. |
| `reconstructed_feature_geometries_spatial_partition_type` | typedef | `GPlatesMaths::CubeQuadTreePartition<ReconstructedFeatureGeometry::non_null_ptr_type>` | public | Typedef for a spatial partition of reconstructed feature geometries. |
| `geometries_spatial_partition_type` | typedef | `GPlatesMaths::CubeQuadTreePartition<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | public | Typedef for a spatial partition of geometries. |
| `reconstructions_spatial_partition_type` | typedef | `GPlatesMaths::CubeQuadTreePartition<ReconstructContext::Reconstruction>` | public | Typedef for a spatial partition of reconstructed feature geometries that reference present day geometries. |
| `DEFAULT_SPATIAL_PARTITION_DEPTH` | field | `unsigned int` | public | The default depth of the spatial partition (the quad trees in each cube face). |
| `MAX_NUM_RECONSTRUCTIONS_IN_CACHE` | field | `unsigned int` | public | The maximum number of reconstructions to cache for different reconstruction time / reconstruct param combinations - each combination represents one cached object. |
| `create( const ReconstructMethodRegistry &reconstruct_method_registry, const ReconstructParams &reconstruct_params = ReconstructParams(), unsigned int max_num_reconstructions_in_cache = MAX_NUM_RECONSTRUCTIONS_IN_CACHE)` | method | `non_null_ptr_type` | public | Creates a ReconstructLayerProxy object. |
| `~ReconstructLayerProxy()` | destructor | `None` | public | — |
| `get_reconstructed_feature_geometries( std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &reconstructed_feature_geometries)` | method | `ReconstructHandle::type` | public | Returns the reconstructed feature geometries, for the current reconstruct params and current reconstruction time, by appending them to reconstructed\_feature\_geometries. |
| `get_reconstructed_feature_geometries( std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &reconstructed_feature_geometries, const ReconstructParams &reconstruct_params)` | method | `ReconstructHandle::type` | public | Returns the reconstructed feature geometries, for the specified reconstruct params and current reconstruction time, by appending them to reconstructed\_feature\_geometries. |
| `get_reconstructed_feature_geometries( std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &reconstructed_feature_geometries, const double &reconstruction_time)` | method | `ReconstructHandle::type` | public | Returns the reconstructed feature geometries, for the current reconstruct params and specified reconstruction time, by appending them to reconstructed\_feature\_geometries. |
| `get_reconstructed_feature_geometries( std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &reconstructed_feature_geometries, const ReconstructParams &reconstruct_params, const double &reconstruction_time)` | method | `ReconstructHandle::type` | public | Returns the reconstructed feature geometries, for the specified reconstruct params and reconstruction time, by appending them to reconstructed\_feature\_geometries. |
| `get_reconstructions( std::vector<ReconstructContext::Reconstruction> &reconstructions)` | method | `ReconstructHandle::type` | public | Returns the reconstructed feature geometries, for the current reconstruction time, by appending them to reconstructions. |
| `get_reconstructions( std::vector<ReconstructContext::Reconstruction> &reconstructions, const ReconstructParams &reconstruct_params)` | method | `ReconstructHandle::type` | public | Returns the reconstructions, for the specified reconstruct params and current reconstruction time, by appending them to reconstructions. |
| `get_reconstructions( std::vector<ReconstructContext::Reconstruction> &reconstructions, const double &reconstruction_time)` | method | `ReconstructHandle::type` | public | Returns the reconstructions, for the current reconstruct params and specified reconstruction time, by appending them to reconstructions. |
| `get_reconstructions( std::vector<ReconstructContext::Reconstruction> &reconstructions, const ReconstructParams &reconstruct_params, const double &reconstruction_time)` | method | `ReconstructHandle::type` | public | Returns the reconstructions, for the specified reconstruct params and reconstruction time, by appending them to reconstructions. |
| `get_reconstructed_feature_geometries_spatial_partition( ReconstructHandle::type *reconstruct_handle = NULL)` | method | `reconstructed_feature_geometries_spatial_partition_type::non_null_ptr_to_const_type` | public | Returns the spatial partition of reconstructed feature geometries for the current reconstruct params and the current reconstruction time. |
| `get_reconstructed_feature_geometries_spatial_partition( const ReconstructParams &reconstruct_params, ReconstructHandle::type *reconstruct_handle = NULL)` | method | `reconstructed_feature_geometries_spatial_partition_type::non_null_ptr_to_const_type` | public | Returns the spatial partition of reconstructed feature geometries for the specified reconstruct params and the current reconstruction time. |
| `get_reconstructed_feature_geometries_spatial_partition( const double &reconstruction_time, ReconstructHandle::type *reconstruct_handle = NULL)` | method | `reconstructed_feature_geometries_spatial_partition_type::non_null_ptr_to_const_type` | public | Returns the spatial partition of reconstructed feature geometries for the current reconstruct params and the specified reconstruction time. |
| `get_reconstructed_feature_geometries_spatial_partition( const ReconstructParams &reconstruct_params, const double &reconstruction_time, ReconstructHandle::type *reconstruct_handle = NULL)` | method | `reconstructed_feature_geometries_spatial_partition_type::non_null_ptr_to_const_type` | public | Returns the spatial partition of reconstructed feature geometries for the specified reconstruct params and reconstruction time. |
| `get_reconstructions_spatial_partition( ReconstructHandle::type *reconstruct_handle = NULL)` | method | `reconstructions_spatial_partition_type::non_null_ptr_to_const_type` | public | Returns the spatial partition of reconstructions for the current reconstruct params and the current reconstruction time. |
| `get_reconstructions_spatial_partition( const ReconstructParams &reconstruct_params, ReconstructHandle::type *reconstruct_handle = NULL)` | method | `reconstructions_spatial_partition_type::non_null_ptr_to_const_type` | public | Returns the spatial partition of reconstructions for the specified reconstruct params and the current reconstruction time. |
| `get_reconstructions_spatial_partition( const double &reconstruction_time, ReconstructHandle::type *reconstruct_handle = NULL)` | method | `reconstructions_spatial_partition_type::non_null_ptr_to_const_type` | public | Returns the spatial partition of reconstructions for the current reconstruct params and the specified reconstruction time. |
| `get_reconstructions_spatial_partition( const ReconstructParams &reconstruct_params, const double &reconstruction_time, ReconstructHandle::type *reconstruct_handle = NULL)` | method | `reconstructions_spatial_partition_type::non_null_ptr_to_const_type` | public | Returns the spatial partition of reconstructions for the specified reconstruct params and reconstruction time. |
| `get_reconstructed_features( std::vector<ReconstructContext::ReconstructedFeature> &reconstructed_features)` | method | `ReconstructHandle::type` | public | Returns the reconstructed feature geometries (grouped by feature), for the current reconstruction time, by appending them to reconstructed\_features. |
| `get_reconstructed_features( std::vector<ReconstructContext::ReconstructedFeature> &reconstructed_features, const ReconstructParams &reconstruct_params)` | method | `ReconstructHandle::type` | public | Returns the reconstructed feature geometries (grouped by feature), for the specified reconstruct params and current reconstruction time, by appending them to reconstructed\_features. |
| `get_reconstructed_features( std::vector<ReconstructContext::ReconstructedFeature> &reconstructed_features, const double &reconstruction_time)` | method | `ReconstructHandle::type` | public | Returns the reconstructed feature geometries (grouped by feature), for the current reconstruct params and specified reconstruction time, by appending them to reconstructed\_features. |
| `get_reconstructed_features( std::vector<ReconstructContext::ReconstructedFeature> &reconstructed_features, const ReconstructParams &reconstruct_params, const double &reconstruction_time)` | method | `ReconstructHandle::type` | public | Returns the reconstructed feature geometries (grouped by feature), for the specified reconstruct params and reconstruction time, by appending them to reconstructed\_features. |
| `get_reconstructed_feature_time_spans( std::vector<ReconstructContext::ReconstructedFeatureTimeSpan> &reconstructed_feature_time_spans, const TimeSpanUtils::TimeRange &time_range)` | method | `ReconstructHandle::type` | public | Returns reconstructed feature time spans for the current reconstruct params. |
| `get_reconstructed_feature_time_spans( std::vector<ReconstructContext::ReconstructedFeatureTimeSpan> &reconstructed_feature_time_spans, const TimeSpanUtils::TimeRange &time_range, const ReconstructParams &reconstruct_params)` | method | `ReconstructHandle::type` | public | Returns reconstructed feature time spans for the specified reconstruct params. |
| `get_topology_reconstructed_feature_time_spans( std::vector<ReconstructContext::TopologyReconstructedFeatureTimeSpan> &topology_reconstructed_feature_time_spans)` | method | `void` | public | Returns any topology-reconstructed feature time spans, for the current reconstruct params. |
| `get_topology_reconstructed_feature_time_spans( std::vector<ReconstructContext::TopologyReconstructedFeatureTimeSpan> &topology_reconstructed_feature_time_spans, const ReconstructParams &reconstruct_params)` | method | `void` | public | Returns any topology-reconstructed feature time spans, for the specified reconstruct params. |
| `get_reconstructed_topological_sections( std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &reconstructed_topological_sections, const std::set<GPlatesModel::FeatureId> &topological_sections_referenced)` | method | `ReconstructHandle::type` | public | Returns the reconstructed topological sections with matching feature IDs, for the current reconstruct params and current reconstruction time, by appending them to reconstructed\_topological\_sections. |
| `get_reconstructed_topological_sections( std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &reconstructed_topological_sections, const std::set<GPlatesModel::FeatureId> &topological_sections_referenced, const ReconstructParams &reconstruct_params)` | method | `ReconstructHandle::type` | public | Returns the reconstructed topological sections with matching feature IDs, for the specified reconstruct params and current reconstruction time, by appending them to reconstructed\_topological\_sections. |
| `get_reconstructed_topological_sections( std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &reconstructed_topological_sections, const std::set<GPlatesModel::FeatureId> &topological_sections_referenced, const double &reconstruction_time)` | method | `ReconstructHandle::type` | public | Returns the reconstructed topological sections with matching feature IDs, for the current reconstruct params and specified reconstruction time, by appending them to reconstructed\_topological\_sections. |
| `get_reconstructed_topological_sections( std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &reconstructed_topological_sections, const std::set<GPlatesModel::FeatureId> &topological_sections_referenced, const ReconstructParams &reconstruct_params, const double &reconstruction_time)` | method | `ReconstructHandle::type` | public | Returns the reconstructed topological sections with matching feature IDs, for the specified reconstruct params and reconstruction time, by appending them to v. |
| `get_reconstructed_static_polygon_meshes( GPlatesOpenGL::GLRenderer &renderer, bool reconstructing_with_age_grid, const double &reconstruction_time)` | method | `GPlatesOpenGL::GLReconstructedStaticPolygonMeshes::non_null_ptr_type` | public | The (reconstructed) present day polygon meshes in OpenGL form at the specified reconstruction time. |
| `get_reconstructed_static_polygon_meshes( GPlatesOpenGL::GLRenderer &renderer, bool reconstructing_with_age_grid)` | method | `GPlatesOpenGL::GLReconstructedStaticPolygonMeshes::non_null_ptr_type` | public | The (reconstructed) present day polygon meshes in OpenGL form at the current reconstruction time. |
| `get_reconstructed_feature_velocities( std::vector<MultiPointVectorField::non_null_ptr_type> &reconstructed_feature_velocities, VelocityDeltaTime::Type velocity_delta_time_type = VelocityDeltaTime::T_PLUS_MINUS_HALF_DELTA_T, const double &velocity_delta_time = 1.0)` | method | `ReconstructHandle::type` | public | Returns the velocities associated with reconstructed feature geometries, for the current reconstruct params and current reconstruction time, by appending them to reconstructed\_feature\_velocities. |
| `get_reconstructed_feature_velocities( std::vector<MultiPointVectorField::non_null_ptr_type> &reconstructed_feature_velocities, const ReconstructParams &reconstruct_params, VelocityDeltaTime::Type velocity_delta_time_type = VelocityDeltaTime::T_PLUS_MINUS_HALF_DELTA_T, const double &velocity_delta_time = 1.0)` | method | `ReconstructHandle::type` | public | Returns the velocities associated with reconstructed feature geometries, for the specified reconstruct params and current reconstruction time, by appending them to reconstructed\_feature\_velocities. |
| `get_reconstructed_feature_velocities( std::vector<MultiPointVectorField::non_null_ptr_type> &reconstructed_feature_velocities, const double &reconstruction_time, VelocityDeltaTime::Type velocity_delta_time_type = VelocityDeltaTime::T_PLUS_MINUS_HALF_DELTA_T, const double &velocity_delta_time = 1.0)` | method | `ReconstructHandle::type` | public | Returns the velocities associated with reconstructed feature geometries, for the current reconstruct params and specified reconstruction time, by appending them to reconstructed\_feature\_velocities. |
| `get_reconstructed_feature_velocities( std::vector<MultiPointVectorField::non_null_ptr_type> &reconstructed_feature_velocities, const ReconstructParams &reconstruct_params, const double &reconstruction_time, VelocityDeltaTime::Type velocity_delta_time_type = VelocityDeltaTime::T_PLUS_MINUS_HALF_DELTA_T, const double &ve ...` | method | `ReconstructHandle::type` | public | Returns the velocities associated with reconstructed feature geometries, for the specified reconstruct params and reconstruction time, by appending them to reconstructed\_feature\_velocities. |
| `get_reconstruct_method_context()` | method | `ReconstructMethodInterface::Context` | public | Returns the reconstruct method context, for the current reconstruct params, used to reconstruct features. |
| `get_reconstruct_method_context( const ReconstructParams &reconstruct_params)` | method | `ReconstructMethodInterface::Context` | public | Returns the reconstruct method context, for the specified reconstruct params, used to reconstruct features. |
| `get_present_day_geometries` | field | `std::vector<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | public | Returns the present day geometries of the current set of reconstructable feature collections input to this layer proxy. |
| `get_present_day_polygon_meshes` | field | `std::vector<boost::optional<GPlatesMaths::PolygonMesh::non_null_ptr_to_const_type> >` | public | Returns the present day geometries of the current set of reconstructable feature collections input to this layer proxy. |
| `get_present_day_geometries_spatial_partition()` | method | `geometries_spatial_partition_type::non_null_ptr_to_const_type` | public | Returns the present day geometries in a spatial partition. |
| `get_present_day_geometries_spatial_partition_locations` | field | `std::vector<GPlatesMaths::CubeQuadTreeLocation>` | public | Returns the present day geometries in a spatial partition. |
| `get_current_reconstructable_features( std::vector<GPlatesModel::FeatureHandle::weak_ref> &features)` | method | `void` | public | Returns only the reconstructable (non-topological) subset of features set by add\_reconstructable\_feature\_collection, etc. |
| `get_current_features( std::vector<GPlatesModel::FeatureHandle::weak_ref> &features)` | method | `void` | public | Returns all features set by add\_reconstructable\_feature\_collection, etc. |
| `get_current_reconstruction_layer_proxy()` | method | `ReconstructionLayerProxy::non_null_ptr_type` | public | Returns the current reconstruction layer proxy used for reconstructions. |
| `get_subject_token` | field | `GPlatesUtils::SubjectToken` | public | Returns the subject token that clients can use to determine if the reconstructed feature geometries have changed since they were last retrieved. |
| `get_reconstructable_feature_collections_subject_token` | field | `GPlatesUtils::SubjectToken` | public | Returns the subject token that clients can use to determine if the reconstructable feature collections have changed. |
| `accept_visitor( ConstLayerProxyVisitor &visitor)` | method | `void` | public | Accept a ConstLayerProxyVisitor instance. |
| `accept_visitor( LayerProxyVisitor &visitor)` | method | `void` | public | Accept a LayerProxyVisitor instance. |
| `set_current_reconstruction_time( const double &reconstruction_time)` | method | `void` | public | Sets the current reconstruction time as set by the layer system. |
| `set_current_reconstruct_params( const ReconstructParams &reconstruct_params)` | method | `void` | public | Sets the parameters used for reconstructing. |
| `set_current_reconstruction_layer_proxy( const ReconstructionLayerProxy::non_null_ptr_type &reconstruction_layer_proxy)` | method | `void` | public | Set the reconstruction layer proxy used to rotate the feature geometries. |
| `set_current_topology_surface_layer_proxies( const std::vector<GPlatesGlobal::PointerTraits<TopologyGeometryResolverLayerProxy>::non_null_ptr_type> & resolved_boundary_topology_surface_layer_proxies, const std::vector<GPlatesGlobal::PointerTraits<TopologyNetworkResolverLayerProxy>::non_null_ptr_type> & resolved_network_ ...` | method | `void` | public | Sets the current topology surface layer proxies (used if reconstructing using topologies). |
| `add_reconstructable_feature_collection( const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection)` | method | `void` | public | Add to the list of feature collections that will be reconstructed. |
| `remove_reconstructable_feature_collection( const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection)` | method | `void` | public | Remove from the list of feature collections that will be reconstructed. |
| `modified_reconstructable_feature_collection( const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection)` | method | `void` | public | A reconstructable feature collection was modified. |
| `using_topologies_to_reconstruct()` | method | `bool` | public | Returns true if we are reconstructing geometries using topologies. |
| `ReconstructionInfo` | struct | `None` | private | Contains optional reconstructed feature geometries as sequences and spatial partitions. |
| `reconstruction_cache_key_type` | typedef | `std::pair<GPlatesMaths::real_t, ReconstructParams>` | private | Typedef for the key type to the reconstruction cache (reconstruction time and reconstruct params). |
| `reconstruction_cache_value_type` | typedef | `ReconstructionInfo` | private | Typedef for the value type stored in the reconstruction cache. |
| `reconstruction_cache_type` | typedef | `GPlatesUtils::KeyValueCache< reconstruction_cache_key_type, reconstruction_cache_value_type>` | private | Typedef for a cache of reconstruction information keyed by reconstruction time and reconstruct params. |
| `reconstruct_context_state_map_type` | typedef | `std::map<ReconstructParams, ReconstructContext::context_state_weak_reference_type>` | private | Typedef for mapping reconstruct parameters to their associated reconstruct context state. |
| `PresentDayInfo` | struct | `None` | private | Contains optional cached present day geometries and polygon meshes. |
| `GLReconstructedPolygonMeshes` | struct | `None` | private | Contains optional cached reconstructed polygon meshes. |
| `POLYGON_MESH_EDGE_LENGTH_THRESHOLD_RADIANS` | field | `double` | private | PolygonMesh objects are mesh refined such that all mesh edge lengths are below this threshold. |
| `d_reconstruct_method_registry` | field | `ReconstructMethodRegistry` | private | Used to associate features with reconstruct methods. |
| `d_reconstruct_context` | field | `ReconstructContext` | private | Used to reconstruct features into ReconstructedFeatureGeometry objects. |
| `d_reconstruct_context_state_map` | field | `reconstruct_context_state_map_type` | private | A mapping of reconstruct parameters to their associated reconstruct context state. |
| `d_current_reconstructable_features` | field | `std::vector<GPlatesModel::FeatureHandle::weak_ref>` | private | The subset of features that are reconstructable (non-topological). |
| `d_current_feature_collections` | field | `std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref>` | private | All input feature collections. |
| `d_current_reconstruction_layer_proxy` | field | `LayerProxyUtils::InputLayerProxy<ReconstructionLayerProxy>` | private | Used to get reconstruction trees at desired reconstruction times. |
| `d_current_topological_boundary_resolver_layer_proxies` | field | `LayerProxyUtils::InputLayerProxySequence<TopologyGeometryResolverLayerProxy>` | private | Used to get resolved topology boundaries. |
| `d_current_topological_network_resolver_layer_proxies` | field | `LayerProxyUtils::InputLayerProxySequence<TopologyNetworkResolverLayerProxy>` | private | Used to get resolved topology networks. |
| `d_current_reconstruction_time` | field | `double` | private | The current reconstruction time as set by the layer system. |
| `d_current_reconstruct_params` | field | `ReconstructParams` | private | The current reconstruct parameters as set by the layer system. |
| `d_cached_reconstructions` | field | `reconstruction_cache_type` | private | The various reconstructions cached according to reconstruction time and reconstruct params. |
| `d_cached_reconstructions_default_maximum_size` | field | `unsigned int` | private | The default maximum size of the reconstructions cache. |
| `d_cached_present_day_info` | field | `PresentDayInfo` | private | The cached present day geometries and polygon meshes. |
| `d_cached_reconstructed_polygon_meshes` | field | `GLReconstructedPolygonMeshes` | private | The cached present day polygon meshes in OpenGL vertex array form. |
| `d_subject_token` | field | `GPlatesUtils::SubjectToken` | private | Used to notify polling observers that we've been updated. |
| `d_reconstructable_feature_collections_subject_token` | field | `GPlatesUtils::SubjectToken` | private | The subject token that clients can use to determine if the reconstructable feature collections have changed. |
| `ReconstructLayerProxy( const ReconstructMethodRegistry &reconstruct_method_registry, const ReconstructParams &reconstruct_params, unsigned int max_num_reconstructions_in_cache)` | constructor | `None` | private | — |
| `reset_reconstruction_cache()` | method | `void` | public | Resets any cached \*reconstruction\* variables forcing them to be recalculated next time they're accessed. |
| `reset_reconstructable_feature_collection_caches()` | method | `void` | private | Resets any cached variables forcing them to be recalculated next time they're accessed. |
| `check_input_layer_proxy( InputLayerProxyWrapperType &input_layer_proxy_wrapper)` | method | `void` | private | Checks if the specified input layer proxy has changed. |
| `check_input_layer_proxies()` | method | `void` | private | Checks if any input layer proxies have changed. |
| `cache_reconstructed_features` | field | `std::vector<ReconstructContext::ReconstructedFeature>` | private | Generates reconstructed features for the specified reconstruct params and reconstruction time if they're not already cached. |
| `cache_reconstructions_spatial_partition( ReconstructionInfo &reconstruction_info, const double &reconstruction_time)` | method | `reconstructions_spatial_partition_type::non_null_ptr_to_const_type` | private | Generates a reconstructions spatial partition for the specified reconstruct params and reconstruction time if it's not already cached. |
| `cache_reconstructed_feature_velocities` | field | `std::vector<MultiPointVectorField::non_null_ptr_type>` | private | Generates reconstructed feature \*velocities\* for the specified reconstruct params and reconstruction time if they're not already cached. |
| `create_reconstruction_info( const reconstruction_cache_key_type &reconstruction_cache_key)` | method | `ReconstructionInfo` | private | Utility method used by reconstruction\_cache\_type when it needs a new ReconstructionInfo for a new reconstruction time / reconstruct params input pair. |
| `get_or_create_reconstruct_context( const ReconstructParams &reconstruct_params)` | method | `ReconstructContext::context_state_reference_type` | private | Utility method to get, or create, a reconstruct context for the specified reconstruct parameters. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `add_reconstruction_to_root_element_of_rfg_spatial_partition( ReconstructLayerProxy::reconstructed_feature_geometries_spatial_partition_type &rfg_spatial_partition, const ReconstructContext::Reconstruction &reconstruction)` | function | `void` | Helper function for 'GPlatesMaths::CubeQuadTreePartitionUtils::mirror' when mirroring elements at the root of a cube quad tree. |
| `add_reconstruction_to_node_element_of_rfg_spatial_partition( ReconstructLayerProxy::reconstructed_feature_geometries_spatial_partition_type &rfg_spatial_partition, ReconstructLayerProxy::reconstructed_feature_geometries_spatial_partition_type::node_reference_type rfg_node, const ReconstructContext::Reconstruction &reco ...` | function | `void` | Helper function for 'GPlatesMaths::CubeQuadTreePartitionUtils::mirror' when mirroring elements at a quad node of a cube quad tree. |
| `POLYGON_MESH_EDGE_LENGTH_THRESHOLD_RADIANS` | variable | `double` | — |
| `GPLATES_APP_LOGIC_RECONSTRUCTLAYERPROXY_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/ReconstructLayerProxy tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/TopologyGeometryResolverLayerProxy](TopologyGeometryResolverLayerProxy.md) | app-logic | 77 |
| [app-logic/VelocityFieldCalculatorLayerProxy](VelocityFieldCalculatorLayerProxy.md) | app-logic | 50 |
| [app-logic/TopologyNetworkResolverLayerProxy](TopologyNetworkResolverLayerProxy.md) | app-logic | 47 |
| [app-logic/ScalarField3DLayerProxy](ScalarField3DLayerProxy.md) | app-logic | 43 |
| [app-logic/ReconstructScalarCoverageLayerProxy](ReconstructScalarCoverageLayerProxy.md) | app-logic | 33 |
| [app-logic/ReconstructLayerTask](ReconstructLayerTask.md) | app-logic | 11 |
| [app-logic/TopologyGeometryResolverLayerTask](TopologyGeometryResolverLayerTask.md) | app-logic | 5 |
| [app-logic/AssignPlateIds](AssignPlateIds.md) | app-logic | 3 |
| [app-logic/CoRegistrationLayerProxy](CoRegistrationLayerProxy.md) | app-logic | 3 |
| [app-logic/LayerProxyUtils](LayerProxyUtils.md) | app-logic | 3 |
| [app-logic/RasterLayerProxy](RasterLayerProxy.md) | app-logic | 3 |
| [app-logic/ReconstructScalarCoverageLayerTask](ReconstructScalarCoverageLayerTask.md) | app-logic | 3 |
| [app-logic/VelocityFieldCalculatorLayerTask](VelocityFieldCalculatorLayerTask.md) | app-logic | 3 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 3 |
| [qt-widgets/GenerateDeformingMeshPointsDialog](../qt-widgets/GenerateDeformingMeshPointsDialog.md) | qt-widgets | 3 |
| [view-operations/FocusedFeatureGeometryManipulator](../view-operations/FocusedFeatureGeometryManipulator.md) | view-operations | 3 |
| [app-logic/DependentTopologicalSectionLayers](DependentTopologicalSectionLayers.md) | app-logic | 2 |
| [app-logic/ReconstructGraph](ReconstructGraph.md) | app-logic | 2 |
| [app-logic/ResolvedRaster](ResolvedRaster.md) | app-logic | 2 |
| [app-logic/TopologyNetworkResolverLayerTask](TopologyNetworkResolverLayerTask.md) | app-logic | 2 |

*... and 10 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructLayerProxy.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructLayerProxy --body
python scripts/gpq.py uses ReconstructLayerProxy --kind class
python scripts/gpq.py hier ReconstructLayerProxy
```
