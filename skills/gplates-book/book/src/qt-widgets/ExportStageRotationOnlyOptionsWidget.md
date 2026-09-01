# ExportStageRotationOnlyOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 274 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ExportStageRotationOnlyOptionsWidget.h` | C++ | 122 |
| `src/qt-widgets/ExportStageRotationOnlyOptionsWidgetUi.ui` | Qt form | 98 |

## Overview

Provides the user interface for configuring stage rotation-specific export options. Unlike other export option widgets, this does not inherit from `ExportOptionsWidget` and is not a standalone widget—it is designed to be embedded inside another export options widget as a sub-component.

The widget allows users to set the time interval between output stage rotations. It manages a single control: a spin box for the time interval value. When the user changes the interval, the widget updates the internal configuration object, which can be retrieved via `get_export_stage_rotation_options()`.

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

*None.*

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
