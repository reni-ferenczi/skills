# VisualLayers

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 260 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/VisualLayers.h` | C++ | 517 |
| `src/presentation/VisualLayers.cc` | C++ | 804 |

## Overview

[[[PROSE overview unit=presentation/VisualLayers tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPresentation::VisualLayers`](#gplatespresentationvisuallayers) | class | `QObject`<br>`boost::noncopyable` | — | 0 | — |

## Members

### `GPlatesPresentation::VisualLayers`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `VisualLayers( GPlatesAppLogic::ApplicationState &application_state, ViewState &view_state)` | constructor | `None` | public | Constructor. |
| `size()` | method | `size_t` | public | Returns the number of visual layers. |
| `move_layer( size_t from_index, size_t to_index)` | method | `void` | public | Moves the layer at from\_index to to\_index. |
| `visual_layer_at( size_t index)` | method | `boost::weak_ptr<const VisualLayer>` | public | Returns the visual layer that is at position index in the layer ordering. |
| `child_layer_index_at( size_t index)` | method | `GPlatesViewOperations::RenderedGeometryCollection::child_layer_index_type` | public | Returns the rendered geometry child layer index belonging to the visual layer at index. |
| `get_visual_layer( const GPlatesAppLogic::Layer &layer)` | method | `boost::weak_ptr<const VisualLayer>` | public | Returns the corresponding visual layer for the given layer. |
| `rendered_geometry_layer_seq_type` | typedef | `std::vector<GPlatesViewOperations::RenderedGeometryCollection::child_layer_index_type>` | public | Typedef for the container that stores the visual layers ordering. |
| `get_layer_order` | field | `rendered_geometry_layer_seq_type` | public | Returns the visual layers ordering as a sequence of rendered geometry layers indices. |
| `const_iterator` | typedef | `rendered_geometry_layer_seq_type::const_iterator` | public | Typedef for const iterator over the ordering of visual layers. |
| `order_begin()` | method | `const_iterator` | public | Returns the 'begin' iterator for the visual layers ordering. |
| `order_end()` | method | `const_iterator` | public | Returns the 'end' iterator for the visual layers ordering. |
| `show_all()` | method | `void` | public | Set visibility of all visual layers to true |
| `hide_all()` | method | `void` | public | Set visibility of all visual layers to false |
| `create_rendered_geometries()` | method | `void` | public | Creates rendered geometries for each active visual layer. |
| `layer_order_changed( size_t first_index, size_t last_index)` | method | `void` | public | Indicates that there has been a change in the ordering of layer indices from first\_index to last\_index, inclusive. |
| `begin_add_or_remove_layers()` | method | `void` | public | This signal is emitted before any layers are added or removed. begin\_add\_or\_remove\_layers / end\_add\_or\_remove\_layers usually surrounds the addition or removal of one or more layers. |
| `end_add_or_remove_layers()` | method | `void` | public | This signal is emitted after layers have been added or removed. begin\_add\_or\_remove\_layers / end\_add\_or\_remove\_layers usually surrounds the addition or removal of one or more layers. |
| `layer_about_to_be_added( size_t index)` | method | `void` | public | This signal is emitted just before a new visual layer is added. |
| `layer_added( size_t index)` | method | `void` | public | This signal is emitted just after a new visual layer is added. |
| `layer_added( boost::weak_ptr<GPlatesPresentation::VisualLayer> visual_layer)` | method | `void` | public | This signal is emitted just after a new visual layer is added. |
| `layer_about_to_be_removed( size_t index)` | method | `void` | public | This signal is emitted just before a visual layer is removed. |
| `layer_about_to_be_removed( boost::weak_ptr<GPlatesPresentation::VisualLayer> visual_layer)` | method | `void` | public | This signal is emitted just before a visual layer is removed. |
| `layer_removed( size_t index)` | method | `void` | public | This signal is emitted just after a visual layer is removed. |
| `layer_modified( size_t index)` | method | `void` | public | This signal is emitted just after a visual layer's underlying reconstruct graph layer is modified. |
| `layer_modified( boost::weak_ptr<GPlatesPresentation::VisualLayer> visual_layer)` | method | `void` | public | layer\_modified(size\_t). |
| `changed()` | method | `void` | public | This signal is emitted after a visual layer has been added, removed or modified, or if the ordering of visual layers has changed. |
| `handle_begin_add_or_remove_layers()` | method | `void` | private | NOTE: all signals/slots should use namespace scope for all arguments otherwise differences between signals and slots will cause Qt to not be able to connect them at runtime. |
| `handle_end_add_or_remove_layers()` | method | `void` | private | — |
| `handle_layer_added( GPlatesAppLogic::ReconstructGraph &reconstruct_graph, GPlatesAppLogic::Layer layer)` | method | `void` | private | — |
| `handle_layer_about_to_be_removed( GPlatesAppLogic::ReconstructGraph &reconstruct_graph, GPlatesAppLogic::Layer layer)` | method | `void` | private | — |
| `handle_layer_removed( GPlatesAppLogic::ReconstructGraph &reconstruct_graph)` | method | `void` | private | — |
| `handle_layer_activation_changed( GPlatesAppLogic::ReconstructGraph &reconstruct_graph, GPlatesAppLogic::Layer layer, bool activation)` | method | `void` | private | — |
| `handle_layer_params_changed( GPlatesAppLogic::ReconstructGraph &reconstruct_graph, GPlatesAppLogic::Layer layer, GPlatesAppLogic::LayerParams &layer_params)` | method | `void` | private | — |
| `handle_layer_added_input_connection( GPlatesAppLogic::ReconstructGraph &reconstruct_graph, GPlatesAppLogic::Layer layer, GPlatesAppLogic::Layer::InputConnection input_connection)` | method | `void` | private | — |
| `handle_layer_removed_input_connection( GPlatesAppLogic::ReconstructGraph &reconstruct_graph, GPlatesAppLogic::Layer layer)` | method | `void` | private | — |
| `handle_file_state_changed( GPlatesAppLogic::FeatureCollectionFileState &file_state)` | method | `void` | private | — |
| `handle_default_reconstruction_tree_layer_changed( GPlatesAppLogic::ReconstructGraph &reconstruct_graph, GPlatesAppLogic::Layer prev_default_reconstruction_tree_layer, GPlatesAppLogic::Layer new_default_reconstruction_tree_layer)` | method | `void` | private | — |
| `visual_layer_ptr_type` | typedef | `boost::shared_ptr<VisualLayer>` | private | Typedef for a shared pointer to a VisualLayer. |
| `visual_layer_map_type` | typedef | `std::map<GPlatesAppLogic::Layer, visual_layer_ptr_type>` | private | Typedef for mapping a layer to a visual layer. |
| `index_map_type` | typedef | `std::map< GPlatesViewOperations::RenderedGeometryCollection::child_layer_index_type, boost::weak_ptr<VisualLayer> >` | private | Typedef for mapping a rendered geometry layer index to a visual layer. |
| `make_signal_slot_connections()` | method | `void` | private | — |
| `create_visual_layer( GPlatesAppLogic::Layer &layer)` | method | `visual_layer_ptr_type` | private | — |
| `add_layer( GPlatesAppLogic::Layer &layer)` | method | `void` | private | — |
| `remove_layer( const GPlatesAppLogic::Layer &layer)` | method | `void` | private | — |
| `handle_layer_modified( const GPlatesAppLogic::Layer &layer)` | method | `void` | private | — |
| `refresh_all_layers()` | method | `void` | private | — |
| `get_visual_layer( GPlatesViewOperations::RenderedGeometryCollection::child_layer_index_type index)` | method | `boost::weak_ptr<const VisualLayer>` | private | Returns the visual layer that owns the rendered geometry layer with the given index. |
| `get_index_of_new_layer( VisualLayerType::Type visual_layer_type)` | method | `std::size_t` | private | Calculates where a new layer of the given type should go in the ordering. |
| `emit_layer_modified( GPlatesViewOperations::RenderedGeometryCollection::child_layer_index_type index)` | method | `void` | private | Emits the layer\_modified signal, if index is found in the layer ordering. |
| `notify_visual_layer_params( const GPlatesAppLogic::Layer &layer)` | method | `void` | private | Notifies the corresponding visual layer params object about a change in layer. |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_view_state` | field | `ViewState` | private | — |
| `d_rendered_geometry_collection` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | — |
| `d_visual_layers` | field | `visual_layer_map_type` | private | Record of all visual layers associated with application state layers. |
| `d_layer_order` | field | `rendered_geometry_layer_seq_type` | private | A custom ordering of child layers in the RECONSTRUCTION\_LAYER. |
| `d_index_map` | field | `index_map_type` | private | Associates rendered geometry collection layer indices with a visual layer. |
| `d_next_visual_layer_number` | field | `int` | private | The number that will be given to the next visual layer created. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PRESENTATION_VISUALLAYERS_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=presentation/VisualLayers tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/GlobeRenderedGeometryCollectionPainter](../gui/GlobeRenderedGeometryCollectionPainter.md) | gui | 15 |
| [presentation/TranscribeSession](TranscribeSession.md) | presentation | 14 |
| [gui/MapRenderedGeometryCollectionPainter](../gui/MapRenderedGeometryCollectionPainter.md) | gui | 10 |
| [qt-widgets/MergeReconstructionLayersDialog](../qt-widgets/MergeReconstructionLayersDialog.md) | qt-widgets | 4 |
| [gui/VelocityLegendOverlay](../gui/VelocityLegendOverlay.md) | gui | 3 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 3 |
| [qt-widgets/DrawStyleDialog](../qt-widgets/DrawStyleDialog.md) | qt-widgets | 3 |
| [qt-widgets/GenerateDeformingMeshPointsDialog](../qt-widgets/GenerateDeformingMeshPointsDialog.md) | qt-widgets | 3 |
| [gui/CommandServer](../gui/CommandServer.md) | gui | 2 |
| [gui/ExportAnimationStrategy](../gui/ExportAnimationStrategy.md) | gui | 2 |
| [gui/ExportDeformationAnimationStrategy](../gui/ExportDeformationAnimationStrategy.md) | gui | 2 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 2 |
| [gui/ExportScalarCoverageAnimationStrategy](../gui/ExportScalarCoverageAnimationStrategy.md) | gui | 2 |
| [gui/ExportVelocityAnimationStrategy](../gui/ExportVelocityAnimationStrategy.md) | gui | 2 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 2 |
| [presentation/VisualLayer](VisualLayer.md) | presentation | 2 |
| [qt-widgets/AssignReconstructionPlateIdsDialog](../qt-widgets/AssignReconstructionPlateIdsDialog.md) | qt-widgets | 2 |
| [qt-widgets/TotalReconstructionPolesDialog](../qt-widgets/TotalReconstructionPolesDialog.md) | qt-widgets | 2 |
| [qt-widgets/VisualLayersComboBox](../qt-widgets/VisualLayersComboBox.md) | qt-widgets | 2 |
| [gui/Globe](../gui/Globe.md) | gui | 1 |

*... and 7 more units.*

## Related

**Qt signal/slot connections** (15 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&d_application_state` | `reconstructed( GPlatesAppLogic::ApplicationState &)` | `this` | `create_rendered_geometries()` |
| `reconstruct_graph` | `begin_add_or_remove_layers()` | `this` | `handle_begin_add_or_remove_layers()` |
| `reconstruct_graph` | `end_add_or_remove_layers()` | `this` | `handle_end_add_or_remove_layers()` |
| `reconstruct_graph` | `layer_added( GPlatesAppLogic::ReconstructGraph &, GPlatesAppLogic::Layer)` | `this` | `handle_layer_added( GPlatesAppLogic::ReconstructGraph &, GPlatesAppLogic::Layer)` |
| `reconstruct_graph` | `layer_about_to_be_removed( GPlatesAppLogic::ReconstructGraph &, GPlatesAppLogic::Layer)` | `this` | `handle_layer_about_to_be_removed( GPlatesAppLogic::ReconstructGraph &, GPlatesAppLogic::Layer)` |
| `reconstruct_graph` | `layer_removed( GPlatesAppLogic::ReconstructGraph &)` | `this` | `handle_layer_removed( GPlatesAppLogic::ReconstructGraph &)` |
| `reconstruct_graph` | `layer_activation_changed( GPlatesAppLogic::ReconstructGraph &, GPlatesAppLogic::Layer, bool)` | `this` | `handle_layer_activation_changed( GPlatesAppLogic::ReconstructGraph &, GPlatesAppLogic::Layer, bool)` |
| `reconstruct_graph` | `layer_params_changed( GPlatesAppLogic::ReconstructGraph &, GPlatesAppLogic::Layer, GPlatesAppLogic::LayerParams &)` | `this` | `handle_layer_params_changed( GPlatesAppLogic::ReconstructGraph &, GPlatesAppLogic::Layer, GPlatesAppLogic::LayerParams &)` |
| `reconstruct_graph` | `layer_added_input_connection( GPlatesAppLogic::ReconstructGraph &, GPlatesAppLogic::Layer, GPlatesAppLogic::Layer::InputConnection)` | `this` | `handle_layer_added_input_connection( GPlatesAppLogic::ReconstructGraph &, GPlatesAppLogic::Layer, GPlatesAppLogic::Layer::InputConnection)` |
| `reconstruct_graph` | `layer_removed_input_connection( GPlatesAppLogic::ReconstructGraph &, GPlatesAppLogic::Layer)` | `this` | `handle_layer_removed_input_connection( GPlatesAppLogic::ReconstructGraph &, GPlatesAppLogic::Layer)` |
| `reconstruct_graph` | `default_reconstruction_tree_layer_changed( GPlatesAppLogic::ReconstructGraph &, GPlatesAppLogic::Layer, GPlatesAppLogic::Layer)` | `this` | `handle_default_reconstruction_tree_layer_changed( GPlatesAppLogic::ReconstructGraph &, GPlatesAppLogic::Layer, GPlatesAppLogic::Layer)` |
| `file_state` | `file_state_changed( GPlatesAppLogic::FeatureCollectionFileState &)` | — | `handle_file_state_changed( GPlatesAppLogic::FeatureCollectionFileState &)` |
| `&d_view_state.get_rendered_geometry_parameters()` | `parameters_changed(GPlatesViewOperations::RenderedGeometryParameters &)` | `this` | `create_rendered_geometries()` |
| `&d_view_state.get_render_settings()` | `settings_changed()` | `this` | `create_rendered_geometries()` |
| `GPlatesGui::DrawStyleManager::instance()` | `draw_style_changed()` | `this` | `create_rendered_geometries()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/presentation/VisualLayers.h
python scripts/gpq.py def GPlatesPresentation::VisualLayers --body
python scripts/gpq.py uses VisualLayers --kind class
python scripts/gpq.py hier VisualLayers
```
