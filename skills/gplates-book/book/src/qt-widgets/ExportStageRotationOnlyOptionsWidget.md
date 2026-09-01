# ExportStageRotationOnlyOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 274 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ExportStageRotationOnlyOptionsWidget.h` | C++ | 122 |
| `src/qt-widgets/ExportStageRotationOnlyOptionsWidgetUi.ui` | Qt form | 98 |

## Overview

[[[PROSE overview unit=qt-widgets/ExportStageRotationOnlyOptionsWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ExportStageRotationOnlyOptionsWidget`](#gplatesqtwidgetsexportstagerotationonlyoptionswidget) | class | `QWidget`<br>`Ui_ExportStageRotationOnlyOptionsWidget` | — | 0 | ExportStageRotationOnlyOptionsWidget is used to allow the user to change rotations options that \*only\* appy to \*stage\* rotation exports (not \*total\* rotation exports). |

## Members

### `GPlatesQtWidgets::ExportStageRotationOnlyOptionsWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( QWidget *parent, const GPlatesGui::ExportOptionsUtils::ExportStageRotationOptions &default_export_stage_rotation_options_)` | method | `ExportStageRotationOnlyOptionsWidget` | public | Creates a ExportStageRotationOnlyOptionsWidget using default options. |
| `react_time_interval_value_changed( double time_interval)` | method | `void` | private | — |
| `ExportStageRotationOnlyOptionsWidget( QWidget *parent_, const GPlatesGui::ExportOptionsUtils::ExportStageRotationOptions &export_stage_rotation_options_)` | constructor | `None` | private | — |
| `make_signal_slot_connections()` | method | `void` | private | — |
| `d_export_stage_rotation_options` | field | `GPlatesGui::ExportOptionsUtils::ExportStageRotationOptions` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QT_WIDGETS_EXPORTSTAGEROTATIONONLYOPTIONSWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ExportStageRotationOnlyOptionsWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ExportStageRotationOptionsWidget](ExportStageRotationOptionsWidget.md) | qt-widgets | 3 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ExportStageRotationOnlyOptionsWidget` | `QWidget` | Form | 5 |

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `double_spin_box_time_interval` | `valueChanged(double)` | `this` | `react_time_interval_value_changed(double)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ExportStageRotationOnlyOptionsWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ExportStageRotationOnlyOptionsWidget --body
python scripts/gpq.py uses ExportStageRotationOnlyOptionsWidget --kind class
python scripts/gpq.py hier ExportStageRotationOnlyOptionsWidget
```
