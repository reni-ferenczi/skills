# MaxReducer

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 1525 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/MaxReducer.h` | C++ | 76 |

## Overview

A reducer that returns the maximum numeric value from a dataset. Extracts opaque data from all inputs, converts them to doubles, and returns the largest one; returns empty data if no inputs are provided.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::MaxReducer`](#gplatesdataminingmaxreducer) | class | [`CoRegReducer`](CoRegReducer.md) | — | 0 | — |

## Members

### `GPlatesDataMining::MaxReducer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Config` | class | `None` | public | — |
| `~MaxReducer()` | destructor | `None` | public | — |
| `exec( ReducerInDataset::const_iterator first, ReducerInDataset::const_iterator last)` | method | `OpaqueData` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_MAXREDUCER_H` | macro | `None` | — |

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
python scripts/gpq.py file src/data-mining/MaxReducer.h
python scripts/gpq.py def GPlatesDataMining::MaxReducer --body
python scripts/gpq.py uses MaxReducer --kind class
python scripts/gpq.py hier MaxReducer
```
