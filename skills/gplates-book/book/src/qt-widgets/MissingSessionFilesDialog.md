# MissingSessionFilesDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1166 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/MissingSessionFilesDialog.h` | C++ | 127 |
| `src/qt-widgets/MissingSessionFilesDialog.cc` | C++ | 195 |
| `src/qt-widgets/MissingSessionFilesDialogUi.ui` | Qt form | 115 |

## Overview

[[[PROSE overview unit=qt-widgets/MissingSessionFilesDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::MissingSessionFilesDialog`](#gplatesqtwidgetsmissingsessionfilesdialog) | class | `QDialog`<br>`Ui_MissingSessionFilesDialog` | — | 0 | This dialog pops up if the user loads a project/session that has missing files and asks them to optionally locate the files before loading the project/session. |

## Members

### `GPlatesQtWidgets::MissingSessionFilesDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ActionRequested` | enum | `None` | public | — |
| `MissingSessionFilesDialog( GPlatesPresentation::ViewState &view_state_, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `populate( ActionRequested action_requested, QStringList missing_file_paths)` | method | `void` | public | Set the missing file paths to be displayed in the dialog. |
| `get_file_path_remapping()` | method | `boost::optional< QMap<QString/*missing*/, QString/*existing*/> >` | public | Returns those missing files that were remapped to existing files (if any were remapped). |
| `load()` | method | `void` | private | — |
| `abort_load()` | method | `void` | private | — |
| `update( int row)` | method | `void` | private | — |
| `ColumnNames` | struct | `None` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_signal_mapper` | field | `QSignalMapper` | private | — |
| `d_missing_file_paths` | field | `QStringList` | private | The original missing file paths. |
| `d_file_path_remapping` | field | `QMap<QString, QString>` | private | Map of missing file paths to updated file paths of any remapped file paths. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_MISSINGSESSIONFILESDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/MissingSessionFilesDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 7 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `MissingSessionFilesDialog` | `QDialog` | — | 4 |

**Qt signal/slot connections** (4 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `buttonbox->button(QDialogButtonBox::Ok)` | `clicked()` | `this` | `load()` |
| `buttonbox->button(QDialogButtonBox::Abort)` | `clicked()` | `this` | `abort_load()` |
| `d_signal_mapper` | `mapped(int)` | `this` | `update(int)` |
| `update_item` | `clicked()` | `d_signal_mapper` | `map()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/MissingSessionFilesDialog.h
python scripts/gpq.py def GPlatesQtWidgets::MissingSessionFilesDialog --body
python scripts/gpq.py uses MissingSessionFilesDialog --kind class
python scripts/gpq.py hier MissingSessionFilesDialog
```
