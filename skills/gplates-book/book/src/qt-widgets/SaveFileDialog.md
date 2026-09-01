# SaveFileDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 970 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/SaveFileDialog.h` | C++ | 148 |
| `src/qt-widgets/SaveFileDialog.cc` | C++ | 113 |

## Overview

[[[PROSE overview unit=qt-widgets/SaveFileDialog tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::SaveFileDialog`](#gplatesqtwidgetssavefiledialog) | class | — | — | 0 | SaveFileDialog retrieves a file name for saving from the user. |

## Members

### `GPlatesQtWidgets::SaveFileDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `filter_list_type` | typedef | `std::vector<FileDialogFilter>` | public | Typedef for a sequence of FileDialogFilter. |
| `~SaveFileDialog()` | destructor | `None` | public | — |
| `SaveFileDialog( QWidget *parent, const QString &caption, const filter_list_type &filters, GPlatesPresentation::ViewState &view_state)` | constructor | `None` | public | Constructs a SaveFileDialog. |
| `SaveFileDialog( QWidget *parent, const QString &caption, const filter_list_type &filters, GPlatesGui::DirectoryConfiguration &configuration)` | constructor | `None` | public | Constructs a SaveFileDialog. |
| `get_file_name( QString *selected_filter = NULL)` | method | `boost::optional<QString>` | public | Gets a file name from the user. returned in this variable. |
| `set_filters( const filter_list_type &filters)` | method | `void` | public | Changes the filters used by the dialog box. |
| `select_file( const QString &file_path)` | method | `void` | public | Selects a file in the dialog box. |
| `d_impl` | field | `boost::scoped_ptr<SaveFileDialogInternals::SaveFileDialogImpl>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_USE_NATIVE_FILE_DIALOG` | macro | `None` | — |
| `GPLATES_QTWIDGETS_SAVEFILEDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/SaveFileDialog tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/SaveFileDialogImpl](SaveFileDialogImpl.md) | qt-widgets | 18 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 15 |
| [qt-widgets/ExportCoordinatesDialog](ExportCoordinatesDialog.md) | qt-widgets | 14 |
| [qt-widgets/KinematicGraphsDialog](KinematicGraphsDialog.md) | qt-widgets | 8 |
| [qt-widgets/ColourScaleWidget](ColourScaleWidget.md) | qt-widgets | 7 |
| [qt-widgets/TotalReconstructionPolesDialog](TotalReconstructionPolesDialog.md) | qt-widgets | 7 |
| [qt-widgets/PythonConsoleDialog](PythonConsoleDialog.md) | qt-widgets | 5 |
| [qt-widgets/CoRegistrationResultTableDialog](CoRegistrationResultTableDialog.md) | qt-widgets | 1 |
| [qt-widgets/ManageFeatureCollectionsDialog](ManageFeatureCollectionsDialog.md) | qt-widgets | 1 |
| [qt-widgets/ViewportWindow](ViewportWindow.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/SaveFileDialog.h
python scripts/gpq.py def GPlatesQtWidgets::SaveFileDialog --body
python scripts/gpq.py uses SaveFileDialog --kind class
python scripts/gpq.py hier SaveFileDialog
```
