# PythonReadlineDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1720 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/PythonReadlineDialog.h` | C++ | 61 |
| `src/qt-widgets/PythonReadlineDialog.cc` | C++ | 68 |
| `src/qt-widgets/PythonReadlineDialogUi.ui` | Qt form | 83 |

## Overview

Modal dialog for getting a single line of user input, used by the embedded Python console. It displays a prompt (truncated to 50 characters) and an input line edit. The dialog returns the entered text with a newline appended and remembers its window position across successive invocations.

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

*None.*

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
