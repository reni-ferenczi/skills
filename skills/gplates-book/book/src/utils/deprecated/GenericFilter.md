# GenericFilter

[Book TOC](../../../TOC.md) · [utils](../../../components/utils.md) · cluster Community 770 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/deprecated/GenericFilter.h` | C++ | 155 |

## Overview

[[[PROSE overview unit=utils/deprecated/GenericFilter tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::GenericFilter`](#gplatesutilsgenericfilter) | class | `Filter< InputIterator, OutputIterator, std::vector<typename OutputIterator::value_type> >` | `< class InputIterator, class OutputIterator, class Implementation >` | 0 | — |

## Members

### `GPlatesUtils::GenericFilter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GenericFilter( Implementation impl)` | constructor | `None` | public | TODO: comments.... |
| `operator()( InputIterator input_begin, InputIterator input_end, OutputIterator result)` | operator | `boost::tuple< OutputIterator, //result begin OutputIterator>` | public | TODO: comments.... |
| `operator()( InputIterator input_begin, InputIterator input_end)` | operator | `boost::tuple< OutputIterator, //result begin OutputIterator>` | public | TODO: comments.... |
| `operator()( InputIterator input_begin, InputIterator input_end, std::vector<typename OutputIterator::value_type> &result)` | operator | `boost::tuple< OutputIterator, //result begin OutputIterator>` | public | TODO: comments.... |
| `operator<<( boost::tuple< InputIterator, InputIterator> )` | operator | `boost::tuple< OutputIterator, //result begin OutputIterator>` | public | TODO: comments.... |
| `d_impl` | field | `Implementation` | protected | — |
| `d_output_data` | field | `std::vector<typename OutputIterator::value_type>` | protected | — |
| `GenericFilter()` | constructor | `None` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_GENERICFILTER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=utils/deprecated/GenericFilter tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/deprecated/GenericFilter.h
python scripts/gpq.py def GPlatesUtils::GenericFilter --body
python scripts/gpq.py uses GenericFilter --kind class
python scripts/gpq.py hier GenericFilter
```
