# PreferencesPaneNetwork

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 0 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/PreferencesPaneNetwork.h` | C++ | 79 |
| `src/qt-widgets/PreferencesPaneNetwork.cc` | C++ | 59 |
| `src/qt-widgets/PreferencesPaneNetworkUi.ui` | Qt form | 187 |

## Overview

[[[PROSE overview unit=qt-widgets/PreferencesPaneNetwork tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=qt-widgets/PreferencesPaneNetwork tier=3]]]
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
