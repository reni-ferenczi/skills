# ViewFeatureGeometriesWidgetPopulator

[Book TOC](../../TOC.md) · [feature-visitors](../../components/feature-visitors.md) · cluster Community 360 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/feature-visitors/ViewFeatureGeometriesWidgetPopulator.h` | C++ | 232 |
| `src/feature-visitors/ViewFeatureGeometriesWidgetPopulator.cc` | C++ | 786 |

## Overview

[[[PROSE overview unit=feature-visitors/ViewFeatureGeometriesWidgetPopulator tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::CoordinatePeriods::CoordinatePeriod`](#anonymouscoordinateperiodscoordinateperiod) | enum | — | — | 0 | — |
| [`(anonymous)::item_handle_seq_type`](#anonymousitem_handle_seq_type) | typedef | — | — | 0 | A sequence of item handles used in the TreeWidgetBuilder interface. |
| [`GPlatesFeatureVisitors::ViewFeatureGeometriesWidgetPopulator`](#gplatesfeaturevisitorsviewfeaturegeometrieswidgetpopulator) | class | [`GPlatesModel::FeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | — |

## Members

### `(anonymous)::CoordinatePeriods::CoordinatePeriod`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PRESENT` | enumerator | `None` | — | — |
| `RECONSTRUCTED` | enumerator | `None` | — | — |

### `(anonymous)::item_handle_seq_type`

*None.*

### `GPlatesFeatureVisitors::ViewFeatureGeometriesWidgetPopulator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ViewFeatureGeometriesWidgetPopulator( const GPlatesAppLogic::Reconstruction &reconstruction, QTreeWidget &tree_widget)` | constructor | `None` | public | — |
| `populate( GPlatesModel::FeatureHandle::weak_ref &feature, GPlatesAppLogic::ReconstructionGeometry::maybe_null_ptr_to_const_type focused_rg)` | method | `void` | public | Populates the tree widget passed into constructor with the properties of feature\_handle. focused\_rg is the clicked geometry, if any, and is the only geometry property that is expanded in the widget. |
| `initialise_pre_feature_properties( GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | private | — |
| `finalise_post_feature_properties( GPlatesModel::FeatureHandle &feature_handle)` | method | `void` | private | — |
| `initialise_pre_property_values( GPlatesModel::TopLevelPropertyInline &top_level_property_inline)` | method | `bool` | private | — |
| `finalise_post_property_values( GPlatesModel::TopLevelPropertyInline &top_level_property_inline)` | method | `void` | private | — |
| `visit_gml_line_string( GPlatesPropertyValues::GmlLineString &gml_line_string)` | method | `void` | private | — |
| `visit_gml_multi_point( GPlatesPropertyValues::GmlMultiPoint &gml_multi_point)` | method | `void` | private | — |
| `visit_gml_orientable_curve( GPlatesPropertyValues::GmlOrientableCurve &gml_orientable_curve)` | method | `void` | private | — |
| `visit_gml_point( GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | private | — |
| `visit_gml_polygon( GPlatesPropertyValues::GmlPolygon &gml_polygon)` | method | `void` | private | — |
| `visit_gpml_constant_value( GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | private | — |
| `PropertyInfo` | struct | `None` | private | Records details about the top-level items (properties) that we are building. |
| `property_info_vector_type` | typedef | `std::vector<PropertyInfo>` | private | — |
| `property_info_vector_const_iterator` | typedef | `property_info_vector_type::const_iterator` | private | — |
| `ReconstructedGeometryInfo` | struct | `None` | private | Stores the reconstructed geometry and the property it belongs to. |
| `geometries_for_property_type` | typedef | `std::vector<ReconstructedGeometryInfo>` | private | — |
| `geometries_for_property_const_iterator` | typedef | `geometries_for_property_type::const_iterator` | private | — |
| `d_reconstruction_ptr` | field | `GPlatesAppLogic::Reconstruction` | private | The Reconstruction which we will scan for RFGs from. |
| `d_tree_widget_ptr` | field | `QTreeWidget` | private | The tree widget we are populating. |
| `d_tree_widget_builder` | field | `GPlatesGui::TreeWidgetBuilder` | private | Used to build the QTreeWidget from QTreeWidgetItems. |
| `d_focused_geometry` | field | `boost::optional<GPlatesModel::FeatureHandle::iterator>` | private | The focused geometry if any. |
| `d_property_info_vector` | field | `property_info_vector_type` | private | Records details about the top-level items (properties) that we are building. |
| `d_rfg_geometries` | field | `geometries_for_property_type` | private | Stores the reconstructed geometries and the properties they belong to. |
| `populate_rfg_geometries_for_feature( GPlatesModel::FeatureHandle &feature_handle)` | method | `void` | private | Iterates over d\_reconstruction\_ptr's RFGs, fills in the d\_rfg\_geometries table with geometry found from RFGs which belong to the given feature. |
| `get_reconstructed_geometry_for_property( const GPlatesModel::FeatureHandle::iterator property)` | method | `boost::optional<const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | private | Searches the d\_rfg\_geometries table for geometry matching the given property. |
| `add_child_then_visit_value( const QString &name, const QString &value, GPlatesModel::PropertyValue &property_value_to_visit)` | method | `void` | private | — |
| `write_polygon_ring( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type polygon, boost::optional<unsigned int> interior_ring_index = boost::none)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `make_top_level_item_for_property( GPlatesGui::TreeWidgetBuilder &tree_widget_builder, const GPlatesModel::PropertyName &name)` | function | `GPlatesGui::TreeWidgetBuilder::item_handle_type` | Create a top-level QTreeWidgetItem but don't add as a top-level item yet. |
| `fill_coordinates_with_blank_items( GPlatesGui::TreeWidgetBuilder &tree_widget_builder, item_handle_seq_type &coordinate_widgets, unsigned int new_size)` | function | `void` | Ensures the given coordinate\_widgets list has a minimum number of blank QTreeWidgetItems suitable for populating with coordinates. |
| `populate_coordinates_from_polygon_ring( GPlatesGui::TreeWidgetBuilder &tree_widget_builder, item_handle_seq_type &coordinate_widgets, const GPlatesMaths::PolygonOnSphere::ring_vertex_const_iterator &ring_begin, const GPlatesMaths::PolygonOnSphere::ring_vertex_const_iterator &ring_end, CoordinatePeriods::CoordinatePerio ...` | function | `void` | Iterates over the vertices of the polygon ring, setting the coordinates in the column of each QTreeWidget corresponding to 'period'. |
| `populate_coordinates_from_multi_point( GPlatesGui::TreeWidgetBuilder &tree_widget_builder, item_handle_seq_type &coordinate_widgets, GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multi_point, CoordinatePeriods::CoordinatePeriod period)` | function | `void` | Iterates over the vertices of the multipoint, setting the coordinates in the column of each QTreeWidget corresponding to 'period'. |
| `populate_coordinates_from_polyline( GPlatesGui::TreeWidgetBuilder &tree_widget_builder, item_handle_seq_type &coordinate_widgets, GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline, CoordinatePeriods::CoordinatePeriod period)` | function | `void` | Iterates over the vertices of the polyline, setting the coordinates in the column of each QTreeWidget corresponding to 'period'. |
| `populate_coordinates_from_point( GPlatesGui::TreeWidgetBuilder &tree_widget_builder, item_handle_seq_type &coordinate_widgets, const GPlatesMaths::PointOnSphere &point_on_sphere, CoordinatePeriods::CoordinatePeriod period)` | function | `void` | Iterates over the vertices of the point, setting the coordinates in the column of each QTreeWidget corresponding to 'period'. |
| `GPLATES_FEATUREVISITORS_VIEWFEATUREGEOMETRIESWIDGETPOPULATOR_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=feature-visitors/ViewFeatureGeometriesWidgetPopulator tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ViewFeatureGeometriesWidget](../qt-widgets/ViewFeatureGeometriesWidget.md) | qt-widgets | 7 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/feature-visitors/ViewFeatureGeometriesWidgetPopulator.h
python scripts/gpq.py def GPlatesFeatureVisitors::ViewFeatureGeometriesWidgetPopulator --body
python scripts/gpq.py uses ViewFeatureGeometriesWidgetPopulator --kind class
python scripts/gpq.py hier ViewFeatureGeometriesWidgetPopulator
```
