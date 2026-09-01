# AbstractPythonRunner

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 284 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/api/AbstractPythonRunner.h` | C++ | 155 |

## Overview

[[[PROSE overview unit=api/AbstractPythonRunner tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesApi::AbstractPythonRunner`](#gplatesapiabstractpythonrunner) | class | — | — | 1 | AbstractPythonRunner provides an interface to execute Python code in various ways, monitored by a PythonExecutionMonitor instance. |

## Members

### `GPlatesApi::AbstractPythonRunner`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~AbstractPythonRunner()` | destructor | `None` | public | — |
| `exec_interactive_command( const QString &command, PythonExecutionMonitor *monitor)` | method | `void` | public | Executes command as entered on an interactive console. |
| `reset_interactive_buffer()` | method | `void` | public | Resets the buffer in the interactive console (e.g. when the user presses Ctrl+C in the console). |
| `exec_string( const QString &string, PythonExecutionMonitor *monitor)` | method | `void` | public | Executes the Python code contained in string. |
| `exec_file( const QString &filename, const QString &filename_encoding, PythonExecutionMonitor *monitor)` | method | `void` | public | Executes filename as a Python script, monitored from another thread by monitor. |
| `eval_string( const QString &string, PythonExecutionMonitor *monitor)` | method | `void` | public | Evaluates the Python expression contained in string. |
| `exec_function( const boost::function< void () > &function, PythonExecutionMonitor *monitor)` | method | `void` | public | Executes the given function. monitor must not be NULL. |
| `eval_function( const boost::function< boost::python::object () > &function, PythonExecutionMonitor *monitor)` | method | `void` | public | Evaluates the given function, which returns a Python object. monitor must not be NULL. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_API_ABSTRACTPYTHONRUNNER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=api/AbstractPythonRunner tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [api/PythonRunner](PythonRunner.md) | api | 37 |
| [api/PythonExecutionThread](PythonExecutionThread.md) | api | 14 |
| [api/PythonUtils](PythonUtils.md) | api | 7 |
| [qt-widgets/PythonConsoleDialog](../qt-widgets/PythonConsoleDialog.md) | qt-widgets | 3 |
| [gui/UtilitiesMenu](../gui/UtilitiesMenu.md) | gui | 1 |
| [qt-widgets/PythonExecutionMonitorWidget](../qt-widgets/PythonExecutionMonitorWidget.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/api/AbstractPythonRunner.h
python scripts/gpq.py def GPlatesApi::AbstractPythonRunner --body
python scripts/gpq.py uses AbstractPythonRunner --kind class
python scripts/gpq.py hier AbstractPythonRunner
```
