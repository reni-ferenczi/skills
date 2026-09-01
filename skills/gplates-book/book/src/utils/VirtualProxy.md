# VirtualProxy

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1461 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/VirtualProxy.h` | C++ | 81 |

## Overview

`VirtualProxy` is a template class that defers the creation of its pointee type until first dereferenced. It wraps a `boost::scoped_ptr` and an optional factory, allowing the expensive construction of the type to be postponed until the moment it is actually needed. `DefaultFactory` is a simple factory that calls the pointee's default constructor; custom factories may override this to perform more complex initialization.

The proxy is non-copyable (due to `boost::scoped_ptr`) and intended for objects that are expensive to create but may not always be used. The indirection operators `operator*()` and `operator->()` perform lazy creation on first use: the factory's `create()` method is invoked exactly once, and subsequent dereferences return the already-constructed object.

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

Non-copyable; the pointee is owned by the proxy and destroyed when the proxy goes out of scope. The factory is copied into the proxy and must be copy-constructable. Creation is not thread-safe: concurrent dereference from multiple threads will result in multiple calls to the factory; the caller must synchronize if thread-safety is needed.

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
