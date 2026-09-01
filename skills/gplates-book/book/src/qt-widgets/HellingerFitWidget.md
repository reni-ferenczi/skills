# HellingerFitWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 155 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/HellingerFitWidget.h` | C++ | 253 |
| `src/qt-widgets/HellingerFitWidget.cc` | C++ | 648 |
| `src/qt-widgets/HellingerFitWidgetUi.ui` | Qt form | 1213 |

## Overview

`HellingerFitWidget` is the "fit" tab of `HellingerDialog`: it exposes the fitting parameters — search radius, grid search toggle, confidence limit, per-pair initial pole estimates (`estimate_12()`/`estimate_13()`), and the "amoeba" (downhill-simplex) stopping criteria, either a residual tolerance or an iteration limit — and shows the fitted poles and uncertainty ellipses the underlying computation produces. `update_fit_widgets_from_model()` and `update_model_from_fit_widgets()` are the two directions of syncing with `HellingerModel`; this widget never mutates `HellingerModel` itself outside those calls. It talks to its owning `HellingerDialog` both directly (`d_hellinger_dialog_ptr`, e.g. to trigger `handle_calculate_fit()`) and via `pole_estimate_12_changed`/`pole_estimate_13_changed` signals that let the dialog keep the on-canvas pole-estimate markers in sync as the spin boxes change.

Two/three-way fitting is a mode switch: `enable_three_way_widgets()`/`show_three_way_widgets()` add the third plate's controls (the "13" and "23" pair estimates/results) when `d_three_way_fitting_is_enabled`, keeping the same widget usable for the simpler two-plate case.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::HellingerFitWidget`](#gplatesqtwidgetshellingerfitwidget) | class | `QWidget`<br>`Ui_HellingerFitWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::HellingerFitWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `HellingerFitWidget( HellingerDialog *hellinger_dialog, HellingerModel *hellinger_model)` | constructor | `None` | public | — |
| `~HellingerFitWidget()` | destructor | `None` | public | — |
| `update_fit_widgets_from_model()` | method | `void` | public | update\_from\_model - update the initial guess spinboxes and fit-related info from the Hellinger model. |
| `update_model_from_fit_widgets()` | method | `void` | public | update\_model\_from\_fit\_related\_data - update the HellingerModel's fit-related input data from the widget. |
| `update_after_switching_tabs()` | method | `void` | public | — |
| `update_enabled_state_of_estimate_widgets( bool adjust_pole_tool_is_active = false)` | method | `void` | public | — |
| `update_after_pole_result()` | method | `void` | public | — |
| `start_progress_bar()` | method | `void` | public | — |
| `stop_progress_bar()` | method | `void` | public | — |
| `show_result_12_checked()` | method | `bool` | public | — |
| `show_result_13_checked()` | method | `bool` | public | — |
| `show_result_23_checked()` | method | `bool` | public | — |
| `show_estimate_12_checked()` | method | `bool` | public | — |
| `show_estimate_13_checked()` | method | `bool` | public | — |
| `estimate_12()` | method | `HellingerPoleEstimate` | public | — |
| `set_estimate_12( const HellingerPoleEstimate &estimate)` | method | `void` | public | — |
| `set_estimate_13( const HellingerPoleEstimate &estimate)` | method | `void` | public | — |
| `estimate_13()` | method | `HellingerPoleEstimate` | public | — |
| `enable_pole_estimate_widgets( bool enable)` | method | `void` | public | — |
| `update_buttons()` | method | `void` | public | — |
| `pole_estimate_12_changed(double,double)` | method | `void` | public | — |
| `pole_estimate_13_changed(double, double)` | method | `void` | public | — |
| `pole_estimate_12_angle_changed(double)` | method | `void` | public | — |
| `pole_estimate_13_angle_changed(double)` | method | `void` | public | — |
| `show_result_checkboxes_clicked()` | method | `void` | public | — |
| `show_estimate_checkboxes_clicked()` | method | `void` | public | — |
| `handle_checkbox_grid_search_changed()` | method | `void` | private | — |
| `handle_spinbox_radius_changed()` | method | `void` | private | — |
| `handle_spinbox_confidence_changed()` | method | `void` | private | — |
| `handle_pole_estimate_12_angle_changed()` | method | `void` | private | — |
| `handle_pole_estimate_13_angle_changed()` | method | `void` | private | — |
| `handle_pole_estimate_12_lat_lon_changed()` | method | `void` | private | — |
| `handle_pole_estimate_13_lat_lon_changed()` | method | `void` | private | — |
| `handle_show_result_checkboxes_clicked()` | method | `void` | private | — |
| `handle_show_estimate_checkboxes_clicked()` | method | `void` | private | — |
| `handle_clipboard_12_clicked()` | method | `void` | private | — |
| `handle_clipboard_13_clicked()` | method | `void` | private | — |
| `handle_clipboard_23_clicked()` | method | `void` | private | — |
| `handle_amoeba_iterations_checked()` | method | `void` | private | — |
| `handle_amoeba_residual_checked()` | method | `void` | private | — |
| `handle_amoeba_iterations_changed()` | method | `void` | private | — |
| `handle_amoeba_residual_changed()` | method | `void` | private | — |
| `initialise_widgets()` | method | `void` | private | — |
| `set_up_connections()` | method | `void` | private | — |
| `enable_three_way_widgets( bool enable)` | method | `void` | private | — |
| `show_three_way_widgets( bool show)` | method | `void` | private | — |
| `d_hellinger_dialog_ptr` | field | `HellingerDialog` | private | — |
| `d_hellinger_model_ptr` | field | `HellingerModel` | private | — |
| `d_pole_has_been_calculated` | field | `bool` | private | — |
| `d_amoeba_residual_ok` | field | `bool` | private | — |
| `d_default_palette` | field | `QPalette` | private | d\_default\_palette - a default palette used for resetting widget backgrounds. |
| `d_red_palette` | field | `QPalette` | private | d\_red\_palette - a red-background palette used to warn of invalid widget data. |
| `d_last_used_two_way_tolerance` | field | `double` | private | — |
| `d_last_used_three_way_tolerance` | field | `double` | private | — |
| `d_three_way_fitting_is_enabled` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `INITIAL_SEARCH_RADIUS` | variable | `double` | — |
| `INITIAL_SIGNIFICANCE_LEVEL` | variable | `double` | — |
| `INITIAL_ROTATION_ANGLE` | variable | `double` | — |
| `GPLATES_QTWIDGETS_HELLINGERFITWIDGET_H` | macro | `None` | — |

