# PredicateFilter

[Book TOC](../../../TOC.md) · [utils](../../../components/utils.md) · cluster Community 1399 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/deprecated/PredicateFilter.h` | C++ | 151 |
| `src/utils/deprecated/PredicateFilter.cc` | C++ | 25 |

## Overview

`PredicateFilter` is a concrete template that implements the abstract `Filter` interface using a user-supplied boolean predicate. It selects elements from an input sequence that satisfy the predicate condition and copies them to the output, supporting three output collection modes: appending to a provided iterator, using an internal vector, or populating a supplied vector. The input and output element types must be identical, enforced by the base class.

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

*None.*

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
