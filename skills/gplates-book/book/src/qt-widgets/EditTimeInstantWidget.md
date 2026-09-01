# EditTimeInstantWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 878 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditTimeInstantWidget.h` | C++ | 85 |
| `src/qt-widgets/EditTimeInstantWidget.cc` | C++ | 109 |
| `src/qt-widgets/EditTimeInstantWidgetUi.ui` | Qt form | 68 |

## Overview

[[[PROSE overview unit=qt-widgets/EditTimeInstantWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::EditTimeInstantWidget`](#gplatesqtwidgetsedittimeinstantwidget) | class | [`AbstractEditWidget`](AbstractEditWidget.md)<br>`Ui_EditTimeInstantWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::EditTimeInstantWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EditTimeInstantWidget( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `reset_widget_to_default_values()` | method | `void` | public | — |
| `update_widget_from_time_instant( GPlatesPropertyValues::GmlTimeInstant &gml_time_instant)` | method | `void` | public | — |
| `create_property_value_from_widget()` | method | `GPlatesModel::PropertyValue::non_null_ptr_type` | public | — |
| `update_property_value_from_widget()` | method | `bool` | public | — |
| `d_time_instant_ptr` | field | `boost::intrusive_ptr<GPlatesPropertyValues::GmlTimeInstant>` | private | This boost::intrusive\_ptr is used to remember the property value which was last loaded into this editing widget. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `create_geo_time_instant_from_widget( QDoubleSpinBox *spinbox)` | function | `GPlatesPropertyValues::GeoTimeInstant` | — |
| `GPLATES_QTWIDGETS_EDITTIMEINSTANTWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/EditTimeInstantWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/EditWidgetGroupBox](EditWidgetGroupBox.md) | qt-widgets | 3 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `EditTimeInstantWidget` | `QWidget` | Form | 4 |

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `spinbox_time_position` | `valueChanged(double)` | `this` | `set_dirty()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/EditTimeInstantWidget.h
python scripts/gpq.py def GPlatesQtWidgets::EditTimeInstantWidget --body
python scripts/gpq.py uses EditTimeInstantWidget --kind class
python scripts/gpq.py hier EditTimeInstantWidget
```
