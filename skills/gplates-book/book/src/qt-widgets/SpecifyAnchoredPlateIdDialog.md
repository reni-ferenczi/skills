# SpecifyAnchoredPlateIdDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 656 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/SpecifyAnchoredPlateIdDialog.h` | C++ | 102 |
| `src/qt-widgets/SpecifyAnchoredPlateIdDialog.cc` | C++ | 224 |
| `src/qt-widgets/SpecifyAnchoredPlateIdDialogUi.ui` | Qt form | 129 |

## Overview

[[[PROSE overview unit=qt-widgets/SpecifyAnchoredPlateIdDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::ExtractPlateIds`](#anonymousextractplateids) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | — |
| [`GPlatesQtWidgets::SpecifyAnchoredPlateIdDialog`](#gplatesqtwidgetsspecifyanchoredplateiddialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_SpecifyAnchoredPlateIdDialog` | — | 0 | — |

## Members

### `(anonymous)::ExtractPlateIds`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `result_type` | typedef | `std::map<QString, GPlatesModel::integer_plate_id_type>` | public | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | public | — |
| `visit_gpml_plate_id( const GPlatesPropertyValues::GpmlPlateId &gpml_plate_id)` | method | `void` | public | — |
| `d_plate_ids` | field | `result_type` | private | — |

### `GPlatesQtWidgets::SpecifyAnchoredPlateIdDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SpecifyAnchoredPlateIdDialog( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `populate( GPlatesModel::integer_plate_id_type plate_id, const GPlatesModel::FeatureHandle::weak_ref &focused_feature)` | method | `void` | public | Call this function before showing the dialog to repopulate its fields with the latest values. |
| `showEvent( QShowEvent *ev)` | method | `void` | protected | — |
| `propagate_value()` | method | `void` | private | — |
| `handle_action_triggered( QAction *action)` | method | `void` | private | — |
| `reset_to_zero()` | method | `void` | private | — |
| `value_changed( GPlatesModel::integer_plate_id_type new_value)` | method | `void` | public | — |
| `populate_spinbox( GPlatesModel::integer_plate_id_type plate_id)` | method | `void` | private | — |
| `populate_menu( const GPlatesModel::FeatureHandle::weak_ref &focused_feature)` | method | `void` | private | — |
| `d_fill_menu` | field | `QMenu` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_SPECIFYANCHOREDPLATEIDDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/SpecifyAnchoredPlateIdDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Dialogs](../gui/Dialogs.md) | gui | 1 |
| [presentation/Application](../presentation/Application.md) | presentation | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `SpecifyAnchoredPlateIdDialog` | `QDialog` | Specify Anchored Plate ID | 7 |

**Qt signal/slot connections** (5 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_fill_menu` | `triggered(QAction *)` | `this` | `handle_action_triggered(QAction *)` |
| `main_buttonbox` | `accepted()` | `this` | `accept()` |
| `main_buttonbox` | `rejected()` | `this` | `reject()` |
| `this` | `accepted()` | `this` | `propagate_value()` |
| `reset_button` | `clicked()` | `this` | `reset_to_zero()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/SpecifyAnchoredPlateIdDialog.h
python scripts/gpq.py def GPlatesQtWidgets::SpecifyAnchoredPlateIdDialog --body
python scripts/gpq.py uses SpecifyAnchoredPlateIdDialog --kind class
python scripts/gpq.py hier SpecifyAnchoredPlateIdDialog
```
