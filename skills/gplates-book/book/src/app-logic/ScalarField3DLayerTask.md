# ScalarField3DLayerTask

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 897 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ScalarField3DLayerTask.h` | C++ | 156 |
| `src/app-logic/ScalarField3DLayerTask.cc` | C++ | 362 |

## Overview

`ScalarField3DLayerTask` manages a 3D scalar field for volume rendering visualization. The task accepts a scalar field feature from a file and optionally connects to multiple `ReconstructLayerProxy`, `TopologyGeometryResolverLayerProxy`, or `TopologyNetworkResolverLayerProxy` layers to provide cross-sections and surface polygon masks for visualization. The actual 3D field processing is delegated to `ScalarField3DLayerProxy`, which computes and caches the scalar field data at each reconstruction time.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ScalarField3DLayerTask`](#gplatesapplogicscalarfield3dlayertask) | class | [`LayerTask`](LayerTask.md) | — | 0 | A layer task for a 3D scalar field to be visualised using volume rendering. |

## Members

### `GPlatesAppLogic::ScalarField3DLayerTask`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `can_process_feature_collection( const GPlatesModel::FeatureCollectionHandle::const_weak_ref &feature_collection)` | method | `bool` | public | — |
| `create_layer_task()` | method | `boost::shared_ptr<ScalarField3DLayerTask>` | public | — |
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
| `d_layer_params` | field | `ScalarField3DLayerParams::non_null_ptr_type` | private | Extra parameters for this layer. |
| `d_scalar_field_layer_proxy` | field | `ScalarField3DLayerProxy::non_null_ptr_type` | private | — |
| `ScalarField3DLayerTask()` | constructor | `None` | private | Constructor. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_SCALARFIELD3DLAYERTASK_H` | macro | `None` | — |

## Notes

The scalar field feature collection is expected to contain exactly one feature; collections with zero or multiple features are handled with warnings and the task uses only the first feature. Unlike most layer tasks, this one does not require a reconstruction layer input.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/LayerTaskRegistry](LayerTaskRegistry.md) | app-logic | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ScalarField3DLayerTask.h
python scripts/gpq.py def GPlatesAppLogic::ScalarField3DLayerTask --body
python scripts/gpq.py uses ScalarField3DLayerTask --kind class
python scripts/gpq.py hier ScalarField3DLayerTask
```
