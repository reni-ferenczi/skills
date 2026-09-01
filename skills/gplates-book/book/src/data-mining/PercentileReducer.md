# PercentileReducer

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 1689 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/PercentileReducer.h` | C++ | 53 |

## Overview

`PercentileReducer` is a placeholder reducer that extends `CoRegReducer` for computing percentiles from a sequence of numerical data in a co-registration pipeline. Its `exec()` method is not yet implemented and returns a stub message. It follows the same pattern as other reducers like `MinReducer` but the implementation is reserved for future work.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::PercentileReducer`](#gplatesdataminingpercentilereducer) | class | [`CoRegReducer`](CoRegReducer.md) | — | 0 | — |

## Members

### `GPlatesDataMining::PercentileReducer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `exec( CoRegReducer::ReducerInDataset::const_iterator input_begin, CoRegReducer::ReducerInDataset::const_iterator input_end)` | method | `OpaqueData` | protected | — |
| `~PercentileReducer()` | destructor | `None` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_PERCENTILEREDUCER_H` | macro | `None` | — |

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
python scripts/gpq.py file src/data-mining/PercentileReducer.h
python scripts/gpq.py def GPlatesDataMining::PercentileReducer --body
python scripts/gpq.py uses PercentileReducer --kind class
python scripts/gpq.py hier PercentileReducer
```
