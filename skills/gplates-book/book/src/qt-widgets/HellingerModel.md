# HellingerModel

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 52 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/HellingerModel.h` | C++ | 618 |
| `src/qt-widgets/HellingerModel.cc` | C++ | 580 |

## Overview

This is the whole data model behind GPlates' Hellinger pole-fitting tool: the
picks the user has digitised, the parameters that drive the fit, and the results
that come back. It is a plain C++ class — no `QObject`, no signals, no dependency
on anything but `GPlatesMaths::LatLonPoint` — deliberately kept as a passive value
holder that `HellingerDialog` and its sub-widgets (`HellingerPickWidget`,
`HellingerFitWidget`, `HellingerSegmentDialog`, `HellingerPointDialog`) all point
at. It lives in `qt-widgets` only because that is where its owner lives; nothing
about it is Qt-specific beyond the use of `QString`.

The shape of the class is dictated by the Hellinger `.com` file format.
`HellingerComFileStructure` is a field-for-field mirror of the parameter file that
the original FORTRAN `hellinger1`/`hellinger3` codes read, and the model stores one
of them as its live parameter block — so most of the "settings" accessors are thin
forwarders onto `d_active_com_file_struct` rather than state of their own.
`GPlatesFileIO::HellingerReader` and `GPlatesFileIO::HellingerWriter` populate and
serialise both that struct and the picks; the reader is also what parses the fit
results and error-ellipse point lists back out of the temporary files the solver
writes.

The picks themselves are a `std::multimap<int, HellingerPick>` keyed by segment
number, and much of the class is the bookkeeping that keying implies:
`renumber_segments()`, `make_space_for_new_segment()`, `segments_are_ordered()`,
and a family of accessors that address a pick by (segment, row) by walking the
`equal_range` for the segment. Actually computing a fit is not this class's job.
`HellingerThread` reads the parameters straight off the model and passes them as
arguments to `calculate_pole_2_way` / `calculate_pole_3_way` in a Python script
executed through Boost.Python; the picks reach that script as a temporary pick file
written by `HellingerWriter`, and the answers come back through `HellingerReader`
into `set_fit_12()` and friends. So the model is the shared clipboard between the
UI, the file-io layer and the Python solver, not a participant in the computation.

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

**The enumerator values are a file format.** `HellingerPlateIndex` is numbered
1, 2, 3 and 31, 32, 33 because those are the plate codes written in and read from
Hellinger pick files. Renumbering them silently breaks every existing `.pick` file.

**"Enabled" is stored twice and the two copies can disagree.** A pick's state
lives both in `HellingerPick::d_is_enabled` and in whether `d_segment_type` is a
`PLATE_n_PICK_TYPE` or a `DISABLED_PLATE_n_PICK_TYPE`. The header's own FIXME
flags this; `set_pick_state()` updates only the boolean. Any code that reads the
enumerator — the writers, and `determine_fit_type_from_model()` — sees the other
copy, so keep both in step whenever you touch a pick.

**Row indices are positional and volatile.** `get_pick()`, `remove_pick()`,
`pick_is_enabled()` and `set_pick_state()` address a pick by counting forward
through the segment's `equal_range`, so every row after a removal or insertion
renumbers. Out-of-range access is silent rather than diagnosed: `get_pick()`
returns `end()` (compare against the model's `end()` before dereferencing),
`pick_is_enabled()` returns `false` — indistinguishable from a genuinely disabled
pick — and `remove_pick()` and `set_pick_state()` simply do nothing.

**Segment numbering invariants.** `renumber_segments()` documents that it assumes
keys are `>= 1`; with a segment 0 present it produces a zero-based result instead.
`make_space_for_new_segment()` does not insert anything — it renumbers everything
from `segment` upward by one to leave a hole, and the caller must then fill it.
`segments_are_ordered()` is the check for the contiguous-from-1 invariant that
most of the UI assumes; it is also O(n²), since it calls `unique_keys()` — which
builds a fresh `std::set` over the whole multimap — once per iteration of its loop.
`number_of_segments()` has the same per-call cost, so avoid it in inner loops.

**No thread safety, and the fit runs on another thread.** `HellingerThread` is a
`QThread` holding a raw `HellingerModel *`; its `run()` reads the parameter
accessors from the worker thread while the dialog still owns the model on the GUI
thread. Nothing here locks. The current code stays safe only because the dialog
does not touch the model between `start()` and `handle_thread_finished()` — keep
it that way, and write results back only from the `finished()` slot.

**Which tolerance you get depends on the current fit type.** The no-argument
`set_amoeba_tolerance()` and `get_amoeba_tolerance()` dispatch on `d_fit_type`, so
changing the fit type silently retargets them at a different field with a very
different default (`1e-10` for two-way, `0.005` for three-way). `get_fit_type(true)`
recomputes the type from the picks and *writes* it back — it is not a pure
accessor, and it decides three-way purely on the presence of any plate-three pick,
enabled or not.

**Partial construction and dead members.** `HellingerPick`'s default constructor
leaves all five fields indeterminate, and `HellingerComFileStructure`'s constructor
leaves `d_search_radius_degrees`, `d_significance_level`,
`d_number_of_grid_iterations` and `d_number_amoeba_iterations` uninitialised —
they are expected to be filled by the reader or the UI. `add_segment()` is
declared but never defined anywhere in the tree; calling it is a link error.
`clear_com_file_struct()` is defined but never called, so `reset_model()` clears
picks and results while leaving the previous run's parameters, pick filename and
initial guesses in place. Note also that if it were called it would set
`d_generate_output_files` to `false`, the opposite of the constructor's default.

**Two incompatible ellipse filename schemes.** The no-argument
`error_ellipse_filename()` yields `<root>_ellipse.dat` while the
`HellingerPlatePairType` overload yields `<root>_ellipse_12_sim.dat` and so on.
They are not variants of one scheme; pick the one that matches what the Python
solver actually wrote.

`unique_keys()` and `determine_fit_type_from_model()` are in an anonymous
namespace in the `.cc` and are not linkable from elsewhere.

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
