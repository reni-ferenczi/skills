# Filter

[Book TOC](../../../TOC.md) · [utils](../../../components/utils.md) · cluster Community 16 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/deprecated/Filter.h` | C++ | 155 |

## Overview

`Filter` is a deprecated abstract template class that defines the interface for filtering operations over ranges. It takes an input range and produces an output range where the input and output value types must be identical. The class provides three overloaded `operator()` signatures for different output buffer management strategies: storing results in an internally-managed buffer, writing to a provided output iterator, or appending to a provided container.

This class is part of a deprecated filtering framework and uses boost::tuple to return both the begin and end iterators of the result range. The `operator<<` and `operator>>` operators allow chaining filters in a pipeline style.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_FILTER_H` | macro | `None` | — |
| `operator()( InputIterator input_begin, InputIterator input_end)` | operator | `boost::tuple< OutputIterator, //result begin OutputIterator >` | TODO: comments.... |
| `operator()( InputIterator input_begin, InputIterator input_end, OutputIterator result)` | operator | `boost::tuple< OutputIterator, //result begin OutputIterator >` | TODO: comments.... |
| `operator()( InputIterator input_begin, InputIterator input_end, OutputContainer &result)` | operator | `boost::tuple< OutputIterator, //result begin OutputIterator >` | TODO: comments.... |
| `operator<<( boost::tuple< InputIterator, InputIterator> )` | operator | `boost::tuple< OutputIterator, //result begin OutputIterator>` | TODO: comments.... |
| `operator>>( boost::tuple< OutputIterator, OutputIterator >, Filter< InputIterator, OutputIterator> )` | operator | `boost::tuple< OutputIterator, //result begin OutputIterator>` | — |

## Notes

Input and output element types are statically checked to be identical via `BOOST_MPL_ASSERT`. Output iterators must be valid for writing.

## Used by

| Unit | Component | References |
|---|---|---|
| [utils/deprecated/GenericFilter](GenericFilter.md) | utils | 1 |
| [utils/deprecated/PredicateFilter](PredicateFilter.md) | utils | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/deprecated/Filter.h
```
