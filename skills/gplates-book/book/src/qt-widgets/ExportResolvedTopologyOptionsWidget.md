# ExportResolvedTopologyOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 913 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ExportResolvedTopologyOptionsWidget.h` | C++ | 114 |
| `src/qt-widgets/ExportResolvedTopologyOptionsWidget.cc` | C++ | 306 |
| `src/qt-widgets/ExportResolvedTopologyOptionsWidgetUi.ui` | Qt form | 236 |

## Overview

[[[PROSE overview unit=qt-widgets/ExportResolvedTopologyOptionsWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ExportResolvedTopologyOptionsWidget`](#gplatesqtwidgetsexportresolvedtopologyoptionswidget) | class | [`ExportOptionsWidget`](ExportOptionsWidget.md)<br>`Ui_ExportResolvedTopologyOptionsWidget` | — | 0 | General (non-CitcomS-specific) resolved topology export options. |

## Members

### `GPlatesQtWidgets::ExportResolvedTopologyOptionsWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( QWidget *parent, GPlatesGui::ExportAnimationContext &export_animation_context, const GPlatesGui::ExportResolvedTopologyAnimationStrategy::const_configuration_ptr & export_configuration, bool configure_dateline_wrapping)` | method | `ExportOptionsWidget` | public | Creates a ExportResolvedTopologyOptionsWidget containing default export options. |
| `create_export_animation_strategy_configuration( const QString &filename_template)` | method | `GPlatesGui::ExportAnimationStrategy::const_configuration_base_ptr` | public | Collects the options specified by the user and returns them as an export animation strategy configuration. |
| `react_export_resolved_geometry_check_box_state_changed( int state)` | method | `void` | private | — |
| `react_force_polygon_orientation_check_box_state_changed( int state)` | method | `void` | private | — |
| `react_polygon_orientation_combobox_state_changed( int index)` | method | `void` | private | — |
| `ExportResolvedTopologyOptionsWidget( QWidget *parent_, const GPlatesGui::ExportResolvedTopologyAnimationStrategy::const_configuration_ptr & export_configuration, bool configure_dateline_wrapping)` | constructor | `None` | private | — |
| `make_signal_slot_connections()` | method | `void` | private | — |
| `d_export_configuration` | field | `GPlatesGui::ExportResolvedTopologyAnimationStrategy::Configuration` | private | — |
| `d_dateline_wrap_options_widget` | field | `DatelineWrapOptionsWidget` | private | — |
| `d_export_file_options_widget` | field | `ExportFileOptionsWidget` | private | — |
| `d_help_export_topological_line_sub_segments_dialog` | field | `InformationDialog` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `HELP_EXPORT_TOPOLOGICAL_LINE_SUB_SEGMENTS_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_EXPORT_TOPOLOGICAL_LINE_SUB_SEGMENTS_DIALOG_TEXT` | variable | `QString` | — |
| `GPLATES_QT_WIDGETS_EXPORTRESOLVEDTOPOLOGYOPTIONSWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ExportResolvedTopologyOptionsWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportAnimationRegistry](../gui/ExportAnimationRegistry.md) | gui | 5 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ExportResolvedTopologyOptionsWidget` | `QWidget` | Form | 18 |

**Qt signal/slot connections** (8 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `export_resolved_lines_checkbox` | `stateChanged(int)` | `this` | `react_export_resolved_geometry_check_box_state_changed(int)` |
| `export_resolved_polygons_checkbox` | `stateChanged(int)` | `this` | `react_export_resolved_geometry_check_box_state_changed(int)` |
| `export_resolved_networks_checkbox` | `stateChanged(int)` | `this` | `react_export_resolved_geometry_check_box_state_changed(int)` |
| `export_resolved_boundary_segments_checkbox` | `stateChanged(int)` | `this` | `react_export_resolved_geometry_check_box_state_changed(int)` |
| `export_topological_line_sub_segments_checkbox` | `stateChanged(int)` | `this` | `react_export_resolved_geometry_check_box_state_changed(int)` |
| `force_polygon_orientation_checkbox` | `stateChanged(int)` | `this` | `react_force_polygon_orientation_check_box_state_changed(int)` |
| `polygon_orientation_combobox` | `currentIndexChanged(int)` | `this` | `react_polygon_orientation_combobox_state_changed(int)` |
| `push_button_help_export_topological_line_sub_segments` | `clicked()` | `d_help_export_topological_line_sub_segments_dialog` | `show()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ExportResolvedTopologyOptionsWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ExportResolvedTopologyOptionsWidget --body
python scripts/gpq.py uses ExportResolvedTopologyOptionsWidget --kind class
python scripts/gpq.py hier ExportResolvedTopologyOptionsWidget
```
