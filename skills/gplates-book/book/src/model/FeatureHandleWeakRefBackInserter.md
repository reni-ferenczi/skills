# FeatureHandleWeakRefBackInserter

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 1641 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/model/FeatureHandleWeakRefBackInserter.h` | C++ | 149 |

## Overview

`FeatureHandleWeakRefBackInserter` is an output iterator adapter that bridges the gap between code that holds strong `FeatureHandle*` pointers and algorithms that need to populate a container of weak references. When the iterator's assignment operator receives a pointer, it automatically calls `reference()` to create a weak reference and pushes it to the back of the target container. Use the convenience function `append_as_weak_refs()` to construct an instance without spelling out the template parameter.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::FeatureHandleWeakRefBackInserter`](#gplatesmodelfeaturehandleweakrefbackinserter) | class | — | `<typename C>` | 0 | A back inserter for FeatureHandle weak-refs. |

## Members

### `GPlatesModel::FeatureHandleWeakRefBackInserter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `container_type` | typedef | `C` | public | The type of the target container. |
| `this_type` | typedef | `FeatureHandleWeakRefBackInserter` | public | The type of this class. |
| `iterator_category` | alias | `std::output_iterator_tag` | public | Iterator typedefs. |
| `value_type` | alias | `void` | public | — |
| `difference_type` | alias | `void` | public | — |
| `pointer` | alias | `void` | public | — |
| `reference` | alias | `void` | public | — |
| `FeatureHandleWeakRefBackInserter( container_type &target_container)` | constructor | `None` | public | Construct an instance of this class which will insert into target\_container. |
| `FeatureHandleWeakRefBackInserter( const FeatureHandleWeakRefBackInserter &other)` | constructor | `None` | public | Copy-constructor. |
| `d_target_container_ptr` | field | `container_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_FEATUREHANDLEWEAKREFBACKINSERTER_H` | macro | `None` | — |
| `append_as_weak_refs( C &container)` | function | `FeatureHandleWeakRefBackInserter<C>` | Convenience function to create an instance of the inserter. |

## Notes

Holds a pointer to the target container; do not use the iterator after the container has been destroyed. The iterator itself is copyable and cheap to move. Thread safety follows the container — if the container supports concurrent insertion from multiple threads, the iterator does too, but if not, you must serialize access.

## Used by

| Unit | Component | References |
|---|---|---|
| [model/ModelUtils](ModelUtils.md) | model | 6 |
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 2 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 1 |
| [app-logic/TopologyNetworkResolver](../app-logic/TopologyNetworkResolver.md) | app-logic | 1 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 1 |
| [gui/TopologySectionsTableColumns](../gui/TopologySectionsTableColumns.md) | gui | 1 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/FeatureHandleWeakRefBackInserter.h
python scripts/gpq.py def GPlatesModel::FeatureHandleWeakRefBackInserter --body
python scripts/gpq.py uses FeatureHandleWeakRefBackInserter --kind class
python scripts/gpq.py hier FeatureHandleWeakRefBackInserter
```
