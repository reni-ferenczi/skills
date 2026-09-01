# UnaryMapper

[Book TOC](../../../TOC.md) · [utils](../../../components/utils.md) · cluster Community 831 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/deprecated/UnaryMapper.h` | C++ | 116 |

## Overview

`UnaryMapper` is a concrete template that implements the abstract `Mapper` interface using a user-supplied unary transformation function. It applies the function element-by-element to an input sequence to produce an output sequence, with an optional output iterator parameter that defaults to an internal vector if not provided. Unlike `GenericMapper`, it does not require the implementation to handle different output collection strategies.

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

*None.*

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
