# SetCameraViewpointDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1602 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/SetCameraViewpointDialog.h` | C++ | 76 |
| `src/qt-widgets/SetCameraViewpointDialog.cc` | C++ | 69 |
| `src/qt-widgets/SetCameraViewpointDialogUi.ui` | Qt form | 115 |

## Overview

`SetCameraViewpointDialog` is a small modal dialog, built from `SetCameraViewpointDialogUi.ui`, that lets the user type an explicit latitude/longitude for the camera instead of dragging the globe. It fixes its own window flags (no resize, no minimize/maximize, no context help button) via `Qt::CustomizeWindowHint | Qt::WindowTitleHint | Qt::WindowSystemMenuHint | Qt::MSWindowsFixedSizeDialogHint`, so it behaves as a plain fixed-size prompt rather than a normal resizable window.

`set_lat_lon()` both seeds the two spin boxes with the camera's current position and pre-selects the latitude field so a caller who opens the dialog can start typing a replacement value immediately; `latitude()` and `longitude()` then read back whatever the user entered once the dialog is accepted.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::SetCameraViewpointDialog`](#gplatesqtwidgetssetcameraviewpointdialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_SetCameraViewpointDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::SetCameraViewpointDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SetCameraViewpointDialog( ViewportWindow &viewport_window, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `set_lat_lon( const double &lat, const double &lon)` | method | `void` | public | — |
| `latitude()` | method | `double` | public | — |
| `longitude()` | method | `double` | public | — |
| `d_viewport_window_ptr` | field | `ViewportWindow` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_SETCAMERAVIEWPOINTDIALOG_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportNetRotationAnimationStrategy](../gui/ExportNetRotationAnimationStrategy.md) | gui | 7 |
| [maths/AzimuthalEqualAreaProjection](../maths/AzimuthalEqualAreaProjection.md) | maths | 7 |
| [maths/DateLineWrapper](../maths/DateLineWrapper.md) | maths | 7 |
| [gui/Dialogs](../gui/Dialogs.md) | gui | 6 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 6 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 5 |
| [qt-widgets/MovePoleWidget](MovePoleWidget.md) | qt-widgets | 5 |
| [qt-widgets/ReconstructionViewWidget](ReconstructionViewWidget.md) | qt-widgets | 5 |
| [utils/LatLonAreaSampling](../utils/LatLonAreaSampling.md) | utils | 5 |
| [app-logic/ResolvedTriangulationDelaunay2](../app-logic/ResolvedTriangulationDelaunay2.md) | app-logic | 4 |
| [feature-visitors/QueryFeaturePropertiesWidgetPopulator](../feature-visitors/QueryFeaturePropertiesWidgetPopulator.md) | feature-visitors | 4 |
| [feature-visitors/ViewFeatureGeometriesWidgetPopulator](../feature-visitors/ViewFeatureGeometriesWidgetPopulator.md) | feature-visitors | 4 |
| [file-io/OgrWriter](../file-io/OgrWriter.md) | file-io | 4 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 4 |
| [qt-widgets/EditGeometryWidget](EditGeometryWidget.md) | qt-widgets | 4 |
| [qt-widgets/FiniteRotationCalculatorDialog](FiniteRotationCalculatorDialog.md) | qt-widgets | 4 |
| [qt-widgets/MapView](MapView.md) | qt-widgets | 4 |
| [app-logic/NetRotationUtils](../app-logic/NetRotationUtils.md) | app-logic | 3 |
| [file-io/GMTFormatFlowlineExport](../file-io/GMTFormatFlowlineExport.md) | file-io | 3 |
| [app-logic/PlateVelocityUtils](../app-logic/PlateVelocityUtils.md) | app-logic | 2 |

*... and 45 more units.*

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `SetCameraViewpointDialog` | `QDialog` | Set Camera Location | 7 |

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `main_buttonbox` | `accepted()` | `this` | `accept()` |
| `main_buttonbox` | `rejected()` | `this` | `reject()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/SetCameraViewpointDialog.h
python scripts/gpq.py def GPlatesQtWidgets::SetCameraViewpointDialog --body
python scripts/gpq.py uses SetCameraViewpointDialog --kind class
python scripts/gpq.py hier SetCameraViewpointDialog
```
