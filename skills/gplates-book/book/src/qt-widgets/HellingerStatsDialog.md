# HellingerStatsDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1542 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/HellingerStatsDialog.h` | C++ | 63 |
| `src/qt-widgets/HellingerStatsDialog.cc` | C++ | 94 |
| `src/qt-widgets/HellingerStatsDialogUi.ui` | Qt form | 97 |

## Overview

[[[PROSE overview unit=qt-widgets/HellingerStatsDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::HellingerStatsDialog`](#gplatesqtwidgetshellingerstatsdialog) | class | `QDialog`<br>`Ui_HellingerStatsDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::HellingerStatsDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `HellingerStatsDialog( const QString &results_file, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `update()` | method | `void` | public | — |
| `handle_export()` | method | `void` | private | — |
| `d_results_file` | field | `QString` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_HELLINGERSTATSDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/HellingerStatsDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/HellingerDialog](HellingerDialog.md) | qt-widgets | 3 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `HellingerStatsDialog` | `QDialog` | Hellinger Calculation Details | 4 |

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_export` | `clicked()` | `this` | `handle_export()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/HellingerStatsDialog.h
python scripts/gpq.py def GPlatesQtWidgets::HellingerStatsDialog --body
python scripts/gpq.py uses HellingerStatsDialog --kind class
python scripts/gpq.py hier HellingerStatsDialog
```
