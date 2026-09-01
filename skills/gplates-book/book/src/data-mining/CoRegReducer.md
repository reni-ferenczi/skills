# CoRegReducer

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 1575 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/CoRegReducer.h` | C++ | 132 |

## Overview

[[[PROSE overview unit=data-mining/CoRegReducer tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=data-mining/CoRegReducer tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
