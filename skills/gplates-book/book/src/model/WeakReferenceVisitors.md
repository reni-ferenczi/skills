# WeakReferenceVisitors

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 1148 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/WeakReferenceVisitors.h` | C++ | 160 |

## Overview

This header supplies the five concrete `WeakObserverVisitor<H>` implementations that turn a `WeakObserverPublisher<H>` lifecycle event into a `WeakReference<H>` callback notification. Each visitor is applied by the publisher (via `apply_weak_observer_visitor()`) to every subscribed observer; when the observer being visited happens to be a `WeakReference`, `visit_weak_reference()` calls straight back into the matching `WeakReference` method — `publisher_modified()`, `publisher_added()`, `publisher_deactivated()`, `publisher_reactivated()`, or `publisher_about_to_be_destroyed()` — which in turn forwards to any `WeakReferenceCallback` the caller attached.

`WeakReferencePublisherModifiedVisitor` and `WeakReferencePublisherAddedVisitor` carry extra state (the modification `Type`, or the container of newly added children) that gets threaded through to the callback along with the notification; the other three visitors are stateless triggers for their respective events. Application-logic code does not normally construct these directly — they are the plumbing a publisher (such as `FeatureHandle`) uses internally to fan a single state change out to every attached `WeakReference`.

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

*None.*

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
