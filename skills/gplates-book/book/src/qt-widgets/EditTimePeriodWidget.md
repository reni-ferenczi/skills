# EditTimePeriodWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 394 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditTimePeriodWidget.h` | C++ | 172 |
| `src/qt-widgets/EditTimePeriodWidget.cc` | C++ | 363 |
| `src/qt-widgets/EditTimePeriodWidgetUi.ui` | Qt form | 187 |

## Overview

`EditTimePeriodWidget` is the `AbstractEditWidget` used to edit a `GmlTimePeriod` property — the begin/end time-of-appearance and time-of-disappearance pair found on most reconstructable features. It presents two spin boxes (in Ma) alongside "distant past"/"distant future" checkboxes for each end, and converts between that UI state and a `GeoTimeInstant` pair via the free function `create_geo_time_instant_from_widgets()`.

`update_widget_from_time_period()` loads an existing `GmlTimePeriod` into the controls and remembers it in `d_time_period_ptr`, a `boost::intrusive_ptr` that keeps the property value alive so `update_property_value_from_widget()` can write the edited begin/end instants straight back into it later. Because having both distant-past and distant-future available for both ends is confusing, the constructor hides the "less likely" checkbox on each side (future-appearance, past-disappearance) while leaving the underlying model support intact, and wires the two spin boxes' `valueChanged` signals to `set_dirty()` so the surrounding form knows to commit.

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

`d_time_period_ptr` may be `NULL` — it is only set by `update_widget_from_time_period()`, and `update_property_value_from_widget()` throws `UninitialisedEditWidgetException` if it is called before that. `valid()` rejects a begin time that is later than the end time, resetting the disappearance spin box to `0` as a side effect of the validation check; `update_property_value_from_widget()` calls it and, if invalid, pops a `QMessageBox` warning and marks the widget clean without writing anything back. `get_time_period_begin()` and `get_time_period_end()` each test `is_distant_past()` twice instead of checking `is_distant_future()` on the second branch, so a distant-future value falls through to the `else` and is read as a real time value rather than being special-cased.

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
