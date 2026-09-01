# WeakObserverPublisher

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 1231 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/WeakObserverPublisher.h` | C++ | 362 |

## Overview

[[[PROSE overview unit=model/WeakObserverPublisher tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=model/WeakObserverPublisher tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
