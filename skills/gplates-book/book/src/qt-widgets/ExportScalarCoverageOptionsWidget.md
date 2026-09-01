# ExportScalarCoverageOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 536 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ExportScalarCoverageOptionsWidget.h` | C++ | 108 |
| `src/qt-widgets/ExportScalarCoverageOptionsWidget.cc` | C++ | 297 |
| `src/qt-widgets/ExportScalarCoverageOptionsWidgetUi.ui` | Qt form | 158 |

## Overview

[[[PROSE overview unit=qt-widgets/ExportScalarCoverageOptionsWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ExportScalarCoverageOptionsWidget`](#gplatesqtwidgetsexportscalarcoverageoptionswidget) | class | [`ExportOptionsWidget`](ExportOptionsWidget.md)<br>`Ui_ExportScalarCoverageOptionsWidget` | — | 0 | ExportScalarCoverageOptionsWidget is used to show export options for exporting reconstructed scalar coverages. |

## Members

### `GPlatesQtWidgets::ExportScalarCoverageOptionsWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( QWidget *parent, GPlatesGui::ExportAnimationContext &export_animation_context, const GPlatesGui::ExportScalarCoverageAnimationStrategy::const_configuration_ptr &export_configuration)` | method | `ExportOptionsWidget` | public | Creates a ExportScalarCoverageOptionsWidget containing default export options. |
| `create_export_animation_strategy_configuration( const QString &filename_template)` | method | `GPlatesGui::ExportAnimationStrategy::const_configuration_base_ptr` | public | Collects the options specified by the user and returns them as an export animation strategy configuration. |
| `react_gmt_domain_point_format_radio_button_toggled( bool checked)` | method | `void` | private | — |
| `react_include_dilatation_strain_check_box_clicked()` | method | `void` | private | — |
| `react_include_dilatation_strain_rate_check_box_clicked()` | method | `void` | private | — |
| `react_include_second_invariant_check_box_clicked()` | method | `void` | private | — |
| `ExportScalarCoverageOptionsWidget( QWidget *parent_, const GPlatesGui::ExportScalarCoverageAnimationStrategy::const_configuration_ptr &export_configuration)` | constructor | `None` | private | — |
| `make_signal_slot_connections()` | method | `void` | private | — |
| `update_output_description_label()` | method | `void` | private | — |
| `d_export_configuration` | field | `GPlatesGui::ExportScalarCoverageAnimationStrategy::configuration_ptr` | private | — |
| `d_export_file_options_widget` | field | `ExportFileOptionsWidget` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QT_WIDGETS_EXPORTSCALARCOVERAGEOPTIONSWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ExportScalarCoverageOptionsWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportAnimationRegistry](../gui/ExportAnimationRegistry.md) | gui | 3 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ExportScalarCoverageOptionsWidget` | `QWidget` | Form | 13 |

**Qt signal/slot connections** (5 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `include_dilatation_strain_check_box` | `stateChanged(int)` | `this` | `react_include_dilatation_strain_check_box_clicked()` |
| `include_dilatation_strain_rate_check_box` | `stateChanged(int)` | `this` | `react_include_dilatation_strain_rate_check_box_clicked()` |
| `include_second_invariant_strain_rate_check_box` | `stateChanged(int)` | `this` | `react_include_second_invariant_check_box_clicked()` |
| `gmt_lon_lat_radio_button` | `toggled(bool)` | `this` | `react_gmt_domain_point_format_radio_button_toggled(bool)` |
| `gmt_lat_lon_radio_button` | `toggled(bool)` | `this` | `react_gmt_domain_point_format_radio_button_toggled(bool)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ExportScalarCoverageOptionsWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ExportScalarCoverageOptionsWidget --body
python scripts/gpq.py uses ExportScalarCoverageOptionsWidget --kind class
python scripts/gpq.py hier ExportScalarCoverageOptionsWidget
```
