# ReconstructGraph

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 54 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructGraph.h` | C++ | 757 |
| `src/app-logic/ReconstructGraph.cc` | C++ | 1009 |

## Overview

[[[PROSE overview unit=app-logic/ReconstructGraph tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructGraph`](#gplatesapplogicreconstructgraph) | class | `QObject`<br>`boost::noncopyable` | — | 0 | Manages layer creation and connection to other layers or input feature collections and generates a Reconstruction that is the accumulated result of all layer outputs for a specific reconstruction time. |

## Members

### `GPlatesAppLogic::ReconstructGraph`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `layer_ptr_type` | typedef | `boost::shared_ptr<ReconstructGraphImpl::Layer>` | private | Typedef for a shared pointer to a layer added to the graph. |
| `layer_ptr_seq_type` | typedef | `std::list<layer_ptr_type>` | private | Typedef for a sequence of layers. |
| `make_layer_fn_type` | typedef | `boost::function< Layer (const boost::shared_ptr<ReconstructGraphImpl::Layer> &) >` | private | Typedef for a function that creates a weak reference to a layer. |
| `const_iterator` | typedef | `boost::transform_iterator<make_layer_fn_type, layer_ptr_seq_type::const_iterator>` | public | Typedef for a const iterator over the layers in the graph. |
| `iterator` | typedef | `boost::transform_iterator<make_layer_fn_type, layer_ptr_seq_type::iterator>` | public | Typedef for an iterator over the layers in the graph. |
| `AutoCreateLayerParams` | struct | `None` | public | Parameters that determine what to do when auto-creating layers (when adding a new file). |
| `ReconstructGraph( ApplicationState &application_state)` | constructor | `None` | public | Constructor. |
| `add_files( const std::vector<FeatureCollectionFileState::file_reference> &files, boost::optional<AutoCreateLayerParams> auto_create_layers = AutoCreateLayerParams())` | method | `void` | public | Adds a group of files to the graph. |
| `add_file( const FeatureCollectionFileState::file_reference &file, boost::optional<AutoCreateLayerParams> auto_create_layers = AutoCreateLayerParams())` | method | `Layer::InputFile` | public | Adds a file to the graph. |
| `remove_file( const FeatureCollectionFileState::file_reference &file)` | method | `void` | public | Removes a file from the graph and disconnects from any connected layers. |
| `get_input_file( const FeatureCollectionFileState::file_reference input_file)` | method | `Layer::InputFile` | public | Gets the input file handle for input\_file. |
| `add_layer( const boost::shared_ptr<LayerTask> &layer_task)` | method | `Layer` | public | Adds a new layer to the graph. |
| `remove_layer( Layer layer)` | method | `void` | public | Removes a layer from the graph and sets the default reconstruction tree layer to none (if removing the default reconstruction tree layer). |
| `set_default_reconstruction_tree_layer( const Layer &default_reconstruction_tree_layer)` | method | `void` | public | Sets the current default reconstruction tree layer. |
| `get_default_reconstruction_tree_layer()` | method | `Layer` | public | Returns the current default reconstruction tree layer. |
| `begin()` | method | `const_iterator` | public | Returns the "begin" const\_iterator to iterate over the sequence of Layer objects in this graph. |
| `end()` | method | `const_iterator` | public | Returns the "end" const\_iterator to iterate over the sequence of Layer objects in this graph. |
| `update_layer_tasks( const double &reconstruction_time, GPlatesModel::integer_plate_id_type anchored_plated_id)` | method | `Reconstruction::non_null_ptr_to_const_type` | public | Updates the layer tasks in the current reconstruction graph. |
| `AddOrRemoveLayersGroup` | class | `None` | public | Used to group one or more layers that are added or removed. |
| `begin_add_or_remove_layers()` | method | `void` | public | This signal is emitted before any layers are added or removed. begin\_add\_or\_remove\_layers / end\_add\_or\_remove\_layers usually surrounds the addition or removal of one or more layers. |
| `end_add_or_remove_layers()` | method | `void` | public | This signal is emitted after layers have been added or removed. begin\_add\_or\_remove\_layers / end\_add\_or\_remove\_layers usually surrounds the addition or removal of one or more layers. |
| `layer_added( GPlatesAppLogic::ReconstructGraph &reconstruct_graph, GPlatesAppLogic::Layer layer)` | method | `void` | public | Emitted when a new layer has been added by add\_layer. |
| `layer_about_to_be_removed( GPlatesAppLogic::ReconstructGraph &reconstruct_graph, GPlatesAppLogic::Layer layer)` | method | `void` | public | Emitted when an existing layer is about to be removed inside remove\_layer. |
| `layer_removed( GPlatesAppLogic::ReconstructGraph &reconstruct_graph)` | method | `void` | public | Emitted after an existing layer has been removed inside remove\_layer. |
| `layer_activation_changed( GPlatesAppLogic::ReconstructGraph &reconstruct_graph, GPlatesAppLogic::Layer layer, bool activation)` | method | `void` | public | Emitted when layer layer has been activated or deactivated. |
| `layer_params_changed( GPlatesAppLogic::ReconstructGraph &reconstruct_graph, GPlatesAppLogic::Layer layer, GPlatesAppLogic::LayerParams &layer_params)` | method | `void` | public | Emitted when layer layer has been activated or deactivated. |
| `layer_added_input_connection( GPlatesAppLogic::ReconstructGraph &reconstruct_graph, GPlatesAppLogic::Layer layer, GPlatesAppLogic::Layer::InputConnection input_connection)` | method | `void` | public | Emitted when layer layer has added a new input connection. |
| `layer_about_to_remove_input_connection( GPlatesAppLogic::ReconstructGraph &reconstruct_graph, GPlatesAppLogic::Layer layer, GPlatesAppLogic::Layer::InputConnection input_connection)` | method | `void` | public | Emitted when layer layer is about to remove an existing input connection. |
| `layer_removed_input_connection( GPlatesAppLogic::ReconstructGraph &reconstruct_graph, GPlatesAppLogic::Layer layer)` | method | `void` | public | Emitted when layer layer has finished removing an existing input connection. |
| `default_reconstruction_tree_layer_changed( GPlatesAppLogic::ReconstructGraph &reconstruct_graph, GPlatesAppLogic::Layer prev_default_reconstruction_tree_layer, GPlatesAppLogic::Layer new_default_reconstruction_tree_layer)` | method | `void` | public | Emitted when the default reconstruction tree layer is changed. |
| `debug_reconstruct_graph_state()` | method | `void` | public | Used by GuiDebug to print out current reconstruct graph state. |
| `handle_layer_params_changed( GPlatesAppLogic::LayerParams &layer_params)` | method | `void` | private | Handles changes to the layer params of a layer. |
| `emit_begin_add_or_remove_layers()` | method | `void` | private | Emits the begin\_add\_or\_remove\_layers signal. |
| `emit_end_add_or_remove_layers()` | method | `void` | private | Emits the end\_add\_or\_remove\_layers signal. |
| `emit_layer_activation_changed( const Layer &layer, bool activation)` | method | `void` | private | Emits the layer\_activation\_changed signal. |
| `emit_layer_params_changed( const Layer &layer, LayerParams &layer_params)` | method | `void` | private | Emits the layer\_params\_changed signal. |
| `emit_layer_added_input_connection( Layer layer, Layer::InputConnection input_connection)` | method | `void` | private | Emits the layer\_added\_input\_connection signal. |
| `emit_layer_about_to_remove_input_connection( Layer layer, Layer::InputConnection input_connection)` | method | `void` | private | Emits the layer\_about\_to\_remove\_input\_connection signal. |
| `emit_layer_removed_input_connection( Layer layer)` | method | `void` | private | Emits the layer\_removed\_input\_connection signal. |
| `input_file_ptr_type` | typedef | `boost::shared_ptr<ReconstructGraphImpl::Data>` | private | Typedef for a shared pointer to an input file. |
| `InputFileInfo` | class | `None` | private | Keeps a strong reference to an input file and receives notifications when it is modified. |
| `input_file_info_map_type` | typedef | `std::map<FeatureCollectionFileState::file_reference, InputFileInfo>` | private | Typedef for a sequence of input files with InputFileInfo as map keys. |
| `default_reconstruction_tree_layer_stack_type` | typedef | `std::vector<Layer>` | private | Typedef for a stack of reconstruction tree layers. |
| `d_application_state` | field | `ApplicationState` | private | Used to reconstruct when a modification is made to a layer's task parameters. |
| `d_layer_task_registry` | field | `LayerTaskRegistry` | private | Used to create layer task when auto-creating layers (when adding a file). |
| `d_input_files` | field | `input_file_info_map_type` | private | The input files in the reconstruct graph. |
| `d_layers` | field | `layer_ptr_seq_type` | private | The layers added to the reconstruct graph. |
| `d_default_reconstruction_tree_layer_stack` | field | `default_reconstruction_tree_layer_stack_type` | private | Keeps track of the default reconstruction tree layers set as rotation files are loaded. |
| `d_identity_rotation_reconstruction_layer_proxy` | field | `ReconstructionLayerProxy::non_null_ptr_type` | private | Used if there are no reconstruction tree layers currently loaded. |
| `d_add_or_remove_layers_group_nested_count` | field | `int` | private | Keeps track of the nesting count for emit\_begin\_add\_or\_remove\_layers / emit\_end\_add\_or\_remove\_layers. |
| `add_file_internal( const FeatureCollectionFileState::file_reference &file)` | method | `Layer::InputFile` | private | Adds the specified file but does not attempt any auto-creation of layers for it. |
| `modified_input_file( const Layer::InputFile &input_file)` | method | `void` | private | Called by FeatureCollectionModified callback when the feature collection inside an input file is modified. |
| `auto_create_layers_for_new_input_file( const Layer::InputFile &input_file, const AutoCreateLayerParams &auto_create_layer_params)` | method | `void` | private | Auto-creates layers that can process the features in the specified file. |
| `auto_create_layer( const Layer::InputFile &input_file, const boost::shared_ptr<LayerTask> &layer_task, const AutoCreateLayerParams &auto_create_layer_params)` | method | `Layer` | private | Creates a layer given the specified layer task and connects to the specified input file. |
| `auto_connect_layers()` | method | `void` | private | Ensures auto-connections such as between velocity and topology layers. |
| `auto_destroy_layers_for_input_file_about_to_be_removed( const Layer::InputFile &input_file_about_to_be_removed)` | method | `void` | private | Auto-destroyes layers that were auto-created from the specified input file. |
| `handle_default_reconstruction_tree_layer_removal( const Layer &layer_being_removed)` | method | `void` | private | Handles removal of the current (or a previous) default reconstruction tree layer. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTGRAPH_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/ReconstructGraph tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/Layer](Layer.md) | app-logic | 58 |
| [qt-widgets/AssignReconstructionPlateIdsDialog](../qt-widgets/AssignReconstructionPlateIdsDialog.md) | qt-widgets | 10 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 9 |
| [presentation/DeprecatedSessionRestore](../presentation/DeprecatedSessionRestore.md) | presentation | 7 |
| [qt-widgets/ManageFeatureCollectionsDialog](../qt-widgets/ManageFeatureCollectionsDialog.md) | qt-widgets | 7 |
| [qt-widgets/MergeReconstructionLayersDialog](../qt-widgets/MergeReconstructionLayersDialog.md) | qt-widgets | 7 |
| [app-logic/ApplicationState](ApplicationState.md) | app-logic | 5 |
| [presentation/SessionManagement](../presentation/SessionManagement.md) | presentation | 4 |
| [qt-widgets/GenerateVelocityDomainCitcomsDialog](../qt-widgets/GenerateVelocityDomainCitcomsDialog.md) | qt-widgets | 4 |
| [qt-widgets/GenerateVelocityDomainLatLonDialog](../qt-widgets/GenerateVelocityDomainLatLonDialog.md) | qt-widgets | 4 |
| [qt-widgets/GenerateVelocityDomainTerraDialog](../qt-widgets/GenerateVelocityDomainTerraDialog.md) | qt-widgets | 4 |
| [entry-points/gplates_main](../entry-points/gplates_main.md) | entry-points | 3 |
| [qt-widgets/VisualLayerWidget](../qt-widgets/VisualLayerWidget.md) | qt-widgets | 3 |
| [gui/ExportAnimationStrategy](../gui/ExportAnimationStrategy.md) | gui | 2 |
| [presentation/VisualLayerRegistry](../presentation/VisualLayerRegistry.md) | presentation | 2 |
| [app-logic/LayerProxyUtils](LayerProxyUtils.md) | app-logic | 1 |
| [gui/AddClickedGeometriesToFeatureTable](../gui/AddClickedGeometriesToFeatureTable.md) | gui | 1 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 1 |
| [gui/ExportVelocityAnimationStrategy](../gui/ExportVelocityAnimationStrategy.md) | gui | 1 |
| [gui/FeatureFocus](../gui/FeatureFocus.md) | gui | 1 |

*... and 9 more units.*

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `layer_task->get_layer_params().get()` | `modified(GPlatesAppLogic::LayerParams &)` | `this` | `handle_layer_params_changed(GPlatesAppLogic::LayerParams &)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructGraph.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructGraph --body
python scripts/gpq.py uses ReconstructGraph --kind class
python scripts/gpq.py hier ReconstructGraph
```
