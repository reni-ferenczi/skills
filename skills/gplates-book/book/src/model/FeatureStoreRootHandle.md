# FeatureStoreRootHandle

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 1833 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/FeatureStoreRootHandle.h` | C++ | 121 |
| `src/model/FeatureStoreRootHandle.cc` | C++ | 45 |

## Overview

`FeatureStoreRootHandle` is the root of the model's three-tiered revisioned
hierarchy: one feature store root contains all currently-loaded
`FeatureCollectionHandle`s, and every loaded feature lives inside one of those
collections. Like the other Handle/Revision pairs in `model`, the concept is
split in two: `FeatureStoreRootHandle` is the persistent, stable-address handle
(owned by a `FeatureStore`, following `Model`), while its content lives in a
succession of `FeatureStoreRootRevision` instances created on every
modification — the handle endures across edits, the revision it points at does
not.

Following the same pattern as `FeatureCollectionHandle` and `FeatureHandle`,
construction is restricted to `create()`, which builds the handle together with
an initial `FeatureStoreRootRevision`; the constructor is private and `Model` is
the sole friend permitted to construct it directly. The class contributes no
new behaviour beyond wiring its base classes together — `BasicHandle` for
revision management and `ReferenceCount` for intrusive-pointer lifetime — so
there is exactly one of these per feature store.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::FeatureStoreRootHandle`](#gplatesmodelfeaturestoreroothandle) | class | [`BasicHandle<FeatureStoreRootHandle>`](BasicHandle.md)<br>[`GPlatesUtils::ReferenceCount<FeatureStoreRootHandle>`](../utils/ReferenceCount.md) | — | 0 | A feature store root handle acts as a persistent handle to the revisioned content of a conceptual feature store root. |

## Members

### `GPlatesModel::FeatureStoreRootHandle`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `this_type` | typedef | `FeatureStoreRootHandle` | public | The type of this class. |
| `create()` | method | `non_null_ptr_type` | public | Creates a new FeatureStoreRootHandle instance. |
| `FeatureStoreRootHandle()` | constructor | `None` | private | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `FeatureStoreRootHandle( const this_type &other)` | constructor | `None` | private | This constructor should not be defined, because we don't want to be able to copy construct one of these objects. |
| `operator=` | field | `this_type` | private | This should not be defined, because we don't want to be able to copy one of these objects. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_FEATURESTOREROOTHANDLE_H` | macro | `None` | — |

## Notes

- Construction is restricted to `create()`; the default and copy constructors
  are private and the copy constructor and `operator=` are declared but never
  defined, so copying a `FeatureStoreRootHandle` is a link error, not just
  disallowed by convention.
- `Model` is a friend specifically so it can construct the single
  `FeatureStoreRootHandle` a feature store needs — other code should go through
  `create()` or the `Model`/`FeatureStore` API rather than instantiating this
  directly.
- The header pulls in `RevisionAwareIterator.h` at the bottom, after the class
  definition, purely for client convenience (so code including this header
  gets iterators for free) rather than because this header itself needs it;
  it is placed there instead of with the other includes to avoid a cyclic
  dependency.

## Used by

| Unit | Component | References |
|---|---|---|
| [model/FeatureCollectionHandle](FeatureCollectionHandle.md) | model | 4 |
| [model/Model](Model.md) | model | 4 |
| [app-logic/ApplicationState](../app-logic/ApplicationState.md) | app-logic | 3 |
| [model/BasicHandle](BasicHandle.md) | model | 3 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 3 |
| [qt-widgets/ColouringDialog](../qt-widgets/ColouringDialog.md) | qt-widgets | 2 |
| [model/RevisionAwareIterator](RevisionAwareIterator.md) | model | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/FeatureStoreRootHandle.h
python scripts/gpq.py def GPlatesModel::FeatureStoreRootHandle --body
python scripts/gpq.py uses FeatureStoreRootHandle --kind class
python scripts/gpq.py hier FeatureStoreRootHandle
```
