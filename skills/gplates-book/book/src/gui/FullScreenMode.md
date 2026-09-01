# FullScreenMode

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 941 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/FullScreenMode.h` | C++ | 170 |
| `src/gui/FullScreenMode.cc` | C++ | 238 |

## Overview

[[[PROSE overview unit=gui/FullScreenMode tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::FullScreenMode`](#gplatesguifullscreenmode) | class | `QObject` | — | 0 | This GUI class encapsulates the ability for GPlates to make the main window into a full-screen window without decorations, suitable for presentations and the like. |

## Members

### `GPlatesGui::FullScreenMode`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FullScreenMode( GPlatesQtWidgets::ViewportWindow &viewport_window_, QObject *parent_ = NULL)` | constructor | `None` | public | — |
| `~FullScreenMode()` | destructor | `None` | public | — |
| `init()` | method | `void` | public | Connects buttons, adds menus, etc. |
| `leave_full_screen()` | method | `void` | public | — |
| `toggle_full_screen( bool wants_full_screen)` | method | `void` | public | — |
| `gmenu_button` | field | `QWidget` | private | Quick method to get at the GMenuButton from inside this class. |
| `leave_full_screen_button` | field | `QWidget` | private | Quick method to get at the LeaveFullScreenButton from inside this class. |
| `reconstruction_view_widget` | field | `QWidget` | private | Quick method to get at the ReconstructionViewWidget from inside this class. |
| `full_screen_action` | field | `QAction` | private | Quick method to get at the Full Screen QAction from inside this class. |
| `d_viewport_window_ptr` | field | `GPlatesQtWidgets::ViewportWindow` | private | Pointer to the window we should be full-screening. |
| `d_viewport_state` | field | `QByteArray` | private | Main window's state, serialised by Qt's saveState() method. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_full_screen_widgets_to_hide()` | function | `QStringList` | This anonymous namespace function is called once to init a static list of widgets in FullScreenMode::toggle\_full\_screen(). |
| `get_actions_to_disable()` | function | `QStringList` | Same as above, but for actions attached to menus. |
| `GPLATES_GUI_FULLSCREENMODE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/FullScreenMode tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 11 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&leave_full_screen_button()` | `clicked()` | `this` | `leave_full_screen()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/FullScreenMode.h
python scripts/gpq.py def GPlatesGui::FullScreenMode --body
python scripts/gpq.py uses FullScreenMode --kind class
python scripts/gpq.py hier FullScreenMode
```
