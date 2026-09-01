# ExportStageRotationOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 274 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ExportStageRotationOptionsWidget.h` | C++ | 129 |

## Overview

[[[PROSE overview unit=qt-widgets/ExportStageRotationOptionsWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ExportStageRotationOptionsWidget`](#gplatesqtwidgetsexportstagerotationoptionswidget) | class | [`ExportOptionsWidget`](ExportOptionsWidget.md) | — | 0 | ExportStageRotationOptionsWidget is used to show export options for exporting stage rotations (including equivalent and relative rotations). |

## Members

### `GPlatesQtWidgets::ExportStageRotationOptionsWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( QWidget *parent, GPlatesGui::ExportAnimationContext &export_animation_context, const GPlatesGui::ExportStageRotationAnimationStrategy::const_configuration_ptr & export_configuration)` | method | `ExportOptionsWidget` | public | Creates a ExportStageRotationOptionsWidget containing default export options. |
| `create_export_animation_strategy_configuration( const QString &filename_template)` | method | `GPlatesGui::ExportAnimationStrategy::const_configuration_base_ptr` | public | Collects the options specified by the user and returns them as an export animation strategy configuration. |
| `ExportStageRotationOptionsWidget( QWidget *parent_, const GPlatesGui::ExportStageRotationAnimationStrategy::const_configuration_ptr & export_configuration)` | constructor | `None` | private | — |
| `d_export_rotation_options_widget` | field | `ExportRotationOptionsWidget` | private | — |
| `d_export_stage_rotation_only_options_widget` | field | `ExportStageRotationOnlyOptionsWidget` | private | — |
| `d_export_configuration` | field | `GPlatesGui::ExportStageRotationAnimationStrategy::Configuration` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QT_WIDGETS_EXPORTSTAGEROTATIONOPTIONSWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ExportStageRotationOptionsWidget tier=3]]]
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
python scripts/gpq.py file src/qt-widgets/ExportStageRotationOptionsWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ExportStageRotationOptionsWidget --body
python scripts/gpq.py uses ExportStageRotationOptionsWidget --kind class
python scripts/gpq.py hier ExportStageRotationOptionsWidget
```
