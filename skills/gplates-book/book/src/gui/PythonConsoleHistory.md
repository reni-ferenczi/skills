# PythonConsoleHistory

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 868 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/PythonConsoleHistory.h` | C++ | 121 |
| `src/gui/PythonConsoleHistory.cc` | C++ | 98 |

## Overview

Manages command history for the Python console, mimicking the behaviour of Bash and the interactive Python interpreter. Maintains two copies of history: `d_unmodifiable_history`, a permanent bounded list of executed commands up to `MAX_HISTORY_SIZE` (80 commands), and `d_modifiable_history`, a working copy that the user can navigate and edit before committing a new command. Navigation with up/down arrows updates the current position in the modifiable copy without affecting the permanent history until the user presses Enter to commit.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::PythonConsoleHistory`](#gplatesguipythonconsolehistory) | class | — | — | 0 | This class encapsulates the logic behind the history functionality in the Python console dialog. |

## Members

### `GPlatesGui::PythonConsoleHistory`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MAX_HISTORY_SIZE` | field | `std::size_t` | public | — |
| `PythonConsoleHistory()` | constructor | `None` | public | — |
| `get_previous_command( const QString &current_command)` | method | `boost::optional<QString>` | public | Handles the case when the user pressses "up" to get the previous command in the history stack, as modified. |
| `get_next_command( const QString &current_command)` | method | `boost::optional<QString>` | public | Handles the case when the user presses "down" to get the next command in the history stack, as modified. |
| `commit_command( const QString &command)` | method | `void` | public | Handles the case when the user presses "enter" and commits the given command as the newest command. |
| `reset_modifiable_history()` | method | `void` | public | Discards any changes made to the modifiable history by the user and starts afresh with a new copy of the history; this handles the case when the user presses Ctrl+C while entering a command. |
| `d_unmodifiable_history` | field | `std::list<QString>` | private | A list of commands in the order that the user entered them. |
| `d_modifiable_history` | field | `std::vector<QString>` | private | A copy of d\_unmodifiable\_history plus an extra entry at the back for a new command. |
| `d_modifiable_history_iter` | field | `std::vector<QString>::iterator` | private | An iterator into d\_modifiable\_history pointing at which item the user is currently modifying. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_PYTHONCONSOLEHISTORY_H` | macro | `None` | — |

## Notes

Duplicate consecutive commands and empty commands are not stored in history. The modifiable history always contains at least the blank entry for new commands, which the iterator always points to a valid position within. Pressing Ctrl+C calls `reset_modifiable_history()` to discard in-progress edits and restore from the permanent history.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/PythonConsoleDialog](../qt-widgets/PythonConsoleDialog.md) | qt-widgets | 6 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/PythonConsoleHistory.h
python scripts/gpq.py def GPlatesGui::PythonConsoleHistory --body
python scripts/gpq.py uses PythonConsoleHistory --kind class
python scripts/gpq.py hier PythonConsoleHistory
```
