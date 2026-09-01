# ProgressDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 683 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ProgressDialog.h` | C++ | 140 |
| `src/qt-widgets/ProgressDialogUi.ui` | Qt form | 71 |

## Overview

A reusable modal-style progress bar dialog wired around `Ui_ProgressDialog` (label, progress bar, cancel button). Callers driving a long-running loop (import, export, animation generation — see the long "Used by" list) call `update_value`/`update_progress` on each iteration; both call `progress_bar->repaint()` followed by `QCoreApplication::processEvents()` so the bar and label actually redraw and the cancel button stays clickable even though the caller's own loop is blocking the event loop.

Cancellation is cooperative rather than exception-driven: `handle_cancel` (triggered by the cancel button or by pressing Escape, which Qt turns into `rejected()`) only sets `cancel_flag`; the caller's loop is expected to poll `canceled()` between iterations and unwind itself. The window is built with `Qt::CustomizeWindowHint | Qt::WindowTitleHint`, so it has a title bar but no system close/minimize/maximize buttons — cancel button or Escape are the only ways to dismiss it.

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

`update_value`/`update_progress` call `QCoreApplication::processEvents()` synchronously from inside whatever loop the caller is running, which re-enters the event loop and can dispatch other pending events (including further user input) before returning — the same reentrancy hazard as any manual `processEvents()` call. `cancel_flag` is only ever set to `true`; nothing resets it, so a dialog instance is single-use for one cancellable operation.

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
