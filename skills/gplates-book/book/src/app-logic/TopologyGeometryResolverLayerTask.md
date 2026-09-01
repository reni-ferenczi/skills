# TopologyGeometryResolverLayerTask

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 575 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/TopologyGeometryResolverLayerTask.h` | C++ | 207 |
| `src/app-logic/TopologyGeometryResolverLayerTask.cc` | C++ | 359 |

## Overview

[[[PROSE overview unit=app-logic/TopologyGeometryResolverLayerTask tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::TopologyGeometryResolverLayerTask`](#gplatesapplogictopologygeometryresolverlayertask) | class | [`LayerTask`](LayerTask.md) | — | 0 | A layer task that resolves topological geometries (boundaries and lines) from feature collection(s) containing topological geometries. |

## Members

### `GPlatesAppLogic::TopologyGeometryResolverLayerTask`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `can_process_feature_collection( const GPlatesModel::FeatureCollectionHandle::const_weak_ref &feature_collection)` | method | `bool` | public | — |
| `create_layer_task()` | method | `boost::shared_ptr<TopologyGeometryResolverLayerTask>` | public | — |
| `~TopologyGeometryResolverLayerTask()` | destructor | `None` | public | — |
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
| `d_layer_params` | field | `LayerParams::non_null_ptr_type` | private | — |
| `d_default_reconstruction_layer_proxy` | field | `ReconstructionLayerProxy::non_null_ptr_type` | private | Keep track of the default reconstruction layer proxy. |
| `d_using_default_reconstruction_layer_proxy` | field | `bool` | private | Are we using the default reconstruction layer proxy. |
| `d_current_reconstructed_geometry_topological_sections_layer_proxies` | field | `std::vector<ReconstructLayerProxy::non_null_ptr_type>` | private | Any currently connected 'reconstructed geometry' topological section layers. |
| `d_current_resolved_line_topological_sections_layer_proxies` | field | `std::vector<TopologyGeometryResolverLayerProxy::non_null_ptr_type>` | private | Any currently connected 'resolved line' topological section layers. |
| `d_topology_geometry_resolver_layer_proxy` | field | `TopologyGeometryResolverLayerProxy::non_null_ptr_type` | private | Does all the resolving. |
| `TopologyGeometryResolverLayerTask()` | constructor | `None` | private | Constructor. |
| `connected_to_topological_section_layers()` | method | `bool` | private | Returns true if any topological section layers are currently connected. |
| `get_reconstructed_geometry_topological_sections_layer_proxies( std::vector<ReconstructLayerProxy::non_null_ptr_type> & reconstructed_geometry_topological_sections_layer_proxies, const Reconstruction::non_null_ptr_type &reconstruction)` | method | `void` | private | Returns the 'reconstructed geometry' topological section layers. |
| `get_resolved_line_topological_sections_layer_proxies( std::vector<TopologyGeometryResolverLayerProxy::non_null_ptr_type> & resolved_line_topological_sections_layer_proxies, const Reconstruction::non_null_ptr_type &reconstruction)` | method | `void` | private | Returns the 'resolved line' topological section layers. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_TOPOLOGYGEOMETRYRESOLVERLAYERTASK_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/TopologyGeometryResolverLayerTask tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/LayerTaskRegistry](LayerTaskRegistry.md) | app-logic | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/TopologyGeometryResolverLayerTask.h
python scripts/gpq.py def GPlatesAppLogic::TopologyGeometryResolverLayerTask --body
python scripts/gpq.py uses TopologyGeometryResolverLayerTask --kind class
python scripts/gpq.py hier TopologyGeometryResolverLayerTask
```
