# RenderedGeometryFactory

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 41 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedGeometryFactory.h` | C++ | 561 |
| `src/view-operations/RenderedGeometryFactory.cc` | C++ | 781 |

## Overview

`RenderedGeometry` is a pimpl: a `boost::intrusive_ptr<RenderedGeometryImpl>` and
nothing else, with no public way to reach the implementation except by visiting it
with a `ConstRenderedGeometryVisitor`. The concrete implementation classes —
`RenderedPointOnSphere`, `RenderedPolygonOnSphere`, `RenderedTangentialArrow`,
`RenderedResolvedRaster`, `RenderedSubductionTeethPolyline` and the rest — are
therefore not part of anyone's interface. This namespace of free functions is the
one place that names them. Producers say what they want drawn and get an opaque
handle back; the globe and map painters recover the type by double dispatch. Add a
new kind of drawable and you touch exactly three places: a new
`RenderedGeometryImpl` subclass, a `create_rendered_*` function here, and a new
visit method on the visitor interface — never any of the producers.

Two anonymous `ConstGeometryOnSphereVisitor` subclasses in the `.cc` cover the
common case where the caller holds a `GPlatesMaths::GeometryOnSphere` and does not
know its derived type; `create_rendered_geometry_on_sphere` and
`create_rendered_coloured_geometry_on_sphere` run one of them and forward to the
type-specific function. That is why those two take both a point size and a line
width hint — only one will end up being used, and the caller cannot tell which.
Colour is taken as a `GPlatesGui::ColourProxy` rather than a
`GPlatesGui::Colour` throughout, so a rendered geometry created from
reconstruction output can carry an unresolved colour that the active
`ColourScheme` supplies at paint time, while UI decorations pass a fixed colour
through the implicit conversion.

Sizes are hints, not measurements: `DEFAULT_POINT_SIZE_HINT` and
`DEFAULT_LINE_WIDTH_HINT` are deliberately the integer 1 — roughly one
device-independent pixel — and anything that needs to look bigger is expected to
scale that in its painter, not to pass a large number here. The arrow and
subduction-teeth parameters are view-dependent scalars expressed either as a
fraction of globe radius when the globe fills the viewport, or in
device-independent pixels; in both cases the painters keep the *projected* size
constant across zoom. `create_rendered_reconstruction_geometry` and
`create_rendered_multi_reconstruction_geometry` are the odd ones out: they are
decorators that wrap an already-built `RenderedGeometry` together with the
`GPlatesAppLogic::ReconstructionGeometry` it came from, which is how a proximity
hit on the canvas is traced back to the app-logic object behind it and how feature
focus works at all. `GPlatesPresentation::ReconstructionGeometryRenderer` is the
heaviest client, converting each frame's reconstruction output into rendered
geometries.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedGeometryFactory::(anonymous)::CreateRenderedGeometryFromGeometryOnSphere`](#gplatesviewoperationsrenderedgeometryfactoryanonymouscreaterenderedgeometryfromgeometryonsphere) | class | [`GPlatesMaths::ConstGeometryOnSphereVisitor`](../maths/ConstGeometryOnSphereVisitor.md) | — | 0 | Determines derived type of a GeometryOnSphere and creates a RenderedGeometry from it. |
| [`GPlatesViewOperations::RenderedGeometryFactory::(anonymous)::CreateRenderedGeometryFromColouredGeometryOnSphere`](#gplatesviewoperationsrenderedgeometryfactoryanonymouscreaterenderedgeometryfromcolouredgeometryonsphere) | class | [`GPlatesMaths::ConstGeometryOnSphereVisitor`](../maths/ConstGeometryOnSphereVisitor.md) | — | 0 | Determines derived type of a GeometryOnSphere and creates a RenderedGeometry from it. |
| [`GPlatesViewOperations::RenderedGeometryFactory::rendered_geometry_seq_type`](#gplatesviewoperationsrenderedgeometryfactoryrendered_geometry_seq_type) | typedef | — | — | 0 | Typedef for sequence of RenderedGeometry objects. |

## Members

### `GPlatesViewOperations::RenderedGeometryFactory::(anonymous)::CreateRenderedGeometryFromGeometryOnSphere`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CreateRenderedGeometryFromGeometryOnSphere( GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type geom_on_sphere, const GPlatesGui::ColourProxy &colour, float point_size_hint, float line_width_hint, bool fill_polygon, bool fill_polyline, const GPlatesGui::Colour &fill_modulate_colour, const boost::optional<GPlates ...` | constructor | `None` | public | — |
| `create_rendered_geometry()` | method | `RenderedGeometry` | public | Creates a RenderedGeometryImpl from GeometryOnSphere passed into constructor. |
| `visit_multi_point_on_sphere( GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere)` | method | `void` | private | — |
| `visit_point_on_sphere( GPlatesMaths::PointGeometryOnSphere::non_null_ptr_to_const_type point_on_sphere)` | method | `void` | private | — |
| `visit_polygon_on_sphere( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere)` | method | `void` | private | — |
| `visit_polyline_on_sphere( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere)` | method | `void` | private | — |
| `d_geom_on_sphere` | field | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | private | — |
| `d_colour` | field | `GPlatesGui::ColourProxy` | private | — |
| `d_point_size_hint` | field | `float` | private | — |
| `d_line_width_hint` | field | `float` | private | — |
| `d_fill_polygon` | field | `bool` | private | — |
| `d_fill_polyline` | field | `bool` | private | — |
| `d_fill_modulate_colour` | field | `GPlatesGui::Colour` | private | — |
| `d_symbol` | field | `boost::optional<GPlatesGui::Symbol>` | private | — |
| `d_rendered_geom` | field | `RenderedGeometry` | private | — |

### `GPlatesViewOperations::RenderedGeometryFactory::(anonymous)::CreateRenderedGeometryFromColouredGeometryOnSphere`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CreateRenderedGeometryFromColouredGeometryOnSphere( GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type geom_on_sphere, const std::vector<GPlatesGui::ColourProxy> &point_colours, float point_size_hint, float line_width_hint, const boost::optional<GPlatesGui::Symbol> &symbol_ = boost::none)` | constructor | `None` | public | — |
| `create_rendered_geometry()` | method | `RenderedGeometry` | public | Creates a RenderedGeometryImpl from GeometryOnSphere passed into constructor. |
| `visit_multi_point_on_sphere( GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere)` | method | `void` | private | — |
| `visit_point_on_sphere( GPlatesMaths::PointGeometryOnSphere::non_null_ptr_to_const_type point_on_sphere)` | method | `void` | private | — |
| `visit_polygon_on_sphere( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere)` | method | `void` | private | — |
| `visit_polyline_on_sphere( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere)` | method | `void` | private | — |
| `d_geom_on_sphere` | field | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | private | — |
| `d_point_colours` | field | `std::vector<GPlatesGui::ColourProxy>` | private | — |
| `d_point_size_hint` | field | `float` | private | — |
| `d_line_width_hint` | field | `float` | private | — |
| `d_symbol` | field | `boost::optional<GPlatesGui::Symbol>` | private | — |
| `d_rendered_geom` | field | `RenderedGeometry` | private | — |

### `GPlatesViewOperations::RenderedGeometryFactory::rendered_geometry_seq_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_RENDEREDGEOMETRYFACTORY_H` | macro | `None` | — |
| `DEFAULT_POINT_SIZE_HINT` | variable | `int` | Default point size hint (roughly one screen-space pixel). |
| `DEFAULT_LINE_WIDTH_HINT` | variable | `int` | Default line width hint (roughly one screen-space pixel). |
| `DEFAULT_COLOUR` | variable | `GPlatesGui::Colour` | Default colour (white). |
| `DEFAULT_RATIO_ARROWHEAD_SIZE_TO_GLOBE_RADIUS` | variable | `float` | Determines the default size of an arrowhead relative to the globe radius when the globe fills the viewport window. |
| `DEFAULT_ARROWHEAD_SIZE_IN_PIXELS` | variable | `float` | Determines the default size of an arrowhead (in device-independent pixels). |
| `DEFAULT_RATIO_ARROWLINE_WIDTH_TO_ARROWHEAD_SIZE` | variable | `float` | Determines the default ratio of the width of an arrowline relative to the size of its arrowhead. |
| `DEFAULT_SUBDUCTION_TEETH_WIDTH_IN_PIXELS` | variable | `float` | Determines the default width of a subduction tooth (in device-independent pixels). |
| `DEFAULT_SUBDUCTION_TEETH_SPACING_TO_WIDTH_RATIO` | variable | `float` | Determines the default spacing-to-width ratio of subduction teeth. |
| `DEFAULT_SUBDUCTION_TEETH_HEIGHT_TO_WIDTH_RATIO` | variable | `float` | Determines the default height-to-width ratio of a subduction tooth . |
| `DEFAULT_SYMBOL_SIZE` | variable | `unsigned int` | Determines the size of symbol rendered geometries. |
| `create_rendered_geometry_on_sphere( GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type, const GPlatesGui::ColourProxy &colour = DEFAULT_COLOUR, float point_size_hint = DEFAULT_POINT_SIZE_HINT, float line_width_hint = DEFAULT_LINE_WIDTH_HINT, bool fill_polygon = false, bool fill_polyline = false, const GPlatesGu ...` | function | `RenderedGeometry` | Creates a RenderedGeometry for a GeometryOnSphere. |
| `create_rendered_point_on_sphere( const GPlatesMaths::PointOnSphere &point_on_sphere, const GPlatesGui::ColourProxy &colour = DEFAULT_COLOUR, float point_size_hint = DEFAULT_POINT_SIZE_HINT)` | function | `RenderedGeometry` | Creates a RenderedGeometry for a PointOnSphere. |
| `create_rendered_multi_point_on_sphere( GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type, const GPlatesGui::ColourProxy &colour = DEFAULT_COLOUR, float point_size_hint = DEFAULT_POINT_SIZE_HINT)` | function | `RenderedGeometry` | Creates a RenderedGeometry for a MultiPointOnSphere. |
| `create_rendered_polyline_on_sphere( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type, const GPlatesGui::ColourProxy &colour = DEFAULT_COLOUR, float line_width_hint = DEFAULT_LINE_WIDTH_HINT, bool filled = false, const GPlatesGui::Colour &fill_modulate_colour = DEFAULT_COLOUR)` | function | `RenderedGeometry` | Creates a RenderedGeometry for a PolylineOnSphere. |
| `create_rendered_polygon_on_sphere( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type, const GPlatesGui::ColourProxy &colour = DEFAULT_COLOUR, float line_width_hint = DEFAULT_LINE_WIDTH_HINT, bool filled = false, const GPlatesGui::Colour &fill_modulate_colour = DEFAULT_COLOUR)` | function | `RenderedGeometry` | Creates a RenderedGeometry for a PolygonOnSphere. |
| `create_rendered_coloured_geometry_on_sphere( GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type, const std::vector<GPlatesGui::ColourProxy> &point_colours, float point_size_hint = DEFAULT_POINT_SIZE_HINT, float line_width_hint = DEFAULT_LINE_WIDTH_HINT, const boost::optional<GPlatesGui::Symbol> &symbol = boost: ...` | function | `RenderedGeometry` | Creates a RenderedGeometry for a GeometryOnSphere with per-point colouring. |
| `create_rendered_coloured_multi_point_on_sphere( GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type, const std::vector<GPlatesGui::ColourProxy> &point_colours, float point_size_hint = DEFAULT_POINT_SIZE_HINT)` | function | `RenderedGeometry` | Creates a RenderedGeometry for a MultiPointOnSphere with per-point colouring. |
| `create_rendered_coloured_polyline_on_sphere( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type, const std::vector<GPlatesGui::ColourProxy> &point_colours, float line_width_hint = DEFAULT_LINE_WIDTH_HINT)` | function | `RenderedGeometry` | Creates a RenderedGeometry for a PolylineOnSphere with per-point colouring. |
| `create_rendered_coloured_polygon_on_sphere( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type, const std::vector<GPlatesGui::ColourProxy> &point_colours, float line_width_hint = DEFAULT_LINE_WIDTH_HINT)` | function | `RenderedGeometry` | Creates a RenderedGeometry for a PolygonOnSphere with per-point colouring. |
| `create_rendered_coloured_edge_surface_mesh( const RenderedColouredEdgeSurfaceMesh::edge_seq_type &mesh_edges, const RenderedColouredEdgeSurfaceMesh::vertex_seq_type &mesh_vertices, const RenderedColouredEdgeSurfaceMesh::colour_seq_type &mesh_colours, bool use_vertex_colours, float line_width_hint = DEFAULT_LINE_WIDTH_H ...` | function | `RenderedGeometry` | Creates a RenderedGeometry for a coloured edge surface mesh. |
| `create_rendered_coloured_triangle_surface_mesh( const RenderedColouredTriangleSurfaceMesh::triangle_seq_type &mesh_triangles, const RenderedColouredTriangleSurfaceMesh::vertex_seq_type &mesh_vertices, const RenderedColouredTriangleSurfaceMesh::colour_seq_type &mesh_colours, bool use_vertex_colours, const GPlatesGui::Co ...` | function | `RenderedGeometry` | Creates a RenderedGeometry for a coloured triangle surface mesh. |
| `create_rendered_resolved_raster( const GPlatesAppLogic::ResolvedRaster::non_null_ptr_to_const_type &resolved_raster, const GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type &raster_colour_palette, const GPlatesGui::Colour &raster_modulate_colour = GPlatesGui::Colour::get_white(), float normal_map_height_field ...` | function | `RenderedGeometry` | Creates a RenderedGeometry for a resolved raster. |
| `create_rendered_resolved_scalar_field_3d( const GPlatesAppLogic::ResolvedScalarField3D::non_null_ptr_to_const_type &resolved_scalar_field, const ScalarField3DRenderParameters &scalar_field_render_parameters)` | function | `RenderedGeometry` | Creates a RenderedGeometry for a resolved 3D scalar field. |
| `create_rendered_tangential_arrow( const GPlatesMaths::PointOnSphere &start, const GPlatesMaths::Vector3D &arrow_direction, const float ratio_unit_vector_direction_to_globe_radius, const GPlatesGui::ColourProxy &colour = DEFAULT_COLOUR, const float ratio_arrowhead_size_to_globe_radius = DEFAULT_RATIO_ARROWHEAD_SIZE_TO_G ...` | function | `RenderedGeometry` | as a ratio of the size of the arrowhead (as rendered in 3D globe view). |
| `create_rendered_radial_arrow( const GPlatesMaths::PointOnSphere &position, float arrow_projected_length, float arrowhead_projected_size = DEFAULT_RATIO_ARROWHEAD_SIZE_TO_GLOBE_RADIUS, float ratio_arrowline_width_to_arrowhead_size = DEFAULT_RATIO_ARROWLINE_WIDTH_TO_ARROWHEAD_SIZE, const GPlatesGui::ColourProxy &arrow_co ...` | function | `RenderedGeometry` | Creates a single arrow, radial (or normal) to the globe's surface, consisting of a line segment with an arrowhead at the end (in the 3D globe view) and a symbol (in 2D map views). |
| `create_rendered_reconstruction_geometry( GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type reconstruction_geom, RenderedGeometry rendered_geom)` | function | `RenderedGeometry` | Creates a composite RenderedGeometry containing another RenderedGeometry and a ReconstructionGeometry associated with it. |
| `create_rendered_multi_reconstruction_geometry( const std::vector<GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type> &reconstruction_geoms, RenderedGeometry rendered_geom)` | function | `RenderedGeometry` | Creates a composite RenderedGeometry containing another RenderedGeometry and multiple ReconstructionGeometry objects associated with it. |
| `create_rendered_string( const GPlatesMaths::PointOnSphere &point_on_sphere, const QString &string, const GPlatesGui::ColourProxy &colour = DEFAULT_COLOUR, const GPlatesGui::ColourProxy &shadow_colour = GPlatesGui::ColourProxy(boost::none), int x_offset = 0, int y_offset = 0, const QFont &font = QFont())` | function | `RenderedGeometry` | Creates a RenderedGeometry for text. |
| `create_rendered_small_circle( const GPlatesMaths::SmallCircle &small_circle, const GPlatesGui::ColourProxy &colour = DEFAULT_COLOUR, float line_width_hint = DEFAULT_LINE_WIDTH_HINT)` | function | `RenderedGeometry` | Creates a RenderedGeometry for a SmallCircle. |
| `create_rendered_small_circle_arc( const GPlatesMaths::SmallCircleArc &small_circle_arc, const GPlatesGui::ColourProxy &colour = DEFAULT_COLOUR, float line_width_hint = DEFAULT_LINE_WIDTH_HINT)` | function | `RenderedGeometry` | Creates a RenderedGeometry for a SmallCircleArc. |
| `create_rendered_ellipse( const GPlatesMaths::PointOnSphere &centre, const GPlatesMaths::Real &semi_major_axis_radians, const GPlatesMaths::Real &semi_minor_axis_radians, const GPlatesMaths::GreatCircle &axis, const GPlatesGui::ColourProxy &colour = DEFAULT_COLOUR, float line_width_hint = DEFAULT_LINE_WIDTH_HINT)` | function | `RenderedGeometry` | Creates a RenderedGeometry for an Ellipse. |
| `create_rendered_arrowed_polyline( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type, const GPlatesGui::ColourProxy &colour = DEFAULT_COLOUR, const float arrowhead_size_in_pixels = DEFAULT_ARROWHEAD_SIZE_IN_PIXELS, const float arrowline_width_hint = DEFAULT_LINE_WIDTH_HINT)` | function | `RenderedGeometry` | Creates a polyline rendered geometry with an arrowhead on each segment. |
| `create_rendered_subduction_teeth_polyline( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline, bool subduction_polarity_is_left, const GPlatesGui::ColourProxy &colour = DEFAULT_COLOUR, float line_width_hint = DEFAULT_LINE_WIDTH_HINT, float teeth_width_in_pixels = DEFAULT_SUBDUCTION_TEETH_WIDTH_IN_PIXEL ...` | function | `RenderedGeometry` | Creates a RenderedGeometry for a PolylineOnSphere that has subduction teeth. |
| `create_rendered_symbol( const GPlatesMaths::PointOnSphere &centre, const GPlatesGui::Symbol &symbol, const GPlatesGui::ColourProxy &colour = DEFAULT_COLOUR, float line_width_hint = DEFAULT_LINE_WIDTH_HINT)` | function | `RenderedGeometry` | Creates a symbol defined by symbol that is centred at centre. |
| `create_rendered_triangle_symbol( const GPlatesMaths::PointOnSphere &centre, const GPlatesGui::ColourProxy &colour = DEFAULT_COLOUR, const unsigned int size = DEFAULT_SYMBOL_SIZE, const bool filled = TRUE, const float line_width_hint = DEFAULT_LINE_WIDTH_HINT)` | function | `RenderedGeometry` | Creates a triangle centred at centre. |
| `create_rendered_square_symbol( const GPlatesMaths::PointOnSphere &centre, const GPlatesGui::ColourProxy &colour = DEFAULT_COLOUR, const unsigned int size = DEFAULT_SYMBOL_SIZE, const bool filled = TRUE, const float line_width_hint = DEFAULT_LINE_WIDTH_HINT)` | function | `RenderedGeometry` | Creates a square centred at centre. |
| `create_rendered_circle_symbol( const GPlatesMaths::PointOnSphere &centre, const GPlatesGui::ColourProxy &colour = DEFAULT_COLOUR, const unsigned int size = DEFAULT_SYMBOL_SIZE, const bool filled = TRUE, const float line_width_hint = DEFAULT_LINE_WIDTH_HINT)` | function | `RenderedGeometry` | Creates a circle centred at centre. |
| `create_rendered_cross_symbol( const GPlatesMaths::PointOnSphere &centre, const GPlatesGui::ColourProxy &colour = DEFAULT_COLOUR, const unsigned int size = DEFAULT_SYMBOL_SIZE, const float line_width_hint = DEFAULT_LINE_WIDTH_HINT)` | function | `RenderedGeometry` | Creates a cross centred at centre. |
| `create_rendered_strain_marker_symbol( const GPlatesMaths::PointOnSphere &centre, const unsigned int size = DEFAULT_SYMBOL_SIZE, const double scale_x = 0, const double scale_y = 0, const double angle = 0)` | function | `RenderedGeometry` | Creates a cross centred at centre. |

## Notes

- **What comes back is shareable and effectively immutable.** The returned
  `RenderedGeometry` is a reference-counted handle whose implementation is only
  ever exposed through const visitor methods, so copies can be dropped into
  several `RenderedGeometryLayer`s without cloning and without aliasing hazards.
  The underlying geometries are `non_null_ptr_to_const_type`, so nothing is
  copied on creation either.
- **A default-constructed `RenderedGeometry` is legal and silent.** It has no
  implementation and `accept_visitor` on it does nothing. Both dispatch visitors
  start with one and return it unchanged if the geometry type has no case, and
  `create_rendered_symbol` returns one after `GPlatesGlobal::Abort` on an
  unrecognised `Symbol` type. A drawable that quietly fails to appear is the
  symptom.
- **The dispatch visitors hold references, not copies.** Both store
  `const GPlatesGui::ColourProxy &` and `const boost::optional<GPlatesGui::Symbol> &`
  members. They are safe only because they are constructed, used and destroyed
  within one factory call; do not store one, return one, or extend its lifetime.
- **Per-point colour counts are a caller obligation.** The `*_coloured_*`
  functions require the colour vector to match the point count — for a polygon,
  the *exterior ring* vertex count. Only the single-point case actually asserts
  (`PreconditionViolationError`); mismatches elsewhere are the painter's problem.
- **`symbol` only affects points.** Passing a symbol to
  `create_rendered_geometry_on_sphere` changes nothing unless the geometry turns
  out to be a `PointGeometryOnSphere`; for a multipoint, polyline or polygon it is
  silently ignored.
- **Fill flags cross type boundaries.** `create_rendered_polyline_on_sphere` takes
  a `filled` flag that makes a polyline fill like a polygon, and the generic
  entry point carries separate `fill_polygon` and `fill_polyline` flags for
  exactly that reason.
- **Arrow parameters are not symmetrical between the two arrow kinds.**
  `create_rendered_tangential_arrow` pre-multiplies the direction by
  `ratio_unit_vector_direction_to_globe_radius` and passes the arrowhead ratio
  through, with a hard-coded cap of 0.5 on arrowhead-to-arrowline length that is
  not exposed as a parameter; `create_rendered_radial_arrow` instead converts its
  width *ratio* into an absolute width before constructing `RenderedRadialArrow`.
- **The defaults are header-scope const objects.** `DEFAULT_COLOUR` in particular
  is a `GPlatesGui::Colour` with a dynamic initialiser defined in the header, so
  every translation unit that includes it gets its own copy constructed at static
  initialisation time. Adding more non-trivial constants here compounds that.

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 68 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 38 |
| [canvas-tools/AdjustFittedPoleEstimate](../canvas-tools/AdjustFittedPoleEstimate.md) | canvas-tools | 27 |
| [view-operations/MoveVertexGeometryOperation](MoveVertexGeometryOperation.md) | view-operations | 20 |
| [qt-widgets/HellingerDialog](../qt-widgets/HellingerDialog.md) | qt-widgets | 15 |
| [view-operations/SplitFeatureGeometryOperation](SplitFeatureGeometryOperation.md) | view-operations | 13 |
| [app-logic/deprecated/PaleomagUtils](../app-logic/deprecated/PaleomagUtils.md) | app-logic | 11 |
| [canvas-tools/MeasureDistance](../canvas-tools/MeasureDistance.md) | canvas-tools | 11 |
| [view-operations/AddPointGeometryOperation](AddPointGeometryOperation.md) | view-operations | 11 |
| [view-operations/DeleteVertexGeometryOperation](DeleteVertexGeometryOperation.md) | view-operations | 9 |
| [view-operations/InsertVertexGeometryOperation](InsertVertexGeometryOperation.md) | view-operations | 9 |
| [canvas-tools/CreateSmallCircle](../canvas-tools/CreateSmallCircle.md) | canvas-tools | 5 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 3 |
| [qt-widgets/ModifyReconstructionPoleWidget](../qt-widgets/ModifyReconstructionPoleWidget.md) | qt-widgets | 3 |
| [qt-widgets/SmallCircleWidget](../qt-widgets/SmallCircleWidget.md) | qt-widgets | 3 |
| [qt-widgets/deprecated/CreateTopologyWidget](../qt-widgets/deprecated/CreateTopologyWidget.md) | qt-widgets | 3 |
| [view-operations/ChangeLightDirectionOperation](ChangeLightDirectionOperation.md) | view-operations | 3 |
| [view-operations/MovePoleOperation](MovePoleOperation.md) | view-operations | 3 |
| [view-operations/RenderedGeometryParameters](RenderedGeometryParameters.md) | view-operations | 3 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 2 |

*... and 6 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedGeometryFactory.h
python scripts/gpq.py def GPlatesViewOperations::RenderedGeometryFactory::(anonymous)::CreateRenderedGeometryFromGeometryOnSphere --body
python scripts/gpq.py uses CreateRenderedGeometryFromGeometryOnSphere --kind class
python scripts/gpq.py hier CreateRenderedGeometryFromGeometryOnSphere
```
