# view-operations

[Book TOC](../TOC.md)

57 unit page(s), 82 source file(s) documented here, 1 further file(s) listed below.

## Overview

[[[PROSE component unit=component:view-operations tier=1]]]
Replace this whole block, markers included, with 2-4 paragraphs: what this component is responsible for, the load-bearing units and how it connects to neighbouring components. Do not restate the unit table.
[[[/PROSE]]]

## Units

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [AddPointGeometryOperation](../src/view-operations/AddPointGeometryOperation.md) | 3 | 571 | 4 | Responds to user clicks to add points to digitized geometry |
| [ChangeLightDirectionOperation](../src/view-operations/ChangeLightDirectionOperation.md) | 2 | 433 | 10 | Drag-driven canvas-tool backend for repositioning the globe's light direction |
| [CloneOperation](../src/view-operations/CloneOperation.md) | 3 | 244 | 1 | Duplicates the focused feature or just its geometry |
| [DeleteFeatureOperation](../src/view-operations/DeleteFeatureOperation.md) | 3 | 130 | 0 | Removes the currently focused feature from its parent collection |
| [DeleteVertexGeometryOperation](../src/view-operations/DeleteVertexGeometryOperation.md) | 3 | 692 | 7 | Responds to user clicks on vertices to delete them |
| [FocusedFeatureGeometryManipulator](../src/view-operations/FocusedFeatureGeometryManipulator.md) | 3 | 728 | 0 | Bridges geometry editing in GeometryBuilder back to the feature model |
| [GeometryBuilder](../src/view-operations/GeometryBuilder.md) | 1 | 1901 | 555 | (pending) |
| [GeometryBuilderUndoCommands](../src/view-operations/GeometryBuilderUndoCommands.md) | 2 | 473 | 5 | QUndoCommand wrappers around GeometryBuilder point/type edits for the digitisation undo stack |
| [GeometryOperation](../src/view-operations/GeometryOperation.md) | 2 | 209 | 19 | Abstract base and highlight-signal plumbing shared by the canvas-tool geometry-editing operations |
| [GeometryOperationUndo](../src/view-operations/GeometryOperationUndo.md) | 3 | 225 | 5 | Coordinates undo/redo for geometry operations and canvas tool state |
| [InsertVertexGeometryOperation](../src/view-operations/InsertVertexGeometryOperation.md) | 2 | 1111 | 13 | Insert-Vertex canvas tool: projects clicks onto line segments or appends at the nearer end |
| [InternalGeometryBuilder](../src/view-operations/InternalGeometryBuilder.md) | 2 | 308 | 28 | Lazily rebuilds a GeometryOnSphere from a raw point sequence, falling back to simpler types |
| [MovePoleOperation](../src/view-operations/MovePoleOperation.md) | 2 | 580 | 28 | Move-Pole canvas tool backend, dragging a MovePoleWidget's pole on both globe and map views |
| [MoveVertexGeometryOperation](../src/view-operations/MoveVertexGeometryOperation.md) | 2 | 1149 | 21 | Move-Vertex canvas tool: drags a selected vertex and searches nearby features for snap targets |
| [QueryProximityThreshold](../src/view-operations/QueryProximityThreshold.md) | 3 | 64 | 6 | Interface for calculating click-hit proximity thresholds |
| [RenderedArrowedPolyline](../src/view-operations/RenderedArrowedPolyline.md) | 3 | 111 | 7 | Renders a polyline with arrows for globe and map display |
| [RenderedCircleSymbol](../src/view-operations/RenderedCircleSymbol.md) | 2 | 119 | 79 | Circle-symbol RenderedGeometry whose hit-testing is delegated entirely to its centre point |
| [RenderedColouredEdgeSurfaceMesh](../src/view-operations/RenderedColouredEdgeSurfaceMesh.md) | 2 | 230 | 95 | A wireframe globe mesh with per-vertex or per-edge deferred colouring |
| [RenderedColouredMultiPointOnSphere](../src/view-operations/RenderedColouredMultiPointOnSphere.md) | 3 | 114 | 9 | (pending) |
| [RenderedColouredPolygonOnSphere](../src/view-operations/RenderedColouredPolygonOnSphere.md) | 3 | 117 | 3 | (pending) |
| [RenderedColouredPolylineOnSphere](../src/view-operations/RenderedColouredPolylineOnSphere.md) | 3 | 116 | 3 | (pending) |
| [RenderedColouredTriangleSurfaceMesh](../src/view-operations/RenderedColouredTriangleSurfaceMesh.md) | 2 | 272 | 39 | The filled, coloured triangle-mesh counterpart to the coloured edge mesh |
| [RenderedCrossSymbol](../src/view-operations/RenderedCrossSymbol.md) | 3 | 111 | 5 | (pending) |
| [RenderedEllipse](../src/view-operations/RenderedEllipse.md) | 3 | 132 | 4 | (pending) |
| [RenderedGeometry](../src/view-operations/RenderedGeometry.md) | 2 | 177 | 358 | Copyable pimpl handle to a RenderedGeometryImpl, the value type passed around rendering |
| [RenderedGeometryCollection](../src/view-operations/RenderedGeometryCollection.md) | 1 | 1660 | 694 | (pending) |
| [RenderedGeometryCollectionVisitor](../src/view-operations/RenderedGeometryCollectionVisitor.md) | 3 | 150 | 0 | (pending) |
| [RenderedGeometryFactory](../src/view-operations/RenderedGeometryFactory.md) | 1 | 1342 | 244 | (pending) |
| [RenderedGeometryImpl](../src/view-operations/RenderedGeometryImpl.md) | 2 | 88 | 53 | Abstract interface every concrete rendered-geometry implementation derives from |
| [RenderedGeometryLayer](../src/view-operations/RenderedGeometryLayer.md) | 1 | 1281 | 186 | (pending) |
| [RenderedGeometryLayerVisitor](../src/view-operations/RenderedGeometryLayerVisitor.md) | 3 | 99 | 0 | (pending) |
| [RenderedGeometryParameters](../src/view-operations/RenderedGeometryParameters.md) | 2 | 481 | 199 | Live, signal-emitting drawing parameters for canvas tools plus fixed geometry-operation constants |
| [RenderedGeometryProximity](../src/view-operations/RenderedGeometryProximity.md) | 2 | 391 | 40 | Free functions doing hit-testing over rendered-geometry layers and collections |
| [RenderedGeometryUtils](../src/view-operations/RenderedGeometryUtils.md) | 2 | 832 | 46 | Helper functions for bulk layer activation, reconstruction-geometry extraction and layer visiting |
| [RenderedGeometryVisitor](../src/view-operations/RenderedGeometryVisitor.md) | 2 | 247 | 133 | The visitor interface RenderedGeometry dispatches to, one method per concrete geometry kind |
| [RenderedMultiPointOnSphere](../src/view-operations/RenderedMultiPointOnSphere.md) | 3 | 99 | 4 | (pending) |
| [RenderedMultiReconstructionGeometry](../src/view-operations/RenderedMultiReconstructionGeometry.md) | 3 | 84 | 0 | Wrapper combining multiple ReconstructionGeometry objects with a rendered representation |
| [RenderedPointOnSphere](../src/view-operations/RenderedPointOnSphere.md) | 3 | 99 | 0 | Rendered geometry wrapper for a point on a sphere |
| [RenderedPolygonOnSphere](../src/view-operations/RenderedPolygonOnSphere.md) | 3 | 149 | 0 | Rendered geometry wrapper for a polygon on a sphere with fill support |
| [RenderedPolylineOnSphere](../src/view-operations/RenderedPolylineOnSphere.md) | 3 | 159 | 1 | Rendered geometry wrapper for a polyline on a sphere with optional fill |
| [RenderedRadialArrow](../src/view-operations/RenderedRadialArrow.md) | 2 | 236 | 35 | Rendered arrow normal to the globe surface, for poles and light direction |
| [RenderedReconstructionGeometry](../src/view-operations/RenderedReconstructionGeometry.md) | 3 | 88 | 0 | Composite wrapper pairing a single ReconstructionGeometry with a rendered representation |
| [RenderedResolvedRaster](../src/view-operations/RenderedResolvedRaster.md) | 3 | 138 | 4 | Rendered geometry wrapper for a georeferenced raster with colour palette and modulation |
| [RenderedResolvedScalarField3D](../src/view-operations/RenderedResolvedScalarField3D.md) | 3 | 107 | 1 | Rendered geometry wrapper for a 3D scalar field with rendering parameters |
| [RenderedSmallCircle](../src/view-operations/RenderedSmallCircle.md) | 3 | 133 | 0 | Rendered geometry wrapper for a small circle on a sphere |
| [RenderedSmallCircleArc](../src/view-operations/RenderedSmallCircleArc.md) | 3 | 97 | 0 | Rendered geometry wrapper for small circle arcs with colour and line width |
| [RenderedSquareSymbol](../src/view-operations/RenderedSquareSymbol.md) | 3 | 120 | 0 | Rendered geometry wrapper for square symbols at a point on the sphere |
| [RenderedStrainMarkerSymbol](../src/view-operations/RenderedStrainMarkerSymbol.md) | 3 | 116 | 10 | Rendered geometry wrapper for strain marker ellipses with scale and rotation |
| [RenderedString](../src/view-operations/RenderedString.md) | 3 | 144 | 4 | Rendered geometry wrapper for text labels positioned on the sphere |
| [RenderedSubductionTeethPolyline](../src/view-operations/RenderedSubductionTeethPolyline.md) | 2 | 139 | 16 | Rendered polyline decorated with subduction teeth on one side |
| [RenderedTangentialArrow](../src/view-operations/RenderedTangentialArrow.md) | 3 | 192 | 4 | Rendered geometry wrapper for directional arrows with constant projected size |
| [RenderedTriangleSymbol](../src/view-operations/RenderedTriangleSymbol.md) | 3 | 122 | 0 | Rendered geometry wrapper for equilateral triangle symbols at a point |
| [ScalarField3DRenderParameters](../src/view-operations/ScalarField3DRenderParameters.md) | 1 | 938 | 663 | (pending) |
| [SplitFeatureGeometryOperation](../src/view-operations/SplitFeatureGeometryOperation.md) | 2 | 975 | 13 | Canvas-tool GeometryOperation that splits a feature's geometry at a clicked vertex |
| [SplitFeatureUndoCommand](../src/view-operations/SplitFeatureUndoCommand.md) | 3 | 448 | 1 | Undo command that splits a polyline feature into two at a specified point |
| [UndoRedo](../src/view-operations/UndoRedo.md) | 2 | 717 | 42 | Singleton owning the shared QUndoGroup/stacks and cross-command undo merging |
| [VisibleReconstructionGeometryExport](../src/view-operations/VisibleReconstructionGeometryExport.md) | 2 | 811 | 29 | Collects on-screen reconstruction geometries and hands them to file-io exporters |

