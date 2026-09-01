# LayerProxyVisitor

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 601 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/LayerProxyVisitor.h` | C++ | 230 |

## Overview

[[[PROSE overview unit=app-logic/LayerProxyVisitor tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::LayerProxyVisitor`](#gplatesapplogiclayerproxyvisitor) | typedef | — | — | 1 | Typedef for visitor over non-const LayerProxy objects. |
| [`GPlatesAppLogic::ConstLayerProxyVisitor`](#gplatesapplogicconstlayerproxyvisitor) | typedef | — | — | 0 | Typedef for visitor over const LayerProxy objects. |
| [`GPlatesAppLogic::LayerProxyVisitorBase`](#gplatesapplogiclayerproxyvisitorbase) | class | — | `<class LayerProxyType>` | 1 | This class defines an abstract interface for a Visitor to visit layer proxy objects. |

## Members

### `GPlatesAppLogic::LayerProxyVisitor`

*None.*

### `GPlatesAppLogic::ConstLayerProxyVisitor`

*None.*

### `GPlatesAppLogic::LayerProxyVisitorBase`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `co_registration_layer_proxy_type` | typedef | `typename GPlatesUtils::CopyConst< LayerProxyType, CoRegistrationLayerProxy>::type` | public | Typedef for CoRegistrationLayerProxy of appropriate const-ness. |
| `raster_layer_proxy_type` | typedef | `typename GPlatesUtils::CopyConst< LayerProxyType, RasterLayerProxy>::type` | public | Typedef for RasterLayerProxy of appropriate const-ness. |
| `reconstruct_layer_proxy_type` | typedef | `typename GPlatesUtils::CopyConst< LayerProxyType, ReconstructLayerProxy>::type` | public | Typedef for ReconstructLayerProxy of appropriate const-ness. |
| `reconstruct_scalar_coverage_layer_proxy_type` | typedef | `typename GPlatesUtils::CopyConst< LayerProxyType, ReconstructScalarCoverageLayerProxy>::type` | public | Typedef for ReconstructScalarCoverageLayerProxy of appropriate const-ness. |
| `reconstruction_layer_proxy_type` | typedef | `typename GPlatesUtils::CopyConst< LayerProxyType, ReconstructionLayerProxy>::type` | public | Typedef for ReconstructionLayerProxy of appropriate const-ness. |
| `scalar_field_3d_layer_proxy_type` | typedef | `typename GPlatesUtils::CopyConst< LayerProxyType, ScalarField3DLayerProxy>::type` | public | Typedef for ScalarField3DLayerProxy of appropriate const-ness. |
| `topology_geometry_resolver_layer_proxy_type` | typedef | `typename GPlatesUtils::CopyConst< LayerProxyType, TopologyGeometryResolverLayerProxy>::type` | public | Typedef for TopologyGeometryResolverLayerProxy of appropriate const-ness. |
| `topology_network_resolver_layer_proxy_type` | typedef | `typename GPlatesUtils::CopyConst< LayerProxyType, TopologyNetworkResolverLayerProxy>::type` | public | Typedef for TopologyNetworkResolverLayerProxy of appropriate const-ness. |
| `velocity_field_calculator_layer_proxy_type` | typedef | `typename GPlatesUtils::CopyConst< LayerProxyType, VelocityFieldCalculatorLayerProxy>::type` | public | Typedef for VelocityFieldCalculatorLayerProxy of appropriate const-ness. |
| `~LayerProxyVisitorBase()` | destructor | `None` | public | We'll make this function pure virtual so that the class is abstract. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<co_registration_layer_proxy_type> &layer_proxy)` | method | `void` | public | Override this function in your own derived class. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<raster_layer_proxy_type> &layer_proxy)` | method | `void` | public | Override this function in your own derived class. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstruct_layer_proxy_type> &layer_proxy)` | method | `void` | public | Override this function in your own derived class. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstruct_scalar_coverage_layer_proxy_type> &layer_proxy)` | method | `void` | public | Override this function in your own derived class. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstruction_layer_proxy_type> &layer_proxy)` | method | `void` | public | Override this function in your own derived class. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<scalar_field_3d_layer_proxy_type> &layer_proxy)` | method | `void` | public | Override this function in your own derived class. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<topology_geometry_resolver_layer_proxy_type> &layer_proxy)` | method | `void` | public | Override this function in your own derived class. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<topology_network_resolver_layer_proxy_type> &layer_proxy)` | method | `void` | public | Override this function in your own derived class. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<velocity_field_calculator_layer_proxy_type> &layer_proxy)` | method | `void` | public | Override this function in your own derived class. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_LAYERPROXYVISITOR_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/LayerProxyVisitor tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLVisualLayers](../opengl/GLVisualLayers.md) | opengl | 23 |
| [presentation/LayerOutputRenderer](../presentation/LayerOutputRenderer.md) | presentation | 21 |
| [app-logic/TopologyGeometryResolverLayerTask](TopologyGeometryResolverLayerTask.md) | app-logic | 17 |
| [app-logic/ReconstructLayerTask](ReconstructLayerTask.md) | app-logic | 15 |
| [app-logic/ResolvedRaster](ResolvedRaster.md) | app-logic | 15 |
| [app-logic/LayerProxyUtils](LayerProxyUtils.md) | app-logic | 10 |
| [app-logic/RasterLayerTask](RasterLayerTask.md) | app-logic | 10 |
| [app-logic/ScalarField3DLayerTask](ScalarField3DLayerTask.md) | app-logic | 10 |
| [app-logic/VelocityFieldCalculatorLayerTask](VelocityFieldCalculatorLayerTask.md) | app-logic | 10 |
| [app-logic/ScalarField3DLayerProxy](ScalarField3DLayerProxy.md) | app-logic | 8 |
| [app-logic/VelocityFieldCalculatorLayerProxy](VelocityFieldCalculatorLayerProxy.md) | app-logic | 8 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 8 |
| [app-logic/Reconstruction](Reconstruction.md) | app-logic | 7 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 6 |
| [app-logic/CoRegistrationLayerProxy](CoRegistrationLayerProxy.md) | app-logic | 5 |
| [app-logic/ReconstructLayerProxy](ReconstructLayerProxy.md) | app-logic | 5 |
| [app-logic/TopologyGeometryResolverLayerProxy](TopologyGeometryResolverLayerProxy.md) | app-logic | 5 |
| [gui/ExportScalarCoverageAnimationStrategy](../gui/ExportScalarCoverageAnimationStrategy.md) | gui | 5 |
| [gui/ExportVelocityAnimationStrategy](../gui/ExportVelocityAnimationStrategy.md) | gui | 5 |
| [app-logic/ReconstructGraph](ReconstructGraph.md) | app-logic | 4 |

*... and 14 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/LayerProxyVisitor.h
python scripts/gpq.py def GPlatesAppLogic::LayerProxyVisitorBase --body
python scripts/gpq.py uses LayerProxyVisitorBase --kind class
python scripts/gpq.py hier LayerProxyVisitorBase
```
