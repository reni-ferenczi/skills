# OgrSrsWriteOptionDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1114 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/OgrSrsWriteOptionDialog.h` | C++ | 77 |
| `src/qt-widgets/OgrSrsWriteOptionDialog.cc` | C++ | 82 |
| `src/qt-widgets/OgrSrsWriteOptionDialogUi.ui` | Qt form | 105 |

## Overview

A dialog that prompts the user when exporting vector data with an OGR format after converting from a non-WGS84 spatial reference system. When data is imported from a file with a non-WGS84 SRS, GPlates converts it to WGS84 for internal processing. This dialog appears at export time to let the user choose how to represent the SRS in the output file.

The user can select one of three behaviors: write to WGS84 SRS (the default), write back to the original SRS, or omit the SRS entirely. The dialog displays the original spatial reference system in WKT format and the filename being exported.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::OgrSrsWriteOptionDialog`](#gplatesqtwidgetsogrsrswriteoptiondialog) | class | `QDialog`<br>`Ui_OgrSrsWriteOptionDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::OgrSrsWriteOptionDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `BehaviourRequested` | enum | `None` | public | — |
| `OgrSrsWriteOptionDialog( QWidget *parent = NULL)` | constructor | `None` | public | — |
| `initialise( const QString &filename, const GPlatesPropertyValues::SpatialReferenceSystem::non_null_ptr_to_const_type &srs)` | method | `void` | public | — |
| `set_up_connections()` | method | `void` | private | — |
| `handle_ok()` | method | `void` | private | — |
| `handle_cancel()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_OGRSRSWRITEOPTIONDIALOG_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 6 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `OgrSrsWriteOptionDialog` | `QDialog` | Choose output SRS | 9 |

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_ok` | `clicked()` | `this` | `handle_ok()` |
| `button_cancel` | `clicked()` | `this` | `handle_cancel()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/OgrSrsWriteOptionDialog.h
python scripts/gpq.py def GPlatesQtWidgets::OgrSrsWriteOptionDialog --body
python scripts/gpq.py uses OgrSrsWriteOptionDialog --kind class
python scripts/gpq.py hier OgrSrsWriteOptionDialog
```
