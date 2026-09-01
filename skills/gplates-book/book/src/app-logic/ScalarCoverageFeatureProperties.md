# ScalarCoverageFeatureProperties

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 398 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ScalarCoverageFeatureProperties.h` | C++ | 122 |
| `src/app-logic/ScalarCoverageFeatureProperties.cc` | C++ | 513 |

## Overview

Identifies and extracts "scalar coverage" data from an ordinary `FeatureHandle`: a geometry domain property paired with a `GmlDataBlock` range property carrying one or more scalar values per domain point (for example imported crustal-thickness values on a `MeshNode` feature). GPlates does not have a dedicated feature type for this — it is a convention recognised by matching property names — so this unit centralises the heuristic in one place rather than letting every layer or exporter reimplement it.

The domain/range pairing is table-driven: `initialise_coverage_domain_to_range_name_mapping()` seeds a lazily-built map from domain property name to range property name, with `gpml:domainSet`/`gpml:rangeSet` as the default pair (`get_default_domain_range_property_names`), and `get_range_property_name_from_domain` looks up the range name for a given domain name. `is_scalar_coverage_feature` and `contains_scalar_coverage_feature` use this mapping to test features and feature collections without fully extracting their data. The actual extraction is done by the internal `ExtractScalarCoverageFeatureProperties` feature visitor (templated on `FeatureHandleType` so it works on both `const` and non-`const` handles), which walks the feature's properties at a given reconstruction time, resolves any time-dependent (`GpmlPiecewiseAggregation`/`GpmlConstantValue`) wrapping, and pairs up each matching domain geometry with its range `GmlDataBlock` into a `Coverage`; `get_coverages` is the public entry point that runs this visitor and returns the results.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::(anonymous)::coverage_domain_to_range_name_map_type`](#gplatesapplogicanonymouscoverage_domain_to_range_name_map_type) | typedef | — | — | 0 | — |
| [`GPlatesAppLogic::(anonymous)::ExtractScalarCoverageFeatureProperties`](#gplatesapplogicanonymousextractscalarcoveragefeatureproperties) | class | [`GPlatesModel::FeatureVisitorBase<FeatureHandleType>`](../model/FeatureVisitor.md) | `<class FeatureHandleType>` | 0 | Visits a scalar coverage feature and extracts domain/range coverages from it. |
| [`GPlatesAppLogic::ScalarCoverageFeatureProperties::Coverage`](#gplatesapplogicscalarcoveragefeaturepropertiescoverage) | struct | — | — | 0 | A coverage maps a geometry domain property to a range property containing one or more scalar types. |

## Members

### `GPlatesAppLogic::(anonymous)::coverage_domain_to_range_name_map_type`

*None.*

### `GPlatesAppLogic::(anonymous)::ExtractScalarCoverageFeatureProperties`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `feature_visitor_type` | typedef | `GPlatesModel::FeatureVisitorBase<FeatureHandleType>` | public | — |
| `Domain` | struct | `None` | public | — |
| `Range` | struct | `None` | public | — |
| `Coverage` | struct | `None` | public | — |
| `ExtractScalarCoverageFeatureProperties( const double &reconstruction_time = 0)` | constructor | `None` | public | — |
| `initialise_pre_feature_properties( typename feature_visitor_type::feature_handle_type &feature_handle)` | method | `bool` | public | — |
| `finalise_post_feature_properties( typename feature_visitor_type::feature_handle_type &feature_handle)` | method | `void` | public | — |
| `visit_gpml_constant_value( typename feature_visitor_type::gpml_constant_value_type &gpml_constant_value)` | method | `void` | public | — |
| `visit_gpml_piecewise_aggregation( typename feature_visitor_type::gpml_piecewise_aggregation_type &gpml_piecewise_aggregation)` | method | `void` | public | — |
| `visit_gml_data_block( typename feature_visitor_type::gml_data_block_type &gml_data_block)` | method | `void` | public | — |
| `visit_gml_line_string( typename feature_visitor_type::gml_line_string_type &gml_line_string)` | method | `void` | public | — |
| `visit_gml_multi_point( typename feature_visitor_type::gml_multi_point_type &gml_multi_point)` | method | `void` | public | — |
| `visit_gml_orientable_curve( typename feature_visitor_type::gml_orientable_curve_type &gml_orientable_curve)` | method | `void` | public | — |
| `visit_gml_point( typename feature_visitor_type::gml_point_type &gml_point)` | method | `void` | public | — |
| `visit_gml_polygon( typename feature_visitor_type::gml_polygon_type &gml_polygon)` | method | `void` | public | — |
| `d_reconstruction_time` | field | `GPlatesPropertyValues::GeoTimeInstant` | private | The reconstruction time at which properties are extracted. |
| `d_domains` | field | `std::vector<Domain>` | private | — |
| `d_ranges` | field | `std::vector<Range>` | private | — |
| `d_coverages` | field | `std::vector<Coverage>` | private | — |

### `GPlatesAppLogic::ScalarCoverageFeatureProperties::Coverage`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Coverage( GPlatesModel::FeatureHandle::iterator domain_property_, GPlatesModel::FeatureHandle::iterator range_property_, const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type domain_, const std::vector<GPlatesPropertyValues::GmlDataBlockCoordinateList::non_null_ptr_to_const_type> &range_)` | constructor | `None` | public | — |
| `domain_property` | field | `GPlatesModel::FeatureHandle::iterator` | public | — |
| `range_property` | field | `GPlatesModel::FeatureHandle::iterator` | public | — |
| `domain` | field | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | public | — |
| `range` | field | `std::vector<GPlatesPropertyValues::GmlDataBlockCoordinateList::non_null_ptr_to_const_type>` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `initialise_coverage_domain_to_range_name_mapping()` | function | `coverage_domain_to_range_name_map_type` | — |
| `GPLATES_APP_LOGIC_SCALARCOVERAGEFEATUREPROPERTIES_H` | macro | `None` | — |
| `is_scalar_coverage_feature( const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `bool` | Returns true if the specified feature behaves like a scalar coverage feature. |
| `contains_scalar_coverage_feature( const GPlatesModel::FeatureCollectionHandle::const_weak_ref &feature_collection)` | function | `bool` | Returns true if the specified feature collection contains a scalar coverage feature. |
| `get_range_property_name_from_domain( const GPlatesModel::PropertyName &domain_property_name)` | function | `boost::optional<GPlatesModel::PropertyName>` | Returns the property name of the range of a scalar coverage, if any, that is associated with the specified property name of a domain. |
| `get_default_domain_range_property_names()` | function | `std::pair<GPlatesModel::PropertyName/*domain*/, GPlatesModel::PropertyName/*range*/>` | Returns the default domain/range property names ('gpml:domainSet' and 'gpml:rangeSet'). |
| `get_coverages( std::vector<Coverage> &coverages, const GPlatesModel::FeatureHandle::weak_ref &feature, const double &reconstruction_time = 0)` | function | `bool` | Visits a scalar coverage feature and extracts domain/range coverages from it. |

## Notes

`get_coverages` returns `false` when no coverages were extracted rather than throwing, so callers must check the return value before trusting the (possibly empty) output vector. Extraction is heuristic, not schema-validated: a feature is treated as a scalar coverage purely because it has a domain property name that the internal mapping recognises paired with a data-block property, so features that happen to reuse `gpml:domainSet`/`gpml:rangeSet` for unrelated purposes would also match.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructScalarCoverageLayerProxy](ReconstructScalarCoverageLayerProxy.md) | app-logic | 48 |
| [app-logic/PartitionFeatureUtils](PartitionFeatureUtils.md) | app-logic | 15 |
| [file-io/GpmlFormatReconstructedScalarCoverageExport](../file-io/GpmlFormatReconstructedScalarCoverageExport.md) | file-io | 9 |
| [file-io/GpmlFormatDeformationExport](../file-io/GpmlFormatDeformationExport.md) | file-io | 5 |
| [app-logic/ReconstructScalarCoverageLayerTask](ReconstructScalarCoverageLayerTask.md) | app-logic | 4 |
| [file-io/FeatureCollectionFileFormatClassify](../file-io/FeatureCollectionFileFormatClassify.md) | file-io | 3 |
| [gui/FeatureInspectionCanvasToolWorkflow](../gui/FeatureInspectionCanvasToolWorkflow.md) | gui | 3 |
| [qt-widgets/GenerateDeformingMeshPointsDialog](../qt-widgets/GenerateDeformingMeshPointsDialog.md) | qt-widgets | 3 |
| [app-logic/ReconstructScalarCoverageLayerParams](ReconstructScalarCoverageLayerParams.md) | app-logic | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ScalarCoverageFeatureProperties.h
python scripts/gpq.py def GPlatesAppLogic::(anonymous)::ExtractScalarCoverageFeatureProperties --body
python scripts/gpq.py uses ExtractScalarCoverageFeatureProperties --kind class
python scripts/gpq.py hier ExtractScalarCoverageFeatureProperties
```
