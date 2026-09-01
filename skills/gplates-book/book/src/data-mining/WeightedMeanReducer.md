# WeightedMeanReducer

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 1751 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/WeightedMeanReducer.h` | C++ | 52 |

## Overview

A stub reducer for co-registration that is currently unimplemented. The `exec()` method is intended to compute weighted means of opaque data values, but currently returns a placeholder message. The reducer is registered with the factory but awaits implementation.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::WeightedMeanReducer`](#gplatesdataminingweightedmeanreducer) | class | [`CoRegReducer`](CoRegReducer.md) | — | 0 | — |

## Members

### `GPlatesDataMining::WeightedMeanReducer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `exec( CoRegReducer::ReducerInDataset::const_iterator input_begin, CoRegReducer::ReducerInDataset::const_iterator input_end)` | method | `OpaqueData` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_WEIGHTEDMEANREDUCER_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [data-mining/CoRegFilterMapReduceFactory](CoRegFilterMapReduceFactory.md) | data-mining | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/WeightedMeanReducer.h
python scripts/gpq.py def GPlatesDataMining::WeightedMeanReducer --body
python scripts/gpq.py uses WeightedMeanReducer --kind class
python scripts/gpq.py hier WeightedMeanReducer
```
