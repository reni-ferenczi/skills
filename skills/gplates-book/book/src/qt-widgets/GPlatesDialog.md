# GPlatesDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1794 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/GPlatesDialog.h` | C++ | 92 |
| `src/qt-widgets/GPlatesDialog.cc` | C++ | 45 |

## Overview

[[[PROSE overview unit=qt-widgets/GPlatesDialog tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::GPlatesDialog`](#gplatesqtwidgetsgplatesdialog) | class | `QDialog`<br>`boost::noncopyable` | — | 37 | Base class to be used in place of a plain QDialog for major GPlates dialogs. |

## Members

### `GPlatesQtWidgets::GPlatesDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GPlatesDialog( QWidget *_parent, Qt::WindowFlags flags = Qt::Window)` | constructor | `None` | public | always have a parent, otherwise they pop up in the middle of the screen. |
| `~GPlatesDialog()` | destructor | `None` | public | — |
| `pop_up()` | method | `void` | public | If the dialog is currently hidden, show it and ask the WM to raise it to the top. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_GPLATESDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/GPlatesDialog tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/HellingerPickWidget](HellingerPickWidget.md) | qt-widgets | 65 |
| [qt-widgets/HellingerSegmentDialog](HellingerSegmentDialog.md) | qt-widgets | 65 |
| [qt-widgets/HellingerFitWidget](HellingerFitWidget.md) | qt-widgets | 40 |
| [gui/Dialogs](../gui/Dialogs.md) | gui | 27 |
| [qt-widgets/ReadErrorAccumulationDialog](ReadErrorAccumulationDialog.md) | qt-widgets | 20 |
| [qt-widgets/HellingerPointDialog](HellingerPointDialog.md) | qt-widgets | 14 |
| [qt-widgets/SpecifyAnchoredPlateIdDialog](SpecifyAnchoredPlateIdDialog.md) | qt-widgets | 11 |
| [qt-widgets/ManageFeatureCollectionsActionWidget](ManageFeatureCollectionsActionWidget.md) | qt-widgets | 9 |
| [qt-widgets/LogDialog](LogDialog.md) | qt-widgets | 8 |
| [qt-widgets/ShapefileAttributeViewerDialog](ShapefileAttributeViewerDialog.md) | qt-widgets | 8 |
| [qt-widgets/FeaturePropertiesDialog](FeaturePropertiesDialog.md) | qt-widgets | 6 |
| [qt-widgets/HellingerDialog](HellingerDialog.md) | qt-widgets | 6 |
| [qt-widgets/SymbolManagerDialog](SymbolManagerDialog.md) | qt-widgets | 6 |
| [qt-widgets/SetCameraViewpointDialog](SetCameraViewpointDialog.md) | qt-widgets | 5 |
| [qt-widgets/ConfigureGraticulesDialog](ConfigureGraticulesDialog.md) | qt-widgets | 4 |
| [qt-widgets/ConfigureTextOverlayDialog](ConfigureTextOverlayDialog.md) | qt-widgets | 4 |
| [qt-widgets/ConfigureVelocityLegendOverlayDialog](ConfigureVelocityLegendOverlayDialog.md) | qt-widgets | 4 |
| [qt-widgets/LicenseDialog](LicenseDialog.md) | qt-widgets | 4 |
| [qt-widgets/PreferencesDialog](PreferencesDialog.md) | qt-widgets | 4 |
| [qt-widgets/VisualLayersDialog](VisualLayersDialog.md) | qt-widgets | 4 |

*... and 23 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/GPlatesDialog.h
python scripts/gpq.py def GPlatesQtWidgets::GPlatesDialog --body
python scripts/gpq.py uses GPlatesDialog --kind class
python scripts/gpq.py hier GPlatesDialog
```
