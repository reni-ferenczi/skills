# PreferencesPaneView

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 0 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/PreferencesPaneView.h` | C++ | 79 |
| `src/qt-widgets/PreferencesPaneView.cc` | C++ | 61 |
| `src/qt-widgets/PreferencesPaneViewUi.ui` | Qt form | 215 |

## Overview

A preference pane for view configuration, embedded in the `PreferencesDialog`. It presents controls for animation and visibility settings managed by `GPlatesAppLogic::UserPreferences`: default time range (start, end, and increment for animations), and toggles for showing stars and topological sections. The constructor uses `GPlatesGui::ConfigGuiUtils::link_widget_to_preference` to synchronise each control with its corresponding preference key. Like other preference panes, it handles only UI presentation; view-related logic that responds to these preferences runs elsewhere in the application.

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

*None.*

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
