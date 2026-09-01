# KinematicGraphsDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 118 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/KinematicGraphsDialog.h` | C++ | 398 |
| `src/qt-widgets/KinematicGraphsDialog.cc` | C++ | 1065 |
| `src/qt-widgets/KinematicGraphsDialogUi.ui` | Qt form | 577 |

## Overview

`KinematicGraphsDialog` is the "Kinematics Tool": for a chosen plate id, anchor plate and point (lat/lon), it walks a time range (`d_begin_time`..`d_end_time` in `d_step_time` increments) and, at each step, reconstructs the point with `GPlatesAppLogic::ReconstructionTree`/`RotationUtils` and computes velocities with `PlateVelocityUtils`, using the finite-difference scheme and delta-time chosen by the embedded `KinematicGraphsConfigurationWidget`/`Configuration`. Each step's results are stored as a `table_entries` row in `d_results`, driving both a `QStandardItemModel` table and a Qwt (`QwtPlot`/`QwtPlotCurve`) plot of whichever `KinematicGraphType` (latitude, longitude, velocity magnitude/azimuth/colatitude/longitude-component, angular velocity) the user has selected with the graph-type radio buttons. `handle_use_feature()` and `handle_use_animation()` let the user seed the lat/lon/plate-id or the time range from the currently focused feature or from the animation controller, instead of typing them in by hand.

