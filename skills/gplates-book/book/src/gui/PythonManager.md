# PythonManager

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 206 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/PythonManager.h` | C++ | 414 |
| `src/gui/PythonManager.cc` | C++ | 666 |

## Overview

`PythonManager` owns the embedded CPython interpreter inside the GPlates GUI.
It exists because embedding Python is a process-wide, once-only act with a fixed
order that no other class is in a position to perform: register the `pygplates`
module with `PyImport_AppendInittab` so that `import pygplates` resolves to the
statically linked bindings rather than to a site-packages copy, set the program
name from `argv[0]`, set `Py_IgnoreEnvironmentFlag` when
`GPlatesFileIO::StandaloneBundle` reports a bundled standard library (so a
stray `PYTHONHOME`/`PYTHONPATH` on the user's machine cannot point the
interpreter at a Python of the wrong version), call `Py_Initialize()`, and then
immediately give up the GIL with `PyEval_SaveThread()` so that from that moment
on every access goes through `GPlatesApi::PythonInterpreterLocker`.
`initialize()` runs that sequence and then builds the rest of the Python
subsystem on it: it caches `__main__` and its `__dict__` as the single execution
namespace shared by all runners, creates the `GPlatesApi::PythonRunner` that
executes on the main thread and the `GPlatesApi::PythonExecutionThread` that
executes off it, smoke-tests the interpreter in `check_python_capability()` by
importing `sys`, `code`, `math`, `platform` and `pygplates`, and creates the
`GPlatesQtWidgets::PythonConsoleDialog`.

It is a deliberately leaked singleton. `src/gplates_main.cc` constructs
`GPlatesPresentation::Application` first (Python code refers back to it), calls
`initialize()` from `initialise_python()`, and deletes the singleton from
`clean_up()` after the Qt event loop returns but while `Application` is still in
scope. Failure is a normal outcome rather than a fatal one: `PythonInitFailed`
propagates out to `initialise_python()`, which offers
`GPlatesQtWidgets::PythonInitFailedDialog` and then disables
`ComponentManager::Component::python()`, so everything downstream is written to
work with Python absent. `GPlatesPresentation::ViewState` caches the pointer
behind `get_python_manager()`, and `GPlatesApi::PythonUtils::python_manager()`
reaches the singleton directly — that free function is how code deep inside
`src/api` calls back into the manager without a dependency on view state.

The second responsibility is discovering and registering the user-facing
scripts, and the two paths differ. Internal scripts are the `.py` files
compiled into the binary under the Qt resource path `:/python/scripts`; they are
compiled with `Py_CompileString` and injected as modules with
`PyImport_ExecCodeModule`, never appearing on `sys.path`. External scripts are
searched for, in descending priority, in a `scripts/` subdirectory of the
current working directory, the `paths/python_system_script_dir` and
`paths/python_user_script_dir` preferences, and the built-in default of the
former; their directories are appended to `sys.path` by `add_sys_path()` and the
modules are then imported by name. Both sets are deduplicated on module base
name, internal modules outranking every external one. The contract a script
must satisfy is the same either way: expose a top-level `register()` function,
which the manager calls and which typically registers a draw style with
`GPlatesGui::DrawStyleManager` or an entry on `GPlatesGui::UtilitiesMenu`
through the `pygplates.Application` bindings.

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

**Initialisation order.** The constructor runs before `Py_Initialize()`, so it
is restricted to the handful of pre-initialisation Python calls — it uses
`Py_GetVersion()` to extract the `major.minor` string — and it builds a local
`GPlatesAppLogic::UserPreferences(NULL)` rather than using the application-wide
one, which does not exist yet. Every preference access in this file repeats
that throwaway-with-`NULL` pattern for the same reason. `check_init()` throws
`PyManagerNotReady` from `get_python_execution_thread()` if `initialize()` has
not run, and `initialize()` is idempotent only in the weak sense that a second
call warns and returns.

**GIL.** After `PyEval_SaveThread()` no thread holds the GIL by default, so
every Python touch — including the ones inside this class — must be bracketed by
a `GPlatesApi::PythonInterpreterLocker`. Note that `set_python_prefix()` and the
`bp::import` in `check_python_capability()` are called from `initialize()` while
the locker created there is still alive; if you add code to `initialize()`,
check which locker covers it.

**The event blackout is two nested mechanisms, and the nesting is fragile.**
`GPlatesGui::EventBlackout` freezes the UI while a script runs.
`python_runner_started()`/`python_runner_finished()` are called by
`GPlatesApi::PythonRunner` around execution on the Python thread; they start and
stop the blackout and exempt the console's cancel widget. Separately,
`exec_function_slot` is invoked on the main thread via
`Qt::BlockingQueuedConnection` from `GPlatesApi::PythonUtils::run_in_main_thread`
and its `PythonExecGuard` calls `python_started()`/`python_finished()`, which
*suspend* the blackout for the duration — deliberately, because main-thread work
is usually PyQt code that needs its events, and the UI is unresponsive anyway
while Python owns the main thread. The suspend/restore state is the single
boolean `d_stopped_event_blackout_for_python_runner`, so it does not nest: if an
`exec_function_slot` call ever re-enters, the inner call restores the blackout
while the outer main-thread call is still running.

**Shutdown.** The destructor asks the execution thread to `quit_event_loop()`
and waits one second; if the thread has not stopped it calls `terminate()`, so a
long-running script can be killed mid-execution at exit. The console dialog is
parented to the main window but is also `delete`d here, which is safe only
because `clean_up()` runs while `Application` is still alive — moving the
teardown later would double-delete it. `Py_Finalize()` is intentionally never
called (a Boost.Python restriction, noted at the end of `internal_main`). The
destructor also clears the `python/prefix` preference unconditionally
(`d_clear_python_prefix_flag` is initialised true and never set false), so the
value `set_python_prefix()` writes at startup only survives while GPlates runs.

**Script registration swallows errors on purpose.** Both
`register_internal_script` and `register_external_script` catch
`bp::error_already_set` and call `GPlatesApi::PythonUtils::get_error_message()`
purely for its side effect of clearing the Python error indicator; without that
call a single bad script would leave the interpreter in an error state for the
next importer. A script that fails to register therefore disappears silently —
`register_external_script` only logs on success.

**Vestigial members.** Several declarations here have no live implementation.
`find_python()` is declared but defined nowhere in the tree, so it cannot be
called. `d_sleeper` is set to `NULL` in the constructor, `delete`d in the
destructor and never assigned in between, despite the `GPlatesApi::Sleeper`
comment. `validate_python_home()` and `get_python_prefix_from_preferences()`
have no callers. The `system_exit_exception_raised` signal is connected by
`GPlatesQtWidgets::PythonConsoleDialog` but is never emitted by this class; the
identically named signals on `GPlatesApi::PythonRunner` and
`GPlatesApi::PythonExecutionThread` are the ones that actually fire.

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
