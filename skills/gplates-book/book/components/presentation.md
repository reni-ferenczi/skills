# presentation

[Book TOC](../TOC.md)

26 unit page(s), 46 source file(s) documented here, 1 further file(s) listed below.

## Overview

[[[PROSE component unit=component:presentation tier=1]]]
Replace this whole block, markers included, with 2-4 paragraphs: what this component is responsible for, the load-bearing units and how it connects to neighbouring components. Do not restate the unit table.
[[[/PROSE]]]

## Units

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [Application](../src/presentation/Application.md) | 2 | 318 | 8 | (pending) |
| [DeprecatedSessionRestore](../src/presentation/DeprecatedSessionRestore.md) | 3 | 677 | 15 | Backward-compatibility loader for pre-scribe session formats (versions 1–3) |
| [InternalSession](../src/presentation/InternalSession.md) | 2 | 833 | 68 | (pending) |
| [LayerOutputRenderer](../src/presentation/LayerOutputRenderer.md) | 2 | 502 | 20 | (pending) |
| [ProjectSession](../src/presentation/ProjectSession.md) | 2 | 820 | 17 | (pending) |
| [RasterVisualLayerParams](../src/presentation/RasterVisualLayerParams.md) | 2 | 374 | 62 | (pending) |
| [ReconstructScalarCoverageVisualLayerParams](../src/presentation/ReconstructScalarCoverageVisualLayerParams.md) | 2 | 399 | 63 | (pending) |
| [ReconstructVisualLayerParams](../src/presentation/ReconstructVisualLayerParams.md) | 2 | 584 | 143 | (pending) |
| [ReconstructionGeometryRenderer](../src/presentation/ReconstructionGeometryRenderer.md) | 2 | 3019 | 60 | (pending) |
| [RemappedColourPaletteParameters](../src/presentation/RemappedColourPaletteParameters.md) | 2 | 578 | 202 | (pending) |
| [ScalarField3DVisualLayerParams](../src/presentation/ScalarField3DVisualLayerParams.md) | 2 | 627 | 173 | (pending) |
| [Session](../src/presentation/Session.md) | 2 | 335 | 11 | (pending) |
| [SessionManagement](../src/presentation/SessionManagement.md) | 2 | 1316 | 20 | (pending) |
| [TopologyGeometryVisualLayerParams](../src/presentation/TopologyGeometryVisualLayerParams.md) | 2 | 157 | 16 | (pending) |
| [TopologyNetworkVisualLayerParams](../src/presentation/TopologyNetworkVisualLayerParams.md) | 2 | 796 | 223 | (pending) |
| [TranscribeSession](../src/presentation/TranscribeSession.md) | 2 | 3805 | 153 | (pending) |
| [VelocityFieldCalculatorVisualLayerParams](../src/presentation/VelocityFieldCalculatorVisualLayerParams.md) | 2 | 146 | 31 | (pending) |
| [ViewState](../src/presentation/ViewState.md) | 1 | 1174 | 1718 | (pending) |
| [VisualLayer](../src/presentation/VisualLayer.md) | 1 | 642 | 490 | (pending) |
| [VisualLayerGroup](../src/presentation/VisualLayerGroup.md) | 3 | 57 | 30 | Enumeration of visual layer categories controlling on-screen organization |
| [VisualLayerInputChannelName](../src/presentation/VisualLayerInputChannelName.md) | 3 | 154 | 1 | Mapping from layer input channel enumerations to GUI display strings |
| [VisualLayerParams](../src/presentation/VisualLayerParams.md) | 2 | 167 | 64 | (pending) |
| [VisualLayerParamsVisitor](../src/presentation/VisualLayerParamsVisitor.md) | 2 | 126 | 57 | (pending) |
| [VisualLayerRegistry](../src/presentation/VisualLayerRegistry.md) | 2 | 880 | 59 | (pending) |
| [VisualLayerType](../src/presentation/VisualLayerType.md) | 2 | 47 | 59 | (pending) |
| [VisualLayers](../src/presentation/VisualLayers.md) | 2 | 1321 | 58 | (pending) |

## Other files

| File | Kind | Lines |
|---|---|---|
| `src/presentation/CMakeLists.txt` | build | 61 |

## Depends on

| Component | References |
|---|---|
| [app-logic](app-logic.md) | 2072 |
| [gui](gui.md) | 1315 |
| [scribe](scribe.md) | 686 |
| [view-operations](view-operations.md) | 326 |
| [global](global.md) | 281 |
| [api](api.md) | 277 |
| [utils](utils.md) | 238 |
| [maths](maths.md) | 219 |
| [data-mining](data-mining.md) | 142 |
| [property-values](property-values.md) | 118 |
| [model](model.md) | 92 |
| [qt-widgets](qt-widgets.md) | 64 |
| [file-io](file-io.md) | 60 |
| [opengl](opengl.md) | 49 |
| [feature-visitors](feature-visitors.md) | 3 |

## Used by

| Component | References |
|---|---|
| [qt-widgets](qt-widgets.md) | 2350 |
| [gui](gui.md) | 566 |
| [view-operations](view-operations.md) | 80 |
| [app-logic](app-logic.md) | 25 |
| [canvas-tools](canvas-tools.md) | 19 |
| [api](api.md) | 15 |
| [opengl](opengl.md) | 6 |
| [data-mining](data-mining.md) | 2 |
| [entry-points](entry-points.md) | 2 |
| [cli](cli.md) | 1 |

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py tree src/presentation
python scripts/gpq.py sym . --mode sub --path src/presentation --defs-only
```
