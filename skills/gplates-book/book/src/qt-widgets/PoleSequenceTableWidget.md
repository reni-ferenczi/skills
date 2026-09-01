# PoleSequenceTableWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1336 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/PoleSequenceTableWidget.h` | C++ | 90 |
| `src/qt-widgets/PoleSequenceTableWidget.cc` | C++ | 34 |
| `src/qt-widgets/PoleSequenceTableWidgetUi.ui` | Qt form | 61 |

## Overview

A Qt widget that displays a table of rotation poles in a sequence. Each row represents one pole with fixed plate ID, moving plate ID, begin time, and end time. The widget packages the relevant data in a `PoleSequenceInfo` struct that holds a reference to a total rotation sequence feature, the plate IDs, the time range, and a flag indicating the plate relationship within the sequence.

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

*None.*

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
