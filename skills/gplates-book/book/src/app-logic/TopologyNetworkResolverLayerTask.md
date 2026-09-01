# TopologyNetworkResolverLayerTask

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 609 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/TopologyNetworkResolverLayerTask.h` | C++ | 203 |
| `src/app-logic/TopologyNetworkResolverLayerTask.cc` | C++ | 310 |

## Overview

A layer task orchestrating the resolution of topological networks from feature collections. The task manages input connections from feature collections containing network features and from upstream topological section layers (both reconstructed geometry and resolved line variants), then delegates to `TopologyNetworkResolverLayerProxy` to perform the actual resolution work.

The task exposes a `LayerProxy` for downstream consumers and maintains layer parameters via `TopologyNetworkLayerParams`, responding to parameter changes through Qt signals.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::TopologyNetworkResolverLayerTask`](#gplatesapplogictopologynetworkresolverlayertask) | class | `QObject`<br>[`LayerTask`](LayerTask.md) | — | 0 | A layer task that resolves topological network from feature collection(s) containing topological networks. |

## Members

### `GPlatesAppLogic::TopologyNetworkResolverLayerTask`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `can_process_feature_collection( const GPlatesModel::FeatureCollectionHandle::const_weak_ref &feature_collection)` | method | `bool` | public | — |
| `create_layer_task()` | method | `boost::shared_ptr<TopologyNetworkResolverLayerTask>` | public | — |
| `get_layer_type()` | method | `LayerTaskType::Type` | public | — |
| `get_input_channel_types()` | method | `std::vector<LayerInputChannelType>` | public | — |
| `get_main_input_feature_collection_channel()` | method | `LayerInputChannelName::Type` | public | — |
| `activate( bool active)` | method | `void` | public | — |
| `add_input_file_connection( LayerInputChannelName::Type input_channel_name, const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection)` | method | `void` | public | — |
| `remove_input_file_connection( LayerInputChannelName::Type input_channel_name, const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection)` | method | `void` | public | — |
| `modified_input_file( LayerInputChannelName::Type input_channel_name, const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection)` | method | `void` | public | — |
| `add_input_layer_proxy_connection( LayerInputChannelName::Type input_channel_name, const LayerProxy::non_null_ptr_type &layer_proxy)` | method | `void` | public | — |
| `remove_input_layer_proxy_connection( LayerInputChannelName::Type input_channel_name, const LayerProxy::non_null_ptr_type &layer_proxy)` | method | `void` | public | — |
| `update( const Reconstruction::non_null_ptr_type &reconstruction)` | method | `void` | public | — |
| `get_layer_proxy()` | method | `LayerProxy::non_null_ptr_type` | public | — |
| `get_layer_params()` | method | `LayerParams::non_null_ptr_type` | public | — |
| `handle_topology_network_params_modified( GPlatesAppLogic::TopologyNetworkLayerParams &layer_params)` | method | `void` | private | — |
| `d_layer_params` | field | `TopologyNetworkLayerParams::non_null_ptr_type` | private | — |
| `d_current_reconstructed_geometry_topological_sections_layer_proxies` | field | `std::vector<ReconstructLayerProxy::non_null_ptr_type>` | private | Any currently connected 'reconstructed geometry' topological section layers. |
| `d_current_resolved_line_topological_sections_layer_proxies` | field | `std::vector<TopologyGeometryResolverLayerProxy::non_null_ptr_type>` | private | Any currently connected 'resolved line' topological section layers. |
| `d_topology_network_resolver_layer_proxy` | field | `TopologyNetworkResolverLayerProxy::non_null_ptr_type` | private | Does all the resolving. |
| `TopologyNetworkResolverLayerTask()` | constructor | `None` | private | Constructor. |
| `connected_to_topological_section_layers()` | method | `bool` | private | Returns true if any topological section layers are currently connected. |
| `get_reconstructed_geometry_topological_sections_layer_proxies( std::vector<ReconstructLayerProxy::non_null_ptr_type> & reconstructed_geometry_topological_sections_layer_proxies, const Reconstruction::non_null_ptr_type &reconstruction)` | method | `void` | private | Returns the 'reconstructed geometry' topological section layers. |
| `get_resolved_line_topological_sections_layer_proxies( std::vector<TopologyGeometryResolverLayerProxy::non_null_ptr_type> & resolved_line_topological_sections_layer_proxies, const Reconstruction::non_null_ptr_type &reconstruction)` | method | `void` | private | Returns the 'resolved line' topological section layers. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_TOPOLOGYNETWORKRESOLVERLAYERTASK_H` | macro | `None` | — |
| `GPLATES_APP_LOGIC_TOPOLOGYBOUNDARYRESOLVERLAYERTASK_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/LayerTaskRegistry](LayerTaskRegistry.md) | app-logic | 3 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_layer_params.get()` | `modified_topology_network_params(GPlatesAppLogic::TopologyNetworkLayerParams &)` | `this` | `handle_topology_network_params_modified(GPlatesAppLogic::TopologyNetworkLayerParams &)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/TopologyNetworkResolverLayerTask.h
python scripts/gpq.py def GPlatesAppLogic::TopologyNetworkResolverLayerTask --body
python scripts/gpq.py uses TopologyNetworkResolverLayerTask --kind class
python scripts/gpq.py hier TopologyNetworkResolverLayerTask
```
