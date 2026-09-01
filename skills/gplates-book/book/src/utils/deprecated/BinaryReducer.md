# BinaryReducer

[Book TOC](../../../TOC.md) · [utils](../../../components/utils.md) · cluster Community 960 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/deprecated/BinaryReducer.h` | C++ | 82 |

## Overview

`BinaryReducer` is a deprecated template class that reduces a sequence of values to a single result by applying a user-supplied binary function. It iterates through the input range, starting with the first element, and pairwise applies the binary function to accumulate a result. The binary function takes two elements and returns an accumulated value of the output type.

This class is part of a deprecated reduction framework and is no longer used in the codebase.

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

The input range must not be empty; the reduction will crash if passed an empty range.

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
