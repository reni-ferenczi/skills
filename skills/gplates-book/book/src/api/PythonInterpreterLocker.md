# PythonInterpreterLocker

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 1470 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/api/PythonInterpreterLocker.h` | C++ | 102 |
| `src/api/PythonInterpreterLocker.cc` | C++ | 74 |

## Overview

[[[PROSE overview unit=api/PythonInterpreterLocker tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesApi::PythonInterpreterLocker`](#gplatesapipythoninterpreterlocker) | class | — | — | 0 | A wrapper around Python's PyGILState\_Ensure (which ensures that the calling thread is ready to call Python C API functions by acquiring the Global Interpreter Lock (GIL) for the current thread) and PyGILState\_Release (which releases the ... |

## Members

### `GPlatesApi::PythonInterpreterLocker`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PythonInterpreterLocker( bool ensure_ = true)` | constructor | `None` | public | Constructs a PythonInterpreterLocker. |
| `~PythonInterpreterLocker()` | destructor | `None` | public | Releases the GIL if we have acquired the GIL, i.e. ensure has been called but release has not been called. |
| `ensure()` | method | `void` | public | Ensures that the calling thread is ready to call Python C API functions by acquiring the Global Interpreter Lock (GIL). |
| `release()` | method | `void` | public | Releases the Global Interpreter Lock (GIL). |
| `d_has_gil` | field | `bool` | private | — |
| `d_gil_state` | field | `PyGILState_STATE` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_API_PYTHONINTERPRETERLOCKER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=api/PythonInterpreterLocker tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/PythonConfiguration](../gui/PythonConfiguration.md) | gui | 15 |
| [api/DeferredApiCallImpl](DeferredApiCallImpl.md) | api | 12 |
| [api/PythonRunner](PythonRunner.md) | api | 11 |
| [qt-widgets/HellingerThread](../qt-widgets/HellingerThread.md) | qt-widgets | 10 |
| [gui/DrawStyleAdapters](../gui/DrawStyleAdapters.md) | gui | 8 |
| [api/Sleeper](Sleeper.md) | api | 7 |
| [gui/PythonManager](../gui/PythonManager.md) | gui | 7 |
| [api/PyApplication](PyApplication.md) | api | 6 |
| [api/PythonUtils](PythonUtils.md) | api | 5 |
| [gui/DrawStyleManager](../gui/DrawStyleManager.md) | gui | 5 |
| [api/ConsoleReader](ConsoleReader.md) | api | 4 |
| [api/ConsoleWriter](ConsoleWriter.md) | api | 4 |
| [api/PythonExecutionThread](PythonExecutionThread.md) | api | 3 |
| [entry-points/gplates_main](../entry-points/gplates_main.md) | entry-points | 3 |
| [api/PythonExecutionMonitor](PythonExecutionMonitor.md) | api | 1 |
| [gui/UtilitiesMenu](../gui/UtilitiesMenu.md) | gui | 1 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 1 |
| [qt-widgets/HellingerDialog](../qt-widgets/HellingerDialog.md) | qt-widgets | 1 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/api/PythonInterpreterLocker.h
python scripts/gpq.py def GPlatesApi::PythonInterpreterLocker --body
python scripts/gpq.py uses PythonInterpreterLocker --kind class
python scripts/gpq.py hier PythonInterpreterLocker
```
