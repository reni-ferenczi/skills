# PythonExecutionMonitor

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 847 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/api/PythonExecutionMonitor.h` | C++ | 258 |
| `src/api/PythonExecutionMonitor.cc` | C++ | 195 |

## Overview

[[[PROSE overview unit=api/PythonExecutionMonitor tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=api/PythonExecutionMonitor tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
