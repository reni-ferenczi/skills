# Sleeper

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 59 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/api/Sleeper.h` | C++ | 55 |
| `src/api/Sleeper.cc` | C++ | 82 |

## Overview

This RAII class replaces Python's `time.sleep` with a custom implementation that enables thread interruption. The built-in `time.sleep` is non-interruptible by `PyThreadState_SetAsyncExc`, so the replacement breaks the requested sleep duration into small increments (10 per second), calling the original sleep repeatedly. This allows interruption checks to occur between micro-sleeps. The original `time.sleep` is saved on construction and restored on destruction.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesApi::Sleeper`](#gplatesapisleeper) | class | — | — | 0 | On construction, replaces Python's time.sleep with our own functor and on destruction restores the original time.sleep. |

## Members

### `GPlatesApi::Sleeper`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Sleeper()` | constructor | `None` | public | — |
| `~Sleeper()` | destructor | `None` | public | — |
| `d_old_object` | field | `boost::python::object` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_API_SLEEPER_H` | macro | `None` | — |

## Notes

All operations require `PythonInterpreterLocker` for GIL safety. The class should be instantiated early in Python initialization so that all subsequent `time.sleep` calls are interruptible. Errors in replacement or restoration are logged but do not throw.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/UtilitiesMenu](../gui/UtilitiesMenu.md) | gui | 2 |
| [qt-widgets/PythonConsoleDialog](../qt-widgets/PythonConsoleDialog.md) | qt-widgets | 2 |
| [api/PyApplication](PyApplication.md) | api | 1 |
| [api/PythonExecutionThread](PythonExecutionThread.md) | api | 1 |
| [api/PythonRunner](PythonRunner.md) | api | 1 |
| [entry-points/gplates_main](../entry-points/gplates_main.md) | entry-points | 1 |
| [gui/PythonManager](../gui/PythonManager.md) | gui | 1 |
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 1 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/api/Sleeper.h
python scripts/gpq.py def GPlatesApi::Sleeper --body
python scripts/gpq.py uses Sleeper --kind class
python scripts/gpq.py hier Sleeper
```
