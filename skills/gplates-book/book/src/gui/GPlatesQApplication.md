# GPlatesQApplication

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 0 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/GPlatesQApplication.h` | C++ | 78 |
| `src/gui/GPlatesQApplication.cc` | C++ | 281 |

## Overview

[[[PROSE overview unit=gui/GPlatesQApplication tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=gui/GPlatesQApplication tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
