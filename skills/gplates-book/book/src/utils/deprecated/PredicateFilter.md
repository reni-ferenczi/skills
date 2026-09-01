# PredicateFilter

[Book TOC](../../../TOC.md) · [utils](../../../components/utils.md) · cluster Community 1399 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/deprecated/PredicateFilter.h` | C++ | 151 |
| `src/utils/deprecated/PredicateFilter.cc` | C++ | 25 |

## Overview

[[[PROSE overview unit=utils/deprecated/PredicateFilter tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::PredicateFilter`](#gplatesutilspredicatefilter) | class | `Filter< InputIterator, OutputIterator, std::vector<typename OutputIterator::value_type> >` | `< typename InputIterator, typename OutputIterator, typename Predicate = bool(*)(typename InputIterator::value_type)>` | 0 | — |

## Members

### `GPlatesUtils::PredicateFilter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PredicateFilter( Predicate pre)` | constructor | `None` | public | TODO: comments.... |
| `operator()( InputIterator input_begin, InputIterator input_end, OutputIterator result)` | operator | `boost::tuple< OutputIterator, //result begin OutputIterator>` | public | TODO: comments.... |
| `operator()( InputIterator input_begin, InputIterator input_end)` | operator | `boost::tuple< OutputIterator, //result begin OutputIterator>` | public | TODO: comments.... |
| `operator()( InputIterator input_begin, InputIterator input_end, std::vector<typename OutputIterator::value_type> &result)` | operator | `boost::tuple< OutputIterator, //result begin OutputIterator>` | public | TODO: comments.... |
| `operator<<( boost::tuple< InputIterator, InputIterator> input)` | operator | `boost::tuple< OutputIterator, //result begin OutputIterator>` | public | TODO: comments.... |
| `d_predicate` | field | `Predicate` | protected | — |
| `d_output_data` | field | `std::vector< typename OutputIterator::value_type >` | protected | — |
| `PredicateFilter()` | constructor | `None` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_PREDICATEFILTER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=utils/deprecated/PredicateFilter tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/deprecated/PredicateFilter.h
python scripts/gpq.py def GPlatesUtils::PredicateFilter --body
python scripts/gpq.py uses PredicateFilter --kind class
python scripts/gpq.py hier PredicateFilter
```
