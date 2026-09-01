# ReconstructionParams

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 628 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructionParams.h` | C++ | 92 |
| `src/app-logic/ReconstructionParams.cc` | C++ | 79 |

## Overview

`ReconstructionParams` is a small value type holding the one user-configurable setting a rotation layer needs beyond its input feature collections and time/anchor state: whether `ReconstructionGraphBuilder` should extend each moving-plate rotation sequence back to the distant past rather than letting it end at its oldest data point. It is passed into `ReconstructionLayerProxy::set_current_reconstruction_params` and stored per-layer by `ReconstructionLayerTask`/`ReconstructionLayerParams`, and its `boost::less_than_comparable`/`boost::equality_comparable` mixins let a layer proxy cheaply detect "params unchanged" and skip invalidating its cached reconstruction trees.

Its `transcribe` method participates in the `GPlatesScribe` serialisation used for sessions and projects; on a failed read it falls back to a default-constructed instance's value rather than failing the whole transcription, which is what lets older or newer saved sessions load even if this parameter set gains or loses fields in a future version.

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

- Defaults to `extend_total_reconstruction_poles_to_distant_past = false`, preserving the original behaviour of respecting each sequence's own time range.
- A transcription failure for the one stored field is not treated as an error: it is replaced with the default-constructed value so forward/backward compatibility across GPlates versions is preserved.

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
