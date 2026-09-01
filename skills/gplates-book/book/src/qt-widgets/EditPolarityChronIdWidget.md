# EditPolarityChronIdWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1596 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditPolarityChronIdWidget.h` | C++ | 85 |
| `src/qt-widgets/EditPolarityChronIdWidget.cc` | C++ | 124 |
| `src/qt-widgets/EditPolarityChronIdWidgetUi.ui` | Qt form | 92 |

## Overview

[[[PROSE overview unit=qt-widgets/EditPolarityChronIdWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=qt-widgets/EditPolarityChronIdWidget tier=3]]]
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
