# LeaveFullScreenButton

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1799 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/LeaveFullScreenButton.h` | C++ | 76 |
| `src/qt-widgets/LeaveFullScreenButtonUi.ui` | Qt form | 71 |

## Overview

A button widget displayed in the main window during full-screen mode. It provides a visible escape route from full-screen mode. The constructor wires the internal button's clicked signal to the widget's own clicked signal, allowing the caller to simply connect to the widget's signal rather than digging into the form. The widget is hidden by default and shown when full-screen mode is activated.

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

*None.*

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
