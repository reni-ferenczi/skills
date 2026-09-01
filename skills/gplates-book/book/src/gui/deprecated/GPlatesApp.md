# GPlatesApp

[Book TOC](../../../TOC.md) · [gui](../../../components/gui.md) · cluster Community 215 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/deprecated/GPlatesApp.h` | C++ | 56 |
| `src/gui/deprecated/GPlatesApp.cc` | C++ | 147 |

## Overview

`GPlatesApp` is the wxWidgets application class that manages application lifecycle during startup and shutdown. When wxWindows begins execution, it calls `OnInit()` to set up the application state, and `OnExit()` to tear it down. During initialization, `GPlatesApp` creates a single `MainWindow` instance, shows it to the user, and registers it as the top window. It applies a Mesa graphics library workaround if needed, and catches any exceptions thrown during the main window construction, reporting them to standard error rather than crashing silently.

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

`OnInit()` catches `GPlatesGlobal::Exception`, `std::exception`, and all other exceptions, preventing any throw from propagating beyond the initialization phase. The `MainWindow` owns the `d_main_win` pointer and the window is deleted in `OnExit()`. The Mesa workaround (`fix_mesa_bug()`) sets an environment variable to disable SSE optimizations in Mesa, which has no effect on systems without Mesa or unaffected by the bug.

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
