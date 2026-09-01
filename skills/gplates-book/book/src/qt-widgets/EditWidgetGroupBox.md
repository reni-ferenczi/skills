# EditWidgetGroupBox

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 35 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditWidgetGroupBox.h` | C++ | 538 |
| `src/qt-widgets/EditWidgetGroupBox.cc` | C++ | 730 |

## Overview

[[[PROSE overview unit=qt-widgets/EditWidgetGroupBox tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::EditWidgetGroupBox`](#gplatesqtwidgetseditwidgetgroupbox) | class | `QGroupBox` | — | 0 | A collection of pre-allocated property edit widgets, which are hidden/shown depending on which edit widget needs to be displayed. |

## Members

### `GPlatesQtWidgets::EditWidgetGroupBox`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `property_value_type` | typedef | `GPlatesModel::GpgimStructuralType::instantiation_type` | public | A property type is the structural type of the property and an optional value type (only used if property value type is a template such as 'gpml:Array'). |
| `property_types_list_type` | typedef | `std::list<property_value_type>` | public | List of property types that are handled by this EditWidgetGroupBox. |
| `property_types_list_const_iterator` | typedef | `property_types_list_type::const_iterator` | public | — |
| `EditWidgetGroupBox( GPlatesPresentation::ViewState &view_state_, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~EditWidgetGroupBox()` | destructor | `None` | public | — |
| `set_edit_verb( const QString &verb)` | method | `void` | public | Changes the verb used as the title of the GroupBox. |
| `get_handled_property_types_list()` | method | `property_types_list_type` | public | List of property types that are handled by this EditWidgetGroupBox. |
| `get_handled_property_types( const GPlatesModel::GpgimProperty &gpgim_property, boost::optional<property_types_list_type &> property_types = boost::none)` | method | `bool` | public | Returns true if the specified GPGIM property has at least one structural type that is supported by an edit widget. |
| `activate_appropriate_edit_widget( const GPlatesModel::TopLevelProperty::non_null_ptr_type &top_level_property)` | method | `void` | public | Uses EditWidgetChooser to activate the editing widget most appropriate for the given top-level property. |
| `activate_appropriate_edit_widget( GPlatesModel::FeatureHandle::iterator it)` | method | `void` | public | Uses EditWidgetChooser to activate the editing widget most appropriate for the given property iterator it. |
| `refresh_edit_widget( GPlatesModel::FeatureHandle::iterator it)` | method | `void` | public | Uses EditWidgetChooser to update the editing widget to the latest value of the property being edited. |
| `activate_widget_by_property_type( const property_value_type &type_of_property)` | method | `void` | public | Uses a dispatch table to activate the editing widget for a given property type. |
| `is_edit_widget_active()` | method | `bool` | public | Call this function before you call create\_property\_value\_from\_widget() to determine if any edit widget is active. |
| `create_property_value_from_widget()` | method | `GPlatesModel::PropertyValue::non_null_ptr_type` | public | Creates an appropriate property value for the currently active edit widget. |
| `update_property_value_from_widget()` | method | `bool` | public | Tells the current edit widget (if any) that it should modify the last PropertyValue that it loaded data from to match what the user has entered. |
| `is_dirty()` | method | `bool` | public | Checks if the current edit widget is 'dirty' (user has modified fields and data is not in the model) If no edit widget is active, this function always returns false. |
| `set_clean()` | method | `void` | public | Informs the EditWidgetGroupBox that the data from the current widget has been committed safely. |
| `set_dirty()` | method | `void` | public | Informs the EditWidgetGroupBox that the data from the current widget does not match the Model. |
| `activate_edit_age_widget( GPlatesPropertyValues::GpmlAge &gpml_age)` | method | `void` | public | Called by EditWidgetChooser to select the appropriate editing widget. #### FIXME: Do we still need these? |
| `activate_edit_time_instant_widget( GPlatesPropertyValues::GmlTimeInstant &gml_time_instant)` | method | `void` | public | Called by EditWidgetChooser to select the appropriate editing widget. |
| `activate_edit_time_period_widget( GPlatesPropertyValues::GmlTimePeriod &gml_time_period)` | method | `void` | public | Called by EditWidgetChooser to select the appropriate editing widget. |
| `activate_edit_old_plates_header_widget( GPlatesPropertyValues::GpmlOldPlatesHeader &gpml_old_plates_header)` | method | `void` | public | Called by EditWidgetChooser to select the appropriate editing widget. |
| `activate_edit_double_widget( GPlatesPropertyValues::XsDouble &xs_double)` | method | `void` | public | Called by EditWidgetChooser to select the appropriate editing widget. |
| `activate_edit_enumeration_widget( GPlatesPropertyValues::Enumeration &enumeration)` | method | `void` | public | Called by EditWidgetChooser to select the appropriate editing widget. |
| `activate_edit_line_string_widget( GPlatesPropertyValues::GmlLineString &gml_line_string)` | method | `void` | public | Called by EditWidgetChooser to select the appropriate editing widget. |
| `activate_edit_multi_point_widget( GPlatesPropertyValues::GmlMultiPoint &gml_multi_point)` | method | `void` | public | Called by EditWidgetChooser to select the appropriate editing widget. |
| `activate_edit_point_widget( GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | public | Called by EditWidgetChooser to select the appropriate editing widget. |
| `activate_edit_polygon_widget( GPlatesPropertyValues::GmlPolygon &gml_polygon)` | method | `void` | public | Called by EditWidgetChooser to select the appropriate editing widget. |
| `activate_edit_integer_widget( GPlatesPropertyValues::XsInteger &xs_integer)` | method | `void` | public | Called by EditWidgetChooser to select the appropriate editing widget. |
| `activate_edit_plate_id_widget( GPlatesPropertyValues::GpmlPlateId &gpml_plate_id)` | method | `void` | public | Called by EditWidgetChooser to select the appropriate editing widget. |
| `activate_edit_polarity_chron_id_widget( GPlatesPropertyValues::GpmlPolarityChronId &gpml_polarity_chron_id)` | method | `void` | public | Called by EditWidgetChooser to select the appropriate editing widget. |
| `activate_edit_angle_widget( GPlatesPropertyValues::GpmlMeasure &gpml_measure)` | method | `void` | public | Called by EditWidgetChooser to select the appropriate editing widget. |
| `activate_edit_string_list_widget( GPlatesPropertyValues::GpmlStringList &gpml_string_list)` | method | `void` | public | Called by EditWidgetChooser to select the appropriate editing widget. |
| `activate_edit_string_widget( GPlatesPropertyValues::XsString &xs_string)` | method | `void` | public | Called by EditWidgetChooser to select the appropriate editing widget. |
| `activate_edit_boolean_widget( GPlatesPropertyValues::XsBoolean &xs_boolean)` | method | `void` | public | Called by EditWidgetChooser to select the appropriate editing widget. |
| `activate_edit_shapefile_attributes_widget( GPlatesPropertyValues::GpmlKeyValueDictionary &gpml_key_value_dictionary)` | method | `void` | public | Called by EditWidgetChooser to select the appropriate editing widget. |
| `activate_edit_time_sequence_widget( GPlatesPropertyValues::GpmlArray &gpml_array)` | method | `void` | public | Called by EditWidgetChooser to select the appropriate editing widget. |
| `commit_property_to_model()` | method | `void` | public | The various edit widgets make changes to what is just a clone of the property. |
| `commit_me()` | method | `void` | public | — |
| `deactivate_edit_widgets()` | method | `void` | public | — |
| `edit_widget_wants_committing()` | method | `void` | public | — |
| `widget_map_type` | typedef | `std::map< property_value_type, AbstractEditWidget *>` | private | Map type used to activate appropriate edit widget given a property value type and optional value type (only used if property type is a template). |
| `widget_map_const_iterator` | typedef | `widget_map_type::const_iterator` | private | — |
| `build_widget_map()` | method | `void` | private | Builds a map of QString to AbstractEditWidget \*, to activate edit widgets based on their property values' types. |
| `get_widget_by_property_type( const property_value_type &type_of_property)` | method | `GPlatesQtWidgets::AbstractEditWidget` | private | Given a property type, returns a pointer to the widget responsible for editing it. |
| `d_active_widget_ptr` | field | `GPlatesQtWidgets::AbstractEditWidget` | private | This pointer always refers to the one edit widget which is currently active and visible. |
| `d_edit_age_widget_ptr` | field | `GPlatesQtWidgets::EditAgeWidget` | private | Please keep these members and their initialisers sorted in alphabetical order. |
| `d_edit_angle_widget_ptr` | field | `GPlatesQtWidgets::EditAngleWidget` | private | — |
| `d_edit_boolean_widget_ptr` | field | `GPlatesQtWidgets::EditBooleanWidget` | private | — |
| `d_edit_double_widget_ptr` | field | `GPlatesQtWidgets::EditDoubleWidget` | private | — |
| `d_edit_enumeration_widget_ptr` | field | `GPlatesQtWidgets::EditEnumerationWidget` | private | — |
| `d_edit_geometry_widget_ptr` | field | `GPlatesQtWidgets::EditGeometryWidget` | private | — |
| `d_edit_integer_widget_ptr` | field | `GPlatesQtWidgets::EditIntegerWidget` | private | — |
| `d_edit_old_plates_header_widget_ptr` | field | `GPlatesQtWidgets::EditOldPlatesHeaderWidget` | private | — |
| `d_edit_plate_id_widget_ptr` | field | `GPlatesQtWidgets::EditPlateIdWidget` | private | — |
| `d_edit_polarity_chron_id_widget_ptr` | field | `GPlatesQtWidgets::EditPolarityChronIdWidget` | private | — |
| `d_edit_shapefile_attributes_widget_ptr` | field | `GPlatesQtWidgets::EditShapefileAttributesWidget` | private | — |
| `d_edit_string_list_widget_ptr` | field | `GPlatesQtWidgets::EditStringListWidget` | private | — |
| `d_edit_string_widget_ptr` | field | `GPlatesQtWidgets::EditStringWidget` | private | — |
| `d_edit_time_instant_widget_ptr` | field | `GPlatesQtWidgets::EditTimeInstantWidget` | private | — |
| `d_edit_time_period_widget_ptr` | field | `GPlatesQtWidgets::EditTimePeriodWidget` | private | — |
| `d_edit_time_sequence_widget_ptr` | field | `GPlatesQtWidgets::EditTimeSequenceWidget` | private | — |
| `d_widget_map` | field | `widget_map_type` | private | Map of property types to edit widgets. |
| `d_edit_verb` | field | `QString` | private | The verb in front of the title of the groupbox, prepended to the PropertyValue name. |
| `d_current_property` | field | `boost::optional<GPlatesModel::TopLevelProperty::non_null_ptr_type>` | private | The TopLevelProperty that we're currently editing using an edit widget. |
| `d_current_property_iterator` | field | `boost::optional<GPlatesModel::FeatureHandle::iterator>` | private | The iterator to the TopLevelProperty that we're currently editing using an edit widget. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_EDITWIDGETGROUPBOX_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/EditWidgetGroupBox tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/EditWidgetChooser](EditWidgetChooser.md) | qt-widgets | 25 |
| [qt-widgets/AddPropertyDialog](AddPropertyDialog.md) | qt-widgets | 18 |
| [qt-widgets/CreateFeatureAddOrEditPropertyDialog](CreateFeatureAddOrEditPropertyDialog.md) | qt-widgets | 13 |
| [qt-widgets/EditFeaturePropertiesWidget](EditFeaturePropertiesWidget.md) | qt-widgets | 9 |
| [feature-visitors/PropertyValueFinder](../feature-visitors/PropertyValueFinder.md) | feature-visitors | 4 |
| [qt-widgets/CreateFeaturePropertiesPage](CreateFeaturePropertiesPage.md) | qt-widgets | 1 |

## Related

**Qt signal/slot connections** (17 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_edit_age_widget_ptr` | `commit_me()` | `this` | `edit_widget_wants_committing()` |
| `d_edit_angle_widget_ptr` | `commit_me()` | `this` | `edit_widget_wants_committing()` |
| `d_edit_boolean_widget_ptr` | `commit_me()` | `this` | `edit_widget_wants_committing()` |
| `d_edit_double_widget_ptr` | `commit_me()` | `this` | `edit_widget_wants_committing()` |
| `d_edit_enumeration_widget_ptr` | `commit_me()` | `this` | `edit_widget_wants_committing()` |
| `d_edit_geometry_widget_ptr` | `commit_me()` | `this` | `edit_widget_wants_committing()` |
| `d_edit_integer_widget_ptr` | `commit_me()` | `this` | `edit_widget_wants_committing()` |
| `d_edit_old_plates_header_widget_ptr` | `commit_me()` | `this` | `edit_widget_wants_committing()` |
| `d_edit_plate_id_widget_ptr` | `commit_me()` | `this` | `edit_widget_wants_committing()` |
| `d_edit_polarity_chron_id_widget_ptr` | `commit_me()` | `this` | `edit_widget_wants_committing()` |
| `d_edit_shapefile_attributes_widget_ptr` | `commit_me()` | `this` | `edit_widget_wants_committing()` |
| `d_edit_string_list_widget_ptr` | `commit_me()` | `this` | `edit_widget_wants_committing()` |
| `d_edit_string_widget_ptr` | `commit_me()` | `this` | `edit_widget_wants_committing()` |
| `d_edit_time_instant_widget_ptr` | `commit_me()` | `this` | `edit_widget_wants_committing()` |
| `d_edit_time_period_widget_ptr` | `commit_me()` | `this` | `edit_widget_wants_committing()` |

*... and 2 more connections.*


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/EditWidgetGroupBox.h
python scripts/gpq.py def GPlatesQtWidgets::EditWidgetGroupBox --body
python scripts/gpq.py uses EditWidgetGroupBox --kind class
python scripts/gpq.py hier EditWidgetGroupBox
```
