# MapRenderedGeometryLayerPainter

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 19 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/MapRenderedGeometryLayerPainter.h` | C++ | 606 |
| `src/gui/MapRenderedGeometryLayerPainter.cc` | C++ | 2934 |

## Overview

[[[PROSE overview unit=gui/MapRenderedGeometryLayerPainter tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::RefinedVertexColouredTriangle`](#anonymousrefinedvertexcolouredtriangle) | struct | — | — | 0 | Used when refining (subdividing) a filled triangle using vertex colouring (the vertex colours must also be interpolated). |
| [`GPlatesGui::MapRenderedGeometryLayerPainter`](#gplatesguimaprenderedgeometrylayerpainter) | class | [`GPlatesViewOperations::ConstRenderedGeometryCollectionVisitor< GPlatesPresentation::VisualLayers::rendered_geometry_layer_seq_type>`](../view-operations/RenderedGeometryCollectionVisitor.md)<br>`boost::noncopyable` | — | 0 | Handles drawing rendered geometries in a single layer by drawing the opaque primitives first followed by the transparent primitives. |

## Members

### `(anonymous)::RefinedVertexColouredTriangle`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RefinedVertexColouredTriangle( const GPlatesMaths::PointOnSphere &vertex_point0_, const GPlatesMaths::PointOnSphere &vertex_point1_, const GPlatesMaths::PointOnSphere &vertex_point2_, const GPlatesGui::Colour &vertex_colour0_, const GPlatesGui::Colour &vertex_colour1_, const GPlatesGui::Colour &vertex_colour2_, boost:: ...` | constructor | `None` | public | — |
| `vertex_points` | field | `boost::optional<GPlatesMaths::PointOnSphere>` | public | Using boost::optional since native array elements must be default constructible. |
| `vertex_lat_lon_points` | field | `boost::optional<GPlatesMaths::LatLonPoint>` | public | — |
| `vertex_colours` | field | `boost::optional<GPlatesGui::Colour>` | public | — |
| `edge_lengths` | field | `boost::optional<GPlatesMaths::AngularDistance>` | public | — |
| `set_edge_lengths()` | method | `void` | private | — |

### `GPlatesGui::MapRenderedGeometryLayerPainter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `cache_handle_type` | typedef | `boost::shared_ptr<void>` | public | Typedef for an opaque object that caches a particular painting. |
| `MapRenderedGeometryLayerPainter( const MapProjection::non_null_ptr_to_const_type &map_projection, const GPlatesViewOperations::RenderedGeometryLayer &rendered_geometry_layer, const GPlatesOpenGL::GLVisualLayers::non_null_ptr_type &gl_visual_layers, const double &inverse_viewport_zoom_factor, const double &device_indepe ...` | constructor | `None` | public | — |
| `paint( GPlatesOpenGL::GLRenderer &renderer, LayerPainter &layer_painter)` | method | `cache_handle_type` | public | Draws the sequence of rendered geometries passed into constructor. |
| `set_scale( float scale)` | method | `void` | public | — |
| `visit_rendered_arrowed_polyline( const GPlatesViewOperations::RenderedArrowedPolyline &rendered_arrowed_polyline)` | method | `void` | private | Please keep these geometries ordered alphabetically. |
| `visit_rendered_cross_symbol( const GPlatesViewOperations::RenderedCrossSymbol &rendered_cross_symbol)` | method | `void` | private | — |
| `visit_rendered_radial_arrow( const GPlatesViewOperations::RenderedRadialArrow &rendered_radial_arrow)` | method | `void` | private | — |
| `visit_rendered_tangential_arrow( const GPlatesViewOperations::RenderedTangentialArrow &rendered_tangential_arrow)` | method | `void` | private | — |
| `visit_rendered_ellipse( const GPlatesViewOperations::RenderedEllipse &rendered_ellipse)` | method | `void` | private | — |
| `visit_rendered_point_on_sphere( const GPlatesViewOperations::RenderedPointOnSphere &rendered_point_on_sphere)` | method | `void` | private | — |
| `visit_rendered_multi_point_on_sphere( const GPlatesViewOperations::RenderedMultiPointOnSphere &rendered_multi_point_on_sphere)` | method | `void` | private | — |
| `visit_rendered_coloured_multi_point_on_sphere( const GPlatesViewOperations::RenderedColouredMultiPointOnSphere &rendered_coloured_multi_point_on_sphere)` | method | `void` | private | — |
| `visit_rendered_polyline_on_sphere( const GPlatesViewOperations::RenderedPolylineOnSphere &rendered_polyline_on_sphere)` | method | `void` | private | — |
| `visit_rendered_coloured_polyline_on_sphere( const GPlatesViewOperations::RenderedColouredPolylineOnSphere &rendered_coloured_polyline_on_sphere)` | method | `void` | private | — |
| `visit_rendered_subduction_teeth_polyline( const GPlatesViewOperations::RenderedSubductionTeethPolyline &rendered_subduction_teeth_polyline)` | method | `void` | private | — |
| `visit_rendered_polygon_on_sphere( const GPlatesViewOperations::RenderedPolygonOnSphere &rendered_polygon_on_sphere)` | method | `void` | private | — |
| `visit_rendered_coloured_polygon_on_sphere( const GPlatesViewOperations::RenderedColouredPolygonOnSphere &rendered_coloured_polygon_on_sphere)` | method | `void` | private | — |
| `visit_rendered_coloured_edge_surface_mesh( const GPlatesViewOperations::RenderedColouredEdgeSurfaceMesh &rendered_coloured_edge_surface_mesh)` | method | `void` | private | — |
| `visit_rendered_coloured_triangle_surface_mesh( const GPlatesViewOperations::RenderedColouredTriangleSurfaceMesh &rendered_coloured_triangle_surface_mesh)` | method | `void` | private | — |
| `visit_rendered_resolved_raster( const GPlatesViewOperations::RenderedResolvedRaster &rendered_resolved_raster)` | method | `void` | private | — |
| `visit_rendered_small_circle( const GPlatesViewOperations::RenderedSmallCircle &rendered_small_circle)` | method | `void` | private | — |
| `visit_rendered_small_circle_arc( const GPlatesViewOperations::RenderedSmallCircleArc &rendered_small_circle_arc)` | method | `void` | private | — |
| `visit_rendered_square_symbol( const GPlatesViewOperations::RenderedSquareSymbol &rendered_square_symbol)` | method | `void` | private | — |
| `visit_rendered_circle_symbol( const GPlatesViewOperations::RenderedCircleSymbol &rendered_circle_symbol)` | method | `void` | private | — |
| `visit_rendered_string( const GPlatesViewOperations::RenderedString &rendered_string)` | method | `void` | private | — |
| `visit_rendered_triangle_symbol( const GPlatesViewOperations::RenderedTriangleSymbol &rendered_triangle_symbol)` | method | `void` | private | — |
| `DatelineWrappedProjectedLineGeometry` | class | `None` | private | Contains the results of dateline wrapping and map projecting a polyline or polygon. |
| `vertex_element_type` | typedef | `LayerPainter::vertex_element_type` | private | Typedef for a vertex element (index). |
| `coloured_vertex_type` | typedef | `LayerPainter::coloured_vertex_type` | private | Typedef for a coloured vertex. |
| `coloured_vertex_seq_type` | typedef | `LayerPainter::coloured_vertex_seq_type` | private | Typedef for a sequence of coloured vertices. |
| `vertex_element_seq_type` | typedef | `LayerPainter::vertex_element_seq_type` | private | Typedef for a sequence of vertex elements. |
| `stream_primitives_type` | typedef | `LayerPainter::stream_primitives_type` | private | Typedef for a primitives stream containing coloured vertices. |
| `d_map_projection` | field | `MapProjection::non_null_ptr_to_const_type` | private | Used to project vertices of rendered geometries to the map. |
| `d_rendered_geometry_layer` | field | `GPlatesViewOperations::RenderedGeometryLayer` | private | — |
| `d_gl_visual_layers` | field | `GPlatesOpenGL::GLVisualLayers::non_null_ptr_type` | private | Keeps track of OpenGL-related objects that persist from one render to the next. |
| `d_inverse_zoom_factor` | field | `double` | private | — |
| `d_device_independent_pixel_to_map_space_ratio` | field | `double` | private | The size of one device-independent pixel in (post projection) map space units. |
| `d_colour_scheme` | field | `ColourScheme::non_null_ptr_type` | private | For assigning colours to RenderedGeometry |
| `d_scale` | field | `float` | private | When rendering scaled maps that are meant to be a scaled version of another |
| `d_dateline_wrapper` | field | `GPlatesMaths::DateLineWrapper::non_null_ptr_type` | private | Wraps polylines/polygons to \[-180,180\] longitude about the central meridian of the map projection. |
| `d_layer_painter` | field | `boost::optional<LayerPainter &>` | private | Used to paint when the paint method is called. |
| `POINT_SIZE_ADJUSTMENT` | field | `float` | private | For hard-coded tweaking of the size of points |
| `LINE_WIDTH_ADJUSTMENT` | field | `float` | private | For hard-coded tweaking of the width of lines |
| `visit_rendered_geometries( GPlatesOpenGL::GLRenderer &renderer)` | method | `void` | private | Visit each rendered geometry in our sequence (or spatial partition). |
| `get_vector_geometry_colour( const ColourProxy &colour_proxy)` | method | `boost::optional<Colour>` | private | Determines the colour of vector geometries. |
| `dateline_wrap_and_project_line_geometry( DatelineWrappedProjectedLineGeometry &dateline_wrapped_projected_line_geometry, const GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type &polyline_on_sphere)` | method | `void` | private | Dateline wraps and map projects polylines. |
| `dateline_wrap_and_project_line_geometry( DatelineWrappedProjectedLineGeometry &dateline_wrapped_projected_line_geometry, const GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type &polygon_on_sphere)` | method | `void` | private | Dateline wraps and map projects polygons. |
| `project_and_tessellate_unwrapped_polyline( DatelineWrappedProjectedLineGeometry &dateline_wrapped_projected_line_geometry, const GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type &polyline_on_sphere)` | method | `void` | private | Project and tessellate great circle arcs of an \*unwrapped\* polyline. |
| `project_and_tessellate_unwrapped_polygon( DatelineWrappedProjectedLineGeometry &dateline_wrapped_projected_line_geometry, const GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type &polygon_on_sphere)` | method | `void` | private | Project and tessellate great circle arcs of an \*unwrapped\* polygon. |
| `project_and_tessellate_unwrapped_geometry_part( DatelineWrappedProjectedLineGeometry &dateline_wrapped_projected_line_geometry, const GreatCircleArcForwardIter &begin_arcs, const GreatCircleArcForwardIter &end_arcs, unsigned int geometry_part_index = 0/*default for polylines*/)` | method | `void` | private | Project and tessellate great circle arcs of an \*unwrapped\* polyline, or ring (part) of a polygon. |
| `project_tessellated_wrapped_polyline( DatelineWrappedProjectedLineGeometry &dateline_wrapped_projected_line_geometry, const GPlatesMaths::DateLineWrapper::LatLonPolyline &wrapped_polyline)` | method | `void` | private | Project and tessellate a \*wrapped\* polyline. |
| `project_tessellated_wrapped_polygon( DatelineWrappedProjectedLineGeometry &dateline_wrapped_projected_line_geometry, const GPlatesMaths::DateLineWrapper::LatLonPolygon &wrapped_polygon)` | method | `void` | private | Project and tessellate a \*wrapped\* polygon. |
| `project_tessellated_wrapped_ring( DatelineWrappedProjectedLineGeometry &dateline_wrapped_projected_line_geometry, const GPlatesMaths::DateLineWrapper::lat_lon_points_seq_type &lat_lon_points, const std::vector<GPlatesMaths::DateLineWrapper::LatLonPolygon::point_flags_type> &point_flags, const GPlatesMaths::DateLineWrap ...` | method | `void` | private | Project and tessellate a \*wrapped\* ring (part) of a polygon. |
| `paint_fill_geometry( GPlatesOpenGL::GLFilledPolygonsMapView::filled_drawables_type &filled_polygons, const typename LineGeometryType::non_null_ptr_to_const_type &line_geometry, rgba8_t rgba8_color)` | method | `void` | private | Paints a \*filled\* line geometry (polyline or polygon) as a filled polygon. |
| `paint_line_geometry( const typename LineGeometryType::non_null_ptr_to_const_type &line_geometry, rgba8_t rgba8_color, stream_primitives_type &lines_stream, boost::optional<double> arrow_head_size = boost::none)` | method | `void` | private | Paints a line geometry (polyline or polygon). |
| `paint_vertex_coloured_polyline( const GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type &polyline, const std::vector<Colour> &original_vertex_colours, stream_primitives_type &lines_stream)` | method | `void` | private | Paints a polyline with per-vertex colouring. |
| `paint_vertex_coloured_polygon( const GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type &polygon, const std::vector<Colour> &original_vertex_colours, stream_primitives_type &lines_stream)` | method | `void` | private | Paints a polygon with per-vertex colouring. |
| `paint_arrow_head( const QPointF &arrow_head_apex, const QPointF &arrow_head_direction, const double &arrowhead_size, rgba8_t rgba8_color)` | method | `void` | private | — |
| `get_projected_wrapped_position( const GPlatesMaths::LatLonPoint &lat_lon_point)` | method | `QPointF` | private | Returns the map projected screen coordinates of the specified point. |
| `get_projected_unwrapped_position( const GPlatesMaths::PointOnSphere &point_on_sphere)` | method | `QPointF` | private | Returns the map projected screen coordinates of the specified point. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GREAT_CIRCLE_ARC_ANGULAR_THRESHOLD` | variable | `double` | We will tessellate a great circle arc if the two endpoints are far enough apart. |
| `COSINE_GREAT_CIRCLE_ARC_ANGULAR_THRESHOLD` | variable | `double` | — |
| `GREAT_CIRCLE_ARC_ANGULAR_EXTENT_THRESHOLD` | variable | `GPlatesMaths::AngularExtent` | — |
| `SMALL_CIRCLE_ANGULAR_INCREMENT` | variable | `double` | We will tessellate a small circle (arc) to this angular resolution. |
| `ELLIPSE_ANGULAR_INCREMENT` | variable | `double` | We will tessellate ellipses to this angular resolution (angle between semi-major and semi-minor axes). |
| `LONGITUDE_RANGE_EPSILON` | variable | `double` | Make sure the longitude is within \[-180+EPSILON, 180-EPSILON\] around the central meridian longitude. |
| `LONGITUDE_RANGE_LOWER_LIMIT` | variable | `double` | Longitude range lower limit. |
| `LONGITUDE_RANGE_UPPER_LIMIT` | variable | `double` | Longitude range upper limit. |
| `TWO_PI` | variable | `double` | — |
| `GLOBE_TO_MAP_SCALE_FACTOR` | variable | `float` | Variables for drawing velocity arrows. |
| `MAX_ARROWED_POLYLINE_ARROWHEAD_SIZE` | variable | `double` | Max arrowhead size for arrowed polylines (in post-projection space). |
| `MAP_VELOCITY_SCALE_FACTOR` | variable | `float` | — |
| `ARROWHEAD_BASE_HEIGHT_RATIO` | variable | `double` | — |
| `SYMBOL_SCALE_FACTOR` | variable | `double` | Scale factor for symbols. |
| `FILLED_CIRCLE_SYMBOL_CORRECTION` | variable | `double` | ! |
| `display_vertex( const GPlatesMaths::PointOnSphere &point)` | function | `void` | — |
| `display_vertex( const GPlatesMaths::PointOnSphere &point, const GPlatesGui::MapProjection &projection)` | function | `void` | — |
| `tessellate_on_plane( GPlatesGui::LayerPainter::coloured_vertex_seq_type &seq, const QPointF &centre, const double &radius, const double &angular_increment, const GPlatesGui::rgba8_t &colour)` | function | `void` | ! tessellate\_on\_plane fills seq with vertices describing a circle on a plane. |
| `POINT_SIZE_ADJUSTMENT` | variable | `float` | — |
| `LINE_WIDTH_ADJUSTMENT` | variable | `float` | — |
| `GPLATES_GUI_MAPCANVASPAINTER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/MapRenderedGeometryLayerPainter tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/MapRenderedGeometryCollectionPainter](MapRenderedGeometryCollectionPainter.md) | gui | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/MapRenderedGeometryLayerPainter.h
python scripts/gpq.py def GPlatesGui::MapRenderedGeometryLayerPainter --body
python scripts/gpq.py uses MapRenderedGeometryLayerPainter --kind class
python scripts/gpq.py hier MapRenderedGeometryLayerPainter
```
