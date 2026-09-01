# LayerProxy

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 1671 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/LayerProxy.h` | C++ | 110 |

## Overview

[[[PROSE overview unit=app-logic/LayerProxy tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::LayerProxyHandle`](#gplatesapplogiclayerproxyhandle) | class | [`GPlatesUtils::ReferenceCount<LayerProxyHandle>`](../utils/ReferenceCount.md) | — | 10 | A handle to a layer proxy. |
| [`GPlatesAppLogic::LayerProxy`](#gplatesapplogiclayerproxy) | class | [`LayerProxyHandle`](LayerProxy.md) | — | 9 | Base class for layer proxies. |

## Members

### `GPlatesAppLogic::LayerProxyHandle`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<LayerProxyHandle>` | public | Convenience typedefs for a shared pointer to a LayerProxyHandle. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const LayerProxyHandle>` | public | — |
| `~LayerProxyHandle()` | destructor | `None` | public | — |

### `GPlatesAppLogic::LayerProxy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<LayerProxy>` | public | Convenience typedefs for a shared pointer to a LayerProxy. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const LayerProxy>` | public | — |
| `~LayerProxy()` | destructor | `None` | public | — |
| `accept_visitor( ConstLayerProxyVisitor &visitor)` | method | `void` | public | Accept a ConstLayerProxyVisitor instance. |
| `accept_visitor( LayerProxyVisitor &visitor)` | method | `void` | public | Accept a LayerProxyVisitor instance. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_LAYERPROXY_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/LayerProxy tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/TopologyGeometryResolverLayerProxy](TopologyGeometryResolverLayerProxy.md) | app-logic | 56 |
| [app-logic/ReconstructLayerProxy](ReconstructLayerProxy.md) | app-logic | 45 |
| [app-logic/RasterLayerProxy](RasterLayerProxy.md) | app-logic | 38 |
| [app-logic/TopologyNetworkResolverLayerProxy](TopologyNetworkResolverLayerProxy.md) | app-logic | 38 |
| [opengl/GLVisualLayers](../opengl/GLVisualLayers.md) | opengl | 32 |
| [app-logic/PartitionFeatureUtils](PartitionFeatureUtils.md) | app-logic | 30 |
| [app-logic/ScalarField3DLayerProxy](ScalarField3DLayerProxy.md) | app-logic | 28 |
| [app-logic/TopologyUtils](TopologyUtils.md) | app-logic | 26 |
| [app-logic/DependentTopologicalSectionLayers](DependentTopologicalSectionLayers.md) | app-logic | 25 |
| [feature-visitors/ViewFeatureGeometriesWidgetPopulator](../feature-visitors/ViewFeatureGeometriesWidgetPopulator.md) | feature-visitors | 23 |
| [app-logic/VelocityFieldCalculatorLayerProxy](VelocityFieldCalculatorLayerProxy.md) | app-logic | 21 |
| [app-logic/TopologyNetworkResolver](TopologyNetworkResolver.md) | app-logic | 18 |
| [app-logic/TopologyGeometryResolver](TopologyGeometryResolver.md) | app-logic | 16 |
| [app-logic/deprecated/ReconstructedFeatureGeometryPopulator](deprecated/ReconstructedFeatureGeometryPopulator.md) | app-logic | 16 |
| [app-logic/ReconstructGraphImpl](ReconstructGraphImpl.md) | app-logic | 12 |
| [app-logic/ReconstructScalarCoverageLayerProxy](ReconstructScalarCoverageLayerProxy.md) | app-logic | 12 |
| [app-logic/RasterLayerTask](RasterLayerTask.md) | app-logic | 10 |
| [app-logic/ReconstructionGeometryFinder](ReconstructionGeometryFinder.md) | app-logic | 10 |
| [app-logic/VelocityFieldCalculatorLayerTask](VelocityFieldCalculatorLayerTask.md) | app-logic | 10 |
| [app-logic/ReconstructionLayerProxy](ReconstructionLayerProxy.md) | app-logic | 9 |

*... and 23 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/LayerProxy.h
python scripts/gpq.py def GPlatesAppLogic::LayerProxy --body
python scripts/gpq.py uses LayerProxy --kind class
python scripts/gpq.py hier LayerProxy
```
