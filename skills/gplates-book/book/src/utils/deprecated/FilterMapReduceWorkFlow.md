# FilterMapReduceWorkFlow

[Book TOC](../../../TOC.md) · [utils](../../../components/utils.md) · cluster Community 741 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/deprecated/FilterMapReduceWorkFlow.h` | C++ | 152 |

## Overview

`FilterMapReduceWorkFlow` is a deprecated struct template that orchestrates a chain of filter and map operations followed by a final reduce step. It uses template metaprogramming with `boost::mpl::reverse_fold` to construct a pipeline where each filter/map in the input type list is applied in sequence to transform data. The output of each stage becomes the input of the next, and the final reducer is applied to the output of the last filter/map stage.

The workflow is executed by calling `exec()` with a vector of `boost::any`-wrapped filter/map objects, a reducer, and the input range. Each object in the vector is cast to its expected type at pipeline execution; any type mismatch throws `boost::bad_any_cast`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::FilterMapReduceWorkFlow`](#gplatesutilsfiltermapreduceworkflow) | struct | — | `< class FilterMapList, class ReducerType, class InputIterator, class OutputDataType >` | 0 | — |

## Members

### `GPlatesUtils::FilterMapReduceWorkFlow`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ReturnType` | typedef | `typename ReducerType::InputIteratorType` | public | — |
| `exec( std::vector< boost::any >& unit_list, ReducerType& reducer, InputIterator input_begin, InputIterator input_end)` | method | `OutputDataType` | public | The caller needs to make the unit\_list doesn't contain any invalid item( null pointer ). |
| `NullProcessUnit` | struct | `None` | public | — |
| `ProcessUnit` | struct | `None` | public | — |
| `create_workflow` | struct | `None` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_FILTERMAPREDUCEWORKFLOW_H` | macro | `None` | — |

## Notes

The caller must ensure the unit_list vector contains valid non-null pointers for all filter/map objects in the type list, in the correct order, and with types matching the FilterMapList parameter; type mismatches will be caught as `boost::bad_any_cast` exceptions at runtime.

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/FilterTest](../../unit-test/FilterTest.md) | unit-test | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/deprecated/FilterMapReduceWorkFlow.h
python scripts/gpq.py def GPlatesUtils::FilterMapReduceWorkFlow --body
python scripts/gpq.py uses FilterMapReduceWorkFlow --kind struct
python scripts/gpq.py hier FilterMapReduceWorkFlow
```
