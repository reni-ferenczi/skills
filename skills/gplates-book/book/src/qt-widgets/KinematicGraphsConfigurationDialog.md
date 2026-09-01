# KinematicGraphsConfigurationDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1502 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/KinematicGraphsConfigurationDialog.h` | C++ | 78 |
| `src/qt-widgets/KinematicGraphsConfigurationDialog.cc` | C++ | 75 |
| `src/qt-widgets/KinematicGraphsConfigurationDialogUi.ui` | Qt form | 51 |

## Overview

[[[PROSE overview unit=qt-widgets/KinematicGraphsConfigurationDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=qt-widgets/KinematicGraphsConfigurationDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
