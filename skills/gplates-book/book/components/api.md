# api

[Book TOC](../TOC.md)

23 unit page(s), 35 source file(s) documented here, 1 further file(s) listed below.

## Overview

`api` is GPlates' embedded-Python bridge: it hosts a CPython interpreter inside the application, dispatches work safely between the interpreter and the Qt GUI thread, and exposes GPlates' model and application state to Python as Boost.Python bindings. Its job is not reconstruction logic itself but the plumbing that lets a script — typed into the interactive console, loaded from a startup script, or driving `pygplates` as a standalone extension — reach into that logic and back out again without violating the GIL or Qt's single-threaded-widget rule.

The threading and locking machinery is what the rest of the component is built on. `PythonUtils` is the shim everything else rests on: it converts between `QString` and Python strings, turns a pending exception into loggable text, and — via `run_in_main_thread` and the `DISPATCH_GUI_FUN` macro — marshals a call from the Python execution thread onto the Qt main thread and back. `PythonInterpreterLocker` and `PythonInterpreterUnlocker` are the RAII guards, acquiring and releasing the GIL respectively, that every one of those crossings wraps itself in. `AbstractPythonRunner` defines the shape of "run some Python" (interactive command, string, file, or native callable) that `PythonExecutionThread` implements as a dedicated `QThread` running its own event loop, and `PythonExecutionMonitor` is what lets the GUI thread hand a job to that thread and stay responsive while waiting, rather than blocking outright. `AbstractConsole` decouples the interactive console's input/output from whatever widget or headless stream is actually showing it. On top of that infrastructure sit the individual bindings — `PyFeature` and `PyFeatureCollection` wrap `FeatureHandle` and `FeatureCollectionHandle` as safe, weak-reference-holding Python objects, and `PyColour` exports `GPlatesGui::Colour` and its palette and draw-style machinery — plus `CoReg`, `PyFunctions`, `PyApplication` and `PyViewportWindow`, which expose co-registration, reconstruction workflows, application lifecycle and viewport control respectively.

`api`'s heaviest dependencies read as a map of what it wraps: `data-mining` for the co-registration types `CoReg` and `PyCoregistrationLayerProxy` bind, `gui` for `PythonManager`, `Colour` and `DrawStyle`, `model` for the feature and property types `PyFeature` and `PyFeatureCollection` wrap, `app-logic` for the reconstruction workflows `PyFunctions` drives, and `feature-visitors` for the property-to-Python conversion (`GetPropertyAsPythonObjVisitor`, `ShapefileAttributeFinder`) that `PyFeature` relies on. The relationship with `gui` runs both ways: `PythonUtils.h` itself includes `gui/PythonManager.h`, so every translation unit in `api` that touches thread dispatch already depends on `gui`, and `gui/PythonManager` and `gui/DrawStyleAdapters` are in turn among `api`'s heaviest callers. `presentation` and `qt-widgets` are the other big callers, reaching into `PythonUtils` (for cross-thread dispatch), `PyColour` and `PyFeature` from widgets and layer code that need to call into or be called from Python; `utils` calls back in through `GetPropertyAsPythonObjVisitor` for the same property-conversion path `PyFeature` uses internally.

