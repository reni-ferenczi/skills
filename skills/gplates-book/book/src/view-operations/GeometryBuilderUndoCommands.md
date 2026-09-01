# GeometryBuilderUndoCommands

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 320 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/GeometryBuilderUndoCommands.h` | C++ | 245 |
| `src/view-operations/GeometryBuilderUndoCommands.cc` | C++ | 228 |

## Overview

[[[PROSE overview unit=view-operations/GeometryBuilderUndoCommands tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=view-operations/GeometryBuilderUndoCommands tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
