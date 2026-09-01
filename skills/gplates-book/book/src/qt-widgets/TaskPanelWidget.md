# TaskPanelWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 236 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/TaskPanelWidget.h` | C++ | 107 |

## Overview

[[[PROSE overview unit=qt-widgets/TaskPanelWidget tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::TaskPanelWidget`](#gplatesqtwidgetstaskpanelwidget) | class | `QWidget` | — | 9 | TaskPanelWidget is the abstract base class of widgets that are displayed in the TaskPanel. |

## Members

### `GPlatesQtWidgets::TaskPanelWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TaskPanelWidget( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `handle_activation()` | method | `void` | public | — |
| `get_clear_action_text()` | method | `QString` | public | The text of the TaskPanel's clear action when this widget is activated. |
| `clear_action_enabled()` | method | `bool` | public | Whether the TaskPanel's clear action, if visible, is enabled. |
| `handle_clear_action_triggered()` | method | `void` | public | Handle the TaskPanel's clear action being triggered. |
| `clear_action_enabled_changed( bool enabled)` | method | `void` | public | — |
| `emit_clear_action_enabled_changed( bool enabled)` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_TASKPANELWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/TaskPanelWidget tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/DigitisationWidget](DigitisationWidget.md) | qt-widgets | 4 |
| [qt-widgets/FeatureSummaryWidget](FeatureSummaryWidget.md) | qt-widgets | 4 |
| [qt-widgets/TopologyToolsWidget](TopologyToolsWidget.md) | qt-widgets | 4 |
| [qt-widgets/LightingWidget](LightingWidget.md) | qt-widgets | 3 |
| [qt-widgets/MeasureDistanceWidget](MeasureDistanceWidget.md) | qt-widgets | 3 |
| [qt-widgets/ModifyGeometryWidget](ModifyGeometryWidget.md) | qt-widgets | 3 |
| [qt-widgets/ModifyReconstructionPoleWidget](ModifyReconstructionPoleWidget.md) | qt-widgets | 3 |
| [qt-widgets/MovePoleWidget](MovePoleWidget.md) | qt-widgets | 3 |
| [qt-widgets/SmallCircleWidget](SmallCircleWidget.md) | qt-widgets | 3 |
| [qt-widgets/TaskPanel](TaskPanel.md) | qt-widgets | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/TaskPanelWidget.h
python scripts/gpq.py def GPlatesQtWidgets::TaskPanelWidget --body
python scripts/gpq.py uses TaskPanelWidget --kind class
python scripts/gpq.py hier TaskPanelWidget
```
