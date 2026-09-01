# CreateFeaturePropertiesPage

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 306 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/CreateFeaturePropertiesPage.h` | C++ | 213 |
| `src/qt-widgets/CreateFeaturePropertiesPage.cc` | C++ | 743 |
| `src/qt-widgets/CreateFeaturePropertiesPageUi.ui` | Qt form | 242 |

## Overview

[[[PROSE overview unit=qt-widgets/CreateFeaturePropertiesPage tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::DefaultConstructibleNonNullPtrType`](#anonymousdefaultconstructiblenonnullptrtype) | class | — | `<class T, class H = GPlatesUtils::NullIntrusivePointerHandler>` | 0 | A non-null pointer that is default-constructible so it can be used with QVariant. |
| [`(anonymous)::SortByUnqualifiedPropertyName`](#anonymoussortbyunqualifiedpropertyname) | class | — | — | 0 | Used to sort GPGIM properties by the unqualified part of their property names. |
| [`GPlatesQtWidgets::CreateFeaturePropertiesPage`](#gplatesqtwidgetscreatefeaturepropertiespage) | class | `QWidget`<br>`Ui_CreateFeaturePropertiesPage` | — | 0 | — |

## Members

### `(anonymous)::DefaultConstructibleNonNullPtrType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DefaultConstructibleNonNullPtrType()` | constructor | `None` | public | — |
| `DefaultConstructibleNonNullPtrType( const GPlatesUtils::non_null_intrusive_ptr<T,H> &non_null_ptr)` | constructor | `None` | public | — |
| `operator==( const DefaultConstructibleNonNullPtrType &other)` | operator | `bool` | public | — |
| `d_non_null_ptr` | field | `boost::optional< GPlatesUtils::non_null_intrusive_ptr<T,H> >` | private | — |

### `(anonymous)::SortByUnqualifiedPropertyName`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator()( const GPlatesModel::GpgimProperty::non_null_ptr_to_const_type &lhs, const GPlatesModel::GpgimProperty::non_null_ptr_to_const_type &rhs)` | operator | `bool` | public | — |

### `GPlatesQtWidgets::CreateFeaturePropertiesPage`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `property_name_seq_type` | typedef | `std::vector<GPlatesModel::PropertyName>` | public | Typedef for a sequence of property names. |
| `property_seq_type` | typedef | `std::vector<GPlatesModel::TopLevelProperty::non_null_ptr_type>` | public | Typedef for a sequence of top-level feature properties. |
| `CreateFeaturePropertiesPage( GPlatesPresentation::ViewState &view_state, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `initialise( const GPlatesModel::FeatureType &feature_type, const property_seq_type &feature_properties, const property_name_seq_type &reserved_feature_properties = property_name_seq_type(), const QString &adjective = "")` | method | `void` | public | Set the feature type and the initial set of feature properties. |
| `is_finished()` | method | `bool` | public | Returns true if the user has added all feature properties that are required (that have a minimum GPGIM multiplicity of one). |
| `get_feature_properties( property_seq_type &feature_properties)` | method | `void` | public | Returns the current list of feature properties. |
| `finished()` | method | `void` | public | Emitted when there are no remaining \*required\* feature properties for the user to add. |
| `focusInEvent( QFocusEvent *event)` | method | `void` | protected | — |
| `handle_available_properties_selection_changed()` | method | `void` | private | — |
| `handle_existing_properties_selection_changed()` | method | `void` | private | — |
| `handle_add_property_button_clicked()` | method | `void` | private | — |
| `handle_remove_property_button_clicked()` | method | `void` | private | — |
| `handle_edit_property_button_clicked()` | method | `void` | private | — |
| `AvailablePropertiesColumnName` | enum | `None` | private | These should match the 'available properties' table columns set up in the UI designer. |
| `ExistingPropertiesColumnName` | enum | `None` | private | These should match the 'existing properties' table columns set up in the UI designer. |
| `gpgim_property_seq_type` | typedef | `std::vector<GPlatesModel::GpgimProperty::non_null_ptr_to_const_type>` | private | Typedef for a sequence of GPGIM feature properties. |
| `d_feature_type` | field | `GPlatesModel::FeatureType` | private | The type of feature that the properties will be added to. |
| `d_reserved_feature_properties` | field | `property_name_seq_type` | private | The names of any feature properties that will later be added (and hence are equivalent to existing properties in that they are not available for the user to add). |
| `d_property_description_widget` | field | `ResizeToContentsTextEdit` | private | A property description QTextEdit that resizes to its contents. |
| `d_add_or_edit_property_dialog` | field | `CreateFeatureAddOrEditPropertyDialog` | private | Dialog used to add and edit feature properties. |
| `initialise_existing_properties_table( const property_seq_type &feature_propertiesfeature_properties)` | method | `void` | private | — |
| `add_to_existing_properties( const GPlatesModel::TopLevelProperty::non_null_ptr_type &feature_property)` | method | `void` | private | — |
| `update_available_properties_table()` | method | `void` | private | — |
| `get_available_property( int row)` | method | `boost::optional<GPlatesModel::GpgimProperty::non_null_ptr_to_const_type>` | private | — |
| `get_available_properties( gpgim_property_seq_type &gpgim_feature_properties)` | method | `void` | private | — |
| `get_existing_property( int row)` | method | `boost::optional<GPlatesModel::TopLevelProperty::non_null_ptr_type>` | private | — |
| `update_focus()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `convert_top_level_property_to_display_string( const GPlatesModel::TopLevelProperty &top_level_property)` | function | `QString` | Returns a simple string representation the specified top-level property. |
| `feature_has_property_name( const GPlatesModel::PropertyName &property_name, const GPlatesQtWidgets::CreateFeaturePropertiesPage::property_seq_type &feature_properties, const GPlatesQtWidgets::CreateFeaturePropertiesPage::property_name_seq_type &reserved_feature_properties)` | function | `bool` | Returns true if any properties in feature\_properties, or reserved\_feature\_properties, match property\_name. |
| `GPLATES_QTWIDGETS_CREATEFEATUREPROPERTIESPAGE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/CreateFeaturePropertiesPage tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/CreateFeatureDialog](CreateFeatureDialog.md) | qt-widgets | 9 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `CreateFeaturePropertiesPage` | `QWidget` | Form | 13 |

**Qt signal/slot connections** (7 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `add_property_button` | `clicked()` | `this` | `handle_add_property_button_clicked()` |
| `remove_property_button` | `clicked()` | `this` | `handle_remove_property_button_clicked()` |
| `edit_property_button` | `clicked()` | `this` | `handle_edit_property_button_clicked()` |
| `available_properties_table_widget` | `itemSelectionChanged()` | `this` | `handle_available_properties_selection_changed()` |
| `available_properties_table_widget` | `itemActivated(QTableWidgetItem *)` | `this` | `handle_add_property_button_clicked()` |
| `existing_properties_table_widget` | `itemSelectionChanged()` | `this` | `handle_existing_properties_selection_changed()` |
| `existing_properties_table_widget` | `itemActivated(QTableWidgetItem *)` | `this` | `handle_edit_property_button_clicked()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/CreateFeaturePropertiesPage.h
python scripts/gpq.py def GPlatesQtWidgets::CreateFeaturePropertiesPage --body
python scripts/gpq.py uses CreateFeaturePropertiesPage --kind class
python scripts/gpq.py hier CreateFeaturePropertiesPage
```
