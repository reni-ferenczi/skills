# PythonReadlineDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1720 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/PythonReadlineDialog.h` | C++ | 61 |
| `src/qt-widgets/PythonReadlineDialog.cc` | C++ | 68 |
| `src/qt-widgets/PythonReadlineDialogUi.ui` | Qt form | 83 |

## Overview

[[[PROSE overview unit=qt-widgets/PythonReadlineDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::PythonReadlineDialog`](#gplatesqtwidgetspythonreadlinedialog) | class | `QDialog`<br>`Ui_PythonReadlineDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::PythonReadlineDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PythonReadlineDialog( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `get_line( const QString &prompt)` | method | `QString` | public | Opens this dialog as modal and returns the string that the user enters. |
| `d_pos` | field | `QPoint` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_PYTHONREADLINEDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/PythonReadlineDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/PythonConsoleDialog](PythonConsoleDialog.md) | qt-widgets | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `PythonReadlineDialog` | `QDialog` | Python Readline | 4 |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/PythonReadlineDialog.h
python scripts/gpq.py def GPlatesQtWidgets::PythonReadlineDialog --body
python scripts/gpq.py uses PythonReadlineDialog --kind class
python scripts/gpq.py hier PythonReadlineDialog
```
