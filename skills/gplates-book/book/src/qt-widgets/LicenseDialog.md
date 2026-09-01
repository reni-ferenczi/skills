# LicenseDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 0 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/LicenseDialog.h` | C++ | 56 |
| `src/qt-widgets/LicenseDialog.cc` | C++ | 52 |

## Overview

[[[PROSE overview unit=qt-widgets/LicenseDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=qt-widgets/LicenseDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
