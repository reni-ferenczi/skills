# Prospector

[Book TOC](../../../TOC.md) · [data-mining](../../../components/data-mining.md) · cluster Community 397 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/deprecated/Prospector.h` | C++ | 47 |

## Overview

A deprecated abstract base class that defines the interface for prospector jobs. Subclasses implement `do_job()` to perform some work, likely as part of a task queue or data mining workflow.

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

*None.*

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
