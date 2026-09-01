# EditTimePeriodWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 394 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditTimePeriodWidget.h` | C++ | 172 |
| `src/qt-widgets/EditTimePeriodWidget.cc` | C++ | 363 |
| `src/qt-widgets/EditTimePeriodWidgetUi.ui` | Qt form | 187 |

## Overview

[[[PROSE overview unit=qt-widgets/EditTimePeriodWidget tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::EditTimePeriodWidget`](#gplatesqtwidgetsedittimeperiodwidget) | class | [`AbstractEditWidget`](AbstractEditWidget.md)<br>`Ui_EditTimePeriodWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::EditTimePeriodWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EditTimePeriodWidget( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `reset_widget_to_default_values()` | method | `void` | public | — |
| `update_widget_from_time_period( GPlatesPropertyValues::GmlTimePeriod &gml_time_period)` | method | `void` | public | — |
| `create_property_value_from_widget()` | method | `GPlatesModel::PropertyValue::non_null_ptr_type` | public | — |
| `update_property_value_from_widget()` | method | `bool` | public | — |
| `get_time_period_begin()` | method | `double` | public | easy access method |
| `get_time_period_end()` | method | `double` | public | — |
| `label_begin()` | method | `QLabel` | public | Accessor for the '&Begin' label. |
| `label_end()` | method | `QLabel` | public | Accessor for the '&End' label. |
| `valid()` | method | `bool` | public | — |
| `handle_appearance_is_distant_past_check()` | method | `void` | private | — |
| `handle_appearance_is_distant_future_check()` | method | `void` | private | — |
| `handle_disappearance_is_distant_past_check()` | method | `void` | private | — |
| `handle_disappearance_is_distant_future_check()` | method | `void` | private | — |
| `d_time_period_ptr` | field | `boost::intrusive_ptr<GPlatesPropertyValues::GmlTimePeriod>` | private | This boost::intrusive\_ptr is used to remember the property value which was last loaded into this editing widget. |
| `d_help_dialog` | field | `InformationDialog` | private | "What does this mean?" blue question mark help dialog. |
| `s_help_dialog_text` | field | `QString` | private | — |
| `s_help_dialog_title` | field | `QString` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `create_geo_time_instant_from_widgets( QDoubleSpinBox *spinbox, QCheckBox *past, QCheckBox *future)` | function | `GPlatesPropertyValues::GeoTimeInstant` | — |
| `enable_or_disable_spinbox( QDoubleSpinBox *spinbox, QCheckBox *past, QCheckBox *future)` | function | `void` | — |
| `s_help_dialog_text` | variable | `QString` | — |
| `s_help_dialog_title` | variable | `QString` | — |
| `GPLATES_QTWIDGETS_EDITTIMEPERIODWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/EditTimePeriodWidget tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/SetVGPVisibilityDialog](SetVGPVisibilityDialog.md) | qt-widgets | 6 |
| [qt-widgets/CreateFeatureDialog](CreateFeatureDialog.md) | qt-widgets | 3 |
| [qt-widgets/EditWidgetGroupBox](EditWidgetGroupBox.md) | qt-widgets | 3 |
| [qt-widgets/GenerateDeformingMeshPointsDialog](GenerateDeformingMeshPointsDialog.md) | qt-widgets | 3 |
| [qt-widgets/EditFeaturePropertiesWidget](EditFeaturePropertiesWidget.md) | qt-widgets | 2 |
| [qt-widgets/ConnectWFSDialog](ConnectWFSDialog.md) | qt-widgets | 1 |
| [qt-widgets/CreateSmallCircleFeatureDialog](CreateSmallCircleFeatureDialog.md) | qt-widgets | 1 |
| [qt-widgets/EditWidgetChooser](EditWidgetChooser.md) | qt-widgets | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `EditTimePeriodWidget` | `QWidget` | Form | 12 |

**Qt signal/slot connections** (7 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `checkbox_appearance_is_distant_past` | `clicked()` | `this` | `handle_appearance_is_distant_past_check()` |
| `checkbox_appearance_is_distant_future` | `clicked()` | `this` | `handle_appearance_is_distant_future_check()` |
| `checkbox_disappearance_is_distant_past` | `clicked()` | `this` | `handle_disappearance_is_distant_past_check()` |
| `checkbox_disappearance_is_distant_future` | `clicked()` | `this` | `handle_disappearance_is_distant_future_check()` |
| `spinbox_time_of_appearance` | `valueChanged(double)` | `this` | `set_dirty()` |
| `spinbox_time_of_disappearance` | `valueChanged(double)` | `this` | `set_dirty()` |
| `button_help` | `clicked()` | `d_help_dialog` | `show()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/EditTimePeriodWidget.h
python scripts/gpq.py def GPlatesQtWidgets::EditTimePeriodWidget --body
python scripts/gpq.py uses EditTimePeriodWidget --kind class
python scripts/gpq.py hier EditTimePeriodWidget
```
