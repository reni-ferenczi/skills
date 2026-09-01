# ChangeFeatureTypeDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 824 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ChangeFeatureTypeDialog.h` | C++ | 150 |
| `src/qt-widgets/ChangeFeatureTypeDialog.cc` | C++ | 339 |
| `src/qt-widgets/ChangeFeatureTypeDialogUi.ui` | Qt form | 84 |

## Overview

[[[PROSE overview unit=qt-widgets/ChangeFeatureTypeDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ChangeFeatureTypeDialog`](#gplatesqtwidgetschangefeaturetypedialog) | class | `QDialog`<br>`Ui_ChangeFeatureTypeDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ChangeFeatureTypeDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ChangeFeatureTypeDialog( GPlatesAppLogic::ApplicationState &application_state, GPlatesGui::FeatureFocus &feature_focus, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `populate( const GPlatesModel::FeatureHandle::weak_ref &feature_ref)` | method | `void` | public | Sets up the dialog to change the feature type for the given feature. |
| `handle_feature_type_changed( boost::optional<GPlatesModel::FeatureType> feature_type_opt)` | method | `void` | private | — |
| `change_feature_type()` | method | `void` | private | — |
| `InvalidPropertiesWidget` | class | `None` | private | The InvalidPropertiesWidget shows a list of properties that are invalid for the new feature type with an explanatory message. |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_feature_focus` | field | `GPlatesGui::FeatureFocus` | private | — |
| `d_new_feature_type_widget` | field | `ChooseFeatureTypeWidget` | private | Allows the user to choose a new feature type. |
| `d_widget_container` | field | `QWidget` | private | The container holding all the ChangePropertyWidgets. |
| `d_widget_container_layout` | field | `QBoxLayout` | private | The layout of d\_widget\_container. |
| `d_invalid_properties_widget` | field | `InvalidPropertiesWidget` | private | Displays invalid properties to the user. |
| `d_change_property_widget_pool` | field | `std::vector<ChangePropertyWidget *>` | private | A pool of ChangePropertyWidget instances, to save us from having to continuously destroy and create these objects. |
| `d_num_active_widgets` | field | `unsigned int` | private | The number of widgets active in d\_change\_property\_widget\_pool. |
| `d_feature_ref` | field | `GPlatesModel::FeatureHandle::weak_ref` | private | A handle to the feature that we're modifying. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_CHANGEFEATURETYPEDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ChangeFeatureTypeDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/FeaturePropertiesDialog](FeaturePropertiesDialog.md) | qt-widgets | 3 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ChangeFeatureTypeDialog` | `QDialog` | Change Feature Type | 6 |

**Qt signal/slot connections** (3 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_new_feature_type_widget` | `current_index_changed(boost::optional<GPlatesModel::FeatureType>)` | `this` | `handle_feature_type_changed(boost::optional<GPlatesModel::FeatureType>)` |
| `main_buttonbox` | `accepted()` | `this` | `change_feature_type()` |
| `main_buttonbox` | `rejected()` | `this` | `reject()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ChangeFeatureTypeDialog.h
python scripts/gpq.py def GPlatesQtWidgets::ChangeFeatureTypeDialog --body
python scripts/gpq.py uses ChangeFeatureTypeDialog --kind class
python scripts/gpq.py hier ChangeFeatureTypeDialog
```
