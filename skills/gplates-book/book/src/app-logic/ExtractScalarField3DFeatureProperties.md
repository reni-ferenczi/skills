# ExtractScalarField3DFeatureProperties

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 703 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ExtractScalarField3DFeatureProperties.h` | C++ | 117 |
| `src/app-logic/ExtractScalarField3DFeatureProperties.cc` | C++ | 227 |

## Overview

[[[PROSE overview unit=app-logic/ExtractScalarField3DFeatureProperties tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::CanResolveScalarField3DFeature`](#anonymouscanresolvescalarfield3dfeature) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Visits a feature collection and determines whether the feature collection contains any scalar field features. |
| [`GPlatesAppLogic::ExtractScalarField3DFeatureProperties`](#gplatesapplogicextractscalarfield3dfeatureproperties) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Visits a scalar field feature and extracts the following properties from it: - GmlFile inside a GpmlConstantValue or a GpmlPiecewiseAggregation inside a gpml:filename top-level property. |

## Members

### `(anonymous)::CanResolveScalarField3DFeature`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CanResolveScalarField3DFeature()` | constructor | `None` | public | — |
| `has_scalar_field_3d_feature()` | method | `bool` | public | — |
| `initialise_pre_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | public | — |
| `finalise_post_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `void` | public | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | public | — |
| `visit_gpml_piecewise_aggregation( const GPlatesPropertyValues::GpmlPiecewiseAggregation &gpml_piecewise_aggregation)` | method | `void` | public | — |
| `visit_gpml_scalar_field_3d_file( const GPlatesPropertyValues::GpmlScalarField3DFile &gpml_scalar_field_3d_file)` | method | `void` | public | — |
| `d_seen_gpml_scalar_field_3d_file` | field | `bool` | private | — |
| `d_inside_constant_value` | field | `bool` | private | — |
| `d_inside_piecewise_aggregation` | field | `bool` | private | — |
| `d_has_scalar_field_feature` | field | `bool` | private | — |

### `GPlatesAppLogic::ExtractScalarField3DFeatureProperties`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ExtractScalarField3DFeatureProperties( const double &reconstruction_time = 0)` | constructor | `None` | public | — |
| `get_scalar_field_filename` | field | `boost::optional<GPlatesPropertyValues::TextContent>` | public | — |
| `initialise_pre_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | public | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | public | — |
| `visit_gpml_piecewise_aggregation( const GPlatesPropertyValues::GpmlPiecewiseAggregation &gpml_piecewise_aggregation)` | method | `void` | public | — |
| `visit_gpml_scalar_field_3d_file( const GPlatesPropertyValues::GpmlScalarField3DFile &gpml_scalar_field_3d_file)` | method | `void` | public | — |
| `d_reconstruction_time` | field | `GPlatesPropertyValues::GeoTimeInstant` | private | The reconstruction time at which properties are extracted. |
| `d_filename` | field | `boost::optional<GPlatesPropertyValues::TextContent>` | private | The filename. |
| `d_inside_constant_value` | field | `bool` | private | — |
| `d_inside_piecewise_aggregation` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_EXTRACTSCALARFIELD3DFEATUREPROPERTIES_H` | macro | `None` | — |
| `is_scalar_field_3d_feature( const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `bool` | Returns true if the specified feature is a scalar field feature. |
| `contains_scalar_field_3d_feature( const GPlatesModel::FeatureCollectionHandle::const_weak_ref &feature_collection)` | function | `bool` | Returns true if the specified feature collection contains a scalar field feature. |

## Notes

[[[PROSE notes unit=app-logic/ExtractScalarField3DFeatureProperties tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ScalarField3DLayerProxy](ScalarField3DLayerProxy.md) | app-logic | 44 |
| [app-logic/ScalarField3DLayerParams](ScalarField3DLayerParams.md) | app-logic | 6 |
| [app-logic/ScalarField3DLayerTask](ScalarField3DLayerTask.md) | app-logic | 2 |
| [file-io/FeatureCollectionFileFormatClassify](../file-io/FeatureCollectionFileFormatClassify.md) | file-io | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ExtractScalarField3DFeatureProperties.h
python scripts/gpq.py def (anonymous)::CanResolveScalarField3DFeature --body
python scripts/gpq.py uses CanResolveScalarField3DFeature --kind class
python scripts/gpq.py hier CanResolveScalarField3DFeature
```
