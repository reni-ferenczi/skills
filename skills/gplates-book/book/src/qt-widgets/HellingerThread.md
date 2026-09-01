# HellingerThread

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 267 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/HellingerThread.h` | C++ | 139 |
| `src/qt-widgets/HellingerThread.cc` | C++ | 309 |

## Overview

[[[PROSE overview unit=qt-widgets/HellingerThread tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=qt-widgets/HellingerThread tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
