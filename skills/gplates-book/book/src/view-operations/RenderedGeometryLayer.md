# RenderedGeometryLayer

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 140 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedGeometryLayer.h` | C++ | 365 |
| `src/view-operations/RenderedGeometryLayer.cc` | C++ | 916 |

## Overview

[[[PROSE overview unit=view-operations/RenderedGeometryLayer tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedGeometryLayerImpl`](#gplatesviewoperationsrenderedgeometrylayerimpl) | class | [`GPlatesUtils::ReferenceCount<RenderedGeometryLayerImpl>`](../utils/ReferenceCount.md) | — | 2 | Interface for implementation of rendered geometry layer. |
| [`GPlatesViewOperations::(anonymous)::ZoomIndependentLayerImpl`](#gplatesviewoperationsanonymouszoomindependentlayerimpl) | class | [`RenderedGeometryLayerImpl`](RenderedGeometryLayer.md) | — | 0 | Standard rendered layer implementation that simply appends each added rendered geometry to the end of a sequence. |
| [`GPlatesViewOperations::(anonymous)::IsZoomDependent`](#gplatesviewoperationsanonymousiszoomdependent) | class | [`GPlatesViewOperations::ConstRenderedGeometryVisitor`](RenderedGeometryVisitor.md) | — | 0 | Determines if a RenderedGeometry should be classified as zoom-dependent or not. |
| [`GPlatesViewOperations::(anonymous)::ZoomDependentLayerImpl`](#gplatesviewoperationsanonymouszoomdependentlayerimpl) | class | [`RenderedGeometryLayerImpl`](RenderedGeometryLayer.md) | — | 0 | Sequence of RenderedGeometry objects that changes with zoom. |
| [`GPlatesViewOperations::(anonymous)::PartitionedLocatedRenderedGeometry`](#gplatesviewoperationsanonymouspartitionedlocatedrenderedgeometry) | struct | — | — | 0 | Helper structure when copying between render layer impl's in render order. |
| [`GPlatesViewOperations::RenderedGeometryLayer`](#gplatesviewoperationsrenderedgeometrylayer) | class | `QObject` | — | 0 | — |

## Members

### `GPlatesViewOperations::RenderedGeometryLayerImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `rendered_geometry_index_type` | typedef | `RenderedGeometryLayer::rendered_geometry_index_type` | public | Convenience typedef for rendered geometry index. |
| `partitioned_rendered_geometry_type` | typedef | `RenderedGeometryLayer::PartitionedRenderedGeometry` | public | Convenience typedef for a rendered geometry stored in a spatial partition. |
| `rendered_geometries_spatial_partition_type` | typedef | `RenderedGeometryLayer::rendered_geometries_spatial_partition_type` | public | Convenience typedef for rendered geometries spatial partition. |
| `DEFAULT_SPATIAL_PARTITION_DEPTH` | field | `unsigned int` | public | The default depth of the rendered geometries spatial partition (the quad trees in each cube face). |
| `~RenderedGeometryLayerImpl()` | destructor | `None` | public | — |
| `set_ratio_zoom_dependent_bin_dimension_to_globe_radius( float ratio_zoom_dependent_bin_dimension_to_globe_radius)` | method | `void` | public | — |
| `set_viewport_zoom_factor( const double &viewport_zoom_factor)` | method | `void` | public | — |
| `get_viewport_zoom_factor` | field | `double` | public | — |
| `is_empty()` | method | `bool` | public | — |
| `get_num_rendered_geometries()` | method | `unsigned int` | public | — |
| `get_rendered_geometry` | field | `RenderedGeometry` | public | — |
| `get_rendered_geometries()` | method | `rendered_geometries_spatial_partition_type::non_null_ptr_to_const_type` | public | — |
| `add_rendered_geometry( RenderedGeometry, boost::optional<const GPlatesMaths::CubeQuadTreeLocation &> cube_quad_tree_location)` | method | `void` | public | — |
| `clear_rendered_geometries()` | method | `void` | public | — |

### `GPlatesViewOperations::(anonymous)::ZoomIndependentLayerImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ZoomIndependentLayerImpl( const double &viewport_zoom_factor)` | constructor | `None` | public | — |
| `set_ratio_zoom_dependent_bin_dimension_to_globe_radius( float ratio_zoom_dependent_bin_dimension_to_globe_radius)` | method | `void` | public | — |
| `set_viewport_zoom_factor( const double &viewport_zoom_factor)` | method | `void` | public | — |
| `is_empty()` | method | `bool` | public | — |
| `get_num_rendered_geometries()` | method | `unsigned int` | public | — |
| `get_rendered_geometries()` | method | `rendered_geometries_spatial_partition_type::non_null_ptr_to_const_type` | public | — |
| `add_rendered_geometry( RenderedGeometry rendered_geom, boost::optional<const GPlatesMaths::CubeQuadTreeLocation &> cube_quad_tree_location)` | method | `void` | public | — |
| `clear_rendered_geometries()` | method | `void` | public | — |
| `rendered_geom_seq_type` | typedef | `std::vector<RenderedGeometry>` | private | Typedef for sequence of RenderedGeometry objects. |
| `d_rendered_geom_seq` | field | `rendered_geom_seq_type` | private | — |
| `d_rendered_geom_spatial_partition` | field | `rendered_geometries_spatial_partition_type::non_null_ptr_type` | private | — |
| `d_current_viewport_zoom_factor` | field | `double` | private | — |

### `GPlatesViewOperations::(anonymous)::IsZoomDependent`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator()( const RenderedGeometry &rendered_geom)` | operator | `boost::optional<GPlatesMaths::PointOnSphere>` | public | Returns true and position on sphere of rendered geometry if the type of rendered geometry is zoom-dependent. |
| `visit_rendered_point_on_sphere( const GPlatesViewOperations::RenderedPointOnSphere &rendered_point_on_sphere)` | method | `void` | private | — |
| `visit_rendered_radial_arrow( const RenderedRadialArrow &rendered_radial_arrow)` | method | `void` | private | — |
| `visit_rendered_tangential_arrow( const RenderedTangentialArrow &rendered_tangential_arrow)` | method | `void` | private | — |
| `d_position_on_sphere` | field | `boost::optional<GPlatesMaths::PointOnSphere>` | private | — |

### `GPlatesViewOperations::(anonymous)::ZoomDependentLayerImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ZoomDependentLayerImpl( float ratio_zoom_dependent_bin_dimension_to_globe_radius, const double &viewport_zoom_factor)` | constructor | `None` | public | — |
| `set_ratio_zoom_dependent_bin_dimension_to_globe_radius( float ratio_zoom_dependent_bin_dimension_to_globe_radius)` | method | `void` | public | — |
| `set_viewport_zoom_factor( const double &viewport_zoom_factor)` | method | `void` | public | — |
| `is_empty()` | method | `bool` | public | — |
| `get_num_rendered_geometries()` | method | `unsigned int` | public | — |
| `add_rendered_geometry( RenderedGeometry rendered_geom, boost::optional<const GPlatesMaths::CubeQuadTreeLocation &> cube_quad_tree_location)` | method | `void` | public | — |
| `clear_rendered_geometries()` | method | `void` | public | — |
| `get_rendered_geometries()` | method | `rendered_geometries_spatial_partition_type::non_null_ptr_to_const_type` | public | — |
| `zoom_independent_seq_type` | typedef | `std::vector<RenderedGeometry>` | private | Typedef for sequence of zoom-independent RenderedGeometry objects. |
| `zoom_dependent_seq_type` | typedef | `GPlatesUtils::LatLonAreaSampling<RenderedGeometry>` | private | Typedef for sequence of zoom-dependent RenderedGeometry objects. |
| `d_current_ratio_zoom_dependent_bin_dimension_to_globe_radius` | field | `float` | private | — |
| `d_current_viewport_zoom_factor` | field | `GPlatesMaths::real_t` | private | — |
| `d_zoom_independent_seq` | field | `zoom_independent_seq_type` | private | — |
| `d_zoom_independent_rendered_geom_spatial_partition` | field | `rendered_geometries_spatial_partition_type::non_null_ptr_type` | private | — |
| `d_zoom_dependent_seq` | field | `zoom_dependent_seq_type` | private | — |
| `get_zoom_dependent_sample_spacing( float ratio_zoom_dependent_bin_dimension_to_globe_radius, const double &viewport_zoom_factor)` | method | `double` | private | Calculate a lat/lon area sample spacing from the viewport zoom factor. |
| `reset_sample_spacing()` | method | `void` | private | — |

### `GPlatesViewOperations::(anonymous)::PartitionedLocatedRenderedGeometry`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PartitionedLocatedRenderedGeometry( const RenderedGeometryLayer::PartitionedRenderedGeometry &parititioned_rendered_geometry_, const GPlatesMaths::CubeQuadTreeLocation &cube_quad_tree_location_)` | constructor | `None` | public | — |
| `parititioned_rendered_geometry` | field | `RenderedGeometryLayer::PartitionedRenderedGeometry` | public | — |
| `cube_quad_tree_location` | field | `GPlatesMaths::CubeQuadTreeLocation` | public | — |
| `SortRenderOrder` | struct | `None` | public | Used to sort by render order. |

### `GPlatesViewOperations::RenderedGeometryLayer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `user_data_type` | typedef | `boost::any` | public | Typedef for arbitrary user-supplied data that will be returned when layer\_was\_updated signal is emitted. |
| `rendered_geometry_index_type` | typedef | `unsigned int` | public | Typedef for a RenderedGeometry index. |
| `rendered_geometry_layer_impl_ptr_type` | typedef | `boost::intrusive_ptr<RenderedGeometryLayerImpl>` | public | Typedef for pointer to rendered geometry layer implementation. |
| `PartitionedRenderedGeometry` | struct | `None` | public | Rendered geometries stored in a spatial partition are sorted spatially rather than by render (draw) order - so this structure associated each rendered geometry with its render order. |
| `rendered_geometries_spatial_partition_type` | typedef | `GPlatesMaths::CubeQuadTreePartition<PartitionedRenderedGeometry>` | public | Typedef for a spatial partition of rendered geometries. |
| `RenderedGeometryIterator` | class | `None` | public | Iterator over rendered geometries. |
| `iterator` | typedef | `RenderedGeometryIterator` | public | Typedef for iterator over rendered geometries. |
| `RenderedGeometryLayer( const double &viewport_zoom_factor, user_data_type user_data)` | constructor | `None` | public | Construct a regular rendered geometry layer where each rendered geometry added gets pushed onto end of a list of rendered geometries. when layer\_was\_updated signal is emitted - currently this should only be used by ... |
| `RenderedGeometryLayer( float ratio_zoom_dependent_bin_dimension_to_globe_radius, const double &viewport_zoom_factor, user_data_type user_data)` | constructor | `None` | public | Construct a zoom-dependent rendered geometry layer where the globe is divided into roughly equal area latitude/longitude bins that the rendered geometries are added to. |
| `~RenderedGeometryLayer()` | destructor | `None` | public | — |
| `set_ratio_zoom_dependent_bin_dimension_to_globe_radius( float ratio_zoom_dependent_bin_dimension_to_globe_radius = 0)` | method | `void` | public | If set to a non-zero value then constructs a zoom-dependent rendered geometry layer where the globe is divided into roughly equal area latitude/longitude bins that the rendered geometries are added to (at most one geometry is rendered per ... |
| `set_viewport_zoom_factor( const double &viewport_zoom_factor)` | method | `void` | public | Sets the viewport zoom factor. |
| `set_active( bool active = true)` | method | `void` | public | — |
| `is_active()` | method | `bool` | public | — |
| `is_empty()` | method | `bool` | public | — |
| `get_num_rendered_geometries()` | method | `unsigned int` | public | — |
| `get_rendered_geometry( rendered_geometry_index_type rendered_geom_index)` | method | `RenderedGeometry` | public | Returns the 'rendered\_geom\_index'th rendered geometry added via add\_rendered\_geometry. |
| `get_rendered_geometries()` | method | `GPlatesUtils::non_null_intrusive_ptr<const rendered_geometries_spatial_partition_type>` | public | Returns the rendered geometries in a spatial partition. |
| `rendered_geometry_begin()` | method | `iterator` | public | Begin iterator for sequence of RenderedGeometry objects. |
| `rendered_geometry_end()` | method | `iterator` | public | End iterator for sequence of RenderedGeometry objects. |
| `add_rendered_geometry( RenderedGeometry, boost::optional<const GPlatesMaths::CubeQuadTreeLocation &> cube_quad_tree_location = boost::none)` | method | `void` | public | Adds a rendered geometry to the list. |
| `clear_rendered_geometries()` | method | `void` | public | — |
| `accept_visitor( ConstRenderedGeometryLayerVisitor &)` | method | `void` | public | — |
| `accept_visitor( RenderedGeometryLayerVisitor &)` | method | `void` | public | — |
| `layer_was_updated( GPlatesViewOperations::RenderedGeometryLayer &, GPlatesViewOperations::RenderedGeometryLayer::user_data_type user_data)` | method | `void` | public | Signal is emitted whenever this rendered geometry layer has been updated. |
| `d_user_data` | field | `user_data_type` | private | — |
| `d_impl` | field | `rendered_geometry_layer_impl_ptr_type` | private | — |
| `d_is_active` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `is_zoom_dependent( const RenderedGeometry &rendered_geom)` | function | `boost::optional<GPlatesMaths::PointOnSphere>` | Returns true and position on sphere of rendered geometry if the type of rendered geometry is zoom-dependent. |
| `copy_rendered_geometries_in_render_order( RenderedGeometryLayerImpl &dst_rendered_geometry_layer_impl, const RenderedGeometryLayerImpl &src_rendered_geometry_layer_impl)` | function | `void` | Copy the src rendered layer's rendered geometries and over to the dst layer in rendered order. |
| `GPLATES_VIEWOPERATIONS_RENDEREDGEOMETRYLAYER_H` | macro | `None` | — |
| `operator==( const RenderedGeometryLayer::RenderedGeometryIterator &lhs, const RenderedGeometryLayer::RenderedGeometryIterator &rhs)` | operator | `bool` | — |

## Notes

[[[PROSE notes unit=view-operations/RenderedGeometryLayer tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [canvas-tools/AdjustFittedPoleEstimate](../canvas-tools/AdjustFittedPoleEstimate.md) | canvas-tools | 25 |
| [view-operations/MoveVertexGeometryOperation](MoveVertexGeometryOperation.md) | view-operations | 21 |
| [view-operations/DeleteVertexGeometryOperation](DeleteVertexGeometryOperation.md) | view-operations | 19 |
| [view-operations/SplitFeatureGeometryOperation](SplitFeatureGeometryOperation.md) | view-operations | 15 |
| [canvas-tools/MeasureDistance](../canvas-tools/MeasureDistance.md) | canvas-tools | 13 |
| [view-operations/AddPointGeometryOperation](AddPointGeometryOperation.md) | view-operations | 13 |
| [view-operations/InsertVertexGeometryOperation](InsertVertexGeometryOperation.md) | view-operations | 13 |
| [canvas-tools/SelectHellingerGeometries](../canvas-tools/SelectHellingerGeometries.md) | canvas-tools | 8 |
| [view-operations/RenderedGeometryCollection](RenderedGeometryCollection.md) | view-operations | 8 |
| [view-operations/RenderedGeometryProximity](RenderedGeometryProximity.md) | view-operations | 8 |
| [qt-widgets/HellingerDialog](../qt-widgets/HellingerDialog.md) | qt-widgets | 7 |
| [qt-widgets/ModifyReconstructionPoleWidget](../qt-widgets/ModifyReconstructionPoleWidget.md) | qt-widgets | 7 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 6 |
| [canvas-tools/CreateSmallCircle](../canvas-tools/CreateSmallCircle.md) | canvas-tools | 5 |
| [view-operations/RenderedGeometryLayerVisitor](RenderedGeometryLayerVisitor.md) | view-operations | 5 |
| [qt-widgets/HellingerPickWidget](../qt-widgets/HellingerPickWidget.md) | qt-widgets | 4 |
| [gui/GeometryFocusHighlight](../gui/GeometryFocusHighlight.md) | gui | 2 |
| [gui/GlobeRenderedGeometryCollectionPainter](../gui/GlobeRenderedGeometryCollectionPainter.md) | gui | 2 |
| [gui/MapRenderedGeometryCollectionPainter](../gui/MapRenderedGeometryCollectionPainter.md) | gui | 2 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 2 |

*... and 10 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedGeometryLayer.h
python scripts/gpq.py def GPlatesViewOperations::RenderedGeometryLayer --body
python scripts/gpq.py uses RenderedGeometryLayer --kind class
python scripts/gpq.py hier RenderedGeometryLayer
```
