# FeatureStoreRootHandle

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 1833 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/FeatureStoreRootHandle.h` | C++ | 121 |
| `src/model/FeatureStoreRootHandle.cc` | C++ | 45 |

## Overview

[[[PROSE overview unit=model/FeatureStoreRootHandle tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=model/FeatureStoreRootHandle tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
