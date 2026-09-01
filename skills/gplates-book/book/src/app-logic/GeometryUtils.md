# GeometryUtils

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 231 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/GeometryUtils.h` | C++ | 442 |
| `src/app-logic/GeometryUtils.cc` | C++ | 1569 |

## Overview

[[[PROSE overview unit=app-logic/GeometryUtils tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::GetGeometryOnSphereType`](#anonymousgetgeometryonspheretype) | class | [`GPlatesMaths::ConstGeometryOnSphereVisitor`](../maths/ConstGeometryOnSphereVisitor.md) | — | 0 | Determines the geometry type of a derived GeometryOnSphere. |
| [`(anonymous)::GetNumGeometryOnSpherePoints`](#anonymousgetnumgeometryonspherepoints) | class | [`GPlatesMaths::ConstGeometryOnSphereVisitor`](../maths/ConstGeometryOnSphereVisitor.md) | — | 0 | Gets the number of points in a derived GeometryOnSphere. |
| [`(anonymous)::GetGeometryOnSpherePoints`](#anonymousgetgeometryonspherepoints) | class | [`GPlatesMaths::ConstGeometryOnSphereVisitor`](../maths/ConstGeometryOnSphereVisitor.md) | — | 0 | Retrieves points in a derived GeometryOnSphere. |
| [`(anonymous)::GetGeometryOnSphereExteriorEndPoints`](#anonymousgetgeometryonsphereexteriorendpoints) | class | [`GPlatesMaths::ConstGeometryOnSphereVisitor`](../maths/ConstGeometryOnSphereVisitor.md) | — | 0 | Retrieves the end points in a derived GeometryOnSphere. |
| [`(anonymous)::GetBoundingSmallCircle`](#anonymousgetboundingsmallcircle) | class | [`GPlatesMaths::ConstGeometryOnSphereVisitor`](../maths/ConstGeometryOnSphereVisitor.md) | — | 0 | Retrieves the bounding small circle of a derived GeometryOnSphere if appropriate for the type. |
| [`(anonymous)::ConvertGeometryToMultiPoint`](#anonymousconvertgeometrytomultipoint) | class | [`GPlatesMaths::ConstGeometryOnSphereVisitor`](../maths/ConstGeometryOnSphereVisitor.md) | — | 0 | Uses the points in a derived GeometryOnSphere object to create a multi-point. |
| [`(anonymous)::ConvertGeometryToPolyline`](#anonymousconvertgeometrytopolyline) | class | [`GPlatesMaths::ConstGeometryOnSphereVisitor`](../maths/ConstGeometryOnSphereVisitor.md) | — | 0 | Uses the points in a derived GeometryOnSphere object to create a polyline. |
| [`(anonymous)::ConvertGeometryToPolygon`](#anonymousconvertgeometrytopolygon) | class | [`GPlatesMaths::ConstGeometryOnSphereVisitor`](../maths/ConstGeometryOnSphereVisitor.md) | — | 0 | Uses the points in a derived GeometryOnSphere object to create a polygon. |
| [`(anonymous)::GetGeometryFromPropertyVisitor`](#anonymousgetgeometryfrompropertyvisitor) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Visits a property value to retrieve the geometry contained inside it. |
| [`(anonymous)::CreateGeometryProperty`](#anonymouscreategeometryproperty) | class | [`GPlatesMaths::ConstGeometryOnSphereVisitor`](../maths/ConstGeometryOnSphereVisitor.md) | — | 0 | Visits a GeometryOnSphere and creates a suitable property value for it. |

## Members

### `(anonymous)::GetGeometryOnSphereType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GetGeometryOnSphereType()` | constructor | `None` | public | — |
| `get_geometry_on_sphere_type()` | method | `GPlatesMaths::GeometryType::Value` | public | — |
| `visit_point_on_sphere( GPlatesMaths::PointGeometryOnSphere::non_null_ptr_to_const_type /*point_on_sphere*/)` | method | `void` | public | — |
| `visit_multi_point_on_sphere( GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type /*multi_point_on_sphere*/)` | method | `void` | public | — |
| `visit_polygon_on_sphere( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type /*polygon_on_sphere*/)` | method | `void` | public | — |
| `visit_polyline_on_sphere( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type /*polyline_on_sphere*/)` | method | `void` | public | — |
| `d_geometry_on_sphere_type` | field | `GPlatesMaths::GeometryType::Value` | private | — |

### `(anonymous)::GetNumGeometryOnSpherePoints`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GetNumGeometryOnSpherePoints( bool exterior_points_only)` | constructor | `None` | public | — |
| `get_num_geometry_points()` | method | `unsigned int` | public | — |
| `visit_point_on_sphere( GPlatesMaths::PointGeometryOnSphere::non_null_ptr_to_const_type point_on_sphere)` | method | `void` | public | — |
| `visit_multi_point_on_sphere( GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere)` | method | `void` | public | — |
| `visit_polygon_on_sphere( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere)` | method | `void` | public | — |
| `visit_polyline_on_sphere( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere)` | method | `void` | public | — |
| `d_exterior_points_only` | field | `bool` | private | — |
| `d_num_geometry_points` | field | `unsigned int` | private | — |

### `(anonymous)::GetGeometryOnSpherePoints`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GetGeometryOnSpherePoints( std::vector<GPlatesMaths::PointOnSphere> &points, boost::optional<const std::pair<unsigned int/*first*/, unsigned int/*second*/>&> range, bool reverse_points, bool exterior_points_only)` | constructor | `None` | public | Note that the optional range \[first, second) is a half-range where 'second' is one past the last vertex to be returned (this is similar to begin/end iterators). |
| `get_geometry_type()` | method | `GPlatesMaths::GeometryType::Value` | public | — |
| `visit_point_on_sphere( GPlatesMaths::PointGeometryOnSphere::non_null_ptr_to_const_type point_on_sphere)` | method | `void` | public | — |
| `visit_multi_point_on_sphere( GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere)` | method | `void` | public | — |
| `visit_polygon_on_sphere( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere)` | method | `void` | public | — |
| `visit_polyline_on_sphere( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere)` | method | `void` | public | — |
| `d_point_seq` | field | `std::vector<GPlatesMaths::PointOnSphere>` | private | Sequence of points to append to when visiting geometry on spheres. |
| `d_range` | field | `boost::optional<const std::pair<unsigned int, unsigned int>&>` | private | Optional indexed range of points to return. |
| `d_reverse_points` | field | `bool` | private | Whether to reverse the visiting geometry points before appending. |
| `d_exterior_points_only` | field | `bool` | private | Whether to only consider exterior ring points in polygons. |
| `d_geometry_type` | field | `GPlatesMaths::GeometryType::Value` | private | — |

### `(anonymous)::GetGeometryOnSphereExteriorEndPoints`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `get_geometry_exterior_end_points( const GPlatesMaths::GeometryOnSphere &geometry_on_sphere, bool reverse_points)` | method | `std::pair< GPlatesMaths::PointOnSphere/*start point*/, GPlatesMaths::PointOnSphere/*end point*/>` | public | Visits geometry\_on\_sphere and returns its start and end points. |
| `d_start_point` | field | `boost::optional<GPlatesMaths::PointOnSphere>` | private | Start point of visited geometry on sphere. |
| `d_end_point` | field | `boost::optional<GPlatesMaths::PointOnSphere>` | private | End point of visited geometry on sphere. |
| `d_reverse_points` | field | `bool` | private | Whether to reverse the visiting geometry end points before returning them. |
| `visit_point_on_sphere( GPlatesMaths::PointGeometryOnSphere::non_null_ptr_to_const_type point_on_sphere)` | method | `void` | private | — |
| `visit_multi_point_on_sphere( GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere)` | method | `void` | private | — |
| `visit_polygon_on_sphere( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere)` | method | `void` | private | — |
| `visit_polyline_on_sphere( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere)` | method | `void` | private | — |

### `(anonymous)::GetBoundingSmallCircle`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `visit_point_on_sphere( GPlatesMaths::PointGeometryOnSphere::non_null_ptr_to_const_type point_on_sphere)` | method | `void` | public | — |
| `visit_multi_point_on_sphere( GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere)` | method | `void` | public | — |
| `visit_polygon_on_sphere( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere)` | method | `void` | public | — |
| `visit_polyline_on_sphere( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere)` | method | `void` | public | — |
| `d_bounding_small_circle` | field | `boost::optional<const GPlatesMaths::BoundingSmallCircle &>` | private | — |

### `(anonymous)::ConvertGeometryToMultiPoint`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ConvertGeometryToMultiPoint( bool include_polygon_interior_ring_points)` | constructor | `None` | public | — |
| `get_multi_point()` | method | `GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type` | public | — |
| `visit_point_on_sphere( GPlatesMaths::PointGeometryOnSphere::non_null_ptr_to_const_type point_on_sphere)` | method | `void` | public | — |
| `visit_multi_point_on_sphere( GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere)` | method | `void` | public | — |
| `visit_polygon_on_sphere( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere)` | method | `void` | public | — |
| `visit_polyline_on_sphere( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere)` | method | `void` | public | — |
| `d_include_polygon_interior_ring_points` | field | `bool` | private | — |
| `d_multi_point` | field | `boost::optional<GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type>` | private | — |

### `(anonymous)::ConvertGeometryToPolyline`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ConvertGeometryToPolyline( bool exclude_polygons_with_interior_rings)` | constructor | `None` | public | — |
| `visit_point_on_sphere( GPlatesMaths::PointGeometryOnSphere::non_null_ptr_to_const_type point_on_sphere)` | method | `void` | public | — |
| `visit_multi_point_on_sphere( GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere)` | method | `void` | public | — |
| `visit_polygon_on_sphere( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere)` | method | `void` | public | — |
| `visit_polyline_on_sphere( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere)` | method | `void` | public | — |
| `d_exclude_polygons_with_interior_rings` | field | `bool` | private | — |
| `d_polyline` | field | `boost::optional<GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type>` | private | — |

### `(anonymous)::ConvertGeometryToPolygon`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `visit_point_on_sphere( GPlatesMaths::PointGeometryOnSphere::non_null_ptr_to_const_type point_on_sphere)` | method | `void` | public | — |
| `visit_multi_point_on_sphere( GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere)` | method | `void` | public | — |
| `visit_polygon_on_sphere( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere)` | method | `void` | public | — |
| `visit_polyline_on_sphere( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere)` | method | `void` | public | — |
| `d_polygon` | field | `boost::optional<GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type>` | private | — |

### `(anonymous)::GetGeometryFromPropertyVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `get_geometry_from_property( const GPlatesModel::FeatureHandle::iterator &property, const double &reconstruction_time)` | method | `boost::optional<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | public | — |
| `get_geometry_from_property( const GPlatesModel::TopLevelProperty::non_null_ptr_type &property, const double &reconstruction_time)` | method | `boost::optional<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | public | — |
| `get_geometry_from_property_value( const GPlatesModel::PropertyValue &property_value, const double &reconstruction_time)` | method | `boost::optional<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | public | — |
| `visit_gpml_constant_value( const gpml_constant_value_type &gpml_constant_value)` | method | `void` | private | — |
| `visit_gpml_piecewise_aggregation( const gpml_piecewise_aggregation_type &gpml_piecewise_aggregation)` | method | `void` | private | — |
| `visit_gml_line_string( const gml_line_string_type &gml_line_string)` | method | `void` | private | — |
| `visit_gml_multi_point( const gml_multi_point_type &gml_multi_point)` | method | `void` | private | — |
| `visit_gml_orientable_curve( const gml_orientable_curve_type &gml_orientable_curve)` | method | `void` | private | — |
| `visit_gml_point( const gml_point_type &gml_point)` | method | `void` | private | — |
| `visit_gml_polygon( const gml_polygon_type &gml_polygon)` | method | `void` | private | — |
| `d_reconstruction_time` | field | `boost::optional<GPlatesPropertyValues::GeoTimeInstant>` | private | — |
| `d_geometry` | field | `boost::optional<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | private | — |

### `(anonymous)::CreateGeometryProperty`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create_geometry_property( const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &geometry)` | method | `GPlatesModel::PropertyValue::non_null_ptr_type` | public | — |
| `visit_multi_point_on_sphere( GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere)` | method | `void` | protected | — |
| `visit_point_on_sphere( GPlatesMaths::PointGeometryOnSphere::non_null_ptr_to_const_type point_on_sphere)` | method | `void` | protected | — |
| `visit_polygon_on_sphere( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere)` | method | `void` | protected | — |
| `visit_polyline_on_sphere( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere)` | method | `void` | protected | — |
| `d_geometry_property` | field | `boost::optional<GPlatesModel::PropertyValue::non_null_ptr_type>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_GEOMETRY_UTILS_H` | macro | `None` | — |
| `get_point_on_sphere( const GPlatesMaths::GeometryOnSphere &geometry_on_sphere)` | function | `boost::optional<const GPlatesMaths::PointOnSphere &>` | Returns the specified geometry-on-sphere as a point-on-sphere. |
| `get_multi_point_on_sphere( const GPlatesMaths::GeometryOnSphere &geometry_on_sphere)` | function | `boost::optional<GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type>` | Returns the specified geometry-on-sphere as a multi-point-on-sphere. |
| `get_polyline_on_sphere( const GPlatesMaths::GeometryOnSphere &geometry_on_sphere)` | function | `boost::optional<GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type>` | Returns the specified geometry-on-sphere as a polyline-on-sphere. |
| `get_polygon_on_sphere( const GPlatesMaths::GeometryOnSphere &geometry_on_sphere)` | function | `boost::optional<GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type>` | Returns the specified geometry-on-sphere as a polygon-on-sphere. |
| `get_geometry_type( const GPlatesMaths::GeometryOnSphere &geometry_on_sphere)` | function | `GPlatesMaths::GeometryType::Value` | Returns the type of the specified GeometryOnSphere object. |
| `get_num_geometry_points( const GPlatesMaths::GeometryOnSphere &geometry_on_sphere)` | function | `unsigned int` | Returns the number of points in the specified geometry. |
| `get_num_geometry_exterior_points( const GPlatesMaths::GeometryOnSphere &geometry_on_sphere)` | function | `unsigned int` | Returns the number of points in the specified geometry. |
| `get_geometry_points( const GPlatesMaths::GeometryOnSphere &geometry_on_sphere, std::vector<GPlatesMaths::PointOnSphere> &points, bool reverse_points = false)` | function | `GPlatesMaths::GeometryType::Value` | Copies the PointOnSphere points from geometry\_on\_sphere to the points array. |
| `get_geometry_points_range( const GPlatesMaths::GeometryOnSphere &geometry_on_sphere, std::vector<GPlatesMaths::PointOnSphere> &points, unsigned int start_vertex_index, unsigned int end_vertex_index, bool reverse_points = false)` | function | `GPlatesMaths::GeometryType::Value` | Same as get\_geometry\_points except only the points in the specified range are returned. |
| `get_geometry_exterior_points( const GPlatesMaths::GeometryOnSphere &geometry_on_sphere, std::vector<GPlatesMaths::PointOnSphere> &points, bool reverse_points = false)` | function | `GPlatesMaths::GeometryType::Value` | Same as get\_geometry\_points except, if geometry\_on\_sphere is a polygon then only its \*exterior\* ring points are copied. |
| `get_geometry_exterior_points_range( const GPlatesMaths::GeometryOnSphere &geometry_on_sphere, std::vector<GPlatesMaths::PointOnSphere> &points, unsigned int start_vertex_index, unsigned int end_vertex_index, bool reverse_points = false)` | function | `GPlatesMaths::GeometryType::Value` | Same as get\_geometry\_exterior\_points except only the points in the specified range are returned. |
| `get_geometry_exterior_end_points( const GPlatesMaths::GeometryOnSphere &geometry_on_sphere, bool reverse_points = false)` | function | `std::pair< GPlatesMaths::PointOnSphere/*start point*/, GPlatesMaths::PointOnSphere/*end point*/>` | Returns the end points of geometry\_on\_sphere. |
| `get_geometry_bounding_small_circle( const GPlatesMaths::GeometryOnSphere &geometry_on_sphere)` | function | `boost::optional<const GPlatesMaths::BoundingSmallCircle &>` | Returns the small circle that bounds the specified geometry. |
| `convert_geometry_to_multi_point( const GPlatesMaths::GeometryOnSphere &geometry_on_sphere, bool include_polygon_interior_ring_points = true)` | function | `GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type` | Converts the specified geometry to a MultiPointOnSphere by treating storing the geometry points as a multi-point. |
| `convert_geometry_to_polyline( const GPlatesMaths::GeometryOnSphere &geometry_on_sphere, bool exclude_polygons_with_interior_rings = true)` | function | `boost::optional<GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type>` | Converts the specified geometry to a PolylineOnSphere if it is a polygon or multipoint (or already a polyline) by treating the geometry points as a linear list of polyline points. |
| `force_convert_geometry_to_polyline( const GPlatesMaths::GeometryOnSphere &geometry_on_sphere)` | function | `GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type` | Same as convert\_geometry\_to\_polyline except, if geometry has less than two points then duplicates last point, or if geometry is a polygon then only the exterior ring is converted to a polyline (the interior rings are ignored). |
| `convert_geometry_to_polygon( const GPlatesMaths::GeometryOnSphere &geometry_on_sphere)` | function | `boost::optional<GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type>` | Converts the specified geometry to a PolygonOnSphere if it is a polyline or multipoint (or already a polygon) by treating the geometry points as a linear list of polygon points. |
| `force_convert_geometry_to_polygon( const GPlatesMaths::GeometryOnSphere &geometry_on_sphere)` | function | `GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type` | Same as convert\_geometry\_to\_polygon except, if geometry has less than three points then, duplicates last point until has three points. |
| `convert_polygon_to_oriented_polygon( const GPlatesMaths::PolygonOnSphere &polygon_on_sphere, GPlatesMaths::PolygonOrientation::Orientation polygon_orientation, bool ensure_interior_ring_orientation_opposite_to_exterior_ring = true)` | function | `GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type` | Convert the polygon to the specified orientation (if necessary). |
| `convert_geometry_to_oriented_geometry( const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &geometry, GPlatesMaths::PolygonOrientation::Orientation polygon_orientation, bool ensure_interior_ring_orientation_opposite_to_exterior_ring = true)` | function | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | Converts geometry to the specified orientation if it's a polygon and has a different orientation, otherwise geometry is returned. |
| `get_geometry_from_property( const GPlatesModel::FeatureHandle::iterator &property, const double &reconstruction_time = 0)` | function | `boost::optional<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | Returns the geometry contained within the specified property. |
| `get_geometry_from_property( const GPlatesModel::TopLevelProperty::non_null_ptr_type &property, const double &reconstruction_time = 0)` | function | `boost::optional<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | Returns the geometry contained within the specified property. |
| `get_geometry_from_property_value( const GPlatesModel::PropertyValue &property_value, const double &reconstruction_time = 0)` | function | `boost::optional<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | Returns the geometry contained within the specified property value. |
| `create_geometry_property_value( const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &geometry)` | function | `GPlatesModel::PropertyValue::non_null_ptr_type` | Visits a geometry and attempts to create a suitable geometric PropertyValue using it. |
| `create_point_geometry_property_value( const GPlatesMaths::PointOnSphere &point)` | function | `GPlatesModel::PropertyValue::non_null_ptr_type` | Creates a suitable geometric PropertyValue using point. |
| `create_multipoint_geometry_property_value( const GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type &multipoint)` | function | `GPlatesModel::PropertyValue::non_null_ptr_type` | Creates a suitable geometric PropertyValue using multipoint. |
| `create_polyline_geometry_property_value( const GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type &polyline)` | function | `GPlatesModel::PropertyValue::non_null_ptr_type` | Creates a suitable geometric PropertyValue using polyline. |
| `create_polygon_geometry_property_value( const GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type &polygon)` | function | `GPlatesModel::PropertyValue::non_null_ptr_type` | Creates a suitable geometric PropertyValue using polygon. |
| `remove_geometry_properties_from_feature( const GPlatesModel::FeatureHandle::weak_ref &feature_ref)` | function | `void` | Removes any properties that contain geometry from feature\_ref. |
| `create_geometry_property_value( PointForwardIter begin, PointForwardIter end, GPlatesMaths::GeometryType::Value type)` | function | `boost::optional<GPlatesModel::PropertyValue::non_null_ptr_type>` | — |

## Notes

[[[PROSE notes unit=app-logic/GeometryUtils tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ResolvedSubSegmentRangeInSection](ResolvedSubSegmentRangeInSection.md) | app-logic | 46 |
| [app-logic/TopologyReconstruct](TopologyReconstruct.md) | app-logic | 28 |
| [app-logic/TopologyGeometryResolver](TopologyGeometryResolver.md) | app-logic | 24 |
| [app-logic/VelocityFieldCalculatorLayerProxy](VelocityFieldCalculatorLayerProxy.md) | app-logic | 23 |
| [file-io/CitcomsResolvedTopologicalBoundaryExport](../file-io/CitcomsResolvedTopologicalBoundaryExport.md) | file-io | 23 |
| [view-operations/VisibleReconstructionGeometryExport](../view-operations/VisibleReconstructionGeometryExport.md) | view-operations | 20 |
| [file-io/ResolvedTopologicalGeometryExport](../file-io/ResolvedTopologicalGeometryExport.md) | file-io | 19 |
| [file-io/GMTFormatResolvedTopologicalGeometryExport](../file-io/GMTFormatResolvedTopologicalGeometryExport.md) | file-io | 17 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 16 |
| [file-io/OgrFormatResolvedTopologicalGeometryExport](../file-io/OgrFormatResolvedTopologicalGeometryExport.md) | file-io | 15 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 15 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 13 |
| [view-operations/SplitFeatureUndoCommand](../view-operations/SplitFeatureUndoCommand.md) | view-operations | 13 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 12 |
| [opengl/GLReconstructedStaticPolygonMeshes](../opengl/GLReconstructedStaticPolygonMeshes.md) | opengl | 12 |
| [app-logic/MotionPathGeometryPopulator](MotionPathGeometryPopulator.md) | app-logic | 11 |
| [app-logic/PartitionFeatureUtils](PartitionFeatureUtils.md) | app-logic | 11 |
| [app-logic/TopologyIntersections](TopologyIntersections.md) | app-logic | 11 |
| [app-logic/ResolvedTriangulationNetwork](ResolvedTriangulationNetwork.md) | app-logic | 9 |
| [view-operations/RenderedGeometryUtils](../view-operations/RenderedGeometryUtils.md) | view-operations | 9 |

*... and 31 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/GeometryUtils.h
python scripts/gpq.py def (anonymous)::GetGeometryOnSpherePoints --body
python scripts/gpq.py uses GetGeometryOnSpherePoints --kind class
python scripts/gpq.py hier GetGeometryOnSpherePoints
```
