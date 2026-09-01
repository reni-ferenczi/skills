# GPlatesDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1794 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/GPlatesDialog.h` | C++ | 92 |
| `src/qt-widgets/GPlatesDialog.cc` | C++ | 45 |

## Overview

`GPlatesDialog` is the base class every major GPlates dialog inherits from instead of `QDialog` directly. It exists to work around platform-specific quirks in how dialogs open and close, and to standardise a couple of behaviours that plain `QDialog` leaves to each caller: `pop_up()` centralises the show-or-raise logic (delegating to `QtWidgetUtils::pop_up_dialog`) so a dialog that is already open is brought to the front rather than spawning a duplicate, and the constructor requires a parent widget so a dialog can never pop up parentless in the middle of the screen.

`GPlatesGui::Dialogs` is the intended owner of instances of these dialogs, keeping `ViewportWindow` from accumulating direct references to every dialog in the application.

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

Subclasses must still declare `Q_OBJECT` themselves; inheriting from `GPlatesDialog` does not provide it. `pop_up()` is a `Q_SLOT` intended for menu-item wiring rather than direct C++ calls, though nothing prevents the latter.

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
