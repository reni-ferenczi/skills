# EditStringWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1448 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditStringWidget.h` | C++ | 94 |
| `src/qt-widgets/EditStringWidget.cc` | C++ | 106 |
| `src/qt-widgets/EditStringWidgetUi.ui` | Qt form | 82 |

## Overview

A simple editor widget for `XsString` property values (XML schema strings). The widget provides a line edit for entering the string value. A code-space selector is defined in the form but remains hidden; support for editing the code-space attribute is not yet implemented (marked FIXME). The widget follows the standard `AbstractEditWidget` pattern for loading, editing, and committing string values.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::EditStringWidget`](#gplatesqtwidgetseditstringwidget) | class | [`AbstractEditWidget`](AbstractEditWidget.md)<br>`Ui_EditStringWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::EditStringWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EditStringWidget( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `reset_widget_to_default_values()` | method | `void` | public | — |
| `update_widget_from_string( GPlatesPropertyValues::XsString &xs_string)` | method | `void` | public | — |
| `create_property_value_from_widget()` | method | `GPlatesModel::PropertyValue::non_null_ptr_type` | public | — |
| `update_property_value_from_widget()` | method | `bool` | public | — |
| `get_string()` | method | `QString` | public | Return a copy of the string from the QLineEdit widget. |
| `d_string_ptr` | field | `boost::intrusive_ptr<GPlatesPropertyValues::XsString>` | private | This boost::intrusive\_ptr is used to remember the property value which was last loaded into this editing widget. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_EDITSTRINGWIDGET_H` | macro | `None` | — |

## Notes

Calling `update_property_value_from_widget()` before loading a string with `update_widget_from_string()` throws `UninitialisedEditWidgetException`.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/EditWidgetGroupBox](EditWidgetGroupBox.md) | qt-widgets | 3 |
| [qt-widgets/GenerateDeformingMeshPointsDialog](GenerateDeformingMeshPointsDialog.md) | qt-widgets | 3 |
| [qt-widgets/CreateFeatureDialog](CreateFeatureDialog.md) | qt-widgets | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `EditStringWidget` | `QWidget` | Form | 5 |

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `combobox_code_space` | `activated(int)` | `this` | `set_dirty()` |
| `line_edit` | `textEdited(const QString &)` | `this` | `set_dirty()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/EditStringWidget.h
python scripts/gpq.py def GPlatesQtWidgets::EditStringWidget --body
python scripts/gpq.py uses EditStringWidget --kind class
python scripts/gpq.py hier EditStringWidget
```
