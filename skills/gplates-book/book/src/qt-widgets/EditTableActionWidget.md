# EditTableActionWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1109 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditTableActionWidget.h` | C++ | 79 |
| `src/qt-widgets/EditTableActionWidget.cc` | C++ | 66 |
| `src/qt-widgets/EditTableActionWidgetUi.ui` | Qt form | 113 |

## Overview

`EditTableActionWidget` is a small per-row toolbar (insert above, insert below, delete) meant to be embedded as a cell widget inside a `QTableWidget` owned by an `EditTableWidget`. Each button's `clicked()` signal is wired in the constructor to one of the three slots, which simply forward the request to the owning `EditTableWidget` via `handle_insert_row_above()`, `handle_insert_row_below()` and `handle_delete_row()`, passing `this` so the table widget knows which row the action came from.

The widget holds no editing state itself; it is purely a dispatcher that lets each table row carry its own row-management controls without the table widget having to track button identity by position.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::EditTableActionWidget`](#gplatesqtwidgetsedittableactionwidget) | class | `QWidget`<br>`Ui_EditTableActionWidget` | — | 1 | — |

## Members

### `GPlatesQtWidgets::EditTableActionWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EditTableActionWidget( EditTableWidget *table_widget, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~EditTableActionWidget()` | destructor | `None` | public | Note that since we are adding these ActionWidgets with a QWidget parent, and then setting them as a cell widget inside the list-of-points QTableWidget, Qt will kindly manage the memory for us. |
| `insert_row_above()` | method | `void` | public | — |
| `insert_row_below()` | method | `void` | public | — |
| `delete_row()` | method | `void` | public | — |
| `d_table_widget_ptr` | field | `EditTableWidget` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_EDITTABLEACTIONWIDGET_H` | macro | `None` | — |

## Notes

Ownership is implicit rather than enforced: the destructor comment records that because instances are constructed with a `QWidget` parent and then installed as a cell widget in the list-of-points table, Qt's parent-child ownership deletes them automatically, so callers must not delete an `EditTableActionWidget` themselves.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/EditTotalReconstructionSequenceWidget](EditTotalReconstructionSequenceWidget.md) | qt-widgets | 46 |
| [qt-widgets/EditTimeSequenceWidget](EditTimeSequenceWidget.md) | qt-widgets | 16 |
| [qt-widgets/EditTotalReconstructionSequenceDialog](EditTotalReconstructionSequenceDialog.md) | qt-widgets | 9 |
| [qt-widgets/EditGeometryWidget](EditGeometryWidget.md) | qt-widgets | 2 |
| [qt-widgets/EditStringListWidget](EditStringListWidget.md) | qt-widgets | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `EditTableActionWidget` | `QWidget` | Feature Collection Actions | 4 |

**Qt signal/slot connections** (3 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_insert_above` | `clicked()` | `this` | `insert_row_above()` |
| `button_insert_below` | `clicked()` | `this` | `insert_row_below()` |
| `button_delete` | `clicked()` | `this` | `delete_row()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/EditTableActionWidget.h
python scripts/gpq.py def GPlatesQtWidgets::EditTableActionWidget --body
python scripts/gpq.py uses EditTableActionWidget --kind class
python scripts/gpq.py hier EditTableActionWidget
```
