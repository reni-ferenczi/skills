# AddPropertyDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 467 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/AddPropertyDialog.h` | C++ | 154 |
| `src/qt-widgets/AddPropertyDialog.cc` | C++ | 572 |
| `src/qt-widgets/AddPropertyDialogUi.ui` | Qt form | 182 |

## Overview

`AddPropertyDialog` is the modal dialog behind "add a property to this
feature": the user picks a property name and a property value type from two
comboboxes, the dialog swaps in the matching `EditWidgetGroupBox` edit widget,
and on accept it builds a `PropertyValue` from that widget and calls
`GPlatesModel::ModelUtils::add_property()` to attach it to the focused
feature. Which property names are offered, and whether a chosen name is valid
for the feature's type, is decided by consulting `GPlatesModel::Gpgim` — the
dialog does not hard-code GPGIM's feature/property rules itself, it queries
them live via `Gpgim::instance().get_feature_property()`.

`set_feature()` re-populates the property-name combobox every time it is
called, even for the same feature and feature type, because GPGIM property
multiplicity means which names are still legal to add can change as the
feature's existing properties change; since the dialog is modal, nothing else
can mutate the feature while it is open, so this is simpler than listening
for model change callbacks. `add_property()` deliberately adds the property
without GPGIM's usual name/multiplicity/value-type checks, since the name and
type were already chosen from GPGIM-derived comboboxes.

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

`d_feature_ref` is a `weak_ref`; `add_property()` checks `is_valid()` and
shows a warning dialog instead of adding the property if the feature has gone
away while the dialog was open. The `EditWidgetGroupBox` is combined into the
Designer-generated `Ui_AddPropertyDialog` layout by hand in
`set_up_edit_widgets()`, since Qt Designer forms cannot embed a hand-coded
composite widget directly.

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