## Notes

`d_hellinger_dialog_ptr` and `d_hellinger_model_ptr` are non-owning; both are constructed and owned by `HellingerDialog`, which outlives this widget. `d_red_palette` is swapped onto a field's palette to flag invalid input (e.g. an unparsable amoeba tolerance) and must be restored from `d_default_palette` once the value becomes valid again — there is no automatic reset.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/HellingerDialog](HellingerDialog.md) | qt-widgets | 26 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `HellingerFitWidget` | `QWidget` | Form | 62 |

**Qt signal/slot connections** (24 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_calculate_fit` | `clicked()` | `d_hellinger_dialog_ptr` | `handle_calculate_fit()` |
| `button_calculate_uncertainties` | `clicked()` | `d_hellinger_dialog_ptr` | `handle_calculate_uncertainties()` |
| `button_show_details` | `clicked()` | `d_hellinger_dialog_ptr` | `handle_show_details()` |
| `spinbox_radius` | `valueChanged(double)` | `this` | `handle_spinbox_radius_changed()` |
| `spinbox_conf_limit` | `valueChanged(double)` | `this` | `handle_spinbox_confidence_changed()` |
| `checkbox_grid_search` | `clicked()` | `this` | `handle_checkbox_grid_search_changed()` |
| `spinbox_lat_estimate_12` | `valueChanged(double)` | `this` | `handle_pole_estimate_12_lat_lon_changed()` |
| `spinbox_lon_estimate_12` | `valueChanged(double)` | `this` | `handle_pole_estimate_12_lat_lon_changed()` |
| `spinbox_rho_estimate_12` | `valueChanged(double)` | `this` | `handle_pole_estimate_12_angle_changed()` |
| `spinbox_lat_estimate_13` | `valueChanged(double)` | `this` | `handle_pole_estimate_13_lat_lon_changed()` |
| `spinbox_lon_estimate_13` | `valueChanged(double)` | `this` | `handle_pole_estimate_13_lat_lon_changed()` |
| `spinbox_rho_estimate_13` | `valueChanged(double)` | `this` | `handle_pole_estimate_13_angle_changed()` |
| `checkbox_show_result_12` | `clicked()` | `this` | `handle_show_result_checkboxes_clicked()` |
| `checkbox_show_result_13` | `clicked()` | `this` | `handle_show_result_checkboxes_clicked()` |
| `checkbox_show_result_23` | `clicked()` | `this` | `handle_show_result_checkboxes_clicked()` |

*... and 9 more connections.*


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/HellingerFitWidget.h
python scripts/gpq.py def GPlatesQtWidgets::HellingerFitWidget --body
python scripts/gpq.py uses HellingerFitWidget --kind class
python scripts/gpq.py hier HellingerFitWidget
```
