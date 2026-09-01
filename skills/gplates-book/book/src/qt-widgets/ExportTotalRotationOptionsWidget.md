# ExportTotalRotationOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 428 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ExportTotalRotationOptionsWidget.h` | C++ | 115 |

## Overview

[[[PROSE overview unit=qt-widgets/ExportTotalRotationOptionsWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ExportTotalRotationOptionsWidget`](#gplatesqtwidgetsexporttotalrotationoptionswidget) | class | [`ExportOptionsWidget`](ExportOptionsWidget.md) | — | 0 | ExportTotalRotationOptionsWidget is used to show export options for exporting total rotations (including equivalent and relative rotations). |

## Members

### `GPlatesQtWidgets::ExportTotalRotationOptionsWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( QWidget *parent, GPlatesGui::ExportAnimationContext &export_animation_context, const GPlatesGui::ExportTotalRotationAnimationStrategy::const_configuration_ptr & export_configuration)` | method | `ExportOptionsWidget` | public | Creates a ExportTotalRotationOptionsWidget containing default export options. |
| `create_export_animation_strategy_configuration( const QString &filename_template)` | method | `GPlatesGui::ExportAnimationStrategy::const_configuration_base_ptr` | public | Collects the options specified by the user and returns them as an export animation strategy configuration. |
| `ExportTotalRotationOptionsWidget( QWidget *parent_, const GPlatesGui::ExportTotalRotationAnimationStrategy::const_configuration_ptr & export_configuration)` | constructor | `None` | private | — |
| `d_export_rotation_options_widget` | field | `ExportRotationOptionsWidget` | private | — |
| `d_export_configuration` | field | `GPlatesGui::ExportTotalRotationAnimationStrategy::Configuration` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QT_WIDGETS_EXPORTTOTALROTATIONOPTIONSWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ExportTotalRotationOptionsWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportAnimationRegistry](../gui/ExportAnimationRegistry.md) | gui | 7 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ExportTotalRotationOptionsWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ExportTotalRotationOptionsWidget --body
python scripts/gpq.py uses ExportTotalRotationOptionsWidget --kind class
python scripts/gpq.py hier ExportTotalRotationOptionsWidget
```
