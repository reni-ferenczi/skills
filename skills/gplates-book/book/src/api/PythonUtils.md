# PythonUtils

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 59 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/api/PythonUtils.h` | C++ | 187 |
| `src/api/PythonUtils.cc` | C++ | 229 |

## Overview

`PythonUtils` is the shim that everything embedding CPython in GPlates rests on. It is a namespace of free functions plus one RAII guard rather than a class, and it answers three recurring needs: converting between `QString` and Python string objects, turning a pending Python exception into text you can hand to `qWarning()`, and marshalling a call from whichever thread is running onto the Qt main thread.

The threading part is the reason the unit exists at all. GPlates runs the interpreter on a dedicated `PythonExecutionThread` driving a `PythonRunner`, while Qt widgets may only be touched from the main thread, so every call that crosses that line has to be queued and the GIL has to change hands at the same moment. `run_in_main_thread` is the interpreter-to-GUI direction: the `void` specialisation posts the `boost::function` to `GPlatesGui::PythonManager::exec_function_slot` over a `Qt::BlockingQueuedConnection` while a `ThreadSwitchGuard` holds the GIL released, and the templated overload builds on it by stashing the result in a `boost::any`. `GPlatesApi::PythonExecutionThread::run_in_python_thread` is the mirror image, posting to `PythonRunner::exec_function_slot` under the same guard. On the receiving side both slots wrap the call in their own `PythonExecGuard` so `PythonManager`/`PythonRunner` see a matched started/finished pair.

`DISPATCH_GUI_FUN` is the sugar that Python-facing wrappers put at the top of any method touching the GUI. It expands to `if (!is_main_thread()) return run_in_main_thread`, so a call site written as `DISPATCH_GUI_FUN<void>(boost::bind(&Application::exec_gui_string, this, str));` re-enters the very same method on the main thread and returns; the code below the macro therefore only ever executes there. The bindings in `PyApplication.cc` and `PyViewportWindow.cc` are built almost entirely out of this one line. The remaining helpers serve the same bindings: `to_QString` and `qstring_to_python_string` at the string boundary, `get_error_message` in the `catch (const boost::python::error_already_set &)` blocks that appear throughout `src/api`, and `is_gui_object`, which reads a `gui_obj` attribute off a registered Python utility so `call_utility` can decide whether that utility needs dispatching to the GUI thread.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesApi::PythonUtils::ThreadSwitchGuard`](#gplatesapipythonutilsthreadswitchguard) | class | — | — | 0 | — |

## Members

### `GPlatesApi::PythonUtils::ThreadSwitchGuard`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ThreadSwitchGuard()` | constructor | `None` | public | — |
| `~ThreadSwitchGuard()` | destructor | `None` | public | — |
| `d_gil_state` | field | `PyGILState_STATE` | private | — |
| `d_thread_state` | field | `PyThreadState` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `DISABLE_GCC_WARNING` | variable | `PUSH_GCC_WARNINGS` | For PyUnicode\_Check and PyString\_Check below. |
| `GPLATES_API_PYTHONUTILS_H` | macro | `None` | — |
| `DISPATCH_GUI_FUN` | macro | `if(!GPlatesApi::PythonUtils::is_main_thread()) \ return GPlatesApi::PythonUtils::run_in_main_thread` | — |
| `to_QString(const boost::python::object &obj)` | function | `QString` | Stringifies obj. |
| `run_startup_scripts( PythonExecutionThread *python_execution_thread, GPlatesAppLogic::UserPreferences &user_prefs)` | function | `void` | Runs all startup scripts in pre-defined search directories on the given python\_execution\_thread. |
| `get_error_message()` | function | `QString` | — |
| `is_main_thread()` | function | `bool` | — |
| `helper_fun( const boost::function< Type () > &f, boost::any* ret)` | function | `void` | — |
| `run_in_main_thread( const boost::function< ReturnType () > &f)` | function | `ReturnType` | — |
| `run_in_main_thread( const boost::function< void () > &f)` | function | `void` | — |
| `is_gui_object(const boost::python::object &obj)` | function | `bool` | — |
| `qstring_to_python_string( const QString& str_input)` | function | `boost::python::str` | — |

## Notes

`ThreadSwitchGuard` is not a scoped lock, despite the shape. Its constructor calls `PyGILState_Ensure` and then immediately `PyEval_SaveThread`; the destructor undoes them in the reverse order. The net effect for the guard's lifetime is that the current thread is registered with the interpreter but does *not* hold the GIL — the opposite of `PythonInterpreterLocker`, and closer to `PythonInterpreterUnlocker` with the ensure step prepended so it also works on a thread Python has not seen before. That is precisely what makes the blocking cross-thread call safe: the caller drops the GIL before blocking, so the receiving thread can take it. Nesting a `PythonInterpreterLocker` inside a `ThreadSwitchGuard` is fine; assuming you still hold the GIL inside one is not.

The `void` specialisation blocks until the main thread's event loop gets around to the call. Do not invoke it while holding a lock the main thread might want, and note that both overloads short-circuit to a direct `f()` when `is_main_thread()` is already true — no queueing, no guard, and no thread switch to reason about. The templated overload round-trips the result through `boost::any`, so `ReturnType` must be copy-constructible and the explicit template argument must match the function's return type exactly, or `boost::any_cast` throws `boost::bad_any_cast`.

`DISPATCH_GUI_FUN` needs its template argument spelled out at the call site and expands to an unbraced `if (...) return ...`. The `return` is the whole point and is easy to miss when reading a method that uses it; the missing braces mean that dropping the macro into an `if`/`else` chain without braces of its own will capture the `else`.

Responsibility for the GIL is uneven across the helpers. `to_QString`, `get_error_message` and `is_gui_object` each construct their own `PythonInterpreterLocker`; `qstring_to_python_string` does not, so the caller must already hold the GIL before it builds the `boost::python::str`. It also constructs from `QByteArray::constData()`, so an embedded NUL truncates the result.

`get_error_message` uses `PyErr_Fetch`, which *clears* the pending exception — it consumes the error rather than inspecting it, so call it once per caught `error_already_set` and not again afterwards. It fetches the traceback only to `Py_XDECREF` it, returns the literal `"Unknown error."` when either type or value came back null, and under Python 3 it checks `PyUnicode_Check` on the stringified object but then reads it with `PyBytes_AsString`, taking the value line from `value` rather than from the stringified `p_str`. Do not rely on the exact text.

`to_QString`'s Doxygen describes unicode/str/other handling with a decoding step and documents that it throws `boost::python::error_already_set`. The implementation does none of that: it extracts a `const char *` and calls `QString::fromUtf8`, and on `error_already_set` it warns and returns a default-constructed `QString`. A failed conversion is therefore indistinguishable from a genuinely empty string.

`run_startup_scripts` has no caller anywhere in the tree. `GPlatesGui::PythonManager` took over startup script discovery: it scans the same `paths/python_system_script_dir` and `paths/python_user_script_dir` preferences (plus the platform default system directory, and the `scripts/` subdirectory of the working directory) and collects them into a module list keyed by module name, instead of feeding each file to `PythonExecutionThread::exec_file`. Treat this function as dead code, and change `PythonManager` rather than this when startup-script behaviour needs to move.

Finally, `PythonUtils.h` includes `gui/PythonManager.h` and `python_manager()` dereferences the `GPlatesGui::PythonManager::instance()` singleton, so this header drags a `gui` dependency into every `api` translation unit that includes it.

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 109 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 106 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 82 |
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](../qt-widgets/TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 43 |
| [presentation/VisualLayers](../presentation/VisualLayers.md) | presentation | 31 |
| [gui/PythonManager](../gui/PythonManager.md) | gui | 24 |
| [qt-widgets/ModifyReconstructionPoleWidget](../qt-widgets/ModifyReconstructionPoleWidget.md) | qt-widgets | 21 |
| [api/PyApplication](PyApplication.md) | api | 20 |
| [api/PyViewportWindow](PyViewportWindow.md) | api | 18 |
| [api/PythonRunner](PythonRunner.md) | api | 16 |
| [gui/DrawStyleAdapters](../gui/DrawStyleAdapters.md) | gui | 16 |
| [presentation/VisualLayerRegistry](../presentation/VisualLayerRegistry.md) | presentation | 16 |
| [api/PyFunctions](PyFunctions.md) | api | 13 |
| [api/PythonExecutionMonitor](PythonExecutionMonitor.md) | api | 9 |
| [api/PythonExecutionThread](PythonExecutionThread.md) | api | 8 |
| [gui/DrawStyleManager](../gui/DrawStyleManager.md) | gui | 8 |
| [api/ConsoleWriter](ConsoleWriter.md) | api | 7 |
| [api/ConsoleReader](ConsoleReader.md) | api | 5 |
| [api/Sleeper](Sleeper.md) | api | 5 |
| [presentation/TopologyNetworkVisualLayerParams](../presentation/TopologyNetworkVisualLayerParams.md) | presentation | 5 |

*... and 12 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/api/PythonUtils.h
python scripts/gpq.py def GPlatesApi::PythonUtils::ThreadSwitchGuard --body
python scripts/gpq.py uses ThreadSwitchGuard --kind class
python scripts/gpq.py hier ThreadSwitchGuard
```
