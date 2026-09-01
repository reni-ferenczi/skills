# SetTopologyReconstructionParametersDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 830 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/SetTopologyReconstructionParametersDialog.h` | C++ | 146 |
| `src/qt-widgets/SetTopologyReconstructionParametersDialog.cc` | C++ | 469 |
| `src/qt-widgets/SetTopologyReconstructionParametersDialogUi.ui` | Qt form | 761 |

## Overview

A dialog for configuring topology-based feature geometry reconstruction. Users control when reconstruction begins (feature appearance or import time), set time intervals for iterative reconstruction, and enable optional features like lifetime detection (subduction/ridge consumption), line tessellation, deformed network interpolation modes, and strain accumulation tracking. Built-in help dialogs explain each feature with detailed parameter descriptions.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::SetTopologyReconstructionParametersDialog`](#gplatesqtwidgetssettopologyreconstructionparametersdialog) | class | `QDialog`<br>`Ui_SetTopologyReconstructionParametersDialog` | — | 0 | Dialog to view and modify parameters for reconstructing feature geometries using topologies. |

## Members

### `GPlatesQtWidgets::SetTopologyReconstructionParametersDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SetTopologyReconstructionParametersDialog( GPlatesAppLogic::ApplicationState &application_state, bool only_ok_button = false, QWidget *parent_ = NULL)` | constructor | `None` | public | only\_ok\_button is useful when the parameters must be accepted by the user (ie, no cancel). |
| `populate( const boost::weak_ptr<GPlatesPresentation::VisualLayer> &visual_layer)` | method | `bool` | public | Causes the dialog to be populated with values from the given visual\_layer. |
| `handle_always_visible()` | method | `void` | private | — |
| `handle_time_window()` | method | `void` | private | — |
| `handle_delta_t()` | method | `void` | private | — |
| `handle_distant_past( bool state)` | method | `void` | private | — |
| `handle_distant_future( bool state)` | method | `void` | private | — |
| `handle_begin_time_spinbox_changed( double value)` | method | `void` | private | — |
| `handle_end_time_spinbox_changed( double value)` | method | `void` | private | — |
| `handle_time_increment_spinbox_changed( double value)` | method | `void` | private | — |
| `react_enable_detect_lifetime_changed( int state)` | method | `void` | private | — |
| `react_enable_line_tessellation_changed( int state)` | method | `void` | private | — |
| `react_show_strain_accumulation_changed( int state)` | method | `void` | private | — |
| `handle_apply()` | method | `void` | private | — |
| `setup_connections()` | method | `void` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_current_visual_layer` | field | `boost::weak_ptr<GPlatesPresentation::VisualLayer>` | private | The visual layer for which we are currently displaying settings. |
| `d_help_start_reconstruction_at_time_of_appearance_dialog` | field | `GPlatesQtWidgets::InformationDialog` | private | — |
| `d_help_detect_lifetimes_dialog` | field | `GPlatesQtWidgets::InformationDialog` | private | — |
| `d_help_tessellate_lines_dialog` | field | `GPlatesQtWidgets::InformationDialog` | private | — |
| `d_help_deformed_network_interpolation_dialog` | field | `GPlatesQtWidgets::InformationDialog` | private | — |
| `d_help_strain_accumulation_dialog` | field | `GPlatesQtWidgets::InformationDialog` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `HELP_START_RECONSTRUCTION_AT_TIME_OF_DISAPPEARANCE_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_START_RECONSTRUCTION_AT_TIME_OF_DISAPPEARANCE_DIALOG_TEXT` | variable | `QString` | — |
| `HELP_DETECT_LIFETIMES_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_DETECT_LIFETIMES_DIALOG_TEXT` | variable | `QString` | — |
| `HELP_TESSELLATE_LINES_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_TESSELLATE_LINES_DIALOG_TEXT` | variable | `QString` | — |
| `HELP_DEFORMED_NETWORK_INTERPOLATION_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_DEFORMED_NETWORK_INTERPOLATION_DIALOG_TEXT` | variable | `QString` | — |
| `HELP_STRAIN_ACCUMULATION_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_STRAIN_ACCUMULATION_DIALOG_TEXT` | variable | `QString` | — |
| `GPLATES_QTWIDGETS_SETTOPOLOGYRECONSTRUCTIONPARAMETERSDIALOG_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/GenerateDeformingMeshPointsDialog](GenerateDeformingMeshPointsDialog.md) | qt-widgets | 2 |
| [qt-widgets/ReconstructLayerOptionsWidget](ReconstructLayerOptionsWidget.md) | qt-widgets | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `SetTopologyReconstructionParametersDialog` | `QDialog` | Set Topology Reconstruction Parameters | 43 |

**Qt signal/slot connections** (14 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `main_buttonbox` | `accepted()` | `this` | `handle_apply()` |
| `main_buttonbox` | `rejected()` | `this` | `reject()` |
| `spinbox_begin_time` | `valueChanged(double)` | `this` | `handle_begin_time_spinbox_changed(double)` |
| `spinbox_end_time` | `valueChanged(double)` | `this` | `handle_end_time_spinbox_changed(double)` |
| `spinbox_time_increment` | `valueChanged(double)` | `this` | `handle_time_increment_spinbox_changed(double)` |
| `enable_detect_lifetime_check_box` | `stateChanged(int)` | `this` | `react_enable_detect_lifetime_changed(int)` |
| `enable_line_tessellation_degrees_check_box` | `stateChanged(int)` | `this` | `react_enable_line_tessellation_changed(int)` |
| `show_strain_accumulation_checkbox` | `stateChanged(int)` | `this` | `react_show_strain_accumulation_changed(int)` |
| `show_strain_accumulation_checkbox` | `stateChanged(int)` | `this` | `react_show_strain_accumulation_changed(int)` |
| `push_button_help_start_reconstruction_at_time_of_appearance` | `clicked()` | `d_help_start_reconstruction_at_time_of_appearance_dialog` | `show()` |
| `push_button_help_detect_lifetimes` | `clicked()` | `d_help_detect_lifetimes_dialog` | `show()` |
| `push_button_help_tessellate_lines` | `clicked()` | `d_help_tessellate_lines_dialog` | `show()` |
| `push_button_help_deformed_network_interpolation` | `clicked()` | `d_help_deformed_network_interpolation_dialog` | `show()` |
| `push_button_help_strain_accumulation` | `clicked()` | `d_help_strain_accumulation_dialog` | `show()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/SetTopologyReconstructionParametersDialog.h
python scripts/gpq.py def GPlatesQtWidgets::SetTopologyReconstructionParametersDialog --body
python scripts/gpq.py uses SetTopologyReconstructionParametersDialog --kind class
python scripts/gpq.py hier SetTopologyReconstructionParametersDialog
```
