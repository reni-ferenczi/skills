# PreferencesPanePython

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 0 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/PreferencesPanePython.h` | C++ | 79 |
| `src/qt-widgets/PreferencesPanePython.cc` | C++ | 84 |
| `src/qt-widgets/PreferencesPanePythonUi.ui` | Qt form | 292 |

## Overview

[[[PROSE overview unit=qt-widgets/PreferencesPanePython tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=qt-widgets/PreferencesPanePython tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
