# FeatureCollectionRevision

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 376 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/model/FeatureCollectionRevision.h` | C++ | 120 |
| `src/model/FeatureCollectionRevision.cc` | C++ | 42 |

## Overview

[[[PROSE overview unit=model/FeatureCollectionRevision tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=model/FeatureCollectionRevision tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
