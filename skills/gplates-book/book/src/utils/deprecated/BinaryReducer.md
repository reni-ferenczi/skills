# BinaryReducer

[Book TOC](../../../TOC.md) · [utils](../../../components/utils.md) · cluster Community 960 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/deprecated/BinaryReducer.h` | C++ | 82 |

## Overview

[[[PROSE overview unit=utils/deprecated/BinaryReducer tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::BinaryReducer`](#gplatesutilsbinaryreducer) | class | [`Reducer< InputIterator, OutputDataType >`](../Reducer.md) | `< typename InputIterator, typename OutputDataType, typename BinaryFunction = OutputDataType (*) (typename InputIterator::value_type, typename InputIterator::value_type)>` | 0 | — |

## Members

### `GPlatesUtils::BinaryReducer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `BinaryReducer( BinaryFunction binary_fun)` | constructor | `None` | public | TODO: comments.... |
| `operator()( InputIterator input_begin, InputIterator input_end )` | operator | `OutputDataType` | public | TODO: comments.... |
| `d_binary_fun` | field | `BinaryFunction` | protected | — |
| `BinaryReducer()` | constructor | `None` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_BINARYREDUCER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=utils/deprecated/BinaryReducer tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/deprecated/BinaryReducer.h
python scripts/gpq.py def GPlatesUtils::BinaryReducer --body
python scripts/gpq.py uses BinaryReducer --kind class
python scripts/gpq.py hier BinaryReducer
```
