# QtWidgetUtils

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 0 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/QtWidgetUtils.h` | C++ | 119 |
| `src/qt-widgets/QtWidgetUtils.cc` | C++ | 165 |

## Overview

[[[PROSE overview unit=qt-widgets/QtWidgetUtils tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=qt-widgets/QtWidgetUtils tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
