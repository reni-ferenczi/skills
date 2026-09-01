# FeatureCollectionFileFormatClassify

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1065 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/FeatureCollectionFileFormatClassify.h` | C++ | 180 |
| `src/file-io/FeatureCollectionFileFormatClassify.cc` | C++ | 246 |

## Overview

[[[PROSE overview unit=file-io/FeatureCollectionFileFormatClassify tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::FeatureCollectionFileFormat::(anonymous)::Classify`](#gplatesfileiofeaturecollectionfileformatanonymousclassify) | class | — | — | 0 | Used to test a single ClassificationType from a classifications\_type. |
| [`GPlatesFileIO::FeatureCollectionFileFormat::ClassificationType`](#gplatesfileiofeaturecollectionfileformatclassificationtype) | enum | — | — | 0 | The types in which a feature collection can be classified for file reading/writing. |
| [`GPlatesFileIO::FeatureCollectionFileFormat::classifications_type`](#gplatesfileiofeaturecollectionfileformatclassifications_type) | typedef | — | — | 0 | A std::bitset for testing multiple classification types for a single feature collection. |
| [`GPlatesFileIO::FeatureCollectionFileFormat::classification_predicate_type`](#gplatesfileiofeaturecollectionfileformatclassification_predicate_type) | typedef | — | — | 0 | Typedef for a predicate function that accepts a classifications\_type as it argument and returns a bool. |

## Members

### `GPlatesFileIO::FeatureCollectionFileFormat::(anonymous)::Classify`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Classify( ClassificationType classification_)` | constructor | `None` | public | — |
| `operator()( const classifications_type & classifications)` | operator | `bool` | public | — |
| `classification` | field | `ClassificationType` | private | — |

### `GPlatesFileIO::FeatureCollectionFileFormat::ClassificationType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RASTER` | enumerator | `None` | — | Rasters features contain image data. |
| `SCALAR_COVERAGE` | enumerator | `None` | — | Scalar coverage features contain a geometry and a scalar value per point in geometry. |
| `SCALAR_FIELD_3D` | enumerator | `None` | — | Scalar field features contain scalar volume data. |
| `TOPOLOGICAL` | enumerator | `None` | — | Topological features contain topological geometry that references other feature geometries. |
| `RECONSTRUCTION` | enumerator | `None` | — | Reconstruction features have 'fixedReferenceFrame' and 'movingReferenceFrame' plate ids and are used to rotate other features. |
| `NUM_CLASSIFICATION_TYPES` | enumerator | `None` | — | — |

### `GPlatesFileIO::FeatureCollectionFileFormat::classifications_type`

*None.*

### `GPlatesFileIO::FeatureCollectionFileFormat::classification_predicate_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_feature_classification( classifications_type &classifications, const GPlatesModel::FeatureHandle::const_weak_ref &feature, const GPlatesAppLogic::ReconstructMethodRegistry &reconstruct_method_registry, const std::vector<GPlatesAppLogic::ReconstructMethod::Type> &reconstruct_methods)` | function | `void` | Extracts and returns the feature classification of the specified feature. |
| `GPLATES_FILE_IO_FEATURECOLLECTIONFILEFORMATCLASSIFY_H` | macro | `None` | — |
| `intersect( const classifications_type &classifications1, const classifications_type &classifications2)` | function | `bool` | Returns true if either classification intersects the other. |
| `classify( const GPlatesModel::FeatureCollectionHandle::const_weak_ref &feature_collection, const GPlatesAppLogic::ReconstructMethodRegistry &reconstruct_method_registry)` | function | `classifications_type` | Returns the classification type(s) of feature\_collection. |
| `classify( const GPlatesModel::FeatureHandle::const_weak_ref &feature, const GPlatesAppLogic::ReconstructMethodRegistry &reconstruct_method_registry)` | function | `classifications_type` | Returns the classification type(s) of feature. |
| `find_classified_features( std::vector<GPlatesModel::FeatureHandle::weak_ref> &found_features, const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection, const GPlatesAppLogic::ReconstructMethodRegistry &reconstruct_method_registry, ClassificationType classification)` | function | `bool` | Finds features in feature\_collection that contain the classification classification. |
| `find_classified_features( std::vector<GPlatesModel::FeatureHandle::weak_ref> &found_features, const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection, const GPlatesAppLogic::ReconstructMethodRegistry &reconstruct_method_registry, const classification_predicate_type &classification_predicate)` | function | `bool` | Finds features in feature\_collection that match the classification predicate classification\_predicate. |

## Notes

[[[PROSE notes unit=file-io/FeatureCollectionFileFormatClassify tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/FeatureCollectionFileFormatRegistry](FeatureCollectionFileFormatRegistry.md) | file-io | 21 |
| [qt-widgets/ChooseFeatureCollectionWidget](../qt-widgets/ChooseFeatureCollectionWidget.md) | qt-widgets | 15 |
| [app-logic/deprecated/PaleomagWorkflow](../app-logic/deprecated/PaleomagWorkflow.md) | app-logic | 4 |
| [app-logic/deprecated/PlateVelocityWorkflow](../app-logic/deprecated/PlateVelocityWorkflow.md) | app-logic | 4 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 4 |
| [qt-widgets/CreateTotalReconstructionSequenceDialog](../qt-widgets/CreateTotalReconstructionSequenceDialog.md) | qt-widgets | 2 |
| [qt-widgets/ChooseFeatureCollectionDialog](../qt-widgets/ChooseFeatureCollectionDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/FeatureCollectionFileFormatClassify.h
python scripts/gpq.py def GPlatesFileIO::FeatureCollectionFileFormat::ClassificationType --body
python scripts/gpq.py uses ClassificationType --kind enum
```
