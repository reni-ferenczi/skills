# EditOldPlatesHeaderWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 452 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditOldPlatesHeaderWidget.h` | C++ | 84 |
| `src/qt-widgets/EditOldPlatesHeaderWidget.cc` | C++ | 183 |
| `src/qt-widgets/EditOldPlatesHeaderWidgetUi.ui` | Qt form | 466 |

## Overview

A specialized widget for editing `GpmlOldPlatesHeader` property values, which represent the header information of old PLATES format polygon files. The widget provides fields for all the header metadata: region and reference numbers, string number, geographic description, plate ID, age of appearance and disappearance, data type codes, conjugate plate ID, and colour code. The number of points is displayed read-only. Following the `AbstractEditWidget` pattern, it can be initialized from an existing header via `update_widget_from_old_plates_header()`, edited by the user, and then either create a new header via `create_property_value_from_widget()` or update the existing one. Each field change marks the widget dirty.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::EditOldPlatesHeaderWidget`](#gplatesqtwidgetseditoldplatesheaderwidget) | class | [`AbstractEditWidget`](AbstractEditWidget.md)<br>`Ui_EditOldPlatesHeaderWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::EditOldPlatesHeaderWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EditOldPlatesHeaderWidget( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `reset_widget_to_default_values()` | method | `void` | public | — |
| `update_widget_from_old_plates_header( GPlatesPropertyValues::GpmlOldPlatesHeader &gpml_old_plates_header)` | method | `void` | public | — |
| `create_property_value_from_widget()` | method | `GPlatesModel::PropertyValue::non_null_ptr_type` | public | — |
| `update_property_value_from_widget()` | method | `bool` | public | — |
| `d_old_plates_header_ptr` | field | `boost::intrusive_ptr<GPlatesPropertyValues::GpmlOldPlatesHeader>` | private | This boost::intrusive\_ptr is used to remember the property value which was last loaded into this editing widget. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_EDITOLDPLATESHEADERWIDGET_H` | macro | `None` | — |

## Notes

The `d_old_plates_header_ptr` pointer can be NULL when adding new properties (as opposed to editing existing ones). Calling `update_property_value_from_widget()` on an uninitialized widget throws `UninitialisedEditWidgetException`; ensure the widget is either initialized via `update_widget_from_old_plates_header()` or used only for creating new properties. The number-of-points field is read-only (populated from the header but not sent back when updating), as it cannot be edited by the user.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/EditWidgetGroupBox](EditWidgetGroupBox.md) | qt-widgets | 3 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `EditOldPlatesHeaderWidget` | `QWidget` | Form | 27 |

**Qt signal/slot connections** (12 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `spinbox_region_number` | `valueChanged(int)` | `this` | `set_dirty()` |
| `spinbox_reference_number` | `valueChanged(int)` | `this` | `set_dirty()` |
| `spinbox_string_number` | `valueChanged(int)` | `this` | `set_dirty()` |
| `lineedit_geographic_description` | `textEdited(const QString &)` | `this` | `set_dirty()` |
| `spinbox_plate_id_number` | `valueChanged(int)` | `this` | `set_dirty()` |
| `doublespinbox_age_of_appearance` | `valueChanged(double)` | `this` | `set_dirty()` |
| `doublespinbox_age_of_disappearance` | `valueChanged(double)` | `this` | `set_dirty()` |
| `lineedit_data_type_code` | `textEdited(const QString &)` | `this` | `set_dirty()` |
| `spinbox_data_type_code_number` | `valueChanged(int)` | `this` | `set_dirty()` |
| `lineedit_data_type_code_number_additional` | `textEdited(const QString &)` | `this` | `set_dirty()` |
| `spinbox_conjugate_plate_id_number` | `valueChanged(int)` | `this` | `set_dirty()` |
| `spinbox_colour_code` | `valueChanged(int)` | `this` | `set_dirty()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/EditOldPlatesHeaderWidget.h
python scripts/gpq.py def GPlatesQtWidgets::EditOldPlatesHeaderWidget --body
python scripts/gpq.py uses EditOldPlatesHeaderWidget --kind class
python scripts/gpq.py hier EditOldPlatesHeaderWidget
```
