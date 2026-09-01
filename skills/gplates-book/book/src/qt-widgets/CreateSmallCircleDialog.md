# CreateSmallCircleDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1106 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/CreateSmallCircleDialog.h` | C++ | 96 |
| `src/qt-widgets/CreateSmallCircleDialog.cc` | C++ | 304 |
| `src/qt-widgets/CreateSmallCircleDialogUi.ui` | Qt form | 510 |

## Overview

[[[PROSE overview unit=qt-widgets/CreateSmallCircleDialog tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=qt-widgets/CreateSmallCircleDialog tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
