# InsertVertexGeometryOperation

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 309 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/InsertVertexGeometryOperation.h` | C++ | 307 |
| `src/view-operations/InsertVertexGeometryOperation.cc` | C++ | 804 |

## Overview

`InsertVertexGeometryOperation` is the `GeometryOperation` behind the "Insert Vertex" canvas tool. On `left_click` it first tests proximity against the line-segments `RenderedGeometryLayer`; a hit projects the click onto that segment (`project_point_onto_line_segment`) and inserts there via `insert_vertex_on_line_segment`, while a miss falls through to `insert_vertex_off_line_segment`, which appends the new vertex at whichever end of the geometry `get_closest_geometry_end_point_to` finds nearer to the click. Every insertion is pushed as a `GeometryBuilderInsertPointUndoCommand` (from `GeometryBuilderUndoCommands`) alongside a `GPlatesGui::ChooseCanvasToolUndoCommand` that restores the Insert Vertex tool itself via `d_canvas_tool_workflows` when the edit is undone or redone, so vertex insertion is part of the shared undo/redo history rather than a private one.

It maintains three rendered layers — line segments, points, and a single highlight layer for whichever point or segment the cursor is closest to — which it fully rebuilds from `GeometryBuilder` state whenever the builder signals `stopped_updating_geometry`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::InsertVertexGeometryOperation`](#gplatesviewoperationsinsertvertexgeometryoperation) | class | [`GeometryOperation`](GeometryOperation.md)<br>`boost::noncopyable` | — | 0 | Deletes a vertex in GeometryBuilder and manages RenderedGeometry objects in a RenderedGeometryCollection layer. |

## Members

### `GPlatesViewOperations::InsertVertexGeometryOperation`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InsertVertexGeometryOperation( GeometryBuilder &geometry_builder, GPlatesCanvasTools::GeometryOperationState &geometry_operation_state, RenderedGeometryCollection &rendered_geometry_collection, RenderedGeometryCollection::MainLayerType main_rendered_layer_type, GPlatesGui::CanvasToolWorkflows &canvas_tool_workflows, co ...` | constructor | `None` | public | — |
| `activate()` | method | `void` | public | Activate this operation. |
| `deactivate()` | method | `void` | public | Deactivate this operation. |
| `left_click( const GPlatesMaths::PointOnSphere &oriented_pos_on_sphere, const double &closeness_inclusion_threshold)` | method | `void` | public | User has just clicked on the sphere. |
| `mouse_move( const GPlatesMaths::PointOnSphere &oriented_pos_on_sphere, const double &closeness_inclusion_threshold)` | method | `void` | public | The mouse has moved but it is not a drag because mouse button is not pressed. |
| `geometry_builder_stopped_updating_geometry()` | method | `void` | public | NOTE: all signals/slots should use namespace scope for all arguments otherwise differences between signals and slots will cause Qt to not be able to connect them at runtime. |
| `ClosestEndPoint` | enum | `None` | private | Enumeration for the closest end point of the geometry to the insertion point. |
| `d_geometry_builder` | field | `GeometryBuilder` | private | This is used to build geometry. |
| `d_geometry_operation_state` | field | `GPlatesCanvasTools::GeometryOperationState` | private | We call this when we activate/deactivate. |
| `d_rendered_geometry_collection` | field | `RenderedGeometryCollection` | private | This is where we render our geometries and activate our render layer. |
| `d_main_rendered_layer_type` | field | `RenderedGeometryCollection::MainLayerType` | private | The main rendered layer we're currently rendering into. |
| `d_line_segments_layer_ptr` | field | `RenderedGeometryCollection::child_layer_owner_ptr_type` | private | Rendered geometry layer used for line segments. |
| `d_points_layer_ptr` | field | `RenderedGeometryCollection::child_layer_owner_ptr_type` | private | Rendered geometry layer used for points. |
| `d_highlight_layer_ptr` | field | `RenderedGeometryCollection::child_layer_owner_ptr_type` | private | Rendered geometry layer used for the single highlighted point (the point that the mouse cursor is currently hovering over if any). |
| `d_line_to_point_mapping` | field | `std::vector<GeometryBuilder::PointIndex>` | private | A mapping from rendered line segment indices to point indices, such that the i-th element of this vector is the index of the point at the beginning of the i-th rendered line segment. |
| `d_canvas_tool_workflows` | field | `GPlatesGui::CanvasToolWorkflows` | private | Used by undo/redo to make sure appropriate tool is active when the undo/redo happens. |
| `d_query_proximity_threshold` | field | `QueryProximityThreshold` | private | Used to query the proximity threshold based on position on globe. |
| `insert_vertex_on_line_segment( const unsigned int line_segment_index, const GPlatesMaths::PointOnSphere &oriented_pos_on_sphere, const double &closeness_inclusion_threshold)` | method | `void` | private | Insert a vertex on the specified line segment. |
| `insert_vertex_off_line_segment( const GPlatesMaths::PointOnSphere &oriented_pos_on_sphere)` | method | `void` | private | Insert a vertex off the specified line segment. |
| `insert_vertex( const GeometryBuilder::PointIndex insert_vertex_index, const GPlatesMaths::PointOnSphere &insert_pos_on_sphere)` | method | `void` | private | Perform the actual insert vertex command. |
| `project_point_onto_line_segment( const unsigned int line_segment_index, const GPlatesMaths::PointOnSphere &oriented_pos_on_sphere)` | method | `GPlatesMaths::PointOnSphere` | private | Projects the specified point onto the specified line segment. |
| `test_proximity_to_rendered_geom_layer( const RenderedGeometryLayer &rendered_geom_layer, const GPlatesMaths::PointOnSphere &oriented_pos_on_sphere, const double &closeness_inclusion_threshold)` | method | `boost::optional<GPlatesViewOperations::RenderedGeometryProximityHit>` | private | Tests proximity of specified point to the rendered geometries in the specified rendered geometry layer. |
| `get_closest_geometry_end_point_to( const GPlatesMaths::PointOnSphere &oriented_pos_on_sphere)` | method | `boost::optional<ClosestEndPoint>` | private | Determines which end point (in geometry contained in our geometry builder) is closest to the specified point. |
| `connect_to_geometry_builder_signals()` | method | `void` | private | — |
| `disconnect_from_geometry_builder_signals()` | method | `void` | private | — |
| `create_rendered_geometry_layers()` | method | `void` | private | — |
| `update_rendered_geometries()` | method | `void` | private | Update all RenderedGeometry objects. |
| `update_rendered_geometry( GeometryBuilder::GeometryIndex geom_index)` | method | `void` | private | — |
| `update_rendered_polyline_on_sphere( GeometryBuilder::GeometryIndex geom_index)` | method | `void` | private | — |
| `update_rendered_polygon_on_sphere( GeometryBuilder::GeometryIndex geom_index)` | method | `void` | private | — |
| `add_rendered_points( GeometryBuilder::GeometryIndex geom_index)` | method | `void` | private | — |
| `add_rendered_lines( GeometryBuilder::GeometryIndex geom_index, const GPlatesMaths::GeometryType::Value actual_geom_type)` | method | `void` | private | — |
| `update_highlight_rendered_layer( const GPlatesMaths::PointOnSphere &oriented_pos_on_sphere, const double &closeness_inclusion_threshold)` | method | `void` | private | — |
| `add_rendered_highlight_on_line_segment( const unsigned int line_segment_index, const GPlatesMaths::PointOnSphere &oriented_pos_on_sphere, const double &closeness_inclusion_threshold)` | method | `void` | private | — |
| `add_rendered_highlight_off_line_segment( const GPlatesMaths::PointOnSphere &oriented_pos_on_sphere)` | method | `void` | private | — |
| `add_rendered_highlight_line_segment( const unsigned int highlight_line_segment_index)` | method | `void` | private | — |
| `add_rendered_highlight_line_segment( const GPlatesMaths::PointOnSphere &start_point, const GPlatesMaths::PointOnSphere &end_point)` | method | `void` | private | — |
| `add_rendered_highlight_line_segment( ForwardIterPointOnSphere begin_point_on_sphere, ForwardIterPointOnSphere end_point_on_sphere)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_INSERTVERTEXGEOMETRYOPERATION_H` | macro | `None` | — |

## Notes

`d_line_to_point_mapping` maps rendered *line-segment* indices back to point indices, not the other way around, because a line segment is not rendered between two points that are too close together — the two index spaces diverge whenever that happens, so code indexing this vector must not assume segment index equals point index.

## Used by

| Unit | Component | References |
|---|---|---|
| [canvas-tools/InsertVertex](../canvas-tools/InsertVertex.md) | canvas-tools | 14 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&d_geometry_builder` | `stopped_updating_geometry()` | `this` | `geometry_builder_stopped_updating_geometry()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/InsertVertexGeometryOperation.h
python scripts/gpq.py def GPlatesViewOperations::InsertVertexGeometryOperation --body
python scripts/gpq.py uses InsertVertexGeometryOperation --kind class
python scripts/gpq.py hier InsertVertexGeometryOperation
```
