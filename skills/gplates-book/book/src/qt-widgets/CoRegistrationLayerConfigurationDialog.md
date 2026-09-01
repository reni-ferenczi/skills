# CoRegistrationLayerConfigurationDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 132 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/CoRegistrationLayerConfigurationDialog.h` | C++ | 395 |
| `src/qt-widgets/CoRegistrationLayerConfigurationDialog.cc` | C++ | 1490 |
| `src/qt-widgets/CoRegistrationLayerConfigurationDialogUi.ui` | Qt form | 229 |

## Overview

Configuration dialog for co-registration layers, which perform data mining by associating reconstructed geometries or raster data with feature attributes according to user-specified rules. The dialog displays a list of target layers (raster or reconstructed geometries), allows users to select a target and add configuration rows that define how attributes should be computed. Each configuration row maps a specific attribute on the target layer to a source layer using a filter type, an optional reduction function, and layer/attribute information.

The dialog presents two attribute categories: relational attributes (for geometry targets) and co-registration attributes (with level-of-detail and polygon-filling options for raster targets). Configuration changes are immediately reflected in `CoRegConfigurationTable` and synchronized to the layer parameters. Input layer changes are detected and the GUI is automatically updated when the feature store is modified, as available attributes depend on the current data.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::CoRegistrationLayerConfigurationDialog`](#gplatesqtwidgetscoregistrationlayerconfigurationdialog) | class | `QDialog`<br>`Ui_CoRegistrationLayerConfigurationDialog` | — | 0 | The configuration dialog for Co-registration layer. |

## Members

### `GPlatesQtWidgets::CoRegistrationLayerConfigurationDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ConfigurationTableColumnType` | enum | `None` | public | — |
| `LayerItem` | struct | `None` | public | A QListWidgetItem derivation so that we can display a list of layers in the list widget using the layer name as the label, while keeping track of which list item corresponds to which layer. |
| `AttributeItem` | struct | `None` | public | — |
| `AttributeListItem` | struct | `None` | public | — |
| `LayerTableItem` | struct | `None` | public | — |
| `AttributeTableItem` | struct | `None` | public | — |
| `CoRegistrationLayerConfigurationDialog( GPlatesPresentation::ViewState &view_state, ViewportWindow *viewport_window, boost::weak_ptr<GPlatesPresentation::VisualLayer> layer)` | constructor | `None` | public | — |
| `pop_up()` | method | `void` | public | — |
| `set_visual_layer( boost::weak_ptr<GPlatesPresentation::VisualLayer> layer)` | method | `void` | public | — |
| `reject()` | method | `void` | public | — |
| `apply( QAbstractButton*)` | method | `void` | public | — |
| `update( bool update_only_when_visible = true)` | method | `void` | public | Updates GUI and co-registration configuration. |
| `react_target_layer_selection_changed()` | method | `void` | private | — |
| `react_add_configuration_row()` | method | `void` | private | — |
| `populate_attributes()` | method | `void` | private | — |
| `populate_relational_attributes()` | method | `void` | private | — |
| `populate_coregistration_attributes()` | method | `void` | private | — |
| `handle_co_registration_input_layer_list_changed( GPlatesAppLogic::ReconstructGraph &, GPlatesAppLogic::Layer)` | method | `void` | private | Is called whenever an input layer to our co-registration layer has been added or removed. |
| `remove()` | method | `void` | private | — |
| `remove_all()` | method | `void` | private | — |
| `cfg_table_cell_changed( int row, int column)` | method | `void` | private | — |
| `update_cfg_table()` | method | `void` | private | — |
| `get_configuration_table_from_layer( GPlatesAppLogic::CoRegistrationLayerParams &)` | method | `void` | private | Handle config table modified via the layer params (instead of via this dialog). |
| `UpdateWhenFeatureStoreIsModified` | struct | `None` | private | The model callback that notifies us when the feature store is modified so that we can do a reconstruction. |
| `is_raster_co_registration_supported()` | method | `bool` | private | — |
| `populate_target_layers_list()` | method | `void` | private | — |
| `populate_reconstructed_geometries_coregistration_attributes( const GPlatesAppLogic::Layer &target_layer)` | method | `void` | private | — |
| `populate_raster_coregistration_attributes( const GPlatesAppLogic::Layer &target_layer)` | method | `void` | private | — |
| `does_raster_layer_contain_numerical_data( const GPlatesAppLogic::Layer &raster_layer)` | method | `bool` | private | — |
| `create_gl_renderer()` | method | `GPlatesGlobal::PointerTraits<GPlatesOpenGL::GLRenderer>::non_null_ptr_type` | private | Creates an OpenGL renderer so we can query raster-related information. |
| `get_unique_attribute_names( const GPlatesAppLogic::Layer &target_layer, std::set< GPlatesModel::PropertyName > &property_names, std::set< QString > &shapefile_attr_names)` | method | `void` | private | — |
| `setup_reducer_combobox( const QString& attribute_name, QComboBox* combo, const GPlatesAppLogic::LayerTaskType::Type target_layer_type)` | method | `void` | private | — |
| `setup_reducer_relational_combobox( const QString& attribute_name, QComboBox* combo, const GPlatesAppLogic::LayerTaskType::Type target_layer_type)` | method | `void` | private | — |
| `setup_reducer_non_relational_combobox( const QString& attribute_name, QComboBox* combo, const GPlatesAppLogic::LayerTaskType::Type target_layer_type)` | method | `void` | private | — |
| `setup_association_type_combobox( QComboBox* combo)` | method | `void` | private | — |
| `setup_raster_level_of_detail_combo_box( QComboBox* combo, const GPlatesAppLogic::Layer &raster_target_layer, const QString &raster_band_name)` | method | `bool` | private | — |
| `setup_raster_fill_polygons_check_box( QCheckBox* check_box)` | method | `void` | private | — |
| `remove_config_rows_referencing_nonexistent_target_layer()` | method | `bool` | private | — |
| `get_input_target_layers()` | method | `std::vector<GPlatesAppLogic::Layer>` | private | — |
| `get_input_seed_layers()` | method | `std::vector<GPlatesAppLogic::Layer>` | private | — |
| `get_input_layers( GPlatesAppLogic::LayerInputChannelName::Type channel_name, bool target_layers)` | method | `std::vector<GPlatesAppLogic::Layer>` | private | — |
| `create_configuration_table( GPlatesDataMining::CoRegConfigurationTable &cfg_table)` | method | `void` | private | — |
| `set_configuration_table_on_layer( const GPlatesDataMining::CoRegConfigurationTable &cfg_table)` | method | `void` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_viewport_window` | field | `ViewportWindow` | private | — |
| `d_visual_layers` | field | `GPlatesPresentation::VisualLayers` | private | — |
| `AttrTypeNameMap` | typedef | `std::multimap< QString, GPlatesDataMining::AttributeTypeEnum >` | private | — |
| `d_attr_name_type_map` | field | `AttrTypeNameMap` | private | — |
| `d_visual_layer` | field | `boost::weak_ptr<GPlatesPresentation::VisualLayer>` | private | — |
| `d_cfg_table` | field | `GPlatesDataMining::CoRegConfigurationTable` | private | The current configuration table. |
| `d_callback_feature_store` | field | `GPlatesModel::FeatureStoreRootHandle::const_weak_ref` | private | Keep a weak reference to the feature store root handle just for our callback. |
| `d_raster_co_registration_supported` | field | `bool` | private | Is raster co-registration supported (are the necessary OpenGL extensions available). |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `DISTANCE` | variable | `char` | — |
| `PRESENCE` | variable | `char` | — |
| `NUM_ROI` | variable | `char` | — |
| `HIGHEST` | variable | `char` | — |
| `DISABLE_GCC_WARNING` | variable | `PUSH_GCC_WARNINGS` | The BOOST\_FOREACH macro in versions of boost before 1.37 uses the same local variable name in each instantiation. |
| `GPLATES_QT_WIDGETS_COREGISTRATIONLAYERCONFIGURATIONDIALOG_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/CoRegistrationOptionsWidget](CoRegistrationOptionsWidget.md) | qt-widgets | 7 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `CoRegistrationLayerConfigurationDialog` | `QDialog` | Co-Registration Layer Configuration | 13 |

**Qt signal/slot connections** (21 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `target_layers_list_widget` | `itemSelectionChanged()` | `this` | `react_target_layer_selection_changed()` |
| `target_layers_list_widget` | `itemClicked(QListWidgetItem *)` | `this` | `react_target_layer_selection_changed()` |
| `add_push_button` | `clicked()` | `this` | `react_add_configuration_row()` |
| `button_box` | `clicked(QAbstractButton*)` | `this` | `apply(QAbstractButton*)` |
| `relational_radio_button` | `clicked()` | `this` | `populate_relational_attributes()` |
| `co_reg_radio_buttton` | `clicked()` | `this` | `populate_coregistration_attributes()` |
| `remove_push_button` | `clicked()` | `this` | `remove()` |
| `remove_all_push_button` | `clicked()` | `this` | `remove_all()` |
| `co_reg_cfg_table_widget` | `cellChanged(int, int)` | `this` | `cfg_table_cell_changed(int,int)` |
| `layer_params` | `modified_cfg_table(GPlatesAppLogic::CoRegistrationLayerParams &)` | `this` | `get_configuration_table_from_layer(GPlatesAppLogic::CoRegistrationLayerParams &)` |
| `&d_application_state.get_reconstruct_graph()` | `layer_added_input_connection( GPlatesAppLogic::ReconstructGraph &, GPlatesAppLogic::Layer, GPlatesAppLogic::Layer::InputConnection)` | `this` | `handle_co_registration_input_layer_list_changed( GPlatesAppLogic::ReconstructGraph &, GPlatesAppLogic::Layer )` |
| `&d_application_state.get_reconstruct_graph()` | `layer_removed_input_connection( GPlatesAppLogic::ReconstructGraph &, GPlatesAppLogic::Layer)` | `this` | `handle_co_registration_input_layer_list_changed( GPlatesAppLogic::ReconstructGraph &, GPlatesAppLogic::Layer )` |
| `&d_application_state.get_reconstruct_graph()` | `layer_activation_changed( GPlatesAppLogic::ReconstructGraph &, GPlatesAppLogic::Layer, bool)` | `this` | `handle_co_registration_input_layer_list_changed( GPlatesAppLogic::ReconstructGraph &, GPlatesAppLogic::Layer )` |
| `combo` | `currentIndexChanged(int)` | `this` | `update_cfg_table()` |
| `association_combo` | `currentIndexChanged(int)` | `this` | `update_cfg_table()` |

*... and 6 more connections.*


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/CoRegistrationLayerConfigurationDialog.h
python scripts/gpq.py def GPlatesQtWidgets::CoRegistrationLayerConfigurationDialog --body
python scripts/gpq.py uses CoRegistrationLayerConfigurationDialog --kind class
python scripts/gpq.py hier CoRegistrationLayerConfigurationDialog
```
