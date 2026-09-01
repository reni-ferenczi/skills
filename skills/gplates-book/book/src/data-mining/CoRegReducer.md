# CoRegReducer

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 1575 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/CoRegReducer.h` | C++ | 132 |

## Overview

`CoRegReducer` is the abstract "reduce" stage of the co-registration pipeline, following filtering and mapping: `process()` collapses a `ReducerInDataset` — the `(OpaqueData, ReconstructedFeature)` tuples a `CoRegMapper` produced — down to a single `OpaqueData` result for a seed feature. `process()` is non-virtual and handles the empty-range case itself, returning `EmptyData`; subclasses only implement the protected `exec()` for the non-empty case. The many concrete reducers (`MaxReducer`, `MinReducer`, `MeanReducer`, `MedianReducer`, `PercentileReducer`, `VoteReducer`, `WeightedMeanReducer`, `LookupReducer`) each interpret the mapped values differently — numeric aggregation, majority vote, or nearest-value lookup — and are selected via a nested `Config` that lets the co-registration configuration table compare and identify reducer types with `is_same_type()`.

The free function `extract_opaque_data()` is a shared helper for subclasses: it strips the `ReconstructedFeature` half of each tuple and copies just the `OpaqueData` values into a plain vector, which is what most reducers actually aggregate over.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::CoRegReducer`](#gplatesdataminingcoregreducer) | class | — | — | 9 | — |
| [`GPlatesDataMining::DummyReducer`](#gplatesdataminingdummyreducer) | class | [`CoRegReducer`](CoRegReducer.md) | — | 0 | — |

## Members

### `GPlatesDataMining::CoRegReducer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `reconstructed_feature_vector_type` | typedef | `std::vector<GPlatesAppLogic::ReconstructContext::ReconstructedFeature>` | public | — |
| `ReducerInDataset` | typedef | `std::vector< boost::tuple< OpaqueData, GPlatesAppLogic::ReconstructContext::ReconstructedFeature> >` | public | — |
| `Config` | class | `None` | public | — |
| `~CoRegReducer()` | destructor | `None` | public | — |
| `process( ReducerInDataset::const_iterator first, ReducerInDataset::const_iterator last)` | method | `OpaqueData` | public | — |
| `exec( ReducerInDataset::const_iterator first, ReducerInDataset::const_iterator last)` | method | `OpaqueData` | protected | — |

### `GPlatesDataMining::DummyReducer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Config` | class | `None` | public | — |
| `exec( CoRegReducer::ReducerInDataset::const_iterator first, CoRegReducer::ReducerInDataset::const_iterator last)` | method | `OpaqueData` | protected | — |
| `~DummyReducer()` | destructor | `None` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_COREGREDUCER_H` | macro | `None` | — |
| `extract_opaque_data( CoRegReducer::ReducerInDataset::const_iterator first, CoRegReducer::ReducerInDataset::const_iterator last, std::vector<OpaqueData>& output)` | function | `void` | — |

## Notes

Subclasses must override `exec()`, not `process()`; `process()` already guarantees `first != last` before calling `exec()`, so an empty-range check inside `exec()` is redundant.

## Used by

| Unit | Component | References |
|---|---|---|
| [data-mining/LookupReducer](LookupReducer.md) | data-mining | 11 |
| [data-mining/MaxReducer](MaxReducer.md) | data-mining | 7 |
| [data-mining/MeanReducer](MeanReducer.md) | data-mining | 7 |
| [data-mining/MinReducer](MinReducer.md) | data-mining | 7 |
| [data-mining/PercentileReducer](PercentileReducer.md) | data-mining | 6 |
| [data-mining/WeightedMeanReducer](WeightedMeanReducer.md) | data-mining | 6 |
| [data-mining/MedianReducer](MedianReducer.md) | data-mining | 5 |
| [data-mining/VoteReducer](VoteReducer.md) | data-mining | 5 |
| [data-mining/CoRegFilterMapReduceFactory](CoRegFilterMapReduceFactory.md) | data-mining | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/CoRegReducer.h
python scripts/gpq.py def GPlatesDataMining::CoRegReducer --body
python scripts/gpq.py uses CoRegReducer --kind class
python scripts/gpq.py hier CoRegReducer
```
