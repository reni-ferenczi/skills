# GenerateVelocityDomainTerraDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 722 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/GenerateVelocityDomainTerraDialog.h` | C++ | 116 |
| `src/qt-widgets/GenerateVelocityDomainTerraDialog.cc` | C++ | 672 |
| `src/qt-widgets/GenerateVelocityDomainTerraDialogUi.ui` | Qt form | 332 |

## Overview

Dialog for generating velocity domain points using the Terra spherical icosahedral gridding library. The Terra algorithm creates a grid of points distributed across the globe according to configurable parameters: mt controls the icosahedral diamond resolution (power of two), nt controls the local subdomain resolution (power of two), and nd controls diamond density per processor (5 or 10). The dialog lets users set these parameters, choose an output directory, and define a filename template to save the generated points as GPML files.

The dialog delegates the actual gridding work to `GenerateVelocityDomainTerra` in app-logic and saves the result as features in the model. It enforces parameter constraints via custom spinbox validators — `PowerOfTwoSpinBox` for mt and nt, and `NdSpinBox` which accepts only 5 or 10. Parameter changes trigger recalculation of the required processor count via the formula (mt/nt)² × (10/nd), which the dialog displays to guide the user towards feasible configurations.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::PowerOfTwoSpinBox`](#anonymouspoweroftwospinbox) | class | `QSpinBox` | — | 0 | A QSpinBox that only allows power-of-two values. |
| [`(anonymous)::NdSpinBox`](#anonymousndspinbox) | class | `QSpinBox` | — | 0 | A QSpinBox for the Terra 'nd' parameter which can only be 5 or 10. |
| [`GPlatesQtWidgets::GenerateVelocityDomainTerraDialog`](#gplatesqtwidgetsgeneratevelocitydomainterradialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_GenerateVelocityDomainTerraDialog` | — | 0 | — |

## Members

### `(anonymous)::PowerOfTwoSpinBox`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PowerOfTwoSpinBox( QWidget *parent_)` | constructor | `None` | public | — |
| `stepBy( int steps)` | method | `void` | public | — |
| `validate( QString &input_, int &pos_)` | method | `QValidator::State` | public | — |
| `fixup( QString &input_)` | method | `void` | public | — |

### `(anonymous)::NdSpinBox`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `NdSpinBox( QWidget *parent_)` | constructor | `None` | public | — |
| `validate( QString &input_, int &pos_)` | method | `QValidator::State` | public | — |

### `GPlatesQtWidgets::GenerateVelocityDomainTerraDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GenerateVelocityDomainTerraDialog( ViewportWindow &main_window_, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `generate_velocity_domain()` | method | `void` | private | — |
| `handle_mt_value_changed( int mt)` | method | `void` | private | — |
| `handle_nt_value_changed( int nt)` | method | `void` | private | — |
| `handle_nd_value_changed( int nd)` | method | `void` | private | — |
| `set_path()` | method | `void` | private | — |
| `select_path()` | method | `void` | private | — |
| `set_file_name_template()` | method | `void` | private | — |
| `d_main_window` | field | `ViewportWindow` | private | — |
| `d_mt` | field | `int` | private | — |
| `d_nt` | field | `int` | private | — |
| `d_nd` | field | `int` | private | — |
| `d_num_processors` | field | `int` | private | — |
| `d_path` | field | `QString` | private | — |
| `d_file_name_template` | field | `std::string` | private | — |
| `d_mt_spinbox` | field | `QSpinBox` | private | — |
| `d_nt_spinbox` | field | `QSpinBox` | private | — |
| `d_help_dialog_configuration` | field | `InformationDialog` | private | — |
| `d_help_dialog_output` | field | `InformationDialog` | private | — |
| `d_open_directory_dialog` | field | `OpenDirectoryDialog` | private | — |
| `set_num_processors()` | method | `void` | private | — |
| `save_velocity_domain_file( const GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type &velocity_sub_domain, int processor_number)` | method | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `MT_PLACE_HOLDER` | variable | `std::string` | — |
| `NT_PLACE_HOLDER` | variable | `std::string` | — |
| `ND_PLACE_HOLDER` | variable | `std::string` | — |
| `NP_PLACE_HOLDER` | variable | `std::string` | — |
| `HELP_DIALOG_TITLE_CONFIGURATION` | variable | `char` | — |
| `HELP_DIALOG_TEXT_CONFIGURATION` | variable | `char` | — |
| `HELP_DIALOG_TITLE_OUTPUT` | variable | `char` | — |
| `HELP_DIALOG_TEXT_OUTPUT` | variable | `char` | — |
| `replace_place_holder( std::string &str, const std::string &place_holder, const std::string &replacement)` | function | `void` | Replace all occurrences of a place holder substring with its replacement substring. |
| `GENERATE_VELOCITY_DOMAIN_TERRA_DIALOG_H` | macro | `None` | — |

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
| `GenerateVelocityDomainTerraDialog` | `QDialog` | Generate Terra Velocity Domain Points | 20 |

**Qt signal/slot connections** (10 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_mt_spinbox` | `valueChanged(int)` | `this` | `handle_mt_value_changed(int)` |
| `d_nt_spinbox` | `valueChanged(int)` | `this` | `handle_nt_value_changed(int)` |
| `nd_spinbox` | `valueChanged(int)` | `this` | `handle_nd_value_changed(int)` |
| `button_path` | `clicked()` | `this` | `select_path()` |
| `lineEdit_path` | `editingFinished()` | `this` | `set_path()` |
| `lineEdit_file_template` | `editingFinished()` | `this` | `set_file_name_template()` |
| `pushButton_info_output` | `clicked()` | `d_help_dialog_output` | `show()` |
| `pushButton_info_configuration` | `clicked()` | `d_help_dialog_configuration` | `show()` |
| `main_buttonbox` | `accepted()` | `this` | `generate_velocity_domain()` |
| `main_buttonbox` | `rejected()` | `this` | `reject()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/GenerateVelocityDomainTerraDialog.h
python scripts/gpq.py def (anonymous)::PowerOfTwoSpinBox --body
python scripts/gpq.py uses PowerOfTwoSpinBox --kind class
python scripts/gpq.py hier PowerOfTwoSpinBox
```
