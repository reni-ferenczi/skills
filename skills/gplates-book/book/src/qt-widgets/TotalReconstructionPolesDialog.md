# TotalReconstructionPolesDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 471 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/TotalReconstructionPolesDialog.h` | C++ | 207 |
| `src/qt-widgets/TotalReconstructionPolesDialog.cc` | C++ | 729 |
| `src/qt-widgets/TotalReconstructionPolesDialogUi.ui` | Qt form | 596 |

## Overview

A dialog for examining and exporting total reconstruction poles at the current reconstruction time. It displays rotation data in two tabular views: relative rotations (each plate relative to the stationary plate) and equivalent rotations (absolute positions). It also shows the reconstruction tree as a hierarchy and the plate circuit as a tree from any plate to the stationary plate. The dialog can export both rotation tables as CSV in multiple formats. It monitors changes to the reconstruction time and the selected visual layer, updating its display automatically when either changes. Stationary plate and time are set by the caller via dedicated methods.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`ColumnNames::ColumnName`](#columnnamescolumnname) | enum | — | — | 0 | These should match the columns set up in the designer. |
| [`(anonymous)::FileDialogFilterOption`](#anonymousfiledialogfilteroption) | struct | — | — | 0 | Struct to build the following table of file dialog filters / options. |
| [`(anonymous)::FileDialogFilterMapType`](#anonymousfiledialogfiltermaptype) | typedef | — | — | 0 | — |
| [`GPlatesQtWidgets::TotalReconstructionPolesDialog`](#gplatesqtwidgetstotalreconstructionpolesdialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_TotalReconstructionPolesDialog` | — | 0 | — |

## Members

### `ColumnNames::ColumnName`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PLATEID` | enumerator | `None` | — | — |
| `LATITUDE` | enumerator | `None` | — | — |
| `LONGITUDE` | enumerator | `None` | — | — |
| `ANGLE` | enumerator | `None` | — | — |
| `FIXED` | enumerator | `None` | — | — |

### `(anonymous)::FileDialogFilterOption`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `text` | field | `char` | public | — |
| `options` | field | `GPlatesGui::CsvExport::ExportOptions` | public | — |

### `(anonymous)::FileDialogFilterMapType`

*None.*

### `GPlatesQtWidgets::TotalReconstructionPolesDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TotalReconstructionPolesDialog( GPlatesPresentation::ViewState &view_state, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `update()` | method | `void` | public | Updates the dialog. |
| `update( boost::weak_ptr<GPlatesPresentation::VisualLayer> visual_layer)` | method | `void` | public | Updates the dialog to show a particular visual\_layer. |
| `showEvent( QShowEvent *event_)` | method | `void` | protected | — |
| `export_relative()` | method | `void` | private | Export the relative-rotation data in csv form. |
| `export_equivalent()` | method | `void` | private | Export the equivalent-rotation data in csv form. |
| `update_if_visible()` | method | `void` | private | — |
| `update_if_layer_changed()` | method | `void` | private | — |
| `handle_export( const QTableWidget &table)` | method | `void` | private | Called from export\_relative and export\_equivalent to handle getting the filename from the user and different export options. |
| `set_time( const double time)` | method | `void` | private | Set the dialog reconstruction time. |
| `set_plate( unsigned long plate)` | method | `void` | private | Set the dialog stationary plate id. |
| `fill_equivalent_table( const GPlatesAppLogic::ReconstructionTree &reconstruction_tree)` | method | `void` | private | Fill the equivalent-rotation QTableWidget. |
| `fill_relative_table( const GPlatesAppLogic::ReconstructionTree &reconstruction_tree)` | method | `void` | private | Fill the relative-rotation QTableWidget. |
| `fill_reconstruction_tree( const GPlatesAppLogic::ReconstructionTree &reconstruction_tree)` | method | `void` | private | Fill the reconstruction tree QTreeWidget. |
| `fill_circuit_tree( const GPlatesAppLogic::ReconstructionTree &reconstruction_tree)` | method | `void` | private | Fill the circuit-to-stationary-plate QTreeWidget. |
| `make_signal_slot_connections()` | method | `void` | private | — |
| `reset_everything()` | method | `void` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | To query the reconstruction. |
| `d_plate` | field | `unsigned long` | private | The stationary plate id. |
| `d_time` | field | `double` | private | The reconstruction time. |
| `d_save_file_dialog` | field | `SaveFileDialog` | private | Used by handle\_export to obtain a file name from the user. |
| `d_visual_layers_combobox` | field | `VisualLayersComboBox` | private | — |
| `d_curr_visual_layer` | field | `boost::weak_ptr<GPlatesPresentation::VisualLayer>` | private | — |
| `d_need_to_update_when_visible` | field | `bool` | private | When we ignore an update because we are not visible, then we need to do the update the next time we become visible. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `NUM_ELEMS` | macro_function | `(sizeof(a) / sizeof((a)[0]))` | — |
| `file_dialog_filter_table` | variable | `FileDialogFilterOption` | Table of filter options to present to the user when exporting CSV. |
| `build_save_file_dialog_filters()` | function | `GPlatesQtWidgets::SaveFileDialog::filter_list_type` | Construct filters to give to SaveFileDialog. |
| `make_string_from_rotation( const GPlatesMaths::FiniteRotation &rotation)` | function | `QString` | — |
| `fill_tree_item( QTreeWidgetItem* item, const GPlatesAppLogic::ReconstructionTree::Edge &edge)` | function | `void` | — |
| `add_children_of_edge_to_tree_item( const GPlatesAppLogic::ReconstructionTree::Edge &edge, QTreeWidgetItem *item)` | function | `void` | — |
| `populate_rotation_table_row( QTableWidget *table, int row_num, GPlatesModel::integer_plate_id_type plate_id, const GPlatesMaths::FiniteRotation &fr)` | function | `void` | — |
| `GPLATES_QTWIDGETS_TOTALRECONSTRUCTIONPOLESDIALOG_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/VelocityFieldCalculatorLayerOptionsWidget](VelocityFieldCalculatorLayerOptionsWidget.md) | qt-widgets | 2 |
| [gui/Dialogs](../gui/Dialogs.md) | gui | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `TotalReconstructionPolesDialog` | `QWidget` | Total Reconstruction Poles | 30 |

**Qt signal/slot connections** (4 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_export_relative_rotations` | `clicked()` | `this` | `export_relative()` |
| `button_export_equiv_rotations` | `clicked()` | `this` | `export_equivalent()` |
| `d_visual_layers_combobox` | `selected_visual_layer_changed( boost::weak_ptr<GPlatesPresentation::VisualLayer>)` | `this` | `update_if_layer_changed()` |
| `&d_application_state` | `reconstructed(GPlatesAppLogic::ApplicationState &)` | `this` | `update_if_visible()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/TotalReconstructionPolesDialog.h
python scripts/gpq.py def GPlatesQtWidgets::TotalReconstructionPolesDialog --body
python scripts/gpq.py uses TotalReconstructionPolesDialog --kind class
python scripts/gpq.py hier TotalReconstructionPolesDialog
```
