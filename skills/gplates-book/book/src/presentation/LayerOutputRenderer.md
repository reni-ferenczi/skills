# LayerOutputRenderer

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 517 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/LayerOutputRenderer.h` | C++ | 109 |
| `src/presentation/LayerOutputRenderer.cc` | C++ | 393 |

## Overview

`LayerOutputRenderer` is the bridge between the app-logic layer proxies and
the rendering pipeline: it implements `GPlatesAppLogic::LayerProxyVisitor` so
it can be dispatched to whichever concrete `LayerProxy` a layer exposes
(`raster_layer_proxy_type`, `reconstruct_layer_proxy_type`,
`scalar_field_3d_layer_proxy_type`, the topology and velocity proxies, and so
on), pulls that proxy's type-specific output for the current reconstruction
time (a `ResolvedRaster`, a spatial partition of
`ReconstructedFeatureGeometry`, a `ResolvedScalarField3D`, ...), and hands each
result to a shared `ReconstructionGeometryRenderer` to turn into
`RenderedGeometry` objects in a `RenderedGeometryLayer`. It exists so that the
knowledge of each layer proxy's specific interface stays here, while
`ReconstructionGeometryRenderer` only has to know how to render
`ReconstructionGeometry` types. Some layer kinds — co-registration and the
bare reconstruction-tree layer — have nothing to visualise, so their `visit()`
overrides are empty.

The anonymous-namespace helpers exist solely to support the
`reconstruct_layer_proxy_type` case: `render_in_transform_sorted_order()`
sorts the reconstructed feature geometries by their `ReconstructMethodFiniteRotation`
(effectively by plate id) before rendering, using
`ReconstructedFeatureGeometrySpatialPartitionInfo` and
`ReconstructedFeatureGeometryRenderOrder` as intermediate bookkeeping. This
gives a stable, deterministic render order — rather than spatial-partition
traversal order — so that overlapping polygons draw consistently from one
frame to the next.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPresentation::(anonymous)::reconstructed_feature_geometries_spatial_partition_type`](#gplatespresentationanonymousreconstructed_feature_geometries_spatial_partition_type) | typedef | — | — | 0 | Convenience typedef. |
| [`GPlatesPresentation::(anonymous)::ReconstructedFeatureGeometrySpatialPartitionInfo`](#gplatespresentationanonymousreconstructedfeaturegeometryspatialpartitioninfo) | struct | — | — | 0 | Information associating a ReconstructedFeatureGeometry with its location in a spatial partition. |
| [`GPlatesPresentation::(anonymous)::ReconstructedFeatureGeometryRenderOrder`](#gplatespresentationanonymousreconstructedfeaturegeometryrenderorder) | struct | — | — | 0 | Helper structure to sort rendered geometries in their render order. |
| [`GPlatesPresentation::LayerOutputRenderer`](#gplatespresentationlayeroutputrenderer) | class | [`GPlatesAppLogic::LayerProxyVisitor`](../app-logic/LayerProxyVisitor.md) | — | 0 | Visits the output of layers (the layer proxy objects) and renders their outputs to a RenderedGeometryLayer using a ReconstructionGeometryRenderer object. |

## Members

### `GPlatesPresentation::(anonymous)::reconstructed_feature_geometries_spatial_partition_type`

*None.*

### `GPlatesPresentation::(anonymous)::ReconstructedFeatureGeometrySpatialPartitionInfo`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ReconstructedFeatureGeometrySpatialPartitionInfo( const GPlatesAppLogic::ReconstructedFeatureGeometry::non_null_ptr_type &rfg_, const reconstructed_feature_geometries_spatial_partition_type::location_type &rfg_spatial_partition_location_)` | constructor | `None` | public | — |
| `rfg` | field | `GPlatesAppLogic::ReconstructedFeatureGeometry::non_null_ptr_type` | public | — |
| `rfg_spatial_partition_location` | field | `reconstructed_feature_geometries_spatial_partition_type::location_type` | public | — |

### `GPlatesPresentation::(anonymous)::ReconstructedFeatureGeometryRenderOrder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ReconstructedFeatureGeometryRenderOrder( unsigned int rfg_spatial_partition_info_index_, const boost::optional<const GPlatesAppLogic::ReconstructMethodFiniteRotation &> &rfg_transform_)` | constructor | `None` | public | — |
| `rfg_spatial_partition_info_index` | field | `unsigned int` | public | — |
| `rfg_transform` | field | `boost::optional<const GPlatesAppLogic::ReconstructMethodFiniteRotation &>` | public | Note that the boost::optional contains a reference since we don't want to sort by pointer. |
| `SortTransform` | struct | `None` | public | Used to sort by transform. |

### `GPlatesPresentation::LayerOutputRenderer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LayerOutputRenderer( ReconstructionGeometryRenderer &reconstruction_geometry_renderer, GPlatesViewOperations::RenderedGeometryLayer &rendered_geometry_layer)` | constructor | `None` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<co_registration_layer_proxy_type> &layer_proxy)` | method | `void` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<raster_layer_proxy_type> &layer_proxy)` | method | `void` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstruct_layer_proxy_type> &layer_proxy)` | method | `void` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstruct_scalar_coverage_layer_proxy_type> &layer_proxy)` | method | `void` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstruction_layer_proxy_type> &layer_proxy)` | method | `void` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<scalar_field_3d_layer_proxy_type> &layer_proxy)` | method | `void` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<topology_geometry_resolver_layer_proxy_type> &layer_proxy)` | method | `void` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<topology_network_resolver_layer_proxy_type> &layer_proxy)` | method | `void` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<velocity_field_calculator_layer_proxy_type> &layer_proxy)` | method | `void` | public | — |
| `d_reconstruction_geometry_renderer` | field | `ReconstructionGeometryRenderer` | private | — |
| `d_rendered_geometry_layer` | field | `GPlatesViewOperations::RenderedGeometryLayer` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `render_in_transform_sorted_order( ReconstructionGeometryRenderer &reconstruction_geometry_renderer, const reconstructed_feature_geometries_spatial_partition_type &rfg_spatial_partition)` | function | `void` | Sort the RFGs by transform (essentially by plate id) and render them in that order. |
| `GPLATES_PRESENTATION_LAYEROUTPUTRENDERER_H` | macro | `None` | — |

## Notes

The `ReconstructionGeometryRenderer &` and `RenderedGeometryLayer &` are held
by reference, not owned; the caller must keep both alive for the lifetime of
the visitor. Each `visit()` override brackets its work in
`ReconstructionGeometryRenderer::begin_render()` / `end_render()`, so a new
`LayerOutputRenderer` (or a re-run of `visit()`) is needed per rendering pass
rather than accumulating state across calls. `ReconstructedFeatureGeometryRenderOrder::rfg_transform`
deliberately wraps a `boost::optional` around a *reference* rather than a
pointer specifically so the `SortTransform` comparator sorts by the
transform's value, not by address.

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/VisualLayer](VisualLayer.md) | presentation | 11 |
| [app-logic/ReconstructLayerProxy](../app-logic/ReconstructLayerProxy.md) | app-logic | 2 |
| [data-mining/LookupReducer](../data-mining/LookupReducer.md) | data-mining | 2 |
| [opengl/GLRasterCoRegistration](../opengl/GLRasterCoRegistration.md) | opengl | 2 |
| [api/CoReg](../api/CoReg.md) | api | 1 |
| [api/PyFunctions](../api/PyFunctions.md) | api | 1 |
| [app-logic/GeometryCookieCutter](../app-logic/GeometryCookieCutter.md) | app-logic | 1 |
| [cli/CliReconstructCommand](../cli/CliReconstructCommand.md) | cli | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/presentation/LayerOutputRenderer.h
python scripts/gpq.py def GPlatesPresentation::LayerOutputRenderer --body
python scripts/gpq.py uses LayerOutputRenderer --kind class
python scripts/gpq.py hier LayerOutputRenderer
```
