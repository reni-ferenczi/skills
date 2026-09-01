# TopologyNetworkLayerParams

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 64 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/TopologyNetworkLayerParams.h` | C++ | 129 |

## Overview

`TopologyNetworkLayerParams` is the `LayerParams` subclass a topological-network layer exposes to the GUI and to session serialisation: it holds one `TopologyNetworkParams` value object (the triangulation and deformation settings) and does nothing else. `set_topology_network_params()` compares against the current value before storing and emitting `modified_topology_network_params`/`emit_modified()`, so setting the same parameters twice is a no-op — this is what lets `qt-widgets::TopologyNetworkResolverLayerOptionsWidget` push edits from its UI controls without triggering a resolve on every keystroke that didn't actually change anything.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::TopologyNetworkLayerParams`](#gplatesapplogictopologynetworklayerparams) | class | [`LayerParams`](LayerParams.md) | — | 0 | App-logic parameters for a topological network layer. |

## Members

### `GPlatesAppLogic::TopologyNetworkLayerParams`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<TopologyNetworkLayerParams>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const TopologyNetworkLayerParams>` | public | — |
| `create()` | method | `non_null_ptr_type` | public | — |
| `set_topology_network_params( const TopologyNetworkParams &topology_network_params)` | method | `void` | public | Sets the topology network parameters. |
| `accept_visitor( ConstLayerParamsVisitor &visitor)` | method | `void` | public | Override of virtual method in LayerParams base. |
| `accept_visitor( LayerParamsVisitor &visitor)` | method | `void` | public | Override of virtual method in LayerParams base. |
| `modified_topology_network_params( GPlatesAppLogic::TopologyNetworkLayerParams &layer_params)` | method | `void` | public | Emitted when set\_topology\_network\_params has been called (if a change detected). |
| `d_topology_network_params` | field | `TopologyNetworkParams` | private | — |
| `TopologyNetworkLayerParams()` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_TOPOLOGYNETWORKLAYERPARAMS_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](../qt-widgets/TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 7 |
| [app-logic/TopologyNetworkResolverLayerTask](TopologyNetworkResolverLayerTask.md) | app-logic | 3 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/TopologyNetworkLayerParams.h
python scripts/gpq.py def GPlatesAppLogic::TopologyNetworkLayerParams --body
python scripts/gpq.py uses TopologyNetworkLayerParams --kind class
python scripts/gpq.py hier TopologyNetworkLayerParams
```
