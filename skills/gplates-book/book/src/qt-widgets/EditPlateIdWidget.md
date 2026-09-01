# EditPlateIdWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1108 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditPlateIdWidget.h` | C++ | 162 |
| `src/qt-widgets/EditPlateIdWidget.cc` | C++ | 140 |
| `src/qt-widgets/EditPlateIdWidgetUi.ui` | Qt form | 77 |

## Overview

[[[PROSE overview unit=qt-widgets/EditPlateIdWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::EditPlateIdWidget`](#gplatesqtwidgetseditplateidwidget) | class | [`AbstractEditWidget`](AbstractEditWidget.md)<br>`Ui_EditPlateIdWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::EditPlateIdWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EditPlateIdWidget( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `reset_widget_to_default_values()` | method | `void` | public | — |
| `update_widget_from_plate_id( GPlatesPropertyValues::GpmlPlateId &gpml_plate_id)` | method | `void` | public | — |
| `create_property_value_from_widget()` | method | `GPlatesModel::PropertyValue::non_null_ptr_type` | public | — |
| `create_integer_plate_id_from_widget()` | method | `GPlatesModel::integer_plate_id_type` | public | — |
| `update_property_value_from_widget()` | method | `bool` | public | — |
| `supports_null_value()` | method | `bool` | public | Unique to EditPlateIdWidget is the ability to hold a 'None' or null value. |
| `permits_null_value()` | method | `bool` | public | — |
| `set_null_value_permitted( bool null_permitted)` | method | `void` | public | — |
| `is_null()` | method | `bool` | public | — |
| `set_null( bool should_nullify)` | method | `void` | public | — |
| `value_changed()` | method | `void` | public | — |
| `nullify()` | method | `void` | private | Triggered from button. |
| `handle_value_changed()` | method | `void` | private | — |
| `d_plate_id_ptr` | field | `boost::intrusive_ptr<GPlatesPropertyValues::GpmlPlateId>` | private | This boost::intrusive\_ptr is used to remember the property value which was last loaded into this editing widget. |
| `d_null_value_permitted` | field | `bool` | private | Whether we will allow the user to effectively select 'None' as the plate ID. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_EDITPLATEIDWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/EditPlateIdWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/CreateFeatureDialog](CreateFeatureDialog.md) | qt-widgets | 10 |
| [qt-widgets/GenerateDeformingMeshPointsDialog](GenerateDeformingMeshPointsDialog.md) | qt-widgets | 4 |
| [qt-widgets/EditWidgetGroupBox](EditWidgetGroupBox.md) | qt-widgets | 3 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `EditPlateIdWidget` | `QWidget` | Form | 4 |

**Qt signal/slot connections** (3 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `spinbox_plate_id` | `valueChanged(int)` | `this` | `set_dirty()` |
| `button_set_to_null` | `clicked()` | `this` | `nullify()` |
| `spinbox_plate_id` | `valueChanged(int)` | `this` | `handle_value_changed()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/EditPlateIdWidget.h
python scripts/gpq.py def GPlatesQtWidgets::EditPlateIdWidget --body
python scripts/gpq.py uses EditPlateIdWidget --kind class
python scripts/gpq.py hier EditPlateIdWidget
```
