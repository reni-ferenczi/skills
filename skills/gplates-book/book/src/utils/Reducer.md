# Reducer

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 960 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/Reducer.h` | C++ | 73 |

## Overview

[[[PROSE overview unit=utils/Reducer tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::Reducer`](#gplatesutilsreducer) | class | — | `< class InputIterator, class OutputDataType >` | 2 | TODO: comments.... |

## Members

### `GPlatesUtils::Reducer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InputValueType` | typedef | `typename boost::mpl::if_< boost::is_pointer<InputIterator>, boost::remove_pointer<InputIterator>, typename InputIterator::value_type>::type` | public | — |
| `OutputValueType` | typedef | `OutputDataType` | public | — |
| `InputIteratorType` | typedef | `InputIterator` | public | — |
| `operator()( InputIterator input_begin, InputIterator input_end)` | operator | `OutputDataType` | public | TODO: comments.... |
| `~Reducer()` | destructor | `None` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_REDUCER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=utils/Reducer tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [utils/deprecated/BinaryReducer](deprecated/BinaryReducer.md) | utils | 4 |
| [utils/deprecated/GenericReducer](deprecated/GenericReducer.md) | utils | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/Reducer.h
python scripts/gpq.py def GPlatesUtils::Reducer --body
python scripts/gpq.py uses Reducer --kind class
python scripts/gpq.py hier Reducer
```
