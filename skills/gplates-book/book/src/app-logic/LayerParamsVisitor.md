# LayerParamsVisitor

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 189 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/LayerParamsVisitor.h` | C++ | 134 |

## Overview

[[[PROSE overview unit=app-logic/LayerParamsVisitor tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::LayerParamsVisitorBase`](#gplatesapplogiclayerparamsvisitorbase) | class | — | `<bool Const>` | 0 | This class is a base class for visitors that visit LayerParams. |
| [`GPlatesAppLogic::ConstLayerParamsVisitor`](#gplatesapplogicconstlayerparamsvisitor) | typedef | — | — | 1 | This is the base class for visitors that visit const LayerParams. |
| [`GPlatesAppLogic::LayerParamsVisitor`](#gplatesapplogiclayerparamsvisitor) | typedef | — | — | 1 | This is the base class for visitors that visit non-const LayerParams. |

## Members

### `GPlatesAppLogic::LayerParamsVisitorBase`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `co_registration_layer_params_type` | typedef | `typename GPlatesUtils::SetConst<CoRegistrationLayerParams, Const>::type` | public | Typedefs to give the supported derivations the appropriate const-ness. |
| `raster_layer_params_type` | typedef | `typename GPlatesUtils::SetConst<RasterLayerParams, Const>::type` | public | — |
| `reconstruction_layer_params_type` | typedef | `typename GPlatesUtils::SetConst<ReconstructionLayerParams, Const>::type` | public | — |
| `reconstruct_layer_params_type` | typedef | `typename GPlatesUtils::SetConst<ReconstructLayerParams, Const>::type` | public | — |
| `reconstruct_scalar_coverage_layer_params_type` | typedef | `typename GPlatesUtils::SetConst<ReconstructScalarCoverageLayerParams, Const>::type` | public | — |
| `scalar_field_3d_layer_params_type` | typedef | `typename GPlatesUtils::SetConst<ScalarField3DLayerParams, Const>::type` | public | — |
| `topology_network_layer_params_type` | typedef | `typename GPlatesUtils::SetConst<TopologyNetworkLayerParams, Const>::type` | public | — |
| `velocity_field_calculator_layer_params_type` | typedef | `typename GPlatesUtils::SetConst<VelocityFieldCalculatorLayerParams, Const>::type` | public | — |
| `~LayerParamsVisitorBase()` | destructor | `None` | public | — |
| `visit_co_registration_layer_params( co_registration_layer_params_type &params)` | method | `void` | public | — |
| `visit_raster_layer_params( raster_layer_params_type &params)` | method | `void` | public | — |
| `visit_reconstruction_layer_params( reconstruction_layer_params_type &params)` | method | `void` | public | — |
| `visit_reconstruct_layer_params( reconstruct_layer_params_type &params)` | method | `void` | public | — |
| `visit_reconstruct_scalar_coverage_layer_params( reconstruct_scalar_coverage_layer_params_type &params)` | method | `void` | public | — |
| `visit_scalar_field_3d_layer_params( scalar_field_3d_layer_params_type &params)` | method | `void` | public | — |
| `visit_topology_network_layer_params( topology_network_layer_params_type &params)` | method | `void` | public | — |
| `visit_velocity_field_calculator_layer_params( velocity_field_calculator_layer_params_type &params)` | method | `void` | public | — |
| `LayerParamsVisitorBase()` | constructor | `None` | protected | — |

### `GPlatesAppLogic::ConstLayerParamsVisitor`

*None.*

### `GPlatesAppLogic::LayerParamsVisitor`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_LAYERPARAMSVISITOR_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/LayerParamsVisitor tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 19 |
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](../qt-widgets/TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 14 |
| [qt-widgets/VelocityFieldCalculatorLayerOptionsWidget](../qt-widgets/VelocityFieldCalculatorLayerOptionsWidget.md) | qt-widgets | 14 |
| [qt-widgets/ScalarField3DLayerOptionsWidget](../qt-widgets/ScalarField3DLayerOptionsWidget.md) | qt-widgets | 10 |
| [qt-widgets/RasterLayerOptionsWidget](../qt-widgets/RasterLayerOptionsWidget.md) | qt-widgets | 8 |
| [qt-widgets/ReconstructScalarCoverageLayerOptionsWidget](../qt-widgets/ReconstructScalarCoverageLayerOptionsWidget.md) | qt-widgets | 8 |
| [presentation/ReconstructScalarCoverageVisualLayerParams](../presentation/ReconstructScalarCoverageVisualLayerParams.md) | presentation | 6 |
| [qt-widgets/ReconstructLayerOptionsWidget](../qt-widgets/ReconstructLayerOptionsWidget.md) | qt-widgets | 6 |
| [app-logic/CoRegistrationLayerParams](CoRegistrationLayerParams.md) | app-logic | 4 |
| [app-logic/RasterLayerParams](RasterLayerParams.md) | app-logic | 4 |
| [app-logic/RasterLayerProxy](RasterLayerProxy.md) | app-logic | 4 |
| [app-logic/ReconstructLayerParams](ReconstructLayerParams.md) | app-logic | 4 |
| [app-logic/ReconstructScalarCoverageLayerParams](ReconstructScalarCoverageLayerParams.md) | app-logic | 4 |
| [app-logic/ReconstructionLayerParams](ReconstructionLayerParams.md) | app-logic | 4 |
| [app-logic/ScalarField3DLayerParams](ScalarField3DLayerParams.md) | app-logic | 4 |
| [app-logic/TopologyNetworkLayerParams](TopologyNetworkLayerParams.md) | app-logic | 4 |
| [app-logic/VelocityFieldCalculatorLayerParams](VelocityFieldCalculatorLayerParams.md) | app-logic | 4 |
| [qt-widgets/ReconstructionLayerOptionsWidget](../qt-widgets/ReconstructionLayerOptionsWidget.md) | qt-widgets | 4 |
| [qt-widgets/SetTopologyReconstructionParametersDialog](../qt-widgets/SetTopologyReconstructionParametersDialog.md) | qt-widgets | 4 |
| [qt-widgets/SetVGPVisibilityDialog](../qt-widgets/SetVGPVisibilityDialog.md) | qt-widgets | 4 |

*... and 13 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/LayerParamsVisitor.h
python scripts/gpq.py def GPlatesAppLogic::LayerParamsVisitorBase --body
python scripts/gpq.py uses LayerParamsVisitorBase --kind class
python scripts/gpq.py hier LayerParamsVisitorBase
```
