# SetVGPVisibilityDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1015 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/SetVGPVisibilityDialog.h` | C++ | 109 |
| `src/qt-widgets/SetVGPVisibilityDialog.cc` | C++ | 329 |
| `src/qt-widgets/SetVGPVisibilityDialogUi.ui` | Qt form | 183 |

## Overview

A dialog for controlling Virtual Geomagnetic Pole (VGP) visibility in reconstruction layers. Users select between three visibility modes: always visible, visible within a time window (with optional distant past/future checkboxes), or visible within a delta-t interval around a specific geological age. Changes are reflected in the visual layer's parameters upon acceptance.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::SetVGPVisibilityDialog`](#gplatesqtwidgetssetvgpvisibilitydialog) | class | `QDialog`<br>`Ui_SetVGPVisibilityDialog` | — | 0 | Dialog to view and modify the ViewState's VGP parameters (currently handles both app-logic and visual parameters). |

## Members

### `GPlatesQtWidgets::SetVGPVisibilityDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SetVGPVisibilityDialog( GPlatesAppLogic::ApplicationState &application_state, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `populate( const boost::weak_ptr<GPlatesPresentation::VisualLayer> &visual_layer)` | method | `bool` | public | Causes the dialog to be populated with values from the given visual\_layer. |
| `handle_always_visible()` | method | `void` | private | — |
| `handle_time_window()` | method | `void` | private | — |
| `handle_delta_t()` | method | `void` | private | — |
| `handle_distant_past( bool state)` | method | `void` | private | — |
| `handle_distant_future( bool state)` | method | `void` | private | — |
| `handle_apply()` | method | `void` | private | — |
| `setup_connections()` | method | `void` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_current_visual_layer` | field | `boost::weak_ptr<GPlatesPresentation::VisualLayer>` | private | The visual layer for which we are currently displaying settings. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_SETVGPVISIBILITYDIALOG_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ReconstructLayerOptionsWidget](ReconstructLayerOptionsWidget.md) | qt-widgets | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `SetVGPVisibilityDialog` | `QDialog` | Set VGP Visibility | 16 |

**Qt signal/slot connections** (7 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `radiobutton_always_visible` | `clicked()` | `this` | `handle_always_visible()` |
| `radiobutton_time_window` | `clicked()` | `this` | `handle_time_window()` |
| `radiobutton_delta_t_around_age` | `clicked()` | `this` | `handle_delta_t()` |
| `checkbox_past` | `clicked(bool)` | `this` | `handle_distant_past(bool)` |
| `checkbox_future` | `clicked(bool)` | `this` | `handle_distant_future(bool)` |
| `main_buttonbox` | `accepted()` | `this` | `handle_apply()` |
| `main_buttonbox` | `rejected()` | `this` | `reject()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/SetVGPVisibilityDialog.h
python scripts/gpq.py def GPlatesQtWidgets::SetVGPVisibilityDialog --body
python scripts/gpq.py uses SetVGPVisibilityDialog --kind class
python scripts/gpq.py hier SetVGPVisibilityDialog
```
