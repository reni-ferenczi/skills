# HellingerConfigurationDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 761 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/HellingerConfigurationDialog.h` | C++ | 94 |
| `src/qt-widgets/HellingerConfigurationDialog.cc` | C++ | 157 |
| `src/qt-widgets/HellingerConfigurationDialogUi.ui` | Qt form | 51 |

## Overview

Settings dialog for the Hellinger plate motion estimation tool, hosted within `HellingerDialog`. It lets users customize the visual appearance of Hellinger results on the globe: colors and thickness for the estimated and best-fit poles and confidence ellipses, and the size of the pole arrow markers used to visualize pole positions.

The dialog delegates its UI to `HellingerConfigurationWidget` and manages a reference to the parent dialog's `Configuration` structure. On apply, it copies the widget's settings to the configuration object and persists them to `UserPreferences` so they survive between sessions. It validates changes via the configuration widget's `configuration_changed()` signal, enabling the apply button only when the current settings are valid.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::HellingerConfigurationDialog`](#gplatesqtwidgetshellingerconfigurationdialog) | class | `QDialog`<br>`Ui_HellingerConfigurationDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::HellingerConfigurationDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `HellingerConfigurationDialog( HellingerDialog::Configuration &configuration, GPlatesAppLogic::ApplicationState &app_state, QWidget *parent = 0)` | constructor | `None` | public | — |
| `~HellingerConfigurationDialog()` | destructor | `None` | public | — |
| `read_values_from_settings()` | method | `void` | public | — |
| `handle_apply()` | method | `void` | private | — |
| `handle_configuration_changed( bool valid)` | method | `void` | private | handle\_configuration\_changed Responds to signal emitted by the child widget. |
| `configuration_changed()` | method | `void` | public | — |
| `write_values_to_settings()` | method | `void` | private | — |
| `initialise_widget()` | method | `void` | private | — |
| `d_configuration_widget` | field | `HellingerConfigurationWidget` | private | — |
| `d_configuration_ref` | field | `HellingerDialog::Configuration` | private | — |
| `d_app_state_ref` | field | `GPlatesAppLogic::ApplicationState` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `HELLINGERCONFIGURATIONDIALOG_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/HellingerDialog](HellingerDialog.md) | qt-widgets | 10 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `HellingerConfigurationDialog` | `QDialog` | Hellinger Settings | 4 |

**Qt signal/slot connections** (3 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_close` | `clicked()` | `this` | `close()` |
| `button_apply` | `clicked()` | `this` | `handle_apply()` |
| `d_configuration_widget` | `configuration_changed(bool)` | `this` | `handle_configuration_changed(bool)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/HellingerConfigurationDialog.h
python scripts/gpq.py def GPlatesQtWidgets::HellingerConfigurationDialog --body
python scripts/gpq.py uses HellingerConfigurationDialog --kind class
python scripts/gpq.py hier HellingerConfigurationDialog
```
