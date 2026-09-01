# AboutDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 0 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/AboutDialog.h` | C++ | 64 |
| `src/qt-widgets/AboutDialog.cc` | C++ | 62 |
| `src/qt-widgets/AboutDialogUi.ui` | Qt form | 249 |

## Overview

[[[PROSE overview unit=qt-widgets/AboutDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::AboutDialog`](#gplatesqtwidgetsaboutdialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_AboutDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::AboutDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AboutDialog( GPlatesGui::Dialogs &dialogs, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `d_license_dialog_ptr` | field | `QPointer<LicenseDialog>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_ABOUTDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/AboutDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/deprecated/MainWindow](../gui/deprecated/MainWindow.md) | gui | 2 |
| [gui/Dialogs](../gui/Dialogs.md) | gui | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `AboutDialog` | `QDialog` | About GPlates | 9 |

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_License` | `clicked()` | `d_license_dialog_ptr` | `show()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/AboutDialog.h
python scripts/gpq.py def GPlatesQtWidgets::AboutDialog --body
python scripts/gpq.py uses AboutDialog --kind class
python scripts/gpq.py hier AboutDialog
```
