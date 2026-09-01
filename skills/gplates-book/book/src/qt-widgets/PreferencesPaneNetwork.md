# PreferencesPaneNetwork

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 0 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/PreferencesPaneNetwork.h` | C++ | 79 |
| `src/qt-widgets/PreferencesPaneNetwork.cc` | C++ | 59 |
| `src/qt-widgets/PreferencesPaneNetworkUi.ui` | Qt form | 187 |

## Overview

A preference pane for network configuration, embedded in the `PreferencesDialog`. It presents controls for settings managed by `GPlatesAppLogic::UserPreferences`: proxy URL and enabled status, server port, and local listening mode. Widget configuration is generated from a Qt Designer form; the constructor uses `GPlatesGui::ConfigGuiUtils::link_widget_to_preference` to synchronise each control with its corresponding preference key. The pane has no network logic of its own — it only presents a user-friendly layout. Listeners in other classes respond to preference changes as needed.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::PreferencesPaneNetwork`](#gplatesqtwidgetspreferencespanenetwork) | class | `QWidget`<br>`Ui_PreferencesPaneNetwork` | — | 0 | This preference pane provides the controls for various preference settings available in GPlates via GPlatesAppLogic::UserPreferences. |

## Members

### `GPlatesQtWidgets::PreferencesPaneNetwork`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PreferencesPaneNetwork( GPlatesAppLogic::ApplicationState &app_state, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~PreferencesPaneNetwork()` | destructor | `None` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_PREFERENCESPANENETWORK_H` | macro | `None` | — |

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
| `PreferencesPaneNetwork` | `QWidget` | Form | 13 |

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `checkbox_use_proxy` | `toggled(bool)` | `lineedit_proxy_url` | `setEnabled(bool)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/PreferencesPaneNetwork.h
python scripts/gpq.py def GPlatesQtWidgets::PreferencesPaneNetwork --body
python scripts/gpq.py uses PreferencesPaneNetwork --kind class
python scripts/gpq.py hier PreferencesPaneNetwork
```
