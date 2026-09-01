# ReconstructScalarCoverageLayerTask

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 775 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructScalarCoverageLayerTask.h` | C++ | 178 |
| `src/app-logic/ReconstructScalarCoverageLayerTask.cc` | C++ | 181 |

## Overview

`ReconstructScalarCoverageLayerTask` reconstructs and evolves scalar coverage features (such as crustal thickness and topography) as a layer in the reconstruction graph. The task depends on input `ReconstructLayerProxy` layers that provide domain geometries and does not connect to feature files directly. The actual reconstruction and scalar value evolution is delegated to `ReconstructScalarCoverageLayerProxy`, which applies deformation from resolved topological networks to the scalar values over time. For scalar coverage types that do not support evolution, values remain constant across reconstruction time.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructScalarCoverageLayerTask`](#gplatesapplogicreconstructscalarcoveragelayertask) | class | `QObject`<br>[`LayerTask`](LayerTask.md) | — | 0 | A layer task that can evolve specific types of scalar coverages over time (such as crustal thickness and topography). |

## Members

### `GPlatesAppLogic::ReconstructScalarCoverageLayerTask`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `can_process_feature_collection( const GPlatesModel::FeatureCollectionHandle::const_weak_ref &feature_collection)` | method | `bool` | public | — |
| `create_layer_task()` | method | `boost::shared_ptr<ReconstructScalarCoverageLayerTask>` | public | — |
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
| `handle_reconstruct_scalar_coverage_params_modified( GPlatesAppLogic::ReconstructScalarCoverageLayerParams &layer_params)` | method | `void` | private | — |
| `d_reconstruct_scalar_coverage_layer_proxy` | field | `ReconstructScalarCoverageLayerProxy::non_null_ptr_type` | private | Evolves scalar values for coverages that support it (eg, crustal thickness). |
| `d_layer_params` | field | `ReconstructScalarCoverageLayerParams::non_null_ptr_type` | private | Parameters used when calculating reconstructed scalar coverages. |
| `ReconstructScalarCoverageLayerTask()` | constructor | `None` | private | Constructor. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTSCALARCOVERAGELAYERTASK_H` | macro | `None` | — |

## Notes

Member initialization order matters: `d_reconstruct_scalar_coverage_layer_proxy` must be created before `d_layer_params` because the params object takes the proxy as a dependency.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/LayerTaskRegistry](LayerTaskRegistry.md) | app-logic | 3 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_layer_params.get()` | `modified_reconstruct_scalar_coverage_params(GPlatesAppLogic::ReconstructScalarCoverageLayerParams &)` | `this` | `handle_reconstruct_scalar_coverage_params_modified(GPlatesAppLogic::ReconstructScalarCoverageLayerParams &)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructScalarCoverageLayerTask.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructScalarCoverageLayerTask --body
python scripts/gpq.py uses ReconstructScalarCoverageLayerTask --kind class
python scripts/gpq.py hier ReconstructScalarCoverageLayerTask
```
