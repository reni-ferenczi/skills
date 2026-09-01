# Mapper

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 831 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/Mapper.h` | C++ | 122 |

## Overview

[[[PROSE overview unit=utils/Mapper tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=utils/Mapper tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
