# GenericMapperImpl

[Book TOC](../../../TOC.md) · [utils](../../../components/utils.md) · cluster Community 1862 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/deprecated/GenericMapperImpl.h` | C++ | 64 |

## Overview

`GenericMapperImpl` is an abstract template base class that defines the interface for implementation functors used by `GenericMapper`. It declares two virtual operator() overloads that accept input and output iterator pairs and direct results either to an output iterator or into a provided vector, returning the count of items processed. Subclasses supply the actual mapping algorithm.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::GenericMapperImpl`](#gplatesutilsgenericmapperimpl) | class | — | `< class InputIterator, class OutputIterator>` | 0 | TODO: comments.... |

## Members

### `GPlatesUtils::GenericMapperImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator()( InputIterator input_begin, InputIterator input_end, OutputIterator result )` | operator | `int` | public | TODO: comments.... |
| `operator()( InputIterator input_begin, InputIterator input_end, std::vector< typename OutputIterator::value_type >& result )` | operator | `int` | public | — |
| `~GenericMapperImpl()` | destructor | `None` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_GENERICTRANSFORMERIMPL_H` | macro | `None` | — |

## Notes

*None.*

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/deprecated/GenericMapperImpl.h
python scripts/gpq.py def GPlatesUtils::GenericMapperImpl --body
python scripts/gpq.py uses GenericMapperImpl --kind class
python scripts/gpq.py hier GenericMapperImpl
```
