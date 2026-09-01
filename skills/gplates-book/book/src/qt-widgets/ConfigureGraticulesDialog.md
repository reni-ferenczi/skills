# ConfigureGraticulesDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1500 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ConfigureGraticulesDialog.h` | C++ | 85 |
| `src/qt-widgets/ConfigureGraticulesDialog.cc` | C++ | 99 |
| `src/qt-widgets/ConfigureGraticulesDialogUi.ui` | Qt form | 176 |

## Overview

Configures the appearance of latitude/longitude grid lines (graticules) displayed on the globe or map. The dialog provides controls to adjust graticule settings such as colour, spacing, and visibility. Its overridden `exec()` method takes a `GraticuleSettings` reference, populates the form from current settings, and updates the settings object if the user accepts the dialog.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ConfigureGraticulesDialog`](#gplatesqtwidgetsconfiguregraticulesdialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_ConfigureGraticulesDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ConfigureGraticulesDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ConfigureGraticulesDialog( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `exec( GPlatesGui::GraticuleSettings &settings)` | method | `int` | public | Shows the dialog modal to allow the user to modify the graticule settings passed in as a mutable reference, settings. |
| `populate( const GPlatesGui::GraticuleSettings &settings)` | method | `void` | private | — |
| `save( GPlatesGui::GraticuleSettings &settings)` | method | `void` | private | — |
| `d_colour_button` | field | `ChooseColourButton` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_CONFIGUREGRATICULESDIALOG_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Dialogs](../gui/Dialogs.md) | gui | 10 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ConfigureGraticulesDialog` | `QDialog` | Configure Graticules | 12 |

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `main_buttonbox` | `accepted()` | `this` | `accept()` |
| `main_buttonbox` | `rejected()` | `this` | `reject()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ConfigureGraticulesDialog.h
python scripts/gpq.py def GPlatesQtWidgets::ConfigureGraticulesDialog --body
python scripts/gpq.py uses ConfigureGraticulesDialog --kind class
python scripts/gpq.py hier ConfigureGraticulesDialog
```
