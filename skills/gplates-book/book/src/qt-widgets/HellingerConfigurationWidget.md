# HellingerConfigurationWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1061 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/HellingerConfigurationWidget.h` | C++ | 171 |
| `src/qt-widgets/HellingerConfigurationWidget.cc` | C++ | 178 |
| `src/qt-widgets/HellingerConfigurationWidgetUi.ui` | Qt form | 148 |

## Overview

[[[PROSE overview unit=qt-widgets/HellingerConfigurationWidget tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::HellingerConfigurationWidget`](#gplatesqtwidgetshellingerconfigurationwidget) | class | `QWidget`<br>`Ui_HellingerConfigurationWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::HellingerConfigurationWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `HellingerColour` | enum | `None` | public | — |
| `get_colour_from_hellinger_colour( const HellingerColour &hellinger_colour)` | method | `GPlatesGui::Colour` | public | — |
| `colour_description_map_type` | typedef | `QMap<HellingerColour,QString>` | public | — |
| `HellingerConfigurationWidget(QWidget *parent = 0)` | constructor | `None` | public | — |
| `~HellingerConfigurationWidget()` | destructor | `None` | public | — |
| `best_fit_pole_colour()` | method | `HellingerColour` | public | — |
| `ellipse_colour()` | method | `HellingerColour` | public | — |
| `ellipse_line_thickness()` | method | `int` | public | — |
| `initial_estimate_pole_colour()` | method | `HellingerColour` | public | — |
| `pole_arrow_height()` | method | `float` | public | — |
| `pole_arrow_radius()` | method | `float` | public | — |
| `set_ellipse_line_thickness(int thickness)` | method | `void` | public | — |
| `set_best_fit_pole_colour( HellingerColour &colour)` | method | `void` | public | — |
| `set_ellipse_colour( HellingerColour &colour)` | method | `void` | public | — |
| `set_initial_estimate_pole_colour( HellingerColour &colour)` | method | `void` | public | — |
| `set_pole_arrow_height( const float &height)` | method | `void` | public | — |
| `set_pole_arrow_radius( const float &radius)` | method | `void` | public | — |
| `configuration_changed( bool valid)` | method | `void` | public | configuration\_changed This lets parent dialogs react accordingly e.g. enabling/disabling the Apply button. |
| `initialise_widget()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `HELLINGERCONFIGURATIONWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/HellingerConfigurationWidget tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/HellingerDialog](HellingerDialog.md) | qt-widgets | 47 |
| [qt-widgets/HellingerConfigurationDialog](HellingerConfigurationDialog.md) | qt-widgets | 15 |
| [gui/deprecated/GLCanvas](../gui/deprecated/GLCanvas.md) | gui | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `HellingerConfigurationWidget` | `QWidget` | Form | 13 |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/HellingerConfigurationWidget.h
python scripts/gpq.py def GPlatesQtWidgets::HellingerConfigurationWidget --body
python scripts/gpq.py uses HellingerConfigurationWidget --kind class
python scripts/gpq.py hier HellingerConfigurationWidget
```
