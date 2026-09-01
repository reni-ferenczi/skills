# VoteReducer

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 1750 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/VoteReducer.h` | C++ | 85 |

## Overview

[[[PROSE overview unit=data-mining/VoteReducer tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=data-mining/VoteReducer tier=3]]]
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
python scripts/gpq.py file src/data-mining/VoteReducer.h
python scripts/gpq.py def GPlatesDataMining::VoteReducer --body
python scripts/gpq.py uses VoteReducer --kind class
python scripts/gpq.py hier VoteReducer
```
