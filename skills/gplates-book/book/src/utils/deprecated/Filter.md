# Filter

[Book TOC](../../../TOC.md) · [utils](../../../components/utils.md) · cluster Community 16 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/deprecated/Filter.h` | C++ | 155 |

## Overview

[[[PROSE overview unit=utils/deprecated/Filter tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=utils/deprecated/Filter tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
