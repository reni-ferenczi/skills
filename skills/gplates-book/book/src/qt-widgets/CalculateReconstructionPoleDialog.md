# CalculateReconstructionPoleDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 253 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/CalculateReconstructionPoleDialog.h` | C++ | 120 |
| `src/qt-widgets/CalculateReconstructionPoleDialog.cc` | C++ | 237 |
| `src/qt-widgets/CalculateReconstructionPoleDialogUi.ui` | Qt form | 271 |

## Overview

[[[PROSE overview unit=qt-widgets/CalculateReconstructionPoleDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::CalculateReconstructionPoleDialog`](#gplatesqtwidgetscalculatereconstructionpoledialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_CalculateReconstructionPoleDialog` | — | 0 | Dialog to calculate a reconstruction pole from a VGP. |

## Members

### `GPlatesQtWidgets::CalculateReconstructionPoleDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CalculateReconstructionPoleDialog( GPlatesPresentation::ViewState &view_state, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `handle_calculate()` | method | `void` | private | — |
| `handle_button_clicked( QAbstractButton *button)` | method | `void` | private | — |
| `handle_feature_focus_changed()` | method | `void` | private | — |
| `update_buttons()` | method | `void` | private | — |
| `fill_found_fields_from_feature_focus()` | method | `void` | private | Get pmag-related info from the feature focus (if any), and pre-fill the appropriate widgets. |
| `d_dialog_ptr` | field | `InsertVGPReconstructionPoleDialog` | private | — |
| `d_reconstruction_pole_widget_ptr` | field | `ReconstructionPoleWidget` | private | — |
| `d_reconstruction_pole` | field | `boost::optional<ReconstructionPole>` | private | — |
| `d_application_state_ptr` | field | `GPlatesAppLogic::ApplicationState` | private | We need to pass this onto the InsertVGPReconstructionDialog so that the rotation model can be updated if necessary. |
| `d_feature_focus` | field | `GPlatesGui::FeatureFocus` | private | The focussed feature - for listening to changes in focus, and pre-filling the vgp fields from the focussed feature. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_CALCULATERECONSTRUCTIONPOLEDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/CalculateReconstructionPoleDialog tier=3]]]
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
| `CalculateReconstructionPoleDialog` | `QDialog` | Calculate Reconstruction Pole | 17 |

**Qt signal/slot connections** (4 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_calculate` | `clicked()` | `this` | `handle_calculate()` |
| `main_buttonbox` | `rejected()` | `this` | `reject()` |
| `main_buttonbox` | `clicked(QAbstractButton *)` | `this` | `handle_button_clicked(QAbstractButton *)` |
| `&d_feature_focus` | `focus_changed(GPlatesGui::FeatureFocus &)` | `this` | `handle_feature_focus_changed()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/CalculateReconstructionPoleDialog.h
python scripts/gpq.py def GPlatesQtWidgets::CalculateReconstructionPoleDialog --body
python scripts/gpq.py uses CalculateReconstructionPoleDialog --kind class
python scripts/gpq.py hier CalculateReconstructionPoleDialog
```
