# EditAgeWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1058 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditAgeWidget.h` | C++ | 101 |
| `src/qt-widgets/EditAgeWidget.cc` | C++ | 424 |
| `src/qt-widgets/EditAgeWidgetUi.ui` | Qt form | 346 |

## Overview

[[[PROSE overview unit=qt-widgets/EditAgeWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::ComboboxNameOrAbsValues`](#anonymouscomboboxnameorabsvalues) | enum | — | — | 0 | These correspond to the three states of combobox\_name\_or\_abs. |
| [`(anonymous)::ComboboxUncertaintyValues`](#anonymouscomboboxuncertaintyvalues) | enum | — | — | 0 | These correspond to the three states of combobox\_uncertainty. |
| [`GPlatesQtWidgets::EditAgeWidget`](#gplatesqtwidgetseditagewidget) | class | [`AbstractEditWidget`](AbstractEditWidget.md)<br>`Ui_EditAgeWidget` | — | 0 | — |

## Members

### `(anonymous)::ComboboxNameOrAbsValues`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EDIT_AGE_ABSOLUTE` | enumerator | `None` | — | — |
| `EDIT_AGE_NAMED` | enumerator | `None` | — | — |
| `EDIT_AGE_BOTH` | enumerator | `None` | — | — |

### `(anonymous)::ComboboxUncertaintyValues`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UNCERTAINTY_NONE` | enumerator | `None` | — | — |
| `UNCERTAINTY_PLUSMINUS` | enumerator | `None` | — | — |
| `UNCERTAINTY_RANGE` | enumerator | `None` | — | — |

### `GPlatesQtWidgets::EditAgeWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EditAgeWidget( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `reset_widget_to_default_values()` | method | `void` | public | — |
| `update_widget_from_age( GPlatesPropertyValues::GpmlAge &age)` | method | `void` | public | — |
| `create_property_value_from_widget()` | method | `GPlatesModel::PropertyValue::non_null_ptr_type` | public | — |
| `update_property_value_from_widget()` | method | `bool` | public | — |
| `handle_name_or_abs_changed( int slot)` | method | `void` | private | Hides widgets according to the Absolute/Named/Both combobox. |
| `handle_timescale_changed( int slot)` | method | `void` | private | Allows an 'other' value to be edited if selected in the timescale combobox. |
| `d_age_ptr` | field | `boost::intrusive_ptr<GPlatesPropertyValues::GpmlAge>` | private | This boost::intrusive\_ptr is used to remember the property value which was last loaded into this editing widget. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `gimme_double( const QLineEdit &lineedit)` | function | `boost::optional<double>` | — |
| `gimme_qstring( const QLineEdit &lineedit)` | function | `QString` | — |
| `set_lineedit_contents( QLineEdit *lineedit, const boost::optional<GPlatesPropertyValues::TimescaleBand> &band)` | function | `QString` | — |
| `set_lineedit_contents( QLineEdit *lineedit, const boost::optional<GPlatesPropertyValues::TimescaleName> &name)` | function | `QString` | — |
| `set_lineedit_contents( QLineEdit *lineedit, const boost::optional<double> &dbl)` | function | `QString` | — |
| `set_gpml_age_fields_from_widget( const Ui_EditAgeWidget &ui, GPlatesPropertyValues::GpmlAge::non_null_ptr_type age_ptr)` | function | `void` | It occurs to me that perhaps we could move to the 'ui \*' style of doing Qt widgets, and default-constructed property values which we can then set via a common method like this. |
| `GPLATES_QTWIDGETS_EDITAGEWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/EditAgeWidget tier=3]]]
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
| `EditAgeWidget` | `QWidget` | Form | 19 |

**Qt signal/slot connections** (11 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `combobox_name_or_abs` | `activated(int)` | `this` | `set_dirty()` |
| `combobox_timescale` | `activated(int)` | `this` | `set_dirty()` |
| `combobox_uncertainty` | `activated(int)` | `this` | `set_dirty()` |
| `lineedit_abs_age` | `textEdited(const QString &)` | `this` | `set_dirty()` |
| `lineedit_named_age` | `textEdited(const QString &)` | `this` | `set_dirty()` |
| `lineedit_timescale_other` | `textEdited(const QString &)` | `this` | `set_dirty()` |
| `lineedit_uncertainty_plusminus` | `textEdited(const QString &)` | `this` | `set_dirty()` |
| `lineedit_uncertainty_youngest` | `textEdited(const QString &)` | `this` | `set_dirty()` |
| `lineedit_uncertainty_oldest` | `textEdited(const QString &)` | `this` | `set_dirty()` |
| `combobox_name_or_abs` | `currentIndexChanged(int)` | `this` | `handle_name_or_abs_changed(int)` |
| `combobox_timescale` | `currentIndexChanged(int)` | `this` | `handle_timescale_changed(int)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/EditAgeWidget.h
python scripts/gpq.py def GPlatesQtWidgets::EditAgeWidget --body
python scripts/gpq.py uses EditAgeWidget --kind class
python scripts/gpq.py hier EditAgeWidget
```
