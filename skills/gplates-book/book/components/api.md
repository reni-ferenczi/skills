# api

[Book TOC](../TOC.md)

23 unit page(s), 35 source file(s) documented here, 1 further file(s) listed below.

## Overview

[[[PROSE component unit=component:api tier=1]]]
Replace this whole block, markers included, with 2-4 paragraphs: what this component is responsible for, the load-bearing units and how it connects to neighbouring components. Do not restate the unit table.
[[[/PROSE]]]

## Units

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [AbstractConsole](../src/api/AbstractConsole.md) | 2 | 84 | 41 | (pending) |
| [AbstractPythonRunner](../src/api/AbstractPythonRunner.md) | 2 | 155 | 62 | (pending) |
| [CoReg](../src/api/CoReg.md) | 3 | 578 | 1 | Python binding export for co-registration functionality |
| [ConsoleReader](../src/api/ConsoleReader.md) | 3 | 182 | 1 | Python object that intercepts stdin for interactive console input |
| [ConsoleWriter](../src/api/ConsoleWriter.md) | 3 | 196 | 3 | Captures Python output by redirecting sys.stdout or sys.stderr |
| [DeferredApiCall](../src/api/DeferredApiCall.md) | 3 | 161 | 11 | Mechanism for wrapping Qt-dependent functions for main-thread execution from Python |
| [DeferredApiCallImpl](../src/api/DeferredApiCallImpl.md) | 3 | 799 | 1 | Template metaprogramming implementation for deferred API calls with 0-10 parameter arities |
| [PyApplication](../src/api/PyApplication.md) | 3 | 286 | 0 | Python wrapper for application state and lifecycle operations |
| [PyColour](../src/api/PyColour.md) | 2 | 169 | 49 | (pending) |
| [PyCoregistrationLayerProxy](../src/api/PyCoregistrationLayerProxy.md) | 3 | 217 | 0 | Python wrapper exposing co-registration layer results including seed features and data |
| [PyFeature](../src/api/PyFeature.md) | 2 | 418 | 27 | (pending) |
| [PyFeatureCollection](../src/api/PyFeatureCollection.md) | 3 | 138 | 9 | Python wrapper providing safe access to feature collections from Python |
| [PyFunctions](../src/api/PyFunctions.md) | 3 | 303 | 0 | Python bindings for forward and reverse reconstruction workflows |
| [PyTopologyTools](../src/api/PyTopologyTools.md) | 3 | 78 | 0 | Python utility for extracting topology section information from features |
| [PyViewportWindow](../src/api/PyViewportWindow.md) | 3 | 250 | 0 | Python wrapper for GUI viewport and camera controls |
| [Python](../src/api/Python.md) | 3 | 80 | 0 | Module initialization for pygplates, the standalone Python extension |
| [PythonExecutionMonitor](../src/api/PythonExecutionMonitor.md) | 2 | 453 | 21 | (pending) |
| [PythonExecutionThread](../src/api/PythonExecutionThread.md) | 2 | 545 | 16 | (pending) |
| [PythonInterpreterLocker](../src/api/PythonInterpreterLocker.md) | 2 | 176 | 85 | (pending) |
| [PythonInterpreterUnlocker](../src/api/PythonInterpreterUnlocker.md) | 2 | 159 | 14 | (pending) |
| [PythonRunner](../src/api/PythonRunner.md) | 3 | 658 | 3 | Executes Python code with GIL management and interactive console support |
| [PythonUtils](../src/api/PythonUtils.md) | 1 | 416 | 574 | (pending) |
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
