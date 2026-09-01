# CalculateStagePoleDialog

[Book TOC](../../../TOC.md) · [qt-widgets](../../../components/qt-widgets.md) · cluster Community 912 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/deprecated/CalculateStagePoleDialog.h` | C++ | 71 |
| `src/qt-widgets/deprecated/CalculateStagePoleDialog.cc` | C++ | 134 |
| `src/qt-widgets/deprecated/CalculateStagePoleDialogUi.ui` | Qt form | 246 |

## Overview

[[[PROSE overview unit=qt-widgets/deprecated/CalculateStagePoleDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::CalculateStagePoleDialog`](#gplatesqtwidgetscalculatestagepoledialog) | class | `QDialog`<br>`Ui_CalculateStagePoleDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::CalculateStagePoleDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CalculateStagePoleDialog( SmallCircleWidget *small_circle_widget, GPlatesAppLogic::ApplicationState &application_state, QWidget *parent)` | constructor | `None` | public | — |
| `handle_calculate()` | method | `void` | private | — |
| `handle_use()` | method | `void` | private | — |
| `d_small_circle_widget_ptr` | field | `SmallCircleWidget` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_centre` | field | `GPlatesMaths::LatLonPoint` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_axis_llp_from_rotation( const GPlatesMaths::FiniteRotation &rotation)` | function | `GPlatesMaths::LatLonPoint` | — |
| `GPLATES_QTWIDGETS_CALCULATESTAGEPOLEDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/deprecated/CalculateStagePoleDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `CalculateStagePoleDialog` | `QDialog` | Calculate Stage Pole | 17 |

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_calculate` | `clicked()` | `this` | `handle_calculate()` |
| `button_use` | `clicked()` | `this` | `handle_use()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/deprecated/CalculateStagePoleDialog.h
python scripts/gpq.py def GPlatesQtWidgets::CalculateStagePoleDialog --body
python scripts/gpq.py uses CalculateStagePoleDialog --kind class
python scripts/gpq.py hier CalculateStagePoleDialog
```
