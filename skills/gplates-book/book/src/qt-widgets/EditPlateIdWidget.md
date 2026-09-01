# EditPlateIdWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1108 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditPlateIdWidget.h` | C++ | 162 |
| `src/qt-widgets/EditPlateIdWidget.cc` | C++ | 140 |
| `src/qt-widgets/EditPlateIdWidgetUi.ui` | Qt form | 77 |

## Overview

A Qt widget for editing plate ID property values, with an uncommon extension: the ability to hold a null value. The widget presents a spin box for plate ID selection. Unlike most edit widgets, it supports an optional "None" state via `set_null_value_permitted()` and related methods, allowing callers to make null values optional (used in `CreateFeatureDialog` for conjugate plate IDs). When null is permitted, the widget shows -1 as a special "None" value in the spin box and displays a button to toggle the null state. It follows the `AbstractEditWidget` pattern but additionally emits a `value_changed()` signal when the value changes and provides `create_integer_plate_id_from_widget()` to return just the integer value.

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

The `d_plate_id_ptr` pointer can be NULL when adding new properties. Calling any of `create_property_value_from_widget()`, `create_integer_plate_id_from_widget()`, or `update_property_value_from_widget()` on a null or uninitialized widget throws `UninitialisedEditWidgetException`. The null state is represented as -1 and is only meaningful when null values are permitted via `set_null_value_permitted(true)`. The spin box range is 0 to 2^31-1 (max signed 32-bit), or -1 to 2^31-1 when null is permitted. Always call `set_null_value_permitted()` before initializing the widget if null values should be supported.

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
