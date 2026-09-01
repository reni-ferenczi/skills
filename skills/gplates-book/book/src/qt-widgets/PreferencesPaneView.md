# PreferencesPaneView

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 0 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/PreferencesPaneView.h` | C++ | 79 |
| `src/qt-widgets/PreferencesPaneView.cc` | C++ | 61 |
| `src/qt-widgets/PreferencesPaneViewUi.ui` | Qt form | 215 |

## Overview

[[[PROSE overview unit=qt-widgets/PreferencesPaneView tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::PreferencesPaneView`](#gplatesqtwidgetspreferencespaneview) | class | `QWidget`<br>`Ui_PreferencesPaneView` | — | 0 | This preference pane provides the controls for various preference settings available in GPlates via GPlatesAppLogic::UserPreferences. |

## Members

### `GPlatesQtWidgets::PreferencesPaneView`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PreferencesPaneView( GPlatesAppLogic::ApplicationState &app_state, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~PreferencesPaneView()` | destructor | `None` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_PREFERENCESPANEVIEW_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/PreferencesPaneView tier=3]]]
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
| `PreferencesPaneView` | `QWidget` | Form | 13 |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/PreferencesPaneView.h
python scripts/gpq.py def GPlatesQtWidgets::PreferencesPaneView --body
python scripts/gpq.py uses PreferencesPaneView --kind class
python scripts/gpq.py hier PreferencesPaneView
```
