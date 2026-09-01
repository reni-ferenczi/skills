# PreferencesPaneFiles

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 0 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/PreferencesPaneFiles.h` | C++ | 102 |
| `src/qt-widgets/PreferencesPaneFiles.cc` | C++ | 149 |
| `src/qt-widgets/PreferencesPaneFilesUi.ui` | Qt form | 589 |

## Overview

[[[PROSE overview unit=qt-widgets/PreferencesPaneFiles tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::PreferencesPaneFiles`](#gplatesqtwidgetspreferencespanefiles) | class | `QWidget`<br>`Ui_PreferencesPaneFiles` | — | 0 | This preference pane provides the controls for various preference settings available in GPlates via GPlatesAppLogic::UserPreferences. |

## Members

### `GPlatesQtWidgets::PreferencesPaneFiles`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FileBehaviour` | enum | `None` | public | — |
| `PreferencesPaneFiles( GPlatesAppLogic::ApplicationState &app_state, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~PreferencesPaneFiles()` | destructor | `None` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `link_dir_chooser_button( QAbstractButton *button, QLineEdit *lineedit)` | function | `void` | Could probably be moved to QtUtils code. |
| `GPLATES_QTWIDGETS_PREFERENCESPANEFILES_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/PreferencesPaneFiles tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/FileIODirectoryConfigurations](../gui/FileIODirectoryConfigurations.md) | gui | 13 |
| [qt-widgets/PreferencesDialog](PreferencesDialog.md) | qt-widgets | 2 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 1 |
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 1 |
| [qt-widgets/SaveFileDialog](SaveFileDialog.md) | qt-widgets | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `PreferencesPaneFiles` | `QWidget` | Form | 38 |

**Qt signal/slot connections** (3 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button` | `clicked()` | `chooser` | `exec()` |
| `chooser` | `fileSelected(QString)` | `lineedit` | `setText(QString)` |
| `chooser` | `fileSelected(QString)` | — | `None` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/PreferencesPaneFiles.h
python scripts/gpq.py def GPlatesQtWidgets::PreferencesPaneFiles --body
python scripts/gpq.py uses PreferencesPaneFiles --kind class
python scripts/gpq.py hier PreferencesPaneFiles
```
