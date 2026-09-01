# UndoRedo

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 61 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/UndoRedo.h` | C++ | 243 |
| `src/view-operations/UndoRedo.cc` | C++ | 474 |

## Overview

[[[PROSE overview unit=view-operations/UndoRedo tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::UndoRedoInternal::CommandIdFactory`](#gplatesviewoperationsundoredointernalcommandidfactory) | class | — | — | 0 | Manages allocation/deallocation of unique integer IDs. |
| [`GPlatesViewOperations::UndoRedoInternal::CommandIdImpl`](#gplatesviewoperationsundoredointernalcommandidimpl) | class | — | — | 2 | Interface of CommandId pimpl. |
| [`GPlatesViewOperations::UndoRedoInternal::NonNullCommandIdImpl`](#gplatesviewoperationsundoredointernalnonnullcommandidimpl) | class | [`CommandIdImpl`](UndoRedo.md)<br>`boost::noncopyable` | — | 0 | Non-null implementation of CommandId pimpl. |
| [`GPlatesViewOperations::UndoRedoInternal::NullCommandIdImpl`](#gplatesviewoperationsundoredointernalnullcommandidimpl) | class | [`CommandIdImpl`](UndoRedo.md)<br>[`GPlatesUtils::Singleton<NullCommandIdImpl>`](../utils/Singleton.md) | — | 0 | Null implementation of CommandId pimpl. |
| [`GPlatesViewOperations::UndoRedoInternal::MergeUndoCommand`](#gplatesviewoperationsundoredointernalmergeundocommand) | class | `QUndoCommand` | — | 0 | A decorator command that makes an existing undo command mergeable. |
| [`GPlatesViewOperations::UndoRedo`](#gplatesviewoperationsundoredo) | class | [`GPlatesUtils::Singleton<UndoRedo>`](../utils/Singleton.md) | — | 0 | — |

## Members

### `GPlatesViewOperations::UndoRedoInternal::CommandIdFactory`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CommandIdFactory()` | constructor | `None` | public | — |
| `allocate_id()` | method | `int` | public | — |
| `deallocate_id( int command_id)` | method | `void` | public | — |
| `free_id_seq_type` | typedef | `std::vector<int>` | private | — |
| `d_free_id_seq` | field | `free_id_seq_type` | private | — |
| `d_next_id` | field | `int` | private | — |

### `GPlatesViewOperations::UndoRedoInternal::CommandIdImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~CommandIdImpl()` | destructor | `None` | public | — |
| `get_id()` | method | `int` | public | — |

### `GPlatesViewOperations::UndoRedoInternal::NonNullCommandIdImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `NonNullCommandIdImpl(CommandIdFactory *command_id_factory)` | constructor | `None` | public | — |
| `~NonNullCommandIdImpl()` | destructor | `None` | public | — |
| `get_id()` | method | `int` | public | — |
| `d_command_id_factory` | field | `CommandIdFactory` | private | — |
| `d_command_id` | field | `int` | private | — |

### `GPlatesViewOperations::UndoRedoInternal::NullCommandIdImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `null_destroy( void *)` | method | `void` | public | — |
| `get_id()` | method | `int` | public | — |

### `GPlatesViewOperations::UndoRedoInternal::MergeUndoCommand`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MergeUndoCommand( std::unique_ptr<QUndoCommand> command, UndoRedo::CommandId command_id, QUndoCommand *parent = 0)` | constructor | `None` | public | — |
| `redo()` | method | `void` | public | — |
| `undo()` | method | `void` | public | — |
| `id()` | method | `int` | public | — |
| `mergeWith( const QUndoCommand *other_command)` | method | `bool` | public | Merge this command with another command. |
| `undo_command_ptr_type` | typedef | `boost::shared_ptr<QUndoCommand>` | private | — |
| `command_seq_type` | typedef | `std::vector<undo_command_ptr_type>` | private | — |
| `d_command_seq` | field | `command_seq_type` | private | — |
| `d_command_id` | field | `UndoRedo::CommandId` | private | — |

### `GPlatesViewOperations::UndoRedo`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UndoStackHandle` | typedef | `unsigned int` | private | Typedef for a handle to a QUndoStack. |
| `DEFAULT_UNDO_STACK_HANDLE` | field | `UndoStackHandle` | private | Handle of default QUndoStack. |
| `get_undo_group` | field | `QUndoGroup` | private | Returns sole instance of QUndoGroup. |
| `create_undo_stack()` | method | `UndoStackHandle` | private | Creates a QUndoStack and adds it to sole QUndoGroup instance. |
| `get_active_undo_stack` | field | `QUndoStack` | private | Returns current active QUndoStack. |
| `set_active_undo_stack( UndoStackHandle undo_stack_handle)` | method | `void` | private | Sets the currently active QUndoStack. |
| `CommandId` | class | `None` | private | Wrapper around a unique integer id to be used by QUndoCommand derivations. |
| `get_unique_command_id()` | method | `CommandId` | private | Returns a unique command id. |
| `begin_unique_command_id_scope()` | method | `void` | private | Generates a unique command id and stores internally. |
| `end_unique_command_id_scope()` | method | `void` | private | Releases unique command id generated in matching begin\_unique\_command\_id\_scope() provided no copies of command id still exist. |
| `get_unique_command_id_scope()` | method | `CommandId` | private | Returns unique command id generated in current scope. |
| `UniqueCommandIdScopeGuard` | struct | `None` | private | A convenience structure for automating calls to begin\_unique\_command\_id\_scope() and end\_unique\_command\_id\_scope() in a scope block. |
| `make_mergable_undo_command( std::unique_ptr<QUndoCommand>, CommandId merge_id)` | method | `std::unique_ptr<QUndoCommand>` | private | General way to merge unrelated undo commands (that don't know about each other). |
| `make_mergable_undo_command_in_current_unique_command_id_scope( std::unique_ptr<QUndoCommand>)` | method | `std::unique_ptr<QUndoCommand>` | private | Same as above except uses command id returned from get\_unique\_command\_id\_scope. |
| `GroupUndoCommand` | class | `None` | private | Undo/redo command for grouping child commands into one command. |
| `undo_stack_ptr_seq_type` | typedef | `std::vector<QUndoStack *>` | private | Typedef for sequence of QUndoStack pointers. |
| `unique_command_id_scope_stack` | typedef | `std::stack<CommandId>` | private | Typedef for stack of unique command ids in begin/end scopes. |
| `d_undo_group` | field | `QUndoGroup` | private | — |
| `d_undo_stack_seq` | field | `undo_stack_ptr_seq_type` | private | — |
| `d_active_stack_handle` | field | `UndoStackHandle` | private | — |
| `d_unique_command_id_scope_stack` | field | `unique_command_id_scope_stack` | private | — |
| `d_command_id_factory` | field | `boost::shared_ptr<UndoRedoInternal::CommandIdFactory>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_UNDOREDO_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=view-operations/UndoRedo tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [view-operations/GeometryOperationUndo](GeometryOperationUndo.md) | view-operations | 10 |
| [view-operations/MoveVertexGeometryOperation](MoveVertexGeometryOperation.md) | view-operations | 10 |
| [view-operations/GeometryBuilderUndoCommands](GeometryBuilderUndoCommands.md) | view-operations | 8 |
| [qt-widgets/DigitisationWidget](../qt-widgets/DigitisationWidget.md) | qt-widgets | 7 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 5 |
| [view-operations/DeleteVertexGeometryOperation](DeleteVertexGeometryOperation.md) | view-operations | 4 |
| [view-operations/InsertVertexGeometryOperation](InsertVertexGeometryOperation.md) | view-operations | 4 |
| [view-operations/AddPointGeometryOperation](AddPointGeometryOperation.md) | view-operations | 3 |
| [view-operations/FocusedFeatureGeometryManipulator](FocusedFeatureGeometryManipulator.md) | view-operations | 3 |
| [view-operations/SplitFeatureGeometryOperation](SplitFeatureGeometryOperation.md) | view-operations | 2 |
| [view-operations/SplitFeatureUndoCommand](SplitFeatureUndoCommand.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/UndoRedo.h
python scripts/gpq.py def GPlatesViewOperations::UndoRedo --body
python scripts/gpq.py uses UndoRedo --kind class
python scripts/gpq.py hier UndoRedo
```
