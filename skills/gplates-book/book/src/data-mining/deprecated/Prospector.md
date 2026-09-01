# Prospector

[Book TOC](../../../TOC.md) · [data-mining](../../../components/data-mining.md) · cluster Community 397 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/deprecated/Prospector.h` | C++ | 47 |

## Overview

[[[PROSE overview unit=data-mining/deprecated/Prospector tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::Prospector`](#gplatesdataminingprospector) | class | — | — | 1 | — |

## Members

### `GPlatesDataMining::Prospector`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~Prospector()` | destructor | `None` | public | — |
| `do_job()` | method | `void` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_PROSPECTOR_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=data-mining/deprecated/Prospector tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [data-mining/deprecated/TaskQueue](TaskQueue.md) | data-mining | 8 |
| [data-mining/deprecated/SubDataSelector](SubDataSelector.md) | data-mining | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/deprecated/Prospector.h
python scripts/gpq.py def GPlatesDataMining::Prospector --body
python scripts/gpq.py uses Prospector --kind class
python scripts/gpq.py hier Prospector
```
