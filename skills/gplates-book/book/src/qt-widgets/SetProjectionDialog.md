# SetProjectionDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 829 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/SetProjectionDialog.h` | C++ | 99 |
| `src/qt-widgets/SetProjectionDialog.cc` | C++ | 136 |
| `src/qt-widgets/SetProjectionDialogUi.ui` | Qt form | 102 |

## Overview

[[[PROSE overview unit=qt-widgets/SetProjectionDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::SetProjectionDialog`](#gplatesqtwidgetssetprojectiondialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_SetProjectionDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::SetProjectionDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SetProjectionDialog( ViewportWindow &viewport_window, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~SetProjectionDialog()` | destructor | `None` | public | — |
| `setup()` | method | `void` | public | Call this prior to displaying the dialog, so we can set the widgets to their appropriate states. |
| `set_projection( GPlatesGui::MapProjection::Type projection_type)` | method | `void` | public | — |
| `set_central_meridian( double central_meridian)` | method | `void` | public | — |
| `get_projection_type()` | method | `GPlatesGui::MapProjection::Type` | public | — |
| `central_meridian()` | method | `double` | public | — |
| `update_central_meridian_status()` | method | `void` | private | Disables the central\_meridian spinbox when the Orthographic projection is selected. |
| `d_viewport_window_ptr` | field | `ViewportWindow` | private | View state |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_SETPROJECTIONDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/SetProjectionDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Dialogs](../gui/Dialogs.md) | gui | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `SetProjectionDialog` | `QDialog` | Set Projection | 7 |

**Qt signal/slot connections** (3 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `combo_projection` | `currentIndexChanged(int)` | `this` | `update_central_meridian_status()` |
| `main_buttonbox` | `accepted()` | `this` | `accept()` |
| `main_buttonbox` | `rejected()` | `this` | `reject()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/SetProjectionDialog.h
python scripts/gpq.py def GPlatesQtWidgets::SetProjectionDialog --body
python scripts/gpq.py uses SetProjectionDialog --kind class
python scripts/gpq.py hier SetProjectionDialog
```
