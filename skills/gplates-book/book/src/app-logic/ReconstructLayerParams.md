# ReconstructLayerParams

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 1247 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructLayerParams.h` | C++ | 154 |
| `src/app-logic/ReconstructLayerParams.cc` | C++ | 42 |

## Overview

`ReconstructLayerParams` is the `LayerParams` a reconstruct layer exposes to its options widget: it wraps a `ReconstructParams` value (the actual reconstruction settings, such as whether to use topology reconstruction) plus one UI-facing flag, `d_prompt_to_change_topology_reconstruction_parameters`, that controls whether switching to topology reconstruction should first prompt the user to review its parameters. Both setters are change-guarded, only writing the new value and emitting a signal (`modified_reconstruct_params`/the inherited `modified`) when the value actually differs from the current one.

The prompt flag exists specifically to avoid a double wait: since initialising topology reconstruction can be slow, giving the user a chance to fix its parameters before that initialisation runs (rather than after) avoids paying the initialisation cost twice — once on enabling it, once again after the user changes a parameter and it re-initialises.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructLayerParams`](#gplatesapplogicreconstructlayerparams) | class | [`LayerParams`](LayerParams.md) | — | 0 | App-logic parameters for a reconstruct layer. |

## Members

### `GPlatesAppLogic::ReconstructLayerParams`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ReconstructLayerParams>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ReconstructLayerParams>` | public | — |
| `create()` | method | `non_null_ptr_type` | public | — |
| `set_reconstruct_params( const ReconstructParams &reconstruct_params)` | method | `void` | public | Sets the reconstruct parameters. |
| `get_prompt_to_change_topology_reconstruction_parameters()` | method | `bool` | public | Whether to bring up the Set Topology Reconstruction Parameters dialog when selecting to reconstruct with topologies. |
| `set_prompt_to_change_topology_reconstruction_parameters( bool prompt_to_change_parameters)` | method | `void` | public | — |
| `accept_visitor( ConstLayerParamsVisitor &visitor)` | method | `void` | public | Override of virtual method in LayerParams base. |
| `accept_visitor( LayerParamsVisitor &visitor)` | method | `void` | public | Override of virtual method in LayerParams base. |
| `modified_reconstruct_params( GPlatesAppLogic::ReconstructLayerParams &layer_params)` | method | `void` | public | Emitted when set\_reconstruct\_params has been called (if a change detected). |
| `d_reconstruct_params` | field | `ReconstructParams` | private | — |
| `d_prompt_to_change_topology_reconstruction_parameters` | field | `bool` | private | Whether to bring up the Set Topology Reconstruction Parameters dialog when selecting to reconstruct with topologies. |
| `ReconstructLayerParams()` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTLAYERPARAMS_H` | macro | `None` | — |

## Notes

`d_prompt_to_change_topology_reconstruction_parameters` defaults to `true` on construction, so a freshly created reconstruct layer prompts the first time topology reconstruction is enabled.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ReconstructLayerOptionsWidget](../qt-widgets/ReconstructLayerOptionsWidget.md) | qt-widgets | 6 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 4 |
| [app-logic/ReconstructLayerTask](ReconstructLayerTask.md) | app-logic | 3 |
| [qt-widgets/GenerateDeformingMeshPointsDialog](../qt-widgets/GenerateDeformingMeshPointsDialog.md) | qt-widgets | 3 |
| [qt-widgets/SetTopologyReconstructionParametersDialog](../qt-widgets/SetTopologyReconstructionParametersDialog.md) | qt-widgets | 2 |
| [qt-widgets/SetVGPVisibilityDialog](../qt-widgets/SetVGPVisibilityDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructLayerParams.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructLayerParams --body
python scripts/gpq.py uses ReconstructLayerParams --kind class
python scripts/gpq.py hier ReconstructLayerParams
```
