# ChooseCanvasToolUndoCommand

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1093 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ChooseCanvasToolUndoCommand.h` | C++ | 68 |
| `src/gui/ChooseCanvasToolUndoCommand.cc` | C++ | 65 |

## Overview

A `QUndoCommand` that captures and restores the currently active canvas tool. On construction, it saves the active tool by querying `CanvasToolWorkflows`. When undone or redone, it restores that saved tool state by calling `choose_canvas_tool()` on the workflows. This integrates tool selection into the standard undo/redo stack, so switching between tools becomes undoable alongside other operations.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ChooseCanvasToolUndoCommand`](#gplatesguichoosecanvastoolundocommand) | class | `QUndoCommand` | — | 0 | Undo/redo command for choosing a canvas tool. |

## Members

### `GPlatesGui::ChooseCanvasToolUndoCommand`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ChooseCanvasToolUndoCommand( CanvasToolWorkflows &canvas_tool_workflows, QUndoCommand *parent = 0)` | constructor | `None` | public | The canvas tool used for undo/redo is the currently active canvas tool. |
| `redo()` | method | `void` | public | — |
| `undo()` | method | `void` | public | — |
| `d_canvas_tool_workflows` | field | `CanvasToolWorkflows` | private | — |
| `d_canvas_tool` | field | `std::pair<CanvasToolWorkflows::WorkflowType, CanvasToolWorkflows::ToolType>` | private | — |
| `d_first_redo` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_CHOOSECANVASTOOLUNDOCOMMAND_H` | macro | `None` | — |

## Notes

The `d_first_redo` flag suppresses action on the first `redo()` call, since construction already placed the workflows in the correct tool state (the currently active one).

## Used by

| Unit | Component | References |
|---|---|---|
| [view-operations/GeometryOperationUndo](../view-operations/GeometryOperationUndo.md) | view-operations | 5 |
| [qt-widgets/DigitisationWidget](../qt-widgets/DigitisationWidget.md) | qt-widgets | 2 |
| [view-operations/SplitFeatureGeometryOperation](../view-operations/SplitFeatureGeometryOperation.md) | view-operations | 2 |
| [view-operations/SplitFeatureUndoCommand](../view-operations/SplitFeatureUndoCommand.md) | view-operations | 2 |
| [gui/TopologyTools](TopologyTools.md) | gui | 1 |
| [view-operations/AddPointGeometryOperation](../view-operations/AddPointGeometryOperation.md) | view-operations | 1 |
| [view-operations/CloneOperation](../view-operations/CloneOperation.md) | view-operations | 1 |
| [view-operations/DeleteVertexGeometryOperation](../view-operations/DeleteVertexGeometryOperation.md) | view-operations | 1 |
| [view-operations/GeometryBuilderUndoCommands](../view-operations/GeometryBuilderUndoCommands.md) | view-operations | 1 |
| [view-operations/InsertVertexGeometryOperation](../view-operations/InsertVertexGeometryOperation.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ChooseCanvasToolUndoCommand.h
python scripts/gpq.py def GPlatesGui::ChooseCanvasToolUndoCommand --body
python scripts/gpq.py uses ChooseCanvasToolUndoCommand --kind class
python scripts/gpq.py hier ChooseCanvasToolUndoCommand
```
