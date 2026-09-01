# ExposedPresenterObject

[Book TOC](../../../TOC.md) · [deprecated](../../../components/deprecated.md) · cluster Community 900 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/deprecated/presenter/ExposedPresenterObject.h` | C++ | 105 |
| `src/deprecated/presenter/ExposedPresenterObject.cc` | C++ | 34 |

## Overview

Base class for presenter objects exposed to the view layer. Each instance receives a unique sequential identifier assigned at construction time, accessed via `id()`. Intended to be used as a virtual base class. Explicitly non-copyable and non-assignable to ensure identity semantics — each object's ID is fixed at creation.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPresenter::ExposedPresenterObject`](#gplatespresenterexposedpresenterobject) | class | — | — | 1 | This class is inherited by all objects exposed by the Presenter to the View. |

## Members

### `GPlatesPresenter::ExposedPresenterObject`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `id_type` | typedef | `unsigned long` | public | — |
| `id()` | method | `id_type` | public | Return the identifier. |
| `ExposedPresenterObject()` | constructor | `None` | protected | When creating a new ExposedPresenterObject we assign the next id in sequence. |
| `d_next_id` | field | `id_type` | private | The 'global' identifier id sequence counter |
| `d_id` | field | `id_type` | private | The identifer for this object |
| `get_next_id()` | method | `id_type` | private | Return the next avilable identifier value FIXME (ticket:18): At the moment this can only be used in a single thread because there is no mutex protection around the next\_id value; |
| `ExposedPresenterObject(ExposedPresenterObject &)` | constructor | `None` | private | ExposedPresenterObjects should not be copyable. |
| `operator=` | field | `ExposedPresenterObject` | private | ExposedPresenterObjects should not be assignable |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `d_next_id` | variable | `ExposedPresenterObject::id_type` | — |
| `GPLATES_PRESENTER_EXPOSEDPRESENTEROBJECT_H` | macro | `None` | — |

## Notes

The static ID counter `d_next_id` has no mutex protection, so ID allocation is not thread-safe. This class should only be used from a single thread, or ID generation must be externally synchronized.

## Used by

| Unit | Component | References |
|---|---|---|
| [deprecated/presenter/ReconstructionContext](ReconstructionContext.md) | deprecated | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/deprecated/presenter/ExposedPresenterObject.h
python scripts/gpq.py def GPlatesPresenter::ExposedPresenterObject --body
python scripts/gpq.py uses ExposedPresenterObject --kind class
python scripts/gpq.py hier ExposedPresenterObject
```
