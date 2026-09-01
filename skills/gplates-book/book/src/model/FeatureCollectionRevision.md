# FeatureCollectionRevision

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 376 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/model/FeatureCollectionRevision.h` | C++ | 120 |
| `src/model/FeatureCollectionRevision.cc` | C++ | 42 |

## Overview

`FeatureCollectionRevision` holds a snapshot of the content of a feature collection — the set of features it contains — at one point in time. It implements the middle tier of a three-level revisioning hierarchy: the feature store contains feature store roots, which contain feature collections, which contain features. Modifications to any collection create a new `FeatureCollectionRevision` without altering the old one, allowing the application to preserve edit history and support undo.

Client code does not use this class directly. Instead, you access the current revision of a collection through its `FeatureCollectionHandle`, which manages the pointer to whichever revision is active at any given moment. When a transaction commits, the handle's pointer swaps to the new revision.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::FeatureCollectionRevision`](#gplatesmodelfeaturecollectionrevision) | class | [`BasicRevision<FeatureCollectionHandle>`](BasicRevision.md)<br>[`GPlatesUtils::ReferenceCount<FeatureCollectionRevision>`](../utils/ReferenceCount.md) | — | 0 | A feature collection revision contains the revisioned content of a conceptual feature collection. |

## Members

### `GPlatesModel::FeatureCollectionRevision`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `this_type` | typedef | `FeatureCollectionRevision` | public | The type of this class. |
| `create()` | method | `non_null_ptr_type` | public | Creates a new FeatureCollectionRevision instance. |
| `FeatureCollectionRevision()` | constructor | `None` | private | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `FeatureCollectionRevision( const this_type &other)` | constructor | `None` | private | This constructor should not be defined, because we don't want to be able to copy construct one of these objects. |
| `operator=` | field | `this_type` | private | This should not be defined, because we don't want to be able to copy one of these objects. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_FEATURECOLLECTIONREVISION_H` | macro | `None` | — |

## Notes

Instances are always heap-allocated via the static `create()` factory and managed by `ReferenceCount`. Copy construction and assignment are explicitly blocked to enforce the immutability contract and prevent accidental aliasing. Revisions are normally created and discarded by the transaction system; outside of transaction handling, you should not be constructing or destroying them directly.

## Used by

| Unit | Component | References |
|---|---|---|
| [entry-points/gplates_demo_no_gui_main](../entry-points/gplates_demo_no_gui_main.md) | entry-points | 1 |
| [model/FeatureCollectionHandle](FeatureCollectionHandle.md) | model | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/FeatureCollectionRevision.h
python scripts/gpq.py def GPlatesModel::FeatureCollectionRevision --body
python scripts/gpq.py uses FeatureCollectionRevision --kind class
python scripts/gpq.py hier FeatureCollectionRevision
```
