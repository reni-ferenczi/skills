# ReconstructionContext

[Book TOC](../../../TOC.md) · [deprecated](../../../components/deprecated.md) · cluster Community 900 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/deprecated/presenter/ReconstructionContext.h` | C++ | 103 |

## Overview

[[[PROSE overview unit=deprecated/presenter/ReconstructionContext tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=deprecated/presenter/ReconstructionContext tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
