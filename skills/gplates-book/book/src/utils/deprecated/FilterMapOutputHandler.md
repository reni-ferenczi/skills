# FilterMapOutputHandler

[Book TOC](../../../TOC.md) · [utils](../../../components/utils.md) · cluster Community 770 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/deprecated/FilterMapOutputHandler.h` | C++ | 109 |

## Overview

`FilterMapOutputHandler` is a deprecated template class that abstracts output writing for filter/map operations. It takes two template parameters: `OutputHandle` (the target iterator or container) and `OutputMode` (either `OUTPUT_BY_ITERATOR` or `OUTPUT_BY_CONTAINER`). The handler provides an `insert()` method that dispatches to the appropriate output strategy based on the mode.

When in iterator mode, `insert()` writes by dereferencing and advancing the output iterator; in container mode, it appends using `push_back()`. This allows filter/mapper implementations to be mode-agnostic.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::OUTPUT_BY_ITERATOR`](#gplatesutilsoutput_by_iterator) | struct | — | — | 0 | — |
| [`GPlatesUtils::OUTPUT_BY_CONTAINER`](#gplatesutilsoutput_by_container) | struct | — | — | 0 | — |
| [`GPlatesUtils::FilterMapOutputHandler`](#gplatesutilsfiltermapoutputhandler) | class | — | `< typename OutputHandle, typename OutputMode >` | 0 | TODO: comments.... |

## Members

### `GPlatesUtils::OUTPUT_BY_ITERATOR`

*None.*

### `GPlatesUtils::OUTPUT_BY_CONTAINER`

*None.*

### `GPlatesUtils::FilterMapOutputHandler`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FilterMapOutputHandler( OutputHandle &output_handle)` | constructor | `None` | public | TODO: comments.... |
| `insert( const typename OutputHandle::value_type &value)` | method | `void` | public | TODO: comments.... |
| `d_output_handle` | field | `OutputHandle` | protected | — |
| `FilterMapOutputHandler()` | constructor | `None` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_FILTERMAPOUTPUTHANDLER_H` | macro | `None` | — |
| `_insert( OutputHandle &handle, const typename OutputHandle::value_type &value)` | function | `typename boost::enable_if< typename boost::is_same< OutputMode, OUTPUT_BY_ITERATOR>, void>::type` | — |

## Notes

In iterator mode, the output iterator must be valid and derefernceable; in container mode, the container must support `push_back()`. The output handle is held by non-const reference.

## Used by

| Unit | Component | References |
|---|---|---|
| [utils/deprecated/GenericFilter](GenericFilter.md) | utils | 5 |
| [utils/deprecated/GenericMapper](GenericMapper.md) | utils | 5 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/deprecated/FilterMapOutputHandler.h
python scripts/gpq.py def GPlatesUtils::FilterMapOutputHandler --body
python scripts/gpq.py uses FilterMapOutputHandler --kind class
python scripts/gpq.py hier FilterMapOutputHandler
```
