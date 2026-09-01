# KinematicGraphsConfigurationDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1502 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/KinematicGraphsConfigurationDialog.h` | C++ | 78 |
| `src/qt-widgets/KinematicGraphsConfigurationDialog.cc` | C++ | 75 |
| `src/qt-widgets/KinematicGraphsConfigurationDialogUi.ui` | Qt form | 51 |

## Overview

A dialog for configuring kinematic graph calculation parameters. It wraps a `KinematicGraphsConfigurationWidget` in a modal dialog with Apply and Close buttons. The dialog maintains a reference to a `KinematicGraphsDialog::Configuration` object and synchronizes widget state with configuration settings.

When the user clicks Apply, `handle_apply()` copies the current settings (delta time, velocity thresholds, and velocity method) from the widget to the configuration. The `handle_configuration_changed()` slot enables or disables the Apply button based on whether the current widget state represents a valid configuration.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::KinematicGraphsConfigurationDialog`](#gplatesqtwidgetskinematicgraphsconfigurationdialog) | class | `QDialog`<br>`Ui_KinematicGraphsConfigurationDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::KinematicGraphsConfigurationDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `KinematicGraphsConfigurationDialog( KinematicGraphsDialog::Configuration &configuration, QWidget *parent = 0)` | constructor | `None` | public | — |
| `~KinematicGraphsConfigurationDialog()` | destructor | `None` | public | — |
| `handle_apply()` | method | `void` | private | — |
| `handle_configuration_changed( bool valid)` | method | `void` | private | handle\_configuration\_changed Responds to signal emitted by the child widget. |
| `initialise_widget()` | method | `void` | private | — |
| `d_configuration_widget` | field | `KinematicGraphsConfigurationWidget` | private | — |
| `d_configuration_ref` | field | `KinematicGraphsDialog::Configuration` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_KINEMATICGRAPHSCONFIGURATIONDIALOG_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/KinematicGraphsDialog](KinematicGraphsDialog.md) | qt-widgets | 7 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `KinematicGraphsConfigurationDialog` | `QDialog` | Configure Velocity Calculations | 4 |

**Qt signal/slot connections** (3 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_close` | `clicked()` | `this` | `close()` |
| `button_apply` | `clicked()` | `this` | `handle_apply()` |
| `d_configuration_widget` | `configuration_changed(bool)` | `this` | `handle_configuration_changed(bool)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/KinematicGraphsConfigurationDialog.h
python scripts/gpq.py def GPlatesQtWidgets::KinematicGraphsConfigurationDialog --body
python scripts/gpq.py uses KinematicGraphsConfigurationDialog --kind class
python scripts/gpq.py hier KinematicGraphsConfigurationDialog
```
