# RenderedGeometryCollection

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 434 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedGeometryCollection.h` | C++ | 884 |
| `src/view-operations/RenderedGeometryCollection.cc` | C++ | 776 |

## Overview

This is the scene graph of GPlates, and the seam between everything that
*computes* and everything that *draws*. App-logic results, canvas-tool feedback,
measurement overlays and highlight decorations all end up here as
`RenderedGeometry` objects; the globe and map painters
(`GPlatesGui::GlobeRenderedGeometryCollectionPainter` and its map counterpart)
read them back by walking the collection with a
`RenderedGeometryCollectionVisitor`. Nothing else connects the two halves: a
producer never calls the canvas, it drops geometry into a layer and the
collection's `collection_was_updated` signal tells the canvas to redraw.

The structure is deliberately two-level. There is one fixed main layer per
`MainLayerType` — one for reconstruction output, one per canvas-tool workflow —
each with an embedded default `RenderedGeometryLayer` that needs no creation, and
each able to hold explicitly created child layers. The nesting exists purely to
pin down draw order without a depth buffer: main layers are visited in enum
declaration order, a main layer's own geometries before its children, and children
in creation order (unless the visitor overrides it via
`get_custom_child_layers_order`). That is why the move-vertex tool puts base
geometry in one child layer and the grabbable vertex highlights in another — it is
the only guarantee the highlights land on top. Activation is likewise two-level
and conjunctive: a `RenderedGeometryLayer` is drawn only if both it and its main
layer are active. `set_orthogonal_main_layers` turns a chosen set of main layers
into a radio group, which is how switching canvas-tool workflow deactivates the
previous workflow's whole subtree in one call rather than layer by layer.

The one instance lives in `GPlatesPresentation::ViewState` as a `scoped_ptr`.
Child layers, by contrast, are handed out as bare `child_layer_index_type`
indices into a private `RenderedGeometryLayerManager` slot table; the
`transfer_ownership_of_child_rendered_layer` family wraps that index in a
`boost::shared_ptr<RenderedGeometryLayer>` whose deleter calls
`destroy_child_rendered_layer`, so almost every client holds a
`child_layer_owner_ptr_type` and never destroys anything by hand. Update
notification is aggregated rather than immediate: each `RenderedGeometryLayer`
carries the `MainLayerType` of its owning main layer as opaque `user_data`, hands
it back in `layer_was_updated`, and the collection ORs that bit into
`d_main_layers_updated` so a single `collection_was_updated` can tell observers
exactly which main layers changed.

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

- **`UpdateGuard` is global, not per-collection.** Its constructor calls
  `begin_update_all_registered_collections()`, so it suppresses update signals on
  *every* `RenderedGeometryCollection` that exists, via the file-local
  `RenderedGeometryCollectionManager` singleton every collection registers with in
  its constructor. Guards nest and only the outermost exit emits. Omitting a guard
  is never a correctness bug — it just means more redraws — but placing one around
  a long-running loop that also touches another collection will silently freeze
  that collection's updates too.
- **The update signal is a coalesced summary, not an event log.** `signal_update`
  accumulates into `d_main_layers_updated` and `send_update_signal` clears it
  after emitting. An observer that misses or ignores one `collection_was_updated`
  has no way to recover what changed; the intended usage is to re-traverse.
- **Active state is not a property of the collection as far as traversal is
  concerned.** `accept_visitor` does *not* skip inactive layers. The visitor is
  handed the main layer and the `RenderedGeometryLayer` and decides for itself, by
  returning false from `visit_main_rendered_layer` / `visit_rendered_geometry_layer`
  — deliberately, so exporters can render everything regardless of what the user
  currently sees. A new visitor that forgets to test active status will draw
  hidden layers.
- **`restore_main_layer_active_state` reports nothing as changed.** It assigns
  `d_main_layer_active_state` before computing the XOR against it, so the bitset
  passed to `signal_update` is always empty. The signal still fires (through the
  enclosing guard), but the "which main layers changed" bits are lost;
  `set_main_layer_active` gets this right by snapshotting first.
- **Child layer indices are recycled.** `RenderedGeometryLayerManager` pushes
  freed slots onto a reuse stack, so an index held past
  `destroy_child_rendered_layer` will later refer to a *different* layer rather
  than fail. This is the main reason to take ownership through
  `child_layer_owner_ptr_type` instead of passing raw indices around. The manager's
  create and destroy paths are explicitly marked as not exception-safe.
- **Threading.** `d_update_collection_depth_mutex` guards only the increment and
  decrement of the nesting counter; the depth is then re-read outside the lock,
  and everything else — layer mutation, visitor traversal, signal emission — is
  unsynchronised. Treat the whole class as GUI-thread-only; the mutex does not
  make it shareable.
- **Enum ordering is load-bearing.** `MainLayerType` doubles as the visit order
  and as the index into `d_main_layer_seq`, and `NUM_LAYERS` sizes both that
  vector and every `std::bitset` typedef. Reordering the enumerators changes draw
  order; inserting one anywhere but before `NUM_LAYERS` breaks it. Traversal casts
  a loop counter straight back to `MainLayerType`.
- **Zoom-dependent child layers need feeding.** A layer created with a
  `ratio_zoom_dependent_bin_dimension_to_globe_radius` decimates points per sample
  bin, and the bin size is derived from the zoom factor pushed down by
  `set_viewport_zoom_factor`. If the zoom changes and that call is not made, the
  decimation silently uses a stale scale.
- `UpdateGuard::~UpdateGuard` swallows all exceptions, and the destructor
  unregisters from the singleton, so a collection must not outlive the singleton's
  teardown.

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
