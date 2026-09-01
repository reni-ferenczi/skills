# FeatureClassifier

[Book TOC](../../TOC.md) · [feature-visitors](../../components/feature-visitors.md) · cluster Community 778 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/feature-visitors/FeatureClassifier.h` | C++ | 159 |
| `src/feature-visitors/FeatureClassifier.cc` | C++ | 201 |

## Overview

[[[PROSE overview unit=feature-visitors/FeatureClassifier tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFeatureVisitors::FeatureClassifier`](#gplatesfeaturevisitorsfeatureclassifier) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | This const feature visitor can be applied to all the features in a FeatureCollection and accumulates a summary of the kind of FeatureCollection the user is dealing with. |

## Members

### `GPlatesFeatureVisitors::FeatureClassifier`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FeatureClassifier()` | constructor | `None` | public | — |
| `~FeatureClassifier()` | destructor | `None` | public | — |
| `reconstruction_feature_count()` | method | `int` | public | Returns the count of features seen by the visitor which appear to be 'reconstruction' features. |
| `reconstructable_feature_count()` | method | `int` | public | Returns the count of features seen by the visitor which appear to be 'reconstructable' features. |
| `instantaneous_feature_count()` | method | `int` | public | Returns the count of features seen by the visitor which appear to be 'instantaneous' features. |
| `total_feature_count()` | method | `int` | public | Returns the total number of features seen by the visitor. |
| `reset()` | method | `void` | public | Resets the state of the visitor, allowing the same instance to be re-used. |
| `initialise_pre_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | protected | — |
| `finalise_post_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `void` | protected | — |
| `initialise_pre_property_values( const GPlatesModel::TopLevelPropertyInline &top_level_property_inline)` | method | `bool` | protected | — |
| `visit_gml_time_instant( const GPlatesPropertyValues::GmlTimeInstant &gml_time_instant)` | method | `void` | protected | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | protected | — |
| `visit_gpml_plate_id( const GPlatesPropertyValues::GpmlPlateId &gpml_plate_id)` | method | `void` | protected | — |
| `d_property_names_to_allow` | field | `std::vector<GPlatesModel::PropertyName>` | private | — |
| `d_looks_like_reconstruction_feature` | field | `bool` | private | — |
| `d_looks_like_reconstructable_feature` | field | `bool` | private | — |
| `d_looks_like_instantaneous_feature` | field | `bool` | private | — |
| `d_reconstruction_feature_count` | field | `int` | private | — |
| `d_reconstructable_feature_count` | field | `int` | private | — |
| `d_instantaneous_feature_count` | field | `int` | private | — |
| `d_total_feature_count` | field | `int` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `contains_elem( const C &container, const E &elem)` | function | `bool` | — |
| `GPLATES_FEATUREVISITORS_FEATURECLASSIFIER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=feature-visitors/FeatureClassifier tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/feature-visitors/FeatureClassifier.h
python scripts/gpq.py def GPlatesFeatureVisitors::FeatureClassifier --body
python scripts/gpq.py uses FeatureClassifier --kind class
python scripts/gpq.py hier FeatureClassifier
```
