# ExportStageRotationOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 274 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ExportStageRotationOptionsWidget.h` | C++ | 129 |

## Overview

Provides the user interface for configuring export options when exporting stage rotations, including equivalent and relative rotation variants. The widget inherits from `ExportOptionsWidget` and acts as a container that combines two sub-widgets: `ExportRotationOptionsWidget` for general rotation export options and `ExportStageRotationOnlyOptionsWidget` for stage-rotation-specific settings.

The widget delegates to its sub-components to collect rotation options and stage rotation options separately, then merges them back into a unified configuration object when the user is ready to export.

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

*None.*

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
