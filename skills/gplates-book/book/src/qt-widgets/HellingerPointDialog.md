# HellingerPointDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 318 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/HellingerPointDialog.h` | C++ | 126 |
| `src/qt-widgets/HellingerPointDialog.cc` | C++ | 260 |
| `src/qt-widgets/HellingerPointDialogUi.ui` | Qt form | 260 |

## Overview

[[[PROSE overview unit=qt-widgets/HellingerPointDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::HellingerPointDialog`](#gplatesqtwidgetshellingerpointdialog) | class | `QDialog`<br>`Ui_HellingerPointDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::HellingerPointDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `HellingerPointDialog( HellingerDialog *hellinger_dialog, HellingerModel *hellinger_model, bool create_new_point = false)` | constructor | `None` | public | — |
| `update_pick_from_model( const int &segment, const int &row)` | method | `void` | public | — |
| `update_segment_number( const int &segment_number)` | method | `void` | public | — |
| `update_pick_coords( const GPlatesMaths::LatLonPoint &llp)` | method | `void` | public | — |
| `set_active( bool active)` | method | `void` | public | set\_active - disable dialog except for "close" button. |
| `current_pick` | field | `HellingerPick` | public | — |
| `begin_pick_operation( const double &lat = 0, const double &lon = 0)` | method | `void` | public | — |
| `finished_editing()` | method | `void` | public | — |
| `update_editing()` | method | `void` | public | — |
| `close()` | method | `void` | public | — |
| `reject()` | method | `void` | public | — |
| `handle_apply()` | method | `void` | private | — |
| `handle_pick_changed()` | method | `void` | private | — |
| `update_pick_from_widgets()` | method | `void` | private | — |
| `set_initial_values()` | method | `void` | private | — |
| `d_hellinger_dialog_ptr` | field | `HellingerDialog` | private | — |
| `d_hellinger_model_ptr` | field | `HellingerModel` | private | — |
| `d_segment` | field | `int` | private | — |
| `d_row` | field | `int` | private | — |
| `d_create_new_pick` | field | `bool` | private | — |
| `d_pick` | field | `HellingerPick` | private | — |
| `d_radio_button_group` | field | `QButtonGroup` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `INITIAL_UNCERTAINTY` | variable | `double` | — |
| `GPLATES_QTWIDGETS_HELLINGERPOINTDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/HellingerPointDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/HellingerDialog](HellingerDialog.md) | qt-widgets | 12 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `HellingerPointDialog` | `QDialog` | Dialog | 16 |

**Qt signal/slot connections** (7 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_apply` | `clicked()` | `this` | `handle_apply()` |
| `button_cancel` | `clicked()` | `this` | `close()` |
| `spinbox_lat` | `valueChanged(double)` | `this` | `handle_pick_changed()` |
| `spinbox_lon` | `valueChanged(double)` | `this` | `handle_pick_changed()` |
| `radio_plate_index_1` | `toggled(bool)` | `this` | `handle_pick_changed()` |
| `radio_plate_index_2` | `toggled(bool)` | `this` | `handle_pick_changed()` |
| `radio_plate_index_3` | `toggled(bool)` | `this` | `handle_pick_changed()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/HellingerPointDialog.h
python scripts/gpq.py def GPlatesQtWidgets::HellingerPointDialog --body
python scripts/gpq.py uses HellingerPointDialog --kind class
python scripts/gpq.py hier HellingerPointDialog
```
