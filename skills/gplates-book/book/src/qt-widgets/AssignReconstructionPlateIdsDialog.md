# AssignReconstructionPlateIdsDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 146 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/AssignReconstructionPlateIdsDialog.h` | C++ | 407 |
| `src/qt-widgets/AssignReconstructionPlateIdsDialog.cc` | C++ | 1255 |
| `src/qt-widgets/AssignReconstructionPlateIdsDialogUi.ui` | Qt form | 764 |

## Overview

[[[PROSE overview unit=qt-widgets/AssignReconstructionPlateIdsDialog tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::AssignReconstructionPlateIdsDialog`](#gplatesqtwidgetsassignreconstructionplateidsdialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_AssignReconstructionPlateIdsDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::AssignReconstructionPlateIdsDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AssignReconstructionPlateIdsDialog( GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `exec_partition_features_dialog()` | method | `void` | public | Opens a modal dialog allowing user to choose partitioning polygon files and the files contained features to be partitioned by those polygons. |
| `reject()` | method | `void` | public | — |
| `apply()` | method | `void` | private | — |
| `clear()` | method | `void` | private | — |
| `handle_prev()` | method | `void` | private | — |
| `handle_next()` | method | `void` | private | — |
| `handle_page_change( int page)` | method | `void` | private | — |
| `react_cell_changed_partitioned_files( int row, int column)` | method | `void` | private | — |
| `react_clear_all_partitioned_files()` | method | `void` | private | — |
| `react_select_all_partitioned_files()` | method | `void` | private | — |
| `react_cell_changed_partitioning_layers( int row, int column)` | method | `void` | private | — |
| `react_clear_all_partitioning_layers()` | method | `void` | private | — |
| `react_select_all_partitioning_layers()` | method | `void` | private | — |
| `react_reconstruction_time_radio_button( bool checked)` | method | `void` | private | — |
| `react_spin_box_reconstruction_time_changed( double reconstruction_time)` | method | `void` | private | — |
| `react_respect_feature_time_period_check_box_changed()` | method | `void` | private | — |
| `react_partition_options_radio_button( bool checked)` | method | `void` | private | — |
| `react_feature_properties_options_checkbox( bool checked)` | method | `void` | private | — |
| `FileState` | class | `None` | private | Keeps track of which files are enabled/disabled by the user. |
| `file_state_seq_type` | typedef | `std::vector<FileState>` | private | — |
| `FileColumnName` | enum | `None` | private | These should match the table columns set up in the UI designer. |
| `FileStateCollection` | struct | `None` | private | — |
| `file_ptr_seq_type` | typedef | `std::vector<GPlatesFileIO::File::Reference *>` | private | Typedef for a sequence of file pointers. |
| `feature_collection_seq_type` | typedef | `std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref>` | private | Typedef for a sequence of feature collection weak refs. |
| `layer_ptr_type` | typedef | `boost::weak_ptr<GPlatesPresentation::VisualLayer>` | private | Typedef for a layer pointer. |
| `LayerState` | class | `None` | private | Keeps track of which layers are enabled/disabled by the user. |
| `layer_state_seq_type` | typedef | `std::vector<LayerState>` | private | — |
| `LayerColumnName` | enum | `None` | private | These should match the table columns set up in the UI designer. |
| `LayerStateCollection` | struct | `None` | private | — |
| `layer_ptr_seq_type` | typedef | `std::vector<layer_ptr_type>` | private | Typedef for a sequence of visual layers. |
| `ReconstructionTimeType` | enum | `None` | private | The user's choice of reconstruction time. |
| `d_help_partitioning_layer_dialog` | field | `GPlatesQtWidgets::InformationDialog` | private | — |
| `d_help_partitioned_files_dialog` | field | `GPlatesQtWidgets::InformationDialog` | private | — |
| `d_help_reconstruction_time_dialog` | field | `GPlatesQtWidgets::InformationDialog` | private | — |
| `d_help_partition_options_dialog` | field | `GPlatesQtWidgets::InformationDialog` | private | — |
| `d_help_properties_to_assign_dialog` | field | `GPlatesQtWidgets::InformationDialog` | private | — |
| `d_help_respect_feature_time_period` | field | `GPlatesQtWidgets::InformationDialog` | private | — |
| `d_button_create` | field | `QPushButton` | private | Button added to buttonbox for 'Apply' button that partitions the features. |
| `d_feature_collection_file_state` | field | `GPlatesAppLogic::FeatureCollectionFileState` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_feature_focus` | field | `GPlatesGui::FeatureFocus` | private | — |
| `d_visual_layers` | field | `GPlatesPresentation::VisualLayers` | private | The user selects a layer to be the polygon partitioning layer. |
| `d_visual_layer_registry` | field | `GPlatesPresentation::VisualLayerRegistry` | private | Used to obtain the layer type names. |
| `d_partitioning_layer_state_seq` | field | `LayerStateCollection` | private | Keeps track of which partitioning layers are enabled by the user in the GUI. |
| `d_partitioned_file_state_seq` | field | `FileStateCollection` | private | Keeps track of which partitioned files are enabled by the user in the GUI. |
| `d_reconstruction_time_type` | field | `ReconstructionTimeType` | private | Which reconstruction time the user has chosen. |
| `d_spin_box_reconstruction_time` | field | `double` | private | The reconstruction time set by the double spin box. |
| `d_respect_feature_time_period` | field | `bool` | private | Determines if features are only partitioned if the reconstruction time is within the time period over which the features are defined. |
| `d_assign_plate_id_method` | field | `GPlatesAppLogic::AssignPlateIds::AssignPlateIdMethodType` | private | How to assign plate ids to features. |
| `d_assign_reconstruction_plate_ids` | field | `bool` | private | Whether to copy reconstruction plate ids from the partitioning polygons or not. |
| `d_assign_conjugate_plate_ids` | field | `bool` | private | Whether to copy conjugate plate ids from the partitioning polygons or not. |
| `d_assign_time_of_appearance` | field | `bool` | private | Whether to copy times of appearance from the partitioning polygons or not. |
| `d_assign_time_of_disappearance` | field | `bool` | private | Whether to copy times of disappearance from the partitioning polygons or not. |
| `d_verify_information_model` | field | `bool` | private | Whether to verify information model before assigning feature properties. |
| `set_up_button_box()` | method | `void` | private | — |
| `set_up_partitioning_layers_page()` | method | `void` | private | — |
| `set_up_partitioned_files_page()` | method | `void` | private | — |
| `set_up_general_options_page()` | method | `void` | private | — |
| `pop_up_no_partitioning_layers_found_or_selected_message_box()` | method | `void` | private | — |
| `pop_up_no_partitioning_polygons_found_message_box()` | method | `void` | private | — |
| `pop_up_no_partitioned_files_selected_message_box()` | method | `void` | private | — |
| `initialise_file_list( FileStateCollection &file_state_collection, const file_ptr_seq_type &files)` | method | `void` | private | — |
| `clear_file_rows( FileStateCollection &file_state_collection)` | method | `void` | private | — |
| `add_file_row( FileStateCollection &file_state_collection, GPlatesFileIO::File::Reference &file)` | method | `void` | private | — |
| `initialise_layer_list( LayerStateCollection &layer_state_collection, const layer_ptr_seq_type &layers)` | method | `void` | private | — |
| `clear_layer_rows( LayerStateCollection &layer_state_collection)` | method | `void` | private | — |
| `add_layer_row( LayerStateCollection &layer_state_collection, const layer_ptr_type &visual_layer)` | method | `void` | private | — |
| `get_loaded_files()` | method | `file_ptr_seq_type` | private | — |
| `get_possible_partitioning_layers()` | method | `layer_ptr_seq_type` | private | — |
| `get_selected_feature_collections( FileStateCollection &file_state_collection)` | method | `feature_collection_seq_type` | private | — |
| `get_selected_layers( LayerStateCollection &layer_state_collection)` | method | `layer_ptr_seq_type` | private | — |
| `partition_features()` | method | `bool` | private | — |
| `create_plate_id_assigner()` | method | `boost::optional<GPlatesAppLogic::AssignPlateIds::non_null_ptr_type>` | private | — |
| `partition_features( GPlatesAppLogic::AssignPlateIds &plate_id_assigner)` | method | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `HELP_PARTITIONING_LAYER_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_PARTITIONING_LAYER_DIALOG_TEXT` | variable | `QString` | — |
| `HELP_PARTITIONED_FILES_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_PARTITIONED_FILES_DIALOG_TEXT` | variable | `QString` | — |
| `HELP_RECONSTRUCTION_TIME_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_RECONSTRUCTION_TIME_DIALOG_TEXT` | variable | `QString` | — |
| `HELP_PARTITION_OPTIONS_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_PARTITION_OPTIONS_DIALOG_TEXT` | variable | `QString` | — |
| `HELP_PROPERTIES_TO_ASSIGN_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_PROPERTIES_TO_ASSIGN_DIALOG_TEXT` | variable | `QString` | — |
| `HELP_RESPECT_FEATURE_TIME_PERIOD_TITLE` | variable | `QString` | — |
| `HELP_RESPECT_FEATURE_TIME_PERIOD_TEXT` | variable | `QString` | — |
| `get_num_features( const std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref> &feature_collections)` | function | `GPlatesModel::container_size_type` | Finds the total number of features in a set of feature collections. |
| `GPLATES_QT_WIDGETS_ASSIGNRECONSTRUCTIONPLATEIDSDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/AssignReconstructionPlateIdsDialog tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [api/CoReg](../api/CoReg.md) | api | 5 |
| [api/PyApplication](../api/PyApplication.md) | api | 3 |
| [data-mining/DataMiningUtils](../data-mining/DataMiningUtils.md) | data-mining | 3 |
| [gui/Dialogs](../gui/Dialogs.md) | gui | 3 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 3 |
| [api/PythonUtils](../api/PythonUtils.md) | api | 1 |
| [app-logic/ReconstructGraph](../app-logic/ReconstructGraph.md) | app-logic | 1 |
| [file-io/TemporaryFileRegistry](../file-io/TemporaryFileRegistry.md) | file-io | 1 |
| [gui/GPlatesQApplication](../gui/GPlatesQApplication.md) | gui | 1 |
| [qt-widgets/ScalarField3DDepthLayersPage](ScalarField3DDepthLayersPage.md) | qt-widgets | 1 |
| [qt-widgets/TimeDependentRasterPage](TimeDependentRasterPage.md) | qt-widgets | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `AssignReconstructionPlateIdsDialog` | `QDialog` | Assign Plate IDs | 50 |

**Qt signal/slot connections** (29 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `stack_widget` | `currentChanged(int)` | `this` | `handle_page_change(int)` |
| `buttonbox` | `accepted()` | `this` | `apply()` |
| `buttonbox` | `rejected()` | `this` | `reject()` |
| `button_prev` | `clicked()` | `this` | `handle_prev()` |
| `button_next` | `clicked()` | `this` | `handle_next()` |
| `push_button_help_partitioning_layers` | `clicked()` | `d_help_partitioning_layer_dialog` | `show()` |
| `table_partitioning_layers` | `cellChanged(int, int)` | `this` | `react_cell_changed_partitioning_layers(int, int)` |
| `button_clear_all_partitioning_layers` | `clicked()` | `this` | `react_clear_all_partitioning_layers()` |
| `button_select_all_partitioning_layers` | `clicked()` | `this` | `react_select_all_partitioning_layers()` |
| `push_button_help_partitioned_files` | `clicked()` | `d_help_partitioned_files_dialog` | `show()` |
| `table_partitioned_files` | `cellChanged(int, int)` | `this` | `react_cell_changed_partitioned_files(int, int)` |
| `button_clear_all_partitioned_files` | `clicked()` | `this` | `react_clear_all_partitioned_files()` |
| `button_select_all_partitioned_files` | `clicked()` | `this` | `react_select_all_partitioned_files()` |
| `push_button_help_reconstruction_time` | `clicked()` | `d_help_reconstruction_time_dialog` | `show()` |
| `push_button_help_partitions_options` | `clicked()` | `d_help_partition_options_dialog` | `show()` |

*... and 14 more connections.*


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/AssignReconstructionPlateIdsDialog.h
python scripts/gpq.py def GPlatesQtWidgets::AssignReconstructionPlateIdsDialog --body
python scripts/gpq.py uses AssignReconstructionPlateIdsDialog --kind class
python scripts/gpq.py hier AssignReconstructionPlateIdsDialog
```
