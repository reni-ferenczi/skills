# GuiCalls

[Book TOC](../../../TOC.md) · [deprecated](../../../components/deprecated.md) · cluster Community 365 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/deprecated/controls/GuiCalls.h` | C++ | 87 |
| `src/deprecated/controls/GuiCalls.cc` | C++ | 87 |

## Overview

A static callback interface allowing deprecated control classes to invoke methods on GUI components (`MainWindow` and `GLCanvas`) without direct dependencies. All operations are no-ops if components have not been set via `SetComponents()`. Used by `AnimationTimer` to update display state and by other control code to coordinate GUI updates.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesControls::GuiCalls`](#gplatescontrolsguicalls) | class | — | — | 0 | A collection of the calls which the GUI-controls must make back to the GUI. |

## Members

### `GPlatesControls::GuiCalls`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RepaintCanvas()` | method | `void` | public | Repaint the GUI canvas. |
| `SetCurrentTime(const GPlatesGlobal::fpdata_t &t)` | method | `void` | public | Set the current geological time, as displayed in the main GUI window. |
| `SetComponents(GPlatesGui::MainWindow *window, GPlatesGui::GLCanvas *canvas)` | method | `void` | public | Set the main GUI window and the GUI canvas. |
| `SetOpModeToAnimation()` | method | `void` | public | Set the current mode of operation to 'animation'. |
| `ReturnOpModeToNormal()` | method | `void` | public | Return the current mode of operation to 'normal'. |
| `StopAnimation(bool interrupted)` | method | `void` | public | Notify the main window that the animation has been stopped. |
| `_window` | field | `GPlatesGui::MainWindow` | private | — |
| `_canvas` | field | `GPlatesGui::GLCanvas` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_window` | variable | `GPlatesGui::MainWindow` | — |
| `_canvas` | variable | `GPlatesGui::GLCanvas` | — |
| `_GPLATES_CONTROLS_GUICALLS_H_` | macro | `None` | — |

## Notes

All methods safely handle NULL pointers by checking before use. `RepaintCanvas()` posts a `wxPaintEvent` to the canvas rather than calling a paint method directly. Static member pointers are initialized to NULL and must be set by calling `SetComponents()` before the other methods will have effect.

## Used by

| Unit | Component | References |
|---|---|---|
| [deprecated/controls/AnimationTimer](AnimationTimer.md) | deprecated | 11 |
| [gui/deprecated/MainWindow](../../gui/deprecated/MainWindow.md) | gui | 10 |
| [deprecated/controls/Reconstruct](Reconstruct.md) | deprecated | 9 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/deprecated/controls/GuiCalls.h
python scripts/gpq.py def GPlatesControls::GuiCalls --body
python scripts/gpq.py uses GuiCalls --kind class
python scripts/gpq.py hier GuiCalls
```
