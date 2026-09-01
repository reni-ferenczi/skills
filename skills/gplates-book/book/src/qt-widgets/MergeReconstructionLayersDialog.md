# MergeReconstructionLayersDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 319 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/MergeReconstructionLayersDialog.h` | C++ | 152 |
| `src/qt-widgets/MergeReconstructionLayersDialog.cc` | C++ | 356 |
| `src/qt-widgets/MergeReconstructionLayersDialogUi.ui` | Qt form | 145 |

## Overview

[[[PROSE overview unit=qt-widgets/MergeReconstructionLayersDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::MergeReconstructionLayersDialog`](#gplatesqtwidgetsmergereconstructionlayersdialog) | class | `QDialog`<br>`Ui_MergeReconstructionLayersDialog` | — | 0 | Dialog to select 'Reconstruction Tree' layers to merge into the current layer. |

## Members

### `GPlatesQtWidgets::MergeReconstructionLayersDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MergeReconstructionLayersDialog( GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `populate( const boost::weak_ptr<GPlatesPresentation::VisualLayer> &visual_layer)` | method | `bool` | public | Causes the dialog to be populated with all 'Reconstruction Tree' layers except the current visual\_layer. |
| `react_clear_all_layers()` | method | `void` | private | — |
| `react_select_all_layers()` | method | `void` | private | — |
| `react_cell_changed_layers( int row, int column)` | method | `void` | private | — |
| `handle_apply()` | method | `void` | private | — |
| `handle_reject()` | method | `void` | private | — |
| `LayerState` | class | `None` | private | Keeps track of which layers are enabled/disabled by the user. |
| `layer_state_seq_type` | typedef | `std::vector<LayerState>` | private | — |
| `LayerColumnName` | enum | `None` | private | These should match the table columns set up in the UI designer. |
| `setup_connections()` | method | `void` | private | — |
| `clear_layers()` | method | `void` | private | — |
| `get_selected_layers()` | method | `std::vector<GPlatesAppLogic::Layer>` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_current_visual_layer` | field | `boost::weak_ptr<GPlatesPresentation::VisualLayer>` | private | The visual layer for which we are currently merging other 'Reconstruction Tree' layers into. |
| `d_layer_state_seq` | field | `layer_state_seq_type` | private | Keeps track of which layers are enabled by the user in the GUI. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_MERGERECONSTRUCTIONLAYERSDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/MergeReconstructionLayersDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ReconstructionLayerOptionsWidget](ReconstructionLayerOptionsWidget.md) | qt-widgets | 9 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `MergeReconstructionLayersDialog` | `QDialog` | Merge Reconstruction Tree Layers | 9 |

**Qt signal/slot connections** (5 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `reconstruction_tree_layers_to_merge_table_widget` | `cellChanged(int, int)` | `this` | `react_cell_changed_layers(int, int)` |
| `button_clear_all_layers` | `clicked()` | `this` | `react_clear_all_layers()` |
| `button_select_all_layers` | `clicked()` | `this` | `react_select_all_layers()` |
| `main_buttonbox` | `accepted()` | `this` | `handle_apply()` |
| `main_buttonbox` | `rejected()` | `this` | `handle_reject()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/MergeReconstructionLayersDialog.h
python scripts/gpq.py def GPlatesQtWidgets::MergeReconstructionLayersDialog --body
python scripts/gpq.py uses MergeReconstructionLayersDialog --kind class
python scripts/gpq.py hier MergeReconstructionLayersDialog
```
