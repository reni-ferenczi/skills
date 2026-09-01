# CreateFeatureDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 33 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/CreateFeatureDialog.h` | C++ | 532 |
| `src/qt-widgets/CreateFeatureDialog.cc` | C++ | 2644 |
| `src/qt-widgets/CreateFeatureDialogUi.ui` | Qt form | 270 |

## Overview

[[[PROSE overview unit=qt-widgets/CreateFeatureDialog tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::CreateFeatureDialog`](#gplatesqtwidgetscreatefeaturedialog) | class | `QDialog`<br>`Ui_CreateFeatureDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::CreateFeatureDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `StackedWidgetPage` | enum | `None` | public | — |
| `CreateFeatureDialog( GPlatesPresentation::ViewState &view_state_, GPlatesQtWidgets::ViewportWindow &viewport_window_, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `set_geometry_and_display( const GPlatesModel::PropertyValue::non_null_ptr_type &geometry_property_value)` | method | `bool` | public | Rather than simply exec()ing the dialog, you should call this method to ensure you are feeding the CreateFeatureDialog some valid geometry at the same time. |
| `feature_created( GPlatesModel::FeatureHandle::weak_ref feature)` | method | `void` | public | — |
| `handle_prev()` | method | `void` | private | — |
| `handle_next()` | method | `void` | private | — |
| `handle_page_change( int page)` | method | `void` | private | Called when we are switching between pages. |
| `handle_leave_page( int page)` | method | `void` | private | — |
| `handle_enter_page( int page, int last_page)` | method | `void` | private | — |
| `handle_create()` | method | `void` | private | The 'create' button on the last page has been pushed; assemble our lists of properties into actual features (using create\_feature()), add geometry properties and reverse-reconstruct them so the geometry is properly expressed in present-day ... |
| `handle_create_and_save()` | method | `void` | private | — |
| `recon_method_changed( int index)` | method | `void` | private | — |
| `handle_conjugate_plate_id_changed()` | method | `void` | private | — |
| `handle_feature_type_changed()` | method | `void` | private | — |
| `handle_canvas_tool_triggered( GPlatesGui::CanvasToolWorkflows::WorkflowType workflow, GPlatesGui::CanvasToolWorkflows::ToolType tool)` | method | `void` | private | — |
| `set_up_button_box()` | method | `void` | private | — |
| `set_up_custom_properties_page()` | method | `void` | private | — |
| `set_up_feature_type_page()` | method | `void` | private | — |
| `set_up_common_properties_page()` | method | `void` | private | — |
| `set_up_feature_properties_page()` | method | `void` | private | — |
| `set_up_conjugate_properties_page()` | method | `void` | private | — |
| `set_up_feature_collection_page()` | method | `void` | private | — |
| `set_up_feature_list()` | method | `void` | private | — |
| `select_default_feature_type()` | method | `void` | private | — |
| `set_up_geometric_property_list()` | method | `void` | private | — |
| `select_default_geometry_property_name()` | method | `void` | private | — |
| `set_up_common_properties()` | method | `void` | private | — |
| `set_up_all_properties_gui()` | method | `void` | private | — |
| `set_up_conjugate_properties_gui()` | method | `void` | private | — |
| `clear_properties_not_allowed_for_current_feature_type()` | method | `void` | private | — |
| `copy_common_properties_into_all_properties()` | method | `void` | private | — |
| `copy_common_property_into_all_properties( const GPlatesModel::PropertyName &property_name, const GPlatesModel::PropertyValue::non_null_ptr_type &property_value)` | method | `void` | private | — |
| `remove_common_property_from_all_properties( const GPlatesModel::PropertyName &property_name)` | method | `void` | private | — |
| `generate_conjugate_properties_from_all_properties()` | method | `void` | private | Takes the "all properties" list d\_feature\_properties and populates the "conjugate properties" list d\_conjugate\_properties based on that. |
| `generate_conjugate_property( const GPlatesModel::PropertyName &property_name, const GPlatesModel::PropertyValue::non_null_ptr_type &property_value)` | method | `boost::optional<GPlatesModel::TopLevelProperty::non_null_ptr_type>` | private | Helper for generate\_conjugate\_properties\_from\_all\_properties(), in cases where we need to tweak a property's value. |
| `display()` | method | `bool` | private | — |
| `create_feature( const GPlatesModel::FeatureType feature_type, const CreateFeaturePropertiesPage::property_seq_type feature_properties, const GPlatesModel::PropertyName geometry_property_name, const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection)` | method | `GPlatesModel::FeatureHandle::non_null_ptr_type` | private | Handles the main effort of constructing a new feature based on the list of properties we have assembled during this dialog's invocation. |
| `add_geometry_property( const GPlatesModel::FeatureHandle::weak_ref &feature, const GPlatesModel::PropertyName &geometry_property_name)` | method | `boost::optional<GPlatesModel::FeatureHandle::iterator>` | private | — |
| `reverse_reconstruct_geometry_property( const GPlatesModel::FeatureHandle::weak_ref &feature, const GPlatesModel::FeatureHandle::iterator &geometry_property_iterator, const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection)` | method | `bool` | private | — |
| `create_feature_link( GPlatesModel::FeatureHandle::non_null_ptr_type feature, const GPlatesModel::PropertyName &property_name, GPlatesModel::FeatureHandle::non_null_ptr_to_const_type target_feature)` | method | `void` | private | Given two features and a property name (e.g. gpml:conjugate), create a FeatureReference in feature linking to target\_feature. |
| `d_model_ptr` | field | `GPlatesModel::ModelInterface` | private | The Model interface, used to create new features. |
| `d_file_state` | field | `GPlatesAppLogic::FeatureCollectionFileState` | private | The loaded feature collection files. |
| `d_file_io` | field | `GPlatesAppLogic::FeatureCollectionFileIO` | private | Used to create an empty feature collection file. |
| `d_application_state_ptr` | field | `GPlatesAppLogic::ApplicationState` | private | The reconstruction generator is used to access the reconstruction tree to perform reverse reconstruction of the temporary geometry (once we know the plate id). |
| `d_viewport_window_ptr` | field | `ViewportWindow` | private | Used to popup dialogs in the main window. |
| `d_geometry_property_value` | field | `boost::optional<GPlatesModel::PropertyValue::non_null_ptr_type>` | private | The geometry that is to be included with the feature. |
| `d_geometry_property_type` | field | `boost::optional<GPlatesPropertyValues::StructuralType>` | private | The geometry type of the geometry that is to be included with the feature. |
| `d_feature_type` | field | `boost::optional<GPlatesModel::FeatureType>` | private | The feature type (if any selected). |
| `d_previously_selected_feature_type` | field | `boost::optional<GPlatesModel::FeatureType>` | private | The feature type that was previously selected when we last left the Choose Feature Type page. |
| `d_listwidget_geometry_destinations` | field | `ChoosePropertyWidget` | private | Allows the user to pick the property that will store the geometry. |
| `d_recon_method_widget` | field | `QWidget` | private | The reconstruction method widget (containing label and combobox). |
| `d_recon_method_combobox` | field | `QComboBox` | private | reconstruction method combox |
| `d_plate_id_widget` | field | `EditPlateIdWidget` | private | The custom edit widget for reconstruction. |
| `d_conjugate_plate_id_widget` | field | `EditPlateIdWidget` | private | The custom edit widget for conjugate plate id. |
| `d_relative_plate_id_widget` | field | `EditPlateIdWidget` | private | The custom edit widget for 'relative plate' id (for MotionPath feature type). |
| `d_left_plate_id` | field | `EditPlateIdWidget` | private | left plate id |
| `d_right_plate_id` | field | `EditPlateIdWidget` | private | right plate id |
| `d_time_period_widget` | field | `EditTimePeriodWidget` | private | The custom edit widget for GmlTimePeriod. |
| `d_name_widget` | field | `EditStringWidget` | private | The custom edit widget for XsString which we are using for the gml:name property. |
| `d_create_conjugate_feature_checkbox` | field | `QCheckBox` | private | Checkbox for creating a conjugate feature. |
| `d_button_create` | field | `QPushButton` | private | Button added to buttonbox for the final feature creation step; takes the place of an 'OK' button. |
| `d_choose_feature_type_widget` | field | `ChooseFeatureTypeWidget` | private | The widget that allows the user to select the feature type of the new feature. |
| `d_feature_type_description_widget` | field | `ResizeToContentsTextEdit` | private | A feature type description QTextEdit that resizes to its contents. |
| `d_choose_feature_collection_widget` | field | `ChooseFeatureCollectionWidget` | private | The widget that allows the user to select an existing feature collection to add the new feature to, or a new feature collection. |
| `d_custom_properties_widget` | field | `boost::optional<AbstractCustomPropertiesWidget *>` | private | Abstract base widget for custom properties widgets. |
| `d_create_feature_properties_page` | field | `CreateFeaturePropertiesPage` | private | The stacked widget page where properties (allowed by the GPGIM for the feature type) can be added to the feature by the user. |
| `d_create_conjugate_properties_page` | field | `CreateFeaturePropertiesPage` | private | The stacked widget page where properties (allowed by the GPGIM for the feature type) can be modified and added for the conjugate feature, if one is to be created. |
| `d_recon_method` | field | `GPlatesAppLogic::ReconstructMethod::Type` | private | — |
| `d_current_page` | field | `StackedWidgetPage` | private | The index of the current stacked widget page. |
| `d_feature_properties` | field | `CreateFeaturePropertiesPage::property_seq_type` | private | The properties (excluding the selected geometry property) to create the feature with. |
| `d_conjugate_properties` | field | `CreateFeaturePropertiesPage::property_seq_type` | private | The properties (excluding the selected geometry property) to create the conjugate feature with. |
| `d_canvas_tool_last_chosen_by_user` | field | `boost::optional< std::pair< GPlatesGui::CanvasToolWorkflows::WorkflowType, GPlatesGui::CanvasToolWorkflows::ToolType> >` | private | The last canvas tool explicitly chosen by the user (i.e. not the result of an automatic switch of canvas tool by GPlates code). |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `is_topological_line( const GPlatesPropertyValues::StructuralType &property_type)` | function | `bool` | — |
| `is_topological_line( const GPlatesModel::PropertyValue &property_value)` | function | `bool` | — |
| `is_topological_polygon( const GPlatesPropertyValues::StructuralType &property_type)` | function | `bool` | — |
| `is_topological_polygon( const GPlatesModel::PropertyValue &property_value)` | function | `bool` | — |
| `is_topological_network( const GPlatesPropertyValues::StructuralType &property_type)` | function | `bool` | — |
| `is_topological_network( const GPlatesModel::PropertyValue &property_value)` | function | `bool` | — |
| `is_topological_geometry( const GPlatesPropertyValues::StructuralType &property_type)` | function | `bool` | — |
| `is_topological_geometry( const GPlatesModel::PropertyValue &property_value)` | function | `bool` | — |
| `is_non_topological_geometry( const GPlatesPropertyValues::StructuralType &property_type)` | function | `bool` | — |
| `is_non_topological_geometry( const GPlatesModel::PropertyValue &property_value)` | function | `bool` | — |
| `is_geometry( const GPlatesPropertyValues::StructuralType &property_type)` | function | `bool` | — |
| `is_geometry( const GPlatesModel::PropertyValue &property_value)` | function | `bool` | — |
| `should_add_import_geometry_time_prop( const boost::optional<GPlatesModel::FeatureType> &feature_type)` | function | `bool` | Query the GPGIM to determine whether we can add the 'gpml:geometryImportTime' property. |
| `should_offer_reconstruction_plate_id_prop( const boost::optional<GPlatesModel::FeatureType> &feature_type, const boost::optional<GPlatesPropertyValues::StructuralType> &geometry_property_type)` | function | `bool` | Returns whether or not we should offer a reconstruction plate ID property. |
| `should_offer_conjugate_plate_id_prop( const boost::optional<GPlatesModel::FeatureType> &feature_type, const boost::optional<GPlatesPropertyValues::StructuralType> &geometry_property_type)` | function | `bool` | Returns whether or not we should offer a conjugate plate ID property. |
| `should_link_with_conjugate_prop( const boost::optional<GPlatesModel::FeatureType> &feature_type)` | function | `bool` | Query the GPGIM to determine whether we should link conjugate features together using the gpml:conjugate property. |
| `should_offer_create_conjugate_feature_checkbox( const boost::optional<GPlatesModel::FeatureType> &feature_type, const boost::optional<GPlatesPropertyValues::StructuralType> &geometry_property_type)` | function | `bool` | Returns whether or not we offer an additional checkbox for creating a conjugate feature. |
| `should_offer_conjugate_properties_page( const boost::optional<GPlatesModel::FeatureType> &feature_type, const boost::optional<GPlatesPropertyValues::StructuralType> &geometry_property_type, const QCheckBox &create_conjugate_checkbox)` | function | `bool` | Returns whether or not we offer an additional page for adjusting conjugate feature properties. |
| `should_offer_relative_plate_id_prop( const boost::optional<GPlatesModel::FeatureType> &feature_type)` | function | `bool` | Query the GPGIM to determine whether we should present the user with a relativePlate property value edit widget. |
| `should_offer_reconstruct_method_prop( const boost::optional<GPlatesModel::FeatureType> &feature_type, const boost::optional<GPlatesPropertyValues::StructuralType> &geometry_property_type)` | function | `bool` | Returns whether or not we should offer a reconstruction method. |
| `find_property_value( const GPlatesModel::PropertyName &property_name, const GPlatesQtWidgets::CreateFeaturePropertiesPage::property_seq_type &feature_properties)` | function | `boost::optional<typename PropertyValueType::non_null_ptr_type>` | Finds a property value in the sequence of top-level properties that has the specified property name and type, and returns a clone of it (so it can be modified). |
| `get_custom_properties_widget( const boost::optional<GPlatesModel::FeatureType> &feature_type, const GPlatesAppLogic::ApplicationState &application_state, GPlatesQtWidgets::CreateFeatureDialog *create_feature_dialog_ptr)` | function | `boost::optional<GPlatesQtWidgets::AbstractCustomPropertiesWidget *>` | Handles special case properties appropriate to the feature type selected in the choose\_feature\_type\_widget. |
| `GPLATES_QTWIDGETS_CREATEFEATUREDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/CreateFeatureDialog tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/CoRegistrationLayerConfigurationDialog](CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 26 |
| [qt-widgets/ColouringDialog](ColouringDialog.md) | qt-widgets | 5 |
| [qt-widgets/DigitisationWidget](DigitisationWidget.md) | qt-widgets | 4 |
| [qt-widgets/AgeModelManagerDialog](AgeModelManagerDialog.md) | qt-widgets | 2 |
| [qt-widgets/RasterBandPage](RasterBandPage.md) | qt-widgets | 2 |
| [qt-widgets/SelectionWidget](SelectionWidget.md) | qt-widgets | 2 |
| [qt-widgets/TopologyToolsWidget](TopologyToolsWidget.md) | qt-widgets | 2 |
| [qt-widgets/VisualLayersComboBox](VisualLayersComboBox.md) | qt-widgets | 2 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 1 |
| [presentation/Application](../presentation/Application.md) | presentation | 1 |
| [qt-widgets/ViewportWindow](ViewportWindow.md) | qt-widgets | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `CreateFeatureDialog` | `QDialog` | Create Feature | 25 |

**Qt signal/slot connections** (30 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `stack` | `currentChanged(int)` | `this` | `handle_page_change(int)` |
| `&viewport_window_.canvas_tool_bar_dock_widget()` | `canvas_tool_triggered_by_user( GPlatesGui::CanvasToolWorkflows::WorkflowType, GPlatesGui::CanvasToolWorkflows::ToolType)` | `this` | `handle_canvas_tool_triggered( GPlatesGui::CanvasToolWorkflows::WorkflowType, GPlatesGui::CanvasToolWorkflows::ToolType)` |
| `buttonbox` | `accepted()` | `this` | `handle_create()` |
| `buttonbox` | `rejected()` | `this` | `reject()` |
| `button_prev` | `clicked()` | `this` | `handle_prev()` |
| `button_next` | `clicked()` | `this` | `handle_next()` |
| `button_create_and_save` | `clicked()` | `this` | `handle_create_and_save()` |
| `d_choose_feature_type_widget` | `item_activated()` | `this` | `handle_next()` |
| `d_choose_feature_type_widget` | `current_index_changed(boost::optional<GPlatesModel::FeatureType>)` | `this` | `handle_feature_type_changed()` |
| `d_listwidget_geometry_destinations` | `item_activated()` | `d_time_period_widget` | `setFocus()` |
| `d_time_period_widget` | `enter_pressed()` | `d_name_widget` | `setFocus()` |
| `d_name_widget` | `enter_pressed()` | `button_next` | `setFocus()` |
| `d_recon_method_combobox` | `currentIndexChanged(int)` | `this` | `recon_method_changed(int)` |
| `d_conjugate_plate_id_widget` | `value_changed()` | `this` | `handle_conjugate_plate_id_changed()` |
| `d_create_feature_properties_page` | `finished()` | `button_next` | `setFocus()` |

*... and 15 more connections.*


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/CreateFeatureDialog.h
python scripts/gpq.py def GPlatesQtWidgets::CreateFeatureDialog --body
python scripts/gpq.py uses CreateFeatureDialog --kind class
python scripts/gpq.py hier CreateFeatureDialog
```
