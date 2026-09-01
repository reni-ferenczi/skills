# GenericMapper

[Book TOC](../../../TOC.md) · [utils](../../../components/utils.md) · cluster Community 831 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/deprecated/GenericMapper.h` | C++ | 154 |

## Overview

[[[PROSE overview unit=utils/deprecated/GenericMapper tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::GenericMapper`](#gplatesutilsgenericmapper) | class | [`Mapper< InputIterator, OutputIterator, std::vector<typename OutputIterator::value_type> >`](../Mapper.md) | `< class InputIterator, class OutputIterator, class Implementation >` | 0 | — |

## Members

### `GPlatesUtils::GenericMapper`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GenericMapper( Implementation impl)` | constructor | `None` | public | TODO: comments.... |
| `operator()( InputIterator input_begin, InputIterator input_end, OutputIterator result)` | operator | `boost::tuple< OutputIterator, //result begin OutputIterator>` | public | TODO: comments.... |
| `operator()( InputIterator input_begin, InputIterator input_end)` | operator | `boost::tuple< OutputIterator, //result begin OutputIterator>` | public | TODO: comments.... |
| `operator()( InputIterator input_begin, InputIterator input_end, std::vector<typename OutputIterator::value_type> &result)` | operator | `boost::tuple< OutputIterator, //result begin OutputIterator>` | public | TODO: comments.... |
| `operator<<( boost::tuple< InputIterator, InputIterator> )` | operator | `boost::tuple< OutputIterator, //result begin OutputIterator>` | public | TODO: comments.... |
| `d_output_data` | field | `std::vector<typename OutputIterator::value_type>` | protected | — |
| `GenericMapper()` | constructor | `None` | protected | — |
| `d_impl` | field | `Implementation` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_GENERICTRANSFORMER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=utils/deprecated/GenericMapper tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/deprecated/GenericMapper.h
python scripts/gpq.py def GPlatesUtils::GenericMapper --body
python scripts/gpq.py uses GenericMapper --kind class
python scripts/gpq.py hier GenericMapper
```
