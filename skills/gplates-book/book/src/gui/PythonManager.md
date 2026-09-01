# PythonManager

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 206 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/PythonManager.h` | C++ | 414 |
| `src/gui/PythonManager.cc` | C++ | 666 |

## Overview

[[[PROSE overview unit=gui/PythonManager tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::PyManagerNotReady`](#gplatesguipymanagernotready) | class | [`GPlatesGlobal::Exception`](../global/GPlatesException.md) | — | 0 | — |
| [`GPlatesGui::PythonInitFailed`](#gplatesguipythoninitfailed) | class | [`GPlatesGlobal::Exception`](../global/GPlatesException.md) | — | 0 | — |
| [`GPlatesGui::PythonManager`](#gplatesguipythonmanager) | class | `QObject` | — | 0 | — |

## Members

### `GPlatesGui::PyManagerNotReady`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PyManagerNotReady( const GPlatesUtils::CallStack::Trace &exception_source)` | constructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |

### `GPlatesGui::PythonInitFailed`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PythonInitFailed( const GPlatesUtils::CallStack::Trace &exception_source)` | constructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |

### `GPlatesGui::PythonManager`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `initialize( char* argv[], GPlatesPresentation::Application *app=NULL)` | method | `void` | public | — |
| `is_initialized()` | method | `bool` | public | — |
| `~PythonManager()` | destructor | `None` | public | — |
| `instance()` | method | `PythonManager` | public | — |
| `init_python_interpreter( char* argv[])` | method | `void` | public | — |
| `init_python_console()` | method | `void` | public | — |
| `pop_up_python_console()` | method | `void` | public | — |
| `register_utils_scripts()` | method | `void` | public | — |
| `get_internal_scripts()` | method | `QMap<QString/*module name*/, QString/*module filename*/>` | public | Returns a list of built-in scripts (stored internally in Qt resource files). |
| `get_external_scripts()` | method | `QMap<QString/*module name*/, QFileInfo/*module filename*/>` | public | Returns a unique list of scripts (based on their module name) found in the external file search paths. |
| `register_internal_script( const QString &internal_module_name, const QString &internal_module_filename)` | method | `void` | public | Register an internal script (stored in Qt resource files). |
| `register_external_script( const QString &external_module_name)` | method | `void` | public | Register a script that was found in the external file search paths. |
| `get_python_execution_thread()` | method | `GPlatesApi::PythonExecutionThread` | public | Returns a thread on which Python code can be run off the main thread. |
| `show_init_fail_dlg()` | method | `bool` | public | — |
| `find_python()` | method | `void` | public | — |
| `set_show_init_fail_dlg( bool b)` | method | `void` | public | — |
| `set_python_prefix( const QString& str)` | method | `void` | public | — |
| `set_python_prefix()` | method | `void` | public | — |
| `get_python_prefix_from_preferences()` | method | `QString` | public | — |
| `python_runner_started()` | method | `void` | public | — |
| `python_runner_finished()` | method | `void` | public | — |
| `print_py_msg( const QString& msg)` | method | `void` | public | — |
| `system_exit_exception_raised( int exit_status, QString exit_error_message)` | method | `void` | public | — |
| `PythonManager()` | constructor | `None` | protected | — |
| `check_python_capability()` | method | `void` | protected | — |
| `validate_python_home()` | method | `bool` | protected | — |
| `validate_python_home( const QString& new_home)` | method | `bool` | protected | — |
| `PythonExecGuard` | class | `None` | protected | — |
| `exec_function_slot( const boost::function< void () > &f)` | method | `void` | public | — |
| `python_started()` | method | `void` | private | — |
| `python_finished()` | method | `void` | private | — |
| `add_sys_path()` | method | `void` | private | — |
| `check_init()` | method | `void` | private | I wrote this function. |
| `d_python_main_module` | field | `boost::python::object` | private | The "\_\_main\_\_" Python module. |
| `d_python_main_namespace` | field | `boost::python::object` | private | The "\_\_dict\_\_" attribute of the "\_\_main\_\_" Python module. |
| `d_python_main_thread_runner` | field | `GPlatesApi::PythonRunner` | private | Runs Python code on the main thread. |
| `d_python_execution_thread` | field | `GPlatesApi::PythonExecutionThread` | private | The thread on which Python is executed, off the main thread. |
| `d_sleeper` | field | `GPlatesApi::Sleeper` | private | Replaces Python's time.sleep() with our own implementation. |
| `d_inited` | field | `bool` | private | — |
| `d_python_console_dialog_ptr` | field | `GPlatesQtWidgets::PythonConsoleDialog` | private | TODO: This dialog should be taken out from python manager -- MC. |
| `d_external_scripts_paths` | field | `std::vector<QDir>` | private | Paths to external scripts. |
| `d_stopped_event_blackout_for_python_runner` | field | `bool` | private | If true, we stopped the event blackout temporarily because the PythonRunner started to run something on the main thread. |
| `d_event_blackout` | field | `GPlatesGui::EventBlackout` | private | Lock down the user interface during Python execution. |
| `d_show_python_init_fail_dlg` | field | `bool` | private | — |
| `d_clear_python_prefix_flag` | field | `bool` | private | — |
| `d_python_home` | field | `QString` | private | — |
| `d_python_version` | field | `QString` | private | — |
| `d_application` | field | `GPlatesPresentation::Application` | private | Keep a pointer of GPlatesPresentation::Application here. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `PyInit_pygplates(void)` | function | `PyMODINIT_FUNC` | — |
| `GPLATES_GUI_PYTHON_MANAGER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/PythonManager tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/VisualLayers](../presentation/VisualLayers.md) | presentation | 51 |
| [presentation/VisualLayerRegistry](../presentation/VisualLayerRegistry.md) | presentation | 39 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 38 |
| [presentation/ReconstructVisualLayerParams](../presentation/ReconstructVisualLayerParams.md) | presentation | 28 |
| [presentation/VisualLayer](../presentation/VisualLayer.md) | presentation | 20 |
| [presentation/TopologyNetworkVisualLayerParams](../presentation/TopologyNetworkVisualLayerParams.md) | presentation | 19 |
| [gui/UtilitiesMenu](UtilitiesMenu.md) | gui | 11 |
| [qt-widgets/HellingerThread](../qt-widgets/HellingerThread.md) | qt-widgets | 11 |
| [qt-widgets/PythonConsoleDialog](../qt-widgets/PythonConsoleDialog.md) | qt-widgets | 11 |
| [qt-widgets/PythonExecutionMonitorWidget](../qt-widgets/PythonExecutionMonitorWidget.md) | qt-widgets | 11 |
| [api/PyViewportWindow](../api/PyViewportWindow.md) | api | 10 |
| [entry-points/gplates_main](../entry-points/gplates_main.md) | entry-points | 10 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 10 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 6 |
| [qt-widgets/PythonInitFailedDialog](../qt-widgets/PythonInitFailedDialog.md) | qt-widgets | 5 |
| [api/PythonUtils](../api/PythonUtils.md) | api | 4 |
| [gui/FeatureFocus](FeatureFocus.md) | gui | 4 |
| [api/PythonRunner](../api/PythonRunner.md) | api | 3 |
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 3 |
| [gui/DrawStyleManager](DrawStyleManager.md) | gui | 2 |

*... and 3 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/PythonManager.h
python scripts/gpq.py def GPlatesGui::PythonManager --body
python scripts/gpq.py uses PythonManager --kind class
python scripts/gpq.py hier PythonManager
```
