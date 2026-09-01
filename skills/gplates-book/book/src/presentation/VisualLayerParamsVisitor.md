# VisualLayerParamsVisitor

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 189 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/VisualLayerParamsVisitor.h` | C++ | 126 |

## Overview

`VisualLayerParamsVisitorBase` is the visitor-pattern base for dispatching on the concrete subclass of `VisualLayerParams` without a `dynamic_cast` chain. It is parameterised on a `Const` bool so a single template produces both the const and non-const visitor interfaces; `ConstVisualLayerParamsVisitor` and `VisualLayerParamsVisitor` are simply the two instantiations, `VisualLayerParamsVisitorBase<true>` and `VisualLayerParamsVisitorBase<false>`. `GPlatesUtils::SetConst` is used to derive each `visit_*` method's parameter type from `Const`, so the same visitor declarations serve both cases.

Every `visit_*` method has an empty default body, so a concrete visitor only needs to override the handlers for the layer types it actually cares about; unhandled types are silently skipped. `VisualLayerParams::accept_visitor` is the entry point that dispatches to the matching `visit_*` call for a given concrete params object.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPresentation::VisualLayerParamsVisitorBase`](#gplatespresentationvisuallayerparamsvisitorbase) | class | — | `<bool Const>` | 0 | This class is a base class for visitors that visit VisualLayerParams. |
| [`GPlatesPresentation::ConstVisualLayerParamsVisitor`](#gplatespresentationconstvisuallayerparamsvisitor) | typedef | — | — | 2 | This is the base class for visitors that visit const VisualLayerParams. |
| [`GPlatesPresentation::VisualLayerParamsVisitor`](#gplatespresentationvisuallayerparamsvisitor) | typedef | — | — | 1 | This is the base class for visitors that visit non-const VisualLayerParams. |

## Members

### `GPlatesPresentation::VisualLayerParamsVisitorBase`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `raster_visual_layer_params_type` | typedef | `typename GPlatesUtils::SetConst<RasterVisualLayerParams, Const>::type` | public | Typedefs to give the supported derivations the appropriate const-ness. |
| `reconstruct_scalar_coverage_visual_layer_params_type` | typedef | `typename GPlatesUtils::SetConst<ReconstructScalarCoverageVisualLayerParams, Const>::type` | public | — |
| `reconstruct_visual_layer_params_type` | typedef | `typename GPlatesUtils::SetConst<ReconstructVisualLayerParams, Const>::type` | public | — |
| `scalar_field_3d_visual_layer_params_type` | typedef | `typename GPlatesUtils::SetConst<ScalarField3DVisualLayerParams, Const>::type` | public | — |
| `topology_geometry_visual_layer_params_type` | typedef | `typename GPlatesUtils::SetConst<TopologyGeometryVisualLayerParams, Const>::type` | public | — |
| `topology_network_visual_layer_params_type` | typedef | `typename GPlatesUtils::SetConst<TopologyNetworkVisualLayerParams, Const>::type` | public | — |
| `velocity_field_calculator_visual_layer_params_type` | typedef | `typename GPlatesUtils::SetConst<VelocityFieldCalculatorVisualLayerParams, Const>::type` | public | — |
| `~VisualLayerParamsVisitorBase()` | destructor | `None` | public | — |
| `visit_raster_visual_layer_params( raster_visual_layer_params_type &params)` | method | `void` | public | — |
| `visit_reconstruct_scalar_coverage_visual_layer_params( reconstruct_scalar_coverage_visual_layer_params_type &params)` | method | `void` | public | — |
| `visit_reconstruct_visual_layer_params( reconstruct_visual_layer_params_type &params)` | method | `void` | public | — |
| `visit_scalar_field_3d_visual_layer_params( scalar_field_3d_visual_layer_params_type &params)` | method | `void` | public | — |
| `visit_topology_geometry_visual_layer_params( topology_geometry_visual_layer_params_type &params)` | method | `void` | public | — |
| `visit_topology_network_visual_layer_params( topology_network_visual_layer_params_type &params)` | method | `void` | public | — |
| `visit_velocity_field_calculator_visual_layer_params( velocity_field_calculator_visual_layer_params_type &params)` | method | `void` | public | — |
| `VisualLayerParamsVisitorBase()` | constructor | `None` | protected | — |

### `GPlatesPresentation::ConstVisualLayerParamsVisitor`

*None.*

### `GPlatesPresentation::VisualLayerParamsVisitor`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PRESENTATION_VISUALLAYERPARAMSVISITOR_H` | macro | `None` | — |

## Notes

Adding a new visual layer params subclass means adding both a forward declaration and a `visit_*` overload here; nothing in the type system otherwise forces every `VisualLayerParams` derivation to be visitable.

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/TranscribeSession](TranscribeSession.md) | presentation | 21 |
| [presentation/ReconstructionGeometryRenderer](ReconstructionGeometryRenderer.md) | presentation | 9 |
| [presentation/RasterVisualLayerParams](RasterVisualLayerParams.md) | presentation | 4 |
| [presentation/ReconstructScalarCoverageVisualLayerParams](ReconstructScalarCoverageVisualLayerParams.md) | presentation | 4 |
| [presentation/ReconstructVisualLayerParams](ReconstructVisualLayerParams.md) | presentation | 4 |
| [presentation/ScalarField3DVisualLayerParams](ScalarField3DVisualLayerParams.md) | presentation | 4 |
| [presentation/TopologyGeometryVisualLayerParams](TopologyGeometryVisualLayerParams.md) | presentation | 4 |
| [presentation/TopologyNetworkVisualLayerParams](TopologyNetworkVisualLayerParams.md) | presentation | 4 |
| [presentation/VelocityFieldCalculatorVisualLayerParams](VelocityFieldCalculatorVisualLayerParams.md) | presentation | 4 |
| [presentation/VisualLayerParams](VisualLayerParams.md) | presentation | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/presentation/VisualLayerParamsVisitor.h
python scripts/gpq.py def GPlatesPresentation::VisualLayerParamsVisitorBase --body
python scripts/gpq.py uses VisualLayerParamsVisitorBase --kind class
python scripts/gpq.py hier VisualLayerParamsVisitorBase
```
