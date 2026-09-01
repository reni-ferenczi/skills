# HellingerDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 10 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/HellingerDialog.h` | C++ | 688 |
| `src/qt-widgets/HellingerDialog.cc` | C++ | 2004 |
| `src/qt-widgets/HellingerDialogUi.ui` | Qt form | 580 |

## Overview

[[[PROSE overview unit=qt-widgets/HellingerDialog tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::TabPages`](#anonymoustabpages) | enum | — | — | 0 | — |
| [`GPlatesQtWidgets::CanvasOperationType`](#gplatesqtwidgetscanvasoperationtype) | enum | — | — | 0 | — |
| [`GPlatesQtWidgets::HellingerDialog`](#gplatesqtwidgetshellingerdialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_HellingerDialog` | — | 0 | — |

## Members

### `(anonymous)::TabPages`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PICKS_TAB_PAGE` | enumerator | `None` | — | — |
| `FIT_TAB_PAGE` | enumerator | `None` | — | — |
| `NUM_TAB_PAGES` | enumerator | `None` | — | — |

### `GPlatesQtWidgets::CanvasOperationType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SELECT_OPERATION` | enumerator | `None` | — | — |
| `EDIT_POINT_OPERATION` | enumerator | `None` | — | — |
| `NEW_POINT_OPERATION` | enumerator | `None` | — | — |
| `EDIT_SEGMENT_OPERATION` | enumerator | `None` | — | — |
| `NEW_SEGMENT_OPERATION` | enumerator | `None` | — | — |

### `GPlatesQtWidgets::HellingerDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Configuration` | struct | `None` | public | — |
| `expanded_status_map_type` | typedef | `std::map<int,bool>` | public | — |
| `geometry_to_model_map_type` | typedef | `std::vector<hellinger_model_type::const_iterator >` | public | — |
| `HellingerDialog( GPlatesPresentation::ViewState &view_state, GPlatesQtWidgets::ReadErrorAccumulationDialog &read_error_dialog, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `restore()` | method | `void` | public | Set the pick layer active, and draw the model contents on the canvas |
| `update_widgets_from_model()` | method | `void` | public | Update whole dialog from model, and then update the canvas |
| `get_pick_layer()` | method | `GPlatesViewOperations::RenderedGeometryCollection::child_layer_owner_ptr_type` | public | — |
| `get_editing_layer()` | method | `GPlatesViewOperations::RenderedGeometryCollection::child_layer_owner_ptr_type` | public | — |
| `get_feature_highlight_layer()` | method | `GPlatesViewOperations::RenderedGeometryCollection::child_layer_owner_ptr_type` | public | — |
| `get_pole_estimate_layer()` | method | `GPlatesViewOperations::RenderedGeometryCollection::child_layer_owner_ptr_type` | public | — |
| `set_hovered_pick( const unsigned int index)` | method | `void` | public | — |
| `set_selected_pick( const unsigned int index)` | method | `void` | public | — |
| `clear_hovered_layer_and_table()` | method | `void` | public | — |
| `clear_selection_layer()` | method | `void` | public | — |
| `clear_editing_layer()` | method | `void` | public | — |
| `clear_feature_highlight_layer()` | method | `void` | public | — |
| `edit_current_pick()` | method | `void` | public | — |
| `update_edit_layer( const GPlatesMaths::PointOnSphere &pos)` | method | `void` | public | — |
| `set_enlarged_edit_geometry( bool enlarged = true)` | method | `void` | public | — |
| `is_in_edit_point_state()` | method | `bool` | public | — |
| `is_in_new_point_state()` | method | `bool` | public | — |
| `is_in_edit_segment_state()` | method | `bool` | public | — |
| `is_in_new_segment_state()` | method | `bool` | public | — |
| `set_feature_highlight( const GPlatesMaths::PointOnSphere &pos)` | method | `void` | public | — |
| `update_after_new_or_edited_pick( const hellinger_model_type::const_iterator &it, const int segment_number)` | method | `void` | public | — |
| `update_after_new_or_edited_segment( const int segment_number)` | method | `void` | public | — |
| `enable_pole_estimate_widgets( bool enable)` | method | `void` | public | — |
| `set_layer_state_for_active_pole_tool( bool pole_tool_is_active)` | method | `void` | public | — |
| `get_pole_estimate_12_lat_lon` | field | `GPlatesMaths::LatLonPoint` | public | — |
| `get_pole_estimate_12_angle` | field | `double` | public | — |
| `get_pole_estimate_13_lat_lon` | field | `GPlatesMaths::LatLonPoint` | public | — |
| `get_pole_estimate_13_angle` | field | `double` | public | — |
| `update_pole_estimates( const GPlatesMaths::PointOnSphere &point_12, double &angle_12, const GPlatesMaths::PointOnSphere &point_13, double &angle_13)` | method | `void` | public | — |
| `adjust_pole_tool_is_active()` | method | `bool` | public | — |
| `set_adjust_pole_tool_is_active( bool active)` | method | `void` | public | — |
| `set_state_for_pole_adjustment_tool( bool pole_adjustment_tool_is_active)` | method | `void` | public | — |
| `output_file_path()` | method | `QString` | public | — |
| `output_file_path_is_valid()` | method | `bool` | public | — |
| `get_fit_type` | field | `HellingerFitType` | public | — |
| `close()` | method | `void` | public | — |
| `hide()` | method | `void` | public | hide - override the QDialog method so that we can hide child dialogs too. |
| `keyPressEvent(QKeyEvent *event)` | method | `void` | public | — |
| `begin_edit_pick()` | method | `void` | public | — |
| `begin_new_pick()` | method | `void` | public | — |
| `finished_editing()` | method | `void` | public | — |
| `pole_estimate_12_lat_lon_changed( double, double)` | method | `void` | public | — |
| `pole_estimate_12_angle_changed( double)` | method | `void` | public | — |
| `pole_estimate_13_lat_lon_changed( double, double)` | method | `void` | public | — |
| `pole_estimate_13_angle_changed( double)` | method | `void` | public | — |
| `check_and_highlight_output_path()` | method | `void` | private | — |
| `set_up_connections()` | method | `void` | private | — |
| `set_up_child_layers()` | method | `void` | private | — |
| `activate_layers( bool activate = true)` | method | `void` | private | — |
| `clear_rendered_geometries()` | method | `void` | private | — |
| `clear_pick_geometries()` | method | `void` | private | — |
| `highlight_selected_pick( const HellingerPick& pick)` | method | `void` | private | — |
| `highlight_selected_segment( const int &segment_number)` | method | `void` | private | — |
| `draw_pole_result( const double &lat, const double &lon, const HellingerConfigurationWidget::HellingerColour &colour)` | method | `void` | private | — |
| `update_results_on_canvas()` | method | `void` | private | — |
| `update_estimates_on_canvas()` | method | `void` | private | — |
| `draw_error_ellipse( const GPlatesQtWidgets::HellingerPlatePairType &type = GPlatesQtWidgets::PLATES_1_2_PAIR_TYPE)` | method | `void` | private | — |
| `create_feature_collection()` | method | `void` | private | Import the currently loaded hellinger pick data into the main gplates model. |
| `draw_picks_of_plate_index( const HellingerPlateIndex &fixed_plate_index)` | method | `void` | private | — |
| `draw_picks()` | method | `void` | private | — |
| `draw_pole_estimate( const HellingerPoleEstimate &estimate, const HellingerConfigurationWidget::HellingerColour &colour)` | method | `void` | private | — |
| `hide_child_dialogs()` | method | `void` | private | — |
| `update_chron_time()` | method | `void` | private | update\_chron\_time - check the chron string against the active age model, and convert it to an age if appropriate. |
| `update_model_from_file_related_data()` | method | `void` | private | — |
| `enable_pole_estimate_signals( bool enable)` | method | `void` | private | — |
| `handle_show_estimate_checkboxes_clicked()` | method | `void` | private | — |
| `handle_show_result_checkboxes_clicked()` | method | `void` | private | — |
| `handle_thread_finished()` | method | `void` | private | — |
| `handle_calculate_fit()` | method | `void` | private | — |
| `handle_import_hellinger_file()` | method | `void` | private | — |
| `handle_show_details()` | method | `void` | private | — |
| `handle_add_new_pick()` | method | `void` | private | — |
| `handle_export_pick_file()` | method | `void` | private | — |
| `handle_export_com_file()` | method | `void` | private | — |
| `handle_edit_pick()` | method | `void` | private | — |
| `handle_add_new_segment()` | method | `void` | private | — |
| `handle_edit_segment()` | method | `void` | private | — |
| `handle_calculate_uncertainties()` | method | `void` | private | — |
| `handle_close()` | method | `void` | private | — |
| `handle_pole_estimate_12_changed(double, double)` | method | `void` | private | — |
| `handle_pole_estimate_12_angle_changed(double)` | method | `void` | private | — |
| `handle_pole_estimate_13_changed(double, double)` | method | `void` | private | — |
| `handle_pole_estimate_13_angle_changed(double)` | method | `void` | private | — |
| `handle_chron_time_changed( const double &time)` | method | `void` | private | — |
| `handle_recon_time_spinbox_changed( const double &time)` | method | `void` | private | — |
| `handle_recon_time_slider_changed( const int &value)` | method | `void` | private | — |
| `handle_pick_dialog_updated()` | method | `void` | private | — |
| `handle_cancel()` | method | `void` | private | — |
| `handle_finished_editing()` | method | `void` | private | — |
| `handle_update_point_editing()` | method | `void` | private | — |
| `handle_update_segment_editing()` | method | `void` | private | — |
| `handle_active_age_model_changed()` | method | `void` | private | — |
| `handle_settings_clicked()` | method | `void` | private | — |
| `handle_configuration_changed()` | method | `void` | private | — |
| `handle_tab_changed(int)` | method | `void` | private | — |
| `handle_output_path_button_clicked()` | method | `void` | private | — |
| `handle_output_path_changed()` | method | `void` | private | — |
| `handle_output_path_editing_finished()` | method | `void` | private | — |
| `child_layer_ptr_type` | typedef | `GPlatesViewOperations::RenderedGeometryCollection::child_layer_owner_ptr_type` | private | Convenience typedef for GPlatesViewOperations::RenderedGeometryCollection::child\_layer\_owner\_ptr\_type |
| `initialise_widgets()` | method | `void` | private | initialise\_widgets - set-up initial state of widgets. |
| `update_canvas()` | method | `void` | private | Draw the model contents on the globe/map. |
| `update_selected_geometries()` | method | `void` | private | — |
| `reconstruct_picks()` | method | `void` | private | Reconstruct the moving picks |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_rendered_geom_collection_ptr` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | For creating child layers |
| `d_pick_layer_ptr` | field | `child_layer_ptr_type` | private | For drawing picks |
| `d_hover_layer_ptr` | field | `child_layer_ptr_type` | private | For highlighting picks which are hovered over. |
| `d_selection_layer_ptr` | field | `child_layer_ptr_type` | private | For selected pick / segment |
| `d_result_layer_ptr` | field | `child_layer_ptr_type` | private | For fitted pole, uncertainty |
| `d_editing_layer_ptr` | field | `child_layer_ptr_type` | private | For geometries being edited |
| `d_feature_highlight_layer_ptr` | field | `child_layer_ptr_type` | private | For highlighting feature geometries which can be selected |
| `d_pole_estimate_layer_ptr` | field | `child_layer_ptr_type` | private | For displaying the pole estimate |
| `d_read_error_accumulation_dialog` | field | `ReadErrorAccumulationDialog` | private | — |
| `d_hellinger_model` | field | `HellingerModel` | private | — |
| `d_hellinger_stats_dialog` | field | `HellingerStatsDialog` | private | — |
| `d_hellinger_edit_point_dialog` | field | `HellingerPointDialog` | private | — |
| `d_hellinger_new_point_dialog` | field | `HellingerPointDialog` | private | — |
| `d_hellinger_edit_segment_dialog` | field | `HellingerSegmentDialog` | private | — |
| `d_hellinger_new_segment_dialog` | field | `HellingerSegmentDialog` | private | — |
| `d_hellinger_thread` | field | `HellingerThread` | private | — |
| `d_plate_1_id` | field | `GPlatesModel::integer_plate_id_type` | private | For storing moving and fixed plate IDs for later insertion of rotation pole into model. |
| `d_plate_2_id` | field | `GPlatesModel::integer_plate_id_type` | private | — |
| `d_plate_3_id` | field | `GPlatesModel::integer_plate_id_type` | private | — |
| `d_recon_time` | field | `double` | private | — |
| `d_chron_time` | field | `double` | private | — |
| `d_moving_symbol` | field | `GPlatesGui::Symbol` | private | symbols for depicting moving and fixed picks. |
| `d_fixed_symbol` | field | `GPlatesGui::Symbol` | private | — |
| `d_thread_type` | field | `ThreadType` | private | d\_thread\_type - enum describing the thread type - i.e .pole calculation thread or stats calculation thread. |
| `d_python_path` | field | `QString` | private | d\_python\_path - At present we need to pass the hellinger python file to boost::python::exec\_file. |
| `d_python_file` | field | `QString` | private | d\_python\_file - the full filename (including path) of the hellinger python file. |
| `d_path_for_temporary_files` | field | `QString` | private | d\_path\_for\_temporary\_files - location for storing temporary files used for passing data between the python scripts and GPlates. |
| `d_output_file_path` | field | `QString` | private | — |
| `d_geometry_to_model_map` | field | `geometry_to_model_map_type` | private | — |
| `d_edit_point_is_enlarged` | field | `bool` | private | — |
| `d_canvas_operation_type` | field | `CanvasOperationType` | private | — |
| `d_pole_estimate_12_llp` | field | `GPlatesMaths::LatLonPoint` | private | — |
| `d_pole_estimate_13_llp` | field | `GPlatesMaths::LatLonPoint` | private | — |
| `d_pole_estimate_12_angle` | field | `double` | private | — |
| `d_pole_estimate_13_angle` | field | `double` | private | — |
| `d_spin_box_palette` | field | `QPalette` | private | d\_spin\_box\_palette - the palette used in begin/end spinboxes. |
| `d_configuration_dialog` | field | `HellingerConfigurationDialog` | private | d\_settings\_dialog - Dialog for changing configuration |
| `d_configuration` | field | `Configuration` | private | d\_configuration - instance of structure holding settings for rendering of certain hellinger-related geometries |
| `d_pick_widget` | field | `HellingerPickWidget` | private | — |
| `d_fit_widget` | field | `HellingerFitWidget` | private | — |
| `d_adjust_pole_tool_is_active` | field | `bool` | private | — |
| `d_open_directory_dialog` | field | `OpenDirectoryDialog` | private | — |
| `d_output_path_is_valid` | field | `bool` | private | — |
| `d_three_way_fitting_is_enabled` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `SLIDER_MULTIPLIER` | variable | `double` | — |
| `DEFAULT_SYMBOL_SIZE` | variable | `int` | — |
| `ENLARGED_SYMBOL_SIZE` | variable | `int` | — |
| `POLE_ESTIMATE_SYMBOL_SIZE` | variable | `int` | — |
| `MAIN_PYTHON_FILENAME` | variable | `QString` | — |
| `DEFAULT_POINT_SIZE` | variable | `double` | — |
| `DEFAULT_LINE_THICKNESS` | variable | `double` | — |
| `ENLARGED_POINT_SIZE` | variable | `double` | — |
| `DEFAULT_OUTPUT_FILE_ROOT` | variable | `QString` | — |
| `set_chron_time( double &chron_time, const QString &chron_string, const GPlatesAppLogic::ApplicationState::chron_to_time_interval_map_type &map)` | function | `void` | set\_chron\_time where \<y\|o\> can be "y" or "o", indicating which of the younger or older ends of the time interval is to be used. |
| `check_output_file_root( QLineEdit *line_edit)` | function | `void` | — |
| `create_results_filename( const QString &path, const QString &root)` | function | `QString` | — |
| `try_to_find_chron_time( const QString &chron_string, const GPlatesAppLogic::AgeModelCollection &age_model_collection)` | function | `boost::optional<double>` | try\_to\_find\_chron\_time if we find a matching chron\_string in the active AgeModel, we return an optional form of the time (Ma) of that chron. |
| `edit_operation_active(const GPlatesQtWidgets::CanvasOperationType &type)` | function | `bool` | — |
| `get_moving_plate_indices( const GPlatesQtWidgets::HellingerPlateIndex &fixed_index)` | function | `std::pair<GPlatesQtWidgets::HellingerPlateIndex,GPlatesQtWidgets::HellingerPlateIndex>` | — |
| `correct_directions_of_rotations( boost::optional<GPlatesQtWidgets::HellingerFitStructure> &fit_a, boost::optional<GPlatesQtWidgets::HellingerFitStructure> &fit_b, const GPlatesQtWidgets::HellingerPlateIndex &fixed_plate_index)` | function | `void` | — |
| `get_rotation( const boost::optional<GPlatesQtWidgets::HellingerFitStructure> &fit, double fraction)` | function | `boost::optional<GPlatesMaths::FiniteRotation>` | — |
| `add_pick_geometry_to_layer( const GPlatesQtWidgets::HellingerPick &pick, GPlatesViewOperations::RenderedGeometryCollection::child_layer_owner_ptr_type &layer, const GPlatesGui::Colour &colour, bool use_enlarged_symbol_size = false)` | function | `void` | — |
| `add_segment_geometries_to_layer( const GPlatesQtWidgets::hellinger_model_const_range_type &segment, GPlatesViewOperations::RenderedGeometryCollection::child_layer_owner_ptr_type &layer, const GPlatesGui::Colour &colour)` | function | `void` | — |
| `GPLATES_QTWIDGETS_HELLINGERDIALOG_H` | macro | `None` | — |
| `INITIAL_BEST_FIT_POLE_COLOUR` | variable | `HellingerConfigurationWidget::HellingerColour` | — |
| `INITIAL_POLE_SIZE` | variable | `float` | — |
| `INITIAL_ELLIPSE_COLOUR` | variable | `HellingerConfigurationWidget::HellingerColour` | — |
| `INITIAL_ELLIPSE_THICKNESS` | variable | `int` | — |
| `INITIAL_POLE_ARROW_HEIGHT` | variable | `float` | — |
| `INITIAL_POLE_ARROW_RADIUS` | variable | `float` | — |
| `INITIAL_PLATE_ONE_PICK_SYMBOL` | variable | `GPlatesGui::Symbol::SymbolType` | — |
| `INITIAL_PLATE_TWO_PICK_SYMBOL` | variable | `GPlatesGui::Symbol::SymbolType` | — |
| `INITIAL_PLATE_THREE_PICK_SYMBOL` | variable | `GPlatesGui::Symbol::SymbolType` | — |
| `INITIAL_PLATE_ONE_PICK_SYMBOL_SIZE` | variable | `int` | — |
| `INITIAL_PLATE_TWO_PICK_SYMBOL_SIZE` | variable | `int` | — |
| `INITIAL_PLATE_THREE_PICK_SYMBOL_SIZE` | variable | `int` | — |
| `POLE_12_COLOUR` | variable | `HellingerConfigurationWidget::HellingerColour` | Initial colours - control this from the settings dialog eventually. |
| `POLE_13_COLOUR` | variable | `HellingerConfigurationWidget::HellingerColour` | — |
| `POLE_23_COLOUR` | variable | `HellingerConfigurationWidget::HellingerColour` | — |
| `POLE_ESTIMATE_12_COLOUR` | variable | `HellingerConfigurationWidget::HellingerColour` | — |
| `POLE_ESTIMATE_13_COLOUR` | variable | `HellingerConfigurationWidget::HellingerColour` | — |

## Notes

[[[PROSE notes unit=qt-widgets/HellingerDialog tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [canvas-tools/AdjustFittedPoleEstimate](../canvas-tools/AdjustFittedPoleEstimate.md) | canvas-tools | 65 |
| [canvas-tools/SelectHellingerGeometries](../canvas-tools/SelectHellingerGeometries.md) | canvas-tools | 56 |
| [qt-widgets/HellingerConfigurationDialog](HellingerConfigurationDialog.md) | qt-widgets | 31 |
| [qt-widgets/HellingerThread](HellingerThread.md) | qt-widgets | 25 |
| [qt-widgets/HellingerPickWidget](HellingerPickWidget.md) | qt-widgets | 22 |
| [qt-widgets/HellingerFitWidget](HellingerFitWidget.md) | qt-widgets | 17 |
| [qt-widgets/HellingerSegmentDialog](HellingerSegmentDialog.md) | qt-widgets | 11 |
| [qt-widgets/HellingerPointDialog](HellingerPointDialog.md) | qt-widgets | 5 |
| [gui/HellingerCanvasToolWorkflow](../gui/HellingerCanvasToolWorkflow.md) | gui | 3 |
| [gui/Dialogs](../gui/Dialogs.md) | gui | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `HellingerDialog` | `QDialog` | Hellinger Fitting Tool | 35 |

**Qt signal/slot connections** (36 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_fit_widget` | `pole_estimate_12_changed(double, double)` | `this` | `handle_pole_estimate_12_changed(double, double)` |
| `d_fit_widget` | `pole_estimate_13_changed(double, double)` | `this` | `handle_pole_estimate_13_changed(double, double)` |
| `d_fit_widget` | `pole_estimate_12_angle_changed(double)` | `this` | `handle_pole_estimate_12_angle_changed(double)` |
| `d_fit_widget` | `pole_estimate_13_angle_changed(double)` | `this` | `handle_pole_estimate_13_angle_changed(double)` |
| `button_close` | `rejected()` | `this` | `handle_close()` |
| `button_import_file` | `clicked()` | `this` | `handle_import_hellinger_file()` |
| `button_export_pick_file` | `clicked()` | `this` | `handle_export_pick_file()` |
| `button_export_com_file` | `clicked()` | `this` | `handle_export_com_file()` |
| `button_output_path` | `clicked()` | `this` | `handle_output_path_button_clicked()` |
| `line_edit_output_path` | `editingFinished()` | `this` | `handle_output_path_editing_finished()` |
| `line_edit_output_path` | `textChanged(const QString&)` | `this` | `handle_output_path_changed()` |
| `d_fit_widget` | `pole_estimate_12_changed(double, double)` | `this` | `handle_pole_estimate_12_changed(double, double)` |
| `d_fit_widget` | `pole_estimate_13_changed(double, double)` | `this` | `handle_pole_estimate_13_changed(double, double)` |
| `d_fit_widget` | `pole_estimate_12_angle_changed(double)` | `this` | `handle_pole_estimate_12_angle_changed(double)` |
| `d_fit_widget` | `pole_estimate_13_angle_changed(double)` | `this` | `handle_pole_estimate_13_angle_changed(double)` |

*... and 21 more connections.*


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/HellingerDialog.h
python scripts/gpq.py def GPlatesQtWidgets::HellingerDialog --body
python scripts/gpq.py uses HellingerDialog --kind class
python scripts/gpq.py hier HellingerDialog
```
