# GuiCalls

[Book TOC](../../../TOC.md) · [deprecated](../../../components/deprecated.md) · cluster Community 365 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/deprecated/controls/GuiCalls.h` | C++ | 87 |
| `src/deprecated/controls/GuiCalls.cc` | C++ | 87 |

## Overview

[[[PROSE overview unit=deprecated/controls/GuiCalls tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=deprecated/controls/GuiCalls tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
