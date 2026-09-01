# EditDoubleWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1160 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditDoubleWidget.h` | C++ | 85 |
| `src/qt-widgets/EditDoubleWidget.cc` | C++ | 91 |
| `src/qt-widgets/EditDoubleWidgetUi.ui` | Qt form | 64 |

## Overview

[[[PROSE overview unit=qt-widgets/EditDoubleWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=qt-widgets/EditDoubleWidget tier=3]]]
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
