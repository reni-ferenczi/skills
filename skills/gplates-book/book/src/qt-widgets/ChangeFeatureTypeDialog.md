# ChangeFeatureTypeDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 824 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ChangeFeatureTypeDialog.h` | C++ | 150 |
| `src/qt-widgets/ChangeFeatureTypeDialog.cc` | C++ | 339 |
| `src/qt-widgets/ChangeFeatureTypeDialogUi.ui` | Qt form | 84 |

## Overview

Dialog for changing the feature type of an existing feature. When a feature type changes, its properties must be re-validated: some existing properties may become invalid for the new type, or valid in type but requiring renaming. This dialog guides the user through that reconciliation by showing a `ChooseFeatureTypeWidget` to select the new type, then dynamically populating `ChangePropertyWidget` instances for each property that needs renaming, and displaying a list of properties that have become entirely invalid.

Properties are reused in a pool (`d_change_property_widget_pool`) to avoid repeated allocation and destruction. When the feature type selection changes, the dialog re-evaluates all properties against the GPGIM constraints: properties with matching names require no action, properties with matching type but incompatible names are offered for renaming through the widget pool, and properties with incompatible types are listed as unresolvable. The OK button is disabled until the user selects a type different from the current one.

After confirmation, the dialog applies the type change to the model, asks each active property widget to commit its renaming, and if any geometry property was renamed to the focused geometry, it triggers reconstruction and updates the feature focus.

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

*None.*

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
