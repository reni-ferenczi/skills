# KinematicGraphsConfigurationWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 724 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/KinematicGraphsConfigurationWidget.h` | C++ | 183 |
| `src/qt-widgets/KinematicGraphsConfigurationWidget.cc` | C++ | 109 |
| `src/qt-widgets/KinematicGraphsConfigurationWidgetUi.ui` | Qt form | 150 |

## Overview

`KinematicGraphsConfigurationWidget` is the settings form for the kinematic (velocity/rotation) graphs feature: it exposes the finite-difference time step `delta_time`, the yellow/red velocity warning thresholds, and which of the three `VelocityMethod` finite-difference schemes (`T_TO_T_MINUS_DT`, `T_PLUS_DT_TO_T`, `T_PLUS_MINUS_HALF_DT`) to use when computing velocities from rotations. It is embedded both in `KinematicGraphsDialog`/`KinematicGraphsConfigurationDialog`, where the user tweaks graph parameters interactively, and in `PreferencesPaneKinematicGraphs`, where the same values are persisted as application preferences via `GPlatesGui::ConfigGuiUtils` — `build_velocity_method_description_map()` supplies the string labels that map `VelocityMethod` enum values to preference keys.

Each control change fires `configuration_changed(bool valid)` so an embedding dialog can enable or disable its Apply/OK button; `valid` becomes `false` only when the delta-time spinbox is exactly zero, in which case `handle_delta_time_changed()` also paints the spinbox with a red palette to flag the invalid state, restoring `d_spin_box_palette` once the value is non-zero again.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::KinematicGraphsConfigurationWidget`](#gplatesqtwidgetskinematicgraphsconfigurationwidget) | class | `QWidget`<br>`Ui_KinematicGraphsConfigurationWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::KinematicGraphsConfigurationWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `VelocityMethod` | enum | `None` | public | — |
| `KinematicGraphsConfigurationWidget(QWidget *parent = 0)` | constructor | `None` | public | — |
| `~KinematicGraphsConfigurationWidget()` | destructor | `None` | public | — |
| `delta_time_spinbox()` | method | `QDoubleSpinBox` | public | — |
| `velocity_yellow_spinbox()` | method | `QDoubleSpinBox` | public | — |
| `velocity_red_spinbox()` | method | `QDoubleSpinBox` | public | — |
| `velocity_method_button_group()` | method | `QButtonGroup` | public | — |
| `delta_time()` | method | `double` | public | — |
| `set_delta_time( double delta_time_)` | method | `void` | public | — |
| `yellow_velocity_threshold()` | method | `double` | public | — |
| `set_yellow_velocity_threshold( double yellow)` | method | `void` | public | — |
| `red_velocity_threshold()` | method | `double` | public | — |
| `set_red_velocity_threshold( double red)` | method | `void` | public | — |
| `velocity_method()` | method | `VelocityMethod` | public | — |
| `set_velocity_method( const VelocityMethod &method)` | method | `void` | public | — |
| `configuration_changed( bool valid)` | method | `void` | public | configuration\_changed - emitted when the dt spinbox has changed. |
| `handle_velocity_method_changed()` | method | `void` | private | — |
| `handle_delta_time_changed()` | method | `void` | private | — |
| `handle_velocity_yellow_changed()` | method | `void` | private | — |
| `handle_velocity_red_changed()` | method | `void` | private | — |
| `d_velocity_method` | field | `VelocityMethod` | private | — |
| `d_spin_box_palette` | field | `QPalette` | private | d\_spin\_box\_palette - the palette used in the delta\_time spinboxe. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_KINEMATICGRAPHSCONFIGURATIONWIDGET_H` | macro | `None` | — |

## Notes

The `VelocityMethod` enum values are also the ids used by `button_group_velocity_method` and are written directly to preferences, so their numeric order must not change independently of the stored configuration format.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/KinematicGraphsDialog](KinematicGraphsDialog.md) | qt-widgets | 12 |
| [qt-widgets/KinematicGraphsConfigurationDialog](KinematicGraphsConfigurationDialog.md) | qt-widgets | 11 |
| [qt-widgets/PreferencesPaneKinematicGraphs](PreferencesPaneKinematicGraphs.md) | qt-widgets | 7 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `KinematicGraphsConfigurationWidget` | `QWidget` | Form | 11 |

**Qt signal/slot connections** (6 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `radio_t_to_t_minus_dt` | `clicked()` | `this` | `handle_velocity_method_changed()` |
| `radio_t_plus_dt_to_t` | `clicked()` | `this` | `handle_velocity_method_changed()` |
| `radio_t_plus_dt_to_t_minus_dt` | `clicked()` | `this` | `handle_velocity_method_changed()` |
| `spinbox_dt` | `valueChanged(double)` | `this` | `handle_delta_time_changed()` |
| `spinbox_yellow` | `valueChanged(double)` | `this` | `handle_velocity_yellow_changed()` |
| `spinbox_red` | `valueChanged(double)` | `this` | `handle_velocity_red_changed()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/KinematicGraphsConfigurationWidget.h
python scripts/gpq.py def GPlatesQtWidgets::KinematicGraphsConfigurationWidget --body
python scripts/gpq.py uses KinematicGraphsConfigurationWidget --kind class
python scripts/gpq.py hier KinematicGraphsConfigurationWidget
```