## Other files

| File | Kind | Lines |
|---|---|---|
| `src/view-operations/CMakeLists.txt` | build | 97 |

## Depends on

| Component | References |
|---|---|
| [maths](maths.md) | 1688 |
| [gui](gui.md) | 721 |
| [app-logic](app-logic.md) | 609 |
| [model](model.md) | 389 |
| [canvas-tools](canvas-tools.md) | 247 |
| [global](global.md) | 190 |
| [scribe](scribe.md) | 157 |
| [utils](utils.md) | 131 |
| [presentation](presentation.md) | 80 |
| [feature-visitors](feature-visitors.md) | 76 |
| [file-io](file-io.md) | 52 |
| [property-values](property-values.md) | 19 |
| [qt-widgets](qt-widgets.md) | 14 |

## Used by

| Component | References |
|---|---|
| [qt-widgets](qt-widgets.md) | 653 |
| [gui](gui.md) | 622 |
| [canvas-tools](canvas-tools.md) | 497 |
| [presentation](presentation.md) | 326 |
| [opengl](opengl.md) | 243 |
| [app-logic](app-logic.md) | 58 |
| [maths](maths.md) | 4 |
| [file-io](file-io.md) | 1 |

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py tree src/view-operations
python scripts/gpq.py sym . --mode sub --path src/view-operations --defs-only
```
