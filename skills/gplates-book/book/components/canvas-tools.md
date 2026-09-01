# canvas-tools

[Book TOC](../TOC.md)

27 unit page(s), 51 source file(s) documented here, 1 further file(s) listed below.

## Overview

[[[PROSE component unit=component:canvas-tools tier=1]]]
Replace this whole block, markers included, with 2-4 paragraphs: what this component is responsible for, the load-bearing units and how it connects to neighbouring components. Do not restate the unit table.
[[[/PROSE]]]

## Units

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [AdjustFittedPoleEstimate](../src/canvas-tools/AdjustFittedPoleEstimate.md) | 2 | 1284 | 18 | Canvas tool for dragging the Hellinger tool's initial 1-2 and 1-3 pole estimates |
| [BuildTopology](../src/canvas-tools/BuildTopology.md) | 2 | 401 | 38 | Canvas tool for picking features to add as sections of a topological line/boundary/network |
| [CanvasTool](../src/canvas-tools/CanvasTool.md) | 1 | 281 | 534 | view-agnostic base for interactive canvas tools, adapted onto the globe and map canvases |
| [CanvasToolAdapterForGlobe](../src/canvas-tools/CanvasToolAdapterForGlobe.md) | 2 | 622 | 59 | Adapts a widget-agnostic CanvasTool to the GlobeCanvasTool globe event interface |
| [CanvasToolAdapterForMap](../src/canvas-tools/CanvasToolAdapterForMap.md) | 2 | 662 | 23 | Adapts a widget-agnostic CanvasTool to the MapCanvasTool map event interface |
| [ChangeLightDirectionGlobe](../src/canvas-tools/ChangeLightDirectionGlobe.md) | 2 | 460 | 11 | Globe canvas tool for dragging the light-direction arrow |
| [ChangeLightDirectionMap](../src/canvas-tools/ChangeLightDirectionMap.md) | 3 | 132 | 1 | Map canvas tool for changing light direction (currently unimplemented) |
| [ClickGeometry](../src/canvas-tools/ClickGeometry.md) | 2 | 349 | 29 | Default canvas tool for focusing a feature by clicking its geometry |
| [CreateSmallCircle](../src/canvas-tools/CreateSmallCircle.md) | 3 | 334 | 3 | Canvas tool for drawing small circles (geographic circles) on the globe |
| [DeleteVertex](../src/canvas-tools/DeleteVertex.md) | 2 | 236 | 57 | Canvas tool wrapper for deleting a vertex from digitised or focused geometry |
| [DigitiseGeometry](../src/canvas-tools/DigitiseGeometry.md) | 3 | 240 | 3 | Canvas tool for creating new geometries by clicking points interactively |
| [EditTopology](../src/canvas-tools/EditTopology.md) | 3 | 380 | 1 | Canvas tool for selecting features to build plate boundary topologies |
| [GeometryOperationState](../src/canvas-tools/GeometryOperationState.md) | 2 | 165 | 369 | Tracks the single active GeometryOperation and GeometryBuilder, signalling on change |
| [InsertVertex](../src/canvas-tools/InsertVertex.md) | 3 | 258 | 2 | Canvas tool for inserting vertices into existing or temporary geometries |
| [ManipulatePole](../src/canvas-tools/ManipulatePole.md) | 3 | 304 | 3 | Canvas tool for interactively adjusting plate rotation poles via dragging |
| [MeasureDistance](../src/canvas-tools/MeasureDistance.md) | 2 | 825 | 14 | Globe/map canvas tool for Quick Measure and Feature Measure distance display |
| [MeasureDistanceState](../src/canvas-tools/MeasureDistanceState.md) | 2 | 724 | 32 | Shared measurement data and geometry-builder tracking behind the measure distance tool |
| [ModifyGeometryState](../src/canvas-tools/ModifyGeometryState.md) | 3 | 77 | 5 | Signal relay for snap-to-vertices configuration between UI and canvas tools |
| [MovePoleGlobe](../src/canvas-tools/MovePoleGlobe.md) | 3 | 261 | 1 | Canvas tool for repositioning rotation poles on the globe view |
| [MovePoleMap](../src/canvas-tools/MovePoleMap.md) | 3 | 324 | 5 | Map canvas tool for interactive pole manipulation |
| [MoveVertex](../src/canvas-tools/MoveVertex.md) | 3 | 365 | 6 | Canvas tool for interactive vertex editing on the globe |
| [PanMap](../src/canvas-tools/PanMap.md) | 3 | 201 | 1 | Map canvas tool for panning and reorienting the map view |
| [ReorientGlobe](../src/canvas-tools/ReorientGlobe.md) | 3 | 256 | 1 | Globe canvas tool for rotating the 3D globe view |
| [SelectHellingerGeometries](../src/canvas-tools/SelectHellingerGeometries.md) | 3 | 684 | 1 | Canvas tool for selecting geometries to fit a Hellinger rotation pole |
| [SplitFeature](../src/canvas-tools/SplitFeature.md) | 3 | 274 | 3 | Canvas tool for inserting vertices into feature geometry |
| [ZoomGlobe](../src/canvas-tools/ZoomGlobe.md) | 3 | 212 | 1 | Globe canvas tool for zooming into the 3D globe view |
| [ZoomMap](../src/canvas-tools/ZoomMap.md) | 3 | 220 | 1 | Map canvas tool for zooming into the map view |

## Other files

| File | Kind | Lines |
|---|---|---|
| `src/canvas-tools/CMakeLists.txt` | build | 66 |

## Depends on

| Component | References |
|---|---|
| [gui](gui.md) | 799 |
| [view-operations](view-operations.md) | 497 |
| [maths](maths.md) | 390 |
| [qt-widgets](qt-widgets.md) | 275 |
| [app-logic](app-logic.md) | 140 |
| [model](model.md) | 49 |
| [utils](utils.md) | 21 |
| [presentation](presentation.md) | 19 |
| [global](global.md) | 6 |
| [file-io](file-io.md) | 3 |
| [feature-visitors](feature-visitors.md) | 2 |
| [property-values](property-values.md) | 2 |

## Used by

| Component | References |
|---|---|
| [gui](gui.md) | 544 |
| [view-operations](view-operations.md) | 247 |
| [qt-widgets](qt-widgets.md) | 95 |
| [data-mining](data-mining.md) | 3 |
| [opengl](opengl.md) | 3 |

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py tree src/canvas-tools
python scripts/gpq.py sym . --mode sub --path src/canvas-tools --defs-only
```
