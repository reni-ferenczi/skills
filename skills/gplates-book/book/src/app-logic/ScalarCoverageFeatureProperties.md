# ScalarCoverageFeatureProperties

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 398 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ScalarCoverageFeatureProperties.h` | C++ | 122 |
| `src/app-logic/ScalarCoverageFeatureProperties.cc` | C++ | 513 |

## Overview

[[[PROSE overview unit=app-logic/ScalarCoverageFeatureProperties tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=app-logic/ScalarCoverageFeatureProperties tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
