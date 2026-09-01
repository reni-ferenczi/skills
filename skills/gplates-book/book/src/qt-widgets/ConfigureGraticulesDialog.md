# ConfigureGraticulesDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1500 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ConfigureGraticulesDialog.h` | C++ | 85 |
| `src/qt-widgets/ConfigureGraticulesDialog.cc` | C++ | 99 |
| `src/qt-widgets/ConfigureGraticulesDialogUi.ui` | Qt form | 176 |

## Overview

A small modal dialog for editing the latitude/longitude grid lines (graticules) drawn on the globe or map. It edits exactly the four values a `GPlatesGui::GraticuleSettings` holds: the latitude spacing, the longitude spacing, the line colour and a line-width hint. There is no visibility control: `SphericalGrid`/`MapGrid` draw the graticules from these settings unconditionally, and a spacing of zero is what suppresses lines of latitude or of longitude.

The whole dialog is driven by `exec(GraticuleSettings &)`: it calls `populate()` to load the form, runs `QDialog::exec()`, and on `Accepted` calls `save()` to write the edited values back into the caller's settings object; on Cancel the settings are left untouched. `populate`/`save` are also where the unit conversion happens — `GraticuleSettings` stores the two spacings in *radians* while the spin boxes show *degrees*, so they convert in both directions via `GPlatesMaths::convert_rad_to_deg`/`convert_deg_to_rad`. The colour is edited by a `ChooseColourButton` created in the constructor and dropped into the form's placeholder widget, so it does not appear in the generated UI class.

Note that `exec(GraticuleSettings &)` is not an override of `QDialog::exec()` — it is a non-virtual overload with a different signature, and the header makes the inherited zero-argument version private (`using GPlatesDialog::exec;`) to stop it being called by accident. That protection only holds when the object is used through a `ConfigureGraticulesDialog` reference: calling `exec()` through a `QDialog *`/`GPlatesDialog *` still reaches Qt's version and shows the dialog without ever running `populate` or `save`. The single caller, `GPlatesGui::Dialogs::pop_up_configure_graticules_dialog()`, uses the concrete type and passes the view state's graticule settings.

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
