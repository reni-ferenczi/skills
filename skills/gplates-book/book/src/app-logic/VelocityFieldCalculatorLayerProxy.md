# VelocityFieldCalculatorLayerProxy

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 316 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/VelocityFieldCalculatorLayerProxy.h` | C++ | 441 |
| `src/app-logic/VelocityFieldCalculatorLayerProxy.cc` | C++ | 536 |

## Overview

[[[PROSE overview unit=app-logic/VelocityFieldCalculatorLayerProxy tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::VelocityFieldCalculatorLayerProxy`](#gplatesapplogicvelocityfieldcalculatorlayerproxy) | class | [`LayerProxy`](LayerProxy.md) | — | 0 | A layer proxy that calculates velocity fields on domains of mesh points inside reconstructed static polygons, resolved topological dynamic polygons or resolved topological networks. |

## Members

### `GPlatesAppLogic::VelocityFieldCalculatorLayerProxy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<VelocityFieldCalculatorLayerProxy>` | public | A convenience typedef for a shared pointer to a non-const VelocityFieldCalculatorLayerProxy. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const VelocityFieldCalculatorLayerProxy>` | public | A convenience typedef for a shared pointer to a const VelocityFieldCalculatorLayerProxy. |
| `MAX_NUM_VELOCITY_RESULTS_IN_CACHE` | field | `unsigned int` | public | The maximum number of velocity results to cache for different reconstruction time / velocity param combinations - each combination represents one cached object. |
| `create( const VelocityParams &velocity_params = VelocityParams(), unsigned int max_num_velocity_results_in_cache = MAX_NUM_VELOCITY_RESULTS_IN_CACHE)` | method | `non_null_ptr_type` | public | Creates a VelocityFieldCalculatorLayerProxy object. |
| `~VelocityFieldCalculatorLayerProxy()` | destructor | `None` | public | — |
| `get_velocity_multi_point_vector_fields( std::vector<MultiPointVectorField::non_null_ptr_type> &multi_point_vector_fields)` | method | `void` | public | Returns the velocities in multi-point vector fields, for the current velocity params and current reconstruction time, by appending them to them to multi\_point\_vector\_fields. |
| `get_velocity_multi_point_vector_fields( std::vector<MultiPointVectorField::non_null_ptr_type> &multi_point_vector_fields, const VelocityParams &velocity_params)` | method | `void` | public | Returns the velocities, for the specified velocity params and current reconstruction time, by appending them to multi\_point\_vector\_fields. |
| `get_velocity_multi_point_vector_fields( std::vector<MultiPointVectorField::non_null_ptr_type> &multi_point_vector_fields, const double &reconstruction_time)` | method | `void` | public | Returns the velocities, for the current velocity params and specified reconstruction time, by appending them to multi\_point\_vector\_fields. |
| `get_velocity_multi_point_vector_fields( std::vector<MultiPointVectorField::non_null_ptr_type> &multi_point_vector_fields, const VelocityParams &velocity_params, const double &reconstruction_time)` | method | `void` | public | Returns the velocities, for the specified velocity params and reconstruction time, by appending them to multi\_point\_vector\_fields. |
| `get_subject_token` | field | `GPlatesUtils::SubjectToken` | public | Returns the subject token that clients can use to determine if the velocities have changed since they were last retrieved. |
| `accept_visitor( ConstLayerProxyVisitor &visitor)` | method | `void` | public | Accept a ConstLayerProxyVisitor instance. |
| `accept_visitor( LayerProxyVisitor &visitor)` | method | `void` | public | Accept a LayerProxyVisitor instance. |
| `set_current_reconstruction_time( const double &reconstruction_time)` | method | `void` | public | Sets the current reconstruction time as set by the layer system. |
| `set_current_velocity_params( const VelocityParams &velocity_params)` | method | `void` | public | Sets the parameters used for calculating velocities. |
| `add_domain_reconstruct_layer_proxy( const ReconstructLayerProxy::non_null_ptr_type &domain_reconstruct_layer_proxy)` | method | `void` | public | Add a domain reconstruct layer proxy. |
| `remove_domain_reconstruct_layer_proxy( const ReconstructLayerProxy::non_null_ptr_type &domain_reconstruct_layer_proxy)` | method | `void` | public | Remove a domain reconstructed geometries layer proxy. |
| `add_domain_topological_geometry_resolver_layer_proxy( const TopologyGeometryResolverLayerProxy::non_null_ptr_type &domain_topological_geometry_resolver_layer_proxy)` | method | `void` | public | Add a domain topological geometry resolver layer proxy. |
| `remove_domain_topological_geometry_resolver_layer_proxy( const TopologyGeometryResolverLayerProxy::non_null_ptr_type &domain_topological_geometry_resolver_layer_proxy)` | method | `void` | public | Remove a domain topological geometry resolver layer proxy. |
| `add_domain_topological_network_resolver_layer_proxy( const TopologyNetworkResolverLayerProxy::non_null_ptr_type &domain_topological_network_resolver_layer_proxy)` | method | `void` | public | Add a domain topological network resolver layer proxy. |
| `remove_domain_topological_network_resolver_layer_proxy( const TopologyNetworkResolverLayerProxy::non_null_ptr_type &domain_topological_network_resolver_layer_proxy)` | method | `void` | public | Remove a domain topological network resolver layer proxy. |
| `add_surface_reconstructed_polygons_layer_proxy( const ReconstructLayerProxy::non_null_ptr_type &surface_reconstructed_polygons_layer_proxy)` | method | `void` | public | Add a surface reconstructed static polygons layer proxy. |
| `remove_surface_reconstructed_polygons_layer_proxy( const ReconstructLayerProxy::non_null_ptr_type &surface_reconstructed_polygons_layer_proxy)` | method | `void` | public | Remove a surface reconstructed static polygons layer proxy. |
| `add_surface_topological_geometry_resolver_layer_proxy( const TopologyGeometryResolverLayerProxy::non_null_ptr_type &surface_topological_geometry_resolver_layer_proxy)` | method | `void` | public | Add a surface topological geometry resolver layer proxy. |
| `remove_surface_topological_geometry_resolver_layer_proxy( const TopologyGeometryResolverLayerProxy::non_null_ptr_type &surface_topological_geometry_resolver_layer_proxy)` | method | `void` | public | Remove a surface topological geometry resolver layer proxy. |
| `add_surface_topological_network_resolver_layer_proxy( const TopologyNetworkResolverLayerProxy::non_null_ptr_type &surface_topological_network_resolver_layer_proxy)` | method | `void` | public | Add a surface topological network resolver layer proxy. |
| `remove_surface_topological_network_resolver_layer_proxy( const TopologyNetworkResolverLayerProxy::non_null_ptr_type &surface_topological_network_resolver_layer_proxy)` | method | `void` | public | Remove a surface topological network resolver layer proxy. |
| `VelocityInfo` | struct | `None` | private | Contains optional multi-point velocity fields. |
| `velocity_cache_key_type` | typedef | `std::pair<GPlatesMaths::real_t, VelocityParams>` | private | Typedef for the key type to the velocity cache (reconstruction time and velocity params). |
| `velocity_cache_value_type` | typedef | `VelocityInfo` | private | Typedef for the value type stored in the velocity cache. |
| `velocity_cache_type` | typedef | `GPlatesUtils::KeyValueCache<velocity_cache_key_type, velocity_cache_value_type>` | private | Typedef for a cache of velocity information keyed by reconstruction time and velocity params. |
| `d_current_surface_reconstructed_polygon_layer_proxies` | field | `LayerProxyUtils::InputLayerProxySequence<ReconstructLayerProxy>` | private | Used to get surface reconstructed static polygon surfaces to calculate velocities on. |
| `d_current_surface_topological_geometry_resolver_layer_proxies` | field | `LayerProxyUtils::InputLayerProxySequence<TopologyGeometryResolverLayerProxy>` | private | Used to get surface resolved topology boundary surfaces to calculate velocities \*on\*. |
| `d_current_surface_topological_network_resolver_layer_proxies` | field | `LayerProxyUtils::InputLayerProxySequence<TopologyNetworkResolverLayerProxy>` | private | Used to get surface resolved topology network surfaces to calculate velocities on. |
| `d_current_domain_reconstruct_layer_proxies` | field | `LayerProxyUtils::InputLayerProxySequence<ReconstructLayerProxy>` | private | Used to get domain reconstructed geometries to calculate velocities at. |
| `d_current_domain_topological_geometry_resolver_layer_proxies` | field | `LayerProxyUtils::InputLayerProxySequence<TopologyGeometryResolverLayerProxy>` | private | Used to get domain resolved topological geometries to calculate velocities at. |
| `d_current_domain_topological_network_resolver_layer_proxies` | field | `LayerProxyUtils::InputLayerProxySequence<TopologyNetworkResolverLayerProxy>` | private | Used to get domain resolved topological network boundaries to calculate velocities at. |
| `d_current_reconstruction_time` | field | `double` | private | The current reconstruction time as set by the layer system. |
| `d_current_velocity_params` | field | `VelocityParams` | private | The current velocity parameters as set by the layer system. |
| `d_cached_velocities` | field | `velocity_cache_type` | private | The velocities cached according to reconstruction time and velocity params. |
| `d_subject_token` | field | `GPlatesUtils::SubjectToken` | private | Used to notify polling observers that we've been updated. |
| `VelocityFieldCalculatorLayerProxy( const VelocityParams &velocity_params, unsigned int max_num_velocity_results_in_cache)` | constructor | `None` | private | — |
| `reset_cache()` | method | `void` | private | Resets any cached variables forcing them to be recalculated next time they're accessed. |
| `check_input_layer_proxy( InputLayerProxyWrapperType &input_layer_proxy_wrapper)` | method | `void` | private | Checks if the specified input layer proxy has changed. |
| `check_input_layer_proxies()` | method | `void` | private | Checks if any input layer proxies have changed. |
| `cache_velocities` | field | `std::vector<MultiPointVectorField::non_null_ptr_type>` | private | Generates velocities for the specified velocity params and reconstruction time if they're not already cached. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_VELOCITYFIELDCALCULATORLAYERPROXY_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/VelocityFieldCalculatorLayerProxy tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/VelocityFieldCalculatorLayerTask](VelocityFieldCalculatorLayerTask.md) | app-logic | 15 |
| [gui/ExportNetRotationAnimationStrategy](../gui/ExportNetRotationAnimationStrategy.md) | gui | 2 |
| [gui/ExportVelocityAnimationStrategy](../gui/ExportVelocityAnimationStrategy.md) | gui | 2 |
| [presentation/LayerOutputRenderer](../presentation/LayerOutputRenderer.md) | presentation | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/VelocityFieldCalculatorLayerProxy.h
python scripts/gpq.py def GPlatesAppLogic::VelocityFieldCalculatorLayerProxy --body
python scripts/gpq.py uses VelocityFieldCalculatorLayerProxy --kind class
python scripts/gpq.py hier VelocityFieldCalculatorLayerProxy
```
