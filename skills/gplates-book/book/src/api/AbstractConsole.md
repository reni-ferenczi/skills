# AbstractConsole

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 115 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/api/AbstractConsole.h` | C++ | 84 |

## Overview

[[[PROSE overview unit=api/AbstractConsole tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesApi::AbstractConsole`](#gplatesapiabstractconsole) | class | — | — | 1 | The abstract base class for consoles that can display output from Python, and read lines as input. |

## Members

### `GPlatesApi::AbstractConsole`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~AbstractConsole()` | destructor | `None` | public | — |
| `append_text( const QString &text, bool error = false)` | method | `void` | public | Appends the given text to the console. |
| `append_text( const boost::python::object &obj, bool error = false)` | method | `void` | public | Appends the stringified version of obj to the console. |
| `read_line()` | method | `QString` | public | Prompts the user for a line of input. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_API_ABSTRACTCONSOLE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=api/AbstractConsole tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/PythonManager](../gui/PythonManager.md) | gui | 14 |
| [api/ConsoleReader](ConsoleReader.md) | api | 13 |
| [api/ConsoleWriter](ConsoleWriter.md) | api | 13 |
| [qt-widgets/PythonConsoleDialog](../qt-widgets/PythonConsoleDialog.md) | qt-widgets | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/api/AbstractConsole.h
python scripts/gpq.py def GPlatesApi::AbstractConsole --body
python scripts/gpq.py uses AbstractConsole --kind class
python scripts/gpq.py hier AbstractConsole
```
