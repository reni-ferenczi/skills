# HellingerThread

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 267 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/HellingerThread.h` | C++ | 139 |
| `src/qt-widgets/HellingerThread.cc` | C++ | 309 |

## Overview

`HellingerThread` runs the Hellinger pole-fitting and uncertainty calculations on a background `QThread` so the actual number-crunching, which is delegated to Python, does not block the GUI. `run()` dispatches on `d_thread_type` (`TWO_WAY_POLE_THREAD_TYPE`, `THREE_WAY_POLE_THREAD_TYPE`, `TWO_WAY_UNCERTAINTY_THREAD_TYPE`, `THREE_WAY_UNCERTAINTY_THREAD_TYPE`) to one of `calculate_two_way_fit()`, `calculate_three_way_fit()`, `calculate_two_way_uncertainties()` or `calculate_three_way_uncertainties()`. Each of these takes a `GPlatesApi::PythonInterpreterLocker`, `exec_file`s the bundled `hellinger.py` (`d_python_file`) into the embedded interpreter, and calls a named function in it (e.g. `calculate_pole_2_way`) with the current picks and fit parameters read from `HellingerModel`, passing file paths rather than in-memory data — picks and results are handed to and from the Python side entirely via temporary files under `d_path_for_temporary_files` (`temp_pick_filename()`, `temp_result_filename()`, `temp_par_filename()`).

`HellingerDialog` owns one `HellingerThread`, configures it with `initialise()` and `set_python_script_type()`, starts it, and picks up the result once the thread's `finished` signal fires.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ThreadType`](#gplatesqtwidgetsthreadtype) | enum | — | — | 0 | — |
| [`GPlatesQtWidgets::HellingerThread`](#gplatesqtwidgetshellingerthread) | class | `QThread` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ThreadType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TWO_WAY_POLE_THREAD_TYPE` | enumerator | `None` | — | — |
| `THREE_WAY_POLE_THREAD_TYPE` | enumerator | `None` | — | — |
| `TWO_WAY_UNCERTAINTY_THREAD_TYPE` | enumerator | `None` | — | — |
| `THREE_WAY_UNCERTAINTY_THREAD_TYPE` | enumerator | `None` | — | — |
| `NUM_THREAD_TYPES` | enumerator | `None` | — | — |

### `GPlatesQtWidgets::HellingerThread`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `HellingerThread( HellingerDialog *hellinger_dialog, HellingerModel *hellinger_model)` | constructor | `None` | public | — |
| `run()` | method | `void` | public | — |
| `temp_pick_filename()` | method | `QString` | public | — |
| `temp_result_filename()` | method | `QString` | public | — |
| `temp_par_filename()` | method | `QString` | public | — |
| `path()` | method | `QString` | public | — |
| `thread_failed()` | method | `bool` | public | — |
| `initialise(const QString &python_file, const QString &output_path, const QString &results_filename_root, const QString &temporary_path)` | method | `void` | public | — |
| `set_python_script_type(ThreadType thread_type)` | method | `void` | public | — |
| `calculate_two_way_fit()` | method | `void` | private | — |
| `calculate_three_way_fit()` | method | `void` | private | — |
| `calculate_two_way_uncertainties()` | method | `void` | private | — |
| `calculate_three_way_uncertainties()` | method | `void` | private | — |
| `d_hellinger_dialog_ptr` | field | `HellingerDialog` | private | — |
| `d_hellinger_model_ptr` | field | `HellingerModel` | private | — |
| `d_thread_type` | field | `ThreadType` | private | — |
| `d_python_file` | field | `QString` | private | d\_python\_file - the main hellinger python file (hellinger.py) including the path. |
| `d_output_path` | field | `QString` | private | d\_output\_path - path for outputting results |
| `d_results_filename_root` | field | `QString` | private | — |
| `d_path_for_temporary_files` | field | `QString` | private | d\_path\_for\_temporary\_files - Data are communicated to and from the python scripts by file - these are stored in the location given by d\_path\_for\_temporary\_files. |
| `d_temp_pick_file` | field | `QString` | private | Various temporary files for communication with python. |
| `d_temp_result_filename` | field | `QString` | private | — |
| `d_temp_par` | field | `QString` | private | — |
| `d_temp_res` | field | `QString` | private | — |
| `d_thread_failed` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `BOOST_PYTHON_MAX_ARITY` | macro | `16` | This definition sets the maximum number of parameters that you can send to a boost python function. |
| `TEMP_PICK_FILENAME` | variable | `QString` | — |
| `TEMP_RESULT_FILENAME` | variable | `QString` | — |
| `TEMP_PAR_FILENAME` | variable | `QString` | — |
| `TEMP_RES_FILENAME` | variable | `QString` | — |
| `GPLATES_QTWIDGETS_HELLINGERTHREAD_H` | macro | `None` | — |

## Notes

`d_hellinger_dialog_ptr` and `d_hellinger_model_ptr` are non-owning pointers into objects owned by `HellingerDialog`; because `run()` executes on a separate thread, both must remain valid and effectively read-only from the GUI thread's perspective for the duration of the run. `BOOST_PYTHON_MAX_ARITY` is defined to 16 in the `.cc` (before any Boost.Python header is included) because `calculate_pole_2_way` and its three-way counterpart are called with more arguments than Boost.Python's default arity limit allows.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/HellingerDialog](HellingerDialog.md) | qt-widgets | 18 |
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 3 |
| [presentation/Session](../presentation/Session.md) | presentation | 2 |
| [qt-widgets/ColouringDialog](ColouringDialog.md) | qt-widgets | 2 |
| [qt-widgets/ConnectWFSDialog](ConnectWFSDialog.md) | qt-widgets | 2 |
| [qt-widgets/OpenFileDialog](OpenFileDialog.md) | qt-widgets | 2 |
| [qt-widgets/SaveFileDialogImpl](SaveFileDialogImpl.md) | qt-widgets | 2 |
| [qt-widgets/ScalarField3DLayerOptionsWidget](ScalarField3DLayerOptionsWidget.md) | qt-widgets | 2 |
| [cli/CliFeatureCollectionFileIO](../cli/CliFeatureCollectionFileIO.md) | cli | 1 |
| [file-io/FileInfo](../file-io/FileInfo.md) | file-io | 1 |
| [qt-widgets/AssignReconstructionPlateIdsDialog](AssignReconstructionPlateIdsDialog.md) | qt-widgets | 1 |
| [qt-widgets/ImportRasterDialog](ImportRasterDialog.md) | qt-widgets | 1 |
| [qt-widgets/ManageFeatureCollectionsDialog](ManageFeatureCollectionsDialog.md) | qt-widgets | 1 |
| [qt-widgets/PythonArgumentWidget](PythonArgumentWidget.md) | qt-widgets | 1 |
| [qt-widgets/RasterLayerOptionsWidget](RasterLayerOptionsWidget.md) | qt-widgets | 1 |
| [qt-widgets/ReconstructScalarCoverageLayerOptionsWidget](ReconstructScalarCoverageLayerOptionsWidget.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/HellingerThread.h
python scripts/gpq.py def GPlatesQtWidgets::HellingerThread --body
python scripts/gpq.py uses HellingerThread --kind class
python scripts/gpq.py hier HellingerThread
```
