# ModelUtils

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 152 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/ModelUtils.h` | C++ | 614 |
| `src/model/ModelUtils.cc` | C++ | 1485 |

## Overview

This is the namespace where the revisioned model meets the GPGIM. `FeatureHandle`
will let you `add` any `TopLevelProperty` at all; it knows nothing about which
properties a feature type may hold or how their values must be shaped. The
functions here are the layer that consults `Gpgim` first, and they are what
almost everything outside the model calls when it needs to build or change a
feature: `add_property`, `set_property`, `set_properties`,
`create_top_level_property`, `rename_feature_properties`. If you write directly
to a `FeatureHandle` instead, you bypass every schema check the application
relies on.

The central piece of that work is the time-dependent wrapper.
`add_remove_or_convert_time_dependent_wrapper` compares the actual structural
type of a `PropertyValue` against the `GpgimProperty`'s time-dependent flags and
adds, removes or converts a `gpml:ConstantValue`, `gpml:PiecewiseAggregation` or
`gpml:IrregularSampling` wrapper so the stored value matches what the GPGIM
mandates. Every creation path funnels through it, which is why callers can hand
in a bare `GmlPoint` or an already-wrapped value and get back something the
schema accepts. `get_non_time_dependent_property_structural_type` is the
complement: it looks *through* a wrapper to the value type inside, so type
checking compares like with like.

Around that core sit three smaller groups. A handful of `create_gml_*` factories
attach the boilerplate XML attributes (the `gml:frame` of
`http://gplates.org/TRS/flat`, the `gml:orientation` sign) that GPML expects, so
those literals live in one place. A rotation-file group —
`TotalReconstructionPole`, `create_total_reconstruction_pole`,
`create_total_recon_seq`, `create_gml_time_sample`, `get_mprs_attributes` —
assembles `gpml:TotalReconstructionSequence` features out of five-tuples, and
carries a comment saying it would be better placed on a Handle class. Finally
`find_feature` resolves a `FeatureId` back to a live `FeatureHandle::weak_ref`
through the feature-ID back-reference registry.

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

The `error_code` out-parameter is written only on failure and is never cleared on
success, so it is meaningless unless the function returned `boost::none` or
`false`. It also defaults to `NULL` everywhere, and every site guards with
`if (error_code)` — except one: in
`get_non_time_dependent_gpgim_structural_type`, the
`PROPERTY_VALUE_TYPE_NOT_RECOGNISED` assignment is unguarded, so calling it with
the default argument on a property value the GPGIM does not recognise
dereferences a null pointer. Pass an `error_code` if you call that function
directly.

The three `check_*` boolean parameters default to `true` and each one turns off a
distinct GPGIM check: the property name against the feature type, the property
multiplicity, and the property value's structural type. Passing `false` is how
the file readers load pre-existing data that does not conform — turning one off
is a deliberate loosening, not a performance tweak. Note the asymmetry of the
`GpgimProperty` overloads: when you supply the GPGIM property yourself, no
feature-type check happens at all, and the header states that the caller is then
responsible for the property being legal on that feature type.

Wrapper conversion is deliberately not symmetric.
A `gpml:IrregularSampling` can neither be unwrapped nor converted to another
wrapper, and nothing can be wrapped *into* one — an irregular sampling has to be
built directly. A `gpml:PiecewiseAggregation` can only be reduced to a constant
value (or unwrapped) when it holds exactly one time window that spans distant
past to distant future and whose value is a `gpml:ConstantValue`; otherwise the
conversion fails rather than discarding data. When a bare value must be wrapped
and the GPGIM allows both, constant-value wins over piecewise aggregation.

Ownership: these functions never mutate the property value you hand them. Each
returns a new `PropertyValue` when a wrapper is added or removed, and the
original is returned unchanged when nothing is needed. `rename_property` deep
clones the value before rebuilding the property, so the renamed property shares
nothing with the original — but it does carry the original's XML attributes over.

`rename_feature_properties` is two-phase on purpose: it builds every renamed
property first and only touches the feature once all of them have succeeded, so a
failure leaves the feature untouched. Because a top-level property's name cannot
be changed in place, the rename is a remove-then-add, which means renamed
properties move to the end of the feature's property list and any iterator you
held to the old property is stale afterwards. The same applies to `set_property`
and `set_properties`, which mutate the feature *while* iterating it —
`FeatureHandle::remove` nulls a slot without shortening the sequence, so the
iterators stay usable, but existing iterators held elsewhere do not survive the
revisioning.

`add_property`, `set_property` and `set_properties` dereference the
`FeatureHandle::weak_ref` without checking `is_valid()`, unlike
`get_top_level_properties` and `get_top_level_geometry_properties`, which check.
Validate the weak reference before calling the mutating functions.

Two smaller traps. `get_mprs_attributes` takes a `const_weak_ref` and returns a
*non-const* pointer obtained with `const_cast`, and it throws
`GPlatesGlobal::LogException` when the `gpml:mprsAttributes` property is absent
rather than returning an optional — it is the one function here that reports
failure by exception. And `create_total_recon_seq` takes a `ModelInterface &`
that its body never uses; the feature is created through
`FeatureHandle::create` on the target collection.

`create_gml_time_period` defaults `check_begin_end_times` to `false` because,
as the header says, a lot of real data has a begin time later than its end time.
Turning the check on makes it throw `BeginTimeLaterThanEndTimeException`.

Both `get_error_message` overloads index a static array with the enum value and
assert its length against `NUM_ERRORS` at compile time, so the message array and
the enumerator order must be kept in step and `NUM_ERRORS` must stay last.
`GetGpgimTemplateStructuralTypeVisitor` lives in an anonymous namespace in the
`.cc` and is not part of the interface.

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
