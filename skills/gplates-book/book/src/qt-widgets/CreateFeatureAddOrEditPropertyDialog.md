# CreateFeatureAddOrEditPropertyDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 555 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/CreateFeatureAddOrEditPropertyDialog.h` | C++ | 146 |
| `src/qt-widgets/CreateFeatureAddOrEditPropertyDialog.cc` | C++ | 429 |
| `src/qt-widgets/CreateFeatureAddOrEditPropertyDialogUi.ui` | Qt form | 146 |

## Overview

`CreateFeatureAddOrEditPropertyDialog` is the single modal dialog used both to add a
new property to a feature and to edit an existing one, chosen by which of
`add_property()` or `edit_property()` the caller invokes. It wraps an
`EditWidgetGroupBox`, which owns one edit widget per supported property value type;
the dialog itself only figures out which structural type is in play and asks the
group box to activate the matching widget. Adding a property lets the user pick the
value type from `combobox_property_type` (populated from the `GpgimProperty`'s
allowed structural types via `GpgimProperty::get_default_structural_type()`), while
editing shows that combobox with the feature's existing type only, since the type
of an existing property cannot be changed.

The property type combobox is populated as encoded strings such as
`gpml:PiecewiseAggregation<gpml:FiniteRotation>` for template types, and
`set_appropriate_edit_widget_by_property_value_type()` parses that string back apart
to resolve the `GPlatesPropertyValues::StructuralType` and, for templates, the value
type, before asking the group box to activate the right widget. `is_property_supported()`
lets callers (such as `CreateFeatureDialog`) skip GPGIM properties that have no
edit widget at all before ever showing this dialog.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::CreateFeatureAddOrEditPropertyDialog`](#gplatesqtwidgetscreatefeatureaddoreditpropertydialog) | class | `QDialog`<br>`Ui_CreateFeatureAddOrEditPropertyDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::CreateFeatureAddOrEditPropertyDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CreateFeatureAddOrEditPropertyDialog( GPlatesPresentation::ViewState &view_state_, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~CreateFeatureAddOrEditPropertyDialog()` | destructor | `None` | public | — |
| `add_property( const GPlatesModel::GpgimProperty &gpgim_feature_property)` | method | `boost::optional<GPlatesModel::TopLevelProperty::non_null_ptr_type>` | public | Pops up the CreateFeatureAddOrEditPropertyDialog as a modal dialog and allows user to create a feature property identified by the specified GPGIM property. |
| `edit_property( const GPlatesModel::TopLevelProperty::non_null_ptr_type &feature_property)` | method | `void` | public | Pops up the CreateFeatureAddOrEditPropertyDialog as a modal dialog and allows user to edit the specified feature property. |
| `is_property_supported( const GPlatesModel::GpgimProperty &gpgim_property)` | method | `bool` | public | Returns true if the specified GPGIM property has at least one structural type that is supported by an edit widget. |
| `set_appropriate_edit_widget_by_property_value_type()` | method | `void` | private | — |
| `create_property_from_edit_widget()` | method | `void` | private | — |
| `update_property_from_edit_widget()` | method | `void` | private | — |
| `AddProperty` | struct | `None` | private | Associates a GPGIM property to the created feature property when adding a new property. |
| `set_up_edit_widgets()` | method | `void` | private | — |
| `connect_to_combobox_property_type_signals( bool connects_signal_slot)` | method | `void` | private | — |
| `populate_add_property_type_combobox( const GPlatesModel::GpgimProperty &gpgim_property)` | method | `void` | private | — |
| `populate_edit_property_type_combobox( const GPlatesModel::TopLevelProperty::non_null_ptr_type &feature_property)` | method | `void` | private | — |
| `d_edit_widget_group_box` | field | `EditWidgetGroupBox` | private | Used to add or edit a feature property. |
| `d_add_property` | field | `boost::optional<AddProperty>` | private | Only used to store feature property when 'adding' a property (as opposed to editing). |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_CREATEFEATUREADDOREDITPROPERTYDIALOG_H` | macro | `None` | — |

## Notes

`add_property()` and `edit_property()` are mutually exclusive entry points into the
same dialog instance: each rewires `buttonBox`'s `accepted()` signal to a different
slot (`create_property_from_edit_widget()` vs. `update_property_from_edit_widget()`)
and reconfigures the standard buttons, so the two must not be interleaved on the
same call. `add_property()` returns `boost::none` both when the user cancels and
when property creation fails after "OK" is pressed; `d_add_property` is only valid
between entering `add_property()` and its return, and is reset to `boost::none`
before returning either way. Editing offers no "Cancel" button, since a user
edit cannot be undone once applied to the widget; if no edit widget is available,
`update_property_from_edit_widget()` calls `reject()` to close the dialog since
there is no button to do it for the user.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlFeatureReaderFactory](../file-io/GpmlFeatureReaderFactory.md) | file-io | 7 |
| [qt-widgets/CreateFeaturePropertiesPage](CreateFeaturePropertiesPage.md) | qt-widgets | 7 |
| [model/GpgimFeatureClass](../model/GpgimFeatureClass.md) | model | 6 |
| [qt-widgets/AddPropertyDialog](AddPropertyDialog.md) | qt-widgets | 2 |
| [qt-widgets/CreateFeatureDialog](CreateFeatureDialog.md) | qt-widgets | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `CreateFeatureAddOrEditPropertyDialog` | `QDialog` | Add/Edit Property | 7 |

**Qt signal/slot connections** (4 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `buttonBox` | `accepted()` | `this` | `create_property_from_edit_widget()` |
| `buttonBox` | `accepted()` | `this` | `update_property_from_edit_widget()` |
| `d_edit_widget_group_box` | `commit_me()` | `buttonBox` | `setFocus()` |
| `combobox_property_type` | `currentIndexChanged(int)` | `this` | `set_appropriate_edit_widget_by_property_value_type()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/CreateFeatureAddOrEditPropertyDialog.h
python scripts/gpq.py def GPlatesQtWidgets::CreateFeatureAddOrEditPropertyDialog --body
python scripts/gpq.py uses CreateFeatureAddOrEditPropertyDialog --kind class
python scripts/gpq.py hier CreateFeatureAddOrEditPropertyDialog
```
