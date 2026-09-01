# PercentileReducer

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 1689 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/PercentileReducer.h` | C++ | 53 |

## Overview

[[[PROSE overview unit=data-mining/PercentileReducer tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=data-mining/PercentileReducer tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
