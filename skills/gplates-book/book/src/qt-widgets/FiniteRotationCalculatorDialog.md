# FiniteRotationCalculatorDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 589 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/FiniteRotationCalculatorDialog.h` | C++ | 101 |
| `src/qt-widgets/FiniteRotationCalculatorDialog.cc` | C++ | 428 |
| `src/qt-widgets/FiniteRotationCalculatorDialogUi.ui` | Qt form | 1203 |

## Overview

[[[PROSE overview unit=qt-widgets/FiniteRotationCalculatorDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::FiniteRotationCalculatorDialog`](#gplatesqtwidgetsfiniterotationcalculatordialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_FiniteRotationCalculatorDialog` | — | 0 | Dialog containing various utilities related to finite rotation calculations. |

## Members

### `GPlatesQtWidgets::FiniteRotationCalculatorDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FiniteRotationCalculatorDialog( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `eventFilter( QObject *watched, QEvent *ev)` | method | `bool` | protected | An event filter to change the default dialog button when the focus changes between inputs. |
| `handle_rotate_a_point()` | method | `void` | private | — |
| `handle_add_finite_rotations()` | method | `void` | private | — |
| `handle_compute_difference_rotation()` | method | `void` | private | — |
| `handle_calc_rotation_between_points()` | method | `void` | private | — |
| `handle_add_finite_rotations_input_changed()` | method | `void` | private | — |
| `handle_compute_difference_rotation_input_changed()` | method | `void` | private | — |
| `handle_calc_rotation_between_points_input_changed()` | method | `void` | private | — |
| `handle_rotate_a_point_input_changed()` | method | `void` | private | — |
| `install_event_filters()` | method | `void` | private | — |
| `make_signal_slot_connections()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_FINITEROTATIONCALCULATORDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/FiniteRotationCalculatorDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Dialogs](../gui/Dialogs.md) | gui | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `FiniteRotationCalculatorDialog` | `QWidget` | Finite Rotation Calculator | 76 |

**Qt signal/slot connections** (26 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `main_buttonbox` | `rejected()` | `this` | `reject()` |
| `add_finite_rotations_button` | `clicked()` | `this` | `handle_add_finite_rotations()` |
| `compute_difference_rotation_button` | `clicked()` | `this` | `handle_compute_difference_rotation()` |
| `calc_rotation_between_points_button` | `clicked()` | `this` | `handle_calc_rotation_between_points()` |
| `rotate_a_point_button` | `clicked()` | `this` | `handle_rotate_a_point()` |
| `add_finite_rotations_rotation1_lat_spinbox` | `valueChanged(double)` | `this` | `handle_add_finite_rotations_input_changed()` |
| `add_finite_rotations_rotation1_lon_spinbox` | `valueChanged(double)` | `this` | `handle_add_finite_rotations_input_changed()` |
| `add_finite_rotations_rotation1_angle_spinbox` | `valueChanged(double)` | `this` | `handle_add_finite_rotations_input_changed()` |
| `add_finite_rotations_rotation2_lat_spinbox` | `valueChanged(double)` | `this` | `handle_add_finite_rotations_input_changed()` |
| `add_finite_rotations_rotation2_lon_spinbox` | `valueChanged(double)` | `this` | `handle_add_finite_rotations_input_changed()` |
| `add_finite_rotations_rotation2_angle_spinbox` | `valueChanged(double)` | `this` | `handle_add_finite_rotations_input_changed()` |
| `compute_difference_rotation_rotation1_lat_spinbox` | `valueChanged(double)` | `this` | `handle_compute_difference_rotation_input_changed()` |
| `compute_difference_rotation_rotation1_lon_spinbox` | `valueChanged(double)` | `this` | `handle_compute_difference_rotation_input_changed()` |
| `compute_difference_rotation_rotation1_angle_spinbox` | `valueChanged(double)` | `this` | `handle_compute_difference_rotation_input_changed()` |
| `compute_difference_rotation_rotation2_lat_spinbox` | `valueChanged(double)` | `this` | `handle_compute_difference_rotation_input_changed()` |

*... and 11 more connections.*


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/FiniteRotationCalculatorDialog.h
python scripts/gpq.py def GPlatesQtWidgets::FiniteRotationCalculatorDialog --body
python scripts/gpq.py uses FiniteRotationCalculatorDialog --kind class
python scripts/gpq.py hier FiniteRotationCalculatorDialog
```