## Units

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [AbstractConsole](../src/api/AbstractConsole.md) | 2 | 84 | 41 | Interface for pluggable Python console I/O, implemented by GUI and headless consoles |
| [AbstractPythonRunner](../src/api/AbstractPythonRunner.md) | 2 | 155 | 62 | Interface for running Python code (string, file, function) monitored asynchronously |
| [CoReg](../src/api/CoReg.md) | 3 | 578 | 1 | Python binding export for co-registration functionality |
| [ConsoleReader](../src/api/ConsoleReader.md) | 3 | 182 | 1 | Python object that intercepts stdin for interactive console input |
| [ConsoleWriter](../src/api/ConsoleWriter.md) | 3 | 196 | 3 | Captures Python output by redirecting sys.stdout or sys.stderr |
| [DeferredApiCall](../src/api/DeferredApiCall.md) | 3 | 161 | 11 | Mechanism for wrapping Qt-dependent functions for main-thread execution from Python |
| [DeferredApiCallImpl](../src/api/DeferredApiCallImpl.md) | 3 | 799 | 1 | Template metaprogramming implementation for deferred API calls with 0-10 parameter arities |
| [PyApplication](../src/api/PyApplication.md) | 3 | 286 | 0 | Python wrapper for application state and lifecycle operations |
| [PyColour](../src/api/PyColour.md) | 2 | 169 | 49 | Boost.Python bindings for named Colour constants, Palette and DrawStyle |
| [PyCoregistrationLayerProxy](../src/api/PyCoregistrationLayerProxy.md) | 3 | 217 | 0 | Python wrapper exposing co-registration layer results including seed features and data |
| [PyFeature](../src/api/PyFeature.md) | 2 | 418 | 27 | Python wrapper exposing a feature handle's id, type, time range, plate id and properties |
| [PyFeatureCollection](../src/api/PyFeatureCollection.md) | 3 | 138 | 9 | Python wrapper providing safe access to feature collections from Python |
| [PyFunctions](../src/api/PyFunctions.md) | 3 | 303 | 0 | Python bindings for forward and reverse reconstruction workflows |
| [PyTopologyTools](../src/api/PyTopologyTools.md) | 3 | 78 | 0 | Python utility for extracting topology section information from features |
| [PyViewportWindow](../src/api/PyViewportWindow.md) | 3 | 250 | 0 | Python wrapper for GUI viewport and camera controls |
| [Python](../src/api/Python.md) | 3 | 80 | 0 | Module initialization for pygplates, the standalone Python extension |
| [PythonExecutionMonitor](../src/api/PythonExecutionMonitor.md) | 2 | 453 | 21 | Local Qt event loop that lets the GUI thread wait for a Python job without blocking events |
| [PythonExecutionThread](../src/api/PythonExecutionThread.md) | 2 | 545 | 16 | QThread that owns the Python interpreter's execution context and dispatches jobs to it |
| [PythonInterpreterLocker](../src/api/PythonInterpreterLocker.md) | 2 | 176 | 85 | RAII guard around PyGILState\_Ensure/Release for calling into Python from non-Python threads |
| [PythonInterpreterUnlocker](../src/api/PythonInterpreterUnlocker.md) | 2 | 159 | 14 | RAII guard around PyEval\_SaveThread/RestoreThread to release the GIL during non-Python work |
| [PythonRunner](../src/api/PythonRunner.md) | 3 | 658 | 3 | Executes Python code with GIL management and interactive console support |
| [PythonUtils](../src/api/PythonUtils.md) | 1 | 416 | 574 | GIL-aware helpers bridging the embedded interpreter to the Qt main thread, plus string and error conversion |
| [Sleeper](../src/api/Sleeper.md) | 3 | 137 | 0 | Makes Python time.sleep interruptible by replacing it with incremental micro-sleeps |

## Other files

| File | Kind | Lines |
|---|---|---|
| `src/api/CMakeLists.txt` | build | 50 |

## Depends on

| Component | References |
|---|---|
| [utils](utils.md) | 333 |
| [data-mining](data-mining.md) | 166 |
| [gui](gui.md) | 157 |
| [model](model.md) | 147 |
| [app-logic](app-logic.md) | 120 |
| [global](global.md) | 74 |
| [file-io](file-io.md) | 56 |
| [feature-visitors](feature-visitors.md) | 40 |
| [qt-widgets](qt-widgets.md) | 30 |
| [presentation](presentation.md) | 15 |
| [maths](maths.md) | 7 |
| [opengl](opengl.md) | 6 |
| [unit-test](unit-test.md) | 5 |
| [property-values](property-values.md) | 5 |

## Used by

| Component | References |
|---|---|
| [presentation](presentation.md) | 277 |
| [qt-widgets](qt-widgets.md) | 159 |
| [gui](gui.md) | 155 |
| [utils](utils.md) | 82 |
| [app-logic](app-logic.md) | 4 |
| [entry-points](entry-points.md) | 4 |
| [file-io](file-io.md) | 3 |

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py tree src/api
python scripts/gpq.py sym . --mode sub --path src/api --defs-only
```
