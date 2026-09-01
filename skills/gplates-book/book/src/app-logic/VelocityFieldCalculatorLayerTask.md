# VelocityFieldCalculatorLayerTask

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 776 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/VelocityFieldCalculatorLayerTask.h` | C++ | 168 |
| `src/app-logic/VelocityFieldCalculatorLayerTask.cc` | C++ | 308 |

## Overview

A layer task that calculates velocity fields on mesh point domains inside static polygons, dynamic resolved topological polygons, or resolved topological networks. The task accepts feature collections and delegates actual calculation work to `VelocityFieldCalculatorLayerProxy`, exposing a layer proxy for downstream consumers and managing parameters through `VelocityFieldCalculatorLayerParams` with Qt signal notifications.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::VelocityFieldCalculatorLayerTask`](#gplatesapplogicvelocityfieldcalculatorlayertask) | class | `QObject`<br>[`LayerTask`](LayerTask.md) | — | 0 | A layer task that calculates velocity fields on domains of mesh points inside reconstructed static polygons, resolved topological dynamic polygons or resolved topological networks. |

## Members

### `GPlatesAppLogic::VelocityFieldCalculatorLayerTask`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `can_process_feature_collection( const GPlatesModel::FeatureCollectionHandle::const_weak_ref &feature_collection)` | method | `bool` | public | — |
| `create_layer_task()` | method | `boost::shared_ptr<VelocityFieldCalculatorLayerTask>` | public | — |
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
| `handle_velocity_params_modified( GPlatesAppLogic::VelocityFieldCalculatorLayerParams &layer_params)` | method | `void` | private | — |
| `d_layer_params` | field | `VelocityFieldCalculatorLayerParams::non_null_ptr_type` | private | Parameters used when calculating velocities. |
| `d_velocity_field_calculator_layer_proxy` | field | `VelocityFieldCalculatorLayerProxy::non_null_ptr_type` | private | Does all the velocity calculations. |
| `VelocityFieldCalculatorLayerTask()` | constructor | `None` | private | Constructor. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_VELOCITYFIELDCALCULATORLAYERTASK_H` | macro | `None` | — |

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
| `d_layer_params.get()` | `modified_velocity_params(GPlatesAppLogic::VelocityFieldCalculatorLayerParams &)` | `this` | `handle_velocity_params_modified(GPlatesAppLogic::VelocityFieldCalculatorLayerParams &)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/VelocityFieldCalculatorLayerTask.h
python scripts/gpq.py def GPlatesAppLogic::VelocityFieldCalculatorLayerTask --body
python scripts/gpq.py uses VelocityFieldCalculatorLayerTask --kind class
python scripts/gpq.py hier VelocityFieldCalculatorLayerTask
```
