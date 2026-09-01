# ChangePropertyWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1217 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ChangePropertyWidget.h` | C++ | 109 |
| `src/qt-widgets/ChangePropertyWidget.cc` | C++ | 201 |
| `src/qt-widgets/ChangePropertyWidgetUi.ui` | Qt form | 44 |

## Overview

[[[PROSE overview unit=qt-widgets/ChangePropertyWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ChangePropertyWidget`](#gplatesqtwidgetschangepropertywidget) | class | `QWidget`<br>`Ui_ChangePropertyWidget` | — | 0 | The ChangePropertyWidget is a helper widget for the ChangeFeatureTypeDialog; for each problematic property detected by the ChangeFeatureTypeDialog, it will spawn one of these widgets, which is responsible for presenting the user with a ... |

## Members

### `GPlatesQtWidgets::ChangePropertyWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ChangePropertyWidget( const GPlatesGui::FeatureFocus &feature_focus, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `populate( const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const GPlatesModel::FeatureHandle::iterator &feature_property, const GPlatesPropertyValues::StructuralType &feature_property_type, const GPlatesModel::FeatureType &new_feature_type)` | method | `void` | public | Causes the widget to present to the user a choice of alternative properties suitable for the new\_feature\_type chosen for the given feature\_property of a particular feature\_ref. |
| `process( GPlatesModel::FeatureHandle::iterator &new_focused_geometry_property)` | method | `void` | public | Change the property to the user's choice, if the user has elected to change the property. |
| `handle_checkbox_state_changed( int state)` | method | `void` | private | — |
| `d_feature_focus` | field | `GPlatesGui::FeatureFocus` | private | — |
| `d_property_destinations_widget` | field | `ChoosePropertyWidget` | private | — |
| `d_default_explanatory_text` | field | `QString` | private | — |
| `d_feature_ref` | field | `GPlatesModel::FeatureHandle::weak_ref` | private | — |
| `d_property` | field | `GPlatesModel::FeatureHandle::iterator` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `DISABLE_GCC_WARNING` | variable | `PUSH_GCC_WARNINGS` | For the BOOST\_STATIC\_ASSERT below with GCC 4.2. |
| `GPLATES_QTWIDGETS_CHANGEPROPERTYWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ChangePropertyWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ChangeFeatureTypeDialog](ChangeFeatureTypeDialog.md) | qt-widgets | 3 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ChangePropertyWidget` | `QWidget` | Change Geometry Property | 3 |

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `change_property_checkbox` | `stateChanged(int)` | `this` | `handle_checkbox_state_changed(int)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ChangePropertyWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ChangePropertyWidget --body
python scripts/gpq.py uses ChangePropertyWidget --kind class
python scripts/gpq.py hier ChangePropertyWidget
```
