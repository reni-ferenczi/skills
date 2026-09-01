# EditAngleWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1595 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditAngleWidget.h` | C++ | 84 |
| `src/qt-widgets/EditAngleWidget.cc` | C++ | 100 |
| `src/qt-widgets/EditAngleWidgetUi.ui` | Qt form | 70 |

## Overview

A simple edit widget for composing and modifying `GpmlMeasure` property values representing angles. Wraps a spin box for numeric input and maintains a reference-counted pointer to the edited measure value.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::EditAngleWidget`](#gplatesqtwidgetseditanglewidget) | class | [`AbstractEditWidget`](AbstractEditWidget.md)<br>`Ui_EditAngleWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::EditAngleWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EditAngleWidget( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `reset_widget_to_default_values()` | method | `void` | public | — |
| `update_widget_from_angle( GPlatesPropertyValues::GpmlMeasure &gpml_measure)` | method | `void` | public | — |
| `create_property_value_from_widget()` | method | `GPlatesModel::PropertyValue::non_null_ptr_type` | public | — |
| `update_property_value_from_widget()` | method | `bool` | public | — |
| `d_angle_ptr` | field | `boost::intrusive_ptr<GPlatesPropertyValues::GpmlMeasure>` | private | This boost::intrusive\_ptr is used to remember the property value which was last loaded into this editing widget. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_EDITANGLEWIDGET_H` | macro | `None` | — |

## Notes

The stored `d_angle_ptr` may be null: initially when the widget is created, or when editing newly-added properties not yet in the model. Code updating the property value must handle this case.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/EditWidgetGroupBox](EditWidgetGroupBox.md) | qt-widgets | 3 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `EditAngleWidget` | `QWidget` | Form | 3 |

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `spinbox_double` | `valueChanged(double)` | `this` | `set_dirty()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/EditAngleWidget.h
python scripts/gpq.py def GPlatesQtWidgets::EditAngleWidget --body
python scripts/gpq.py uses EditAngleWidget --kind class
python scripts/gpq.py hier EditAngleWidget
```
