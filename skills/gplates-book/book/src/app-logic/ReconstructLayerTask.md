# ReconstructLayerTask

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 669 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructLayerTask.h` | C++ | 219 |
| `src/app-logic/ReconstructLayerTask.cc` | C++ | 371 |

## Overview

[[[PROSE overview unit=app-logic/ReconstructLayerTask tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructLayerTask`](#gplatesapplogicreconstructlayertask) | class | `QObject`<br>[`LayerTask`](LayerTask.md) | — | 0 | A layer task that reconstructs geometries of features from feature collection(s). |

## Members

### `GPlatesAppLogic::ReconstructLayerTask`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `can_process_feature_collection( const GPlatesModel::FeatureCollectionHandle::const_weak_ref &feature_collection, ApplicationState &application_state)` | method | `bool` | public | — |
| `create_layer_task( ApplicationState &application_state)` | method | `boost::shared_ptr<ReconstructLayerTask>` | public | — |
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
| `handle_reconstruct_params_modified( GPlatesAppLogic::ReconstructLayerParams &layer_params)` | method | `void` | private | — |
| `d_layer_params` | field | `ReconstructLayerParams::non_null_ptr_type` | private | Parameters used when reconstructing. |
| `d_default_reconstruction_layer_proxy` | field | `ReconstructionLayerProxy::non_null_ptr_type` | private | Keep track of the default reconstruction layer proxy. |
| `d_using_default_reconstruction_layer_proxy` | field | `bool` | private | Are we using the default reconstruction layer proxy. |
| `d_current_resolved_boundary_topology_surface_layer_proxies` | field | `std::vector<TopologyGeometryResolverLayerProxy::non_null_ptr_type>` | private | Any currently connected 'resolved boundary' topology surface layers. |
| `d_current_resolved_network_topology_surface_layer_proxies` | field | `std::vector<TopologyNetworkResolverLayerProxy::non_null_ptr_type>` | private | Any currently connected 'resolved network' topology surface layers. |
| `d_reconstruct_layer_proxy` | field | `ReconstructLayerProxy::non_null_ptr_type` | private | Does all the reconstructing. |
| `ReconstructLayerTask( const ReconstructMethodRegistry &reconstruct_method_registry)` | constructor | `None` | private | Constructor. |
| `connected_to_topology_surface_layers()` | method | `bool` | private | Returns true if any topology surface layers are currently connected. |
| `get_resolved_boundary_topology_surface_layer_proxies( std::vector<TopologyGeometryResolverLayerProxy::non_null_ptr_type> & resolved_boundary_topology_surface_layer_proxies, const Reconstruction::non_null_ptr_type &reconstruction)` | method | `void` | private | Returns the 'resolved boundary' topology surface layers. |
| `get_resolved_network_topology_surface_layer_proxies( std::vector<TopologyNetworkResolverLayerProxy::non_null_ptr_type> & resolved_network_topology_surface_layer_proxies, const Reconstruction::non_null_ptr_type &reconstruction)` | method | `void` | private | Returns the 'resolved network' topology surface layers. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTLAYERTASK_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/ReconstructLayerTask tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/LayerTaskRegistry](LayerTaskRegistry.md) | app-logic | 3 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_layer_params.get()` | `modified_reconstruct_params(GPlatesAppLogic::ReconstructLayerParams &)` | `this` | `handle_reconstruct_params_modified(GPlatesAppLogic::ReconstructLayerParams &)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructLayerTask.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructLayerTask --body
python scripts/gpq.py uses ReconstructLayerTask --kind class
python scripts/gpq.py hier ReconstructLayerTask
```
