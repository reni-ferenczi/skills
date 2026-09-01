# FileDialogFilter

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 903 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/FileDialogFilter.h` | C++ | 152 |

## Overview

[[[PROSE overview unit=qt-widgets/FileDialogFilter tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::FileDialogFilter`](#gplatesqtwidgetsfiledialogfilter) | class | — | — | 0 | FileDialogFilter encapsulates one file dialog filter entry, that has a description and a number of file extensions, the first of which is taken to be the "default" extension for that filter entry. |

## Members

### `GPlatesQtWidgets::FileDialogFilter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FileDialogFilter( const QString &description)` | constructor | `None` | public | — |
| `FileDialogFilter( const QString &description, const QString &extension)` | constructor | `None` | public | — |
| `FileDialogFilter( const QString &description, Iterator extensions_begin, Iterator extensions_end)` | constructor | `None` | public | — |
| `add_extension( const QString &extension)` | method | `void` | public | Adds extension to this filter. |
| `create_filter_string()` | method | `QString` | public | Returns the filter as a string that can be used with open and save file dialogs. |
| `create_filter_string( Iterator filters_begin, Iterator filters_end)` | method | `QString` | public | Creates the sequence of filters as a string that can be used with open and save file dialogs. |
| `d_description` | field | `QString` | private | — |
| `d_extensions` | field | `std::vector<QString>` | private | — |
| `d_cached_filter_string` | field | `boost::optional<QString>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_FILEDIALOGFILTER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/FileDialogFilter tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 10 |
| [qt-widgets/OpenFileDialog](OpenFileDialog.md) | qt-widgets | 6 |
| [qt-widgets/ExportCoordinatesDialog](ExportCoordinatesDialog.md) | qt-widgets | 5 |
| [qt-widgets/SaveFileDialog](SaveFileDialog.md) | qt-widgets | 2 |
| [qt-widgets/KinematicGraphsDialog](KinematicGraphsDialog.md) | qt-widgets | 1 |
| [qt-widgets/PythonConsoleDialog](PythonConsoleDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/FileDialogFilter.h
python scripts/gpq.py def GPlatesQtWidgets::FileDialogFilter --body
python scripts/gpq.py uses FileDialogFilter --kind class
python scripts/gpq.py hier FileDialogFilter
```
