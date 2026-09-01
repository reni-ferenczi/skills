# PythonInitFailedDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1396 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/PythonInitFailedDialog.h` | C++ | 58 |
| `src/qt-widgets/PythonInitFailedDialog.cc` | C++ | 117 |
| `src/qt-widgets/PythonInitFailedDialogUi.ui` | Qt form | 80 |

## Overview

[[[PROSE overview unit=qt-widgets/PythonInitFailedDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::PythonInitFailedDialog`](#gplatesqtwidgetspythoninitfaileddialog) | class | `QDialog`<br>`Ui_PythonInitFailedDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::PythonInitFailedDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PythonInitFailedDialog( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `show_again()` | method | `bool` | public | — |
| `assemble_message()` | method | `void` | protected | — |
| `d_html_page` | field | `QString` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `python_failed_msg` | variable | `char` | — |
| `python26_install_instructions_win` | variable | `char` | — |
| `python27_install_instructions_win` | variable | `char` | — |
| `python26_install_instructions_mac` | variable | `char` | — |
| `python27_install_instructions_mac` | variable | `char` | — |
| `python26_install_instructions_linux` | variable | `char` | — |
| `python27_install_instructions_linux` | variable | `char` | — |
| `GPLATES_QTWIDGETS_PYTHONINITFAILEDDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/PythonInitFailedDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [entry-points/gplates_main](../entry-points/gplates_main.md) | entry-points | 4 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `PythonInitFailedDialog` | `QDialog` | Python Initialization Failed | 4 |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/PythonInitFailedDialog.h
python scripts/gpq.py def GPlatesQtWidgets::PythonInitFailedDialog --body
python scripts/gpq.py uses PythonInitFailedDialog --kind class
python scripts/gpq.py hier PythonInitFailedDialog
```
