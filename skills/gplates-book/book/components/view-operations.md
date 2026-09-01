# view-operations

[Book TOC](../TOC.md)

57 unit page(s), 82 source file(s) documented here, 1 further file(s) listed below.

## Overview

This is the seam between what GPlates computes and what it draws, and the mutable
model behind on-screen geometry editing. One half is a scene-graph: every piece of
drawable output — reconstructed features, canvas-tool feedback, measurement
overlays, highlight decoration — is wrapped as a `RenderedGeometry` and handed to
`RenderedGeometryCollection`, which the globe and map painters read back by
visiting it, with no other channel connecting producers to the canvas. The other
half is `GeometryBuilder`, the observable point-sequence model that lets
digitisation and vertex-editing tools accumulate a half-finished geometry before
an immutable `GeometryOnSphere` can exist, plus the small hierarchy of
`GeometryOperation` subclasses that drive it from mouse input. A handful of
cross-cutting services — shared undo/redo, hit-testing, and export of on-screen
geometry to file — round the component out.

`RenderedGeometryCollection` supplies the two-level main-layer/child-layer
structure, activation rules and aggregated update signal that let unrelated
producers share one scene without colliding on draw order. `RenderedGeometry`
itself is deliberately inert: a thin, copyable pimpl over an abstract
`RenderedGeometryImpl`, reachable only through `RenderedGeometryVisitor` double
dispatch, and buildable only through `RenderedGeometryFactory` — the one place
that names any of the twenty-odd concrete implementation types, so adding a new
kind of drawable never touches a producer. `RenderedGeometryLayer` is where those
handles actually live, stored twice — once in draw order, once in a spatial
partition — so painters and proximity tests can each get the ordering they need.
On the editing side, `GeometryBuilder` leans on `InternalGeometryBuilder` to
rebuild geometry lazily and on a memento-based undo protocol that plugs into
`UndoRedo`'s shared `QUndoGroup` and its cross-command merging; the five
`GeometryOperation` subclasses (add-point, insert-vertex, move-vertex,
delete-vertex, split-feature) each mutate a builder and then render the result.
`RenderedGeometryParameters` and `ScalarField3DRenderParameters` are the
component's shared vocabulary objects — live, signal-emitting drawing settings in
the first case, a scribe-persisted parameter bundle in the second — that give
otherwise-unrelated subsystems a single place to agree on how something should
look.

The component leans heavily on `maths` for the geometric primitives and the
`CubeQuadTreePartition` behind spatial layer storage, and on `model` and
`property-values` for the feature mutation that `GeometryBuilder` and
`FocusedFeatureGeometryManipulator` keep synchronised in both directions.
`app-logic` supplies the `ReconstructionGeometry` objects that rendered geometry
wraps and that `RenderedGeometryUtils` extracts back out; `gui` supplies the
deferred `ColourProxy` colour scheme every coloured rendered geometry defers to at
paint time; `scribe` carries `ScalarField3DRenderParameters` and friends across
sessions and project files. Running the other way, `presentation` owns the single
`RenderedGeometryCollection` and the two `GeometryBuilder` instances on its
`ViewState`, and its `ReconstructionGeometryRenderer` is the heaviest single
producer of `RenderedGeometry` each frame; `gui` and `opengl` painters are the
heaviest consumers, walking the collection or the scalar-field parameters to put
pixels on the globe and map; `qt-widgets` drives geometry editing through the
operation classes and observes `GeometryBuilder`/`RenderedGeometryParameters` to
keep dialogs and tables in sync. `canvas-tools` and this component are mutually
dependent: view-operations supplies the rendering substrate, the editing
operations and the proximity/undo machinery that concrete canvas tools are built
from, while canvas-tools feeds back tool-specific policy. `file-io` is a much
smaller, one-directional edge — `VisibleReconstructionGeometryExport` collects
what is currently on screen and hands it to file-io's exporters.

