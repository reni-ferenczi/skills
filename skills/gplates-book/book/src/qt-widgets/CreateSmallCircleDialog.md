# CreateSmallCircleDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1106 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/CreateSmallCircleDialog.h` | C++ | 96 |
| `src/qt-widgets/CreateSmallCircleDialog.cc` | C++ | 304 |
| `src/qt-widgets/CreateSmallCircleDialogUi.ui` | Qt form | 510 |

## Overview

`CreateSmallCircleDialog` lets the user add one or a family of small circles
(latitude/longitude parallels around an arbitrary centre) to a `SmallCircleWidget`,
which owns the resulting collection. It supports two independent ways of choosing
the centre: type latitude/longitude directly, or check "stage pole" and let
`handle_calculate()` derive the centre from the stage rotation between two plate
IDs at two reconstruction times, computed through `RotationUtils::get_stage_pole()`
against the `ReconstructionTree`s for those times and converted to a
`GPlatesMaths::LatLonPoint` via the file-local `get_axis_llp_from_rotation()`. The
radius can likewise be a single value or a range (start/stop/step), stepped over
in `handle_preview()` to build a `GPlatesMaths::SmallCircle` per radius; `radio_button_single`
and `radio_button_multiple` toggle which set of spin boxes is enabled.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::CreateSmallCircleDialog`](#gplatesqtwidgetscreatesmallcircledialog) | class | `QDialog`<br>`Ui_CreateSmallCircleDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::CreateSmallCircleDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CreateSmallCircleDialog( GPlatesQtWidgets::SmallCircleWidget *small_circle_widget, GPlatesAppLogic::ApplicationState &application_state, QWidget *parent)` | constructor | `None` | public | — |
| `init()` | method | `void` | public | — |
| `handle_stage_pole_checkbox_state()` | method | `void` | private | — |
| `handle_calculate()` | method | `void` | private | — |
| `handle_preview()` | method | `void` | private | — |
| `handle_single_changed( bool state)` | method | `void` | private | — |
| `handle_multiple_changed( bool state)` | method | `void` | private | — |
| `handle_multiple_circle_fields_changed()` | method | `void` | private | — |
| `set_multiple_circle_field_colours( const QColor &color)` | method | `void` | private | — |
| `highlight_invalid_radius_fields()` | method | `void` | private | — |
| `d_small_circle_widget_ptr` | field | `SmallCircleWidget` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `set_widget_background_colour( QWidget *widget, const QColor &colour)` | function | `void` | — |
| `fields_are_valid( double r1, double r2, double dr)` | function | `bool` | Check that the entered mulitple-radii fields make sense. |
| `get_axis_llp_from_rotation( const GPlatesMaths::FiniteRotation &rotation)` | function | `GPlatesMaths::LatLonPoint` | — |
| `GPLATES_QTWIDGETS_CREATESMALLCIRCLEDIALOG_H` | macro | `None` | — |

## Notes

`handle_preview()` silently does nothing for the "multiple" case when
`fields_are_valid()` rejects the range (non-positive radius, non-positive step, or
end before start) beyond calling `highlight_invalid_radius_fields()` to turn the
radius fields red; it does not stop the "single" circle (if also requested) from
being added. The dialog is deliberately left open after `handle_preview()` adds
circles (a `// FIXME` notes this may be revisited) rather than closing on each
addition. `init()` must be called after construction to seed `spinbox_time_1` with
the current reconstruction time; it is not called from the constructor.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/deprecated/SmallCircleManager](deprecated/SmallCircleManager.md) | qt-widgets | 14 |
| [qt-widgets/SmallCircleWidget](SmallCircleWidget.md) | qt-widgets | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `CreateSmallCircleDialog` | `QDialog` | Create Small Circles | 29 |

**Qt signal/slot connections** (8 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `checkbox_stage_pole` | `stateChanged(int)` | `this` | `handle_stage_pole_checkbox_state()` |
| `button_calculate_stage_pole` | `clicked()` | `this` | `handle_calculate()` |
| `button_preview` | `clicked()` | `this` | `handle_preview()` |
| `radio_button_single` | `toggled(bool)` | `this` | `handle_single_changed(bool)` |
| `radio_button_multiple` | `toggled(bool)` | `this` | `handle_multiple_changed(bool)` |
| `spinbox_radius_1` | `valueChanged(double)` | — | `handle_multiple_circle_fields_changed()` |
| `spinbox_radius_2` | `valueChanged(double)` | — | `handle_multiple_circle_fields_changed()` |
| `spinbox_step` | `valueChanged(double)` | — | `handle_multiple_circle_fields_changed()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/CreateSmallCircleDialog.h
python scripts/gpq.py def GPlatesQtWidgets::CreateSmallCircleDialog --body
python scripts/gpq.py uses CreateSmallCircleDialog --kind class
python scripts/gpq.py hier CreateSmallCircleDialog
```
