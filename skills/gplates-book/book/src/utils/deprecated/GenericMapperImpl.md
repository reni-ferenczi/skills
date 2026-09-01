# GenericMapperImpl

[Book TOC](../../../TOC.md) · [utils](../../../components/utils.md) · cluster Community 1862 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/deprecated/GenericMapperImpl.h` | C++ | 64 |

## Overview

[[[PROSE overview unit=utils/deprecated/GenericMapperImpl tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::GenericMapperImpl`](#gplatesutilsgenericmapperimpl) | class | — | `< class InputIterator, class OutputIterator>` | 0 | TODO: comments.... |

## Members

### `GPlatesUtils::GenericMapperImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator()( InputIterator input_begin, InputIterator input_end, OutputIterator result )` | operator | `int` | public | TODO: comments.... |
| `operator()( InputIterator input_begin, InputIterator input_end, std::vector< typename OutputIterator::value_type >& result )` | operator | `int` | public | — |
| `~GenericMapperImpl()` | destructor | `None` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_GENERICTRANSFORMERIMPL_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=utils/deprecated/GenericMapperImpl tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/deprecated/GenericMapperImpl.h
python scripts/gpq.py def GPlatesUtils::GenericMapperImpl --body
python scripts/gpq.py uses GenericMapperImpl --kind class
python scripts/gpq.py hier GenericMapperImpl
```
