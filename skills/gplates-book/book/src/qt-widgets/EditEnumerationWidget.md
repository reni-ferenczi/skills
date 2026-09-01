# EditEnumerationWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1331 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditEnumerationWidget.h` | C++ | 109 |
| `src/qt-widgets/EditEnumerationWidget.cc` | C++ | 208 |
| `src/qt-widgets/EditEnumerationWidgetUi.ui` | Qt form | 52 |

## Overview

[[[PROSE overview unit=qt-widgets/EditEnumerationWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::EditEnumerationWidget`](#gplatesqtwidgetseditenumerationwidget) | class | [`AbstractEditWidget`](AbstractEditWidget.md)<br>`Ui_EditEnumerationWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::EditEnumerationWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EditEnumerationWidget( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `configure_for_property_value_type( const GPlatesPropertyValues::StructuralType &property_value_type)` | method | `void` | public | — |
| `reset_widget_to_default_values()` | method | `void` | public | — |
| `update_widget_from_enumeration( GPlatesPropertyValues::Enumeration &enumeration)` | method | `void` | public | — |
| `create_property_value_from_widget()` | method | `GPlatesModel::PropertyValue::non_null_ptr_type` | public | — |
| `update_property_value_from_widget()` | method | `bool` | public | — |
| `handle_combobox_change()` | method | `void` | private | — |
| `d_property_value_type` | field | `boost::optional<GPlatesPropertyValues::StructuralType>` | private | The type of the PropertyValue which this widget is currently configured to produce. |
| `d_enumeration_ptr` | field | `boost::intrusive_ptr<GPlatesPropertyValues::Enumeration>` | private | This boost::intrusive\_ptr is used to remember the property value which was last loaded into this editing widget. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `is_property_value_type_handled( const GPlatesPropertyValues::StructuralType &property_value_type)` | function | `bool` | Query GPGIM to see if the specified property value type is a recognised enumeration type. |
| `get_enumeration_string_list( const GPlatesPropertyValues::StructuralType &property_value_type)` | function | `QStringList` | Retrieve the list of allowed enumeration values for the specified property (enumeration) type. |
| `GPLATES_QTWIDGETS_EDITENUMERATIONWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/EditEnumerationWidget tier=3]]]
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
| `EditEnumerationWidget` | `QWidget` | Form | 3 |

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `combobox_enumeration` | `activated(int)` | `this` | `handle_combobox_change()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/EditEnumerationWidget.h
python scripts/gpq.py def GPlatesQtWidgets::EditEnumerationWidget --body
python scripts/gpq.py uses EditEnumerationWidget --kind class
python scripts/gpq.py hier EditEnumerationWidget
```
