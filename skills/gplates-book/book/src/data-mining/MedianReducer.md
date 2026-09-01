# MedianReducer

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 1749 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/MedianReducer.h` | C++ | 69 |

## Overview

A reducer that returns the median of numeric values from a dataset. Extracts opaque data, converts to doubles, and uses `std::nth_element` to partition around the middle position. For even-length vectors, this returns the upper median (the element at position length/2) rather than averaging the two middle elements.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::MedianReducer`](#gplatesdataminingmedianreducer) | class | [`CoRegReducer`](CoRegReducer.md) | — | 0 | — |

## Members

### `GPlatesDataMining::MedianReducer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `exec( ReducerInDataset::const_iterator in_first, ReducerInDataset::const_iterator in_last)` | method | `OpaqueData` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_MEDIANREDUCER_H` | macro | `None` | — |

## Notes

For even-length datasets, returns the upper median (element at length/2) rather than the average of the two middle values. Call `std::nth_element` once, not twice.

## Used by

| Unit | Component | References |
|---|---|---|
| [data-mining/CoRegFilterMapReduceFactory](CoRegFilterMapReduceFactory.md) | data-mining | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/MedianReducer.h
python scripts/gpq.py def GPlatesDataMining::MedianReducer --body
python scripts/gpq.py uses MedianReducer --kind class
python scripts/gpq.py hier MedianReducer
```
