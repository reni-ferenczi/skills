# HellingerModel

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 52 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/HellingerModel.h` | C++ | 618 |
| `src/qt-widgets/HellingerModel.cc` | C++ | 580 |

## Overview

[[[PROSE overview unit=qt-widgets/HellingerModel tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::HellingerFitType`](#gplatesqtwidgetshellingerfittype) | enum | — | — | 0 | — |
| [`GPlatesQtWidgets::HellingerPlateIndex`](#gplatesqtwidgetshellingerplateindex) | enum | — | — | 0 | — |
| [`GPlatesQtWidgets::HellingerPlatePairType`](#gplatesqtwidgetshellingerplatepairtype) | enum | — | — | 0 | — |
| [`GPlatesQtWidgets::HellingerPick`](#gplatesqtwidgetshellingerpick) | struct | — | — | 0 | NOTE: should the pick structure contain its segment number? |
| [`GPlatesQtWidgets::HellingerPoleEstimate`](#gplatesqtwidgetshellingerpoleestimate) | struct | — | — | 0 | — |
| [`GPlatesQtWidgets::hellinger_model_type`](#gplatesqtwidgetshellinger_model_type) | typedef | — | — | 0 | — |
| [`GPlatesQtWidgets::hellinger_model_pair_type`](#gplatesqtwidgetshellinger_model_pair_type) | typedef | — | — | 0 | — |
| [`GPlatesQtWidgets::hellinger_model_const_range_type`](#gplatesqtwidgetshellinger_model_const_range_type) | typedef | — | — | 0 | — |
| [`GPlatesQtWidgets::hellinger_model_range_type`](#gplatesqtwidgetshellinger_model_range_type) | typedef | — | — | 0 | — |
| [`GPlatesQtWidgets::hellinger_segment_type`](#gplatesqtwidgetshellinger_segment_type) | typedef | — | — | 0 | — |
| [`GPlatesQtWidgets::HellingerComFileStructure`](#gplatesqtwidgetshellingercomfilestructure) | struct | — | — | 0 | The HellingerComFileStructure struct This structure mirrors the content of a Hellinger .com file. |
| [`GPlatesQtWidgets::HellingerFitStructure`](#gplatesqtwidgetshellingerfitstructure) | struct | — | — | 0 | The result of the fit. |
| [`GPlatesQtWidgets::HellingerModel`](#gplatesqtwidgetshellingermodel) | class | — | — | 0 | The HellingerModel class This class holds the input data for the hellinger fit (picks, initial guess etc) and the output results (the pole, and associated uncertainty/goodness-of-fit info). |

## Members

### `GPlatesQtWidgets::HellingerFitType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TWO_PLATE_FIT_TYPE` | enumerator | `None` | — | — |
| `THREE_PLATE_FIT_TYPE` | enumerator | `None` | — | — |

### `GPlatesQtWidgets::HellingerPlateIndex`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PLATE_ONE_PICK_TYPE` | enumerator | `None` | — | — |
| `PLATE_TWO_PICK_TYPE` | enumerator | `None` | — | — |
| `PLATE_THREE_PICK_TYPE` | enumerator | `None` | — | — |
| `DISABLED_PLATE_ONE_PICK_TYPE` | enumerator | `None` | — | — |
| `DISABLED_PLATE_TWO_PICK_TYPE` | enumerator | `None` | — | — |
| `DISABLED_PLATE_THREE_PICK_TYPE` | enumerator | `None` | — | — |

### `GPlatesQtWidgets::HellingerPlatePairType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PLATES_1_2_PAIR_TYPE` | enumerator | `None` | — | — |
| `PLATES_1_3_PAIR_TYPE` | enumerator | `None` | — | — |
| `PLATES_2_3_PAIR_TYPE` | enumerator | `None` | — | — |

### `GPlatesQtWidgets::HellingerPick`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `HellingerPick( const HellingerPlateIndex &type, const double &lat, const double &lon, const double &uncertainty, const bool &enabled)` | constructor | `None` | public | — |
| `HellingerPick()` | constructor | `None` | public | — |
| `d_segment_type` | field | `HellingerPlateIndex` | public | — |
| `d_lat` | field | `double` | public | — |
| `d_lon` | field | `double` | public | — |
| `d_uncertainty` | field | `double` | public | — |
| `d_is_enabled` | field | `bool` | public | — |

### `GPlatesQtWidgets::HellingerPoleEstimate`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `HellingerPoleEstimate()` | constructor | `None` | public | — |
| `HellingerPoleEstimate( const double &lat, const double &lon, const double &angle)` | constructor | `None` | public | — |
| `d_lat` | field | `double` | public | — |
| `d_lon` | field | `double` | public | — |
| `d_angle` | field | `double` | public | — |

### `GPlatesQtWidgets::hellinger_model_type`

*None.*

### `GPlatesQtWidgets::hellinger_model_pair_type`

*None.*

### `GPlatesQtWidgets::hellinger_model_const_range_type`

*None.*

### `GPlatesQtWidgets::hellinger_model_range_type`

*None.*

### `GPlatesQtWidgets::hellinger_segment_type`

*None.*

### `GPlatesQtWidgets::HellingerComFileStructure`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `HellingerComFileStructure()` | constructor | `None` | public | — |
| `d_pick_file` | field | `QString` | public | — |
| `d_estimate_12` | field | `HellingerPoleEstimate` | public | — |
| `d_estimate_13` | field | `HellingerPoleEstimate` | public | — |
| `d_search_radius_degrees` | field | `double` | public | — |
| `d_perform_grid_search` | field | `bool` | public | — |
| `d_number_of_grid_iterations` | field | `unsigned int` | public | — |
| `d_use_amoeba_iteration_limit` | field | `bool` | public | — |
| `d_number_amoeba_iterations` | field | `unsigned int` | public | — |
| `d_use_amoeba_tolerance` | field | `bool` | public | — |
| `d_amoeba_two_way_tolerance` | field | `double` | public | — |
| `d_amoeba_three_way_tolerance` | field | `double` | public | — |
| `d_significance_level` | field | `double` | public | — |
| `d_estimate_kappa` | field | `bool` | public | — |
| `d_generate_output_files` | field | `bool` | public | — |
| `d_error_ellipse_filename_12` | field | `QString` | public | NOTE: for three-way fitting results, we have the 3 combinations of plate-pairs (12,13,23) and for each pair we have both simultaneous and individual results. |
| `d_upper_surface_filename_12` | field | `QString` | public | — |
| `d_lower_surface_filename_12` | field | `QString` | public | — |
| `d_error_ellipse_filename_13` | field | `QString` | public | — |
| `d_upper_surface_filename_13` | field | `QString` | public | — |
| `d_lower_surface_filename_13` | field | `QString` | public | — |
| `d_error_ellipse_filename_23` | field | `QString` | public | — |
| `d_upper_surface_filename_23` | field | `QString` | public | — |
| `d_lower_surface_filename_23` | field | `QString` | public | — |

### `GPlatesQtWidgets::HellingerFitStructure`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `HellingerFitStructure(double lat, double lon, double angle, double eps=0)` | constructor | `None` | public | — |
| `d_lat` | field | `double` | public | — |
| `d_lon` | field | `double` | public | — |
| `d_angle` | field | `double` | public | — |
| `d_eps` | field | `double` | public | — |

### `GPlatesQtWidgets::HellingerModel`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `HellingerModel()` | constructor | `None` | public | — |
| `add_pick(const HellingerPick &pick, const unsigned int &segment_number)` | method | `hellinger_model_type::const_iterator` | public | — |
| `add_segment(hellinger_segment_type &picks, const unsigned int &segment_number)` | method | `void` | public | — |
| `get_pick( const unsigned int &segment, const unsigned int &row)` | method | `hellinger_model_type::const_iterator` | public | boost::optional\<const HellingerPick &\> get\_pick( const unsigned int &index) const; |
| `pick_is_enabled( const unsigned int &segment, const unsigned int &row)` | method | `bool` | public | — |
| `set_pick_state( const unsigned int &segment, const unsigned int &row, bool enabled)` | method | `void` | public | — |
| `get_segment( const unsigned int &segment)` | method | `hellinger_segment_type` | public | — |
| `get_segment_as_range( const unsigned int &segment)` | method | `hellinger_model_const_range_type` | public | — |
| `num_rows_in_segment( const unsigned int &segment)` | method | `int` | public | — |
| `remove_pick( const unsigned int &segment, const unsigned int &row)` | method | `void` | public | — |
| `remove_segment( const unsigned int &segment)` | method | `void` | public | — |
| `reset_model()` | method | `void` | public | — |
| `clear_all_picks()` | method | `void` | public | — |
| `clear_fit_results()` | method | `void` | public | — |
| `clear_uncertainty_results()` | method | `void` | public | — |
| `set_fit_12( const HellingerFitStructure &fit_12)` | method | `void` | public | — |
| `set_fit_13( const HellingerFitStructure &fit_12)` | method | `void` | public | — |
| `set_fit_23( const HellingerFitStructure &fit_12)` | method | `void` | public | — |
| `set_com_file_structure( const HellingerComFileStructure &com_file_structure)` | method | `void` | public | — |
| `get_fit_12()` | method | `boost::optional<HellingerFitStructure>` | public | — |
| `get_fit_13()` | method | `boost::optional<HellingerFitStructure>` | public | — |
| `get_fit_23()` | method | `boost::optional<HellingerFitStructure>` | public | — |
| `error_ellipse_points` | field | `std::vector<GPlatesMaths::LatLonPoint>` | public | — |
| `get_initial_guess_12()` | method | `HellingerPoleEstimate` | public | — |
| `get_initial_guess_13()` | method | `HellingerPoleEstimate` | public | — |
| `set_initial_guess_12( const HellingerPoleEstimate &estimate)` | method | `void` | public | — |
| `set_initial_guess_13( const HellingerPoleEstimate &estimate)` | method | `void` | public | — |
| `set_initial_guess_12( const double &lat, const double &lon, const double &rho)` | method | `void` | public | — |
| `set_initial_guess_13( const double &lat, const double &lon, const double &rho)` | method | `void` | public | — |
| `set_search_radius( const double &radius)` | method | `void` | public | — |
| `get_search_radius()` | method | `double` | public | — |
| `set_confidence_level(const double &conf)` | method | `void` | public | — |
| `get_confidence_level()` | method | `double` | public | — |
| `get_grid_iterations()` | method | `int` | public | — |
| `get_grid_search()` | method | `bool` | public | — |
| `set_number_of_amoeba_iterations( const unsigned int &iterations)` | method | `void` | public | — |
| `get_amoeba_iterations()` | method | `unsigned int` | public | — |
| `get_amoeba_tolerance()` | method | `double` | public | — |
| `get_amoeba_two_way_tolerance()` | method | `double` | public | — |
| `get_amoeba_three_way_tolerance()` | method | `double` | public | — |
| `set_amoeba_two_way_tolerance( const double &tolerance)` | method | `void` | public | — |
| `set_amoeba_three_way_tolerance( const double &tolerance)` | method | `void` | public | — |
| `set_amoeba_tolerance( const double &tolerance)` | method | `void` | public | — |
| `set_amoeba_tolerance( const double &tolerance, const HellingerFitType &type)` | method | `void` | public | — |
| `get_use_amoeba_iterations()` | method | `bool` | public | — |
| `set_use_amoeba_iterations( bool use)` | method | `void` | public | — |
| `get_use_amoeba_tolerance()` | method | `bool` | public | — |
| `set_use_amoeba_tolerance( bool use)` | method | `void` | public | — |
| `set_estimate_kappa(bool estimate)` | method | `void` | public | — |
| `set_input_pick_filename( const QString &input_filename)` | method | `void` | public | — |
| `set_fit_type( const HellingerFitType &type)` | method | `void` | public | — |
| `get_fit_type` | field | `HellingerFitType` | public | — |
| `get_com_file()` | method | `boost::optional<HellingerComFileStructure>` | public | TODO: don't think we need this as optional.... check. |
| `get_pick_filename()` | method | `QString` | public | — |
| `get_chron_string()` | method | `QString` | public | — |
| `set_chron_string( const QString &chron_string)` | method | `void` | public | — |
| `begin()` | method | `hellinger_model_type::const_iterator` | public | — |
| `end()` | method | `hellinger_model_type::const_iterator` | public | — |
| `segment_begin( const int &segment)` | method | `hellinger_model_type::const_iterator` | public | — |
| `segment_end( const int &segment)` | method | `hellinger_model_type::const_iterator` | public | — |
| `segment_number_exists( int segment_num)` | method | `bool` | public | — |
| `make_space_for_new_segment( int segment)` | method | `void` | public | make\_space\_for\_new\_segment Shifts the segments from |
| `renumber_segments()` | method | `void` | public | renumber\_segments Reorganise the model such that segments numbers (i.e. the keys in the model multimap) are contiguous from 1. |
| `number_of_segments()` | method | `int` | public | — |
| `segments_are_ordered()` | method | `bool` | public | — |
| `clear_error_ellipse( const HellingerPlatePairType &type = PLATES_1_2_PAIR_TYPE)` | method | `void` | public | — |
| `clear_error_ellipses()` | method | `void` | public | — |
| `error_ellipse_filename()` | method | `QString` | public | — |
| `error_ellipse_filename( const HellingerPlatePairType &type)` | method | `QString` | public | — |
| `picks_are_valid()` | method | `bool` | public | — |
| `set_output_file_root( const QString &root)` | method | `void` | public | — |
| `output_file_root()` | method | `QString` | public | — |
| `set_model_data( const hellinger_model_type &model_data_)` | method | `void` | public | — |
| `clear_com_file_struct()` | method | `void` | private | — |
| `d_active_com_file_struct` | field | `HellingerComFileStructure` | private | — |
| `d_last_fit_12_result` | field | `boost::optional<HellingerFitStructure>` | private | — |
| `d_last_fit_13_result` | field | `boost::optional<HellingerFitStructure>` | private | — |
| `d_last_fit_23_result` | field | `boost::optional<HellingerFitStructure>` | private | — |
| `d_model_data` | field | `hellinger_model_type` | private | — |
| `d_error_ellipse_points` | field | `std::vector<GPlatesMaths::LatLonPoint>` | private | — |
| `d_error_ellipse_12_points` | field | `std::vector<GPlatesMaths::LatLonPoint>` | private | — |
| `d_error_ellipse_13_points` | field | `std::vector<GPlatesMaths::LatLonPoint>` | private | — |
| `d_error_ellipse_23_points` | field | `std::vector<GPlatesMaths::LatLonPoint>` | private | — |
| `d_chron_string` | field | `QString` | private | — |
| `d_fit_type` | field | `HellingerFitType` | private | d\_fit\_type. |
| `d_output_file_root` | field | `QString` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `unique_keys( const GPlatesQtWidgets::hellinger_model_type &model)` | function | `int` | — |
| `determine_fit_type_from_model( const GPlatesQtWidgets::hellinger_model_type &model_data)` | function | `GPlatesQtWidgets::HellingerFitType` | determine\_fit\_type\_from\_model - determine the fit type (i.e. two-way or three-way) of the model. |
| `GPLATES_QTWIDGETS_HELLINGERMODEL_H` | macro | `None` | — |
| `DEFAULT_OUTPUT_FILE_EXTENSION` | variable | `QString` | — |
| `INITIAL_AMOEBA_TWO_WAY_RESIDUAL` | variable | `double` | — |
| `INITIAL_AMOEBA_THREE_WAY_RESIDUAL` | variable | `double` | — |

## Notes

[[[PROSE notes unit=qt-widgets/HellingerModel tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/HellingerReader](../file-io/HellingerReader.md) | file-io | 178 |
| [qt-widgets/HellingerDialog](HellingerDialog.md) | qt-widgets | 146 |
| [qt-widgets/HellingerFitWidget](HellingerFitWidget.md) | qt-widgets | 83 |
| [qt-widgets/HellingerThread](HellingerThread.md) | qt-widgets | 53 |
| [qt-widgets/HellingerSegmentDialog](HellingerSegmentDialog.md) | qt-widgets | 51 |
| [file-io/HellingerWriter](../file-io/HellingerWriter.md) | file-io | 43 |
| [qt-widgets/HellingerPickWidget](HellingerPickWidget.md) | qt-widgets | 40 |
| [qt-widgets/HellingerPointDialog](HellingerPointDialog.md) | qt-widgets | 27 |
| [canvas-tools/AdjustFittedPoleEstimate](../canvas-tools/AdjustFittedPoleEstimate.md) | canvas-tools | 2 |
| [utils/ConfigBundle](../utils/ConfigBundle.md) | utils | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/HellingerModel.h
python scripts/gpq.py def GPlatesQtWidgets::HellingerModel --body
python scripts/gpq.py uses HellingerModel --kind class
python scripts/gpq.py hier HellingerModel
```
