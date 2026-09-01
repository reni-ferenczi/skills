# ExportRotationOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 428 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ExportRotationOptionsWidget.h` | C++ | 168 |
| `src/qt-widgets/ExportRotationOptionsWidgetUi.ui` | Qt form | 119 |

## Overview

[[[PROSE overview unit=qt-widgets/ExportRotationOptionsWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ExportRotationOptionsWidget`](#gplatesqtwidgetsexportrotationoptionswidget) | class | `QWidget`<br>`Ui_ExportRotationOptionsWidget` | — | 0 | ExportRotationOptionsWidget is used to allow the user to change rotations options common to both \*total\* and \*stage\* rotation exports. |

## Members

### `GPlatesQtWidgets::ExportRotationOptionsWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( QWidget *parent, const GPlatesGui::ExportOptionsUtils::ExportRotationOptions &default_export_rotation_options)` | method | `ExportRotationOptionsWidget` | public | Creates a ExportRotationOptionsWidget using default options. |
| `react_identity_radio_button_clicked()` | method | `void` | private | — |
| `react_euler_pole_format_radio_button_clicked()` | method | `void` | private | — |
| `ExportRotationOptionsWidget( QWidget *parent_, const GPlatesGui::ExportOptionsUtils::ExportRotationOptions &export_rotation_options_)` | constructor | `None` | private | — |
| `make_signal_slot_connections()` | method | `void` | private | — |
| `d_export_rotation_options` | field | `GPlatesGui::ExportOptionsUtils::ExportRotationOptions` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QT_WIDGETS_EXPORTROTATIONOPTIONSWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ExportRotationOptionsWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ExportStageRotationOptionsWidget](ExportStageRotationOptionsWidget.md) | qt-widgets | 3 |
| [qt-widgets/ExportTotalRotationOptionsWidget](ExportTotalRotationOptionsWidget.md) | qt-widgets | 3 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ExportRotationOptionsWidget` | `QWidget` | Form | 8 |

**Qt signal/slot connections** (4 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `radio_button_indeterminate` | `clicked(bool)` | `this` | `react_identity_radio_button_clicked()` |
| `radio_button_north_pole` | `clicked(bool)` | `this` | `react_identity_radio_button_clicked()` |
| `radio_button_lat_lon` | `clicked(bool)` | `this` | `react_euler_pole_format_radio_button_clicked()` |
| `radio_button_cartesian` | `clicked(bool)` | `this` | `react_euler_pole_format_radio_button_clicked()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ExportRotationOptionsWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ExportRotationOptionsWidget --body
python scripts/gpq.py uses ExportRotationOptionsWidget --kind class
python scripts/gpq.py hier ExportRotationOptionsWidget
```
