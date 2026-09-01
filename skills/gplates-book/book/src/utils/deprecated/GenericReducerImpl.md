# GenericReducerImpl

[Book TOC](../../../TOC.md) · [utils](../../../components/utils.md) · cluster Community 1863 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/deprecated/GenericReducerImpl.h` | C++ | 55 |

## Overview

`GenericReducerImpl` is an abstract template base class that defines the interface for implementation functors used by `GenericReducer`. It declares a single virtual operator() that accepts an input iterator pair and returns a single value of the specified output type. Subclasses implement the actual reduction algorithm that combines multiple inputs into one output.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::GenericReducerImpl`](#gplatesutilsgenericreducerimpl) | class | — | `< class InputIterator, class OutputDataType>` | 0 | TODO: comments.... |

## Members

### `GPlatesUtils::GenericReducerImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator()( InputIterator input_begin, InputIterator input_end)` | operator | `OutputDataType` | public | TODO: comments.... |
| `~GenericReducerImpl()` | destructor | `None` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_GENERICREDUCERIMPL_H` | macro | `None` | — |

## Notes

*None.*

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/deprecated/GenericReducerImpl.h
python scripts/gpq.py def GPlatesUtils::GenericReducerImpl --body
python scripts/gpq.py uses GenericReducerImpl --kind class
python scripts/gpq.py hier GenericReducerImpl
```
