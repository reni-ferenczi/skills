# VelocityFieldCalculatorLayerParams

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 1422 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/VelocityFieldCalculatorLayerParams.h` | C++ | 118 |
| `src/app-logic/VelocityFieldCalculatorLayerParams.cc` | C++ | 42 |

## Overview

[[[PROSE overview unit=app-logic/VelocityFieldCalculatorLayerParams tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::VelocityFieldCalculatorLayerParams`](#gplatesapplogicvelocityfieldcalculatorlayerparams) | class | [`LayerParams`](LayerParams.md) | — | 0 | App-logic parameters for a velocity layer. |

## Members

### `GPlatesAppLogic::VelocityFieldCalculatorLayerParams`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<VelocityFieldCalculatorLayerParams>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const VelocityFieldCalculatorLayerParams>` | public | — |
| `create()` | method | `non_null_ptr_type` | public | — |
| `set_velocity_params( const VelocityParams &velocity_params)` | method | `void` | public | Sets the velocity parameters. |
| `accept_visitor( ConstLayerParamsVisitor &visitor)` | method | `void` | public | Override of virtual method in LayerParams base. |
| `accept_visitor( LayerParamsVisitor &visitor)` | method | `void` | public | Override of virtual method in LayerParams base. |
| `modified_velocity_params( GPlatesAppLogic::VelocityFieldCalculatorLayerParams &layer_params)` | method | `void` | public | Emitted when set\_velocity\_params has been called (if a change detected). |
| `d_velocity_params` | field | `VelocityParams` | private | — |
| `VelocityFieldCalculatorLayerParams()` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_VELOCITYFIELDCALCULATORLAYERPARAMS_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/VelocityFieldCalculatorLayerParams tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/VelocityFieldCalculatorLayerOptionsWidget](../qt-widgets/VelocityFieldCalculatorLayerOptionsWidget.md) | qt-widgets | 7 |
| [app-logic/VelocityFieldCalculatorLayerTask](VelocityFieldCalculatorLayerTask.md) | app-logic | 3 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/VelocityFieldCalculatorLayerParams.h
python scripts/gpq.py def GPlatesAppLogic::VelocityFieldCalculatorLayerParams --body
python scripts/gpq.py uses VelocityFieldCalculatorLayerParams --kind class
python scripts/gpq.py hier VelocityFieldCalculatorLayerParams
```
