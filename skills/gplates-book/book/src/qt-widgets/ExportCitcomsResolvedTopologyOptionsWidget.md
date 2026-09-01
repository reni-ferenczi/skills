# ExportCitcomsResolvedTopologyOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 828 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ExportCitcomsResolvedTopologyOptionsWidget.h` | C++ | 99 |
| `src/qt-widgets/ExportCitcomsResolvedTopologyOptionsWidget.cc` | C++ | 320 |
| `src/qt-widgets/ExportCitcomsResolvedTopologyOptionsWidgetUi.ui` | Qt form | 271 |

## Overview

`ExportCitcomsResolvedTopologyOptionsWidget` is the options panel for exporting resolved topology in CitcomS format. It presents checkboxes for controlling which geometry types (plate polygons, network polygons, slab polygons, plate boundaries, network boundaries, slab boundaries) are exported and whether they go into a single file, individual files per feature, or type-based files.

The widget is created via a factory method and initialized with existing export settings. When the user accepts the export, `create_export_animation_strategy_configuration()` collects the user's choices and builds a configuration object for the `ExportCitcomsResolvedTopologyAnimationStrategy`. It optionally includes a `DatelineWrapOptionsWidget` for controlling whether geometries are wrapped to the dateline.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ExportCitcomsResolvedTopologyOptionsWidget`](#gplatesqtwidgetsexportcitcomsresolvedtopologyoptionswidget) | class | [`ExportOptionsWidget`](ExportOptionsWidget.md)<br>`Ui_ExportCitcomsResolvedTopologyOptionsWidget` | — | 0 | CitcomS-specific resolved topology export options. |

## Members

### `GPlatesQtWidgets::ExportCitcomsResolvedTopologyOptionsWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( QWidget *parent, GPlatesGui::ExportAnimationContext &export_animation_context, const GPlatesGui::ExportCitcomsResolvedTopologyAnimationStrategy::const_configuration_ptr & export_configuration, bool configure_dateline_wrapping)` | method | `ExportOptionsWidget` | public | Creates a ExportCitcomsResolvedTopologyOptionsWidget containing default export options. |
| `create_export_animation_strategy_configuration( const QString &filename_template)` | method | `GPlatesGui::ExportAnimationStrategy::const_configuration_base_ptr` | public | Collects the options specified by the user and returns them as an export animation strategy configuration. |
| `react_check_box_state_changed( int state)` | method | `void` | private | — |
| `ExportCitcomsResolvedTopologyOptionsWidget( QWidget *parent_, const GPlatesGui::ExportCitcomsResolvedTopologyAnimationStrategy::const_configuration_ptr & export_configuration, bool configure_dateline_wrapping)` | constructor | `None` | private | — |
| `make_signal_slot_connections()` | method | `void` | private | — |
| `d_export_configuration` | field | `GPlatesGui::ExportCitcomsResolvedTopologyAnimationStrategy::Configuration` | private | — |
| `d_dateline_wrap_options_widget` | field | `DatelineWrapOptionsWidget` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QT_WIDGETS_EXPORTCITCOMSRESOLVEDTOPOLOGYOPTIONSWIDGET_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportAnimationRegistry](../gui/ExportAnimationRegistry.md) | gui | 5 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ExportCitcomsResolvedTopologyOptionsWidget` | `QWidget` | Export Options | 28 |

**Qt signal/slot connections** (15 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `checkBox_export_plate_polygons_to_all_polygons_file` | `stateChanged(int)` | `this` | `react_check_box_state_changed(int)` |
| `checkBox_export_network_polygons_to_all_polygons_file` | `stateChanged(int)` | `this` | `react_check_box_state_changed(int)` |
| `checkBox_export_slab_polygons_to_all_polygons_file` | `stateChanged(int)` | `this` | `react_check_box_state_changed(int)` |
| `checkBox_export_plate_boundaries_to_all_boundaries_file` | `stateChanged(int)` | `this` | `react_check_box_state_changed(int)` |
| `checkBox_export_network_boundaries_to_all_boundaries_file` | `stateChanged(int)` | `this` | `react_check_box_state_changed(int)` |
| `checkBox_export_slab_boundaries_to_all_boundaries_file` | `stateChanged(int)` | `this` | `react_check_box_state_changed(int)` |
| `checkBox_export_individual_plate_polygon_files` | `stateChanged(int)` | `this` | `react_check_box_state_changed(int)` |
| `checkBox_export_plate_polygons_to_single_file` | `stateChanged(int)` | `this` | `react_check_box_state_changed(int)` |
| `checkBox_export_plate_boundaries_to_type_files` | `stateChanged(int)` | `this` | `react_check_box_state_changed(int)` |
| `checkBox_export_individual_network_polygon_files` | `stateChanged(int)` | `this` | `react_check_box_state_changed(int)` |
| `checkBox_export_network_polygons_to_single_file` | `stateChanged(int)` | `this` | `react_check_box_state_changed(int)` |
| `checkBox_export_network_boundaries_to_type_files` | `stateChanged(int)` | `this` | `react_check_box_state_changed(int)` |
| `checkBox_export_individual_slab_polygon_files` | `stateChanged(int)` | `this` | `react_check_box_state_changed(int)` |
| `checkBox_export_slab_polygons_to_single_file` | `stateChanged(int)` | `this` | `react_check_box_state_changed(int)` |
| `checkBox_export_slab_boundaries_to_type_files` | `stateChanged(int)` | `this` | `react_check_box_state_changed(int)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ExportCitcomsResolvedTopologyOptionsWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ExportCitcomsResolvedTopologyOptionsWidget --body
python scripts/gpq.py uses ExportCitcomsResolvedTopologyOptionsWidget --kind class
python scripts/gpq.py hier ExportCitcomsResolvedTopologyOptionsWidget
```
