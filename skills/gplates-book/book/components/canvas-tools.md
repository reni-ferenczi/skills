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
| [AdjustFittedPoleEstimate](../src/canvas-tools/AdjustFittedPoleEstimate.md) | 2 | 1284 | 18 | (pending) |
| [BuildTopology](../src/canvas-tools/BuildTopology.md) | 2 | 401 | 38 | (pending) |
| [CanvasTool](../src/canvas-tools/CanvasTool.md) | 1 | 281 | 534 | (pending) |
| [CanvasToolAdapterForGlobe](../src/canvas-tools/CanvasToolAdapterForGlobe.md) | 2 | 622 | 59 | (pending) |
| [CanvasToolAdapterForMap](../src/canvas-tools/CanvasToolAdapterForMap.md) | 2 | 662 | 23 | (pending) |
| [ChangeLightDirectionGlobe](../src/canvas-tools/ChangeLightDirectionGlobe.md) | 2 | 460 | 11 | (pending) |
| [ChangeLightDirectionMap](../src/canvas-tools/ChangeLightDirectionMap.md) | 3 | 132 | 1 | (pending) |
| [ClickGeometry](../src/canvas-tools/ClickGeometry.md) | 2 | 349 | 29 | (pending) |
| [CreateSmallCircle](../src/canvas-tools/CreateSmallCircle.md) | 3 | 334 | 3 | (pending) |
| [DeleteVertex](../src/canvas-tools/DeleteVertex.md) | 2 | 236 | 57 | (pending) |
| [DigitiseGeometry](../src/canvas-tools/DigitiseGeometry.md) | 3 | 240 | 3 | (pending) |
| [EditTopology](../src/canvas-tools/EditTopology.md) | 3 | 380 | 1 | (pending) |
| [GeometryOperationState](../src/canvas-tools/GeometryOperationState.md) | 2 | 165 | 369 | (pending) |
| [InsertVertex](../src/canvas-tools/InsertVertex.md) | 3 | 258 | 2 | (pending) |
| [ManipulatePole](../src/canvas-tools/ManipulatePole.md) | 3 | 304 | 3 | (pending) |
| [MeasureDistance](../src/canvas-tools/MeasureDistance.md) | 2 | 825 | 14 | (pending) |
| [MeasureDistanceState](../src/canvas-tools/MeasureDistanceState.md) | 2 | 724 | 32 | (pending) |
| [ModifyGeometryState](../src/canvas-tools/ModifyGeometryState.md) | 3 | 77 | 5 | (pending) |
| [MovePoleGlobe](../src/canvas-tools/MovePoleGlobe.md) | 3 | 261 | 1 | (pending) |
| [MovePoleMap](../src/canvas-tools/MovePoleMap.md) | 3 | 324 | 5 | (pending) |
| [MoveVertex](../src/canvas-tools/MoveVertex.md) | 3 | 365 | 6 | (pending) |
| [PanMap](../src/canvas-tools/PanMap.md) | 3 | 201 | 1 | (pending) |
| [ReorientGlobe](../src/canvas-tools/ReorientGlobe.md) | 3 | 256 | 1 | (pending) |
| [SelectHellingerGeometries](../src/canvas-tools/SelectHellingerGeometries.md) | 3 | 684 | 1 | (pending) |
| [SplitFeature](../src/canvas-tools/SplitFeature.md) | 3 | 274 | 3 | (pending) |
| [ZoomGlobe](../src/canvas-tools/ZoomGlobe.md) | 3 | 212 | 1 | (pending) |
| [ZoomMap](../src/canvas-tools/ZoomMap.md) | 3 | 220 | 1 | (pending) |

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
