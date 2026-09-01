# EditDoubleWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1160 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditDoubleWidget.h` | C++ | 85 |
| `src/qt-widgets/EditDoubleWidget.cc` | C++ | 91 |
| `src/qt-widgets/EditDoubleWidgetUi.ui` | Qt form | 64 |

## Overview

A Qt widget for editing double-precision floating-point property values. The widget presents a spin box to the user for fine-grained numeric input and adjustment. Following the `AbstractEditWidget` pattern, it can be initialized with an `XsDouble` property value, edited by the user, and then either create a new property value via `create_property_value_from_widget()` or update the existing one via `update_property_value_from_widget()`. Each change to the spin box triggers the dirty flag and emits `commit_me()` to notify the containing dialog.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::EditDoubleWidget`](#gplatesqtwidgetseditdoublewidget) | class | [`AbstractEditWidget`](AbstractEditWidget.md)<br>`Ui_EditDoubleWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::EditDoubleWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EditDoubleWidget( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `reset_widget_to_default_values()` | method | `void` | public | — |
| `update_widget_from_double( GPlatesPropertyValues::XsDouble &xs_double)` | method | `void` | public | — |
| `create_property_value_from_widget()` | method | `GPlatesModel::PropertyValue::non_null_ptr_type` | public | — |
| `update_property_value_from_widget()` | method | `bool` | public | — |
| `d_double_ptr` | field | `boost::intrusive_ptr<GPlatesPropertyValues::XsDouble>` | private | This boost::intrusive\_ptr is used to remember the property value which was last loaded into this editing widget. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_EDITDOUBLEWIDGET_H` | macro | `None` | — |

## Notes

The `d_double_ptr` pointer can be NULL when adding new properties (as opposed to editing existing ones). Calling `update_property_value_from_widget()` on an uninitialized widget throws `UninitialisedEditWidgetException`; ensure the widget is either initialized via `update_widget_from_double()` or used only for creating new properties.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/EditWidgetGroupBox](EditWidgetGroupBox.md) | qt-widgets | 3 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `EditDoubleWidget` | `QWidget` | Form | 3 |

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `spinbox_double` | `valueChanged(double)` | `this` | `set_dirty()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/EditDoubleWidget.h
python scripts/gpq.py def GPlatesQtWidgets::EditDoubleWidget --body
python scripts/gpq.py uses EditDoubleWidget --kind class
python scripts/gpq.py hier EditDoubleWidget
```
