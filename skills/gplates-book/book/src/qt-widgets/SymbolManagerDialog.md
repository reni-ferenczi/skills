# SymbolManagerDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1805 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/SymbolManagerDialog.h` | C++ | 60 |
| `src/qt-widgets/SymbolManagerDialog.cc` | C++ | 49 |
| `src/qt-widgets/SymbolManagerDialogUi.ui` | Qt form | 69 |

## Overview

A modeless dialog for managing drawing symbols, which may be used to configure marker appearance and other symbol properties. The dialog is built from a Qt Designer form and provides minimal code logic beyond connecting its close button to the `reject()` slot.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::SymbolManagerDialog`](#gplatesqtwidgetssymbolmanagerdialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_SymbolManagerDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::SymbolManagerDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SymbolManagerDialog( QWidget *parent = 0)` | constructor | `None` | public | — |
| `handle_close()` | method | `void` | private | — |
| `set_up_connections()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_SYMBOLMANAGERDIALOG_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Dialogs](../gui/Dialogs.md) | gui | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `SymbolManagerDialog` | `QDialog` | Manage Symbols | 5 |

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_close` | `clicked()` | `this` | `handle_close()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/SymbolManagerDialog.h
python scripts/gpq.py def GPlatesQtWidgets::SymbolManagerDialog --body
python scripts/gpq.py uses SymbolManagerDialog --kind class
python scripts/gpq.py hier SymbolManagerDialog
```
