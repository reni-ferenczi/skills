# ExportImageResolutionOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 347 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ExportImageResolutionOptionsWidget.h` | C++ | 115 |
| `src/qt-widgets/ExportImageResolutionOptionsWidget.cc` | C++ | 167 |
| `src/qt-widgets/ExportImageResolutionOptionsWidgetUi.ui` | Qt form | 175 |

## Overview

[[[PROSE overview unit=qt-widgets/ExportImageResolutionOptionsWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ExportImageResolutionOptionsWidget`](#gplatesqtwidgetsexportimageresolutionoptionswidget) | class | `QWidget`<br>`Ui_ExportImageResolutionOptionsWidget` | — | 0 | ExportImageResolutionOptionsWidget is used to show export options for exporting images of the globe/map view (including SVG export). |

## Members

### `GPlatesQtWidgets::ExportImageResolutionOptionsWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( QWidget *parent, GPlatesGui::ExportAnimationContext &export_animation_context, const GPlatesGui::ExportOptionsUtils::ExportImageResolutionOptions &default_export_image_resolution_options)` | method | `ExportImageResolutionOptionsWidget` | public | Creates a ExportImageResolutionOptionsWidget containing default export options. |
| `react_width_spin_box_value_changed( int value)` | method | `void` | private | — |
| `react_height_spin_box_value_changed( int value)` | method | `void` | private | — |
| `react_constrain_aspect_ratio_check_box_clicked()` | method | `void` | private | — |
| `handle_use_main_window_dimensions_push_button_clicked()` | method | `void` | private | — |
| `d_export_animation_context` | field | `GPlatesGui::ExportAnimationContext` | private | — |
| `d_export_image_resolution_options` | field | `GPlatesGui::ExportOptionsUtils::ExportImageResolutionOptions` | private | — |
| `d_constrained_aspect_ratio` | field | `boost::optional<double>` | private | — |
| `ExportImageResolutionOptionsWidget( QWidget *parent_, GPlatesGui::ExportAnimationContext &export_animation_context, const GPlatesGui::ExportOptionsUtils::ExportImageResolutionOptions &default_export_image_resolution_options)` | constructor | `None` | private | — |
| `make_signal_slot_connections()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QT_WIDGETS_EXPORTIMAGERESOLUTIONOPTIONSWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ExportImageResolutionOptionsWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ExportSvgOptionsWidget](ExportSvgOptionsWidget.md) | qt-widgets | 5 |
| [qt-widgets/ExportImageOptionsWidget](ExportImageOptionsWidget.md) | qt-widgets | 3 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ExportImageResolutionOptionsWidget` | `QWidget` | Form | 9 |

**Qt signal/slot connections** (4 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `width_spin_box` | `valueChanged(int)` | `this` | `react_width_spin_box_value_changed(int)` |
| `height_spin_box` | `valueChanged(int)` | `this` | `react_height_spin_box_value_changed(int)` |
| `constrain_aspect_ratio_check_box` | `stateChanged(int)` | `this` | `react_constrain_aspect_ratio_check_box_clicked()` |
| `use_main_window_dimensions_push_button` | `clicked()` | `this` | `handle_use_main_window_dimensions_push_button_clicked()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ExportImageResolutionOptionsWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ExportImageResolutionOptionsWidget --body
python scripts/gpq.py uses ExportImageResolutionOptionsWidget --kind class
python scripts/gpq.py hier ExportImageResolutionOptionsWidget
```
