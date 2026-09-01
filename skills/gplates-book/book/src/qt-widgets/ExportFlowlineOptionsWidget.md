# ExportFlowlineOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1162 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ExportFlowlineOptionsWidget.h` | C++ | 131 |

## Overview

[[[PROSE overview unit=qt-widgets/ExportFlowlineOptionsWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ExportFlowlineOptionsWidget`](#gplatesqtwidgetsexportflowlineoptionswidget) | class | [`ExportOptionsWidget`](ExportOptionsWidget.md) | — | 0 | ExportFlowlineOptionsWidget is used to show export options for exporting flowlines. |

## Members

### `GPlatesQtWidgets::ExportFlowlineOptionsWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( QWidget *parent, GPlatesGui::ExportAnimationContext &export_animation_context, const GPlatesGui::ExportFlowlineAnimationStrategy::const_configuration_ptr & export_configuration, bool configure_dateline_wrapping)` | method | `ExportOptionsWidget` | public | Creates a ExportFlowlineOptionsWidget containing default export options. |
| `create_export_animation_strategy_configuration( const QString &filename_template)` | method | `GPlatesGui::ExportAnimationStrategy::const_configuration_base_ptr` | public | Collects the options specified by the user and returns them as an export animation strategy configuration. |
| `ExportFlowlineOptionsWidget( QWidget *parent_, const GPlatesGui::ExportFlowlineAnimationStrategy::const_configuration_ptr & export_configuration, bool configure_dateline_wrapping)` | constructor | `None` | private | — |
| `d_dateline_wrap_options_widget` | field | `DatelineWrapOptionsWidget` | private | — |
| `d_export_file_options_widget` | field | `ExportFileOptionsWidget` | private | — |
| `d_export_configuration` | field | `GPlatesGui::ExportFlowlineAnimationStrategy::Configuration` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QT_WIDGETS_EXPORTFLOWLINEOPTIONSWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ExportFlowlineOptionsWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportAnimationRegistry](../gui/ExportAnimationRegistry.md) | gui | 5 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ExportFlowlineOptionsWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ExportFlowlineOptionsWidget --body
python scripts/gpq.py uses ExportFlowlineOptionsWidget --kind class
python scripts/gpq.py hier ExportFlowlineOptionsWidget
```
