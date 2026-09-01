# RenderedGeometryLayer

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 140 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedGeometryLayer.h` | C++ | 365 |
| `src/view-operations/RenderedGeometryLayer.cc` | C++ | 916 |

## Overview

The leaf container of the rendered-geometry system: one drawable ordering unit,
held either as a main layer's embedded default or as an explicitly created child
of one, and drawn into its own depth layer so its contents never interleave with
another layer's. Its whole outward job is to accumulate `RenderedGeometry` handles
and to shout `layer_was_updated` whenever it changes, carrying back the
`user_data` `boost::any` it was constructed with — which `RenderedGeometryCollection`
uses to stash the owning `MainLayerType` so it can decode which main layer moved.
That `user_data` has no other intended user.

Internally the contents are stored twice, and the reason is that the two consumers
want opposite orderings. A painter that draws the whole layer wants insertion
order, so there is a plain `std::vector<RenderedGeometry>`, exposed through
`get_rendered_geometry` and the forward `RenderedGeometryIterator`. Anything that
wants to cull — view-frustum rejection, proximity picking — wants spatial
locality, so the same handles also go into a
`GPlatesMaths::CubeQuadTreePartition`, and because that partition is sorted
spatially rather than by draw order, each entry is wrapped in a
`PartitionedRenderedGeometry` that remembers its `render_order`. A spatial
traversal can therefore be sorted back into correct draw order, which is exactly
what `copy_rendered_geometries_in_render_order` does. Callers of
`add_rendered_geometry` who already know where their geometry sits in the cube quad
tree pass a `CubeQuadTreeLocation`; everyone else's geometry lands in the
partition's unpartitioned root and gets no spatial acceleration.

The class itself is a thin `QObject` shell over a swappable
`RenderedGeometryLayerImpl`, and the two implementations are the point of the
design. `ZoomIndependentLayerImpl` is the plain append-to-a-vector case.
`ZoomDependentLayerImpl` exists so that a layer full of velocity arrows or sampled
points does not become an unreadable smear when zoomed out: it routes each added
geometry through the `IsZoomDependent` visitor, and anything with a single point
position — currently `RenderedPointOnSphere`, `RenderedRadialArrow` and
`RenderedTangentialArrow` — goes into a `GPlatesUtils::LatLonAreaSampling` that
keeps only the geometry nearest each bin centre, while multipoints, polylines and
polygons take the ordinary path. Bin spacing is recomputed from the ratio and the
viewport zoom factor, so decimation density stays constant on screen as the user
zooms. `set_ratio_zoom_dependent_bin_dimension_to_globe_radius` switches a live
layer between the two implementations by building the new one and copying the
contents across in render order; zero means zoom-independent.

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

- **A new layer is inactive.** `d_is_active` starts false in both constructors,
  so a freshly created child layer draws nothing until `set_active(true)` — and
  even then only while its main layer is active too.
- **`get_rendered_geometries()` is not a getter on a zoom-dependent layer.** If
  the zoom-dependent sequence is non-empty it builds a *new* spatial partition on
  every call: merges the whole zoom-independent partition into it and then appends
  every sampled geometry. Calling it per frame, or once per candidate during
  picking, is a real cost. The zoom-independent implementation, by contrast,
  returns its live partition — which later `add`/`clear` calls will mutate under
  a caller still holding it.
- **The insertion-order guarantee does not survive zoom dependence.** In a
  zoom-dependent layer all zoom-independent geometries are indexed first and keep
  their relative order; the zoom-dependent ones follow, have lost their relative
  order, and some were never stored at all because another geometry already
  occupied their bin. Index-based `get_rendered_geometry` and the iterators
  reflect that. Zoom-dependent geometries also always end up in the *root* of the
  returned partition, so they are never spatially culled.
- **Every mutation signals, including no-ops.** `add_rendered_geometry` and
  `clear_rendered_geometries` emit `layer_was_updated` unconditionally — the
  emptiness check around `clear` was deliberately removed (it is still in the
  source, `#if 0`-ed) so that clearing an already-empty layer still forces a
  canvas refresh. `set_active` is the exception: it only emits on an actual
  change. Batch bulk edits inside a `RenderedGeometryCollection::UpdateGuard`.
- **Some mutations signal nothing.** Neither `set_viewport_zoom_factor` nor
  `set_ratio_zoom_dependent_bin_dimension_to_globe_radius` emits, even though both
  can change what is visible on a zoom-dependent layer and the latter replaces the
  implementation object wholesale. Whoever drives the zoom is expected to trigger
  the redraw.
- **Iterators are index-and-impl pairs, not real iterators.** `operator*`
  dereferences into the implementation's vector, so adding geometries invalidates
  outstanding iterators, and clearing them makes dereference out-of-range.
  `operator==` compares the implementation *pointer* as well as the index, so a
  begin/end pair that straddles an implementation swap will never compare equal.
  They hold an `intrusive_ptr` to the implementation, which keeps the old one
  alive after a swap rather than dangling — an iterator obtained before a swap
  silently keeps walking the discarded contents.
- **Sample spacing is clamped.** `get_zoom_dependent_sample_spacing` floors the
  bin spacing at 0.25 degrees, explicitly to stop the bin count exploding at
  extreme zoom. Past that point the decimation stops tracking zoom.
- **Threading.** `QObject` with direct connections to the owning collection:
  `add_rendered_geometry` runs the collection's slot synchronously inside the call.
  Not thread-safe; GUI thread only.
- The spatial partition depth is fixed at `DEFAULT_SPATIAL_PARTITION_DEPTH` (7)
  for every layer, and the destructor and iterator copy/destroy bodies exist only
  because `boost::intrusive_ptr` needs the complete implementation type.

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
