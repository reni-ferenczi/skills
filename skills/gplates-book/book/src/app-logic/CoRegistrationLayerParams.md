# CoRegistrationLayerParams

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 1471 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/CoRegistrationLayerParams.h` | C++ | 119 |
| `src/app-logic/CoRegistrationLayerParams.cc` | C++ | 42 |

## Overview

[[[PROSE overview unit=app-logic/CoRegistrationLayerParams tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::CoRegistrationLayerParams`](#gplatesapplogiccoregistrationlayerparams) | class | [`LayerParams`](LayerParams.md) | — | 0 | App-logic parameters for a co-registration layer. |

## Members

### `GPlatesAppLogic::CoRegistrationLayerParams`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<CoRegistrationLayerParams>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const CoRegistrationLayerParams>` | public | — |
| `create()` | method | `non_null_ptr_type` | public | — |
| `set_cfg_table( const GPlatesDataMining::CoRegConfigurationTable &table)` | method | `void` | public | Sets the configuration table. |
| `accept_visitor( ConstLayerParamsVisitor &visitor)` | method | `void` | public | Override of virtual method in LayerParams base. |
| `accept_visitor( LayerParamsVisitor &visitor)` | method | `void` | public | Override of virtual method in LayerParams base. |
| `modified_cfg_table( GPlatesAppLogic::CoRegistrationLayerParams &layer_params)` | method | `void` | public | Emitted when set\_cfg\_table has been called (if a change detected). |
| `d_cfg_table` | field | `GPlatesDataMining::CoRegConfigurationTable` | private | — |
| `CoRegistrationLayerParams()` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_COREGISTRATIONLAYERPARAMS_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/CoRegistrationLayerParams tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 23 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 12 |
| [app-logic/CoRegistrationLayerTask](CoRegistrationLayerTask.md) | app-logic | 6 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/CoRegistrationLayerParams.h
python scripts/gpq.py def GPlatesAppLogic::CoRegistrationLayerParams --body
python scripts/gpq.py uses CoRegistrationLayerParams --kind class
python scripts/gpq.py hier CoRegistrationLayerParams
```
