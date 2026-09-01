# OpenFileDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1335 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/OpenFileDialog.h` | C++ | 119 |
| `src/qt-widgets/OpenFileDialog.cc` | C++ | 84 |

## Overview

[[[PROSE overview unit=qt-widgets/OpenFileDialog tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::OpenFileDialog`](#gplatesqtwidgetsopenfiledialog) | class | — | — | 0 | — |

## Members

### `GPlatesQtWidgets::OpenFileDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `filter_list_type` | typedef | `std::vector<FileDialogFilter>` | public | Typedef for a sequence of FileDialogFilter. |
| `OpenFileDialog( QWidget *parent, const QString &caption, Iterator filters_begin, Iterator filters_end, GPlatesGui::DirectoryConfiguration &configuration)` | constructor | `None` | public | Constructs an OpenFileDialog with a sequence of FileDialogFilter specified by filters\_begin and filters\_end. |
| `OpenFileDialog( QWidget *parent, const QString &caption, const filter_list_type &filters, GPlatesGui::DirectoryConfiguration &configuration)` | constructor | `None` | public | Constructs an OpenFileDialog with a sequence of FileDialogFilter specified by filters. |
| `OpenFileDialog( QWidget *parent, const QString &caption, const QString &filter, GPlatesPresentation::ViewState &view_state)` | constructor | `None` | public | Constructs an OpenFileDialog with a preformatted filter, which should look something like: "Text Documents (\*.txt \*.foo);;All Files (\*)" |
| `get_open_file_name()` | method | `QString` | public | Prompts the user to select one file name and returns it. |
| `get_open_file_names()` | method | `QStringList` | public | Prompts the user to select at least one file name and returns them in a list. |
| `d_parent` | field | `QWidget` | private | — |
| `d_caption` | field | `QString` | private | — |
| `d_filter` | field | `QString` | private | — |
| `d_selected_filter` | field | `QString` | private | — |
| `d_directory_configuration` | field | `GPlatesGui::DirectoryConfiguration` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_OPENFILEDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/OpenFileDialog tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 17 |
| [qt-widgets/ColouringDialog](ColouringDialog.md) | qt-widgets | 7 |
| [qt-widgets/PythonConsoleDialog](PythonConsoleDialog.md) | qt-widgets | 5 |
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 5 |
| [qt-widgets/ScalarField3DLayerOptionsWidget](ScalarField3DLayerOptionsWidget.md) | qt-widgets | 4 |
| [qt-widgets/ImportRasterDialog](ImportRasterDialog.md) | qt-widgets | 3 |
| [qt-widgets/RasterLayerOptionsWidget](RasterLayerOptionsWidget.md) | qt-widgets | 3 |
| [qt-widgets/ReconstructScalarCoverageLayerOptionsWidget](ReconstructScalarCoverageLayerOptionsWidget.md) | qt-widgets | 3 |
| [qt-widgets/ScalarField3DDepthLayersPage](ScalarField3DDepthLayersPage.md) | qt-widgets | 3 |
| [qt-widgets/TimeDependentRasterPage](TimeDependentRasterPage.md) | qt-widgets | 3 |
| [qt-widgets/AgeModelManagerDialog](AgeModelManagerDialog.md) | qt-widgets | 2 |
| [qt-widgets/ImportScalarField3DDialog](ImportScalarField3DDialog.md) | qt-widgets | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/OpenFileDialog.h
python scripts/gpq.py def GPlatesQtWidgets::OpenFileDialog --body
python scripts/gpq.py uses OpenFileDialog --kind class
python scripts/gpq.py hier OpenFileDialog
```
