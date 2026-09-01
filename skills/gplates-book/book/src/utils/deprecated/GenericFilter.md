# GenericFilter

[Book TOC](../../../TOC.md) · [utils](../../../components/utils.md) · cluster Community 770 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/deprecated/GenericFilter.h` | C++ | 155 |

## Overview

`GenericFilter` is a deprecated template class that implements the `Filter` interface by wrapping a user-supplied implementation functor. It provides three overloaded `operator()` signatures supporting different output buffer management: writing to an external output iterator, using an internally-managed output vector, or appending to an external container.

The implementation functor is responsible for iterating the input range and calling the output handler's `insert()` method for each filtered element. `GenericFilter` abstracts away the output handling details and returns a tuple of begin/end iterators for the result.

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

The internal output vector d_output_data is shared across all three operator() variants; if you use different variants in sequence, results from earlier calls may be overwritten or mixed. When using iterator mode, the implementation's return value indicates the number of elements written, which is used to advance the result end iterator.

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
