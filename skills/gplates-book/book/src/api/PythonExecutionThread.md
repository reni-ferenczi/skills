# PythonExecutionThread

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 341 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/api/PythonExecutionThread.h` | C++ | 272 |
| `src/api/PythonExecutionThread.cc` | C++ | 273 |

## Overview

`GPlatesApi::PythonExecutionThread` is the `QThread` subclass that owns the
Python interpreter's execution context away from the GUI thread. Its `run()`
creates a `PythonRunner` bound to the shared namespace and enters a local
`QEventLoop`; every `exec_*`/`eval_*` method (mirroring
`AbstractPythonRunner`'s interface) packages its arguments plus the internal
`PythonExecutionMonitor` `d_monitor` into a `boost::function` and hands it to
`run_in_python_thread`, which invokes the corresponding `PythonRunner` slot
across threads via `QMetaObject::invokeMethod` and then blocks the calling
(main GUI) thread on `d_monitor.exec()` until the job posts back that it
finished.

`get_python_thread_id()` and `raise_keyboard_interrupt_exception()` exist
because interrupting a Python call in progress needs the interpreter-level
thread id captured when `run()` starts, not the `QThread` id;
`raise_keyboard_interrupt_exception()` uses it with `PyThreadState_SetAsyncExc`
to deliver a `KeyboardInterrupt` into whatever Python code the thread is
currently running.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesApi::PythonExecutionThread`](#gplatesapipythonexecutionthread) | class | `QThread` | — | 0 | The thread on which Python gets executed, away from the main thread. |

## Members

### `GPlatesApi::PythonExecutionThread`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PythonExecutionThread( const boost::python::object &main_namespace, QObject *parent_)` | constructor | `None` | public | — |
| `exec_interactive_command( const QString &command)` | method | `void` | public | Executes command as entered on an interactive console on this thread, monitored from another thread by monitor. |
| `reset_interactive_buffer()` | method | `void` | public | Resets the buffer in the interactive console (e.g. when the user presses Ctrl+C in the console). |
| `exec_string( const QString &string)` | method | `void` | public | Executes the Python code in string on this thread, monitored from another thread by monitor. |
| `exec_file( const QString &filename, const QString &filename_encoding)` | method | `void` | public | Executes filename as a Python script, monitored from another thread by monitor. |
| `eval_string( const QString &string)` | method | `void` | public | Evaluates the Python expression contained in string, monitored from another thread by monitor. |
| `exec_function( const boost::function< void () > &function)` | method | `void` | public | Executes the given function, monitored from another thread by monitor. monitor must not be NULL. |
| `eval_function( const boost::function< boost::python::object () > &function)` | method | `void` | public | Evaluates the given function, which returns a Python object, monitored from another thread by monitor. monitor must not be NULL. |
| `quit_event_loop()` | method | `void` | public | Quit the event loop, if it is running. |
| `get_python_thread_id()` | method | `long` | public | Returns the thread id as reported by Python, if the thread is running. |
| `raise_keyboard_interrupt_exception()` | method | `void` | public | Raises a Python KeyboardInterrupt exception in the Python thread, if it is running. |
| `continue_interactive_input()` | method | `bool` | public | — |
| `system_exit_exception_raised( int exit_status, QString exit_error_message)` | method | `void` | public | Emitted when an unhandled Python SystemExit exception is raised in the thread. |
| `run()` | method | `void` | protected | — |
| `check_python_runner()` | method | `void` | protected | — |
| `run_in_python_thread( boost::function< void () > &f)` | method | `void` | protected | — |
| `wait_done()` | method | `void` | protected | — |
| `handle_system_exit_exception_raised( int exit_status, QString exit_error_message)` | method | `void` | private | — |
| `d_namespace` | field | `boost::python::object` | private | — |
| `d_python_runner` | field | `PythonRunner` | private | — |
| `d_event_loop` | field | `QEventLoop` | private | — |
| `d_python_thread_id` | field | `long` | private | — |
| `d_monitor` | field | `PythonExecutionMonitor` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_API_PYTHONEXECUTIONTHREAD_H` | macro | `None` | — |

## Notes

`d_namespace` is stored as a reference (`const boost::python::object &`), not
a copy, so the namespace object passed to the constructor must outlive the
thread. `d_python_runner` is only non-null while `run()` is executing —
`check_python_runner()` throws `GPlatesGlobal::LogException` if a caller
invokes one of the `exec_*`/`eval_*` methods before the thread has started (or
after it has stopped). `run_in_python_thread` silently does nothing if it is
called from any thread other than the main thread, rather than dispatching
the job or raising an error, so calling the `exec_*`/`eval_*` methods off the
main GUI thread is a no-op, not a crash.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/PythonManager](../gui/PythonManager.md) | gui | 9 |
| [api/PythonUtils](PythonUtils.md) | api | 4 |
| [qt-widgets/PythonExecutionMonitorWidget](../qt-widgets/PythonExecutionMonitorWidget.md) | qt-widgets | 4 |
| [qt-widgets/PythonConsoleDialog](../qt-widgets/PythonConsoleDialog.md) | qt-widgets | 3 |
| [gui/UtilitiesMenu](../gui/UtilitiesMenu.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/api/PythonExecutionThread.h
python scripts/gpq.py def GPlatesApi::PythonExecutionThread --body
python scripts/gpq.py uses PythonExecutionThread --kind class
python scripts/gpq.py hier PythonExecutionThread
```
