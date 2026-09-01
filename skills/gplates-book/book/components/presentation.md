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
| [Application](../src/presentation/Application.md) | 2 | 318 | 8 | Singleton owning ApplicationState, ViewState and ViewportWindow, wiring them together at startup |
| [DeprecatedSessionRestore](../src/presentation/DeprecatedSessionRestore.md) | 3 | 677 | 15 | Backward-compatibility loader for pre-scribe session formats (versions 1–3) |
| [InternalSession](../src/presentation/InternalSession.md) | 2 | 833 | 68 | Session saved to the user preferences store, spanning three on-disk format generations |
| [LayerOutputRenderer](../src/presentation/LayerOutputRenderer.md) | 2 | 502 | 20 | Layer-proxy visitor that hands each layer's output to ReconstructionGeometryRenderer for drawing |
| [ProjectSession](../src/presentation/ProjectSession.md) | 2 | 820 | 17 | Session saved to a project archive file, tracking moved files and unsaved-state changes |
| [RasterVisualLayerParams](../src/presentation/RasterVisualLayerParams.md) | 2 | 374 | 62 | Presentation-side settings for a raster layer: palette, opacity, intensity, relief scale |
| [ReconstructScalarCoverageVisualLayerParams](../src/presentation/ReconstructScalarCoverageVisualLayerParams.md) | 2 | 399 | 63 | Per-scalar-type colour palettes for a reconstruct-scalar-coverage layer, created lazily |
| [ReconstructVisualLayerParams](../src/presentation/ReconstructVisualLayerParams.md) | 2 | 584 | 143 | Visual settings for a reconstruct layer: VGP visibility, fill styling, topology display options |
| [ReconstructionGeometryRenderer](../src/presentation/ReconstructionGeometryRenderer.md) | 2 | 3019 | 60 | Visitor turning any ReconstructionGeometry into RenderedGeometry, driven by a RenderParams config |
| [RemappedColourPaletteParameters](../src/presentation/RemappedColourPaletteParameters.md) | 2 | 578 | 202 | A real-valued colour palette plus an optional remapped input range |
| [ScalarField3DVisualLayerParams](../src/presentation/ScalarField3DVisualLayerParams.md) | 2 | 627 | 173 | Display settings for a scalar-field-3D layer, lazily seeded from field statistics |
| [Session](../src/presentation/Session.md) | 2 | 335 | 11 | Abstract base for a saved GPlates session's timestamp, files and description |
| [SessionManagement](../src/presentation/SessionManagement.md) | 2 | 1316 | 20 | Owns recent-session and project persistence: file lists and layer state across restarts |
| [TopologyGeometryVisualLayerParams](../src/presentation/TopologyGeometryVisualLayerParams.md) | 2 | 157 | 16 | Fill display options for a resolved-topological-geometry layer |
| [TopologyNetworkVisualLayerParams](../src/presentation/TopologyNetworkVisualLayerParams.md) | 2 | 796 | 223 | Triangulation draw/colour modes and strain-rate colour palettes for a network layer |
| [TranscribeSession](../src/presentation/TranscribeSession.md) | 2 | 3805 | 153 | Scribe-based save/load of an entire GPlates session: files, layers, params, view state |
| [VelocityFieldCalculatorVisualLayerParams](../src/presentation/VelocityFieldCalculatorVisualLayerParams.md) | 2 | 146 | 31 | Arrow body scale, arrowhead scale and spacing for a velocity-field-calculator layer |
| [ViewState](../src/presentation/ViewState.md) | 1 | 1174 | 1718 | the presentation-tier state hub owning all non-widget display state, between ApplicationState and ViewportWindow |
| [VisualLayer](../src/presentation/VisualLayer.md) | 1 | 642 | 490 | presentation counterpart of one ReconstructGraph layer; turns its output into rendered geometry |
| [VisualLayerGroup](../src/presentation/VisualLayerGroup.md) | 3 | 57 | 30 | Enumeration of visual layer categories controlling on-screen organization |
| [VisualLayerInputChannelName](../src/presentation/VisualLayerInputChannelName.md) | 3 | 154 | 1 | Mapping from layer input channel enumerations to GUI display strings |
| [VisualLayerParams](../src/presentation/VisualLayerParams.md) | 2 | 167 | 64 | Base class for per-visual-layer-type display parameters, kept separate from app-logic LayerParams |
| [VisualLayerParamsVisitor](../src/presentation/VisualLayerParamsVisitor.md) | 2 | 126 | 57 | Const/non-const visitor base for dispatching on the concrete VisualLayerParams subclass |
| [VisualLayerRegistry](../src/presentation/VisualLayerRegistry.md) | 2 | 880 | 59 | Lookup table of display metadata and factory functions for each registered visual layer type |
| [VisualLayerType](../src/presentation/VisualLayerType.md) | 2 | 47 | 59 | Typedef alias of GPlatesAppLogic::LayerTaskType::Type used by presentation-layer code |
| [VisualLayers](../src/presentation/VisualLayers.md) | 2 | 1321 | 58 | Mirrors ReconstructGraph's layers as VisualLayer objects and manages their draw order |

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
