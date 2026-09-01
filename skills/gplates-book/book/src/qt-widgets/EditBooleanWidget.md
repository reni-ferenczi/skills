# EditBooleanWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1107 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditBooleanWidget.h` | C++ | 93 |
| `src/qt-widgets/EditBooleanWidget.cc` | C++ | 106 |
| `src/qt-widgets/EditBooleanWidgetUi.ui` | Qt form | 52 |

## Overview

[[[PROSE overview unit=qt-widgets/EditBooleanWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::EditBooleanWidget`](#gplatesqtwidgetseditbooleanwidget) | class | [`AbstractEditWidget`](AbstractEditWidget.md)<br>`Ui_EditBooleanWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::EditBooleanWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EditBooleanWidget( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `reset_widget_to_default_values()` | method | `void` | public | — |
| `update_widget_from_boolean( GPlatesPropertyValues::XsBoolean &xs_boolean)` | method | `void` | public | — |
| `create_property_value_from_widget()` | method | `GPlatesModel::PropertyValue::non_null_ptr_type` | public | — |
| `update_property_value_from_widget()` | method | `bool` | public | — |
| `handle_combobox_change()` | method | `void` | private | — |
| `d_boolean_ptr` | field | `boost::intrusive_ptr<GPlatesPropertyValues::XsBoolean>` | private | This boost::intrusive\_ptr is used to remember the property value which was last loaded into this editing widget. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_EDITBOOLEANWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/EditBooleanWidget tier=3]]]
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
| `EditBooleanWidget` | `QWidget` | Form | 3 |

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `combobox_boolean` | `activated(int)` | `this` | `handle_combobox_change()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/EditBooleanWidget.h
python scripts/gpq.py def GPlatesQtWidgets::EditBooleanWidget --body
python scripts/gpq.py uses EditBooleanWidget --kind class
python scripts/gpq.py hier EditBooleanWidget
```
