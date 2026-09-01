# VisualLayersDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 0 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/VisualLayersDialog.h` | C++ | 65 |
| `src/qt-widgets/VisualLayersDialog.cc` | C++ | 51 |

## Overview

A top-level dialog window that displays a `VisualLayersWidget`, providing access to layer management from the main application window or other contexts where a dialog is needed.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::VisualLayersDialog`](#gplatesqtwidgetsvisuallayersdialog) | class | [`GPlatesDialog`](GPlatesDialog.md) | — | 0 | — |

## Members

### `GPlatesQtWidgets::VisualLayersDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `VisualLayersDialog( GPlatesPresentation::VisualLayers &visual_layers, GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, ViewportWindow *viewport_window, QWidget *parent_ = NULL)` | constructor | `None` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_VISUALLAYERSDIALOG_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Dialogs](../gui/Dialogs.md) | gui | 1 |
| [qt-widgets/ColourScaleWidget](ColourScaleWidget.md) | qt-widgets | 1 |
| [qt-widgets/ReconstructLayerOptionsWidget](ReconstructLayerOptionsWidget.md) | qt-widgets | 1 |
| [qt-widgets/ReconstructionLayerOptionsWidget](ReconstructionLayerOptionsWidget.md) | qt-widgets | 1 |
| [qt-widgets/RemappedColourPaletteWidget](RemappedColourPaletteWidget.md) | qt-widgets | 1 |
| [qt-widgets/ScalarField3DLayerOptionsWidget](ScalarField3DLayerOptionsWidget.md) | qt-widgets | 1 |
| [qt-widgets/TopologyGeometryResolverLayerOptionsWidget](TopologyGeometryResolverLayerOptionsWidget.md) | qt-widgets | 1 |
| [qt-widgets/ViewportWindow](ViewportWindow.md) | qt-widgets | 1 |
| [qt-widgets/VisualLayerWidget](VisualLayerWidget.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/VisualLayersDialog.h
python scripts/gpq.py def GPlatesQtWidgets::VisualLayersDialog --body
python scripts/gpq.py uses VisualLayersDialog --kind class
python scripts/gpq.py hier VisualLayersDialog
```
