# MeanReducer

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 1748 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/MeanReducer.h` | C++ | 59 |

## Overview

[[[PROSE overview unit=data-mining/MeanReducer tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::MeanReducer`](#gplatesdataminingmeanreducer) | class | [`CoRegReducer`](CoRegReducer.md) | — | 0 | — |

## Members

### `GPlatesDataMining::MeanReducer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `exec( CoRegReducer::ReducerInDataset::const_iterator first, CoRegReducer::ReducerInDataset::const_iterator last)` | method | `OpaqueData` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_MEANREDUCER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=data-mining/MeanReducer tier=3]]]
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
python scripts/gpq.py file src/data-mining/MeanReducer.h
python scripts/gpq.py def GPlatesDataMining::MeanReducer --body
python scripts/gpq.py uses MeanReducer --kind class
python scripts/gpq.py hier MeanReducer
```
