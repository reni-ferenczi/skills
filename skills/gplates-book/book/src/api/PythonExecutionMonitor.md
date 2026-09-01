# PythonExecutionMonitor

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 847 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/api/PythonExecutionMonitor.h` | C++ | 258 |
| `src/api/PythonExecutionMonitor.cc` | C++ | 195 |

## Overview

`GPlatesApi::PythonExecutionMonitor` lets the GUI thread hand a job to
`PythonExecutionThread`, keep processing Qt events, and be woken up when that
job finishes, instead of blocking synchronously. The caller constructs a
monitor, passes it down with the job, then calls `exec()`, which runs a local
`QEventLoop` until one of the `signal_exec_*`/`signal_eval_finished` methods
stops it; `get_finish_reason()`, `get_evaluation_result()` and related getters
then report how the job ended.

Because the event loop must be started and stopped on the thread that created
it, every `signal_*` and `set_system_exit_exception_raised` call — which may be
invoked from the Python execution thread — marshals its work back onto the
main thread via `GPlatesApi::PythonUtils::run_in_main_thread` before touching
any monitor state, rather than mutating state directly from whichever thread
calls them. The constructor enforces that a monitor is created on the main GUI
thread by throwing `PythonExecutionMonitorNotInMainGUIThread` otherwise.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesApi::PythonExecutionMonitorNotInMainGUIThread`](#gplatesapipythonexecutionmonitornotinmainguithread) | class | [`GPlatesGlobal::Exception`](../global/GPlatesException.md) | — | 0 | — |
| [`GPlatesApi::PythonExecutionMonitor`](#gplatesapipythonexecutionmonitor) | class | `QObject` | — | 0 | Provides a local event loop that runs parallel to a PythonExecutionThread and allows the main GUI thread to remain responsive while waiting for execution of Python code to finish. |

## Members

### `GPlatesApi::PythonExecutionMonitorNotInMainGUIThread`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PythonExecutionMonitorNotInMainGUIThread( const GPlatesUtils::CallStack::Trace &exception_source)` | constructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |

### `GPlatesApi::PythonExecutionMonitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FinishReason` | enum | `None` | public | An enumeration of reasons why the execution or evaluation finished. |
| `PythonExecutionMonitor()` | constructor | `None` | public | Constructs a PythonExecutionMonitor. |
| `continue_interactive_input()` | method | `bool` | public | If we are monitoring the execution of interactive input from a console, returns whether more input is required before the command can be executed. |
| `get_finish_reason()` | method | `FinishReason` | public | Once execution or evaluation has finished, returns the reason why execution or evaluation finished. |
| `get_exit_status()` | method | `int` | public | Returns the exit status upon finishing execution or evaluation. |
| `exec()` | method | `FinishReason` | public | Starts the local event loop. |
| `signal_exec_interactive_command_finished( bool continue_interactive_input_)` | method | `void` | public | Stops the local event loop, after an interactive command has finished executing. |
| `signal_exec_finished()` | method | `void` | public | Stops the local event loop, after the execution (of anything other than an interactive command) has finished. |
| `signal_eval_finished( const boost::python::object &result)` | method | `void` | public | Stops the local event loop, after the evaluation of a Python expression has finished. |
| `set_system_exit_exception_raised( int exit_status, QString exit_error_message)` | method | `void` | public | Sets the finish reason to be SYSTEM\_EXIT\_EXCEPTION, so that the caller of the Python code can work out how it finished. |
| `set_keyboard_interrupt_exception_raised()` | method | `void` | public | Sets the finish reason to be KEYBOARD\_INTERRUPT\_EXCEPTION. |
| `set_other_exception_raised()` | method | `void` | public | Sets the finish reason to be OTHER\_EXCEPTION. |
| `handle_exec_interactive_command_finished( bool continue_interactive_input_)` | method | `void` | private | — |
| `handle_exec_finished()` | method | `void` | private | — |
| `handle_eval_finished( const boost::python::object &result)` | method | `void` | private | — |
| `handle_system_exit_exception_raised( int exit_status, QString exit_error_message)` | method | `void` | private | — |
| `stop_monitor()` | method | `void` | private | — |
| `PythonExecutionMonitor(const PythonExecutionMonitor&)` | constructor | `None` | private | — |
| `d_continue_interactive_input` | field | `bool` | private | — |
| `d_evaluation_result` | field | `boost::python::object` | private | — |
| `d_event_loop` | field | `QEventLoop` | private | — |
| `d_finish_reason` | field | `FinishReason` | private | — |
| `d_exit_status` | field | `int` | private | — |
| `d_exit_error_message` | field | `QString` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_API_PYTHONEXECUTIONMONITOR_H` | macro | `None` | — |

## Notes

`set_keyboard_interrupt_exception_raised()` and `set_other_exception_raised()`
are the exception, not the rule: unlike the other `signal_*`/`set_*` methods
they write `d_finish_reason` directly, without going through
`run_in_main_thread`, so calling them off the main thread is not safe the way
the rest of the class is documented to be. `stop_monitor()` also polls in a
loop (up to roughly a second) for `d_event_loop` to actually be running before
calling `quit()`, and gives up with a warning if it never starts — `exec()`
must therefore be called promptly after the job is dispatched, with no chance
for Qt to process other events in between, exactly as the header for `exec()`
warns.

## Used by

| Unit | Component | References |
|---|---|---|
| [api/PythonRunner](PythonRunner.md) | api | 13 |
| [api/PythonExecutionThread](PythonExecutionThread.md) | api | 8 |
| [qt-widgets/PythonConsoleDialog](../qt-widgets/PythonConsoleDialog.md) | qt-widgets | 3 |
| [api/PyApplication](PyApplication.md) | api | 1 |
| [api/PythonUtils](PythonUtils.md) | api | 1 |
| [gui/UtilitiesMenu](../gui/UtilitiesMenu.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/api/PythonExecutionMonitor.h
python scripts/gpq.py def GPlatesApi::PythonExecutionMonitor --body
python scripts/gpq.py uses PythonExecutionMonitor --kind class
python scripts/gpq.py hier PythonExecutionMonitor
```
