# EditPolarityChronIdWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1596 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditPolarityChronIdWidget.h` | C++ | 85 |
| `src/qt-widgets/EditPolarityChronIdWidget.cc` | C++ | 124 |
| `src/qt-widgets/EditPolarityChronIdWidgetUi.ui` | Qt form | 92 |

## Overview

An editor widget for `GpmlPolarityChronId` property values. These values store magnetic polarity chron identification data as three optional fields: an era (text, presented as a dropdown), a major region (integer, presented as a spinbox), and a minor region (text, presented as a line edit). The widget follows the `AbstractEditWidget` protocol: it updates its UI from a loaded property value, signals when edited, and can either update an existing value in place or create a new value from the current UI state.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::EditPolarityChronIdWidget`](#gplatesqtwidgetseditpolaritychronidwidget) | class | [`AbstractEditWidget`](AbstractEditWidget.md)<br>`Ui_EditPolarityChronIdWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::EditPolarityChronIdWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EditPolarityChronIdWidget( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `reset_widget_to_default_values()` | method | `void` | public | — |
| `update_widget_from_polarity_chron_id( GPlatesPropertyValues::GpmlPolarityChronId &polarity_chron_id)` | method | `void` | public | — |
| `create_property_value_from_widget()` | method | `GPlatesModel::PropertyValue::non_null_ptr_type` | public | — |
| `update_property_value_from_widget()` | method | `bool` | public | — |
| `d_polarity_chron_id_ptr` | field | `boost::intrusive_ptr<GPlatesPropertyValues::GpmlPolarityChronId>` | private | This boost::intrusive\_ptr is used to remember the property value which was last loaded into this editing widget. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_EDITPOLARITYCHRONIDWIDGET_H` | macro | `None` | — |

## Notes

Calling `update_property_value_from_widget()` before loading a property value with `update_widget_from_polarity_chron_id()` throws `UninitialisedEditWidgetException`. The era dropdown accepts values not in its predefined list — if a loaded value's era does not match any item, it is appended to the dropdown.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/EditWidgetGroupBox](EditWidgetGroupBox.md) | qt-widgets | 3 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `EditPolarityChronIdWidget` | `QWidget` | Form | 7 |

**Qt signal/slot connections** (3 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `combobox_era` | `activated(int)` | `this` | `set_dirty()` |
| `spinbox_major` | `valueChanged(int)` | `this` | `set_dirty()` |
| `lineedit_minor` | `textEdited(const QString &)` | `this` | `set_dirty()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/EditPolarityChronIdWidget.h
python scripts/gpq.py def GPlatesQtWidgets::EditPolarityChronIdWidget --body
python scripts/gpq.py uses EditPolarityChronIdWidget --kind class
python scripts/gpq.py hier EditPolarityChronIdWidget
```
