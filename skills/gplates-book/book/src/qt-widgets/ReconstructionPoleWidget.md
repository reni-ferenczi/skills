# ReconstructionPoleWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 253 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ReconstructionPoleWidget.h` | C++ | 109 |
| `src/qt-widgets/ReconstructionPoleWidget.cc` | C++ | 72 |
| `src/qt-widgets/ReconstructionPoleWidgetUi.ui` | Qt form | 157 |

## Overview

[[[PROSE overview unit=qt-widgets/ReconstructionPoleWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ReconstructionPole`](#gplatesqtwidgetsreconstructionpole) | struct | — | — | 0 | — |
| [`GPlatesQtWidgets::ReconstructionPoleWidget`](#gplatesqtwidgetsreconstructionpolewidget) | class | `QWidget`<br>`Ui_ReconstructionPoleWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ReconstructionPole`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `d_moving_plate` | field | `unsigned long` | public | — |
| `d_age` | field | `double` | public | — |
| `d_latitude` | field | `double` | public | — |
| `d_longitude` | field | `double` | public | — |
| `d_angle` | field | `double` | public | — |
| `d_fixed_plate` | field | `unsigned long` | public | — |
| `ReconstructionPole()` | constructor | `None` | public | — |
| `ReconstructionPole( unsigned long moving_plate, double age, double latitude, double longitude, double angle, unsigned long fixed_plate )` | constructor | `None` | public | — |

### `GPlatesQtWidgets::ReconstructionPoleWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ReconstructionPoleWidget( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `set_fields( const GPlatesModel::integer_plate_id_type &moving_plate_id, const double &time, const double &latitude, const double &longitude, const double &angle, const GPlatesModel::integer_plate_id_type &fixed_plate_id)` | method | `void` | public | — |
| `set_fields( const ReconstructionPole &reconstruction_pole)` | method | `void` | public | — |
| `d_reconstruction_pole` | field | `ReconstructionPole` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_RECONSTRUCTIONPOLEWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ReconstructionPoleWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/CalculateReconstructionPoleDialog](CalculateReconstructionPoleDialog.md) | qt-widgets | 9 |
| [qt-widgets/InsertVGPReconstructionPoleDialog](InsertVGPReconstructionPoleDialog.md) | qt-widgets | 8 |
| [qt-widgets/TaskPanel](TaskPanel.md) | qt-widgets | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ReconstructionPoleWidget` | `QWidget` | Reconstruction Pole | 13 |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ReconstructionPoleWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ReconstructionPole --body
python scripts/gpq.py uses ReconstructionPole --kind struct
python scripts/gpq.py hier ReconstructionPole
```
