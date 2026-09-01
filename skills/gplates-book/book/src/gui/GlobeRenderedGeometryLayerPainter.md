# GlobeRenderedGeometryLayerPainter

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 62 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/GlobeRenderedGeometryLayerPainter.h` | C++ | 523 |
| `src/gui/GlobeRenderedGeometryLayerPainter.cc` | C++ | 2971 |

## Overview

[[[PROSE overview unit=gui/GlobeRenderedGeometryLayerPainter tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::GlobeRenderedGeometryLayerPainter`](#gplatesguigloberenderedgeometrylayerpainter) | class | [`GPlatesViewOperations::ConstRenderedGeometryVisitor`](../view-operations/RenderedGeometryVisitor.md)<br>`boost::noncopyable` | — | 0 | Handles drawing rendered geometries in a single rendered layer. |

## Members

### `GPlatesGui::GlobeRenderedGeometryLayerPainter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `cache_handle_type` | typedef | `boost::shared_ptr<void>` | public | Typedef for an opaque object that caches a particular painting. |
| `PaintRegionType` | enum | `None` | public | Determines whether to paint the globe surface or sub-surface. |
| `GlobeRenderedGeometryLayerPainter( const GPlatesViewOperations::RenderedGeometryLayer &rendered_geometry_layer, const double &inverse_viewport_zoom_factor, const double &device_independent_pixel_to_world_space_ratio, const GlobeVisibilityTester &visibility_tester, ColourScheme::non_null_ptr_type colour_scheme, PaintReg ...` | constructor | `None` | public | paint\_region specifies whether to draw surface or sub-surface rendered geometries in paint. vector\_geometries\_override\_colour is used to optionally override the colour of vector geometries on the surface (this is useful when rendering ... |
| `paint( GPlatesOpenGL::GLRenderer &renderer, LayerPainter &layer_painter)` | method | `cache_handle_type` | public | Draws rendered geometries on the globe surface or sub-surface depending on the PaintRegionType passed into constructor. |
| `set_scale( float scale)` | method | `void` | public | — |
| `visit_rendered_arrowed_polyline( const GPlatesViewOperations::RenderedArrowedPolyline &rendered_arrowed_polyline)` | method | `void` | private | — |
| `visit_rendered_strain_marker_symbol( const GPlatesViewOperations::RenderedStrainMarkerSymbol &)` | method | `void` | private | — |
| `visit_rendered_cross_symbol( const GPlatesViewOperations::RenderedCrossSymbol &)` | method | `void` | private | — |
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
| `visit_rendered_resolved_scalar_field_3d( const GPlatesViewOperations::RenderedResolvedScalarField3D &rendered_resolved_scalar_field)` | method | `void` | private | — |
| `visit_rendered_radial_arrow( const GPlatesViewOperations::RenderedRadialArrow &rendered_radial_arrow)` | method | `void` | private | — |
| `visit_rendered_tangential_arrow( const GPlatesViewOperations::RenderedTangentialArrow &rendered_tangential_arrow)` | method | `void` | private | — |
| `visit_rendered_small_circle( const GPlatesViewOperations::RenderedSmallCircle &rendered_small_circle)` | method | `void` | private | — |
| `visit_rendered_small_circle_arc( const GPlatesViewOperations::RenderedSmallCircleArc &rendered_small_circle_arc)` | method | `void` | private | — |
| `visit_rendered_square_symbol( const GPlatesViewOperations::RenderedSquareSymbol &rendered_square_symbol)` | method | `void` | private | — |
| `visit_rendered_circle_symbol( const GPlatesViewOperations::RenderedCircleSymbol &rendered_circle_symbol)` | method | `void` | private | — |
| `visit_rendered_string( const GPlatesViewOperations::RenderedString &rendered_string)` | method | `void` | private | — |
| `visit_rendered_triangle_symbol( const GPlatesViewOperations::RenderedTriangleSymbol &rendered_triangle_symbol)` | method | `void` | private | — |
| `vertex_element_type` | typedef | `LayerPainter::vertex_element_type` | private | Typedef for a vertex element (index). |
| `vertex_element_seq_type` | typedef | `LayerPainter::vertex_element_seq_type` | private | Typedef for a sequence of vertex elements. |
| `coloured_vertex_type` | typedef | `LayerPainter::coloured_vertex_type` | private | Typedefs related to LayerPainter::coloured\_vertex\_type. |
| `coloured_vertex_seq_type` | typedef | `LayerPainter::coloured_vertex_seq_type` | private | — |
| `stream_primitives_type` | typedef | `LayerPainter::stream_primitives_type` | private | — |
| `axially_symmetric_mesh_vertex_type` | typedef | `LayerPainter::AxiallySymmetricMeshVertex` | private | Typedefs related to LayerPainter::AxiallySymmetricMeshVertex. |
| `axially_symmetric_mesh_vertex_seq_type` | typedef | `LayerPainter::axially_symmetric_mesh_vertex_seq_type` | private | — |
| `axially_symmetric_mesh_stream_primitives_type` | typedef | `LayerPainter::axially_symmetric_mesh_stream_primitives_type` | private | — |
| `rendered_geometries_spatial_partition_type` | typedef | `GPlatesViewOperations::RenderedGeometryLayer::rendered_geometries_spatial_partition_type` | private | Typedef for a rendered geometries spatial partition. |
| `cube_subdivision_cache_type` | typedef | `GPlatesOpenGL::GLCubeSubdivisionCache< false/*CacheProjectionTransform*/, false/*CacheLooseProjectionTransform*/, false/*CacheFrusum*/, false/*CacheLooseFrustum*/, false/*CacheBoun ...` | private | Typedef for a GLCubeSubvision cache that caches loose bounds. |
| `RenderedGeometryInfo` | struct | `None` | private | Information associated with a rendered geometry. |
| `RenderedGeometryOrder` | struct | `None` | private | Helper structure to sort rendered geometries in their render order. |
| `d_rendered_geometry_layer` | field | `GPlatesViewOperations::RenderedGeometryLayer` | private | — |
| `d_inverse_zoom_factor` | field | `double` | private | — |
| `d_device_independent_pixel_to_world_space_ratio` | field | `double` | private | The size of one device-independent pixel in world space units. |
| `d_visibility_tester` | field | `GlobeVisibilityTester` | private | For determining whether a particular point on the globe is visible or not |
| `d_colour_scheme` | field | `ColourScheme::non_null_ptr_type` | private | For assigning colours to RenderedGeometry |
| `d_scale` | field | `float` | private | When rendering scaled globes that are meant to be a scaled version of another |
| `d_paint_region` | field | `PaintRegionType` | private | Whether to render the globe surface or sub-surface. |
| `d_layer_painter` | field | `boost::optional<LayerPainter &>` | private | Used to paint when the paint method is called. |
| `d_frustum_planes` | field | `boost::optional<GPlatesOpenGL::GLFrustum>` | private | Used for frustum culling when the paint method is called. |
| `d_vector_geometries_override_colour` | field | `boost::optional<Colour>` | private | Optional override colour of vector geometries (useful when rendering geometries gray on rear of globe). |
| `d_surface_occlusion_texture` | field | `boost::optional<GPlatesOpenGL::GLTexture::shared_ptr_to_const_type>` | private | A viewport-size 2D texture containing the RGBA rendering of the surface geometries/rasters on the \*front\* of the globe. |
| `d_improve_performance_reduce_quality_hint` | field | `bool` | private | A hint to improve performance presumably at the cost of quality. |
| `d_current_spatial_partition_location` | field | `boost::optional<const rendered_geometries_spatial_partition_type::location_type &>` | private | Location in cube quad tree (spatial partition) when traversing a rendered geometries spatial partition. |
| `POINT_SIZE_ADJUSTMENT` | field | `float` | private | Multiplying factor to get point size of 1.0f to look like one screen-space pixel. |
| `LINE_WIDTH_ADJUSTMENT` | field | `float` | private | Multiplying factor to get line width of 1.0f to look like one screen-space pixel. |
| `visit_rendered_geometries( GPlatesOpenGL::GLRenderer &renderer)` | method | `void` | private | Visit each rendered geometry in our sequence (or spatial partition). |
| `get_visible_rendered_geometries( GPlatesOpenGL::GLRenderer &renderer, std::vector<RenderedGeometryInfo> &rendered_geometry_infos, std::vector<RenderedGeometryOrder> &rendered_geometry_orders, const rendered_geometries_spatial_partition_type &rendered_geometries_spatial_partition)` | method | `void` | private | — |
| `get_visible_rendered_geometries_from_spatial_partition_quad_tree( std::vector<RenderedGeometryInfo> &rendered_geometry_infos, std::vector<RenderedGeometryOrder> &rendered_geometry_orders, const GPlatesMaths::CubeQuadTreeLocation &cube_quad_tree_node_location, rendered_geometries_spatial_partition_type::const_node_refer ...` | method | `void` | private | — |
| `get_vector_geometry_colour( const ColourProxy &colour_proxy)` | method | `boost::optional<Colour>` | private | Determines the colour of vector geometries. |
| `paint_great_circle_arcs( GreatCircleArcForwardIter begin_arcs, GreatCircleArcForwardIter end_arcs, rgba8_t rgba8_color, stream_primitives_type &lines_stream)` | method | `void` | private | Paints great circle arcs of polylines and polygons. |
| `paint_vertex_coloured_great_circle_arcs( GreatCircleArcForwardIter begin_arcs, GreatCircleArcForwardIter end_arcs, VertexColourForwardIter begin_vertex_colours, VertexColourForwardIter end_vertex_colours, stream_primitives_type &lines_stream)` | method | `void` | private | Paints great circle arcs of polylines and polygons with per-vertex colouring. |
| `paint_ellipse( const GPlatesViewOperations::RenderedEllipse &rendered_ellipse, rgba8_t rgba8_color, stream_primitives_type &lines_stream)` | method | `void` | private | Paints an ellipse. |
| `paint_arrow( const GPlatesMaths::Vector3D &start, const GPlatesMaths::Vector3D &end, const GPlatesMaths::UnitVector3D &arrowline_unit_vector, const GPlatesMaths::real_t &arrowline_width, const GPlatesMaths::real_t &arrowhead_size, rgba8_t rgba8_color, axially_symmetric_mesh_stream_primitives_type &triangles_stream)` | method | `void` | private | Paints an arrow (straight line, not curved over globe) as a 3D arrow. |
| `paint_arrow_head_3D( const GPlatesMaths::Vector3D &apex, const GPlatesMaths::UnitVector3D &cone_x_axis, const GPlatesMaths::UnitVector3D &cone_y_axis, const GPlatesMaths::UnitVector3D &cone_z_axis, const GPlatesMaths::real_t &cone_axis_mag, rgba8_t rgba8_color, axially_symmetric_mesh_stream_primitives_type &triangles_s ...` | method | `void` | private | Paints a 3D cone for an arrow head. |
| `paint_arrow_head_2D( const GPlatesMaths::UnitVector3D &apex, const GPlatesMaths::UnitVector3D &direction, const GPlatesMaths::real_t &size, rgba8_t rgba8_color, stream_primitives_type &triangles_stream)` | method | `void` | private | Paints a flat triangle tangential to the globe for an arrow head. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GREAT_CIRCLE_ARC_ANGULAR_THRESHOLD` | variable | `double` | We will tessellate a great circle arc if the two endpoints are far enough apart. |
| `COSINE_GREAT_CIRCLE_ARC_ANGULAR_THRESHOLD` | variable | `double` | — |
| `SMALL_CIRCLE_ANGULAR_INCREMENT` | variable | `double` | We will tessellate a small circle (arc) to this angular resolution. |
| `TWO_PI` | variable | `double` | — |
| `MAX_ARROWED_POLYLINE_ARROWHEAD_SIZE` | variable | `double` | Max arrowhead size for arrowed polylines (in world space). |
| `ARROWHEAD_BASE_HEIGHT_RATIO` | variable | `double` | — |
| `COSINE_ARROWHEAD_BASE_HEIGHT_RATIO` | variable | `double` | — |
| `SINE_ARROWHEAD_BASE_HEIGHT_RATIO` | variable | `double` | — |
| `SYMBOL_SCALE_FACTOR` | variable | `double` | ! |
| `FILLED_CIRCLE_SYMBOL_CORRECTION` | variable | `double` | ! |
| `POINT_SIZE_ADJUSTMENT` | variable | `float` | — |
| `LINE_WIDTH_ADJUSTMENT` | variable | `float` | — |
| `GPLATES_GUI_GLOBERENDEREDGEOMETRYLAYERPAINTER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/GlobeRenderedGeometryLayerPainter tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/GlobeRenderedGeometryCollectionPainter](GlobeRenderedGeometryCollectionPainter.md) | gui | 14 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/GlobeRenderedGeometryLayerPainter.h
python scripts/gpq.py def GPlatesGui::GlobeRenderedGeometryLayerPainter --body
python scripts/gpq.py uses GlobeRenderedGeometryLayerPainter --kind class
python scripts/gpq.py hier GlobeRenderedGeometryLayerPainter
```
