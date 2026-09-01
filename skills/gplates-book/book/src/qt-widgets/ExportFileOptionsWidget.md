# ExportFileOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 48 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ExportFileOptionsWidget.h` | C++ | 155 |
| `src/qt-widgets/ExportFileOptionsWidgetUi.ui` | Qt form | 91 |

## Overview

[[[PROSE overview unit=qt-widgets/ExportFileOptionsWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ExportFileOptionsWidget`](#gplatesqtwidgetsexportfileoptionswidget) | class | `QWidget`<br>`Ui_ExportFileOptionsWidget` | — | 0 | ExportFileOptionsWidget is used to allow the user to select exporting to a single file or exporting to multiple files (one output file per input file) or both. |

## Members

### `GPlatesQtWidgets::ExportFileOptionsWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( QWidget *parent, const GPlatesGui::ExportOptionsUtils::ExportFileOptions &default_export_file_options)` | method | `ExportFileOptionsWidget` | public | Creates a ExportFileOptionsWidget using default options. |
| `react_check_box_state_changed( int state)` | method | `void` | private | — |
| `ExportFileOptionsWidget( QWidget *parent_, const GPlatesGui::ExportOptionsUtils::ExportFileOptions &export_file_options_)` | constructor | `None` | private | — |
| `make_signal_slot_connections()` | method | `void` | private | — |
| `d_export_file_options` | field | `GPlatesGui::ExportOptionsUtils::ExportFileOptions` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QT_WIDGETS_EXPORTFILEOPTIONSWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ExportFileOptionsWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ExportFlowlineOptionsWidget](ExportFlowlineOptionsWidget.md) | qt-widgets | 3 |
| [qt-widgets/ExportMotionPathOptionsWidget](ExportMotionPathOptionsWidget.md) | qt-widgets | 3 |
| [qt-widgets/ExportReconstructedGeometryOptionsWidget](ExportReconstructedGeometryOptionsWidget.md) | qt-widgets | 3 |
| [qt-widgets/ExportVelocityOptionsWidget](ExportVelocityOptionsWidget.md) | qt-widgets | 3 |
| [qt-widgets/ExportResolvedTopologyOptionsWidget](ExportResolvedTopologyOptionsWidget.md) | qt-widgets | 2 |
| [qt-widgets/ExportScalarCoverageOptionsWidget](ExportScalarCoverageOptionsWidget.md) | qt-widgets | 2 |
| [qt-widgets/ExportDeformationOptionsWidget](ExportDeformationOptionsWidget.md) | qt-widgets | 1 |
| [qt-widgets/ExportNetRotationOptionsWidget](ExportNetRotationOptionsWidget.md) | qt-widgets | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ExportFileOptionsWidget` | `QWidget` | Export Options | 6 |

**Qt signal/slot connections** (3 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `checkBox_export_to_single_file` | `stateChanged(int)` | `this` | `react_check_box_state_changed(int)` |
| `checkBox_export_to_multiple_files` | `stateChanged(int)` | `this` | `react_check_box_state_changed(int)` |
| `checkBox_separate_output_directory_per_file` | `stateChanged(int)` | `this` | `react_check_box_state_changed(int)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ExportFileOptionsWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ExportFileOptionsWidget --body
python scripts/gpq.py uses ExportFileOptionsWidget --kind class
python scripts/gpq.py hier ExportFileOptionsWidget
```
