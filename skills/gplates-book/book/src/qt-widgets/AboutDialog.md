# AboutDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 0 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/AboutDialog.h` | C++ | 64 |
| `src/qt-widgets/AboutDialog.cc` | C++ | 62 |
| `src/qt-widgets/AboutDialogUi.ui` | Qt form | 249 |

## Overview

Modal dialog displaying application version and copyright information. The constructor sets the GPlates version label from the global version string, fetches the GPGIM version from `Gpgim::instance()`, and populates a text box with the HTML copyright notice. A License button in the dialog opens a full `LicenseDialog` on click through a `QPointer<LicenseDialog>` member.

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

*None.*

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
