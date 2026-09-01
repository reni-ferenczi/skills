# ExportSvgOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 347 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ExportSvgOptionsWidget.h` | C++ | 87 |
| `src/qt-widgets/ExportSvgOptionsWidget.cc` | C++ | 68 |

## Overview

Provides the user interface for configuring export options when exporting the globe or map view to SVG format. The widget inherits from `ExportOptionsWidget` and delegates to `ExportImageResolutionOptionsWidget` to handle image resolution settings.

The widget manages a configuration object for SVG export and collects image resolution options from its embedded sub-widget when the user initiates the export.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ExportSvgOptionsWidget`](#gplatesqtwidgetsexportsvgoptionswidget) | class | [`ExportOptionsWidget`](ExportOptionsWidget.md) | — | 0 | ExportSvgOptionsWidget is used to show export options for exporting the globe/map view to SVG. |

## Members

### `GPlatesQtWidgets::ExportSvgOptionsWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( QWidget *parent, GPlatesGui::ExportAnimationContext &export_animation_context, const GPlatesGui::ExportSvgAnimationStrategy::const_configuration_ptr &export_configuration)` | method | `ExportOptionsWidget` | public | Creates a ExportSvgOptionsWidget containing default export options. |
| `create_export_animation_strategy_configuration( const QString &filename_template)` | method | `GPlatesGui::ExportAnimationStrategy::const_configuration_base_ptr` | public | Collects the options specified by the user and returns them as an export animation strategy configuration. |
| `d_export_image_resolution_options_widget` | field | `ExportImageResolutionOptionsWidget` | private | — |
| `d_export_configuration` | field | `GPlatesGui::ExportSvgAnimationStrategy::Configuration` | private | — |
| `ExportSvgOptionsWidget( QWidget *parent_, GPlatesGui::ExportAnimationContext &export_animation_context, const GPlatesGui::ExportSvgAnimationStrategy::const_configuration_ptr &export_configuration)` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QT_WIDGETS_EXPORTSVGOPTIONSWIDGET_H` | macro | `None` | — |

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
python scripts/gpq.py file src/qt-widgets/ExportSvgOptionsWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ExportSvgOptionsWidget --body
python scripts/gpq.py uses ExportSvgOptionsWidget --kind class
python scripts/gpq.py hier ExportSvgOptionsWidget
```
