# FilterMapReduceWorkFlow

[Book TOC](../../../TOC.md) · [utils](../../../components/utils.md) · cluster Community 741 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/deprecated/FilterMapReduceWorkFlow.h` | C++ | 152 |

## Overview

[[[PROSE overview unit=utils/deprecated/FilterMapReduceWorkFlow tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=utils/deprecated/FilterMapReduceWorkFlow tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
