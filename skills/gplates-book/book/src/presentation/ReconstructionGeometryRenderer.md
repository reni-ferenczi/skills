# ReconstructionGeometryRenderer

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 40 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/ReconstructionGeometryRenderer.h` | C++ | 634 |
| `src/presentation/ReconstructionGeometryRenderer.cc` | C++ | 2385 |

## Overview

`ReconstructionGeometryRenderer` is the single place that knows how to turn
any concrete `ReconstructionGeometry` (RFGs, resolved topologies and
networks, resolved rasters and scalar fields, flowlines, motion paths, VGPs,
multi-point vector fields, co-registration data) into `RenderedGeometry`
objects, via `GPlatesAppLogic::ConstReconstructionGeometryVisitor` double
dispatch. `LayerOutputRenderer` is its usual caller: it hands each layer
proxy's output to `render()`, one reconstruction geometry at a time, bracketed
by `begin_render()`/`end_render()` (which cannot nest, and accumulate into
whatever the target `RenderedGeometryLayer` already holds — clearing it is
the caller's job). Rendering is controlled entirely through the `RenderParams`
struct, a flat bag of per-layer-type settings (fill colours, line widths,
scalar/raster colour palettes, VGP visibility predicate, topological network
triangulation mode, and so on); `RenderParamsPopulator` builds one by visiting
whichever concrete `VisualLayerParams` a layer has, so this class itself never
has to know about `RasterVisualLayerParams`, `ReconstructVisualLayerParams`
and the rest directly.

Colouring and symbol lookup are centralised in the free functions `get_colour()`
and `get_symbol()`: `get_colour()` picks, in order, an explicit override
colour, a Python `DrawStyle` (when the Python component is enabled and a
`StyleAdapter` is supplied), or else a `ColourProxy` that defers to the
legacy hard-coded colouring schemes; `get_symbol()` looks up a
`GPlatesGui::Symbol` by feature type in an optional `symbol_map_type`. Shared
topological sub-segments are handled specially: `add_topological_shared_sub_segments()`
accumulates, per rendered layer, which resolved boundaries/networks share
each `ResolvedTopologicalSharedSubSegment`, and `render_topological_shared_sub_segments()`
draws each one once at `end_render()` — as ordinary polylines, or with
subduction teeth when `get_subduction_polarity()` finds a `gpml:SubductionZone`
feature with a `gpml:subductionPolarity` of `Left` or `Right` — associating
the rendered geometry with *all* the topologies that share it so clicking it
selects the right features. The large block of `render_topological_network_*`
private methods handles the several ways a `ResolvedTopologicalNetwork`'s
Delaunay triangulation can be drawn: filled by draw style, coloured by
smoothed or unsmoothed strain rate (barycentric or natural-neighbour
subdivision, each with its own angular subdivision threshold), rigid blocks,
and per-point velocities.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPresentation::ReconstructionGeometryRenderer`](#gplatespresentationreconstructiongeometryrenderer) | class | [`GPlatesAppLogic::ConstReconstructionGeometryVisitor`](../app-logic/ReconstructionGeometry.md) | — | 0 | Visits classes derived from ReconstructionGeometry and renders them by creating RenderedGeometry objects. |

## Members

### `GPlatesPresentation::ReconstructionGeometryRenderer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderParams` | struct | `None` | public | Various parameters that control rendering. |
| `RenderParamsPopulator` | class | `None` | public | Populates RenderParams from VisualLayerParams. |
| `rendered_geometries_spatial_partition_type` | typedef | `GPlatesMaths::CubeQuadTreePartition<GPlatesViewOperations::RenderedGeometry>` | public | Typedef for a spatial partition of rendered geometries. |
| `ReconstructionGeometryRenderer( const RenderParams &render_params, const GPlatesGui::RenderSettings &render_settings, const std::set<GPlatesModel::FeatureId> &topological_sections, const GPlatesAppLogic::TopologyUtils::resolved_topological_boundaries_networks_to_shared_sub_segments_map_type &all_resolved_topological_sh ...` | constructor | `None` | public | Created RenderedGeometry objects are added to the spatial partition of rendered geometries rendered\_geometry\_spatial\_partition. |
| `begin_render( GPlatesViewOperations::RenderedGeometryLayer &rendered_geometry_layer)` | method | `void` | public | Begins rendering into the specified rendered\_geometry\_layer. |
| `end_render()` | method | `void` | public | Renders all created rendered geometries since the last call to begin\_render into the rendered geometry layer specified in begin\_render. |
| `render( const GPlatesUtils::non_null_intrusive_ptr<ReconstructionGeometryDerivedType> &reconstruction_geometry, boost::optional<const GPlatesMaths::CubeQuadTreeLocation &> spatial_partition_location = boost::none)` | method | `void` | public | Creates rendered geometry(s) from the specified reconstruction geometry (a derived type). |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<co_registration_data_type> &crr)` | method | `void` | private | The following methods are for visiting derived ReconstructionGeometry objects. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<multi_point_vector_field_type> &mpvf)` | method | `void` | private | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstructed_feature_geometry_type> &rfg)` | method | `void` | private | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstructed_flowline_type> &rf)` | method | `void` | private | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstructed_motion_path_type> &rmp)` | method | `void` | private | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstructed_scalar_coverage_type> &rsc)` | method | `void` | private | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstructed_small_circle_type> &rsc)` | method | `void` | private | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstructed_virtual_geomagnetic_pole_type> &rvgp)` | method | `void` | private | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_raster_type> &rr)` | method | `void` | private | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_scalar_field_3d_type> &rsf)` | method | `void` | private | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_topological_geometry_type> &rtg)` | method | `void` | private | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_topological_network_type> &rtn)` | method | `void` | private | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<topology_reconstructed_feature_geometry_type> &trfg)` | method | `void` | private | — |
| `DEFAULT_SPATIAL_PARTITION_DEPTH` | field | `unsigned int` | private | The default depth of the rendered geometries spatial partition (the quad trees in each cube face). |
| `d_render_params` | field | `RenderParams` | private | — |
| `d_render_settings` | field | `GPlatesGui::RenderSettings` | private | — |
| `d_topological_sections` | field | `std::set<GPlatesModel::FeatureId>` | private | — |
| `d_all_resolved_topological_shared_sub_segments` | field | `GPlatesAppLogic::TopologyUtils::resolved_topological_boundaries_networks_to_shared_sub_segments_map_type` | private | — |
| `d_colour` | field | `boost::optional<GPlatesGui::Colour>` | private | — |
| `d_reconstruction_adjustment` | field | `boost::optional<GPlatesMaths::Rotation>` | private | — |
| `d_feature_type_symbol_map` | field | `boost::optional<const GPlatesGui::symbol_map_type &>` | private | — |
| `d_style_adapter` | field | `boost::optional<const GPlatesGui::StyleAdapter &>` | private | — |
| `d_rendered_geometry_layer` | field | `boost::optional<GPlatesViewOperations::RenderedGeometryLayer &>` | private | The rendered geometry layer for all rendering between begin\_render and end\_render. |
| `d_rendered_geometries_spatial_partition_location` | field | `boost::optional<const rendered_geometries_spatial_partition_type::location_type &>` | private | Location in the rendered geometries spatial partition to add rendered geometries to. |
| `d_resolved_topological_shared_sub_segments_map` | field | `std::map< GPlatesAppLogic::ResolvedTopologicalSharedSubSegment::non_null_ptr_type, std::vector<GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type>>` | private | Mapping from shared boundary sub-segments to their sharing resolved topological boundaries and networks (rendered in the current rendered geometry layer). |
| `render( const GPlatesViewOperations::RenderedGeometry &rendered_geometry)` | method | `void` | private | Adds a rendered geometry that does not correspond to a GeometryOnSphere from a reconstruction geometry. |
| `render_reconstruction_geometry_on_sphere( const GPlatesViewOperations::RenderedGeometry &rendered_geometry)` | method | `void` | private | Adds the specified rendered geometry that corresponds to the GeometryOnSphere in the ReconstructionGeometry being visited - for example, for RFGs this is the geometry returned by 'ReconstructedFeatureGeometry::reconstructed\_geometry()'. |
| `smoothed_vertex_type` | typedef | `std::pair< GPlatesMaths::PointOnSphere, GPlatesAppLogic::ResolvedTriangulation::Delaunay_2::Face_handle>` | private | — |
| `SmoothedVertexMapPredicate` | class | `None` | private | Enables smoothed\_vertex\_type to be used as a key in a 'std::map'. |
| `smoothed_vertex_indices_type` | typedef | `GPlatesAppLogic::ResolvedTriangulation::VertexIndices< smoothed_vertex_type, SmoothedVertexMapPredicate>` | private | — |
| `unsmoothed_vertex_indices_type` | typedef | `GPlatesAppLogic::ResolvedTriangulation::VertexIndices< GPlatesAppLogic::ResolvedTriangulation::Delaunay_2::Vertex_handle>` | private | — |
| `render_topological_network_delaunay_face_smoothed_strain_rate( const GPlatesMaths::PointOnSphere &point1, const GPlatesMaths::PointOnSphere &point2, const GPlatesMaths::PointOnSphere &point3, smoothed_vertex_indices_type &vertex_indices, GPlatesViewOperations::RenderedColouredTriangleSurfaceMesh::triangle_seq_type &ren ...` | method | `void` | private | — |
| `render_topological_network_delaunay_faces_smoothed_strain_rates( const GPlatesAppLogic::ResolvedTopologicalNetwork::non_null_ptr_to_const_type &rtn, const double &subdivide_face_threshold)` | method | `void` | private | — |
| `render_topological_network_delaunay_faces_unsmoothed_strain_rates( const GPlatesAppLogic::ResolvedTopologicalNetwork::non_null_ptr_to_const_type &rtn)` | method | `void` | private | — |
| `render_topological_network_delaunay_edges_smoothed_strain_rates( const GPlatesAppLogic::ResolvedTopologicalNetwork::non_null_ptr_to_const_type &rtn, const double &subdivide_edge_threshold_angle)` | method | `void` | private | — |
| `render_topological_network_delaunay_edges_unsmoothed_strain_rates( const GPlatesAppLogic::ResolvedTopologicalNetwork::non_null_ptr_to_const_type &rtn)` | method | `void` | private | — |
| `render_topological_network_delaunay_edges_using_draw_style( const GPlatesAppLogic::ResolvedTopologicalNetwork::non_null_ptr_to_const_type &rtn)` | method | `void` | private | — |
| `render_topological_network_fill_using_draw_style( const GPlatesAppLogic::ResolvedTopologicalNetwork::non_null_ptr_to_const_type &rtn)` | method | `void` | private | — |
| `render_topological_network_rigid_blocks( const GPlatesAppLogic::ResolvedTopologicalNetwork::non_null_ptr_to_const_type &rtn)` | method | `void` | private | — |
| `render_topological_network_velocities( const GPlatesAppLogic::ResolvedTopologicalNetwork::non_null_ptr_to_const_type &topological_network)` | method | `void` | private | Get the reconstruction geometries that are resolved topological networks and draw the velocities at the network points if there are any. |
| `add_topological_shared_sub_segments( const GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type &resolved_topology, const GPlatesModel::FeatureHandle::iterator &resolved_topology_feature_property)` | method | `void` | private | Add the shared sub-segments of a resolved topological boundary or network to be rendered later (at the end of the current rendered geometry layer). |
| `render_topological_shared_sub_segments()` | method | `void` | private | Render shared sub-segments of resolved topological boundaries and networks (rendered in the current rendered geometry layer). |
| `SubductionPolarity` | enum | `None` | private | — |
| `get_subduction_polarity( const GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type &resolved_topological_section)` | method | `boost::optional<SubductionPolarity>` | private | Returns the subduction polarity if the specified reconstruction geometry represents a subduction zone. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `is_topological_section( const ReconstructionGeometryPointer &reconstruction_geometry, const std::set<GPlatesModel::FeatureId> &topological_sections)` | function | `bool` | Returns true if the reconstruction geometry is used as a topological section in any topology for any reconstruction time. |
| `get_symbol( boost::optional<const GPlatesGui::symbol_map_type &> symbol_map, const GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type &reconstruction_geometry)` | function | `boost::optional<GPlatesGui::Symbol>` | Returns a GPlatesGui::Symbol for the feature type of the reconstruction\_geometry, if an appropriate entry in the feature\_type\_symbol\_map exists. |
| `get_colour( const GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type &reconstruction_geometry, const boost::optional<GPlatesGui::Colour> &colour, boost::optional<const GPlatesGui::StyleAdapter &> style_adapter)` | function | `GPlatesGui::ColourProxy` | Returns a GPlatesGui::ColourProxy. |
| `create_rendered_reconstruction_geometry( const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &geometry, const GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type &reconstruction_geometry, const GPlatesPresentation::ReconstructionGeometryRenderer::RenderParams &render_params, const GPlatesGu ...` | function | `GPlatesViewOperations::RenderedGeometry` | Creates a RenderedGeometry from geometry and wraps it in another RenderedGeometry that references reconstruction\_geometry. |
| `SUBDIVIDE_TOPOLOGICAL_NETWORK_DELAUNAY_BARYCENTRIC_SMOOTHED_ANGLE` | variable | `double` | Threshold used when subdividing a topological network delaunay face to visualise 'smoothed' strain rates. |
| `SUBDIVIDE_TOPOLOGICAL_NETWORK_DELAUNAY_NATURAL_NEIGHBOUR_SMOOTHED_ANGLE` | variable | `double` | — |
| `DISABLE_GCC_WARNING` | variable | `PUSH_GCC_WARNINGS` | The BOOST\_FOREACH macro in versions of boost before 1.37 uses the same local variable name in each instantiation. |
| `GPLATES_PRESENTATION_RECONSTRUCTION_GEOMETRY_RENDERER_H` | macro | `None` | — |

## Notes

`begin_render()`/`end_render()` calls cannot nest and must be paired —
mismatches throw `GPlatesGlobal::PreconditionViolationError`, as does calling
the templated `render()` outside such a pair. `render()` dispatches through
`accept_visitor()` rather than calling a `visit()` overload directly because
some derived reconstruction-geometry types (for example flowlines) derive
from another visited type (RFG), so full virtual dispatch is required to hit
the right overload. Only rendered geometries that represent a
`ReconstructionGeometry`'s own `GeometryOnSphere` should go through
`render_reconstruction_geometry_on_sphere()` (which honours the current
spatial-partition location); everything else — velocity arrows, shared
sub-segments, network fills — must go through the plain `render(RenderedGeometry)`
overload, which always adds to the spatial partition root. `d_render_settings`,
`d_topological_sections` and `d_all_resolved_topological_shared_sub_segments`
are held by reference, not owned, so the renderer must not outlive whatever
constructed those. `d_resolved_topological_shared_sub_segments_map` is
per-rendered-geometry-layer bookkeeping only valid between `begin_render()`
and `end_render()`; shared sub-segments accumulate there and are drawn only
once, at the end, regardless of how many topologies reference them.

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/LayerOutputRenderer](LayerOutputRenderer.md) | presentation | 15 |
| [qt-widgets/ModifyReconstructionPoleWidget](../qt-widgets/ModifyReconstructionPoleWidget.md) | qt-widgets | 15 |
| [gui/GeometryFocusHighlight](../gui/GeometryFocusHighlight.md) | gui | 11 |
| [qt-widgets/ReconstructLayerOptionsWidget](../qt-widgets/ReconstructLayerOptionsWidget.md) | qt-widgets | 8 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 6 |
| [presentation/VisualLayer](VisualLayer.md) | presentation | 4 |
| [qt-widgets/TopologyGeometryResolverLayerOptionsWidget](../qt-widgets/TopologyGeometryResolverLayerOptionsWidget.md) | qt-widgets | 4 |
| [view-operations/RenderedGeometryFactory](../view-operations/RenderedGeometryFactory.md) | view-operations | 1 |
| [view-operations/RenderedGeometryLayer](../view-operations/RenderedGeometryLayer.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/presentation/ReconstructionGeometryRenderer.h
python scripts/gpq.py def GPlatesPresentation::ReconstructionGeometryRenderer --body
python scripts/gpq.py uses ReconstructionGeometryRenderer --kind class
python scripts/gpq.py hier ReconstructionGeometryRenderer
```
