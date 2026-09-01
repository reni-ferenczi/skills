# CoRegistrationLayerParams

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 1471 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/CoRegistrationLayerParams.h` | C++ | 119 |
| `src/app-logic/CoRegistrationLayerParams.cc` | C++ | 42 |

## Overview

`CoRegistrationLayerParams` is the `LayerParams` subclass for a co-registration
layer: it holds the single piece of user-configurable state a co-registration layer
needs, a `GPlatesDataMining::CoRegConfigurationTable` describing which seed/target
features and reducers make up the co-registration query. It follows the same shape as
every other `LayerParams` subclass — private constructor reached only via `create()`,
and `accept_visitor()` double-dispatching to `visit_co_registration_layer_params()` on
`ConstLayerParamsVisitor`/`LayerParamsVisitor` so generic layer-params code (e.g.
`qt-widgets/CoRegistrationLayerConfigurationDialog`, `presentation/TranscribeSession`)
can recognise and edit or serialise it.

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

`set_cfg_table()` compares the new table against the current one and is a no-op if
they are equal, so `modified_cfg_table` and the inherited `modified` signal only fire
on an actual change.

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
