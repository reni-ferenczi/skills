# GenerateVelocityDomainLatLonDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 371 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/GenerateVelocityDomainLatLonDialog.h` | C++ | 140 |
| `src/qt-widgets/GenerateVelocityDomainLatLonDialog.cc` | C++ | 611 |
| `src/qt-widgets/GenerateVelocityDomainLatLonDialogUi.ui` | Qt form | 603 |

## Overview

[[[PROSE overview unit=qt-widgets/GenerateVelocityDomainLatLonDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::GenerateVelocityDomainLatLonDialog`](#gplatesqtwidgetsgeneratevelocitydomainlatlondialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_GenerateVelocityDomainLatLonDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::GenerateVelocityDomainLatLonDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GenerateVelocityDomainLatLonDialog( ViewportWindow &main_window_, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `generate_velocity_domain()` | method | `void` | private | — |
| `react_top_extents_spin_box_value_changed( double value)` | method | `void` | private | — |
| `react_bottom_extents_spin_box_value_changed( double value)` | method | `void` | private | — |
| `react_left_extents_spin_box_value_changed( double value)` | method | `void` | private | — |
| `react_right_extents_spin_box_value_changed( double value)` | method | `void` | private | — |
| `handle_use_global_extents_button_clicked()` | method | `void` | private | — |
| `handle_num_latitude_grid_intervals_value_changed( int num_latitude_grid_intervals)` | method | `void` | private | — |
| `handle_num_longitude_grid_intervals_value_changed( int num_longitude_grid_intervals)` | method | `void` | private | — |
| `react_cell_centred_check_box_changed()` | method | `void` | private | — |
| `set_path()` | method | `void` | private | — |
| `select_path()` | method | `void` | private | — |
| `set_file_name_template()` | method | `void` | private | — |
| `d_main_window` | field | `ViewportWindow` | private | — |
| `d_num_latitude_grid_intervals` | field | `unsigned int` | private | — |
| `d_num_longitude_grid_intervals` | field | `unsigned int` | private | — |
| `d_extents_top` | field | `double` | private | — |
| `d_extents_bottom` | field | `double` | private | — |
| `d_extents_left` | field | `double` | private | — |
| `d_extents_right` | field | `double` | private | — |
| `d_cell_centred_nodes` | field | `bool` | private | — |
| `d_path` | field | `QString` | private | — |
| `d_file_name_template` | field | `std::string` | private | — |
| `d_help_dialog_configuration` | field | `InformationDialog` | private | — |
| `d_help_dialog_output` | field | `InformationDialog` | private | — |
| `d_open_directory_dialog` | field | `OpenDirectoryDialog` | private | — |
| `get_num_latitude_nodes()` | method | `unsigned int` | private | — |
| `get_num_longitude_nodes()` | method | `unsigned int` | private | — |
| `display_num_nodes()` | method | `void` | private | — |
| `generate_lat_lon_domain()` | method | `GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type` | private | — |
| `save_velocity_domain_file( const GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type &velocity_sub_domain)` | method | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `NUM_LATITUDE_GRID_INTERVALS_PLACE_HOLDER` | variable | `std::string` | — |
| `NUM_LONGITUDE_GRID_INTERVALS_PLACE_HOLDER` | variable | `std::string` | — |
| `HELP_DIALOG_TITLE_CONFIGURATION` | variable | `char` | — |
| `HELP_DIALOG_TEXT_CONFIGURATION` | variable | `char` | — |
| `HELP_DIALOG_TITLE_OUTPUT` | variable | `char` | — |
| `HELP_DIALOG_TEXT_OUTPUT` | variable | `char` | — |
| `replace_place_holder( std::string &str, const std::string &place_holder, const std::string &replacement)` | function | `void` | Replace all occurrences of a place holder substring with its replacement substring. |
| `GENERATE_VELOCITY_DOMAIN_LATLON_DIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/GenerateVelocityDomainLatLonDialog tier=3]]]
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
| `GenerateVelocityDomainLatLonDialog` | `QDialog` | Generate Latitude/Longitude Velocity Domain Points | 33 |

**Qt signal/slot connections** (15 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `top_extents_spinbox` | `valueChanged(double)` | `this` | `react_top_extents_spin_box_value_changed(double)` |
| `bottom_extents_spinbox` | `valueChanged(double)` | `this` | `react_bottom_extents_spin_box_value_changed(double)` |
| `left_extents_spinbox` | `valueChanged(double)` | `this` | `react_left_extents_spin_box_value_changed(double)` |
| `right_extents_spinbox` | `valueChanged(double)` | `this` | `react_right_extents_spin_box_value_changed(double)` |
| `use_global_extents_button` | `clicked()` | `this` | `handle_use_global_extents_button_clicked()` |
| `lattitude_grid_intervals_spinbox` | `valueChanged(int)` | `this` | `handle_num_latitude_grid_intervals_value_changed(int)` |
| `longitude_grid_intervals_spinbox` | `valueChanged(int)` | `this` | `handle_num_longitude_grid_intervals_value_changed(int)` |
| `cell_centred_checkbox` | `stateChanged(int)` | `this` | `react_cell_centred_check_box_changed()` |
| `button_path` | `clicked()` | `this` | `select_path()` |
| `lineEdit_path` | `editingFinished()` | `this` | `set_path()` |
| `lineEdit_file_name_template` | `editingFinished()` | `this` | `set_file_name_template()` |
| `pushButton_info_output` | `clicked()` | `d_help_dialog_output` | `show()` |
| `pushButton_info_configuration` | `clicked()` | `d_help_dialog_configuration` | `show()` |
| `main_buttonbox` | `accepted()` | `this` | `generate_velocity_domain()` |
| `main_buttonbox` | `rejected()` | `this` | `reject()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/GenerateVelocityDomainLatLonDialog.h
python scripts/gpq.py def GPlatesQtWidgets::GenerateVelocityDomainLatLonDialog --body
python scripts/gpq.py uses GenerateVelocityDomainLatLonDialog --kind class
python scripts/gpq.py hier GenerateVelocityDomainLatLonDialog
```
