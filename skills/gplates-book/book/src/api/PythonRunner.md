# PythonRunner

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 284 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/api/PythonRunner.h` | C++ | 190 |
| `src/api/PythonRunner.cc` | C++ | 468 |

## Overview

[[[PROSE overview unit=api/PythonRunner tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesApi::PythonRunner`](#gplatesapipythonrunner) | class | `QObject`<br>[`AbstractPythonRunner`](AbstractPythonRunner.md) | — | 0 | PythonRunner executes Python code in the same thread as the caller, or if posted a DeferredCallEvent, in the thread of its creation. |

## Members

### `GPlatesApi::PythonRunner`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PythonRunner( const boost::python::object &, QObject *parent_ = NULL)` | constructor | `None` | public | — |
| `~PythonRunner()` | destructor | `None` | public | — |
| `exec_interactive_command( const QString &line, PythonExecutionMonitor *monitor)` | method | `void` | public | — |
| `exec_string( const QString &string, PythonExecutionMonitor *monitor)` | method | `void` | public | — |
| `reset_interactive_buffer()` | method | `void` | public | — |
| `exec_file( const QString &filename, const QString &filename_encoding, PythonExecutionMonitor *monitor)` | method | `void` | public | — |
| `eval_string( const QString &string, PythonExecutionMonitor *monitor)` | method | `void` | public | — |
| `exec_function( const boost::function< void () > &function, PythonExecutionMonitor *monitor)` | method | `void` | public | — |
| `eval_function( const boost::function< boost::python::object () > &function, PythonExecutionMonitor *monitor)` | method | `void` | public | — |
| `system_exit_exception_raised( int exit_status, QString exit_error_message)` | method | `void` | public | — |
| `python_started()` | method | `void` | protected | — |
| `python_finished()` | method | `void` | protected | — |
| `PythonExecGuard` | class | `None` | protected | — |
| `exec_function_slot( const boost::function< void () > &f)` | method | `void` | public | — |
| `event( QEvent *ev)` | method | `bool` | protected | — |
| `reset_buffer()` | method | `void` | private | Resets the interactive console's buffer. |
| `handle_exception( PythonExecutionMonitor *monitor)` | method | `void` | private | Handles the occurrence of an exception during Python execution. |
| `handle_system_exit( PythonExecutionMonitor *monitor)` | method | `void` | private | Handle the SystemExit exception, which can be raised explicitly or via quit() or sys.exit(). |
| `d_namespace` | field | `boost::python::object` | private | — |
| `d_console` | field | `boost::python::object` | private | — |
| `d_compile` | field | `boost::python::object` | private | — |
| `d_eval` | field | `boost::python::object` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `DISABLE_GCC_WARNING` | variable | `PUSH_GCC_WARNINGS` | For Py\_XDECREF below. |
| `GPLATES_API_PYTHONRUNNER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=api/PythonRunner tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [api/PyApplication](PyApplication.md) | api | 4 |
| [api/PythonExecutionThread](PythonExecutionThread.md) | api | 2 |
| [api/PythonUtils](PythonUtils.md) | api | 1 |
| [gui/PythonManager](../gui/PythonManager.md) | gui | 1 |
| [qt-widgets/PythonConsoleDialog](../qt-widgets/PythonConsoleDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/api/PythonRunner.h
python scripts/gpq.py def GPlatesApi::PythonRunner --body
python scripts/gpq.py uses PythonRunner --kind class
python scripts/gpq.py hier PythonRunner
```
