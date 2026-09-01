# InsertionPointWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1797 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/InsertionPointWidget.h` | C++ | 61 |
| `src/qt-widgets/InsertionPointWidgetUi.ui` | Qt form | 76 |

## Overview

[[[PROSE overview unit=qt-widgets/InsertionPointWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::InsertionPointWidget`](#gplatesqtwidgetsinsertionpointwidget) | class | `QWidget`<br>`Ui_InsertionPointWidget` | — | 0 | Lightweight Qt widget to display the 'Insertion Point' arrow plus cancel button. |

## Members

### `GPlatesQtWidgets::InsertionPointWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InsertionPointWidget( QAction &action, QWidget *parent_ = NULL)` | constructor | `None` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_INSERTIONPOINTWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/InsertionPointWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/TopologySectionsTable](../gui/TopologySectionsTable.md) | gui | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `InsertionPointWidget` | `QWidget` | Insertion Point | 3 |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/InsertionPointWidget.h
python scripts/gpq.py def GPlatesQtWidgets::InsertionPointWidget --body
python scripts/gpq.py uses InsertionPointWidget --kind class
python scripts/gpq.py hier InsertionPointWidget
```
