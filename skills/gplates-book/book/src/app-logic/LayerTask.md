# LayerTask

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 1244 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/LayerTask.h` | C++ | 199 |

## Overview

`LayerTask` is the abstract interface every concrete layer implementation (reconstruct, raster, topology resolver, velocity calculator, co-registration, and so on) implements to plug into `ReconstructGraph`. It declares its own `LayerInputChannelType` set and main input channel, receives file and layer-proxy connect/disconnect notifications on those channels, and exposes a `LayerProxy` at its output plus a `LayerParams` for its configuration — the graph and `Layer` wrapper drive a task purely through this interface, never through a concrete subclass.

`update()` is the task's one hook to react to anything it did not directly observe through the connection methods: a reconstruction time or anchored plate change, a model edit, or a change propagating from a dependent layer — the task is expected to flush any cached internal state affected by such changes. The `LayerTaskType` returned by `get_layer_type()` exists mainly so the GUI can pick the right visual representation and options widget for a given task without a subclass check.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::LayerTask`](#gplatesapplogiclayertask) | class | — | — | 9 | Abstract interface for processing input feature collections and/or the outputs of other layers (each layer has a layer proxy at its output). |

## Members

### `GPlatesAppLogic::LayerTask`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~LayerTask()` | destructor | `None` | public | — |
| `get_layer_type()` | method | `LayerTaskType::Type` | public | Returns the type of this layer task. |
| `get_input_channel_types()` | method | `std::vector<LayerInputChannelType>` | public | Returns the input channels expected by this task and the data types and arity for each channel. |
| `get_main_input_feature_collection_channel()` | method | `LayerInputChannelName::Type` | public | Returns the main input feature collection channel used by this layer task. |
| `activate( bool active)` | method | `void` | public | Activates (or deactivates) this layer tasks to reflect active state of owning layer. |
| `add_input_file_connection( LayerInputChannelName::Type input_channel_name, const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection)` | method | `void` | public | An input file has been connected on the specified input channel. |
| `remove_input_file_connection( LayerInputChannelName::Type input_channel_name, const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection)` | method | `void` | public | An input file has been disconnected on the specified input channel. |
| `modified_input_file( LayerInputChannelName::Type input_channel_name, const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection)` | method | `void` | public | An input file has been modified. |
| `add_input_layer_proxy_connection( LayerInputChannelName::Type input_channel_name, const LayerProxy::non_null_ptr_type &layer_proxy)` | method | `void` | public | The output of another layer (a layer proxy) has been connected on the specified input channel. |
| `remove_input_layer_proxy_connection( LayerInputChannelName::Type input_channel_name, const LayerProxy::non_null_ptr_type &layer_proxy)` | method | `void` | public | The output of another layer (a layer proxy) has been disconnected on the specified input channel. |
| `update( const Reconstruction::non_null_ptr_type &reconstruction)` | method | `void` | public | Update this task. |
| `get_layer_proxy()` | method | `LayerProxy::non_null_ptr_type` | public | Returns the layer proxy that clients can use to request results from this layer - typically the layer proxy does the real processing and it sits at the output of this layer in the reconstruct graph. |
| `get_layer_params()` | method | `LayerParams::non_null_ptr_type` | public | Returns the additional parameters and configuration options of this layer. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_LAYERTASK_H` | macro | `None` | — |

## Notes

The `reconstruction` passed to `update()` already contains all active layer proxies, including the task's own — a task should use it to look up other layers' current output, not to find itself. Each layer proxy tracks its own connection changes independently, so `update()` exists only to react to changes elsewhere (other layers, the model, reconstruction time/anchor); it is not the place to re-derive state already handled by the `add_input_*`/`remove_input_*` callbacks.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructGraphImpl](ReconstructGraphImpl.md) | app-logic | 8 |
| [app-logic/ReconstructGraph](ReconstructGraph.md) | app-logic | 5 |
| [app-logic/Layer](Layer.md) | app-logic | 4 |
| [presentation/DeprecatedSessionRestore](../presentation/DeprecatedSessionRestore.md) | presentation | 2 |
| [app-logic/ApplicationState](ApplicationState.md) | app-logic | 1 |
| [app-logic/CoRegistrationLayerTask](CoRegistrationLayerTask.md) | app-logic | 1 |
| [app-logic/LayerTaskRegistry](LayerTaskRegistry.md) | app-logic | 1 |
| [app-logic/RasterLayerTask](RasterLayerTask.md) | app-logic | 1 |
| [app-logic/ReconstructLayerTask](ReconstructLayerTask.md) | app-logic | 1 |
| [app-logic/ReconstructScalarCoverageLayerTask](ReconstructScalarCoverageLayerTask.md) | app-logic | 1 |
| [app-logic/ReconstructionLayerTask](ReconstructionLayerTask.md) | app-logic | 1 |
| [app-logic/ScalarField3DLayerTask](ScalarField3DLayerTask.md) | app-logic | 1 |
| [app-logic/TopologyGeometryResolverLayerTask](TopologyGeometryResolverLayerTask.md) | app-logic | 1 |
| [app-logic/TopologyNetworkResolverLayerTask](TopologyNetworkResolverLayerTask.md) | app-logic | 1 |
| [app-logic/VelocityFieldCalculatorLayerTask](VelocityFieldCalculatorLayerTask.md) | app-logic | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/LayerTask.h
python scripts/gpq.py def GPlatesAppLogic::LayerTask --body
python scripts/gpq.py uses LayerTask --kind class
python scripts/gpq.py hier LayerTask
```
