# InsertVGPReconstructionPoleDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 253 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/InsertVGPReconstructionPoleDialog.h` | C++ | 94 |
| `src/qt-widgets/InsertVGPReconstructionPoleDialog.cc` | C++ | 302 |
| `src/qt-widgets/InsertVGPReconstructionPoleDialogUi.ui` | Qt form | 158 |

## Overview

[[[PROSE overview unit=qt-widgets/InsertVGPReconstructionPoleDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::InsertVGPReconstructionPoleDialog`](#gplatesqtwidgetsinsertvgpreconstructionpoledialog) | class | `QDialog`<br>`Ui_InsertVGPReconstructionPoleDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::InsertVGPReconstructionPoleDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InsertVGPReconstructionPoleDialog( GPlatesPresentation::ViewState &view_state_, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `setup( const GPlatesQtWidgets::ReconstructionPole &reconstruction_pole)` | method | `void` | public | — |
| `d_reconstruction_pole` | field | `ReconstructionPole` | private | — |
| `d_pole_sequence_table_widget_ptr` | field | `PoleSequenceTableWidget` | private | — |
| `d_reconstruction_pole_widget_ptr` | field | `ReconstructionPoleWidget` | private | — |
| `d_application_state_ptr` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_file_state` | field | `GPlatesAppLogic::FeatureCollectionFileState` | private | The loaded feature collection files. |
| `d_file_io` | field | `GPlatesAppLogic::FeatureCollectionFileIO` | private | Used to create an empty feature collection file. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `examine_trs( std::vector<GPlatesQtWidgets::PoleSequenceTableWidget::PoleSequenceInfo> & sequence_choices, GPlatesFeatureVisitors::TotalReconstructionSequencePlateIdFinder &trs_plate_id_finder, GPlatesFeatureVisitors::TotalReconstructionSequenceTimePeriodFinder &trs_time_period_finder, GPlatesModel::integer_plate_id_typ ...` | function | `void` | Adapted from ModifyReconstructionPoleWidget class. |
| `find_trses( std::vector<GPlatesQtWidgets::PoleSequenceTableWidget::PoleSequenceInfo> & sequence_choices, GPlatesFeatureVisitors::TotalReconstructionSequencePlateIdFinder &trs_plate_id_finder, GPlatesFeatureVisitors::TotalReconstructionSequenceTimePeriodFinder &trs_time_period_finder, GPlatesModel::integer_plate_id_type ...` | function | `void` | This finds all the TRSes (total reconstruction sequences) in the supplied reconstruction whose fixed or moving ref-frame plate ID matches our plate ID of interest. |
| `GPLATES_QTWIDGETS_INSERTVGPRECONSTRUCTIONPOLEDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/InsertVGPReconstructionPoleDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/CalculateReconstructionPoleDialog](CalculateReconstructionPoleDialog.md) | qt-widgets | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `InsertVGPReconstructionPoleDialog` | `QDialog` | Insert VGP Reconstruction Pole | 14 |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/InsertVGPReconstructionPoleDialog.h
python scripts/gpq.py def GPlatesQtWidgets::InsertVGPReconstructionPoleDialog --body
python scripts/gpq.py uses InsertVGPReconstructionPoleDialog --kind class
python scripts/gpq.py hier InsertVGPReconstructionPoleDialog
```
