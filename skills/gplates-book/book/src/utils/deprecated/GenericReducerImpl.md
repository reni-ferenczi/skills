# GenericReducerImpl

[Book TOC](../../../TOC.md) · [utils](../../../components/utils.md) · cluster Community 1863 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/deprecated/GenericReducerImpl.h` | C++ | 55 |

## Overview

[[[PROSE overview unit=utils/deprecated/GenericReducerImpl tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=utils/deprecated/GenericReducerImpl tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
