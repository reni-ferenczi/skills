# PreferencesPanePython

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 0 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/PreferencesPanePython.h` | C++ | 79 |
| `src/qt-widgets/PreferencesPanePython.cc` | C++ | 84 |
| `src/qt-widgets/PreferencesPanePythonUi.ui` | Qt form | 292 |

## Overview

A preference pane for Python configuration, embedded in the `PreferencesDialog`. It presents controls for settings managed by `GPlatesAppLogic::UserPreferences`: the Python home directory, Python system and user script directories, and an option to show the Python initialization failure dialog. The constructor uses `GPlatesGui::ConfigGuiUtils::link_widget_to_preference` to synchronise widgets with preference keys, and a local helper `link_dir_chooser_button` creates directory chooser dialogs that update line edits and signal completion to trigger preference updates. Like other preference panes, it handles only UI presentation; actual Python initialization and configuration is managed elsewhere.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::PreferencesPanePython`](#gplatesqtwidgetspreferencespanepython) | class | `QWidget`<br>`Ui_PreferencesPanePython` | — | 0 | This preference pane provides the controls for various preference settings available in GPlates via GPlatesAppLogic::UserPreferences. |

## Members

### `GPlatesQtWidgets::PreferencesPanePython`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PreferencesPanePython( GPlatesAppLogic::ApplicationState &app_state, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~PreferencesPanePython()` | destructor | `None` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `link_dir_chooser_button( QAbstractButton *button, QLineEdit *lineedit)` | function | `void` | Could probably be moved to QtUtils code. |
| `GPLATES_QTWIDGETS_PREFERENCESPYTHONPANE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/PreferencesDialog](PreferencesDialog.md) | qt-widgets | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `PreferencesPanePython` | `QWidget` | Form | 17 |

**Qt signal/slot connections** (3 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button` | `clicked()` | `chooser` | `exec()` |
| `chooser` | `fileSelected(QString)` | `lineedit` | `setText(QString)` |
| `chooser` | `fileSelected(QString)` | — | `None` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/PreferencesPanePython.h
python scripts/gpq.py def GPlatesQtWidgets::PreferencesPanePython --body
python scripts/gpq.py uses PreferencesPanePython --kind class
python scripts/gpq.py hier PreferencesPanePython
```
