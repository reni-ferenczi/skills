# UnaryMapper

[Book TOC](../../../TOC.md) · [utils](../../../components/utils.md) · cluster Community 831 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/deprecated/UnaryMapper.h` | C++ | 116 |

## Overview

[[[PROSE overview unit=utils/deprecated/UnaryMapper tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::UnaryMapper`](#gplatesutilsunarymapper) | class | [`Mapper< InputIterator, OutputIterator>`](../Mapper.md) | `< typename InputIterator, typename OutputIterator, typename UnaryFuntion = bool(*)(typename InputIterator::value_type) >` | 0 | — |

## Members

### `GPlatesUtils::UnaryMapper`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UnaryMapper( UnaryFuntion unary_fun)` | constructor | `None` | public | TODO: comments.... |
| `operator()( InputIterator input_begin, InputIterator input_end, boost::optional<OutputIterator> result = boost::none)` | operator | `boost::tuple< OutputIterator, //result begin OutputIterator>` | public | TODO: comments.... |
| `operator<<( boost::tuple< InputIterator, InputIterator> input)` | operator | `boost::tuple< OutputIterator, //result begin OutputIterator>` | public | TODO: comments.... |
| `d_unary_fun` | field | `UnaryFuntion` | protected | — |
| `UnaryMapper()` | constructor | `None` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_UNARYTRANSFORMER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=utils/deprecated/UnaryMapper tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/deprecated/UnaryMapper.h
python scripts/gpq.py def GPlatesUtils::UnaryMapper --body
python scripts/gpq.py uses UnaryMapper --kind class
python scripts/gpq.py hier UnaryMapper
```
