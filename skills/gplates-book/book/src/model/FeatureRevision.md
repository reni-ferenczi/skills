# FeatureRevision

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 204 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/model/FeatureRevision.h` | C++ | 188 |
| `src/model/FeatureRevision.cc` | C++ | 101 |

## Overview

[[[PROSE overview unit=model/FeatureRevision tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::FeatureRevision`](#gplatesmodelfeaturerevision) | class | [`BasicRevision<FeatureHandle>`](BasicRevision.md)<br>[`GPlatesUtils::ReferenceCount<FeatureRevision>`](../utils/ReferenceCount.md) | — | 0 | A feature revision contains the revisioned content of a conceptual feature. |

## Members

### `GPlatesModel::FeatureRevision`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `this_type` | typedef | `FeatureRevision` | public | The type of this class. |
| `property_predicate_type` | typedef | `child_predicate_type` | public | Typedef for a function that accepts a pointer to a property and returns a boolean. |
| `create( const RevisionId &revision_id_ = RevisionId())` | method | `non_null_ptr_type` | public | Creates a new FeatureRevision instance with an optional unique revision ID. |
| `clone()` | method | `non_null_ptr_type` | public | Creates a copy of this FeatureRevision instance. |
| `clone( const property_predicate_type &clone_properties_predicate)` | method | `non_null_ptr_type` | public | Creates a copy of this FeatureRevision instance, copying only those properties for which the predicate clone\_properties\_predicate returns true. |
| `revision_id` | field | `RevisionId` | public | The unique revision ID for this feature revision. |
| `update_revision_id()` | method | `void` | public | Changes the revision ID of this feature revision to a new ID. |
| `FeatureRevision( const RevisionId &revision_id_)` | constructor | `None` | private | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `FeatureRevision( const this_type &other)` | constructor | `None` | private | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `FeatureRevision( const this_type &other, const property_predicate_type &clone_properties_predicate)` | constructor | `None` | private | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `operator=` | field | `this_type` | private | This should not be defined, because we don't want to be able to copy one of these objects. |
| `d_revision_id` | field | `RevisionId` | private | The unique revision ID for this feature revision. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_FEATUREREVISION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=model/FeatureRevision tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [model/FeatureHandle](FeatureHandle.md) | model | 4 |
| [data-mining/PopulateShapeFileAttributesVisitor](../data-mining/PopulateShapeFileAttributesVisitor.md) | data-mining | 1 |
| [entry-points/gplates_demo_no_gui_main](../entry-points/gplates_demo_no_gui_main.md) | entry-points | 1 |
| [feature-visitors/FromQvariantConverter](../feature-visitors/FromQvariantConverter.md) | feature-visitors | 1 |
| [feature-visitors/QueryFeaturePropertiesWidgetPopulator](../feature-visitors/QueryFeaturePropertiesWidgetPopulator.md) | feature-visitors | 1 |
| [feature-visitors/ShapefileAttributeFinder](../feature-visitors/ShapefileAttributeFinder.md) | feature-visitors | 1 |
| [feature-visitors/ToQvariantConverter](../feature-visitors/ToQvariantConverter.md) | feature-visitors | 1 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 1 |
| [feature-visitors/ViewFeatureGeometriesWidgetPopulator](../feature-visitors/ViewFeatureGeometriesWidgetPopulator.md) | feature-visitors | 1 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 1 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 1 |
| [file-io/PlatesRotationFormatWriter](../file-io/PlatesRotationFormatWriter.md) | file-io | 1 |
| [file-io/deprecated/GpmlOnePointFiveOutputVisitor](../file-io/deprecated/GpmlOnePointFiveOutputVisitor.md) | file-io | 1 |
| [model/BasicHandle](BasicHandle.md) | model | 1 |
| [qt-widgets/EditWidgetChooser](../qt-widgets/EditWidgetChooser.md) | qt-widgets | 1 |
| [qt-widgets/FeaturePropertiesDialog](../qt-widgets/FeaturePropertiesDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/FeatureRevision.h
python scripts/gpq.py def GPlatesModel::FeatureRevision --body
python scripts/gpq.py uses FeatureRevision --kind class
python scripts/gpq.py hier FeatureRevision
```
