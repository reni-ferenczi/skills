# AbstractPythonRunner

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 284 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/api/AbstractPythonRunner.h` | C++ | 155 |

## Overview

`GPlatesApi::AbstractPythonRunner` is the interface between callers that want
Python code run and whatever actually runs it — the interactive console, a
script file, or an arbitrary `boost::function`. It covers the different shapes
that "run some Python" takes: a line typed interactively (`exec_interactive_command`,
paired with `reset_interactive_buffer` for Ctrl+C handling), a string of code,
a script file (`exec_file`, which takes a separate `filename_encoding` so the
filename itself renders correctly in tracebacks), or a native C++ callable that
executes or evaluates to a `boost::python::object`. Every operation reports its
outcome back through a `PythonExecutionMonitor` rather than a return value,
which is what lets execution happen elsewhere — including on another thread —
while the caller is told the result asynchronously.

The class deliberately leaves threading unspecified: whether Python code runs
on the calling thread or a separate one, and whether the runner's own methods
are safe to call concurrently, is up to the concrete implementation.

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

`monitor` must not be null for any of these calls. `exec_file` reads the target
file in text mode but does not decode it; non-ASCII source must declare its own
encoding via a PEP 263 comment, and `filename_encoding` only affects how the
filename (not the file contents) appears in tracebacks and syntax errors.

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
