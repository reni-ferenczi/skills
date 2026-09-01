# DeleteVertexGeometryOperation

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 488 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/DeleteVertexGeometryOperation.h` | C++ | 229 |
| `src/view-operations/DeleteVertexGeometryOperation.cc` | C++ | 463 |

## Overview

[[[PROSE overview unit=view-operations/DeleteVertexGeometryOperation tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::DeleteVertexGeometryOperation`](#gplatesviewoperationsdeletevertexgeometryoperation) | class | [`GeometryOperation`](GeometryOperation.md)<br>`boost::noncopyable` | — | 0 | Deletes a vertex in GeometryBuilder and manages RenderedGeometry objects in a RenderedGeometryCollection layer. |

## Members

### `GPlatesViewOperations::DeleteVertexGeometryOperation`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DeleteVertexGeometryOperation( GeometryBuilder &geometry_builder, GPlatesCanvasTools::GeometryOperationState &geometry_operation_state, RenderedGeometryCollection &rendered_geometry_collection, RenderedGeometryCollection::MainLayerType main_rendered_layer_type, GPlatesGui::CanvasToolWorkflows &canvas_tool_workflows, co ...` | constructor | `None` | public | — |
| `activate()` | method | `void` | public | Activate this operation. |
| `deactivate()` | method | `void` | public | Deactivate this operation. |
| `left_click( const GPlatesMaths::PointOnSphere &oriented_pos_on_sphere, const double &closeness_inclusion_threshold)` | method | `void` | public | User has just clicked on the sphere. |
| `mouse_move( const GPlatesMaths::PointOnSphere &oriented_pos_on_sphere, const double &closeness_inclusion_threshold)` | method | `void` | public | The mouse has moved but it is not a drag because mouse button is not pressed. |
| `geometry_builder_stopped_updating_geometry()` | method | `void` | public | NOTE: all signals/slots should use namespace scope for all arguments otherwise differences between signals and slots will cause Qt to not be able to connect them at runtime. |
| `d_geometry_builder` | field | `GeometryBuilder` | private | This is used to build geometry. |
| `d_geometry_operation_state` | field | `GPlatesCanvasTools::GeometryOperationState` | private | We call this when we activate/deactivate. |
| `d_rendered_geometry_collection` | field | `RenderedGeometryCollection` | private | This is where we render our geometries and activate our render layer. |
| `d_main_rendered_layer_type` | field | `RenderedGeometryCollection::MainLayerType` | private | The main rendered layer we're currently rendering into. |
| `d_lines_layer_ptr` | field | `RenderedGeometryCollection::child_layer_owner_ptr_type` | private | Rendered geometry layer used for lines. |
| `d_points_layer_ptr` | field | `RenderedGeometryCollection::child_layer_owner_ptr_type` | private | Rendered geometry layer used for points. |
| `d_highlight_point_layer_ptr` | field | `RenderedGeometryCollection::child_layer_owner_ptr_type` | private | Rendered geometry layer used for the single highlighted point (the point that the mouse cursor is currently hovering over if any). |
| `d_canvas_tool_workflows` | field | `GPlatesGui::CanvasToolWorkflows` | private | Used by undo/redo to make sure appropriate tool is active when the undo/redo happens. |
| `d_query_proximity_threshold` | field | `QueryProximityThreshold` | private | Used to query the proximity threshold based on position on globe. |
| `delete_vertex( const GeometryBuilder::PointIndex delete_vertex_index)` | method | `void` | private | Perform the actual delete vertex command. |
| `allow_delete_vertex()` | method | `bool` | private | Returns true if user is allowed to delete a vertex. |
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
| `add_highlight_rendered_point( const GeometryBuilder::PointIndex highlight_point_index)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_DELETEVERTEXGEOMETRYOPERATION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=view-operations/DeleteVertexGeometryOperation tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [canvas-tools/DeleteVertex](../canvas-tools/DeleteVertex.md) | canvas-tools | 8 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&d_geometry_builder` | `stopped_updating_geometry()` | `this` | `geometry_builder_stopped_updating_geometry()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/DeleteVertexGeometryOperation.h
python scripts/gpq.py def GPlatesViewOperations::DeleteVertexGeometryOperation --body
python scripts/gpq.py uses DeleteVertexGeometryOperation --kind class
python scripts/gpq.py hier DeleteVertexGeometryOperation
```
