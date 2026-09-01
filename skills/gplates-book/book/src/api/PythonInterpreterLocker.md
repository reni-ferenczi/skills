# PythonInterpreterLocker

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 1470 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/api/PythonInterpreterLocker.h` | C++ | 102 |
| `src/api/PythonInterpreterLocker.cc` | C++ | 74 |

## Overview

`GPlatesApi::PythonInterpreterLocker` is an RAII wrapper around Python's
`PyGILState_Ensure`/`PyGILState_Release`, the pair of calls a thread that
Python itself did not create must make before touching any Python C API and
after it is done. GPlates runs Python from GUI-created threads (see
`PythonExecutionThread`, `HellingerThread`), so any code path that calls into
the interpreter from one of those threads wraps the call in a
`PythonInterpreterLocker` rather than calling the GIL functions directly; its
wide fan-in reflects how many places in the codebase need to cross back into
the interpreter this way.

Passing `false` to the constructor skips the automatic `ensure()`, letting a
caller call `ensure()` and `release()` explicitly at chosen points while still
getting the destructor's automatic cleanup if `release()` was never reached
(for example, on an exception).

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

`ensure()` must not be called twice on the same instance without an
intervening `release()`; a thread may nest multiple *separate*
`PythonInterpreterLocker` instances, since each `PyGILState_Ensure` call just
needs a matching `PyGILState_Release`. The destructor only releases the GIL if
this instance currently holds it (`d_has_gil`), so constructing with
`ensure_ = false` and never calling `ensure()` is safe and a no-op.

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
