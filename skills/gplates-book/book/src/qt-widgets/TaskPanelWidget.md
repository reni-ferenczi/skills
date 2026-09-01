# TaskPanelWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 236 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/TaskPanelWidget.h` | C++ | 107 |

## Overview

`TaskPanelWidget` is the common interface `TaskPanel` uses to treat its nine tab widgets (`FeatureSummaryWidget`, `DigitisationWidget`, `ModifyGeometryWidget`, `TopologyToolsWidget`, and the rest) uniformly, without knowing which specific tab is active. `handle_activation()` is pure virtual: every subclass must define what "becoming the visible tab" means for it (`SmallCircleWidget`, for instance, uses it to enable itself). The remaining virtuals are optional hooks around `TaskPanel`'s single shared "Clear" action — `get_clear_action_text()` returns an empty string by default, which tells `TaskPanel` to hide the action entirely for widgets that have nothing to clear, and `clear_action_enabled()`/`handle_clear_action_triggered()` default to inert no-ops for the same reason.

`clear_action_enabled_changed` lets a subclass tell `TaskPanel` its clear-action state changed asynchronously (e.g. once some editable state becomes non-empty); subclasses raise it through the protected `emit_clear_action_enabled_changed()` rather than emitting the signal directly.

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

*None.*

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
