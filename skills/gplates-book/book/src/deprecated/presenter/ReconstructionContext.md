# ReconstructionContext

[Book TOC](../../../TOC.md) · [deprecated](../../../components/deprecated.md) · cluster Community 900 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/deprecated/presenter/ReconstructionContext.h` | C++ | 103 |

## Overview

Presenter-side context for managing the inputs to a reconstruction: a collection of feature collections (with usage masks to filter them), a time value, and a root plate ID. Lazily instantiates and caches the actual `Reconstruction` object. Tracks dirtiness to detect when parameters have changed and the reconstruction output needs regeneration. Uses virtual inheritance from `ExposedPresenterObject` to support multiple inheritance patterns.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPresenter::ReconstructionContext`](#gplatespresenterreconstructioncontext) | class | [`ExposedPresenterObject`](ExposedPresenterObject.md) *(virtual)* | — | 0 | A ReconstructionContext is an ExposedPresenterObject which handles the management of data necessary to generate a ReconstructionObject. |

## Members

### `GPlatesPresenter::ReconstructionContext`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ReconstructionContext()` | constructor | `None` | public | — |
| `~ReconstructionContext()` | destructor | `None` | public | — |
| `add_feature_collection( GPlatesModel::FeatureCollection::weak_ref fc, UsageMask mask)` | method | `void` | public | — |
| `remove_feature_collection( GPlatesModel::FeatureCollection::weak_ref fc, UsageMask mask)` | method | `void` | public | — |
| `set_time( unsigned long time)` | method | `void` | public | — |
| `set_root( unsigned long root)` | method | `void` | public | — |
| `is_dirty()` | method | `bool` | public | — |
| `reconstruction_instance()` | method | `Reconstruction::non_null_ptr_type` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PRESENTER_RECONSTRUCTIONCONTEXT_H` | macro | `None` | — |

## Notes

Uses virtual inheritance from `ExposedPresenterObject` to enable multiple inheritance patterns in derived classes. The `reconstruction_instance()` method lazily instantiates the actual `Reconstruction` object on first access, but the implementation in the header is incomplete (marked with a comment). Methods have EMIT comments suggesting they were designed to work with an event/signal system.

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/deprecated/presenter/ReconstructionContext.h
python scripts/gpq.py def GPlatesPresenter::ReconstructionContext --body
python scripts/gpq.py uses ReconstructionContext --kind class
python scripts/gpq.py hier ReconstructionContext
```
