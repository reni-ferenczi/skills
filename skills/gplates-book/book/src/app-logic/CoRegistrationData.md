# CoRegistrationData

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 454 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/CoRegistrationData.h` | C++ | 132 |
| `src/app-logic/CoRegistrationData.cc` | C++ | 46 |

## Overview

[[[PROSE overview unit=app-logic/CoRegistrationData tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::CoRegistrationData`](#gplatesapplogiccoregistrationdata) | class | [`ReconstructionGeometry`](ReconstructionGeometry.md) | — | 0 | CoRegistrationData defines a derived class of ReconstructionGeometry. |

## Members

### `GPlatesAppLogic::CoRegistrationData`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<CoRegistrationData>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const CoRegistrationData>` | public | — |
| `create( const double &reconstruction_time)` | method | `non_null_ptr_type` | public | Creates a new CoRegistrationData object. |
| `~CoRegistrationData()` | destructor | `None` | public | — |
| `get_non_null_pointer_to_const()` | method | `non_null_ptr_to_const_type` | public | — |
| `get_non_null_pointer()` | method | `non_null_ptr_type` | public | — |
| `accept_visitor( ConstReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ConstReconstructionGeometryVisitor instance. |
| `accept_visitor( ReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ReconstructionGeometryVisitor instance. |
| `d_table` | field | `GPlatesDataMining::DataTable` | private | — |
| `CoRegistrationData( const double &reconstruction_time_)` | constructor | `None` | private | Constructor is private so it cannot be created on the runtime stack which could cause problems if a client then tries to get a non\_null\_ptr\_type from the stack object. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_COREGISTRATIONDATA_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/CoRegistrationData tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/CoRegistrationLayerProxy](CoRegistrationLayerProxy.md) | app-logic | 52 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 34 |
| [data-mining/DataSelector](../data-mining/DataSelector.md) | data-mining | 24 |
| [app-logic/CoRegistrationLayerTask](CoRegistrationLayerTask.md) | app-logic | 20 |
| [api/CoReg](../api/CoReg.md) | api | 17 |
| [gui/CommandServer](../gui/CommandServer.md) | gui | 16 |
| [data-mining/LookupReducer](../data-mining/LookupReducer.md) | data-mining | 13 |
| [data-mining/RFGToRelationalPropertyMapper](../data-mining/RFGToRelationalPropertyMapper.md) | data-mining | 9 |
| [gui/ExportCoRegistrationAnimationStrategy](../gui/ExportCoRegistrationAnimationStrategy.md) | gui | 6 |
| [qt-widgets/CoRegistrationResultTableDialog](../qt-widgets/CoRegistrationResultTableDialog.md) | qt-widgets | 6 |
| [api/PyCoregistrationLayerProxy](../api/PyCoregistrationLayerProxy.md) | api | 4 |
| [data-mining/DataMiningUtils](../data-mining/DataMiningUtils.md) | data-mining | 3 |
| [unit-test/CoregTest](../unit-test/CoregTest.md) | unit-test | 2 |
| [data-mining/RFGToPropertyValueMapper](../data-mining/RFGToPropertyValueMapper.md) | data-mining | 1 |
| [data-mining/deprecated/DataOperator](../data-mining/deprecated/DataOperator.md) | data-mining | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/CoRegistrationData.h
python scripts/gpq.py def GPlatesAppLogic::CoRegistrationData --body
python scripts/gpq.py uses CoRegistrationData --kind class
python scripts/gpq.py hier CoRegistrationData
```
