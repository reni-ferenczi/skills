# WeakReferenceVisitors

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 1148 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/WeakReferenceVisitors.h` | C++ | 160 |

## Overview

[[[PROSE overview unit=model/WeakReferenceVisitors tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::WeakReferencePublisherModifiedVisitor`](#gplatesmodelweakreferencepublishermodifiedvisitor) | class | [`WeakObserverVisitor<H>`](WeakObserverVisitor.md) | `<typename H>` | 0 | Notifies the WeakReference that its publisher has been modified. |
| [`GPlatesModel::WeakReferencePublisherAddedVisitor`](#gplatesmodelweakreferencepublisheraddedvisitor) | class | [`WeakObserverVisitor<H>`](WeakObserverVisitor.md) | `<typename H>` | 0 | — |
| [`GPlatesModel::WeakReferencePublisherDeactivatedVisitor`](#gplatesmodelweakreferencepublisherdeactivatedvisitor) | class | [`WeakObserverVisitor<H>`](WeakObserverVisitor.md) | `<typename H>` | 0 | Notifies the WeakReference that its publisher has been deactivated (conceptually deleted). |
| [`GPlatesModel::WeakReferencePublisherReactivatedVisitor`](#gplatesmodelweakreferencepublisherreactivatedvisitor) | class | [`WeakObserverVisitor<H>`](WeakObserverVisitor.md) | `<typename H>` | 0 | Notifies the WeakReference that its publisher has been reactivated (conceptually undeleted). |
| [`GPlatesModel::WeakReferencePublisherDestroyedVisitor`](#gplatesmodelweakreferencepublisherdestroyedvisitor) | class | [`WeakObserverVisitor<H>`](WeakObserverVisitor.md) | `<typename H>` | 0 | Notifies the WeakReference that its publisher is about to be destroyed (in the C++ sense). |

## Members

### `GPlatesModel::WeakReferencePublisherModifiedVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `WeakReferencePublisherModifiedVisitor( typename WeakReferencePublisherModifiedEvent<H>::Type type)` | constructor | `None` | public | — |
| `visit_weak_reference( WeakReference<H> &weak_reference)` | method | `void` | public | — |
| `d_type` | field | `typename WeakReferencePublisherModifiedEvent<H>::Type` | private | — |

### `GPlatesModel::WeakReferencePublisherAddedVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `WeakReferencePublisherAddedVisitor( const typename WeakReferencePublisherAddedEvent<H>::new_children_container_type &new_children)` | constructor | `None` | public | — |
| `visit_weak_reference( WeakReference<H> &weak_reference)` | method | `void` | public | — |
| `d_new_children` | field | `typename WeakReferencePublisherAddedEvent<H>::new_children_container_type` | private | — |

### `GPlatesModel::WeakReferencePublisherDeactivatedVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `visit_weak_reference( WeakReference<H> &weak_reference)` | method | `void` | public | — |

### `GPlatesModel::WeakReferencePublisherReactivatedVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `visit_weak_reference( WeakReference<H> &weak_reference)` | method | `void` | public | — |

### `GPlatesModel::WeakReferencePublisherDestroyedVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `visit_weak_reference( WeakReference<H> &weak_reference)` | method | `void` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_WEAKREFERENCEVISITOR_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=model/WeakReferenceVisitors tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [model/BasicHandle](BasicHandle.md) | model | 11 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/WeakReferenceVisitors.h
python scripts/gpq.py def GPlatesModel::WeakReferencePublisherModifiedVisitor --body
python scripts/gpq.py uses WeakReferencePublisherModifiedVisitor --kind class
python scripts/gpq.py hier WeakReferencePublisherModifiedVisitor
```
