# TopologyNetworkResolverLayerProxy

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 191 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/TopologyNetworkResolverLayerProxy.h` | C++ | 619 |
| `src/app-logic/TopologyNetworkResolverLayerProxy.cc` | C++ | 1093 |

## Overview

[[[PROSE overview unit=app-logic/TopologyNetworkResolverLayerProxy tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::TopologyNetworkResolverLayerProxy`](#gplatesapplogictopologynetworkresolverlayerproxy) | class | [`LayerProxy`](LayerProxy.md) | — | 0 | A layer proxy that resolves topological networks from feature collection(s) containing topological network features. |

## Members

### `GPlatesAppLogic::TopologyNetworkResolverLayerProxy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<TopologyNetworkResolverLayerProxy>` | public | A convenience typedef for a shared pointer to a non-const TopologyNetworkResolverLayerProxy. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const TopologyNetworkResolverLayerProxy>` | public | A convenience typedef for a shared pointer to a const TopologyNetworkResolverLayerProxy. |
| `create( const TopologyNetworkParams &topology_network_params = TopologyNetworkParams())` | method | `non_null_ptr_type` | public | Creates a TopologyNetworkResolverLayerProxy object. |
| `~TopologyNetworkResolverLayerProxy()` | destructor | `None` | public | — |
| `get_resolved_topological_networks( std::vector<ResolvedTopologicalNetwork::non_null_ptr_type> &resolved_topological_networks)` | method | `ReconstructHandle::type` | public | Returns the resolved topological networks, for the current reconstruction time and current topology network params, by appending them to them to resolved\_topological\_networks. |
| `get_resolved_topological_networks( std::vector<ResolvedTopologicalNetwork::non_null_ptr_type> &resolved_topological_networks, const TopologyNetworkParams &topology_network_params)` | method | `ReconstructHandle::type` | public | Returns the resolved topological networks, for the current reconstruction time and specified topology network params, by appending them to them to resolved\_topological\_networks. |
| `get_resolved_topological_networks( std::vector<ResolvedTopologicalNetwork::non_null_ptr_type> &resolved_topological_networks, const double &reconstruction_time)` | method | `ReconstructHandle::type` | public | Returns the resolved topological networks, for the specified reconstruction time and current topology network params, by appending them to them to resolved\_topological\_networks. |
| `get_resolved_topological_networks( std::vector<ResolvedTopologicalNetwork::non_null_ptr_type> &resolved_topological_networks, const TopologyNetworkParams &topology_network_params, const double &reconstruction_time)` | method | `ReconstructHandle::type` | public | Returns the resolved topological networks, for the specified reconstruction time and specified topology network params, by appending them to them to resolved\_topological\_networks. |
| `get_resolved_network_time_span( const TimeSpanUtils::TimeRange &time_range)` | method | `TopologyReconstruct::resolved_network_time_span_type::non_null_ptr_to_const_type` | public | Returns a time span of resolved topological networks, for the current topology network params. |
| `get_resolved_network_time_span( const TimeSpanUtils::TimeRange &time_range, const TopologyNetworkParams &topology_network_params)` | method | `TopologyReconstruct::resolved_network_time_span_type::non_null_ptr_to_const_type` | public | Returns a time span of resolved topological networks, for the specified topology network params. |
| `get_resolved_topological_network_velocities( std::vector<MultiPointVectorField::non_null_ptr_type> &resolved_topological_network_velocities, VelocityDeltaTime::Type velocity_delta_time_type = VelocityDeltaTime::T_PLUS_MINUS_HALF_DELTA_T, const double &velocity_delta_time = 1.0)` | method | `ReconstructHandle::type` | public | Returns the velocities associated with the resolved topological networks, for the current reconstruction time, by appending them to them to resolved\_topological\_network\_velocities. |
| `get_resolved_topological_network_velocities( std::vector<MultiPointVectorField::non_null_ptr_type> &resolved_topological_network_velocities, const TopologyNetworkParams &topology_network_params, VelocityDeltaTime::Type velocity_delta_time_type = VelocityDeltaTime::T_PLUS_MINUS_HALF_DELTA_T, const double &velocity_delta ...` | method | `ReconstructHandle::type` | public | Returns the velocities associated with the resolved topological networks, for the current reconstruction time and specified network params, by appending them to them to resolved\_topological\_network\_velocities. |
| `get_resolved_topological_network_velocities( std::vector<MultiPointVectorField::non_null_ptr_type> &resolved_topological_network_velocities, const double &reconstruction_time, VelocityDeltaTime::Type velocity_delta_time_type = VelocityDeltaTime::T_PLUS_MINUS_HALF_DELTA_T, const double &velocity_delta_time = 1.0)` | method | `ReconstructHandle::type` | public | Returns the velocities associated with the resolved topological networks, for the specified reconstruction time and current network params, by appending them to them to resolved\_topological\_network\_velocities. |
| `get_resolved_topological_network_velocities( std::vector<MultiPointVectorField::non_null_ptr_type> &resolved_topological_network_velocities, const TopologyNetworkParams &topology_network_params, const double &reconstruction_time, VelocityDeltaTime::Type velocity_delta_time_type = VelocityDeltaTime::T_PLUS_MINUS_HALF_DE ...` | method | `ReconstructHandle::type` | public | Returns the velocities associated with the resolved topological networks, for the specified reconstruction time and network params, by appending them to resolved\_topological\_network\_velocities. |
| `get_current_topological_network_features( std::vector<GPlatesModel::FeatureHandle::weak_ref> &topological_network_features)` | method | `void` | public | Returns only the topological network subset of features set by add\_topological\_network\_feature\_collection, etc. |
| `get_current_features( std::vector<GPlatesModel::FeatureHandle::weak_ref> &features)` | method | `void` | public | Returns all features set by add\_topological\_network\_feature\_collection, etc. |
| `get_current_dependent_topological_sections( std::set<GPlatesModel::FeatureId> &dependent_topological_sections)` | method | `void` | public | Inserts the feature IDs of topological sections referenced by the current topological networks for \*all\* times (not just the current time). |
| `get_subject_token` | field | `GPlatesUtils::SubjectToken` | public | Returns the subject token that clients can use to determine if the resolved topological networks have changed since they were last retrieved. |
| `accept_visitor( ConstLayerProxyVisitor &visitor)` | method | `void` | public | Accept a ConstLayerProxyVisitor instance. |
| `accept_visitor( LayerProxyVisitor &visitor)` | method | `void` | public | Accept a LayerProxyVisitor instance. |
| `set_current_reconstruction_time( const double &reconstruction_time)` | method | `void` | public | Sets the current reconstruction time as set by the layer system. |
| `set_current_topology_network_params( const TopologyNetworkParams &topology_network_params)` | method | `void` | public | Sets the parameters used for resolving topological networks and their associated attributes. |
| `set_current_topological_sections_layer_proxies( const std::vector<ReconstructLayerProxy::non_null_ptr_type> & reconstructed_geometry_topological_sections_layer_proxies, const std::vector<TopologyGeometryResolverLayerProxy::non_null_ptr_type> & resolved_line_topological_sections_layer_proxies)` | method | `void` | public | Sets the current layer proxies used to reconstruct/resolve the topological network sections. |
| `add_topological_network_feature_collection( const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection)` | method | `void` | public | Add to the list of feature collections containing topological network features. |
| `remove_topological_network_feature_collection( const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection)` | method | `void` | public | Remove from the list of feature collections containing topological network features. |
| `modified_topological_network_feature_collection( const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection)` | method | `void` | public | A topological network feature collection was modified. |
| `ResolvedNetworks` | struct | `None` | private | Contains resolved topological networks. |
| `ResolvedNetworkTimeSpan` | struct | `None` | private | Contains resolved topological network time span. |
| `d_current_topological_network_features` | field | `std::vector<GPlatesModel::FeatureHandle::weak_ref>` | private | The subset of features that are topological networks. |
| `d_current_feature_collections` | field | `std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref>` | private | All input feature collections. |
| `d_current_reconstructed_geometry_topological_sections_layer_proxies` | field | `LayerProxyUtils::InputLayerProxySequence<ReconstructLayerProxy>` | private | Used to get reconstructed static features that form the topological sections for our topological geometries. |
| `d_current_resolved_line_topological_sections_layer_proxies` | field | `LayerProxyUtils::InputLayerProxySequence<TopologyGeometryResolverLayerProxy>` | private | Used to get resolved topological lines that form the topological sections for our topological geometries. |
| `d_current_reconstruction_time` | field | `double` | private | The current reconstruction time as set by the layer system. |
| `d_current_topology_network_params` | field | `TopologyNetworkParams` | private | The current topology network parameters as set by the layer system. |
| `d_cached_resolved_networks` | field | `ResolvedNetworks` | private | The cached resolved topologies for a single reconstruction time. |
| `d_cached_time_span` | field | `ResolvedNetworkTimeSpan` | private | The cached resolved topologies over a range of reconstruction times. |
| `d_dependent_topological_sections` | field | `DependentTopologicalSectionLayers` | private | The cached resolved networks (including time spans) depend on these topological sections. |
| `d_subject_token` | field | `GPlatesUtils::SubjectToken` | private | Used to notify polling observers that we've been updated. |
| `TopologyNetworkResolverLayerProxy( const TopologyNetworkParams &topology_network_params)` | constructor | `None` | private | — |
| `reset_cache()` | method | `void` | private | Resets any cached variables forcing them to be recalculated next time they're accessed. |
| `check_input_layer_proxies()` | method | `void` | private | Checks if any input layer proxies have changed. |
| `cache_resolved_topological_networks` | field | `std::vector<ResolvedTopologicalNetwork::non_null_ptr_type>` | private | Generates resolved topological networks for the specified reconstruction time if they're not already cached. |
| `cache_resolved_network_time_span( const TimeSpanUtils::TimeRange &time_range, const TopologyNetworkParams &topology_network_params)` | method | `TopologyReconstruct::resolved_network_time_span_type::non_null_ptr_to_const_type` | private | Generates a resolved network time span for the specified time range if one is not already cached. |
| `create_resolved_topological_networks( std::vector<ResolvedTopologicalNetwork::non_null_ptr_type> &resolved_topological_networks, const TopologyNetworkParams &topology_network_params, const double &reconstruction_time)` | method | `ReconstructHandle::type` | private | Creates resolved topological networks for the specified reconstruction time. |
| `create_resolved_topological_network_velocities( std::vector<MultiPointVectorField::non_null_ptr_type> &resolved_topological_network_velocities, const std::vector<ResolvedTopologicalNetwork::non_null_ptr_type> &resolved_topological_networks, const double &reconstruction_time, VelocityDeltaTime::Type velocity_delta_time_ ...` | method | `ReconstructHandle::type` | private | Creates resolved topological network velocities for the specified reconstruction time. |
| `create_resolved_topological_boundary_sub_segment_velocities( std::vector<MultiPointVectorField::non_null_ptr_type> &resolved_topological_boundary_sub_segment_velocities, const sub_segment_seq_type &sub_segments, const double &reconstruction_time, VelocityDeltaTime::Type velocity_delta_time_type, const double &velocity_ ...` | method | `void` | private | — |
| `create_resolved_topological_interior_hole_velocities( std::vector<MultiPointVectorField::non_null_ptr_type> &resolved_topological_interior_hole_velocities, const ResolvedTriangulation::Network::rigid_block_seq_type &interiors, const double &reconstruction_time, VelocityDeltaTime::Type velocity_delta_time_type, const do ...` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `find_topological_network_features( std::vector<GPlatesModel::FeatureHandle::weak_ref> &topological_network_features, const std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref> &feature_collections)` | function | `void` | Filter out features that are topological networks. |
| `GPLATES_APP_LOGIC_TOPOLOGYNETWORKRESOLVERLAYERPROXY_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/TopologyNetworkResolverLayerProxy tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/TopologyNetworkResolverLayerTask](TopologyNetworkResolverLayerTask.md) | app-logic | 5 |
| [app-logic/ScalarField3DLayerProxy](ScalarField3DLayerProxy.md) | app-logic | 3 |
| [app-logic/VelocityFieldCalculatorLayerProxy](VelocityFieldCalculatorLayerProxy.md) | app-logic | 3 |
| [app-logic/AssignPlateIds](AssignPlateIds.md) | app-logic | 2 |
| [app-logic/LayerProxyUtils](LayerProxyUtils.md) | app-logic | 2 |
| [app-logic/ReconstructLayerProxy](ReconstructLayerProxy.md) | app-logic | 2 |
| [app-logic/ReconstructLayerTask](ReconstructLayerTask.md) | app-logic | 2 |
| [presentation/LayerOutputRenderer](../presentation/LayerOutputRenderer.md) | presentation | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/TopologyNetworkResolverLayerProxy.h
python scripts/gpq.py def GPlatesAppLogic::TopologyNetworkResolverLayerProxy --body
python scripts/gpq.py uses TopologyNetworkResolverLayerProxy --kind class
python scripts/gpq.py hier TopologyNetworkResolverLayerProxy
```
