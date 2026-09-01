# ExportMotionPathOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1163 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ExportMotionPathOptionsWidget.h` | C++ | 131 |

## Overview

A widget for collecting export options when exporting motion paths. It optionally includes a `DatelineWrapOptionsWidget` (controlled by the `configure_dateline_wrapping` parameter) and always delegates to `ExportFileOptionsWidget` for file-related settings. The collected options are applied to an `ExportMotionPathAnimationStrategy::Configuration` object.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ExportMotionPathOptionsWidget`](#gplatesqtwidgetsexportmotionpathoptionswidget) | class | [`ExportOptionsWidget`](ExportOptionsWidget.md) | — | 0 | ExportMotionPathOptionsWidget is used to show export options for exporting motion paths. |

## Members

### `GPlatesQtWidgets::ExportMotionPathOptionsWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( QWidget *parent, GPlatesGui::ExportAnimationContext &export_animation_context, const GPlatesGui::ExportMotionPathAnimationStrategy::const_configuration_ptr & export_configuration, bool configure_dateline_wrapping)` | method | `ExportOptionsWidget` | public | Creates a ExportMotionPathOptionsWidget containing default export options. |
| `create_export_animation_strategy_configuration( const QString &filename_template)` | method | `GPlatesGui::ExportAnimationStrategy::const_configuration_base_ptr` | public | Collects the options specified by the user and returns them as an export animation strategy configuration. |
| `ExportMotionPathOptionsWidget( QWidget *parent_, const GPlatesGui::ExportMotionPathAnimationStrategy::const_configuration_ptr & export_configuration, bool configure_dateline_wrapping)` | constructor | `None` | private | — |
| `d_dateline_wrap_options_widget` | field | `DatelineWrapOptionsWidget` | private | — |
| `d_export_file_options_widget` | field | `ExportFileOptionsWidget` | private | — |
| `d_export_configuration` | field | `GPlatesGui::ExportMotionPathAnimationStrategy::Configuration` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QT_WIDGETS_EXPORTMOTIONPATHOPTIONSWIDGET_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportAnimationRegistry](../gui/ExportAnimationRegistry.md) | gui | 5 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ExportMotionPathOptionsWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ExportMotionPathOptionsWidget --body
python scripts/gpq.py uses ExportMotionPathOptionsWidget --kind class
python scripts/gpq.py hier ExportMotionPathOptionsWidget
```
