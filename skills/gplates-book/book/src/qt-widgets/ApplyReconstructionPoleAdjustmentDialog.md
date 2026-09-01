# ApplyReconstructionPoleAdjustmentDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 375 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ApplyReconstructionPoleAdjustmentDialog.h` | C++ | 241 |
| `src/qt-widgets/ApplyReconstructionPoleAdjustmentDialog.cc` | C++ | 414 |
| `src/qt-widgets/ApplyReconstructionPoleAdjustmentDialogUi.ui` | Qt form | 666 |

## Overview

[[[PROSE overview unit=qt-widgets/ApplyReconstructionPoleAdjustmentDialog tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ApplyReconstructionPoleAdjustmentDialog`](#gplatesqtwidgetsapplyreconstructionpoleadjustmentdialog) | class | `QDialog`<br>`Ui_ApplyReconstructionPoleAdjustmentDialog` | — | 0 | — |
| [`GPlatesQtWidgets::AdjustmentApplicator`](#gplatesqtwidgetsadjustmentapplicator) | class | `QObject` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ApplyReconstructionPoleAdjustmentDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PoleSequenceInfo` | struct | `None` | public | — |
| `ColumnNames` | struct | `None` | public | — |
| `fill_in_fields_for_rotation( QLineEdit *lat_field_ptr, QLineEdit *lon_field_ptr, QDoubleSpinBox *angle_ptr, const GPlatesMaths::Rotation &r)` | method | `void` | public | — |
| `ApplyReconstructionPoleAdjustmentDialog( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~ApplyReconstructionPoleAdjustmentDialog()` | destructor | `None` | public | — |
| `setup_for_new_pole( unsigned long moving_plate_, const double &current_time_, const std::vector<PoleSequenceInfo> &sequence_choices_, const GPlatesMaths::Rotation &adjustment_)` | method | `void` | public | — |
| `set_original_pole( const GPlatesMaths::FiniteRotation &fr)` | method | `void` | public | — |
| `set_result_pole( const GPlatesMaths::FiniteRotation &fr)` | method | `void` | public | — |
| `set_adjustment( const GPlatesMaths::Rotation &adjustment_)` | method | `void` | public | — |
| `change_value( int new_value)` | method | `void` | public | — |
| `propagate_value()` | method | `void` | public | — |
| `handle_pole_sequence_selection_changed()` | method | `void` | protected | — |
| `handle_pole_time_changed( double new_pole_time)` | method | `void` | protected | — |
| `pole_sequence_choice_changed( int new_choice)` | method | `void` | public | — |
| `pole_sequence_choice_cleared()` | method | `void` | public | — |
| `pole_time_changed( double new_pole_time)` | method | `void` | public | — |
| `populate_pole_sequence_table( const std::vector<PoleSequenceInfo> &sequence_choices_)` | method | `void` | private | — |

### `GPlatesQtWidgets::AdjustmentApplicator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AdjustmentApplicator( GPlatesPresentation::ViewState &view_state, ApplyReconstructionPoleAdjustmentDialog &dialog)` | constructor | `None` | public | — |
| `set( const std::vector<ApplyReconstructionPoleAdjustmentDialog::PoleSequenceInfo> & sequence_choices_, const GPlatesMaths::Rotation &adjustment_, const GPlatesAppLogic::ReconstructionTree::non_null_ptr_to_const_type &reconstruction_tree_)` | method | `void` | public | — |
| `handle_pole_sequence_choice_changed( int index)` | method | `void` | public | — |
| `handle_pole_sequence_choice_cleared()` | method | `void` | public | — |
| `handle_pole_time_changed( double new_pole_time)` | method | `void` | public | — |
| `apply_adjustment()` | method | `void` | public | — |
| `have_reconstructed()` | method | `void` | public | — |
| `d_application_state_ptr` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_dialog_ptr` | field | `ApplyReconstructionPoleAdjustmentDialog` | private | — |
| `d_adjustment` | field | `boost::optional<GPlatesMaths::Rotation>` | private | The adjustment as calculated interactively, relative to the stationary plate. |
| `d_adjustment_rel_fixed` | field | `boost::optional<GPlatesMaths::Rotation>` | private | The adjustment, compensating for the motion of the fixed plate (if any). |
| `d_reconstruction_tree` | field | `boost::optional<GPlatesAppLogic::ReconstructionTree::non_null_ptr_to_const_type>` | private | The tree that reconstructed the features. |
| `d_pole_time` | field | `double` | private | — |
| `d_sequence_choices` | field | `std::vector<ApplyReconstructionPoleAdjustmentDialog::PoleSequenceInfo>` | private | — |
| `d_sequence_choice_index` | field | `boost::optional<int>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `fill_in_fields_for_finite_rotation( QLineEdit *lat_field_ptr, QLineEdit *lon_field_ptr, QDoubleSpinBox *angle_ptr, const GPlatesMaths::FiniteRotation &fr)` | function | `void` | — |
| `GPLATES_QTWIDGETS_APPLYRECONSTRUCTIONPOLEADJUSTMENTDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ApplyReconstructionPoleAdjustmentDialog tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ModifyReconstructionPoleWidget](ModifyReconstructionPoleWidget.md) | qt-widgets | 31 |
| [qt-widgets/deprecated/CreateTopologyWidget](deprecated/CreateTopologyWidget.md) | qt-widgets | 6 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ApplyReconstructionPoleAdjustmentDialog` | `QDialog` | Apply Reconstruction Pole Adjustment | 38 |

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `table_pole_sequences` | `itemSelectionChanged()` | `this` | `handle_pole_sequence_selection_changed()` |
| `spinbox_pole_time` | `valueChanged(double)` | `this` | `handle_pole_time_changed(double)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ApplyReconstructionPoleAdjustmentDialog.h
python scripts/gpq.py def GPlatesQtWidgets::ApplyReconstructionPoleAdjustmentDialog --body
python scripts/gpq.py uses ApplyReconstructionPoleAdjustmentDialog --kind class
python scripts/gpq.py hier ApplyReconstructionPoleAdjustmentDialog
```
