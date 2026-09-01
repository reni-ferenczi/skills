# VirtualProxy

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1461 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/VirtualProxy.h` | C++ | 81 |

## Overview

[[[PROSE overview unit=utils/VirtualProxy tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::DefaultFactory`](#gplatesutilsdefaultfactory) | class | — | `<class Type>` | 0 | Default factory uses default constructor of pointee. |
| [`GPlatesUtils::VirtualProxy`](#gplatesutilsvirtualproxy) | class | — | `< class Type, class Factory = DefaultFactory<Type> >` | 0 | VirtualProxy template class (non-copyable due to boost::scoped\_ptr). 'Type' is pointee object that's created when VirtualProxy is first dereferenced. 'Factory' is used to create pointee 'Type' and must have a method create() that returns a ... |

## Members

### `GPlatesUtils::DefaultFactory`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create()` | method | `Type` | public | — |

### `GPlatesUtils::VirtualProxy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `VirtualProxy(const Factory& factory = Factory())` | constructor | `None` | public | — |
| `operator->()` | operator | `Type` | public | Indirection operator (first call will create instance of Type). |
| `d_type_ptr` | field | `boost::scoped_ptr<Type>` | private | — |
| `d_factory` | field | `Factory` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_VIRTUALPROXY_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=utils/VirtualProxy tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Globe](../gui/Globe.md) | gui | 1 |
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/VirtualProxy.h
python scripts/gpq.py def GPlatesUtils::VirtualProxy --body
python scripts/gpq.py uses VirtualProxy --kind class
python scripts/gpq.py hier VirtualProxy
```
