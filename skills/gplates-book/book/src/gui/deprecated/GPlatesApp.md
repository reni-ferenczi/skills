# GPlatesApp

[Book TOC](../../../TOC.md) · [gui](../../../components/gui.md) · cluster Community 215 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/deprecated/GPlatesApp.h` | C++ | 56 |
| `src/gui/deprecated/GPlatesApp.cc` | C++ | 147 |

## Overview

`GPlatesApp` is the wxWidgets application class that manages application lifecycle during startup and shutdown. wxWindows calls `OnInit()` to set up the application state, and `OnExit()` to tear it down. In builds compiled with `PACKAGE_IS_BETA`, `OnInit()` first shows a modal warning dialog and returns `FALSE` — aborting startup — if the user declines to continue. It then calls `fix_mesa_bug()` unconditionally before constructing a single `MainWindow`, showing it, registering it as the top window and handing it to `GPlatesControls::Lifetime::init()`. Exceptions escaping that construction are reported to standard error rather than crashing silently.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::GPlatesApp`](#gplatesguigplatesapp) | class | `wxApp` | — | 0 | — |

## Members

### `GPlatesGui::GPlatesApp`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `OnInit()` | method | `bool` | public | This function is called by wxWindows during the application's start-up ("initialisation") phase. |
| `OnExit()` | method | `int` | public | — |
| `d_main_win` | field | `MainWindow` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `fix_mesa_bug()` | function | `void` | Set the MESA\_NO\_SSE environment variable to 1 to circumvent a Mesa bug described at http://www.geosci.usyd.edu.au/users/hlaw/pmwiki/pmwiki.php?pagename=Main.NurbsBug This will have no effect on systems that do not have this bug, nor on ... |
| `GPLATES_GUI_GPLATESAPP_H` | macro | `None` | — |

## Notes

The source warns that the `try ... catch` in `OnInit()` can only catch exceptions thrown during the instantiation of `MainWindow`, not any thrown at a later stage; each of its three handlers (`GPlatesGlobal::Exception`, `std::exception`, `...`) prints to `std::cerr` and returns `FALSE`.

`GPlatesApp` owns the window, not the other way round: `d_main_win` is a private `MainWindow *` field, allocated in `OnInit()` and `delete`d in `OnExit()`.

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/deprecated/PolylineIntersections_test](../../maths/deprecated/PolylineIntersections_test.md) | maths | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/deprecated/GPlatesApp.h
python scripts/gpq.py def GPlatesGui::GPlatesApp --body
python scripts/gpq.py uses GPlatesApp --kind class
python scripts/gpq.py hier GPlatesApp
```