`d_picker` (a `KinematicGraphPicker`, a `QwtPicker` subclass) reports plot coordinates as the mouse moves over the graph. `handle_auto_y_clicked()`, `handle_compress_y_clicked()` and `handle_stretch_y_clicked()` adjust `d_vertical_scale_power` per graph type to rescale the y-axis by powers of `VERTICAL_SCALE_MULTIPLIER`, since velocity and rotation-rate values can span several orders of magnitude across graph types. `handle_export_table()`/`handle_export_graph()` write the current results out through `GPlatesGui::CsvExport`, using the filter table built by `build_save_file_dialog_filters()` to offer the different CSV export option combinations in the save dialog.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`velocity_method_map_type`](#velocity_method_map_type) | typedef | — | — | 0 | — |
| [`(anonymous)::FileDialogFilterOption`](#anonymousfiledialogfilteroption) | struct | — | — | 0 | Struct to build the following table of file dialog filters / options. |
| [`(anonymous)::FileDialogFilterMapType`](#anonymousfiledialogfiltermaptype) | typedef | — | — | 0 | — |
| [`GPlatesQtWidgets::KinematicGraphsDialog`](#gplatesqtwidgetskinematicgraphsdialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_KinematicGraphsDialog` | — | 0 | — |

## Members

### `velocity_method_map_type`

*None.*

### `(anonymous)::FileDialogFilterOption`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `text` | field | `char` | public | — |
| `options` | field | `GPlatesGui::CsvExport::ExportOptions` | public | — |

### `(anonymous)::FileDialogFilterMapType`

*None.*

### `GPlatesQtWidgets::KinematicGraphsDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Configuration` | struct | `None` | public | — |
| `KinematicGraphType` | enum | `None` | public | — |
| `KinematicTableColumns` | enum | `None` | public | — |
| `table_entries` | struct | `None` | public | — |
| `results_type` | typedef | `std::vector<table_entries>` | public | — |
| `results_type_const_iterator` | typedef | `results_type::const_iterator` | public | — |
| `KinematicGraphsDialog( GPlatesPresentation::ViewState &view_state, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `handle_close()` | method | `void` | private | — |
| `handle_update()` | method | `void` | private | handle\_update Calculate new values for the table, and update the graph as appropriate. |
| `handle_settings_clicked()` | method | `void` | private | — |
| `handle_export_table()` | method | `void` | private | — |
| `handle_export_graph()` | method | `void` | private | — |
| `handle_graph_type_radio_toggled( bool state)` | method | `void` | private | — |
| `handle_use_feature()` | method | `void` | private | Handle the "use last-selected feature" button being clicked. |
| `handle_use_animation()` | method | `void` | private | handle\_use\_animation - handle the "use animation values" being clicked. |
| `handle_auto_y_clicked()` | method | `void` | private | handle\_auto\_y\_clicked - handle the "autoscale y axis" button. |
| `handle_compress_y_clicked()` | method | `void` | private | handle\_compress\_y\_clicked - handle the "compress y axis" button |
| `handle_stretch_y_clicked()` | method | `void` | private | handle\_stretch\_y\_clicked - handle the "stretch y axis" button. |
| `handle_flip_horizontal_axis()` | method | `void` | private | handle\_flip\_horizontal\_axis -handle the "flip horizontal axis" button. |
| `update_values_from_widgets()` | method | `void` | private | — |
| `update_table()` | method | `void` | private | — |
| `update_graph()` | method | `void` | private | — |
| `initialise_widgets()` | method | `void` | private | — |
| `set_up_connections()` | method | `void` | private | — |
| `set_graph_axes_and_titles()` | method | `void` | private | — |
| `set_up_axes_ranges()` | method | `void` | private | — |
| `set_up_plot()` | method | `void` | private | — |
| `check_and_highlight_bad_velocity_values()` | method | `void` | private | — |
| `read_values_from_preferences()` | method | `void` | private | — |
| `d_plot` | field | `QwtPlot` | private | m\_plot This widget is given the KinematicGraphsDialog as parent in the initialiser, so should be memory-managed by Qt. |
| `d_plot_curve` | field | `QwtPlotCurve` | private | m\_plot\_curve |
| `d_point_series_data` | field | `QwtPointSeriesData` | private | m\_point\_series\_data |
| `d_samples` | field | `QVector<QPointF>` | private | d\_samples |
| `d_picker` | field | `GPlatesQtWidgets::KinematicGraphPicker` | private | d\_picker - A QwtPicker (http://qwt.sourceforge.net/class\_qwt\_picker.html#details) is used to select data from a Qwt widget. |
| `d_title` | field | `QString` | private | Graph titles,units,ranges etc. |
| `d_x_axis_title` | field | `QString` | private | — |
| `d_y_axis_title` | field | `QString` | private | — |
| `d_x_axis_unit` | field | `QString` | private | — |
| `d_y_axis_unit` | field | `QString` | private | — |
| `d_x_min` | field | `double` | private | — |
| `d_x_max` | field | `double` | private | — |
| `d_y_min` | field | `double` | private | — |
| `d_y_max` | field | `double` | private | — |
| `d_vertical_scale_power` | field | `unsigned int` | private | d\_vertical\_scale\_factor For stretching/compressing the y-axis. |
| `d_vertical_scale_powers` | field | `unsigned int` | private | — |
| `d_vertical_scale_maxes` | field | `double` | private | — |
| `d_vertical_scale_mins` | field | `double` | private | — |
| `d_moving_id` | field | `GPlatesModel::integer_plate_id_type` | private | User-specified variables required for velocity calculations |
| `d_anchor_id` | field | `GPlatesModel::integer_plate_id_type` | private | — |
| `d_begin_time` | field | `double` | private | — |
| `d_end_time` | field | `double` | private | — |
| `d_step_time` | field | `double` | private | — |
| `d_lat` | field | `double` | private | — |
| `d_lon` | field | `double` | private | — |
| `d_graph_type` | field | `KinematicGraphType` | private | The type of graph (e.g. velocity vs time, latitude vs time...) |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | App state, for getting reconstruction features, preferences etc. |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | d\_view\_state, for getting animation control values etc. |
| `d_feature_focus` | field | `GPlatesGui::FeatureFocus` | private | The focussed feature - for pre-filling the lat/lon/plate-id etc. fields from the focussed feature. |
| `d_model` | field | `QStandardItemModel` | private | Data for the table-view. |
| `d_results` | field | `results_type` | private | d\_results - instance of a structure to hold the results of the kinematical calculations. |
| `d_save_file_dialog` | field | `SaveFileDialog` | private | d\_save\_file\_dialog - for exporting table. |
| `d_spin_box_palette` | field | `QPalette` | private | d\_spin\_box\_palette - the palette used in begin/end spinboxes. |
| `d_settings_dialog` | field | `KinematicGraphsConfigurationDialog` | private | d\_settings\_dialog - Dialog for letting user change details relating to velocity calculations. |
| `d_configuration` | field | `Configuration` | private | d\_configuration - instance of structure holding configuration for the velocity calculations - (e.g. time-step) |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `NUM_ELEMS` | macro_function | `(sizeof(a) / sizeof((a)[0]))` | — |
| `VERTICAL_SCALE_MULTIPLIER` | variable | `double` | — |
| `MAX_VERTICAL_SCALE_POWER` | variable | `unsigned int` | — |
| `MIN_VERTICAL_SCALE_POWER` | variable | `unsigned int` | — |
| `INITIAL_BEGIN_TIME` | variable | `double` | — |
| `INITIAL_END_TIME` | variable | `double` | — |
| `INITIAL_TIME_STEP` | variable | `double` | Set start-up time step to 5 Ma for 2.0 |
| `file_dialog_filter_table` | variable | `FileDialogFilterOption` | Table of filter options to present to the user when exporting CSV. |
| `build_save_file_dialog_filters()` | function | `GPlatesQtWidgets::SaveFileDialog::filter_list_type` | Construct filters to give to SaveFileDialog. |
| `append_row( QStandardItemModel *model, const GPlatesQtWidgets::KinematicGraphsDialog::table_entries &values)` | function | `void` | — |
| `get_data_from_result_structure( const GPlatesQtWidgets::KinematicGraphsDialog::KinematicGraphType &graph_type, const GPlatesQtWidgets::KinematicGraphsDialog::table_entries &result)` | function | `double` | — |
| `check_model_for_bad_velocity_values( QStandardItemModel *model, double velocity_threshold, std::vector<QModelIndex> &bad_indices)` | function | `void` | — |
| `highlight_bad_rows_in_table( QStandardItemModel *model, const std::vector<QModelIndex> &bad_indices, const QBrush &brush)` | function | `void` | — |
| `reset_table_background_colours( QStandardItemModel *model)` | function | `void` | — |
| `get_older_and_younger_times( const GPlatesQtWidgets::KinematicGraphsDialog::Configuration &configuration, const double &current_time, double &time_older, double &time_younger)` | function | `void` | get\_older\_and\_younger\_times - on return @time\_older and @time\_younger will hold the appropriate times for the velocity calculation at the @current\_time. |
| `GPLATES_QTWIDGETS_KINEMATICGRAPHSDIALOG_H` | macro | `None` | — |
| `INITIAL_DELTA_T` | variable | `double` | These values should be overridden by values read from preferences when the dialog is created. |
| `INITIAL_THRESHOLD_YELLOW` | variable | `double` | — |
| `INITIAL_THRESHOLD_RED` | variable | `double` | — |

## Notes

`d_plot`, `d_point_series_data` and `d_model` are constructed with `this` as their Qt parent and are not deleted explicitly. `KinematicGraphType` and `KinematicTableColumns` each keep `NUM_*` mid-enum followed by a `ROTATION_RATE_*` value, a deliberate "temp re-ordering to disable rotation rate" that leaves the last enumerator excluded from `NUM_GRAPH_TYPES`/`NUM_COLUMNS`-sized arrays and loops. `check_and_highlight_bad_velocity_values()` flags rows against the yellow/red thresholds from `d_configuration`, which are read once from preferences at construction (`read_values_from_preferences()`) and are otherwise independent of `KinematicGraphsConfigurationWidget`'s own preference-backed copies.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/KinematicGraphPicker](KinematicGraphPicker.md) | qt-widgets | 27 |
| [qt-widgets/KinematicGraphsConfigurationDialog](KinematicGraphsConfigurationDialog.md) | qt-widgets | 13 |
| [gui/Dialogs](../gui/Dialogs.md) | gui | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `KinematicGraphsDialog` | `QDialog` | Kinematics Tool | 39 |

**Qt signal/slot connections** (18 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_close` | `clicked()` | `this` | `handle_close()` |
| `button_update` | `clicked()` | `this` | `handle_update()` |
| `button_use_animation` | `clicked()` | `this` | `handle_use_animation()` |
| `button_use_feature` | `clicked()` | `this` | `handle_use_feature()` |
| `radio_latitude` | `toggled(bool)` | `this` | `handle_graph_type_radio_toggled(bool)` |
| `radio_longitude` | `toggled(bool)` | `this` | `handle_graph_type_radio_toggled(bool)` |
| `radio_velocity_mag` | `toggled(bool)` | `this` | `handle_graph_type_radio_toggled(bool)` |
| `radio_velocity_azimuth` | `toggled(bool)` | `this` | `handle_graph_type_radio_toggled(bool)` |
| `radio_velocity_colat` | `toggled(bool)` | `this` | `handle_graph_type_radio_toggled(bool)` |
| `radio_velocity_lon` | `toggled(bool)` | `this` | `handle_graph_type_radio_toggled(bool)` |
| `radio_angular_velocity` | `toggled(bool)` | `this` | `handle_graph_type_radio_toggled(bool)` |
| `radio_rotation_rate` | `toggled(bool)` | `this` | `handle_graph_type_radio_toggled(bool)` |
| `button_auto_y` | `clicked()` | `this` | `handle_auto_y_clicked()` |
| `button_compress_y` | `clicked()` | `this` | `handle_compress_y_clicked()` |
| `button_stretch_y` | `clicked()` | `this` | `handle_stretch_y_clicked()` |

*... and 3 more connections.*


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/KinematicGraphsDialog.h
python scripts/gpq.py def GPlatesQtWidgets::KinematicGraphsDialog --body
python scripts/gpq.py uses KinematicGraphsDialog --kind class
python scripts/gpq.py hier KinematicGraphsDialog
```
