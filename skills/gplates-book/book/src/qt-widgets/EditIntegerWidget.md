# EditIntegerWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1161 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditIntegerWidget.h` | C++ | 85 |
| `src/qt-widgets/EditIntegerWidget.cc` | C++ | 92 |
| `src/qt-widgets/EditIntegerWidgetUi.ui` | Qt form | 61 |

## Overview

A Qt widget for editing integer property values. The widget presents a spin box for numeric input and adjustment. Following the `AbstractEditWidget` pattern, it can be initialized with an `XsInteger` property value, edited by the user, and then either create a new property value via `create_property_value_from_widget()` or update the existing one via `update_property_value_from_widget()`. Each change to the spin box triggers the dirty flag and signals the containing dialog.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::EditIntegerWidget`](#gplatesqtwidgetseditintegerwidget) | class | [`AbstractEditWidget`](AbstractEditWidget.md)<br>`Ui_EditIntegerWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::EditIntegerWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EditIntegerWidget( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `reset_widget_to_default_values()` | method | `void` | public | — |
| `update_widget_from_integer( GPlatesPropertyValues::XsInteger &xs_integer)` | method | `void` | public | — |
| `create_property_value_from_widget()` | method | `GPlatesModel::PropertyValue::non_null_ptr_type` | public | — |
| `update_property_value_from_widget()` | method | `bool` | public | — |
| `d_integer_ptr` | field | `boost::intrusive_ptr<GPlatesPropertyValues::XsInteger>` | private | This boost::intrusive\_ptr is used to remember the property value which was last loaded into this editing widget. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_EDITINTEGERWIDGET_H` | macro | `None` | — |

## Notes

The `d_integer_ptr` pointer can be NULL when adding new properties (as opposed to editing existing ones). Calling `update_property_value_from_widget()` on an uninitialized widget throws `UninitialisedEditWidgetException`; ensure the widget is either initialized via `update_widget_from_integer()` or used only for creating new properties.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/EditWidgetGroupBox](EditWidgetGroupBox.md) | qt-widgets | 3 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `EditIntegerWidget` | `QWidget` | Form | 3 |

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `spinbox_integer` | `valueChanged(int)` | `this` | `set_dirty()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/EditIntegerWidget.h
python scripts/gpq.py def GPlatesQtWidgets::EditIntegerWidget --body
python scripts/gpq.py uses EditIntegerWidget --kind class
python scripts/gpq.py hier EditIntegerWidget
```
