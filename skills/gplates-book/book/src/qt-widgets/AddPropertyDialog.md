# AddPropertyDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 467 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/AddPropertyDialog.h` | C++ | 154 |
| `src/qt-widgets/AddPropertyDialog.cc` | C++ | 572 |
| `src/qt-widgets/AddPropertyDialogUi.ui` | Qt form | 182 |

## Overview

[[[PROSE overview unit=qt-widgets/AddPropertyDialog tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::SortByUnqualifiedPropertyName`](#anonymoussortbyunqualifiedpropertyname) | class | — | — | 0 | Used to sort GPGIM properties by the unqualified part of their property names. |
| [`GPlatesQtWidgets::AddPropertyDialog`](#gplatesqtwidgetsaddpropertydialog) | class | `QDialog`<br>`Ui_AddPropertyDialog` | — | 0 | — |

## Members

### `(anonymous)::SortByUnqualifiedPropertyName`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator()( const GPlatesModel::GpgimProperty::non_null_ptr_to_const_type &lhs, const GPlatesModel::GpgimProperty::non_null_ptr_to_const_type &rhs)` | operator | `bool` | public | — |

### `GPlatesQtWidgets::AddPropertyDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AddPropertyDialog( GPlatesGui::FeatureFocus &feature_focus_, GPlatesPresentation::ViewState &view_state_, QWidget *parent_ = NULL)` | constructor | `None` | public | Constructs the Add Property Dialog instance. |
| `~AddPropertyDialog()` | destructor | `None` | public | — |
| `set_feature( const GPlatesModel::FeatureHandle::weak_ref &feature_ref)` | method | `void` | public | Set the feature, and its feature type, that the properties are being added to. |
| `reset()` | method | `void` | public | Resets dialog components to default state. |
| `pop_up()` | method | `void` | public | Pops up the AddPropertyDialog as a modal dialog, after resetting itself to default values. |
| `set_appropriate_edit_widget()` | method | `void` | private | — |
| `check_property_name_validity()` | method | `void` | private | — |
| `add_property()` | method | `void` | private | — |
| `populate_property_name_combobox()` | method | `void` | private | — |
| `populate_property_type_combobox()` | method | `void` | private | — |
| `connect_to_combobox_add_property_name_signals( bool connects_signal_slot)` | method | `void` | private | — |
| `connect_to_combobox_add_property_type_signals( bool connects_signal_slot)` | method | `void` | private | — |
| `set_up_add_property_box()` | method | `void` | private | — |
| `set_up_edit_widgets()` | method | `void` | private | — |
| `get_default_feature_type` | field | `GPlatesModel::FeatureType` | private | Default feature type to use when no available feature or invalid feature reference. |
| `d_feature_focus` | field | `GPlatesGui::FeatureFocus` | private | Announce modifications to the focused feature. |
| `d_feature_ref` | field | `GPlatesModel::FeatureHandle::weak_ref` | private | The feature that properties are being added to. |
| `d_feature_type` | field | `GPlatesModel::FeatureType` | private | The type of feature that properties are being added to. |
| `d_edit_widget_group_box_ptr` | field | `EditWidgetGroupBox` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `feature_has_property_name( const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const GPlatesModel::PropertyName &property_name)` | function | `bool` | — |
| `GPLATES_QTWIDGETS_ADDPROPERTYDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/AddPropertyDialog tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/EditFeaturePropertiesWidget](EditFeaturePropertiesWidget.md) | qt-widgets | 16 |
| [qt-widgets/ViewportWindow](ViewportWindow.md) | qt-widgets | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `AddPropertyDialog` | `QDialog` | Add Property | 10 |

**Qt signal/slot connections** (5 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `combobox_add_property_name` | `currentIndexChanged(int)` | `this` | `populate_property_type_combobox()` |
| `combobox_add_property_name` | `currentIndexChanged(int)` | `this` | `check_property_name_validity()` |
| `combobox_add_property_type` | `currentIndexChanged(int)` | `this` | `set_appropriate_edit_widget()` |
| `buttonBox` | `accepted()` | `this` | `add_property()` |
| `d_edit_widget_group_box_ptr` | `commit_me()` | `buttonBox` | `setFocus()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/AddPropertyDialog.h
python scripts/gpq.py def GPlatesQtWidgets::AddPropertyDialog --body
python scripts/gpq.py uses AddPropertyDialog --kind class
python scripts/gpq.py hier AddPropertyDialog
```
