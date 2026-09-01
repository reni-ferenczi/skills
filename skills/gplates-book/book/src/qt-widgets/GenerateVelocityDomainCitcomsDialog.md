# GenerateVelocityDomainCitcomsDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 721 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/GenerateVelocityDomainCitcomsDialog.h` | C++ | 90 |
| `src/qt-widgets/GenerateVelocityDomainCitcomsDialog.cc` | C++ | 401 |
| `src/qt-widgets/GenerateVelocityDomainCitcomsDialogUi.ui` | Qt form | 266 |

## Overview

A dialog for generating a global mesh of velocity domain points suitable for CitcomS (a mantle convection code). Users specify the mesh resolution (nodes per cap diamond edge) and provide an output directory and file name template. The dialog generates 12 mesh files (one for each diamond face of the cube mesh), each containing a set of `MeshNode` features with multipoint geometries.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::GenerateVelocityDomainCitcomsDialog`](#gplatesqtwidgetsgeneratevelocitydomaincitcomsdialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_GenerateVelocityDomainCitcomsDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::GenerateVelocityDomainCitcomsDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GenerateVelocityDomainCitcomsDialog( ViewportWindow &main_window_, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~GenerateVelocityDomainCitcomsDialog()` | destructor | `None` | public | — |
| `gen_mesh()` | method | `void` | private | — |
| `set_node_x(int)` | method | `void` | private | — |
| `set_path()` | method | `void` | private | — |
| `select_path()` | method | `void` | private | — |
| `set_file_name_template()` | method | `void` | private | — |
| `d_node_x` | field | `int` | private | — |
| `d_path` | field | `QString` | private | — |
| `d_main_window` | field | `ViewportWindow` | private | — |
| `d_help_dialog_resolution` | field | `InformationDialog` | private | — |
| `d_help_dialog_output` | field | `InformationDialog` | private | — |
| `d_file_name_template` | field | `std::string` | private | — |
| `d_open_directory_dialog` | field | `OpenDirectoryDialog` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `CAP_NUM_PLACE_HOLDER` | variable | `std::string` | — |
| `DENSITY_PLACE_HOLDER` | variable | `std::string` | — |
| `HELP_DIALOG_TITLE_RESOLUTION` | variable | `char` | — |
| `HELP_DIALOG_TEXT_RESOLUTION` | variable | `char` | — |
| `HELP_DIALOG_TITLE_OUTPUT` | variable | `char` | — |
| `HELP_DIALOG_TEXT_OUTPUT` | variable | `char` | — |
| `GENERATE_VELOCITY_DOMAIN_CITCOMS_DIALOG_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Dialogs](../gui/Dialogs.md) | gui | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `GenerateVelocityDomainCitcomsDialog` | `QDialog` | Generate CitcomS Velocity Domain Points | 18 |

**Qt signal/slot connections** (8 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_path` | `clicked()` | `this` | `select_path()` |
| `lineEdit_path` | `editingFinished()` | `this` | `set_path()` |
| `lineEdit_file_template` | `editingFinished()` | `this` | `set_file_name_template()` |
| `node_X` | `valueChanged(int)` | `this` | `set_node_x(int)` |
| `pushButton_info_output` | `clicked()` | `d_help_dialog_output` | `show()` |
| `pushButton_info_resolution` | `clicked()` | `d_help_dialog_resolution` | `show()` |
| `main_buttonbox` | `accepted()` | `this` | `gen_mesh()` |
| `main_buttonbox` | `rejected()` | `this` | `reject()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/GenerateVelocityDomainCitcomsDialog.h
python scripts/gpq.py def GPlatesQtWidgets::GenerateVelocityDomainCitcomsDialog --body
python scripts/gpq.py uses GenerateVelocityDomainCitcomsDialog --kind class
python scripts/gpq.py hier GenerateVelocityDomainCitcomsDialog
```
