# EditShapefileAttributesWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditShapefileAttributesWidget.h` | C++ | 92 |
| `src/qt-widgets/EditShapefileAttributesWidget.cc` | C++ | 247 |
| `src/qt-widgets/EditShapefileAttributesWidgetUi.ui` | Qt form | 190 |

## Overview

An editor widget for `GpmlKeyValueDictionary` property values, which store shapefile attributes as key-value pairs with typed values (integer, double, or string). The widget displays the dictionary as a three-column table: the first two columns (key and type) are read-only, and the third column (value) is editable. When a user edits a value cell, the widget validates the input against the value's declared type, updates the dictionary if valid, or reverts the cell if invalid. Unlike most edit widgets, this one commits changes immediately by emitting `commit_me()` on each cell edit.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::KeyValueColumnLayout`](#anonymouskeyvaluecolumnlayout) | enum | — | — | 0 | — |
| [`GPlatesQtWidgets::EditShapefileAttributesWidget`](#gplatesqtwidgetseditshapefileattributeswidget) | class | [`AbstractEditWidget`](AbstractEditWidget.md)<br>`Ui_EditShapefileAttributesWidget` | — | 0 | — |

## Members

### `(anonymous)::KeyValueColumnLayout`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `COLUMN_KEY` | enumerator | `None` | — | — |
| `COLUMN_TYPE` | enumerator | `None` | — | — |
| `COLUMN_VALUE` | enumerator | `None` | — | — |

### `GPlatesQtWidgets::EditShapefileAttributesWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EditShapefileAttributesWidget( QWidget *parent_=NULL)` | constructor | `None` | public | — |
| `reset_widget_to_default_values()` | method | `void` | public | — |
| `create_property_value_from_widget()` | method | `GPlatesModel::PropertyValue::non_null_ptr_type` | public | — |
| `update_property_value_from_widget()` | method | `bool` | public | — |
| `update_widget_from_key_value_dictionary( GPlatesPropertyValues::GpmlKeyValueDictionary &gpml_key_value_dictionary)` | method | `void` | public | — |
| `handle_cell_changed( int row, int column)` | method | `void` | private | Handle the content of a cell changing. |
| `d_key_value_dictionary_ptr` | field | `boost::intrusive_ptr<GPlatesPropertyValues::GpmlKeyValueDictionary>` | private | This boost::intrusive\_ptr is used to remember the property value which was last loaded into this editing widget. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_type_qstring_from_qvariant( QVariant &variant)` | function | `QString` | — |
| `GPLATES_QTWIDGETS_EDITSHAPEFILEATTRIBUTESWIDGET_H` | macro | `None` | — |

## Notes

Calling `update_property_value_from_widget()` before loading a dictionary with `update_widget_from_key_value_dictionary()` throws `UninitialisedEditWidgetException`. Invalid cell edits (e.g. non-integer input for an integer value) are silently rejected — the cell reverts to its prior value. The widget emits `commit_me()` on each value cell change, committing immediately rather than deferring to an overall save action.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/EditWidgetGroupBox](EditWidgetGroupBox.md) | qt-widgets | 3 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `EditShapefileAttributesWidget` | `QWidget` | Form | 2 |

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `table_elements` | `cellChanged(int,int)` | `this` | `handle_cell_changed(int,int)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/EditShapefileAttributesWidget.h
python scripts/gpq.py def GPlatesQtWidgets::EditShapefileAttributesWidget --body
python scripts/gpq.py uses EditShapefileAttributesWidget --kind class
python scripts/gpq.py hier EditShapefileAttributesWidget
```
