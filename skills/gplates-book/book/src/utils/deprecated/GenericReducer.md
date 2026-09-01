# GenericReducer

[Book TOC](../../../TOC.md) · [utils](../../../components/utils.md) · cluster Community 960 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/deprecated/GenericReducer.h` | C++ | 76 |

## Overview

`GenericReducer` is a concrete template that implements the abstract `Reducer` interface by accepting a user-provided implementation functor as a template parameter. It combines a sequence of input elements into a single output value of a specified type, delegating the actual reduction algorithm to the implementation callable. This allows flexible reduction strategies to be composed at compile time.

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

*None.*

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
