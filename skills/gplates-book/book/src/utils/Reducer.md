# Reducer

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 960 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/Reducer.h` | C++ | 73 |

## Overview

A template base class that defines the interface for reduction operations over a range of values. Subclasses implement `operator()` to take a pair of iterators and produce a single output value of type `OutputDataType`. The template automatically deduces `InputValueType` from the iterator type, whether it is a pointer iterator or a standard iterator with a `value_type` member. This serves as the functional interface used by more specialized reducer implementations.

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

*None.*

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
