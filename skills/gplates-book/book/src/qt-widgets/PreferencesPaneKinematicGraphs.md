# PreferencesPaneKinematicGraphs

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1600 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/PreferencesPaneKinematicGraphs.h` | C++ | 80 |
| `src/qt-widgets/PreferencesPaneKinematicGraphs.cc` | C++ | 67 |
| `src/qt-widgets/PreferencesPaneKinematicGraphsUi.ui` | Qt form | 37 |

## Overview

A preference pane embedded in the main `PreferencesDialog` that provides controls for kinematic graph settings such as velocity calculations. The pane uses a `KinematicGraphsConfigurationWidget` to manage controls for delta time intervals, velocity warning thresholds (yellow and red levels), and velocity calculation methods.

Settings are linked to the user preferences system, allowing these defaults to persist across sessions.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::PreferencesPaneKinematicGraphs`](#gplatesqtwidgetspreferencespanekinematicgraphs) | class | `QWidget`<br>`Ui_PreferencesPaneKinematicGraphs` | — | 0 | This preference pane provides the controls for various preference settings available in GPlates via GPlatesAppLogic::UserPreferences. |

## Members

### `GPlatesQtWidgets::PreferencesPaneKinematicGraphs`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PreferencesPaneKinematicGraphs( GPlatesAppLogic::ApplicationState &app_state, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~PreferencesPaneKinematicGraphs()` | destructor | `None` | public | — |
| `d_configuration_widget` | field | `KinematicGraphsConfigurationWidget` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_PREFERENCESPANEKINEMATICGRAPHS_H` | macro | `None` | — |

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
| `PreferencesPaneKinematicGraphs` | `QWidget` | Form | 2 |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/PreferencesPaneKinematicGraphs.h
python scripts/gpq.py def GPlatesQtWidgets::PreferencesPaneKinematicGraphs --body
python scripts/gpq.py uses PreferencesPaneKinematicGraphs --kind class
python scripts/gpq.py hier PreferencesPaneKinematicGraphs
```
