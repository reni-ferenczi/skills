# ModelUtils

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 152 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/ModelUtils.h` | C++ | 614 |
| `src/model/ModelUtils.cc` | C++ | 1485 |

## Overview

[[[PROSE overview unit=model/ModelUtils tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::GetGpgimTemplateStructuralTypeVisitor`](#anonymousgetgpgimtemplatestructuraltypevisitor) | class | [`GPlatesModel::ConstFeatureVisitor`](FeatureVisitor.md) | — | 0 | Visits a property value to retrieve the GpgimTemplateStructuralType associated with it (if any). |
| [`GPlatesModel::ModelUtils::TotalReconstructionPole`](#gplatesmodelmodelutilstotalreconstructionpole) | struct | — | — | 0 | Note: Consider adding functions as member functions in one of the Handle classes instead. |
| [`GPlatesModel::ModelUtils::TimeDependentError::Type`](#gplatesmodelmodelutilstimedependenterrortype) | enum | — | — | 0 | — |
| [`GPlatesModel::ModelUtils::TopLevelPropertyError::Type`](#gplatesmodelmodelutilstoplevelpropertyerrortype) | enum | — | — | 0 | — |

## Members

### `(anonymous)::GetGpgimTemplateStructuralTypeVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `get_gpgim_template_structural_type_from_property( const GPlatesModel::FeatureHandle::iterator &property)` | method | `boost::optional<GPlatesModel::GpgimTemplateStructuralType::non_null_ptr_to_const_type>` | public | — |
| `get_gpgim_template_structural_type_from_property( const GPlatesModel::TopLevelProperty::non_null_ptr_type &property)` | method | `boost::optional<GPlatesModel::GpgimTemplateStructuralType::non_null_ptr_to_const_type>` | public | — |
| `get_gpgim_template_structural_type_from_property_value( const GPlatesModel::PropertyValue &property_value)` | method | `boost::optional<GPlatesModel::GpgimTemplateStructuralType::non_null_ptr_to_const_type>` | public | — |
| `visit_gpml_constant_value( const gpml_constant_value_type &gpml_constant_value)` | method | `void` | private | — |
| `visit_gpml_piecewise_aggregation( const gpml_piecewise_aggregation_type &gpml_piecewise_aggregation)` | method | `void` | private | — |
| `visit_gpml_array( const gpml_array_type &gpml_array)` | method | `void` | private | — |
| `d_gpgim_template_structural_type` | field | `boost::optional<GPlatesModel::GpgimTemplateStructuralType::non_null_ptr_to_const_type>` | private | — |

### `GPlatesModel::ModelUtils::TotalReconstructionPole`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `time` | field | `double` | public | — |
| `lat_of_euler_pole` | field | `double` | public | — |
| `lon_of_euler_pole` | field | `double` | public | — |
| `rotation_angle` | field | `double` | public | — |
| `comment` | field | `QString` | public | — |

### `GPlatesModel::ModelUtils::TimeDependentError::Type`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `COULD_NOT_WRAP_INTO_A_TIME_DEPENDENT_PROPERTY` | enumerator | `None` | — | — |
| `COULD_NOT_UNWRAP_EXISTING_TIME_DEPENDENT_PROPERTY` | enumerator | `None` | — | — |
| `COULD_NOT_CONVERT_FROM_ONE_TIME_DEPENDENT_WRAPPER_TO_ANOTHER` | enumerator | `None` | — | — |
| `NUM_ERRORS` | enumerator | `None` | — | — |

### `GPlatesModel::ModelUtils::TopLevelPropertyError::Type`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `NOT_ONE_PROPERTY_VALUE` | enumerator | `None` | — | — |
| `NOT_TOP_LEVEL_PROPERTY_INLINE` | enumerator | `None` | — | — |
| `PROPERTY_NAME_NOT_RECOGNISED` | enumerator | `None` | — | — |
| `PROPERTY_NAME_CAN_OCCUR_AT_MOST_ONCE_IN_A_FEATURE` | enumerator | `None` | — | — |
| `PROPERTY_NAME_NOT_SUPPORTED_BY_FEATURE_TYPE` | enumerator | `None` | — | — |
| `PROPERTY_VALUE_TYPE_NOT_SUPPORTED_BY_PROPERTY_NAME` | enumerator | `None` | — | — |
| `PROPERTY_VALUE_TYPE_NOT_RECOGNISED` | enumerator | `None` | — | — |
| `COULD_NOT_WRAP_INTO_A_TIME_DEPENDENT_PROPERTY` | enumerator | `None` | — | — |
| `COULD_NOT_UNWRAP_EXISTING_TIME_DEPENDENT_PROPERTY` | enumerator | `None` | — | — |
| `COULD_NOT_CONVERT_FROM_ONE_TIME_DEPENDENT_WRAPPER_TO_ANOTHER` | enumerator | `None` | — | — |
| `NUM_ERRORS` | enumerator | `None` | — | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_top_level_property_inline( QualifiedTopLevelProperty &top_level_property, GPlatesModel::ModelUtils::TopLevelPropertyError::Type *error_code)` | function | `boost::optional<QualifiedTopLevelPropertyInline &>` | 'QualifiedTopLevelPropertyInline' can be 'const TopLevelPropertyInline' or 'TopLevelPropertyInline'. 'QualifiedTopLevelProperty' can be 'const TopLevelProperty' or 'TopLevelProperty'. |
| `get_property_value( QualifiedTopLevelProperty &top_level_property, GPlatesModel::ModelUtils::TopLevelPropertyError::Type *error_code)` | function | `boost::optional<GPlatesUtils::non_null_intrusive_ptr<QualifiedPropertyValue> >` | 'QualifiedTopLevelPropertyInline' can be 'const TopLevelPropertyInline' or 'TopLevelPropertyInline'. 'QualifiedTopLevelProperty' can be 'const TopLevelProperty' or 'TopLevelProperty'. |
| `check_property_multiplicity_supports_add_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, const GPlatesModel::GpgimProperty &gpgim_property, GPlatesModel::ModelUtils::TopLevelPropertyError::Type *error_code)` | function | `bool` | Ensure that if a property, described by gpgim\_property, is added to feature then it will not exceed the number of properties allowed per feature for that property description. |
| `check_property_value_type_supported( const GPlatesModel::PropertyValue &property_value, const GPlatesModel::GpgimProperty &gpgim_property, GPlatesModel::ModelUtils::TopLevelPropertyError::Type *error_code)` | function | `bool` | Ensure that the (non-time-dependent) property value structural type of property\_value is one of the supported structural types of gpgim\_property. |
| `add_remove_or_convert_time_dependent_wrapper( const GPlatesModel::PropertyValue::non_null_ptr_type &property_value, const GPlatesModel::GpgimProperty &gpgim_property, GPlatesModel::ModelUtils::TopLevelPropertyError::Type *error_code)` | function | `boost::optional<GPlatesModel::PropertyValue::non_null_ptr_type>` | — |
| `GPLATES_MODEL_MODELUTILS_H` | macro | `None` | — |
| `create_gml_orientable_curve( const GPlatesPropertyValues::GmlLineString::non_null_ptr_type gml_line_string, bool reverse_orientation = false)` | function | `GPlatesPropertyValues::GmlOrientableCurve::non_null_ptr_type` | — |
| `create_gml_time_period( const GPlatesPropertyValues::GeoTimeInstant &geo_time_instant_begin, const GPlatesPropertyValues::GeoTimeInstant &geo_time_instant_end, bool check_begin_end_times = false)` | function | `GPlatesPropertyValues::GmlTimePeriod::non_null_ptr_type` | Create a GmlTimePeriod instance which begins at geo\_time\_instant\_begin and ends at geo\_time\_instant\_end. |
| `create_gml_time_instant( const GPlatesPropertyValues::GeoTimeInstant &geo_time_instant)` | function | `GPlatesPropertyValues::GmlTimeInstant::non_null_ptr_type` | — |
| `create_total_reconstruction_pole( const std::vector<TotalReconstructionPole> &five_tuples)` | function | `TopLevelProperty::non_null_ptr_type` | Create a total reconstruction pole property. |
| `create_total_recon_seq( ModelInterface &model, const FeatureCollectionHandle::weak_ref &target_collection, unsigned long fixed_plate_id, unsigned long moving_plate_id, const std::vector<TotalReconstructionPole> &five_tuples)` | function | `FeatureHandle::weak_ref` | — |
| `create_gml_time_sample( const ModelUtils::TotalReconstructionPole &trp)` | function | `GPlatesPropertyValues::GpmlTimeSample` | Create a total reconstruction pole time sample. |
| `get_error_message( TimeDependentError::Type error_code)` | function | `char` | Returns the error message string associated with the specified error code. |
| `get_non_time_dependent_property_structural_type( const PropertyValue &property_value)` | function | `GPlatesPropertyValues::StructuralType` | Returns the non-time-dependent structural type of the specified property value. |
| `add_remove_or_convert_time_dependent_wrapper( const PropertyValue::non_null_ptr_type &property_value, const GpgimProperty &gpgim_property, TimeDependentError::Type *error_code = NULL)` | function | `boost::optional<PropertyValue::non_null_ptr_type>` | Attempts to add, remove or convert a time-dependent wrapper for the specified property value as dictated by the GPGIM (gpgim\_property). |
| `create_gpml_constant_value( const PropertyValue::non_null_ptr_type &property_value, boost::optional<GPlatesUtils::UnicodeString> description = boost::none)` | function | `GPlatesPropertyValues::GpmlConstantValue::non_null_ptr_type` | Wraps a regular property value in a 'gpml:GpmlConstantValue' property value. |
| `create_gpml_piecewise_aggregation( const GPlatesPropertyValues::GpmlConstantValue::non_null_ptr_type &constant_value_property_value)` | function | `GPlatesPropertyValues::GpmlPiecewiseAggregation::non_null_ptr_type` | Wraps a 'gpml:ConstantValue' property value in a 'gpml:PiecewiseAggregation' property value. |
| `get_error_message( TopLevelPropertyError::Type error_code)` | function | `char` | Returns the error message string associated with the specified error code. |
| `get_top_level_property_inline( const TopLevelProperty &top_level_property, TopLevelPropertyError::Type *error_code = NULL)` | function | `boost::optional<const TopLevelPropertyInline &>` | Returns the specified top-level property as an \*inline\* top-level property. |
| `get_top_level_property_inline( TopLevelProperty &top_level_property, TopLevelPropertyError::Type *error_code = NULL)` | function | `boost::optional<TopLevelPropertyInline &>` | Non-const overload. |
| `get_property_value( const TopLevelProperty &top_level_property, TopLevelPropertyError::Type *error_code = NULL)` | function | `boost::optional<PropertyValue::non_null_ptr_to_const_type>` | Returns the property value of the specified top-level property. |
| `get_property_value( TopLevelProperty &top_level_property, TopLevelPropertyError::Type *error_code = NULL)` | function | `boost::optional<PropertyValue::non_null_ptr_type>` | Non-const overload. |
| `get_top_level_properties( const PropertyName &property_name, FeatureHandle::weak_ref feature)` | function | `std::vector<FeatureHandle::iterator>` | Returns a list of top-level properties matching the specified property name in the specified feature. |
| `get_top_level_geometry_properties( FeatureHandle::weak_ref feature)` | function | `std::vector<FeatureHandle::iterator>` | Returns a list of top-level \*geometry\* properties in the specified feature. |
| `get_gpgim_property( const PropertyName& property_name, boost::optional<FeatureType> feature_type = boost::none, TopLevelPropertyError::Type *error_code = NULL)` | function | `boost::optional<GpgimProperty::non_null_ptr_to_const_type>` | Get the GPGIM property using the property name (and optionally the feature type). |
| `get_non_time_dependent_gpgim_structural_type( const PropertyValue &property_value, TopLevelPropertyError::Type *error_code = NULL)` | function | `boost::optional<GpgimStructuralType::non_null_ptr_to_const_type>` | Get the non-time-dependent GPGIM structural type of the specified property value. |
| `create_top_level_property( const PropertyName& property_name, const PropertyValue::non_null_ptr_type &property_value, boost::optional<FeatureType> feature_type = boost::none, bool check_property_value_type = true, TopLevelPropertyError::Type *error_code = NULL)` | function | `boost::optional<TopLevelProperty::non_null_ptr_type>` | Creates a TopLevelPropertyInline from the specified property value. |
| `create_top_level_property( const GpgimProperty &gpgim_property, const PropertyValue::non_null_ptr_type &property_value, bool check_property_value_type = true, TopLevelPropertyError::Type *error_code = NULL)` | function | `boost::optional<TopLevelProperty::non_null_ptr_type>` | An overload of create\_top\_level\_property for when the GPGIM property has already been determined by the caller (from the property name). |
| `add_property( const FeatureHandle::weak_ref &feature, const PropertyName& property_name, const PropertyValue::non_null_ptr_type &property_value, bool check_property_name_allowed_for_feature_type = true, bool check_property_multiplicity = true, bool check_property_value_type = true, TopLevelPropertyError::Type *error_co ...` | function | `boost::optional<FeatureHandle::iterator>` | Creates a TopLevelPropertyInline from the specified property value and adds it into the specified feature (and returns iterator to property). |
| `add_property( const FeatureHandle::weak_ref &feature, const GpgimProperty &gpgim_property, const PropertyValue::non_null_ptr_type &property_value, bool check_property_multiplicity = true, bool check_property_value_type = true, TopLevelPropertyError::Type *error_code = NULL)` | function | `boost::optional<FeatureHandle::iterator>` | An overload of add\_property for when the GPGIM property has already been determined by the caller (from the property name). |
| `set_property( const FeatureHandle::weak_ref &feature, const PropertyName& property_name, const PropertyValue::non_null_ptr_type &property_value, bool check_property_name_allowed_for_feature_type = true, bool check_property_value_type = true, TopLevelPropertyError::Type *error_code = NULL)` | function | `boost::optional<FeatureHandle::iterator>` | This function is similar to add\_property except it first removes any existing properties named property\_name. |
| `set_property( const FeatureHandle::weak_ref &feature, const GpgimProperty &gpgim_property, const PropertyValue::non_null_ptr_type &property_value, bool check_property_value_type = true, TopLevelPropertyError::Type *error_code = NULL)` | function | `boost::optional<FeatureHandle::iterator>` | An overload of set\_property for when the GPGIM property has already been determined by the caller (from the property name). |
| `set_properties( std::vector<FeatureHandle::iterator> &feature_properties, const FeatureHandle::weak_ref &feature, const PropertyName& property_name, const std::vector<PropertyValue::non_null_ptr_type> &property_values, bool check_property_name_allowed_for_feature_type = true, bool check_property_multiplicity = true, bo ...` | function | `bool` | This function is similar to set\_property except it sets multiple properties with the same name. |
| `set_properties( std::vector<FeatureHandle::iterator> &feature_properties, const FeatureHandle::weak_ref &feature, const GpgimProperty &gpgim_property, const std::vector<PropertyValue::non_null_ptr_type> &property_values, bool check_property_multiplicity = true, bool check_property_value_type = true, TopLevelPropertyErr ...` | function | `bool` | An overload of set\_properties for when the GPGIM property has already been determined by the caller (from the property name). |
| `get_mprs_attributes( FeatureHandle::const_weak_ref f)` | function | `GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type` | Given the feature reference, return the MPRS(Moving Plate Rotation Sequence) metadata as a GpmlKeyValueDictionary. |
| `rename_feature_properties( FeatureHandle &feature, const PropertyName &old_property_name, const PropertyName &new_property_name, bool check_new_property_name_allowed_for_feature_type = true, boost::optional< std::vector<FeatureHandle::iterator> &> renamed_feature_properties = boost::none, TopLevelPropertyError::Type *e ...` | function | `bool` | Renames all properties of feature, with property name matching old\_property\_name, to property name new\_property\_name. |
| `rename_property( const TopLevelProperty &top_level_property, const PropertyName &new_property_name, TopLevelPropertyError::Type *error_code = NULL)` | function | `boost::optional<TopLevelProperty::non_null_ptr_type>` | Takes an existing top\_level\_property and returns a new top-level property object with the same property value (aside from time-dependent differences) as top\_level\_property but with the new\_property\_name. |
| `rename_property( const TopLevelProperty &top_level_property, const GpgimProperty &new_gpgim_property, TopLevelPropertyError::Type *error_code = NULL)` | function | `boost::optional<TopLevelProperty::non_null_ptr_type>` | An overload of rename\_property for when the GPGIM property has already been determined by the caller (from the new property name). |
| `find_feature( const FeatureId &id)` | function | `FeatureHandle::weak_ref` | Find the FeatureHandle weak ref given the feature id as FeatureId. |
| `find_feature( const QString &id)` | function | `FeatureHandle::weak_ref` | Find the FeatureHandle weak ref given the feature id as QString. |

## Notes

[[[PROSE notes unit=model/ModelUtils tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 53 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 41 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 25 |
| [entry-points/gplates_demo_no_gui_main](../entry-points/gplates_demo_no_gui_main.md) | entry-points | 24 |
| [qt-widgets/EditTotalReconstructionSequenceWidget](../qt-widgets/EditTotalReconstructionSequenceWidget.md) | qt-widgets | 20 |
| [qt-widgets/GenerateDeformingMeshPointsDialog](../qt-widgets/GenerateDeformingMeshPointsDialog.md) | qt-widgets | 17 |
| [app-logic/PartitionFeatureUtils](../app-logic/PartitionFeatureUtils.md) | app-logic | 15 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 15 |
| [qt-widgets/CreateFeatureAddOrEditPropertyDialog](../qt-widgets/CreateFeatureAddOrEditPropertyDialog.md) | qt-widgets | 11 |
| [view-operations/SplitFeatureUndoCommand](../view-operations/SplitFeatureUndoCommand.md) | view-operations | 10 |
| [file-io/GmapReader](../file-io/GmapReader.md) | file-io | 9 |
| [qt-widgets/EditTimeSequenceWidget](../qt-widgets/EditTimeSequenceWidget.md) | qt-widgets | 9 |
| [qt-widgets/ChangePropertyWidget](../qt-widgets/ChangePropertyWidget.md) | qt-widgets | 8 |
| [qt-widgets/ImportRasterDialog](../qt-widgets/ImportRasterDialog.md) | qt-widgets | 8 |
| [qt-widgets/MetadataDialog](../qt-widgets/MetadataDialog.md) | qt-widgets | 8 |
| [qt-widgets/CreateVGPDialog](../qt-widgets/CreateVGPDialog.md) | qt-widgets | 7 |
| [qt-widgets/EditTimePeriodWidget](../qt-widgets/EditTimePeriodWidget.md) | qt-widgets | 7 |
| [qt-widgets/TopologyToolsWidget](../qt-widgets/TopologyToolsWidget.md) | qt-widgets | 7 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 7 |
| [file-io/GpmlFormatReconstructedScalarCoverageExport](../file-io/GpmlFormatReconstructedScalarCoverageExport.md) | file-io | 6 |

*... and 44 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/ModelUtils.h
python scripts/gpq.py def (anonymous)::GetGpgimTemplateStructuralTypeVisitor --body
python scripts/gpq.py uses GetGpgimTemplateStructuralTypeVisitor --kind class
python scripts/gpq.py hier GetGpgimTemplateStructuralTypeVisitor
```
