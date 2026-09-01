# LayerOutputRenderer

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 517 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/LayerOutputRenderer.h` | C++ | 109 |
| `src/presentation/LayerOutputRenderer.cc` | C++ | 393 |

## Overview

[[[PROSE overview unit=presentation/LayerOutputRenderer tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=presentation/LayerOutputRenderer tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
