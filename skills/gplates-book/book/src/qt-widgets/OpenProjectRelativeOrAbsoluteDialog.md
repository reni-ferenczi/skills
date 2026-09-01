# OpenProjectRelativeOrAbsoluteDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1167 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/OpenProjectRelativeOrAbsoluteDialog.h` | C++ | 94 |
| `src/qt-widgets/OpenProjectRelativeOrAbsoluteDialog.cc` | C++ | 122 |
| `src/qt-widgets/OpenProjectRelativeOrAbsoluteDialogUi.ui` | Qt form | 321 |

## Overview

A dialog presented when opening a project file that has moved since it was saved, where some referenced data files can be located via both the original absolute paths and new relative paths. This situation arises when projects are relocated to different directories but still contain data files accessible from the new location.

The dialog lists existing and missing files under both the original (absolute) and current (relative to new project location) file paths. The user can choose to load files from the original locations, from the current locations, or abort the open operation. This allows flexible project portability without requiring all data files to be relocated.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::OpenProjectRelativeOrAbsoluteDialog`](#gplatesqtwidgetsopenprojectrelativeorabsolutedialog) | class | `QDialog`<br>`Ui_OpenProjectRelativeOrAbsoluteDialog` | — | 0 | This dialog pops up if the user loads a project file that has moved since it was saved and where some of the data files (referenced by project) exist relative to both the new and the original project locations. |

## Members

### `GPlatesQtWidgets::OpenProjectRelativeOrAbsoluteDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Result` | enum | `None` | public | — |
| `OpenProjectRelativeOrAbsoluteDialog( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~OpenProjectRelativeOrAbsoluteDialog()` | destructor | `None` | public | — |
| `set_file_paths( QStringList existing_absolute_file_paths, QStringList missing_absolute_file_paths, QStringList existing_relative_file_paths, QStringList missing_relative_file_paths)` | method | `void` | public | Set the absolute and relative file paths to be displayed in the dialog. |
| `open_absolute()` | method | `void` | private | — |
| `open_relative()` | method | `void` | private | — |
| `abort_open()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_OPENPROJECTRELATIVEORABSOLUTEDIALOG_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 4 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `OpenProjectRelativeOrAbsoluteDialog` | `QDialog` | Project Has Moved | 20 |

**Qt signal/slot connections** (3 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_open_absolute` | `clicked()` | `this` | `open_absolute()` |
| `button_open_relative` | `clicked()` | `this` | `open_relative()` |
| `button_abort_open` | `clicked()` | `this` | `abort_open()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/OpenProjectRelativeOrAbsoluteDialog.h
python scripts/gpq.py def GPlatesQtWidgets::OpenProjectRelativeOrAbsoluteDialog --body
python scripts/gpq.py uses OpenProjectRelativeOrAbsoluteDialog --kind class
python scripts/gpq.py hier OpenProjectRelativeOrAbsoluteDialog
```
