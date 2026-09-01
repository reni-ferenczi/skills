# QtWidgetUtils

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 0 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/QtWidgetUtils.h` | C++ | 119 |
| `src/qt-widgets/QtWidgetUtils.cc` | C++ | 165 |

## Overview

A grab-bag of Qt widget/dialog helpers used across the dozens of `*Dialog` and `*Widget` classes in this module (see the long "Used by" list) so each one does not reimplement common Qt boilerplate. `add_widget_to_placeholder` is the standard trick for dropping a hand-constructed widget into a spot reserved by a Designer `.ui` form. `reposition_to_side_of_parent` and `pop_up_dialog` paper over platform differences in how dialogs position and raise themselves — the latter's `activateWindow()`/`raise()` sequence exists specifically because re-selecting a menu action for an already-open dialog needs to refocus it, and some platforms do not keep child dialogs on top of their parent by default.

`get_colour_with_alpha` wraps `QColorDialog::getColor` with `ShowAlphaChannel` and converts the result to `GPlatesGui::Colour`, working around the Qt 4.5 `QColorDialog` API change (the older `getRgba()` is deprecated). `is_control_c` normalises the Ctrl+C vs. Cmd+C distinction between macOS and other platforms so callers can check for a single logical shortcut. `create_transparent_checkerboard` renders the usual light/dark grey checkerboard pattern used as a background behind semi-transparent imagery, by painting a 2x2 tile once and tiling it across the requested size.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_QTWIDGETUTILS_H` | macro | `None` | — |
| `add_widget_to_placeholder( QWidget *widget, QWidget *placeholder)` | function | `void` | Inserts widget into placeholder such that widget fills up the entirety of placeholder. |
| `reposition_to_side_of_parent( QDialog *dialog)` | function | `void` | Repositions dialog to the side of its parent. |
| `pop_up_dialog( QWidget *dialog)` | function | `void` | Shows dialog if currently hidden, ensures that it is active and also ensures that it is on top of its parent. |
| `resize_based_on_size_hint( QDialog *dialog)` | function | `void` | Sets the height of dialog to that of its sizeHint(), and ensures that the width of dialog is at least that of its sizeHint(). |
| `get_colour_with_alpha( const GPlatesGui::Colour &initial, QWidget *parent)` | function | `boost::optional<GPlatesGui::Colour>` | Retrieves a colour using a standard dialog box. |
| `is_control_c( QKeyEvent *key_event)` | function | `bool` | Returns true if the key\_event represents Ctrl+C on Windows and Linux, and control+C (not command+C) on the Mac. |
| `create_transparent_checkerboard( int width, int height, int grid_size)` | function | `QPixmap` | Returns a checkboard typically used as the background of a semi-transparent image, with the given width, height and grid\_size. |

## Notes

`resize_based_on_size_hint` only works correctly if any vertical spacers in the dialog's layout have a `sizeHint()` height of 0 (see `SetProjectionDialog` for an example); otherwise the computed height will be wrong. All functions here are free functions with no shared state, so there is nothing to synchronise.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/VisualLayerWidget](VisualLayerWidget.md) | qt-widgets | 21 |
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 17 |
| [qt-widgets/SelectionWidget](SelectionWidget.md) | qt-widgets | 15 |
| [qt-widgets/ConfigureVelocityLegendOverlayDialog](ConfigureVelocityLegendOverlayDialog.md) | qt-widgets | 13 |
| [qt-widgets/CreateFeatureDialog](CreateFeatureDialog.md) | qt-widgets | 13 |
| [qt-widgets/ConfigureCanvasToolGeometryRenderParametersDialog](ConfigureCanvasToolGeometryRenderParametersDialog.md) | qt-widgets | 9 |
| [qt-widgets/GenerateVelocityDomainTerraDialog](GenerateVelocityDomainTerraDialog.md) | qt-widgets | 9 |
| [qt-widgets/ReconstructLayerOptionsWidget](ReconstructLayerOptionsWidget.md) | qt-widgets | 9 |
| [qt-widgets/RemappedColourPaletteWidget](RemappedColourPaletteWidget.md) | qt-widgets | 9 |
| [qt-widgets/ShapefileAttributeMapperDialog](ShapefileAttributeMapperDialog.md) | qt-widgets | 8 |
| [qt-widgets/ShapefileAttributeRemapperDialog](ShapefileAttributeRemapperDialog.md) | qt-widgets | 8 |
| [qt-widgets/ConfigureTextOverlayDialog](ConfigureTextOverlayDialog.md) | qt-widgets | 7 |
| [qt-widgets/ExportVelocityOptionsWidget](ExportVelocityOptionsWidget.md) | qt-widgets | 7 |
| [qt-widgets/CalculateReconstructionPoleDialog](CalculateReconstructionPoleDialog.md) | qt-widgets | 5 |
| [qt-widgets/ConfigureExportParametersDialog](ConfigureExportParametersDialog.md) | qt-widgets | 5 |
| [qt-widgets/ConfigureGraticulesDialog](ConfigureGraticulesDialog.md) | qt-widgets | 5 |
| [qt-widgets/CreateSmallCircleFeatureDialog](CreateSmallCircleFeatureDialog.md) | qt-widgets | 5 |
| [qt-widgets/ElidedLabel](ElidedLabel.md) | qt-widgets | 5 |
| [qt-widgets/ExportResolvedTopologyOptionsWidget](ExportResolvedTopologyOptionsWidget.md) | qt-widgets | 5 |
| [qt-widgets/PythonConsoleDialog](PythonConsoleDialog.md) | qt-widgets | 5 |

*... and 75 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/QtWidgetUtils.h
```
