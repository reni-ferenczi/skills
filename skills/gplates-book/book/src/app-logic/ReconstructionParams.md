# ReconstructionParams

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 628 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructionParams.h` | C++ | 92 |
| `src/app-logic/ReconstructionParams.cc` | C++ | 79 |

## Overview

[[[PROSE overview unit=app-logic/ReconstructionParams tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructionParams`](#gplatesapplogicreconstructionparams) | class | `boost::less_than_comparable<ReconstructionParams>`<br>`boost::equality_comparable<ReconstructionParams>` | — | 0 | ReconstructionParams is used to store additional parameters for calculating reconstruction trees in ReconstructionLayerTask layers. |

## Members

### `GPlatesAppLogic::ReconstructionParams`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ReconstructionParams()` | constructor | `None` | public | — |
| `get_extend_total_reconstruction_poles_to_distant_past()` | method | `bool` | public | Whether each moving plate rotation sequence is extended back to the distant past such that reconstructed geometries are not snapped back to their present day positions. |
| `set_extend_total_reconstruction_poles_to_distant_past( bool extend_total_reconstruction_poles_to_distant_past)` | method | `void` | public | — |
| `operator==( const ReconstructionParams &rhs)` | operator | `bool` | public | Equality comparison operator. |
| `operator<( const ReconstructionParams &rhs)` | operator | `bool` | public | Less than comparison operator. |
| `d_extend_total_reconstruction_poles_to_distant_past` | field | `bool` | private | — |
| `transcribe( GPlatesScribe::Scribe &scribe, bool transcribed_construct_data)` | method | `GPlatesScribe::TranscribeResult` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `operator==( const ReconstructionParams &rhs)` | operator | `bool` | — |
| `operator<( const ReconstructionParams &rhs)` | operator | `bool` | — |
| `GPLATES_APP_LOGIC_RECONSTRUCTIONPARAMS_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/ReconstructionParams tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructionLayerProxy](ReconstructionLayerProxy.md) | app-logic | 6 |
| [qt-widgets/ReconstructionLayerOptionsWidget](../qt-widgets/ReconstructionLayerOptionsWidget.md) | qt-widgets | 5 |
| [app-logic/ReconstructionLayerParams](ReconstructionLayerParams.md) | app-logic | 4 |
| [cli/CliAssignPlateIdsCommand](../cli/CliAssignPlateIdsCommand.md) | cli | 3 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructionParams.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructionParams --body
python scripts/gpq.py uses ReconstructionParams --kind class
python scripts/gpq.py hier ReconstructionParams
```
