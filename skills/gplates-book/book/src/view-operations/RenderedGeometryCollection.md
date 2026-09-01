# RenderedGeometryCollection

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 434 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedGeometryCollection.h` | C++ | 884 |
| `src/view-operations/RenderedGeometryCollection.cc` | C++ | 776 |

## Overview

[[[PROSE overview unit=view-operations/RenderedGeometryCollection tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::(anonymous)::RenderedGeometryCollectionManager`](#gplatesviewoperationsanonymousrenderedgeometrycollectionmanager) | class | [`GPlatesUtils::Singleton<RenderedGeometryCollectionManager>`](../utils/Singleton.md) | — | 0 | Singleton instance to keep track of RenderedGeometryCollection objects. |
| [`GPlatesViewOperations::RenderedGeometryCollection`](#gplatesviewoperationsrenderedgeometrycollection) | class | `QObject`<br>`boost::noncopyable` | — | 0 | There are also implementations for multipoint, polyline and polygon. \* RenderedReconstructionGeometry is an implementation type of RenderedGeometry that is used to wrap a reconstruction geometry. |

## Members

### `GPlatesViewOperations::(anonymous)::RenderedGeometryCollectionManager`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `collection_seq_type` | typedef | `std::list<RenderedGeometryCollection *>` | public | Typedef for sequence of RenderedGeometryCollection pointers. |
| `register_collection( RenderedGeometryCollection *rendered_geom_collection)` | method | `void` | public | — |
| `unregister_collection( RenderedGeometryCollection *rendered_geom_collection)` | method | `void` | public | — |
| `d_registered_collections` | field | `collection_seq_type` | private | — |

### `GPlatesViewOperations::RenderedGeometryCollection`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MainLayerType` | enum | `None` | public | The main render layers. |
| `orthogonal_main_layers_type` | typedef | `std::bitset<NUM_LAYERS>` | public | A std::bitset for setting which main layers are orthogonal. |
| `main_layers_update_type` | typedef | `std::bitset<NUM_LAYERS>` | public | A std::bitset for querying which main layers were updated. |
| `child_layer_index_type` | typedef | `unsigned int` | public | Typedef for an index to a child rendered layer. |
| `child_layer_index_seq_type` | typedef | `std::list<child_layer_index_type>` | public | Typedef for a sequence of child layer indices. |
| `child_layer_owner_ptr_type` | typedef | `boost::shared_ptr<RenderedGeometryLayer>` | public | Typedef for a handle that owns a child layer. |
| `ALL_MAIN_LAYERS` | field | `main_layers_update_type` | public | Specifies all main layers. |
| `RenderedGeometryCollection()` | constructor | `None` | public | — |
| `~RenderedGeometryCollection()` | destructor | `None` | public | — |
| `set_viewport_zoom_factor( const double &viewport_zoom_factor)` | method | `void` | public | Sets the viewport zoom factor. |
| `get_main_rendered_layer( MainLayerType)` | method | `RenderedGeometryLayer` | public | Get the RenderedGeometryLayer corresponding to specified main layer. |
| `create_child_rendered_layer( MainLayerType parent_layer)` | method | `child_layer_index_type` | public | Create a rendered layer that is a child of the specified main rendered layer. |
| `create_child_rendered_layer( MainLayerType parent_layer, float ratio_zoom_dependent_bin_dimension_to_globe_radius)` | method | `child_layer_index_type` | public | Same as the other overload of create\_child\_rendered\_layer except the density of some types of rendered geometries is uniformly spaced. |
| `destroy_child_rendered_layer( child_layer_index_type, MainLayerType parent_layer)` | method | `void` | public | Destroy a rendered layer created with create\_child\_rendered\_layer(). |
| `transfer_ownership_of_child_rendered_layer( child_layer_index_type child_layer_index, MainLayerType parent_layer)` | method | `child_layer_owner_ptr_type` | public | Transfers ownership of a child rendered layer to the object returned. |
| `create_child_rendered_layer_and_transfer_ownership( MainLayerType parent_layer)` | method | `child_layer_owner_ptr_type` | public | Yet another convenience method - creates child rendered layer and transfers ownership to returned pointer type. |
| `create_child_rendered_layer_and_transfer_ownership( MainLayerType parent_layer, float ratio_zoom_dependent_bin_dimension_to_globe_radius)` | method | `child_layer_owner_ptr_type` | public | Same as the other overload of create\_child\_rendered\_layer\_and\_transfer\_ownership except the density of some types of rendered geometries is uniformly spaced. |
| `get_child_rendered_layer( child_layer_index_type)` | method | `RenderedGeometryLayer` | public | Get the RenderedGeometryLayer corresponding to specified child layer. |
| `get_child_rendered_layer_indices` | field | `child_layer_index_seq_type` | public | Get the sequence of child layer indices for the given parent layer. |
| `set_main_layer_active( MainLayerType main_layer_type, bool active = true)` | method | `void` | public | Set a specific main layer as active/inactive. |
| `is_main_layer_active( MainLayerType main_layer_type)` | method | `bool` | public | See if a specific main layer is currently active. |
| `set_orthogonal_main_layers( orthogonal_main_layers_type orthogonal_main_layers)` | method | `void` | public | Specify which main layers are orthogonal to each other in terms of activation. |
| `get_orthogonal_main_layers()` | method | `orthogonal_main_layers_type` | public | Returns group of main layers that are orthogonal to each other in activation terms. |
| `MainLayerActiveState` | class | `None` | public | Opaque type contains main layer active state for all main layers. |
| `capture_main_layer_active_state()` | method | `MainLayerActiveState` | public | Capture active status of all main layers for later restore. |
| `restore_main_layer_active_state( MainLayerActiveState main_layer_active_state)` | method | `void` | public | Restores active status of all main layers. |
| `accept_visitor( ConstRenderedGeometryCollectionVisitor<ForwardReadableRange> &)` | method | `void` | public | Recursively visit the main rendered layers, their child rendered layers and the RenderedGeometry objects in them. |
| `accept_visitor( RenderedGeometryCollectionVisitor<ForwardReadableRange> &)` | method | `void` | public | Recursively visit the main rendered layers, their child rendered layers and the RenderedGeometry objects in them. |
| `begin_update_collection()` | method | `void` | public | @{ Delays signaling updates to observers. |
| `end_update_collection()` | method | `void` | public | — |
| `begin_update_all_registered_collections()` | method | `void` | public | @{ Delays signaling updates to observers for all registered collections. |
| `end_update_all_registered_collections()` | method | `void` | public | — |
| `UpdateGuard` | struct | `None` | public | A convenience structure for automating calls to begin\_update\_collection() and end\_update\_collection() in a scope block. |
| `rendered_geometry_layer_was_updated( GPlatesViewOperations::RenderedGeometryLayer &, GPlatesViewOperations::RenderedGeometryLayer::user_data_type)` | method | `void` | public | Called when a RenderedGeometryLayer is modified. |
| `collection_was_updated( GPlatesViewOperations::RenderedGeometryCollection &rendered_geom_collection, GPlatesViewOperations::RenderedGeometryCollection::main_layers_update_type main_layers_updated)` | method | `void` | public | Signal is emitted whenever this rendered geometry collection has been updated. |
| `main_layer_active_state_internal_type` | typedef | `std::bitset<NUM_LAYERS>` | private | Type contains main layer active state. |
| `RenderedGeometryLayerManager` | class | `None` | private | — |
| `MainLayer` | struct | `None` | private | — |
| `main_layer_seq_type` | typedef | `std::vector<MainLayer>` | private | Typedef for sequence of main rendered geometry layers. |
| `d_current_viewport_zoom_factor` | field | `double` | private | Current viewport zoom factor. |
| `d_rendered_geometry_layer_manager` | field | `RenderedGeometryLayerManager` | private | Manages creation and destruction of RenderedGeometryLayer objects. |
| `d_main_layer_seq` | field | `main_layer_seq_type` | private | Sequence of main rendered layers. |
| `d_main_layer_active_state` | field | `main_layer_active_state_internal_type` | private | Bitwise 'or' of main layer flags showing which are active. |
| `d_main_layers_orthogonal` | field | `orthogonal_main_layers_type` | private | If any main layer is activated that is in this group then the others in the group are automatically deactivated. |
| `d_update_collection_depth` | field | `int` | private | Used by begin\_update\_collection and end\_update\_collection to keep track of the nested call depth. |
| `d_update_collection_depth_mutex` | field | `boost::mutex` | private | — |
| `d_update_notify_queued` | field | `bool` | private | Is true if an update to rendered geometry collection occurred inside a begin\_update\_collection / end\_update\_collection block. |
| `d_main_layers_updated` | field | `main_layers_update_type` | private | Keeps track of which main layers have been updated since the last collection\_was\_updated signal was emitted. |
| `send_update_signal()` | method | `void` | private | Does the actual 'emit' of the collection\_was\_updated signal. |
| `delay_update_notification()` | method | `bool` | private | Should we delay signaling our observers that we've been updated? |
| `signal_update( MainLayerType main_layer_type)` | method | `void` | private | Signal to our observers that we've been updated. |
| `signal_update( main_layers_update_type main_layers_updated)` | method | `void` | private | Signal to our observers that we've been updated. |
| `accept_visitor_internal( RenderedGeometryCollectionVisitorType &visitor, RenderedGeometryCollectionType &rendered_geom_collection)` | method | `void` | private | — |
| `visit_main_rendered_layer( RenderedGeometryCollectionVisitorType &visitor, MainLayerType main_layer_type, RenderedGeometryCollectionType &rendered_geom_collection)` | method | `void` | private | — |
| `visit_main_rendered_layer( RenderedGeometryCollectionVisitorType &visitor, RenderedGeometryCollectionType &rendered_geom_collection, const ChildLayerIndexRangeType &children_range)` | method | `void` | private | — |
| `visit_rendered_geometry_layer( RenderedGeometryCollectionVisitorType &visitor, RenderedGeometryLayerType &rendered_geom_layer)` | method | `void` | private | — |
| `connect_child_rendered_layer_to_parent( const child_layer_index_type child_layer_index, MainLayerType parent_layer)` | method | `void` | private | Does everything required to connect a newly created child rendered layer to its parent layer. |
| `connect_to_rendered_geometry_layer_signal( RenderedGeometryLayer *rendered_geom_layer)` | method | `void` | private | Observe specified RenderedGeometryLayer for updates. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `ALL_MAIN_LAYERS` | variable | `GPlatesViewOperations::RenderedGeometryCollection::main_layers_update_type` | — |
| `GPLATES_VIEWOPERATIONS_RENDEREDGEOMETRYCOLLECTION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=view-operations/RenderedGeometryCollection tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [view-operations/RenderedGeometryUtils](RenderedGeometryUtils.md) | view-operations | 124 |
| [qt-widgets/HellingerDialog](../qt-widgets/HellingerDialog.md) | qt-widgets | 43 |
| [view-operations/RenderedGeometryProximity](RenderedGeometryProximity.md) | view-operations | 43 |
| [presentation/VisualLayers](../presentation/VisualLayers.md) | presentation | 28 |
| [canvas-tools/AdjustFittedPoleEstimate](../canvas-tools/AdjustFittedPoleEstimate.md) | canvas-tools | 25 |
| [qt-widgets/ModifyReconstructionPoleWidget](../qt-widgets/ModifyReconstructionPoleWidget.md) | qt-widgets | 23 |
| [canvas-tools/MeasureDistance](../canvas-tools/MeasureDistance.md) | canvas-tools | 20 |
| [canvas-tools/SelectHellingerGeometries](../canvas-tools/SelectHellingerGeometries.md) | canvas-tools | 20 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 20 |
| [qt-widgets/deprecated/CreateTopologyWidget](../qt-widgets/deprecated/CreateTopologyWidget.md) | qt-widgets | 20 |
| [view-operations/DeleteVertexGeometryOperation](DeleteVertexGeometryOperation.md) | view-operations | 19 |
| [view-operations/InsertVertexGeometryOperation](InsertVertexGeometryOperation.md) | view-operations | 19 |
| [view-operations/RenderedGeometryCollectionVisitor](RenderedGeometryCollectionVisitor.md) | view-operations | 17 |
| [view-operations/AddPointGeometryOperation](AddPointGeometryOperation.md) | view-operations | 16 |
| [view-operations/MovePoleOperation](MovePoleOperation.md) | view-operations | 16 |
| [view-operations/MoveVertexGeometryOperation](MoveVertexGeometryOperation.md) | view-operations | 16 |
| [canvas-tools/CreateSmallCircle](../canvas-tools/CreateSmallCircle.md) | canvas-tools | 14 |
| [app-logic/deprecated/PlateVelocityWorkflow](../app-logic/deprecated/PlateVelocityWorkflow.md) | app-logic | 13 |
| [gui/GlobeRenderedGeometryCollectionPainter](../gui/GlobeRenderedGeometryCollectionPainter.md) | gui | 13 |
| [view-operations/ChangeLightDirectionOperation](ChangeLightDirectionOperation.md) | view-operations | 13 |

*... and 49 more units.*

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `rendered_geom_layer` | `layer_was_updated( GPlatesViewOperations::RenderedGeometryLayer &, GPlatesViewOperations::RenderedGeometryLayer::user_data_type)` | `this` | `rendered_geometry_layer_was_updated( GPlatesViewOperations::RenderedGeometryLayer &, GPlatesViewOperations::RenderedGeometryLayer::user_data_type)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedGeometryCollection.h
python scripts/gpq.py def GPlatesViewOperations::RenderedGeometryCollection --body
python scripts/gpq.py uses RenderedGeometryCollection --kind class
python scripts/gpq.py hier RenderedGeometryCollection
```
