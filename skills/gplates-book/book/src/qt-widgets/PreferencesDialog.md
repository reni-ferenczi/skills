# PreferencesDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1168 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/PreferencesDialog.h` | C++ | 124 |
| `src/qt-widgets/PreferencesDialog.cc` | C++ | 101 |
| `src/qt-widgets/PreferencesDialogUi.ui` | Qt form | 180 |

## Overview

[[[PROSE overview unit=qt-widgets/PreferencesDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ConfigTableView`](#gplatesqtwidgetsconfigtableview) | class | `QTableView` | — | 0 | — |
| [`GPlatesQtWidgets::PreferencesDialog`](#gplatesqtwidgetspreferencesdialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_PreferencesDialog` | — | 0 | This dialog provides users with controls for various preference settings available in GPlates via GPlatesAppLogic::UserPreferences. |

## Members

### `GPlatesQtWidgets::ConfigTableView`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ConfigTableView( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `commit_current_editor_data()` | method | `void` | public | — |

### `GPlatesQtWidgets::PreferencesDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PreferencesDialog( GPlatesAppLogic::ApplicationState &app_state, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~PreferencesDialog()` | destructor | `None` | public | — |
| `reject()` | method | `void` | public | — |
| `add_pane( int index, const QString &category_label, QWidget *pane_widget, bool scrolling)` | method | `void` | private | — |
| `d_cfg_table` | field | `ConfigTableView` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_PREFERENCESDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/PreferencesDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ConfigGuiUtils](../gui/ConfigGuiUtils.md) | gui | 1 |
| [gui/Dialogs](../gui/Dialogs.md) | gui | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `PreferencesDialog` | `QDialog` | Preferences | 9 |

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `list_categories` | `currentRowChanged(int)` | `stack_settings_ui` | `setCurrentIndex(int)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/PreferencesDialog.h
python scripts/gpq.py def GPlatesQtWidgets::PreferencesDialog --body
python scripts/gpq.py uses PreferencesDialog --kind class
python scripts/gpq.py hier PreferencesDialog
```
