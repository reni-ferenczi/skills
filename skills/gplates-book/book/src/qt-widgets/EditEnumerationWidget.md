# EditEnumerationWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1331 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditEnumerationWidget.h` | C++ | 109 |
| `src/qt-widgets/EditEnumerationWidget.cc` | C++ | 208 |
| `src/qt-widgets/EditEnumerationWidgetUi.ui` | Qt form | 52 |

## Overview

A Qt widget for editing enumeration property values of multiple types. Unlike the type-specific edit widgets, this single widget can be configured via `configure_for_property_value_type()` to handle any enumeration type defined in the GPGIM. The widget uses a combo box populated with the valid enumeration values for the configured type. It follows the `AbstractEditWidget` pattern: initialize via `configure_for_property_value_type()` or `update_widget_from_enumeration()`, edit the selection, then create or update the property value. The widget tolerantly preserves unknown enum values if a property is loaded with a value not in the GPGIM definition, adding it to the combo box rather than losing data.

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

Must be configured for a property value type before use via `configure_for_property_value_type()` (which throws `PropertyValueNotSupportedException` if the type is not a valid enumeration). The `d_property_value_type` is optional and will be NULL until configured. The `d_enumeration_ptr` can be NULL when adding new properties; calling `update_property_value_from_widget()` on an uninitialized widget throws `UninitialisedEditWidgetException`. Calling `create_property_value_from_widget()` without a configured type also throws `PropertyValueNotSupportedException`.

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
