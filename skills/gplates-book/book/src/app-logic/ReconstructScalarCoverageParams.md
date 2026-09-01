# ReconstructScalarCoverageParams

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 693 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructScalarCoverageParams.h` | C++ | 69 |
| `src/app-logic/ReconstructScalarCoverageParams.cc` | C++ | 57 |

## Overview

`ReconstructScalarCoverageParams` is the parameters object `ReconstructScalarCoverageLayerProxy` and `ReconstructScalarCoverageLayerParams` hold for configuring how 2D scalar coverages are deformed/evolved. It follows the same pattern as `ReconstructParams`: a comparable, `Scribe`-transcribable value type that a layer's params can compare against to detect configuration changes and that can round-trip through sessions and projects.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructScalarCoverageParams`](#gplatesapplogicreconstructscalarcoverageparams) | class | `boost::less_than_comparable<ReconstructScalarCoverageParams>`<br>`boost::equality_comparable<ReconstructScalarCoverageParams>` | — | 0 | Used to store additional parameters for deforming/evolving 2D scalar fields. |

## Members

### `GPlatesAppLogic::ReconstructScalarCoverageParams`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator==( const ReconstructScalarCoverageParams &rhs)` | operator | `bool` | public | Equality comparison operator. |
| `operator<( const ReconstructScalarCoverageParams &rhs)` | operator | `bool` | public | Less than comparison operator. |
| `transcribe( GPlatesScribe::Scribe &scribe, bool transcribed_construct_data)` | method | `GPlatesScribe::TranscribeResult` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `operator==( const ReconstructScalarCoverageParams &rhs)` | operator | `bool` | — |
| `operator<( const ReconstructScalarCoverageParams &rhs)` | operator | `bool` | — |
| `GPLATES_APP_LOGIC_RECONSTRUCTSCALARCOVERAGEPARAMS_H` | macro | `None` | — |

## Notes

The class currently declares no data members: `operator==` unconditionally returns `true`, `operator<` unconditionally returns `false`, and `transcribe` transcribes nothing. It exists as a placeholder for scalar-coverage-evolution options that have not yet been added; do not assume it carries any configurable state today.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructScalarCoverageLayerProxy](ReconstructScalarCoverageLayerProxy.md) | app-logic | 19 |
| [app-logic/ReconstructScalarCoverageLayerParams](ReconstructScalarCoverageLayerParams.md) | app-logic | 5 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 1 |
| [qt-widgets/ReconstructScalarCoverageLayerOptionsWidget](../qt-widgets/ReconstructScalarCoverageLayerOptionsWidget.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructScalarCoverageParams.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructScalarCoverageParams --body
python scripts/gpq.py uses ReconstructScalarCoverageParams --kind class
python scripts/gpq.py hier ReconstructScalarCoverageParams
```
