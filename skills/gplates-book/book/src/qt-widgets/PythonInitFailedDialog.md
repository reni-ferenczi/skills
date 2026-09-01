# PythonInitFailedDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1396 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/PythonInitFailedDialog.h` | C++ | 58 |
| `src/qt-widgets/PythonInitFailedDialog.cc` | C++ | 117 |
| `src/qt-widgets/PythonInitFailedDialogUi.ui` | Qt form | 80 |

## Overview

Modal dialog displayed when Python initialization fails at startup. It tells the user that GPlates will start up without Python support, and suggests checking the installation or setting the `python/python_home` preference if Python lives in an unusual location. `assemble_message()` builds the HTML by substituting the Python version reported by `GPlatesGui::PythonManager` into a template, along with an install instruction — an installer link on Windows, a package-manager command on macOS and Linux — selected at compile time. A "Do not show this dialog again" control lets the user suppress it on later startups; `gplates_main.cc` reads it through `show_again()` and passes the result to `PythonManager::set_show_init_fail_dlg()`.

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

Two traps in the naming. `show_again_button` is a `QRadioButton`, not a checkbox, and its label is the negative "Do not show this dialog again"; `show_again()` therefore inverts it — `return !show_again_button->isChecked();` — so a checked button means *do not* show again.

`assemble_message()` substitutes `$INSTALL_INSTRUCTION` only for python_version "2.6" or "2.7". Any other version (including the Python 3 versions GPlates 2.5 actually builds against) leaves the literal `$INSTALL_INSTRUCTION` placeholder in the HTML shown to the user.

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