## Units

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [AddPointGeometryOperation](../src/view-operations/AddPointGeometryOperation.md) | 3 | 571 | 4 | Responds to user clicks to add points to digitized geometry |
| [ChangeLightDirectionOperation](../src/view-operations/ChangeLightDirectionOperation.md) | 2 | 433 | 10 | Drag-driven canvas-tool backend for repositioning the globe's light direction |
| [CloneOperation](../src/view-operations/CloneOperation.md) | 3 | 244 | 1 | Duplicates the focused feature or just its geometry |
| [DeleteFeatureOperation](../src/view-operations/DeleteFeatureOperation.md) | 3 | 130 | 0 | Removes the currently focused feature from its parent collection |
| [DeleteVertexGeometryOperation](../src/view-operations/DeleteVertexGeometryOperation.md) | 3 | 692 | 7 | Responds to user clicks on vertices to delete them |
| [FocusedFeatureGeometryManipulator](../src/view-operations/FocusedFeatureGeometryManipulator.md) | 3 | 728 | 0 | Bridges geometry editing in GeometryBuilder back to the feature model |
| [GeometryBuilder](../src/view-operations/GeometryBuilder.md) | 1 | 1901 | 555 | mutable, observable point-sequence model behind geometry digitisation and vertex editing, with memento undo |
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
| [RenderedColouredMultiPointOnSphere](../src/view-operations/RenderedColouredMultiPointOnSphere.md) | 3 | 114 | 9 | Rendered multi-point geometry where each point carries its own colour |
| [RenderedColouredPolygonOnSphere](../src/view-operations/RenderedColouredPolygonOnSphere.md) | 3 | 117 | 3 | Rendered polygon outline where exterior-ring points carry individual colours |
| [RenderedColouredPolylineOnSphere](../src/view-operations/RenderedColouredPolylineOnSphere.md) | 3 | 116 | 3 | Rendered polyline where each point carries its own colour |
| [RenderedColouredTriangleSurfaceMesh](../src/view-operations/RenderedColouredTriangleSurfaceMesh.md) | 2 | 272 | 39 | The filled, coloured triangle-mesh counterpart to the coloured edge mesh |
| [RenderedCrossSymbol](../src/view-operations/RenderedCrossSymbol.md) | 3 | 111 | 5 | Rendered north-south oriented cross symbol at a point on the sphere |
| [RenderedEllipse](../src/view-operations/RenderedEllipse.md) | 3 | 132 | 4 | Rendered ellipse on the sphere with orientation, axes and colour |
| [RenderedGeometry](../src/view-operations/RenderedGeometry.md) | 2 | 177 | 358 | Copyable pimpl handle to a RenderedGeometryImpl, the value type passed around rendering |
| [RenderedGeometryCollection](../src/view-operations/RenderedGeometryCollection.md) | 1 | 1660 | 694 | the scene graph joining app-logic and canvas-tool output to the globe and map painters |
| [RenderedGeometryCollectionVisitor](../src/view-operations/RenderedGeometryCollectionVisitor.md) | 3 | 150 | 0 | Visitor pattern for traversing a rendered geometry collection and its layers |
| [RenderedGeometryFactory](../src/view-operations/RenderedGeometryFactory.md) | 1 | 1342 | 244 | the only place naming the concrete RenderedGeometry implementation types |
| [RenderedGeometryImpl](../src/view-operations/RenderedGeometryImpl.md) | 2 | 88 | 53 | Abstract interface every concrete rendered-geometry implementation derives from |
| [RenderedGeometryLayer](../src/view-operations/RenderedGeometryLayer.md) | 1 | 1281 | 186 | one drawable ordering unit, storing rendered geometries in both draw order and a spatial partition |
| [RenderedGeometryLayerVisitor](../src/view-operations/RenderedGeometryLayerVisitor.md) | 3 | 99 | 0 | Visitor interface for traversing RenderedGeometryLayer and child RenderedGeometry objects |
| [RenderedGeometryParameters](../src/view-operations/RenderedGeometryParameters.md) | 2 | 481 | 199 | Live, signal-emitting drawing parameters for canvas tools plus fixed geometry-operation constants |
| [RenderedGeometryProximity](../src/view-operations/RenderedGeometryProximity.md) | 2 | 391 | 40 | Free functions doing hit-testing over rendered-geometry layers and collections |
| [RenderedGeometryUtils](../src/view-operations/RenderedGeometryUtils.md) | 2 | 832 | 46 | Helper functions for bulk layer activation, reconstruction-geometry extraction and layer visiting |
| [RenderedGeometryVisitor](../src/view-operations/RenderedGeometryVisitor.md) | 2 | 247 | 133 | The visitor interface RenderedGeometry dispatches to, one method per concrete geometry kind |
| [RenderedMultiPointOnSphere](../src/view-operations/RenderedMultiPointOnSphere.md) | 3 | 99 | 4 | Rendered geometry wrapper for MultiPointOnSphere with color and point size properties |
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
| [ScalarField3DRenderParameters](../src/view-operations/ScalarField3DRenderParameters.md) | 1 | 938 | 663 | shared parameter bundle for 3D scalar field visualisation, from options widget to GLSL uniforms |
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
