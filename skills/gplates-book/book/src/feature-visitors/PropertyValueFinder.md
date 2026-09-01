# PropertyValueFinder

[Book TOC](../../TOC.md) · [feature-visitors](../../components/feature-visitors.md) · cluster Community 661 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/feature-visitors/PropertyValueFinder.h` | C++ | 656 |
| `src/feature-visitors/PropertyValueFinder.cc` | C++ | 295 |

## Overview

[[[PROSE overview unit=feature-visitors/PropertyValueFinder tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFeatureVisitors::(anonymous)::InterpolateIrregularSamplingVisitor`](#gplatesfeaturevisitorsanonymousinterpolateirregularsamplingvisitor) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Interpolation of an irregularly-sampled time-dependent property between the two time samples that surround a specific time instant. |
| [`GPlatesFeatureVisitors::Implementation::PropertyValueFinderBase`](#gplatesfeaturevisitorsimplementationpropertyvaluefinderbase) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | `<class PropertyValueType>` | 0 | Base implementation class for feature visitor that finds all PropertyValue's of type PropertyValueType and with property name included in a specified list that are contained within a feature. |

## Members

### `GPlatesFeatureVisitors::(anonymous)::InterpolateIrregularSamplingVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InterpolateIrregularSamplingVisitor( const GPlatesModel::PropertyValue &property_value1, const GPlatesModel::PropertyValue &property_value2, const double &time1, const double &time2, const double &target_time)` | constructor | `None` | public | — |
| `interpolate()` | method | `boost::optional<GPlatesModel::PropertyValue::non_null_ptr_to_const_type>` | public | Returns the interpolated property value if the property value 'type' is interpolable. |
| `visit_gpml_finite_rotation( gpml_finite_rotation_type &gpml_finite_rotation1)` | method | `void` | private | — |
| `visit_xs_double( xs_double_type &xs_double1)` | method | `void` | private | — |
| `d_property_value1` | field | `GPlatesModel::PropertyValue` | private | — |
| `d_property_value2` | field | `GPlatesModel::PropertyValue` | private | — |
| `d_time1` | field | `double` | private | — |
| `d_time2` | field | `double` | private | — |
| `d_target_time` | field | `double` | private | — |
| `d_interpolated_property_value` | field | `boost::optional<GPlatesModel::PropertyValue::non_null_ptr_to_const_type>` | private | — |

### `GPlatesFeatureVisitors::Implementation::PropertyValueFinderBase`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~PropertyValueFinderBase()` | destructor | `None` | public | — |
| `add_property_name_to_allow( const GPlatesModel::PropertyName &property_name_to_allow)` | method | `void` | public | — |
| `initialise_pre_property_values( top_level_property_inline_type &top_level_property_inline)` | method | `bool` | protected | — |
| `visit_gpml_constant_value( gpml_constant_value_type &gpml_constant_value)` | method | `void` | protected | — |
| `visit_gpml_irregular_sampling( gpml_irregular_sampling_type &gpml_irregular_sampling)` | method | `void` | protected | In case property value is time-dependent. |
| `visit_gpml_piecewise_aggregation( gpml_piecewise_aggregation_type &gpml_piecewise_aggregation)` | method | `void` | protected | In case property value is time-dependent. |
| `PropertyValueFinderBase( const double &reconstruction_time = 0)` | constructor | `None` | protected | Only derived class can instantiate. |
| `PropertyValueFinderBase( const GPlatesModel::PropertyName &property_name_to_allow, const double &reconstruction_time = 0)` | constructor | `None` | protected | Only derived class can instantiate. |
| `d_property_names_to_allow` | field | `std::vector<GPlatesModel::PropertyName>` | protected | — |
| `d_reconstruction_time` | field | `GPlatesPropertyValues::GeoTimeInstant` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FEATUREVISITORS_PROPERTYVALUEFINDER_H` | macro | `None` | — |
| `get_property_value( const GPlatesModel::PropertyValue &property_value_base, const double &reconstruction_time = 0)` | function | `boost::optional<typename PropertyValueType::non_null_ptr_to_const_type>` | Returns the derived property value of type PropertValueType if property\_value\_base is an instance of that type. reconstruction\_time only applies to time-dependent properties in which case the value of the property at the specified time is ... |
| `get_property_value( const FeatureOrPropertyType &feature_or_property, const GPlatesModel::PropertyName &property_name, const double &reconstruction_time = 0)` | function | `boost::optional<typename PropertyValueType::non_null_ptr_to_const_type>` | Returns true if feature\_or\_property has/is a property value of type PropertyValueType and property name property\_name. |
| `get_property_value( const FeatureOrPropertyType &feature_or_property, PropertyNamesForwardIter property_names_begin, PropertyNamesForwardIter property_names_end, const double &reconstruction_time = 0)` | function | `boost::optional<typename PropertyValueType::non_null_ptr_to_const_type>` | and property name in the sequence \[property\_names\_begin, property\_names\_end). |
| `get_property_values( const FeatureOrPropertyType &feature_or_property, const GPlatesModel::PropertyName &property_name, const double &reconstruction_time = 0)` | function | `std::vector<typename PropertyValueType::non_null_ptr_to_const_type>` | Returns true if feature\_or\_property has/is any property values of type PropertyValueType with property name property\_name. |
| `get_property_values( const FeatureOrPropertyType &feature_or_property, PropertyNamesForwardIter property_names_begin, PropertyNamesForwardIter property_names_end, const double &reconstruction_time = 0)` | function | `std::vector<typename PropertyValueType::non_null_ptr_to_const_type>` | Returns true if feature\_or\_property has/is any property values of type PropertyValueType and property name in the sequence \[property\_names\_begin, property\_names\_end). |
| `visit_gpml_constant_value( GPlatesModel::ConstFeatureVisitor::gpml_constant_value_type &gpml_constant_value, GPlatesModel::ConstFeatureVisitor &property_value_finder_visitor)` | function | `void` | NOTE: These function are not templates purely so they can be defined in the ".cc" file to avoid cyclic header dependencies including headers for irregular sampling and piecewise aggregation. |
| `visit_gpml_irregular_sampling_at_reconstruction_time( GPlatesModel::ConstFeatureVisitor::gpml_irregular_sampling_type &gpml_irregular_sampling, GPlatesModel::ConstFeatureVisitor &property_value_finder_visitor, const GPlatesPropertyValues::GeoTimeInstant &reconstruction_time, const std::type_info &property_value_type_in ...` | function | `void` | — |
| `visit_gpml_piecewise_aggregation_at_reconstruction_time( GPlatesModel::ConstFeatureVisitor::gpml_piecewise_aggregation_type &gpml_piecewise_aggregation, GPlatesModel::ConstFeatureVisitor &property_value_finder_visitor, const GPlatesPropertyValues::GeoTimeInstant &reconstruction_time)` | function | `void` | — |
| `DECLARE_PROPERTY_VALUE_FINDER_CLASS` | macro_function | `namespace GPlatesFeatureVisitors \ { \ namespace Implementation \ { \ template <> \ class PropertyValueFinder<property_value_type> : \ public PropertyValueFinderBase<property_value ...` | Macro to declare a template specialisation of class PropertyValueFinder. |
| `find_property_values( \ const feature_weak_ref_type &feature_weak_ref)` | function | `property_value_container_range` | Returns begin/end iterator to any found property values. \*/ \\ |
| `find_property_values( \ const feature_collection_iterator_type &feature_collection_iterator)` | function | `property_value_container_range` | Returns begin/end iterator to any found property values. \*/ \\ |
| `find_property_values( \ const feature_iterator_type &feature_iterator)` | function | `property_value_container_range` | Returns begin/end iterator to any found property values. \*/ \\ |
| `find_property_values( \ /* Using PropertyValue instead of derived property value type to avoid undefined class error... */ \ GPlatesUtils::CopyConst<property_value_type, GPlatesModel::PropertyValue>::type &property_value_base)` | function | `property_value_container_range` | Returns begin/end iterator to any found property values. \*/ \\ |
| `d_found_property_values` | variable | `property_value_container_type` | — |
| `DECLARE_PROPERTY_VALUE_FINDER` | macro_function | `DECLARE_PROPERTY_VALUE_FINDER_CLASS( \ boost::add_const<property_value_type>::type, \ visit_property_value_method)` | NOTE: DECLARE\_PROPERTY\_VALUE\_FINDER must be placed at the top of every derivation of GPlatesModel::PropertyValue in order for the get property functions in this file to work with that type of property value. |
| `get_property_value( const GPlatesModel::PropertyValue &property_value_base, const double &reconstruction_time)` | function | `boost::optional<typename PropertyValueType::non_null_ptr_to_const_type>` | — |
| `get_property_values( const FeatureOrPropertyType &feature_or_property, const GPlatesModel::PropertyName &property_name, const double &reconstruction_time)` | function | `std::vector<typename PropertyValueType::non_null_ptr_to_const_type>` | — |
| `get_property_values( const FeatureOrPropertyType &feature_or_property, PropertyNamesForwardIter property_names_begin, PropertyNamesForwardIter property_names_end, const double &reconstruction_time)` | function | `std::vector<typename PropertyValueType::non_null_ptr_to_const_type>` | — |
| `get_property_value( const FeatureOrPropertyType &feature_or_property, const GPlatesModel::PropertyName &property_name, const double &reconstruction_time)` | function | `boost::optional<typename PropertyValueType::non_null_ptr_to_const_type>` | — |
| `get_property_value( const FeatureOrPropertyType &feature_or_property, PropertyNamesForwardIter property_names_begin, PropertyNamesForwardIter property_names_end, const double &reconstruction_time)` | function | `boost::optional<typename PropertyValueType::non_null_ptr_to_const_type>` | — |

## Notes

[[[PROSE notes unit=feature-visitors/PropertyValueFinder tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [feature-visitors/QueryFeaturePropertiesWidgetPopulator](QueryFeaturePropertiesWidgetPopulator.md) | feature-visitors | 27 |
| [feature-visitors/ViewFeatureGeometriesWidgetPopulator](ViewFeatureGeometriesWidgetPopulator.md) | feature-visitors | 15 |
| [feature-visitors/ToQvariantConverter](ToQvariantConverter.md) | feature-visitors | 14 |
| [feature-visitors/TopologySectionsFinder](TopologySectionsFinder.md) | feature-visitors | 12 |
| [file-io/OgrFeatureCollectionWriter](../file-io/OgrFeatureCollectionWriter.md) | file-io | 12 |
| [file-io/PlatesFormatUtils](../file-io/PlatesFormatUtils.md) | file-io | 12 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 12 |
| [file-io/OgrUtils](../file-io/OgrUtils.md) | file-io | 10 |
| [feature-visitors/TotalReconstructionSequencePlateIdFinder](TotalReconstructionSequencePlateIdFinder.md) | feature-visitors | 9 |
| [gui/TopologySectionsTableColumns](../gui/TopologySectionsTableColumns.md) | gui | 9 |
| [qt-widgets/TopologyToolsWidget](../qt-widgets/TopologyToolsWidget.md) | qt-widgets | 9 |
| [feature-visitors/TotalReconstructionSequenceRotationInserter](TotalReconstructionSequenceRotationInserter.md) | feature-visitors | 8 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 8 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 8 |
| [feature-visitors/ShapefileAttributeFinder](ShapefileAttributeFinder.md) | feature-visitors | 7 |
| [feature-visitors/TotalReconstructionSequenceTimePeriodFinder](TotalReconstructionSequenceTimePeriodFinder.md) | feature-visitors | 7 |
| [file-io/GMTFormatDeformationExport](../file-io/GMTFormatDeformationExport.md) | file-io | 7 |
| [file-io/GMTFormatReconstructedScalarCoverageExport](../file-io/GMTFormatReconstructedScalarCoverageExport.md) | file-io | 7 |
| [qt-widgets/FeatureSummaryWidget](../qt-widgets/FeatureSummaryWidget.md) | qt-widgets | 7 |
| [feature-visitors/deprecated/PlateIdFinder](deprecated/PlateIdFinder.md) | feature-visitors | 6 |

*... and 89 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/feature-visitors/PropertyValueFinder.h
python scripts/gpq.py def GPlatesFeatureVisitors::(anonymous)::InterpolateIrregularSamplingVisitor --body
python scripts/gpq.py uses InterpolateIrregularSamplingVisitor --kind class
python scripts/gpq.py hier InterpolateIrregularSamplingVisitor
```
