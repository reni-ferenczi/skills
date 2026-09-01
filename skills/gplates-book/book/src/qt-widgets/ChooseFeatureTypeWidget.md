# ChooseFeatureTypeWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 586 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ChooseFeatureTypeWidget.h` | C++ | 118 |
| `src/qt-widgets/ChooseFeatureTypeWidget.cc` | C++ | 202 |

## Overview

[[[PROSE overview unit=qt-widgets/ChooseFeatureTypeWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::DefaultConstructibleFeatureType`](#anonymousdefaultconstructiblefeaturetype) | class | — | — | 0 | — |
| [`GPlatesQtWidgets::ChooseFeatureTypeWidget`](#gplatesqtwidgetschoosefeaturetypewidget) | class | `QWidget` | — | 0 | — |

## Members

### `(anonymous)::DefaultConstructibleFeatureType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DefaultConstructibleFeatureType()` | constructor | `None` | public | — |
| `DefaultConstructibleFeatureType( const GPlatesModel::FeatureType &feature_type)` | constructor | `None` | public | — |
| `operator==( const DefaultConstructibleFeatureType &other)` | operator | `bool` | public | — |
| `d_feature_type` | field | `boost::optional<GPlatesModel::FeatureType>` | private | — |

### `GPlatesQtWidgets::ChooseFeatureTypeWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ChooseFeatureTypeWidget( SelectionWidget::DisplayWidget display_widget, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `populate( boost::optional<GPlatesPropertyValues::StructuralType> property_type = boost::none)` | method | `void` | public | Initialises the list widget with feature types that, according to the GPGIM, have one (or more) property(s) of the specified structural type. |
| `get_feature_type()` | method | `boost::optional<GPlatesModel::FeatureType>` | public | Gets the currently selected feature type, or boost::none if no feature type is currently selected. |
| `set_feature_type( const GPlatesModel::FeatureType &feature_type)` | method | `void` | public | Changes the currently selected feature type to feature\_type. |
| `item_activated()` | method | `void` | public | — |
| `current_index_changed( boost::optional<GPlatesModel::FeatureType>)` | method | `void` | public | — |
| `focusInEvent( QFocusEvent *ev)` | method | `void` | protected | — |
| `handle_item_activated( int index)` | method | `void` | private | — |
| `handle_current_index_changed( int index)` | method | `void` | private | — |
| `make_signal_slot_connections()` | method | `void` | private | — |
| `d_selection_widget` | field | `SelectionWidget` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_CHOOSEFEATURETYPEWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ChooseFeatureTypeWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/CreateFeatureDialog](CreateFeatureDialog.md) | qt-widgets | 9 |
| [qt-widgets/ChangeFeatureTypeDialog](ChangeFeatureTypeDialog.md) | qt-widgets | 2 |

## Related

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_selection_widget` | `item_activated(int)` | `this` | `handle_item_activated(int)` |
| `d_selection_widget` | `current_index_changed(int)` | `this` | `handle_current_index_changed(int)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ChooseFeatureTypeWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ChooseFeatureTypeWidget --body
python scripts/gpq.py uses ChooseFeatureTypeWidget --kind class
python scripts/gpq.py hier ChooseFeatureTypeWidget
```
