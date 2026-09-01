# EditTableActionWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1109 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditTableActionWidget.h` | C++ | 79 |
| `src/qt-widgets/EditTableActionWidget.cc` | C++ | 66 |
| `src/qt-widgets/EditTableActionWidgetUi.ui` | Qt form | 113 |

## Overview

[[[PROSE overview unit=qt-widgets/EditTableActionWidget tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=qt-widgets/EditTableActionWidget tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
