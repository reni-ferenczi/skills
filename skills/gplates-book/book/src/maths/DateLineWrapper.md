# DateLineWrapper

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 18 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/DateLineWrapper.h` | C++ | 1340 |
| `src/maths/DateLineWrapper.cc` | C++ | 3126 |

## Overview

[[[PROSE overview unit=maths/DateLineWrapper tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::DateLineWrapper`](#gplatesmathsdatelinewrapper) | class | [`GPlatesUtils::ReferenceCount<DateLineWrapper>`](../utils/ReferenceCount.md) | — | 0 | Clips polyline/polygon geometries to the dateline (at -180, or +180, degrees longitude) and wraps them to the opposite longitude so that they display correctly over a (-180,180) rectangular (lat/lon) projection. |

## Members

### `GPlatesMaths::DateLineWrapper`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<DateLineWrapper>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const DateLineWrapper>` | public | — |
| `lat_lon_points_seq_type` | typedef | `std::vector<LatLonPoint>` | public | Typedef for a sequence of lat/lon points. |
| `LatLonPolygon` | class | `None` | public | A wrapped lat/lon polygon. |
| `LatLonPolyline` | class | `None` | public | A wrapped lat/lon polyline. |
| `LatLonMultiPoint` | class | `None` | public | A wrapped lat/lon multi-point. |
| `create( const double &central_meridian = 0.0)` | method | `non_null_ptr_type` | public | Creates a DateLineWrapper object. |
| `wrap_polygon( const PolygonOnSphere::non_null_ptr_to_const_type &input_polygon, std::vector<LatLonPolygon> &wrapped_polygons, boost::optional<AngularExtent> tessellate_threshold = boost::none, bool group_interior_with_exterior_rings = true)` | method | `void` | public | Clips the specified \*polygon\* to the dateline. |
| `wrap_polyline( const PolylineOnSphere::non_null_ptr_to_const_type &input_polyline, std::vector<LatLonPolyline> &wrapped_polylines, boost::optional<AngularExtent> tessellate_threshold = boost::none)` | method | `void` | public | Clips the specified \*polyline\* to the dateline. |
| `wrap_multi_point( const MultiPointOnSphere::non_null_ptr_to_const_type &input_multipoint)` | method | `LatLonMultiPoint` | public | Wraps points in the specified \*multi-point\* to the range \[-180 + central\_meridian, central\_meridian + 180\]. |
| `wrap_point( const PointOnSphere &input_point)` | method | `LatLonPoint` | public | Wraps the specified \*point\* to the range \[-180 + central\_meridian, central\_meridian + 180\]. |
| `possibly_wraps( const PolylineOnSphere::non_null_ptr_to_const_type &input_polyline)` | method | `bool` | public | Returns true if the specified polyline can possibly intersect the (central meridian shifted) dateline arc. |
| `possibly_wraps( const PolygonOnSphere::non_null_ptr_to_const_type &input_polygon)` | method | `bool` | public | Returns true if the specified polygon can possibly intersect the (central meridian shifted) dateline arc. |
| `CentralMeridian` | struct | `None` | private | For non-zero central meridians we need to rotate geometries into a dateline reference frame for clipping/wrapping and then reverse the rotation when outputting wrapped geometries. |
| `LatLonLineGeometry` | class | `None` | private | A possibly tessellated sequence of points (for a polyline/polygon). |
| `VertexClassification` | enum | `None` | private | Classification of a vertex based on its position relative to the dateline. |
| `IntersectionType` | enum | `None` | private | The type of intersection when intersecting a line segment of a geometry with the dateline. |
| `Vertex` | struct | `None` | private | A vertex in the graph. |
| `vertex_list_type` | typedef | `GPlatesUtils::SmartNodeLinkedList<Vertex>` | private | Typedef for a double-linked list of vertices. |
| `vertex_node_pool_type` | typedef | `boost::object_pool<vertex_list_type::Node>` | private | Typedef for a pool allocator of vertex list nodes. |
| `IntersectionGraph` | class | `None` | private | A graph of a geometry potentially intersecting the dateline. |
| `d_central_meridian` | field | `boost::optional<CentralMeridian>` | private | Used to transform input geometries to the dateline reference frame (for wrapping) and back again. |
| `DateLineWrapper( double central_meridian)` | constructor | `None` | private | Constructor. |
| `output_input_polyline( std::vector<LatLonPolyline> &wrapped_polylines, const PolylineOnSphere::non_null_ptr_to_const_type &input_polyline, const boost::optional<AngularExtent> &tessellate_threshold)` | method | `void` | private | Output the input polyline (it is entirely off the dateline). |
| `output_input_polygon( std::vector<LatLonPolygon> &wrapped_polygons, const PolygonOnSphere::non_null_ptr_to_const_type &input_polygon, const boost::optional<AngularExtent> &tessellate_threshold)` | method | `void` | private | Output the input polygon (it is entirely off the dateline). |
| `output_polyline_if_entirely_on_dateline( std::vector<LatLonPolyline> &wrapped_polylines, const PolylineOnSphere::non_null_ptr_to_const_type &input_polyline, const IntersectionGraph &graph, const boost::optional<AngularExtent> &tessellate_threshold_degrees)` | method | `void` | private | Output the input polyline if it is entirely \*on\* the dateline. |
| `output_non_intersecting_polygon_rings( std::vector<LatLonPolygon> &wrapped_polygons, const PolygonOnSphere::non_null_ptr_to_const_type &input_polygon, const IntersectionGraph &graph, const boost::optional<AngularExtent> &tessellate_threshold_degrees, bool group_interior_with_exterior_rings)` | method | `void` | private | Output the rings of the input polygon that do not intersect the dateline (if any). |
| `output_input_line_geometry( const VertexIteratorType vertex_begin, const VertexIteratorType vertex_end, LatLonLineGeometry &output_line_geometry, boost::optional<unsigned int> polygon_ring_index, bool on_dateline_arc, const boost::optional<AngularExtent> &tessellate_threshold_degrees)` | method | `void` | private | Output the non-intersecting input vertices of a polyline, or polygon ring. |
| `intersects_dateline( BoundingSmallCircle geometry_bounding_small_circle)` | method | `bool` | private | Returns true if the specified bounding small circle intersects the dateline arc. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `NORTH_POLE` | variable | `UnitVector3D` | Normal to sphere at the north pole. |
| `SOUTH_POLE` | variable | `UnitVector3D` | Normal to sphere at the south pole. |
| `FRONT_HALF_SPACE_NORMAL` | variable | `UnitVector3D` | Normal to the plane of the dateline great circle arc going from south pole to north pole. |
| `DATELINE_HEMISPHERE_NORMAL` | variable | `UnitVector3D` | Normal to plane dividing globe into hemisphere that contains dateline in front of it. |
| `EPSILON_THICK_PLANE_COSINE` | variable | `double` | Base epsilon calculations off a cosine since that usually has the least accuracy for small angles. '1 - 1e-9' in cosine corresponds to a displacement of about 4.5e-5 \[=sin(acos(1 - 1e-9))\]. |
| `EPSILON_THICK_PLANE_SINE` | variable | `double` | At the dateline we use a dot product and compare near zero. cos(90-epsilon) = sin(epsilon) |
| `does_line_segment_on_dateline_plane_cross_north_pole( const GreatCircleArc &line_segment, bool is_line_segment_start_point_on_dateline)` | function | `bool` | Returns true if the specified line segment crosses north pole, otherwise it crosses south pole. @pre line segment must lie on the 'thick' plane containing the dateline \*and\* the line segment must cross one of the poles. |
| `shift_dateline_frame_lat_lon_point_to_central_meridian_range( const LatLonPoint &lat_lon_point, const double &central_meridian)` | function | `LatLonPoint` | Shift a lat/lon in the \*dateline frame\* to have a longitude in the range... \[-180 + central\_meridian, central\_meridian + 180\] |
| `make_lat_lon_point_in_central_meridian_range( const PointOnSphere &point_on_sphere, const double &central_meridian)` | function | `LatLonPoint` | Convert lat/lon with longitude in the range \[-180 + central\_meridian, central\_meridian + 180\]. |
| `make_lat_lon_point_on_back_dateline_of_central_meridian( const PointOnSphere &point_on_sphere, const double &central_meridian)` | function | `LatLonPoint` | Convert a point on the dateline arc to lat/lon with longitude of 'central\_meridian - 180'. |
| `LISTS_SENTINEL` | variable | `GPlatesMaths::DateLineWrapper::Vertex` | Note that the value doesn't matter - it's just used when constructing list sentinel nodes. |
| `GPLATES_MATHS_DATELINEWRAPPER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=maths/DateLineWrapper tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 140 |
| [file-io/OgrFeatureCollectionWriter](../file-io/OgrFeatureCollectionWriter.md) | file-io | 112 |
| [file-io/OgrWriter](../file-io/OgrWriter.md) | file-io | 90 |
| [file-io/OgrGeometryExporter](../file-io/OgrGeometryExporter.md) | file-io | 9 |
| [app-logic/ResolvedTriangulationUtils](../app-logic/ResolvedTriangulationUtils.md) | app-logic | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/DateLineWrapper.h
python scripts/gpq.py def GPlatesMaths::DateLineWrapper --body
python scripts/gpq.py uses DateLineWrapper --kind class
python scripts/gpq.py hier DateLineWrapper
```
