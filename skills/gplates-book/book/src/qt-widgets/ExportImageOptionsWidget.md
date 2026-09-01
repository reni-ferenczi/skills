# ExportImageOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 347 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ExportImageOptionsWidget.h` | C++ | 87 |
| `src/qt-widgets/ExportImageOptionsWidget.cc` | C++ | 68 |

## Overview

A widget that collects and manages export options when the user exports a static image of the globe or map view. It inherits from `ExportOptionsWidget` and delegates to `ExportImageResolutionOptionsWidget` to handle resolution and image format details. The configuration is applied to an `ExportImageAnimationStrategy::Configuration` object that drives the actual export.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ExportImageOptionsWidget`](#gplatesqtwidgetsexportimageoptionswidget) | class | [`ExportOptionsWidget`](ExportOptionsWidget.md) | — | 0 | ExportImageOptionsWidget is used to show export options for exporting screen shots of the globe/map view. |

## Members

### `GPlatesQtWidgets::ExportImageOptionsWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( QWidget *parent, GPlatesGui::ExportAnimationContext &export_animation_context, const GPlatesGui::ExportImageAnimationStrategy::const_configuration_ptr &export_configuration)` | method | `ExportOptionsWidget` | public | Creates a ExportImageOptionsWidget containing default export options. |
| `create_export_animation_strategy_configuration( const QString &filename_template)` | method | `GPlatesGui::ExportAnimationStrategy::const_configuration_base_ptr` | public | Collects the options specified by the user and returns them as an export animation strategy configuration. |
| `d_export_image_resolution_options_widget` | field | `ExportImageResolutionOptionsWidget` | private | — |
| `d_export_configuration` | field | `GPlatesGui::ExportImageAnimationStrategy::Configuration` | private | — |
| `ExportImageOptionsWidget( QWidget *parent_, GPlatesGui::ExportAnimationContext &export_animation_context, const GPlatesGui::ExportImageAnimationStrategy::const_configuration_ptr &export_configuration)` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QT_WIDGETS_EXPORTIMAGEOPTIONSWIDGET_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportAnimationRegistry](../gui/ExportAnimationRegistry.md) | gui | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ExportImageOptionsWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ExportImageOptionsWidget --body
python scripts/gpq.py uses ExportImageOptionsWidget --kind class
python scripts/gpq.py hier ExportImageOptionsWidget
```
