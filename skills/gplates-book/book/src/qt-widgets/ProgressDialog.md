# ProgressDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 683 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ProgressDialog.h` | C++ | 140 |
| `src/qt-widgets/ProgressDialogUi.ui` | Qt form | 71 |

## Overview

[[[PROSE overview unit=qt-widgets/ProgressDialog tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ProgressDialog`](#gplatesqtwidgetsprogressdialog) | class | `QDialog`<br>`Ui_ProgressDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ProgressDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ProgressDialog( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~ProgressDialog()` | destructor | `None` | public | — |
| `canceled()` | method | `bool` | public | — |
| `disable_cancel_button( bool flag)` | method | `void` | public | — |
| `set_text( const QString message)` | method | `void` | public | — |
| `setRange( int min, int max)` | method | `void` | public | — |
| `setValue( int val)` | method | `void` | public | — |
| `update_value( int val)` | method | `void` | public | — |
| `update_progress( int val, const QString message)` | method | `void` | public | — |
| `handle_cancel()` | method | `void` | private | — |
| `cancel_flag` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `PROGRESS_DIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ProgressDialog tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ScalarField3DLayerOptionsWidget](ScalarField3DLayerOptionsWidget.md) | qt-widgets | 60 |
| [qt-widgets/HellingerFitWidget](HellingerFitWidget.md) | qt-widgets | 27 |
| [qt-widgets/ConfigureCanvasToolGeometryRenderParametersDialog](ConfigureCanvasToolGeometryRenderParametersDialog.md) | qt-widgets | 18 |
| [qt-widgets/EditOldPlatesHeaderWidget](EditOldPlatesHeaderWidget.md) | qt-widgets | 18 |
| [qt-widgets/GenerateVelocityDomainTerraDialog](GenerateVelocityDomainTerraDialog.md) | qt-widgets | 17 |
| [qt-widgets/KinematicGraphsDialog](KinematicGraphsDialog.md) | qt-widgets | 16 |
| [app-logic/UserPreferences](../app-logic/UserPreferences.md) | app-logic | 15 |
| [qt-widgets/GenerateDeformingMeshPointsDialog](GenerateDeformingMeshPointsDialog.md) | qt-widgets | 15 |
| [qt-widgets/ExportAnimationDialog](ExportAnimationDialog.md) | qt-widgets | 14 |
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 14 |
| [qt-widgets/ExportRasterOptionsWidget](ExportRasterOptionsWidget.md) | qt-widgets | 13 |
| [qt-widgets/AnimateDialog](AnimateDialog.md) | qt-widgets | 11 |
| [qt-widgets/GenerateVelocityDomainLatLonDialog](GenerateVelocityDomainLatLonDialog.md) | qt-widgets | 11 |
| [qt-widgets/HellingerPointDialog](HellingerPointDialog.md) | qt-widgets | 11 |
| [qt-widgets/GenerateVelocityDomainCitcomsDialog](GenerateVelocityDomainCitcomsDialog.md) | qt-widgets | 10 |
| [qt-widgets/AssignReconstructionPlateIdsDialog](AssignReconstructionPlateIdsDialog.md) | qt-widgets | 8 |
| [qt-widgets/EditTimeSequenceWidget](EditTimeSequenceWidget.md) | qt-widgets | 8 |
| [qt-widgets/EditTotalReconstructionSequenceWidget](EditTotalReconstructionSequenceWidget.md) | qt-widgets | 8 |
| [qt-widgets/ImportScalarField3DDialog](ImportScalarField3DDialog.md) | qt-widgets | 7 |
| [qt-widgets/ScalarField3DDepthLayersPage](ScalarField3DDepthLayersPage.md) | qt-widgets | 7 |

*... and 63 more units.*

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ProgressDialog` | `QDialog` | Progress | 4 |

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `cancel_button` | `clicked()` | `this` | `handle_cancel()` |
| `this` | `rejected()` | `this` | `handle_cancel()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ProgressDialog.h
python scripts/gpq.py def GPlatesQtWidgets::ProgressDialog --body
python scripts/gpq.py uses ProgressDialog --kind class
python scripts/gpq.py hier ProgressDialog
```
