# Mapper

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 831 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/Mapper.h` | C++ | 122 |

## Overview

`Mapper` is an abstract base class template defining an interface for mapping (transforming) input sequences to output sequences. Subclasses implement the transformation logic via pure virtual operator() overloads. The class supports flexible output handling: writing to an existing iterator, creating a new output container internally, or accepting an output container reference to populate.

Type extraction is handled by template metaprogramming: the class deduces the value type from both iterators and raw pointers using Boost type traits, exposing typedefs for both input and output value types. All operations return a tuple of output iterators (begin and end) to indicate the result range.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::Mapper`](#gplatesutilsmapper) | class | — | `< class InputIterator, class OutputIterator, class OutputContainer = std::vector<typename OutputIterator::value_type> >` | 2 | — |

## Members

### `GPlatesUtils::Mapper`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InputValueType` | typedef | `typename boost::mpl::if_< boost::is_pointer<InputIterator>, boost::remove_pointer<InputIterator>, typename InputIterator::value_type>::type` | public | — |
| `OutputValueType` | typedef | `typename boost::mpl::if_< boost::is_pointer<OutputIterator>, boost::remove_pointer<OutputIterator>, typename OutputIterator::value_type>::type` | public | — |
| `OutputIteratorType` | typedef | `OutputIterator` | public | — |
| `InputIteratorType` | typedef | `InputIterator` | public | — |
| `OutputContainerType` | typedef | `OutputContainer` | public | — |
| `operator()( InputIterator input_begin, InputIterator input_end, OutputIterator result)` | operator | `boost::tuple< OutputIterator, //result begin OutputIterator>` | public | TODO: comments.... |
| `operator()( InputIterator input_begin, InputIterator input_end)` | operator | `boost::tuple< OutputIterator, //result begin OutputIterator>` | public | TODO: comments.... |
| `operator()( InputIterator input_begin, InputIterator input_end, OutputContainer &result)` | operator | `boost::tuple< OutputIterator, //result begin OutputIterator>` | public | TODO: comments.... |
| `operator<<( boost::tuple< InputIterator, InputIterator> )` | operator | `boost::tuple< OutputIterator, //result begin OutputIterator>` | public | TODO: comments.... |
| `~Mapper()` | destructor | `None` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_TRANSFORMER_H` | macro | `None` | — |

## Notes

`Mapper` is an abstract interface; subclasses must implement all four operator() variants. The return type is a tuple of iterators (begin and end), not the container itself; callers must extract the container from the begin iterator if needed. The `operator<<` variant expects a `boost::tuple` of input iterators, supporting a stream-like syntax. All operators are pure virtual, making direct instantiation a compile error.

## Used by

| Unit | Component | References |
|---|---|---|
| [utils/deprecated/Filter](deprecated/Filter.md) | utils | 2 |
| [utils/deprecated/FilterMapReduceWorkFlow](deprecated/FilterMapReduceWorkFlow.md) | utils | 2 |
| [utils/deprecated/GenericMapper](deprecated/GenericMapper.md) | utils | 2 |
| [utils/deprecated/UnaryMapper](deprecated/UnaryMapper.md) | utils | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/Mapper.h
python scripts/gpq.py def GPlatesUtils::Mapper --body
python scripts/gpq.py uses Mapper --kind class
python scripts/gpq.py hier Mapper
```
