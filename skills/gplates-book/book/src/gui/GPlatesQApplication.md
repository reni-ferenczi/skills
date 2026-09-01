# GPlatesQApplication

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 0 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/GPlatesQApplication.h` | C++ | 78 |
| `src/gui/GPlatesQApplication.cc` | C++ | 281 |

## Overview

Extends `QApplication` to provide exception handling for the Qt event loop and special event processing. The `notify()` method wraps event delivery in exception handling that catches uncaught `GPlatesGlobal::Exception`, `std::exception`, and unknown exceptions; reports them to the user via a message dialog (in release builds); and logs them with call stack traces (where available). In debug builds, exceptions are not caught to preserve debugger stack traces. The class also handles `DeferredCallEvent`s intended for the main thread and macOS-specific `FileOpen` events for opening projects from Finder.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::GPlatesQApplication`](#gplatesguigplatesqapplication) | class | `QApplication` | — | 0 | — |

## Members

### `GPlatesGui::GPlatesQApplication`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GPlatesQApplication( int &_argc, char **_argv)` | constructor | `None` | public | — |
| `notify( QObject *, QEvent *)` | method | `bool` | public | This Qt method is overridden in order to catch any uncaught exceptions in the Qt event handling thread. |
| `call_main( int (*main_function)(int, char* []), int argc, char* argv[])` | method | `int` | public | Calls the main-like function main\_function and handles any uncaught exceptions. |
| `event( QEvent *ev)` | method | `bool` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `try_catch( boost::function<ReturnType ()> func, QObject *qreceiver, QEvent *qevent)` | function | `ReturnType` | Call function func and process any uncaught exceptions. |
| `qapplication_notify( QApplication *qapplication, QObject *qreceiver, QEvent *qevent)` | function | `bool` | Convenience function to call base class QApplication::notify method. |
| `GPLATES_GUI_GPLATESQAPPLICATION_H` | macro | `None` | — |

## Notes

Exception handling behavior differs between debug and release builds: debug builds do not catch exceptions (except `NeedExitException`) to allow the debugger to capture the native stack trace; release builds catch all exceptions and exit after reporting them. The `notify()` method creates a `RenderedGeometryCollection::UpdateGuard` at the start of event processing to batch render updates across the single user interaction. `DeferredCallEvent`s are processed at the application level to avoid requiring each class that uses them to handle them separately.

## Used by

| Unit | Component | References |
|---|---|---|
| [entry-points/gplates_main](../entry-points/gplates_main.md) | entry-points | 5 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/GPlatesQApplication.h
python scripts/gpq.py def GPlatesGui::GPlatesQApplication --body
python scripts/gpq.py uses GPlatesQApplication --kind class
python scripts/gpq.py hier GPlatesQApplication
```
