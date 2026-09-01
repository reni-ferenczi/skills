# FeatureStoreRootRevision

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 376 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/model/FeatureStoreRootRevision.h` | C++ | 119 |
| `src/model/FeatureStoreRootRevision.cc` | C++ | 42 |

## Overview

`FeatureStoreRootRevision` is the apex of the three-tier revisioning hierarchy: it holds the collection of currently-loaded feature collections (each corresponding to one loaded file). When feature collections are added or removed from the store, a new `FeatureStoreRootRevision` is created without modifying the old, preserving edit history for undo support.

Like the other revision types, you access the current version through `FeatureStoreRootHandle`, not directly. Clients do not work with this class directly — it is managed by the transaction system.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::FeatureStoreRootRevision`](#gplatesmodelfeaturestorerootrevision) | class | [`BasicRevision<FeatureStoreRootHandle>`](BasicRevision.md)<br>[`GPlatesUtils::ReferenceCount<FeatureStoreRootRevision>`](../utils/ReferenceCount.md) | — | 0 | A feature store root revision contains the revisioned content of a conceptual feature store root. |

## Members

### `GPlatesModel::FeatureStoreRootRevision`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `this_type` | typedef | `FeatureStoreRootRevision` | public | The type of this class. |
| `create()` | method | `non_null_ptr_type` | public | Creates a new FeatureStoreRootRevision instance. |
| `FeatureStoreRootRevision()` | constructor | `None` | private | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `FeatureStoreRootRevision( const this_type &other)` | constructor | `None` | private | This constructor should not be defined, because we don't want to be able to copy construct one of these objects. |
| `operator=` | field | `this_type` | private | This should not be defined, because we don't want to be able to copy one of these objects. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_FEATURESTOREROOTREVISION_H` | macro | `None` | — |

## Notes

Reference counted and heap-allocated only via `create()`. Copy construction and assignment are blocked to enforce immutability. The feature store contains a single root revision, which the transaction system manages; normal application code should not construct or manipulate root revisions directly.

## Used by

| Unit | Component | References |
|---|---|---|
| [model/FeatureStoreRootHandle](FeatureStoreRootHandle.md) | model | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/FeatureStoreRootRevision.h
python scripts/gpq.py def GPlatesModel::FeatureStoreRootRevision --body
python scripts/gpq.py uses FeatureStoreRootRevision --kind class
python scripts/gpq.py hier FeatureStoreRootRevision
```
