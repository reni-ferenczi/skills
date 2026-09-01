# LicenseDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 0 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/LicenseDialog.h` | C++ | 56 |
| `src/qt-widgets/LicenseDialog.cc` | C++ | 52 |

## Overview

A modal dialog that displays the GNU General Public License version 2 text. It inherits from `GPlatesDialog` and uses the `Ui_InformationDialog` form to present the license text in a text widget. The dialog is typically invoked from `AboutDialog` to show the full license terms to the user.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::LicenseDialog`](#gplatesqtwidgetslicensedialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_InformationDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::LicenseDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LicenseDialog( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~LicenseDialog()` | destructor | `None` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_LICENSEDIALOG_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/AboutDialog](AboutDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/LicenseDialog.h
python scripts/gpq.py def GPlatesQtWidgets::LicenseDialog --body
python scripts/gpq.py uses LicenseDialog --kind class
python scripts/gpq.py hier LicenseDialog
```
