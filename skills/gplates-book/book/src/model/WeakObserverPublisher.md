# WeakObserverPublisher

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 1231 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/WeakObserverPublisher.h` | C++ | 362 |

## Overview

`WeakObserverPublisher<H>` is the publisher half of the observer pattern that backs `WeakReference`/`WeakObserver`: a class that wants weak references made to it (such as `FeatureHandle`) derives from `WeakObserverPublisher<H>` and thereby gains the head/tail pointers of two intrusive doubly-linked lists, one for `WeakObserver<H>` (non-const) observers and one for `WeakObserver<const H>` observers. `apply_weak_observer_visitor()` and `apply_const_weak_observer_visitor()` walk each list in turn, handing every subscribed observer to a `WeakObserverVisitor<H>` — this is how a publisher broadcasts lifecycle events (modified, deactivated, about to be destroyed) to everything weakly referencing it, via the visitors in `WeakReferenceVisitors.h`.

The four free `weak_observer_get_first`/`weak_observer_get_last` function templates exist only so `WeakObserver<H>` can pick the correct list (const or non-const) purely by overload resolution on pointer constness, without the publisher needing to expose two differently-named accessor pairs; the unused second parameter is a tag argument chosen only for its type, following the same trick as Boost's `intrusive_ptr_add_ref`/`release`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::WeakObserverPublisher`](#gplatesmodelweakobserverpublisher) | class | — | `<class H>` | 4 | A WeakObserverPublisher corresponds to the publisher component of the observer design pattern. |

## Members

### `GPlatesModel::WeakObserverPublisher`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `const_weak_observer_type` | typedef | `WeakObserver<const H>` | public | The base type of all const weak observers of instances of this class. |
| `weak_observer_type` | typedef | `WeakObserver<H>` | public | The base type of all (non-const) weak observers of instances of this class. |
| `WeakObserverPublisher()` | constructor | `None` | public | Constructor. |
| `~WeakObserverPublisher()` | destructor | `None` | public | Destructor. |
| `apply_weak_observer_visitor( WeakObserverVisitor<H> &visitor)` | method | `void` | public | Apply the supplied WeakObserverVisitor to all (non-const) weak observers of this instance. |
| `apply_const_weak_observer_visitor( WeakObserverVisitor<const H> &visitor)` | method | `void` | public | Apply the supplied WeakObserverVisitor to all const and non-const weak observers of this instance. |
| `first_const_weak_observer` | field | `const_weak_observer_type` | public | Access the first const weak observer of this instance. |
| `first_weak_observer` | field | `weak_observer_type` | public | Access the first weak observer of this instance. |
| `last_const_weak_observer` | field | `const_weak_observer_type` | public | Access the last const weak observer of this instance. |
| `last_weak_observer` | field | `weak_observer_type` | public | Access the last weak observer of this instance. |
| `d_first_const_weak_observer` | field | `const_weak_observer_type` | private | The first const weak observer of this instance. |
| `d_first_weak_observer` | field | `weak_observer_type` | private | The first weak observer of this instance. |
| `d_last_const_weak_observer` | field | `const_weak_observer_type` | private | The last const weak observer of this instance. |
| `d_last_weak_observer` | field | `weak_observer_type` | private | The last weak observer of this instance. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_WEAKOBSERVERPUBLISHER_H` | macro | `None` | — |
| `weak_observer_get_first` | variable | `WeakObserver<const H>` | Get the first weak observer of the publisher pointed-to by publisher\_ptr. |
| `weak_observer_get_last` | variable | `WeakObserver<const H>` | Get the last weak observer of the publisher pointed-to by publisher\_ptr. |

## Notes

The destructor unsubscribes every observer still on either list, so a publisher going out of scope does not leave any `WeakObserver` with a dangling publisher pointer — but this class does not itself notify observers of destruction; that notification is a separate, explicit step callers must trigger (see `WeakReferencePublisherDestroyedVisitor`) before the publisher is actually destroyed. `first_const_weak_observer()`/`last_const_weak_observer()` are declared `const` and mutate `mutable` members, since subscribing a new const observer must be possible even through a const publisher.

## Used by

| Unit | Component | References |
|---|---|---|
| [model/BasicHandle](BasicHandle.md) | model | 12 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/WeakObserverPublisher.h
python scripts/gpq.py def GPlatesModel::WeakObserverPublisher --body
python scripts/gpq.py uses WeakObserverPublisher --kind class
python scripts/gpq.py hier WeakObserverPublisher
```
