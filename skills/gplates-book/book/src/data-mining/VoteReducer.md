# VoteReducer

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 1750 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/VoteReducer.h` | C++ | 85 |

## Overview

Implements a reducer that determines consensus values through a voting mechanism. The `exec()` method takes a range of `OpaqueData` items, converts them to strings, and returns the most frequently occurring value. This is useful in co-registration workflows where feature attributes are being merged and a consensus or majority-rule value is needed.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::VoteReducer`](#gplatesdataminingvotereducer) | class | [`CoRegReducer`](CoRegReducer.md) | — | 0 | — |

## Members

### `GPlatesDataMining::VoteReducer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `exec( ReducerInDataset::const_iterator input_begin, ReducerInDataset::const_iterator input_end)` | method | `OpaqueData` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_VOTEREDUCER_H` | macro | `None` | — |

## Notes

The voting algorithm converts each input value to a string for comparison and counting. The implementation sorts the string values and counts consecutive equal elements to find the mode. If the input is empty, the reducer returns "N/A".

## Used by

| Unit | Component | References |
|---|---|---|
| [data-mining/CoRegFilterMapReduceFactory](CoRegFilterMapReduceFactory.md) | data-mining | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/VoteReducer.h
python scripts/gpq.py def GPlatesDataMining::VoteReducer --body
python scripts/gpq.py uses VoteReducer --kind class
python scripts/gpq.py hier VoteReducer
```
