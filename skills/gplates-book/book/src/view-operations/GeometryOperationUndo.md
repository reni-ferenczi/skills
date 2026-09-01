# GeometryOperationUndo

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 1172 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/GeometryOperationUndo.h` | C++ | 106 |
| `src/view-operations/GeometryOperationUndo.cc` | C++ | 119 |

## Overview

A `QUndoCommand` wrapper that coordinates undo/redo across two separate concerns: the specific geometry operation (add point, delete vertex, etc.) and the canvas tool workflow state. When a user performs a geometry operation and then undoes it, this command ensures both that the operation is undone and that the active canvas tool is restored to what it was before the operation began.

Supports command merging to coalesce related geometry operations into single undo steps (e.g., clicking multiple points in sequence can be undone as one "draw polyline" operation rather than one undo per point).

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::GeometryOperationUndoCommand`](#gplatesviewoperationsgeometryoperationundocommand) | class | `QUndoCommand` | — | 0 | Undo/redo command for handling canvas tool choice undo/redo, geometry operation activation/deactivation and the specific geometry operation undo/redo itself. |

## Members

### `GPlatesViewOperations::GeometryOperationUndoCommand`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GeometryOperationUndoCommand( const QString &text_, std::unique_ptr<QUndoCommand> geometry_operation_command, GeometryOperation *geometry_operation, GPlatesGui::CanvasToolWorkflows &canvas_tool_workflows, UndoRedo::CommandId command_id = UndoRedo::CommandId(), QUndoCommand *parent_ = 0)` | constructor | `None` | public | — |
| `~GeometryOperationUndoCommand()` | destructor | `None` | public | — |
| `redo()` | method | `void` | public | — |
| `undo()` | method | `void` | public | — |
| `id()` | method | `int` | public | The default returned command id is -1 in which case Qt will not try to merge commands. |
| `mergeWith( const QUndoCommand *other_command)` | method | `bool` | public | Merge our geometry operation command with the other geometry operation command. |
| `d_first_redo` | field | `bool` | private | — |
| `d_command_id` | field | `UndoRedo::CommandId` | private | — |
| `d_geometry_operation_command` | field | `boost::scoped_ptr<QUndoCommand>` | private | — |
| `d_geometry_operation` | field | `GeometryOperation` | private | — |
| `d_choose_canvas_tool_command` | field | `boost::scoped_ptr<GPlatesGui::ChooseCanvasToolUndoCommand>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_GEOMETRYOPERATIONUNDO_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [view-operations/AddPointGeometryOperation](AddPointGeometryOperation.md) | view-operations | 2 |
| [view-operations/DeleteVertexGeometryOperation](DeleteVertexGeometryOperation.md) | view-operations | 2 |
| [view-operations/InsertVertexGeometryOperation](InsertVertexGeometryOperation.md) | view-operations | 2 |
| [view-operations/MoveVertexGeometryOperation](MoveVertexGeometryOperation.md) | view-operations | 2 |
| [view-operations/SplitFeatureGeometryOperation](SplitFeatureGeometryOperation.md) | view-operations | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/GeometryOperationUndo.h
python scripts/gpq.py def GPlatesViewOperations::GeometryOperationUndoCommand --body
python scripts/gpq.py uses GeometryOperationUndoCommand --kind class
python scripts/gpq.py hier GeometryOperationUndoCommand
```
