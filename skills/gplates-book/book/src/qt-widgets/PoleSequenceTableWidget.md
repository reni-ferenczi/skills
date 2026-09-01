# PoleSequenceTableWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1336 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/PoleSequenceTableWidget.h` | C++ | 90 |
| `src/qt-widgets/PoleSequenceTableWidget.cc` | C++ | 34 |
| `src/qt-widgets/PoleSequenceTableWidgetUi.ui` | Qt form | 61 |

## Overview

[[[PROSE overview unit=qt-widgets/PoleSequenceTableWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::PoleSequenceTableWidget`](#gplatesqtwidgetspolesequencetablewidget) | class | `QWidget`<br>`Ui_PoleSequenceTableWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::PoleSequenceTableWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PoleSequenceInfo` | struct | `None` | public | — |
| `ColumnNames` | struct | `None` | public | — |
| `PoleSequenceTableWidget( QWidget *parent_ = NULL)` | constructor | `None` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_POLESEQUENCETABLEWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/PoleSequenceTableWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/InsertVGPReconstructionPoleDialog](InsertVGPReconstructionPoleDialog.md) | qt-widgets | 13 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `PoleSequenceTableWidget` | `QWidget` | Form | 2 |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/PoleSequenceTableWidget.h
python scripts/gpq.py def GPlatesQtWidgets::PoleSequenceTableWidget --body
python scripts/gpq.py uses PoleSequenceTableWidget --kind class
python scripts/gpq.py hier PoleSequenceTableWidget
```
