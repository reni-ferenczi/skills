# GenericReducer

[Book TOC](../../../TOC.md) · [utils](../../../components/utils.md) · cluster Community 960 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/deprecated/GenericReducer.h` | C++ | 76 |

## Overview

[[[PROSE overview unit=utils/deprecated/GenericReducer tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::GenericReducer`](#gplatesutilsgenericreducer) | class | [`Reducer< InputIterator, OutputDataType >`](../Reducer.md) | `< class InputIterator, class OutputDataType, class Implementation>` | 0 | — |

## Members

### `GPlatesUtils::GenericReducer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GenericReducer( Implementation impl)` | constructor | `None` | public | TODO: comments.... |
| `operator()( InputIterator input_begin, InputIterator input_end)` | operator | `OutputDataType` | public | TODO: comments.... |
| `GenericReducer()` | constructor | `None` | protected | — |
| `d_impl` | field | `Implementation` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_GENERICREDUCER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=utils/deprecated/GenericReducer tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/deprecated/GenericReducer.h
python scripts/gpq.py def GPlatesUtils::GenericReducer --body
python scripts/gpq.py uses GenericReducer --kind class
python scripts/gpq.py hier GenericReducer
```
