# LayerParams

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 399 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/LayerParams.h` | C++ | 99 |

## Overview

[[[PROSE overview unit=app-logic/LayerParams tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::LayerParams`](#gplatesapplogiclayerparams) | class | `QObject`<br>[`GPlatesUtils::ReferenceCount<LayerParams>`](../utils/ReferenceCount.md) | — | 8 | This is the base class of classes that store parameters and options specific to particular types of layers (layer task types). |

## Members

### `GPlatesAppLogic::LayerParams`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<LayerParams>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const LayerParams>` | public | — |
| `create()` | method | `non_null_ptr_type` | public | — |
| `~LayerParams()` | destructor | `None` | public | — |
| `accept_visitor( ConstLayerParamsVisitor &visitor)` | method | `void` | public | — |
| `accept_visitor( LayerParamsVisitor &visitor)` | method | `void` | public | — |
| `modified( GPlatesAppLogic::LayerParams &layer_params)` | method | `void` | public | Emitted when any aspect of the parameters has been modified. |
| `emit_modified()` | method | `void` | protected | Subclasses should call this method to cause the modified() signal to be emitted. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_LAYERPARAMS_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/LayerParams tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLVisualLayers](../opengl/GLVisualLayers.md) | opengl | 97 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 59 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 51 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 49 |
| [qt-widgets/ImportRasterDialog](../qt-widgets/ImportRasterDialog.md) | qt-widgets | 43 |
| [app-logic/TopologyGeometryResolverLayerTask](TopologyGeometryResolverLayerTask.md) | app-logic | 34 |
| [gui/FeatureTableModel](../gui/FeatureTableModel.md) | gui | 34 |
| [presentation/VisualLayerRegistry](../presentation/VisualLayerRegistry.md) | presentation | 31 |
| [presentation/TopologyNetworkVisualLayerParams](../presentation/TopologyNetworkVisualLayerParams.md) | presentation | 30 |
| [app-logic/TopologyNetworkResolverLayerTask](TopologyNetworkResolverLayerTask.md) | app-logic | 28 |
| [qt-widgets/CreateVGPDialog](../qt-widgets/CreateVGPDialog.md) | qt-widgets | 28 |
| [app-logic/ReconstructLayerTask](ReconstructLayerTask.md) | app-logic | 27 |
| [presentation/ScalarField3DVisualLayerParams](../presentation/ScalarField3DVisualLayerParams.md) | presentation | 27 |
| [qt-widgets/ImportScalarField3DDialog](../qt-widgets/ImportScalarField3DDialog.md) | qt-widgets | 27 |
| [app-logic/LayerProxyUtils](LayerProxyUtils.md) | app-logic | 26 |
| [qt-widgets/GenerateDeformingMeshPointsDialog](../qt-widgets/GenerateDeformingMeshPointsDialog.md) | qt-widgets | 21 |
| [view-operations/FocusedFeatureGeometryManipulator](../view-operations/FocusedFeatureGeometryManipulator.md) | view-operations | 19 |
| [presentation/ReconstructScalarCoverageVisualLayerParams](../presentation/ReconstructScalarCoverageVisualLayerParams.md) | presentation | 18 |
| [app-logic/ReconstructGraphImpl](ReconstructGraphImpl.md) | app-logic | 16 |
| [qt-widgets/CreateSmallCircleFeatureDialog](../qt-widgets/CreateSmallCircleFeatureDialog.md) | qt-widgets | 16 |

*... and 95 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/LayerParams.h
python scripts/gpq.py def GPlatesAppLogic::LayerParams --body
python scripts/gpq.py uses LayerParams --kind class
python scripts/gpq.py hier LayerParams
```
