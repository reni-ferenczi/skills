# PythonUtils

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 59 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/api/PythonUtils.h` | C++ | 187 |
| `src/api/PythonUtils.cc` | C++ | 229 |

## Overview

[[[PROSE overview unit=api/PythonUtils tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=api/PythonUtils tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
