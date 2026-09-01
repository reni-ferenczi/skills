# FeatureVisitor

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 207 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/FeatureVisitor.h` | C++ | 880 |
| `src/model/FeatureVisitor.cc` | C++ | 81 |

## Overview

Property values in GPlates are a large open-ended class hierarchy —
`GpmlPlateId`, `GmlTimePeriod`, `GpmlConstantValue` and forty-odd others — and
almost every consumer of the model (the file writers, the geometry finders, the
edit widgets, the Python bindings) needs to do something different for each of
them. This header is the single Visitor interface that makes that dispatch
possible: `PropertyValue::accept_visitor` calls back into the matching
`visit_<type>` member here, so the type switch lives in the property-value class
rather than in every consumer. Every `visit_` function has an empty default body,
so a derived visitor overrides only what it cares about, and each carries the
target type in its name because overriding any one member named `visit` would
hide all the others in the base.

Traversal is a template method, not something the visitor drives itself.
`visit_feature()` checks the weak-ref or iterator is still valid, then
`visit_feature_handle` runs `initialise_pre_feature_properties` (returning false
skips the rest of the feature, and suppresses `finalise_post_feature_properties`),
walks the top-level properties, and finishes with
`finalise_post_feature_properties`; each `TopLevelPropertyInline` repeats the
pattern one level down with `initialise_pre_property_values` and
`finalise_post_property_values`. While a property is being visited,
`current_top_level_propiter()` and `current_top_level_propname()` tell the visitor
which property it is inside — this is how visitors that only care about, say,
`gpml:reconstructionPlateId` filter without overriding the traversal. Both are
reset to `boost::none` between properties. Derived classes are meant to hook the
initialise/finalise pair, not override `visit_feature_handle` or the non-virtual
`visit_feature_properties`.

The one template parameter, const or non-const `FeatureHandle`, produces the two
typedefs `FeatureVisitor` and `ConstFeatureVisitor`, with
`FeatureVisitorInternals::Traits` and `GPlatesUtils::CopyConst` propagating the
constness to every iterator and property-value parameter. The difference between
them is not cosmetic. Because properties inside the model are immutable, the
non-const specialisation of `visit_feature_property` in `FeatureVisitor.cc` cannot
hand out a mutable property: it takes a `deep_clone()` of the property, visits the
clone, and assigns it back through the iterator — which routes through
`FeatureHandle::set` and deep-clones a second time. Every property of every
feature a non-const visitor touches therefore costs two deep copies and a
modification notification, whether or not the visitor changed anything, which is
why the header urges you to derive from `ConstFeatureVisitor` unless you really
are editing. `FeatureVisitorThatGuaranteesNotToModify` is the acknowledged hack in
between: it `const_cast`s the property instead of cloning it, and its correctness
rests entirely on subclasses honouring the promise in its name.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::FeatureVisitorInternals::Traits`](#gplatesmodelfeaturevisitorinternalstraits) | struct | — | `<class FeatureHandleType>` | 0 | A helper traits class to differentiate between const and non-const FeatureHandles. |
| [`GPlatesModel::FeatureVisitorInternals::Traits<const FeatureHandleType>`](#gplatesmodelfeaturevisitorinternalstraitsconst-featurehandletype) | struct | — | `<class FeatureHandleType>` | 0 | — |
| [`GPlatesModel::FeatureVisitorBase`](#gplatesmodelfeaturevisitorbase) | class | — | `<class FeatureHandleType>` | 1 | This class defines an abstract interface for a Visitor to visit features. |
| [`GPlatesModel::FeatureVisitor`](#gplatesmodelfeaturevisitor) | typedef | — | — | 26 | — |
| [`GPlatesModel::ConstFeatureVisitor`](#gplatesmodelconstfeaturevisitor) | typedef | — | — | 63 | — |
| [`GPlatesModel::FeatureVisitorThatGuaranteesNotToModify`](#gplatesmodelfeaturevisitorthatguaranteesnottomodify) | class | [`FeatureVisitor`](FeatureVisitor.md) | — | 2 | FIXME: This is temporary until we resolve the overhead of cloning properties in non-const visitors or come to accept the overhead or some middle solution. |

## Members

### `GPlatesModel::FeatureVisitorInternals::Traits`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `feature_weak_ref_type` | typedef | `typename HandleTraits<FeatureHandle>::weak_ref` | public | — |
| `feature_iterator_type` | typedef | `typename HandleTraits<FeatureHandle>::iterator` | public | — |
| `feature_collection_iterator_type` | typedef | `typename HandleTraits<FeatureCollectionHandle>::iterator` | public | — |
| `top_level_property_inline_type` | typedef | `TopLevelPropertyInline` | public | — |
| `top_level_property_inline_iterator_type` | typedef | `TopLevelPropertyInline::iterator` | public | — |

### `GPlatesModel::FeatureVisitorInternals::Traits<const FeatureHandleType>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `feature_weak_ref_type` | typedef | `typename HandleTraits<FeatureHandle>::const_weak_ref` | public | — |
| `feature_iterator_type` | typedef | `typename HandleTraits<FeatureHandle>::const_iterator` | public | — |
| `feature_collection_iterator_type` | typedef | `typename HandleTraits<FeatureCollectionHandle>::const_iterator` | public | — |
| `top_level_property_inline_type` | typedef | `TopLevelPropertyInline` | public | — |
| `top_level_property_inline_iterator_type` | typedef | `TopLevelPropertyInline::const_iterator` | public | — |

### `GPlatesModel::FeatureVisitorBase`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `feature_handle_type` | typedef | `FeatureHandleType` | public | Convenience typedef for the template parameter, which is either const or non-const FeatureHandle. |
| `feature_weak_ref_type` | typedef | `typename FeatureVisitorInternals::Traits<feature_handle_type>::feature_weak_ref_type` | public | Convenience typedef for a weak-ref to a feature, with appropriate const-ness. |
| `feature_iterator_type` | typedef | `typename FeatureVisitorInternals::Traits<feature_handle_type>::feature_iterator_type` | public | Convenience typedef for a feature's children iterator, with appropriate const-ness. |
| `feature_collection_iterator_type` | typedef | `typename FeatureVisitorInternals::Traits<feature_handle_type>::feature_collection_iterator_type` | public | Convenience typedef for a feature collection's children iterator (which points to a feature), with appropriate const-ness. |
| `top_level_property_inline_type` | typedef | `typename FeatureVisitorInternals::Traits<feature_handle_type>::top_level_property_inline_type` | public | Convenience typedef for a feature's child type, with appropriate const-ness. |
| `top_level_property_inline_iterator_type` | typedef | `typename FeatureVisitorInternals::Traits<feature_handle_type>::top_level_property_inline_iterator_type` | public | Convenience typedef for a TopLevelProperty's iterator type, with appropriate const-ness. |
| `enumeration_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::Enumeration>::type` | public | Typedefs to give the property values appropriate const-ness. |
| `gml_data_block_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GmlDataBlock>::type` | public | — |
| `gml_file_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GmlFile>::type` | public | — |
| `gml_grid_envelope_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GmlGridEnvelope>::type` | public | — |
| `gml_line_string_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GmlLineString>::type` | public | — |
| `gml_multi_point_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GmlMultiPoint>::type` | public | — |
| `gml_orientable_curve_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GmlOrientableCurve>::type` | public | — |
| `gml_point_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GmlPoint>::type` | public | — |
| `gml_polygon_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GmlPolygon>::type` | public | — |
| `gml_rectified_grid_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GmlRectifiedGrid>::type` | public | — |
| `gml_time_instant_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GmlTimeInstant>::type` | public | — |
| `gml_time_period_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GmlTimePeriod>::type` | public | — |
| `gpml_age_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GpmlAge>::type` | public | — |
| `gpml_array_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GpmlArray>::type` | public | — |
| `gpml_constant_value_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GpmlConstantValue>::type` | public | — |
| `gpml_feature_reference_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GpmlFeatureReference>::type` | public | — |
| `gpml_feature_snapshot_reference_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GpmlFeatureSnapshotReference>::type` | public | — |
| `gpml_finite_rotation_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GpmlFiniteRotation>::type` | public | — |
| `gpml_finite_rotation_slerp_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GpmlFiniteRotationSlerp>::type` | public | — |
| `gpml_hot_spot_trail_mark_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GpmlHotSpotTrailMark>::type` | public | — |
| `gpml_irregular_sampling_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GpmlIrregularSampling>::type` | public | — |
| `gpml_key_value_dictionary_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GpmlKeyValueDictionary>::type` | public | — |
| `gpml_measure_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GpmlMeasure>::type` | public | — |
| `gpml_old_plates_header_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GpmlOldPlatesHeader>::type` | public | — |
| `gpml_piecewise_aggregation_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GpmlPiecewiseAggregation>::type` | public | — |
| `gpml_plate_id_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GpmlPlateId>::type` | public | — |
| `gpml_polarity_chron_id_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GpmlPolarityChronId>::type` | public | — |
| `gpml_property_delegate_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GpmlPropertyDelegate>::type` | public | — |
| `gpml_raster_band_names_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GpmlRasterBandNames>::type` | public | — |
| `gpml_revision_id_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GpmlRevisionId>::type` | public | — |
| `gpml_scalar_field_3d_file_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GpmlScalarField3DFile>::type` | public | — |
| `gpml_string_list_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GpmlStringList>::type` | public | — |
| `gpml_topological_network_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GpmlTopologicalNetwork>::type` | public | — |
| `gpml_topological_polygon_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GpmlTopologicalPolygon>::type` | public | — |
| `gpml_topological_line_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GpmlTopologicalLine>::type` | public | — |
| `gpml_topological_line_section_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GpmlTopologicalLineSection>::type` | public | — |
| `gpml_topological_point_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GpmlTopologicalPoint>::type` | public | — |
| `old_version_property_value_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::OldVersionPropertyValue>::type` | public | — |
| `uninterpreted_property_value_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::UninterpretedPropertyValue>::type` | public | — |
| `xs_boolean_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::XsBoolean>::type` | public | — |
| `xs_double_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::XsDouble>::type` | public | — |
| `xs_integer_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::XsInteger>::type` | public | — |
| `xs_string_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::XsString>::type` | public | — |
| `gpml_metadata_type` | typedef | `typename GPlatesUtils::CopyConst<feature_handle_type, GPlatesPropertyValues::GpmlMetadata>::type` | public | — |
| `~FeatureVisitorBase()` | destructor | `None` | public | Destructor. |
| `visit_feature( const feature_weak_ref_type &feature_weak_ref)` | method | `bool` | public | Visit the feature referenced by feature\_weak\_ref. |
| `visit_feature( const feature_collection_iterator_type &iterator)` | method | `bool` | public | Visit the feature indicated by iterator. |
| `visit_feature_handle( feature_handle_type &feature_handle)` | method | `void` | protected | Visit a feature handle. |
| `initialise_pre_feature_properties( feature_handle_type &feature_handle)` | method | `bool` | protected | Initialise the visitor before visiting the feature properties. |
| `finalise_post_feature_properties( feature_handle_type &feature_handle)` | method | `void` | protected | Finalise the visitor after visiting the feature properties. |
| `visit_feature_property( const feature_iterator_type &feature_iterator)` | method | `void` | protected | Invoke this function in visit\_feature\_properties to visit a feature properties. |
| `visit_feature_properties( feature_handle_type &feature_handle)` | method | `void` | protected | Invoke this function in visit\_feature\_handle to visit each of the the feature properties in turn. |
| `current_top_level_propiter` | field | `boost::optional<feature_iterator_type>` | protected | Access the iterator of the top-level property which we're currently visiting. |
| `current_top_level_propname` | field | `boost::optional<PropertyName>` | protected | Access the name of the top-level property which we're currently visiting. |
| `visit_top_level_property_inline( top_level_property_inline_type &top_level_property_inline)` | method | `void` | public | Visit the inline top-level properties of a feature. |
| `initialise_pre_property_values( top_level_property_inline_type &top_level_property_inline)` | method | `bool` | protected | Initialise the visitor before visiting the property values. |
| `finalise_post_property_values( top_level_property_inline_type &top_level_property_inline)` | method | `void` | protected | Finalise the visitor after visiting the property values. |
| `visit_property_values( top_level_property_inline_type &top_level_property_inline)` | method | `void` | protected | Invoke this function in visit\_top\_level\_property\_inline to visit each of the property-values in turn. |
| `visit_enumeration( enumeration_type &enumeration)` | method | `void` | public | Please keep these property-value types ordered alphabetically. |
| `visit_gml_data_block( gml_data_block_type &gml_data_block)` | method | `void` | public | — |
| `visit_gml_file( gml_file_type &gml_file)` | method | `void` | public | — |
| `visit_gml_grid_envelope( gml_grid_envelope_type &gml_grid_envelope)` | method | `void` | public | — |
| `visit_gml_line_string( gml_line_string_type &gml_line_string)` | method | `void` | public | — |
| `visit_gml_multi_point( gml_multi_point_type &gml_multi_point)` | method | `void` | public | — |
| `visit_gml_orientable_curve( gml_orientable_curve_type &gml_orientable_curve)` | method | `void` | public | — |
| `visit_gml_point( gml_point_type &gml_point)` | method | `void` | public | — |
| `visit_gml_polygon( gml_polygon_type &gml_polygon)` | method | `void` | public | — |
| `visit_gml_rectified_grid( gml_rectified_grid_type &gml_rectified_grid)` | method | `void` | public | — |
| `visit_gml_time_instant( gml_time_instant_type &gml_time_instant)` | method | `void` | public | — |
| `visit_gml_time_period( gml_time_period_type &gml_time_period)` | method | `void` | public | — |
| `visit_gpml_age( gpml_age_type &gpml_age)` | method | `void` | public | — |
| `visit_gpml_array( gpml_array_type &gpml_array)` | method | `void` | public | — |
| `visit_gpml_constant_value( gpml_constant_value_type &gpml_constant_value)` | method | `void` | public | — |
| `visit_gpml_feature_reference( gpml_feature_reference_type &gpml_feature_reference)` | method | `void` | public | — |
| `visit_gpml_feature_snapshot_reference( gpml_feature_snapshot_reference_type &gpml_feature_snapshot_reference)` | method | `void` | public | — |
| `visit_gpml_finite_rotation( gpml_finite_rotation_type &gpml_finite_rotation)` | method | `void` | public | — |
| `visit_gpml_finite_rotation_slerp( gpml_finite_rotation_slerp_type &gpml_finite_rotation_slerp)` | method | `void` | public | — |
| `visit_gpml_hot_spot_trail_mark( gpml_hot_spot_trail_mark_type &gpml_hot_spot_trail_mark)` | method | `void` | public | — |
| `visit_gpml_irregular_sampling( gpml_irregular_sampling_type &gpml_irregular_sampling)` | method | `void` | public | — |
| `visit_gpml_key_value_dictionary( gpml_key_value_dictionary_type &gpml_key_value_dictionary)` | method | `void` | public | — |
| `visit_gpml_measure( gpml_measure_type &gpml_measure)` | method | `void` | public | — |
| `visit_gpml_metadata( gpml_metadata_type &gpml_metadata)` | method | `void` | public | — |
| `visit_gpml_old_plates_header( gpml_old_plates_header_type &gpml_old_plates_header)` | method | `void` | public | — |
| `visit_gpml_piecewise_aggregation( gpml_piecewise_aggregation_type &gpml_piecewise_aggregation)` | method | `void` | public | — |
| `visit_gpml_plate_id( gpml_plate_id_type &gpml_plate_id)` | method | `void` | public | — |
| `visit_gpml_polarity_chron_id( gpml_polarity_chron_id_type &gpml_polarity_chron_id)` | method | `void` | public | — |
| `visit_gpml_property_delegate( gpml_property_delegate_type &gpml_property_delegate)` | method | `void` | public | — |
| `visit_gpml_raster_band_names( gpml_raster_band_names_type &gpml_raster_band_names)` | method | `void` | public | — |
| `visit_gpml_revision_id( gpml_revision_id_type &gpml_revision_id)` | method | `void` | public | — |
| `visit_gpml_scalar_field_3d_file( gpml_scalar_field_3d_file_type &gpml_scalar_field_3d_file)` | method | `void` | public | — |
| `visit_gpml_string_list( gpml_string_list_type &gpml_string_list)` | method | `void` | public | — |
| `visit_gpml_topological_network( gpml_topological_network_type &gpml_topological_network)` | method | `void` | public | — |
| `visit_gpml_topological_polygon( gpml_topological_polygon_type &gpml_topological_polygon)` | method | `void` | public | — |
| `visit_gpml_topological_line( gpml_topological_line_type &gpml_topological_line)` | method | `void` | public | — |
| `visit_gpml_topological_line_section( gpml_topological_line_section_type &gpml_topological_line_section)` | method | `void` | public | — |
| `visit_gpml_topological_point( gpml_topological_point_type &gpml_topological_point)` | method | `void` | public | — |
| `visit_old_version_property_value( old_version_property_value_type &old_version_prop_val)` | method | `void` | public | — |
| `visit_uninterpreted_property_value( uninterpreted_property_value_type &uninterpreted_prop_val)` | method | `void` | public | — |
| `visit_xs_boolean( xs_boolean_type &xs_boolean)` | method | `void` | public | — |
| `visit_xs_double( xs_double_type &xs_double)` | method | `void` | public | — |
| `visit_xs_integer( xs_integer_type &xs_integer)` | method | `void` | public | — |
| `visit_xs_string( xs_string_type &xs_string)` | method | `void` | public | — |
| `d_current_top_level_propiter` | field | `boost::optional<feature_iterator_type>` | private | Tracks the iterator of the most-recently read top-level property. |
| `d_current_top_level_propname` | field | `boost::optional<PropertyName>` | private | Tracks the name of the most-recently read top-level property. |
| `operator=` | field | `FeatureVisitorBase` | private | This operator should never be defined, because we don't want to allow copy-assignment. |

### `GPlatesModel::FeatureVisitor`

*None.*

### `GPlatesModel::ConstFeatureVisitor`

*None.*

### `GPlatesModel::FeatureVisitorThatGuaranteesNotToModify`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `visit_feature_property( const feature_iterator_type &feature_iterator)` | method | `void` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_FEATUREVISITOR_H` | macro | `None` | — |

## Notes

**References taken during a non-const `FeatureVisitor` visit dangle afterwards.**
The `visit_` methods receive a reference into the temporary clone, and once
`visit_feature_property` assigns that clone back into the feature, the model makes
its own copy and the clone is destroyed. Anything you stashed during visitation
points at freed memory by the time `visit_feature()` returns. `ConstFeatureVisitor`
does not have this problem — it visits the property in place — but its references
are still only as good as the feature's lifetime.

**A non-const visit is a model write even when nothing changes.** It bumps
revision IDs, sets the enclosing collection's unsaved-changes flag and emits
modification notifications for every property visited. Do not reach for
`FeatureVisitor` merely because you have a non-const handle.

**Adding a property-value type means editing this header in three places** — the
forward declaration, the `CopyConst` typedef, and the `visit_` member — and the
lists are maintained in alphabetical order by convention. Note that
`GpmlTopologicalInterior` is forward-declared here but has no `visit_` member; the
forward-declaration block and the member list are not automatically in step.

**A missing override is silent, and nesting is not traversed for you.** The
default `visit_` bodies are empty, so a visitor that forgets a type simply does
nothing for it. `PropertyValue::accept_visitor` only calls the one matching
`visit_` member — it does not descend — so a wrapper such as `GpmlConstantValue`
is a dead end unless your override calls
`gpml_constant_value.value()->accept_visitor(*this)` itself, as `GeometryFinder`
does. Since most geometry in real `.gpml` files is wrapped in a
`gpml:ConstantValue`, forgetting that one override is the classic way to write a
visitor that finds nothing.

**Validity is checked once, at entry.** `visit_feature()` tests the weak-ref or
the iterator and returns false if it is stale, but nothing revalidates during
traversal, so a visitor that mutates the feature it is walking — removing
properties, for instance — is outside what the traversal loop in
`visit_feature_properties` guarantees.

**`visit_top_level_property_inline` and all the `visit_` members are public
only** because `TopLevelProperty` and `PropertyValue` subclasses call them from
their `accept_visitor` implementations. They are not an invitation to drive the
visitor by hand.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/OgrFeatureCollectionWriter](../file-io/OgrFeatureCollectionWriter.md) | file-io | 554 |
| [file-io/OgrUtils](../file-io/OgrUtils.md) | file-io | 292 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 268 |
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 174 |
| [model/ModelUtils](ModelUtils.md) | model | 138 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 127 |
| [file-io/GMTFormatHeader](../file-io/GMTFormatHeader.md) | file-io | 119 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 113 |
| [app-logic/ExtractRasterFeatureProperties](../app-logic/ExtractRasterFeatureProperties.md) | app-logic | 94 |
| [qt-widgets/EditWidgetChooser](../qt-widgets/EditWidgetChooser.md) | qt-widgets | 92 |
| [file-io/OgrWriter](../file-io/OgrWriter.md) | file-io | 87 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 79 |
| [feature-visitors/ToQvariantConverter](../feature-visitors/ToQvariantConverter.md) | feature-visitors | 78 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 75 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 74 |
| [app-logic/deprecated/ReconstructedFeatureGeometryPopulator](../app-logic/deprecated/ReconstructedFeatureGeometryPopulator.md) | app-logic | 65 |
| [feature-visitors/PropertyValueFinder](../feature-visitors/PropertyValueFinder.md) | feature-visitors | 62 |
| [app-logic/ReconstructMethodHalfStageRotation](../app-logic/ReconstructMethodHalfStageRotation.md) | app-logic | 61 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 60 |
| [qt-widgets/EditWidgetGroupBox](../qt-widgets/EditWidgetGroupBox.md) | qt-widgets | 59 |

*... and 192 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/FeatureVisitor.h
python scripts/gpq.py def GPlatesModel::FeatureVisitorBase --body
python scripts/gpq.py uses FeatureVisitorBase --kind class
python scripts/gpq.py hier FeatureVisitorBase
```
