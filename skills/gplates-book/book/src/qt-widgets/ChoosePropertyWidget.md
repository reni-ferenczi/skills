# ChoosePropertyWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 554 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ChoosePropertyWidget.h` | C++ | 126 |
| `src/qt-widgets/ChoosePropertyWidget.cc` | C++ | 263 |

## Overview

[[[PROSE overview unit=qt-widgets/ChoosePropertyWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::DefaultConstructiblePropertyName`](#anonymousdefaultconstructiblepropertyname) | class | — | — | 0 | — |
| [`(anonymous)::SortByUnqualifiedPropertyName`](#anonymoussortbyunqualifiedpropertyname) | class | — | — | 0 | Used to sort GPGIM properties by the unqualified part of their property names. |
| [`GPlatesQtWidgets::ChoosePropertyWidget`](#gplatesqtwidgetschoosepropertywidget) | class | `QWidget` | — | 0 | ChoosePropertyWidget encapsulates a widget that offers the user a selection of property names that can be used with a particular feature type and property structural type. |

## Members

### `(anonymous)::DefaultConstructiblePropertyName`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DefaultConstructiblePropertyName()` | constructor | `None` | public | — |
| `DefaultConstructiblePropertyName( const GPlatesModel::PropertyName &property_name)` | constructor | `None` | public | — |
| `operator==( const DefaultConstructiblePropertyName &other)` | operator | `bool` | public | — |
| `d_property_name` | field | `boost::optional<GPlatesModel::PropertyName>` | private | — |

### `(anonymous)::SortByUnqualifiedPropertyName`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator()( const GPlatesModel::GpgimProperty::non_null_ptr_to_const_type &lhs, const GPlatesModel::GpgimProperty::non_null_ptr_to_const_type &rhs)` | operator | `bool` | public | — |

### `GPlatesQtWidgets::ChoosePropertyWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `get_properties_to_populate( std::vector<GPlatesModel::GpgimProperty::non_null_ptr_to_const_type> &gpgim_properties, const GPlatesModel::FeatureType &target_feature_type, const GPlatesPropertyValues::StructuralType &target_property_type, const GPlatesModel::FeatureHandle::weak_ref &source_feature_ref = GPlatesModel::Fea ...` | method | `bool` | public | Returns the list of GPGIM properties that populate will show to the user. |
| `ChoosePropertyWidget( SelectionWidget::DisplayWidget display_widget, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `populate( const GPlatesModel::FeatureType &target_feature_type, const GPlatesPropertyValues::StructuralType &target_property_type, const GPlatesModel::FeatureHandle::weak_ref &source_feature_ref = GPlatesModel::FeatureHandle::weak_ref())` | method | `void` | public | Causes this widget to show properties appropriate for the specified feature type and property type. |
| `get_property_name()` | method | `boost::optional<GPlatesModel::PropertyName>` | public | Returns the currently selected property name. |
| `set_property_name( const GPlatesModel::PropertyName &property_name)` | method | `void` | public | Changes the currently selected property name to property\_name. |
| `item_activated()` | method | `void` | public | — |
| `handle_item_activated( int index)` | method | `void` | private | — |
| `d_selection_widget` | field | `SelectionWidget` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `feature_has_property_name( const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const GPlatesModel::PropertyName &property_name)` | function | `bool` | — |
| `GPLATES_QTWIDGETS_CHOOSEPROPERTYWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ChoosePropertyWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/CreateFeatureDialog](CreateFeatureDialog.md) | qt-widgets | 10 |
| [qt-widgets/ChangeFeatureTypeDialog](ChangeFeatureTypeDialog.md) | qt-widgets | 2 |
| [qt-widgets/ChangePropertyWidget](ChangePropertyWidget.md) | qt-widgets | 2 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_selection_widget` | `item_activated(int)` | `this` | `handle_item_activated(int)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ChoosePropertyWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ChoosePropertyWidget --body
python scripts/gpq.py uses ChoosePropertyWidget --kind class
python scripts/gpq.py hier ChoosePropertyWidget
```
