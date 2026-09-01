# GeometryOperationState

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 37 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/GeometryOperationState.h` | C++ | 165 |

## Overview

`GeometryOperationState` is a small Qt signal hub that tracks which single `GPlatesViewOperations::GeometryOperation` and which single `GPlatesViewOperations::GeometryBuilder` are currently active, since several canvas tools (delete/move/split/add-vertex, and more) share this state but only one operation and one builder are ever active at a time. A `GeometryOperation` calls `set_active_geometry_operation()` on activation and `set_no_active_geometry_operation()` on deactivation; each mutator emits `switched_geometry_operation()` (or `switched_geometry_builder()`) only when the pointer actually changes, letting task-panel widgets such as `ModifyGeometryWidget` and `DigitisationWidget` react to whichever tool just took over geometry editing without depending on any specific tool class.

There is no corresponding `.cc` file — the whole class is defined inline in the header.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCanvasTools::GeometryOperationState`](#gplatescanvastoolsgeometryoperationstate) | class | `QObject` | — | 0 | Keeps track of which GeometryOperation is currently active and which GeometryBuilder contains the geometry. |

## Members

### `GPlatesCanvasTools::GeometryOperationState`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GeometryOperationState()` | constructor | `None` | public | — |
| `set_active_geometry_operation( GPlatesViewOperations::GeometryOperation *geometry_operation)` | method | `void` | public | The newly activated GeometryOperation calls this to indicate it's active. |
| `set_no_active_geometry_operation()` | method | `void` | public | Since only one GeometryOperation is active at any time this method let's listeners know that there's currently no active GeometryOperation. |
| `set_active_geometry_builder( GPlatesViewOperations::GeometryBuilder *geometry_builder)` | method | `void` | public | The newly activated GeometryBuilder calls this to indicate it's active. |
| `set_no_active_geometry_builder()` | method | `void` | public | Since only one GeometryBuilder is active at any time this method let's listeners know that there's currently no active GeometryBuilder. |
| `switched_geometry_operation( GPlatesViewOperations::GeometryOperation *geometry_operation)` | method | `void` | public | The geometry operation emitting signals has changed. |
| `switched_geometry_builder( GPlatesViewOperations::GeometryBuilder *geometry_builder)` | method | `void` | public | The geometry builder emitting signals has changed. |
| `d_active_geometry_operation` | field | `GPlatesViewOperations::GeometryOperation` | private | — |
| `d_active_geometry_builder` | field | `GPlatesViewOperations::GeometryBuilder` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_CANVASTOOLS_GEOMETRYOPERATIONSTATE_H` | macro | `None` | — |

## Notes

A `NULL` argument to either `switched_*` signal means no operation/builder is currently active — listeners must check for it. The header's own comment warns that signal/slot argument types must all be given in namespace scope, otherwise Qt's moc-generated connections silently fail to match a signal to a slot at runtime.

## Used by

| Unit | Component | References |
|---|---|---|
| [view-operations/InsertVertexGeometryOperation](../view-operations/InsertVertexGeometryOperation.md) | view-operations | 59 |
| [view-operations/SplitFeatureGeometryOperation](../view-operations/SplitFeatureGeometryOperation.md) | view-operations | 58 |
| [qt-widgets/LatLonCoordinatesTable](../qt-widgets/LatLonCoordinatesTable.md) | qt-widgets | 53 |
| [view-operations/MoveVertexGeometryOperation](../view-operations/MoveVertexGeometryOperation.md) | view-operations | 50 |
| [view-operations/DeleteVertexGeometryOperation](../view-operations/DeleteVertexGeometryOperation.md) | view-operations | 42 |
| [canvas-tools/MeasureDistance](MeasureDistance.md) | canvas-tools | 38 |
| [canvas-tools/MeasureDistanceState](MeasureDistanceState.md) | canvas-tools | 35 |
| [view-operations/AddPointGeometryOperation](../view-operations/AddPointGeometryOperation.md) | view-operations | 30 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 7 |
| [gui/DigitisationCanvasToolWorkflow](../gui/DigitisationCanvasToolWorkflow.md) | gui | 3 |
| [gui/FeatureInspectionCanvasToolWorkflow](../gui/FeatureInspectionCanvasToolWorkflow.md) | gui | 3 |
| [gui/SmallCircleCanvasToolWorkflow](../gui/SmallCircleCanvasToolWorkflow.md) | gui | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/canvas-tools/GeometryOperationState.h
python scripts/gpq.py def GPlatesCanvasTools::GeometryOperationState --body
python scripts/gpq.py uses GeometryOperationState --kind class
python scripts/gpq.py hier GeometryOperationState
```
