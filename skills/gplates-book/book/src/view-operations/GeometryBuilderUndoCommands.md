# GeometryBuilderUndoCommands

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 320 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/GeometryBuilderUndoCommands.h` | C++ | 245 |
| `src/view-operations/GeometryBuilderUndoCommands.cc` | C++ | 228 |

## Overview

Five `QUndoCommand` subclasses wrap the primitive edits `GeometryBuilder` exposes (insert point, remove point, move point, set geometry type, clear all geometries) so canvas-tool code can push edits onto Qt's undo stack instead of mutating `GeometryBuilder` directly. Each command's `redo()` calls the matching `GeometryBuilder` mutator and stores the `GeometryBuilder::UndoOperation` it returns; `undo()` replays that stored operation through `GeometryBuilder::undo()`. All five commands wrap their call in a `RenderedGeometryCollection::UpdateGuard` so the rendered-geometry redraw triggered by `GeometryBuilder`'s change signal is deferred to the end of the command rather than firing mid-edit.

Two of the commands support coalescing: `GeometryBuilderMovePointUndoCommand::mergeWith` folds a later move into an earlier one (keeping the earlier command's undo operation but the later command's destination), which is how dragging a vertex produces one undo step instead of one per mouse-move event; it is invoked explicitly by calling code rather than by the Qt undo stack, since the class does not override `id()`. `GeometryBuilderSetGeometryTypeUndoCommand` merges through `id()` instead, using a caller-supplied `UndoRedo::CommandId` — the default id of `-1` disables merging.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::GeometryBuilderInsertPointUndoCommand`](#gplatesviewoperationsgeometrybuilderinsertpointundocommand) | class | `QUndoCommand` | — | 0 | Command to add/undo a point to the current geometry of GeometryBuilder. |
| [`GPlatesViewOperations::GeometryBuilderRemovePointUndoCommand`](#gplatesviewoperationsgeometrybuilderremovepointundocommand) | class | `QUndoCommand` | — | 0 | Command to remove/undo a point from the current geometry of GeometryBuilder. |
| [`GPlatesViewOperations::GeometryBuilderMovePointUndoCommand`](#gplatesviewoperationsgeometrybuildermovepointundocommand) | class | `QUndoCommand` | — | 0 | Command to move/undo a point to the current geometry of GeometryBuilder. |
| [`GPlatesViewOperations::GeometryBuilderSetGeometryTypeUndoCommand`](#gplatesviewoperationsgeometrybuildersetgeometrytypeundocommand) | class | `QUndoCommand` | — | 0 | Command to set/undo the build type for the geometry in GeometryBuilder. |
| [`GPlatesViewOperations::GeometryBuilderClearAllGeometries`](#gplatesviewoperationsgeometrybuilderclearallgeometries) | class | `QUndoCommand` | — | 0 | Command to add/undo a point to the current geometry of GeometryBuilder. |

## Members

### `GPlatesViewOperations::GeometryBuilderInsertPointUndoCommand`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GeometryBuilderInsertPointUndoCommand( GeometryBuilder &digitisation_state_ptr, GeometryBuilder::PointIndex point_index_to_insert_at, const GPlatesMaths::PointOnSphere& oriented_pos_on_globe, QUndoCommand *parent = 0)` | constructor | `None` | public | — |
| `redo()` | method | `void` | public | — |
| `undo()` | method | `void` | public | — |
| `d_geometry_builder` | field | `GeometryBuilder` | private | — |
| `d_point_index_to_insert_at` | field | `GeometryBuilder::PointIndex` | private | — |
| `d_oriented_pos_on_globe` | field | `GPlatesMaths::PointOnSphere` | private | — |
| `d_undo_operation` | field | `GeometryBuilder::UndoOperation` | private | — |

### `GPlatesViewOperations::GeometryBuilderRemovePointUndoCommand`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GeometryBuilderRemovePointUndoCommand( GeometryBuilder &geometry_builder, GeometryBuilder::PointIndex point_index_to_remove_at, QUndoCommand *parent = 0)` | constructor | `None` | public | — |
| `redo()` | method | `void` | public | — |
| `undo()` | method | `void` | public | — |
| `d_geometry_builder` | field | `GeometryBuilder` | private | — |
| `d_point_index_to_remove_at` | field | `GeometryBuilder::PointIndex` | private | — |
| `d_undo_operation` | field | `GeometryBuilder::UndoOperation` | private | — |

### `GPlatesViewOperations::GeometryBuilderMovePointUndoCommand`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GeometryBuilderMovePointUndoCommand( GeometryBuilder &geometry_builder, GeometryBuilder::PointIndex point_index_to_move, const GPlatesMaths::PointOnSphere& oriented_pos_on_globe, bool is_intermediate_move, QUndoCommand *parent = 0)` | constructor | `None` | public | — |
| `redo()` | method | `void` | public | — |
| `undo()` | method | `void` | public | — |
| `mergeWith( const QUndoCommand *other_command)` | method | `bool` | public | Merge this move command with another move command. |
| `d_geometry_builder` | field | `GeometryBuilder` | private | — |
| `d_point_index_to_move` | field | `GeometryBuilder::PointIndex` | private | — |
| `d_oriented_pos_on_globe` | field | `GPlatesMaths::PointOnSphere` | private | — |
| `d_secondary_geometries` | field | `std::vector<GPlatesViewOperations::SecondaryGeometry>` | private | — |
| `d_is_intermediate_move` | field | `bool` | private | — |
| `d_undo_operation` | field | `GeometryBuilder::UndoOperation` | private | — |

### `GPlatesViewOperations::GeometryBuilderSetGeometryTypeUndoCommand`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GeometryBuilderSetGeometryTypeUndoCommand( GeometryBuilder &geometry_builder, GPlatesMaths::GeometryType::Value geom_type_to_build, UndoRedo::CommandId commandId = UndoRedo::CommandId(), QUndoCommand *parent = 0)` | constructor | `None` | public | Default command id is -1 which prevents merging of commands. |
| `id()` | method | `int` | public | — |
| `mergeWith( const QUndoCommand *other_command)` | method | `bool` | public | — |
| `redo()` | method | `void` | public | — |
| `undo()` | method | `void` | public | — |
| `d_geometry_builder` | field | `GeometryBuilder` | private | — |
| `d_geom_type_to_build` | field | `GPlatesMaths::GeometryType::Value` | private | — |
| `d_undo_operation` | field | `GeometryBuilder::UndoOperation` | private | — |
| `d_commandId` | field | `UndoRedo::CommandId` | private | — |

### `GPlatesViewOperations::GeometryBuilderClearAllGeometries`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GeometryBuilderClearAllGeometries( GPlatesViewOperations::GeometryBuilder &geometry_builder, QUndoCommand *parent = 0)` | constructor | `None` | public | — |
| `redo()` | method | `void` | public | — |
| `undo()` | method | `void` | public | — |
| `d_geometry_builder` | field | `GeometryBuilder` | private | — |
| `d_undo_operation` | field | `GeometryBuilder::UndoOperation` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_GEOMETRYBUILDERUNDOCOMMANDS_H` | macro | `None` | — |

## Notes

`GeometryBuilderMovePointUndoCommand::d_secondary_geometries` is a reference, not a copy, captured from `GeometryBuilder::get_secondary_geometries()` at construction — it stays bound to that `GeometryBuilder`'s internal container, so the command must not outlive the builder it was created for.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/DigitisationWidget](../qt-widgets/DigitisationWidget.md) | qt-widgets | 2 |
| [view-operations/AddPointGeometryOperation](AddPointGeometryOperation.md) | view-operations | 2 |
| [view-operations/DeleteVertexGeometryOperation](DeleteVertexGeometryOperation.md) | view-operations | 2 |
| [view-operations/InsertVertexGeometryOperation](InsertVertexGeometryOperation.md) | view-operations | 2 |
| [view-operations/MoveVertexGeometryOperation](MoveVertexGeometryOperation.md) | view-operations | 2 |
| [view-operations/SplitFeatureGeometryOperation](SplitFeatureGeometryOperation.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/GeometryBuilderUndoCommands.h
python scripts/gpq.py def GPlatesViewOperations::GeometryBuilderMovePointUndoCommand --body
python scripts/gpq.py uses GeometryBuilderMovePointUndoCommand --kind class
python scripts/gpq.py hier GeometryBuilderMovePointUndoCommand
```
