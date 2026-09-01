# TrinketArea

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1440 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/TrinketArea.h` | C++ | 139 |
| `src/gui/TrinketArea.cc` | C++ | 130 |

## Overview

Manages the status bar icon "trinkets" (small clickable indicators) in the `ViewportWindow`. Each trinket communicates application state: the unsaved-changes trinket signals pending edits, and the read-errors trinket indicates that files were loaded with errors. External code accesses these trinkets via `unsaved_changes_trinket()` and `read_errors_trinket()` to control their visibility and state.

The `init()` method must be called after `ViewportWindow::setupUi()` to connect buttons and menus, since it relies on UI elements that do not exist until layout has been performed. Both trinket icons are parented to the status bar and memory-managed by Qt.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::TrinketArea`](#gplatesguitrinketarea) | class | `QObject` | — | 0 | This GUI class manages the icons displayed in the QStatusBar of the ViewportWindow. |

## Members

### `GPlatesGui::TrinketArea`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TrinketArea( Dialogs &dialogs, GPlatesQtWidgets::ViewportWindow &viewport_window_, QObject *parent_ = NULL)` | constructor | `None` | public | — |
| `~TrinketArea()` | destructor | `None` | public | — |
| `init()` | method | `void` | public | Connects buttons, adds menus, etc. |
| `react_icon_clicked( GPlatesQtWidgets::TrinketIcon *icon, QMouseEvent *ev)` | method | `void` | private | — |
| `status_bar` | field | `QStatusBar` | private | Quick way to access the ViewportWindow's status bar. |
| `d_viewport_window_ptr` | field | `GPlatesQtWidgets::ViewportWindow` | private | Pointer to the ViewportWindow so we can access the status bar. |
| `d_trinket_unsaved` | field | `GPlatesQtWidgets::TrinketIcon` | private | Pointer to the "You have unsaved changes" TrinketIcon. |
| `d_trinket_read_errors` | field | `GPlatesQtWidgets::TrinketIcon` | private | Pointer to the "You loaded some files with read errors" TrinketIcon. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `create_unsaved_changes_trinket( GPlatesGui::Dialogs &dialogs)` | function | `GPlatesQtWidgets::TrinketIcon` | — |
| `create_read_errors_trinket( GPlatesGui::Dialogs &dialogs)` | function | `GPlatesQtWidgets::TrinketIcon` | — |
| `GPLATES_GUI_TRINKETAREA_H` | macro | `None` | — |

## Notes

The `init()` method must be called after `ViewportWindow::setupUi()` has completed, not in the constructor, because it depends on status bar and UI elements that only exist post-setup. Both trinket icons are parented to the status bar, so their lifetime is managed by Qt; do not delete them manually.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 3 |
| [gui/Dialogs](Dialogs.md) | gui | 1 |
| [gui/UnsavedChangesTracker](UnsavedChangesTracker.md) | gui | 1 |

## Related

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_trinket_read_errors` | `clicked(GPlatesQtWidgets::TrinketIcon *, QMouseEvent *)` | `this` | `react_icon_clicked(GPlatesQtWidgets::TrinketIcon *, QMouseEvent *)` |
| `d_trinket_unsaved` | `clicked(GPlatesQtWidgets::TrinketIcon *, QMouseEvent *)` | `this` | `react_icon_clicked(GPlatesQtWidgets::TrinketIcon *, QMouseEvent *)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/TrinketArea.h
python scripts/gpq.py def GPlatesGui::TrinketArea --body
python scripts/gpq.py uses TrinketArea --kind class
python scripts/gpq.py hier TrinketArea
```
