# ReconstructionLayerParams

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 628 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructionLayerParams.h` | C++ | 124 |

## Overview

[[[PROSE overview unit=app-logic/ReconstructionLayerParams tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructionLayerParams`](#gplatesapplogicreconstructionlayerparams) | class | [`LayerParams`](LayerParams.md) | — | 0 | App-logic parameters for a reconstruction layer. |

## Members

### `GPlatesAppLogic::ReconstructionLayerParams`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ReconstructionLayerParams>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ReconstructionLayerParams>` | public | — |
| `create()` | method | `non_null_ptr_type` | public | — |
| `set_reconstruction_params( const ReconstructionParams &reconstruction_params)` | method | `void` | public | Sets the reconstruction parameters. |
| `accept_visitor( ConstLayerParamsVisitor &visitor)` | method | `void` | public | Override of virtual method in LayerParams base. |
| `accept_visitor( LayerParamsVisitor &visitor)` | method | `void` | public | Override of virtual method in LayerParams base. |
| `modified_reconstruction_params( GPlatesAppLogic::ReconstructionLayerParams &layer_params)` | method | `void` | public | Emitted when set\_reconstruction\_params has been called (if a change detected). |
| `d_reconstruction_params` | field | `ReconstructionParams` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTIONLAYERPARAMS_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/ReconstructionLayerParams tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructionLayerTask](ReconstructionLayerTask.md) | app-logic | 3 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 2 |
| [qt-widgets/ReconstructionLayerOptionsWidget](../qt-widgets/ReconstructionLayerOptionsWidget.md) | qt-widgets | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructionLayerParams.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructionLayerParams --body
python scripts/gpq.py uses ReconstructionLayerParams --kind class
python scripts/gpq.py hier ReconstructionLayerParams
```
