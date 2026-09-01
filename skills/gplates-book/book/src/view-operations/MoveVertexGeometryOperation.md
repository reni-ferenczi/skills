# MoveVertexGeometryOperation

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 196 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/MoveVertexGeometryOperation.h` | C++ | 447 |
| `src/view-operations/MoveVertexGeometryOperation.cc` | C++ | 702 |

## Overview

[[[PROSE overview unit=view-operations/MoveVertexGeometryOperation tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::MoveVertexGeometryOperation`](#gplatesviewoperationsmovevertexgeometryoperation) | class | [`GeometryOperation`](GeometryOperation.md)<br>`boost::noncopyable` | — | 0 | Moves a vertex in GeometryBuilder and adds RenderedGeometry objects to RenderedGeometryCollection. |

## Members

### `GPlatesViewOperations::MoveVertexGeometryOperation`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ReconstructionGeometryFinder` | class | `None` | public | Visitor to find a rendered geometry's reconstruction geometry. |
| `RenderedGeometryLayerFiller` | class | `None` | public | A visitor to add rendered geometries to the points and lines layers provided in the constructor. |
| `MoveVertexGeometryOperation( GeometryBuilder &geometry_builder, GPlatesCanvasTools::GeometryOperationState &geometry_operation_state, GPlatesCanvasTools::ModifyGeometryState &modify_geometry_state, RenderedGeometryCollection &rendered_geometry_collection, RenderedGeometryCollection::MainLayerType main_rendered_layer_ty ...` | constructor | `None` | public | — |
| `activate()` | method | `void` | public | Activate this operation. |
| `deactivate()` | method | `void` | public | Deactivate this operation. |
| `left_press( const GPlatesMaths::PointOnSphere &oriented_pos_on_sphere, const double &closeness_inclusion_threshold)` | method | `void` | public | — |
| `start_drag( const GPlatesMaths::PointOnSphere &oriented_pos_on_sphere, const double &closeness_inclusion_threshold)` | method | `void` | public | User has just clicked and dragged on the sphere. |
| `update_drag( const GPlatesMaths::PointOnSphere &oriented_pos_on_sphere)` | method | `void` | public | User is currently in the middle of dragging the mouse. |
| `end_drag( const GPlatesMaths::PointOnSphere &oriented_pos_on_sphere)` | method | `void` | public | User has released mouse button after dragging. |
| `release_click()` | method | `void` | public | User has released the mouse without a drag. |
| `mouse_move( const GPlatesMaths::PointOnSphere &oriented_pos_on_sphere, const double &closeness_inclusion_threshold)` | method | `void` | public | The mouse has moved but it is not a drag because mouse button is not pressed. |
| `geometry_builder_stopped_updating_geometry()` | method | `void` | public | NOTE: all signals/slots should use namespace scope for all arguments otherwise differences between signals and slots will cause Qt to not be able to connect them at runtime. |
| `handle_snap_vertices_setup_changed( bool should_check_nearby_vertices, double threshold, bool should_use_plate_id, GPlatesModel::integer_plate_id_type plate_id)` | method | `void` | private | This will transfer any user-provided move-nearby-vertex information from the task panel tab. |
| `d_geometry_builder` | field | `GeometryBuilder` | private | This is used to build geometry. |
| `d_geometry_operation_state` | field | `GPlatesCanvasTools::GeometryOperationState` | private | We call this when we activate/deactivate. |
| `d_rendered_geometry_collection` | field | `RenderedGeometryCollection` | private | This is where we render our geometries and activate our render layer. |
| `d_main_rendered_layer_type` | field | `RenderedGeometryCollection::MainLayerType` | private | The main rendered layer we're currently rendering into. |
| `d_lines_layer_ptr` | field | `RenderedGeometryCollection::child_layer_owner_ptr_type` | private | Rendered geometry layer used for lines. |
| `d_points_layer_ptr` | field | `RenderedGeometryCollection::child_layer_owner_ptr_type` | private | Rendered geometry layer used for points. |
| `d_highlight_point_layer_ptr` | field | `RenderedGeometryCollection::child_layer_owner_ptr_type` | private | Rendered geometry layer used for the single highlighted point (the point that the mouse cursor is currently hovering over if any). |
| `d_canvas_tool_workflows` | field | `GPlatesGui::CanvasToolWorkflows` | private | Used by undo/redo to make sure appropriate tool is active when the undo/redo happens. |
| `d_query_proximity_threshold` | field | `QueryProximityThreshold` | private | Used to query the proximity threshold based on position on globe. |
| `d_move_vertex_command_id` | field | `UndoRedo::CommandId` | private | Unique command id used to merge move vertex commands together. |
| `d_selected_vertex_index` | field | `unsigned int` | private | Index of vertex selected by user. |
| `d_is_vertex_selected` | field | `bool` | private | Has the user selected a vertex. |
| `d_is_vertex_highlighted` | field | `bool` | private | Is the user hovering over a vertex |
| `d_should_check_nearby_vertices` | field | `bool` | private | Does the user want to check nearby vertices of other geometries |
| `d_should_use_plate_id_filter` | field | `bool` | private | Does the user want to filter other geometries by plate-id |
| `d_nearby_vertex_threshold` | field | `double` | private | Proximity threshold (degrees of arc)for checking nearby vertices. |
| `d_feature_focus` | field | `GPlatesGui::FeatureFocus` | private | Used to retrieve focused geometry when snapping vertices. |
| `d_filter_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | Plate-id provided by user for restricting nearby features to check |
| `move_vertex( const GPlatesMaths::PointOnSphere &oriented_pos_on_sphere, bool is_intermediate_move)` | method | `void` | private | Perform the actual move vertex command. |
| `test_proximity_to_points( const GPlatesMaths::PointOnSphere &oriented_pos_on_sphere, const double &closeness_inclusion_threshold)` | method | `boost::optional<RenderedGeometryProximityHit>` | private | Test proximity to the points (at vertices) to the position on sphere and return closest point if at least one point was close enough, otherwise false. |
| `connect_to_geometry_builder_signals()` | method | `void` | private | — |
| `disconnect_from_geometry_builder_signals()` | method | `void` | private | — |
| `create_rendered_geometry_layers()` | method | `void` | private | — |
| `update_rendered_geometries()` | method | `void` | private | Update all RenderedGeometry objects. |
| `update_rendered_geometry( GeometryBuilder::GeometryIndex geom_index)` | method | `void` | private | — |
| `update_rendered_polyline_on_sphere( GeometryBuilder::GeometryIndex geom_index)` | method | `void` | private | — |
| `update_rendered_polygon_on_sphere( GeometryBuilder::GeometryIndex geom_index)` | method | `void` | private | — |
| `add_rendered_points( GeometryBuilder::GeometryIndex geom_index)` | method | `void` | private | — |
| `add_rendered_lines_for_polygon_on_sphere( GeometryBuilder::GeometryIndex geom_index)` | method | `void` | private | — |
| `add_rendered_lines_for_polyline_on_sphere( GeometryBuilder::GeometryIndex geom_index)` | method | `void` | private | — |
| `update_highlight_rendered_point( const GeometryBuilder::PointIndex highlight_point_index)` | method | `void` | private | — |
| `update_secondary_geometries( const GPlatesMaths::PointOnSphere &point_on_sphere)` | method | `void` | private | Checks for nearby vertices in other geometries, and sends any results to the geometry builder. |
| `update_rendered_secondary_geometries()` | method | `void` | private | Adds any secondary geometries in the geometry\_builder to the appropriate rendered layers. |
| `update_highlight_secondary_vertices()` | method | `void` | private | Highlight any secondary geometry vertices which might be moved. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_MOVEVERTEXGEOMETRYOPERATION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=view-operations/MoveVertexGeometryOperation tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [canvas-tools/MoveVertex](../canvas-tools/MoveVertex.md) | canvas-tools | 10 |
| [app-logic/TopologyGeometryResolverLayerProxy](../app-logic/TopologyGeometryResolverLayerProxy.md) | app-logic | 3 |
| [app-logic/TopologyNetworkResolverLayerProxy](../app-logic/TopologyNetworkResolverLayerProxy.md) | app-logic | 3 |
| [app-logic/TopologyUtils](../app-logic/TopologyUtils.md) | app-logic | 2 |
| [app-logic/ResolvedTopologicalSubSegmentImpl](../app-logic/ResolvedTopologicalSubSegmentImpl.md) | app-logic | 1 |
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 1 |
| [file-io/ResolvedTopologicalGeometryExport](../file-io/ResolvedTopologicalGeometryExport.md) | file-io | 1 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 1 |
| [view-operations/RenderedGeometryUtils](RenderedGeometryUtils.md) | view-operations | 1 |

## Related

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&modify_geometry_state` | `snap_vertices_setup_changed( bool,double,bool,GPlatesModel::integer_plate_id_type)` | `this` | `handle_snap_vertices_setup_changed( bool,double,bool,GPlatesModel::integer_plate_id_type)` |
| `&d_geometry_builder` | `stopped_updating_geometry()` | `this` | `geometry_builder_stopped_updating_geometry()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/MoveVertexGeometryOperation.h
python scripts/gpq.py def GPlatesViewOperations::MoveVertexGeometryOperation --body
python scripts/gpq.py uses MoveVertexGeometryOperation --kind class
python scripts/gpq.py hier MoveVertexGeometryOperation
```
