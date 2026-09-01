# LeaveFullScreenButton

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1799 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/LeaveFullScreenButton.h` | C++ | 76 |
| `src/qt-widgets/LeaveFullScreenButtonUi.ui` | Qt form | 71 |

## Overview

[[[PROSE overview unit=qt-widgets/LeaveFullScreenButton tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::LeaveFullScreenButton`](#gplatesqtwidgetsleavefullscreenbutton) | class | `QWidget`<br>`Ui_LeaveFullScreenButton` | — | 0 | This button appears in the main window during full-screen mode. |

## Members

### `GPlatesQtWidgets::LeaveFullScreenButton`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LeaveFullScreenButton( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~LeaveFullScreenButton()` | destructor | `None` | public | — |
| `clicked()` | method | `void` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_LEAVEFULLSCREENBUTTON_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/LeaveFullScreenButton tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ReconstructionViewWidget](ReconstructionViewWidget.md) | qt-widgets | 3 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `LeaveFullScreenButton` | `QWidget` | LeaveFullScreen | 2 |

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_leave_full_screen` | `clicked()` | — | `None` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/LeaveFullScreenButton.h
python scripts/gpq.py def GPlatesQtWidgets::LeaveFullScreenButton --body
python scripts/gpq.py uses LeaveFullScreenButton --kind class
python scripts/gpq.py hier LeaveFullScreenButton
```
