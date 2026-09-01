# presentation

[Book TOC](../TOC.md)

26 unit page(s), 46 source file(s) documented here, 1 further file(s) listed below.

## Overview

`presentation` is the middle tier of GPlates' three-tier state stack: it holds everything that describes *how* the reconstructed model is displayed without itself computing any plate motion or owning any widget. `Application` builds the stack at startup — `ApplicationState`, then `ViewState`, then `ViewportWindow`, in that order, each depending only on what came before — and wires cross-cutting behaviour (focused-feature routing, the anchored-plate-id and create-feature dialogs feeding back into `ApplicationState::reconstruct()`) that neither the app-logic nor the widget layer should have to know about. `ViewState` is the hub of the tier: it owns `RenderedGeometryCollection`, `VisualLayers`, `FeatureFocus`, viewport zoom and projection, colour-scheme machinery and the visual layer/export-animation registries, all assembled through a fixed constructor dependency graph where member declaration order is load-bearing.

The component's other main job is turning app-logic's pull-model output into drawable geometry. `VisualLayers` mirrors `ReconstructGraph`'s layers one-to-one with `VisualLayer` objects, reacting to layer-lifecycle signals so the two collections never drift apart; each `VisualLayer` holds the presentation-only decisions app-logic has no business making — visibility, name, expanded UI state, and a type-specific `VisualLayerParams` — and calls into a shared `ReconstructionGeometryRenderer` to convert its layer's current output into `RenderedGeometry`. `LayerOutputRenderer` is the visitor that bridges the two: it knows each concrete `LayerProxy`'s interface so `ReconstructionGeometryRenderer` only has to know how to render `ReconstructionGeometry` values, regardless of whether they came from a raster, a resolved topology or network, a scalar field, or a reconstructed feature geometry. `VisualLayerParams` and its dozen concrete subclasses (`RasterVisualLayerParams`, `ReconstructVisualLayerParams`, `ReconstructScalarCoverageVisualLayerParams`, `TopologyNetworkVisualLayerParams`, `ScalarField3DVisualLayerParams`, and others) carry each layer type's own colouring, opacity and display-mode settings, dispatched without `dynamic_cast` chains through `VisualLayerParamsVisitor`; several of them share `RemappedColourPaletteParameters`, which separates a loaded colour palette from an optional user-chosen input range and lazily seeds that range from field statistics the first time real data is available. `VisualLayerRegistry` ties a `VisualLayerType` to its display metadata and its three factory functions (app-logic layer, options widget, params object), so Qt widgets such as `AddNewLayerDialog` never switch on layer type themselves.

The remaining load-bearing group is session persistence: `Session` is the abstract base for a saved set of loaded files and a description, with `InternalSession` (state kept in the `UserPreferences` store, across three on-disk format generations back to a `DeprecatedSessionRestore` path for pre-`Scribe` files) and `ProjectSession` (a standalone `.gproj` archive that can be moved or copied independently of the data it references) as the two concrete forms. Both delegate the actual transcription of layers, params, draw styles and view state to `TranscribeSession`, which dispatches through save/load visitor pairs onto the same `LayerParams`/`VisualLayerParams` subclasses the rendering path uses. `SessionManagement` sits above all of this, owning the recent-sessions list and the project-file workflow that the GUI's Recent Sessions menu and File menu drive.

`presentation` depends heavily on `app-logic` for the `ReconstructGraph`, layer proxies and reconstruction geometries it renders, on `gui` for colour palettes, symbols and draw styles, and on `scribe` for the transcription framework `TranscribeSession` builds on; smaller dependencies reach into `view-operations` for scalar-field render parameters, `maths` and `property-values` for the geometry and value types being rendered, and `data-mining` for co-registration results. In the other direction, `qt-widgets` is overwhelmingly the biggest consumer — nearly every options widget and dialog reads or edits a `VisualLayerParams`, a `VisualLayer` or `ViewState` — followed by `gui`, which reaches back in for the same visual layer and view-state objects it helped populate, and `view-operations` and `canvas-tools`, which query `VisualLayers` and `ViewState` while the user interacts with the globe and map.

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
