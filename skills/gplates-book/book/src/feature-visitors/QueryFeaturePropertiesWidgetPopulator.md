# QueryFeaturePropertiesWidgetPopulator

[Book TOC](../../TOC.md) · [feature-visitors](../../components/feature-visitors.md) · cluster Community 390 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/feature-visitors/QueryFeaturePropertiesWidgetPopulator.h` | C++ | 218 |
| `src/feature-visitors/QueryFeaturePropertiesWidgetPopulator.cc` | C++ | 727 |

## Overview

This visitor populates a `QTreeWidget` with the hierarchical properties of a feature, converting GPML data into a tree view for display in the GUI. It traverses all property types (geometries, times, rotations, measurements, strings) and formats them as human-readable tree items. A key optimization: if a focused geometry is provided (the geometry the user clicked on), only that geometry's subtree is expanded by default, avoiding performance issues when a feature has many geometries. The visitor is used by `QueryFeaturePropertiesWidget` to display feature details when the user queries them.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFeatureVisitors::QueryFeaturePropertiesWidgetPopulator`](#gplatesfeaturevisitorsqueryfeaturepropertieswidgetpopulator) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | — |

## Members

### `GPlatesFeatureVisitors::QueryFeaturePropertiesWidgetPopulator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `QueryFeaturePropertiesWidgetPopulator( QTreeWidget &tree_widget)` | constructor | `None` | public | — |
| `populate( GPlatesModel::FeatureHandle::const_weak_ref &feature, GPlatesAppLogic::ReconstructionGeometry::maybe_null_ptr_to_const_type focused_rg)` | method | `void` | public | Populates the tree widget passed into constructor with the properties of feature. focused\_rg is the clicked geometry, if any, and is the only geometry property that is expanded in the widget. |
| `initialise_pre_property_values( const GPlatesModel::TopLevelPropertyInline &top_level_property_inline)` | method | `bool` | private | — |
| `finalise_post_property_values( const GPlatesModel::TopLevelPropertyInline &top_level_property_inline)` | method | `void` | private | — |
| `visit_enumeration( const GPlatesPropertyValues::Enumeration &enumeration)` | method | `void` | private | — |
| `visit_gml_line_string( const GPlatesPropertyValues::GmlLineString &gml_line_string)` | method | `void` | private | — |
| `visit_gml_multi_point( const GPlatesPropertyValues::GmlMultiPoint &gml_multi_point)` | method | `void` | private | — |
| `visit_gml_orientable_curve( const GPlatesPropertyValues::GmlOrientableCurve &gml_orientable_curve)` | method | `void` | private | — |
| `visit_gml_point( const GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | private | — |
| `visit_gml_polygon( const GPlatesPropertyValues::GmlPolygon &gml_polygon)` | method | `void` | private | — |
| `visit_gml_time_instant( const GPlatesPropertyValues::GmlTimeInstant &gml_time_instant)` | method | `void` | private | — |
| `visit_gml_time_period( const GPlatesPropertyValues::GmlTimePeriod &gml_time_period)` | method | `void` | private | — |
| `visit_gpml_array( const GPlatesPropertyValues::GpmlArray &gpml_array)` | method | `void` | private | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | private | — |
| `visit_gpml_key_value_dictionary( const GPlatesPropertyValues::GpmlKeyValueDictionary &gpml_key_value_dictionary)` | method | `void` | private | — |
| `visit_gpml_measure( const GPlatesPropertyValues::GpmlMeasure &gpml_measure)` | method | `void` | private | — |
| `visit_gpml_plate_id( const GPlatesPropertyValues::GpmlPlateId &gpml_plate_id)` | method | `void` | private | — |
| `visit_gpml_old_plates_header( const GPlatesPropertyValues::GpmlOldPlatesHeader &gpml_old_plates_header)` | method | `void` | private | — |
| `visit_uninterpreted_property_value( const GPlatesPropertyValues::UninterpretedPropertyValue &uninterpreted_prop_val)` | method | `void` | private | — |
| `visit_gpml_string_list( const GPlatesPropertyValues::GpmlStringList &gpml_string_list)` | method | `void` | private | — |
| `visit_xs_boolean( const GPlatesPropertyValues::XsBoolean &xs_boolean)` | method | `void` | private | — |
| `visit_xs_double( const GPlatesPropertyValues::XsDouble &xs_double)` | method | `void` | private | — |
| `visit_xs_integer( const GPlatesPropertyValues::XsInteger& xs_integer)` | method | `void` | private | — |
| `visit_xs_string( const GPlatesPropertyValues::XsString &xs_string)` | method | `void` | private | — |
| `d_tree_widget_ptr` | field | `QTreeWidget` | private | — |
| `d_tree_widget_builder` | field | `GPlatesGui::TreeWidgetBuilder` | private | Used to build the QTreeWidget from QTreeWidgetItems. |
| `d_focused_geometry` | field | `boost::optional<GPlatesModel::FeatureHandle::const_iterator>` | private | The focused geometry if any. |
| `add_child_then_visit_value( const QString &name, const QString &value, const GPlatesModel::PropertyValue &property_value_to_visit)` | method | `void` | private | — |
| `add_gpml_key_value_dictionary_element( const GPlatesPropertyValues::GpmlKeyValueDictionaryElement &element)` | method | `void` | private | — |
| `write_polygon_ring( const GPlatesMaths::PolygonOnSphere::ring_vertex_const_iterator &ring_begin, const GPlatesMaths::PolygonOnSphere::ring_vertex_const_iterator &ring_end)` | method | `void` | private | — |
| `write_multipoint_member( const GPlatesMaths::PointOnSphere &point)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FEATUREVISITORS_QUERYFEATUREPROPERTIESWIDGETPOPULATOR_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/QueryFeaturePropertiesWidget](../qt-widgets/QueryFeaturePropertiesWidget.md) | qt-widgets | 5 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/feature-visitors/QueryFeaturePropertiesWidgetPopulator.h
python scripts/gpq.py def GPlatesFeatureVisitors::QueryFeaturePropertiesWidgetPopulator --body
python scripts/gpq.py uses QueryFeaturePropertiesWidgetPopulator --kind class
python scripts/gpq.py hier QueryFeaturePropertiesWidgetPopulator
```
