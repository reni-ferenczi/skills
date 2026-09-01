# CoRegistrationLayerTask

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 804 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/CoRegistrationLayerTask.h` | C++ | 166 |
| `src/app-logic/CoRegistrationLayerTask.cc` | C++ | 249 |

## Overview

`CoRegistrationLayerTask` is the `LayerTask` that wires a co-registration layer into
`ReconstructGraph`: it owns the layer's `CoRegistrationLayerParams` (the user's
configuration table) and its `CoRegistrationLayerProxy` (the worker that actually
performs the query), and forwards changes between the reconstruct-graph plumbing and
the two. It takes no feature-collection input directly —
`get_main_input_feature_collection_channel()` returns `LayerInputChannelName::UNUSED`
and `can_process_feature_collection()` always returns false — because a co-registration
layer only ever connects to *other layers'* output through
`add_input_layer_proxy_connection()`: `CO_REGISTRATION_SEED_GEOMETRIES` accepts a
`ReconstructLayerProxy`, and `CO_REGISTRATION_TARGET_GEOMETRIES` accepts either a
`ReconstructLayerProxy` or a `RasterLayerProxy`, both forwarded to the corresponding
`add_coregistration_*_layer_proxy()` calls on the underlying layer proxy.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::CoRegistrationLayerTask`](#gplatesapplogiccoregistrationlayertask) | class | `QObject`<br>[`LayerTask`](LayerTask.md) | — | 0 | A layer task that co-registers reconstructed seed geometries with reconstructed target features. |

## Members

### `GPlatesAppLogic::CoRegistrationLayerTask`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `can_process_feature_collection( const GPlatesModel::FeatureCollectionHandle::const_weak_ref &feature_collection)` | method | `bool` | public | — |
| `create_layer_task()` | method | `boost::shared_ptr<CoRegistrationLayerTask>` | public | — |
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
| `handle_cfg_table_modified( GPlatesAppLogic::CoRegistrationLayerParams &layer_params)` | method | `void` | private | — |
| `d_layer_params` | field | `CoRegistrationLayerParams::non_null_ptr_type` | private | — |
| `d_coregistration_layer_proxy` | field | `CoRegistrationLayerProxy::non_null_ptr_type` | private | Does the co-registration. |
| `CoRegistrationLayerTask()` | constructor | `None` | private | Constructor. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_COREGISTRATIONLAYERTASK_H` | macro | `None` | — |

## Notes

`update()` only pushes the current reconstruction time into the layer proxy; it does
not compute co-registration results itself — clients such as the co-registration
results dialog or the export pipeline must query `get_layer_proxy()` directly.
`remove_input_layer_proxy_connection()` also prunes the configuration table: when a
target layer is disconnected, any configuration row whose `target_layer` resolves to
that same layer proxy (or to no output at all, e.g. because the layer was deactivated
first) is dropped and the pruned table is pushed back through
`CoRegistrationLayerParams::set_cfg_table()`, which is what triggers
`handle_cfg_table_modified()` to refresh the layer proxy's configuration.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/LayerTaskRegistry](LayerTaskRegistry.md) | app-logic | 12 |
| [presentation/VisualLayerRegistry](../presentation/VisualLayerRegistry.md) | presentation | 2 |
| [qt-widgets/CoRegistrationOptionsWidget](../qt-widgets/CoRegistrationOptionsWidget.md) | qt-widgets | 1 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_layer_params.get()` | `modified_cfg_table(GPlatesAppLogic::CoRegistrationLayerParams &)` | `this` | `handle_cfg_table_modified(GPlatesAppLogic::CoRegistrationLayerParams &)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/CoRegistrationLayerTask.h
python scripts/gpq.py def GPlatesAppLogic::CoRegistrationLayerTask --body
python scripts/gpq.py uses CoRegistrationLayerTask --kind class
python scripts/gpq.py hier CoRegistrationLayerTask
```
