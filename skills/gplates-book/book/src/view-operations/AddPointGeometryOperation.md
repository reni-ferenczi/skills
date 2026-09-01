# AddPointGeometryOperation

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 625 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/AddPointGeometryOperation.h` | C++ | 195 |
| `src/view-operations/AddPointGeometryOperation.cc` | C++ | 376 |

## Overview

[[[PROSE overview unit=view-operations/AddPointGeometryOperation tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::AddPointGeometryOperation`](#gplatesviewoperationsaddpointgeometryoperation) | class | [`GeometryOperation`](GeometryOperation.md)<br>`boost::noncopyable` | — | 0 | Adds a point to GeometryBuilder and adds RenderedGeometry objects to RenderedGeometryCollection. |

## Members

### `GPlatesViewOperations::AddPointGeometryOperation`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AddPointGeometryOperation( GPlatesMaths::GeometryType::Value build_geom_type, GeometryBuilder &geometry_builder, GPlatesCanvasTools::GeometryOperationState &geometry_operation_state, RenderedGeometryCollection &rendered_geometry_collection, RenderedGeometryCollection::MainLayerType main_rendered_layer_type, GPlatesGui: ...` | constructor | `None` | public | — |
| `activate()` | method | `void` | public | Activate this operation. |
| `deactivate()` | method | `void` | public | Deactivate this operation. |
| `add_point( const GPlatesMaths::PointOnSphere &oriented_pos_on_sphere, const double &closeness_inclusion_threshold)` | method | `void` | public | Add a point to the curent geometry builder at the specified position on sphere. |
| `geometry_builder_stopped_updating_geometry()` | method | `void` | public | NOTE: all signals/slots should use namespace scope for all arguments otherwise differences between signals and slots will cause Qt to not be able to connect them at runtime. |
| `d_build_geom_type` | field | `GPlatesMaths::GeometryType::Value` | private | The type of geometry we are attempting to build. |
| `d_geometry_builder` | field | `GeometryBuilder` | private | This is used to build geometry. |
| `d_geometry_operation_state` | field | `GPlatesCanvasTools::GeometryOperationState` | private | We call this when we activate/deactivate. |
| `d_rendered_geometry_collection` | field | `RenderedGeometryCollection` | private | This is where we render our geometries and activate our render layer. |
| `d_main_rendered_layer_type` | field | `RenderedGeometryCollection::MainLayerType` | private | The main rendered layer we're currently rendering into. |
| `d_lines_layer_ptr` | field | `RenderedGeometryCollection::child_layer_owner_ptr_type` | private | Rendered geometry layer used for lines. |
| `d_points_layer_ptr` | field | `RenderedGeometryCollection::child_layer_owner_ptr_type` | private | Rendered geometry layer used for points. |
| `d_canvas_tool_workflows` | field | `GPlatesGui::CanvasToolWorkflows` | private | Used by undo/redo to make sure appropriate tool is active when the undo/redo happens. |
| `d_query_proximity_threshold` | field | `QueryProximityThreshold` | private | Used to query the proximity threshold based on position on globe. |
| `connect_to_geometry_builder_signals()` | method | `void` | private | — |
| `disconnect_from_geometry_builder_signals()` | method | `void` | private | — |
| `create_rendered_geometry_layers()` | method | `void` | private | — |
| `update_rendered_geometries()` | method | `void` | private | Update all RenderedGeometry objects. |
| `update_rendered_geometry( GeometryBuilder::GeometryIndex geom_index)` | method | `void` | private | — |
| `update_rendered_point_on_sphere( GeometryBuilder::GeometryIndex geom_index)` | method | `void` | private | — |
| `update_rendered_multipoint_on_sphere( GeometryBuilder::GeometryIndex geom_index)` | method | `void` | private | — |
| `update_rendered_polyline_on_sphere( GeometryBuilder::GeometryIndex geom_index)` | method | `void` | private | — |
| `update_rendered_polygon_on_sphere( GeometryBuilder::GeometryIndex geom_index)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_ADDPOINTGEOMETRYOPERATION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=view-operations/AddPointGeometryOperation tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [canvas-tools/DigitiseGeometry](../canvas-tools/DigitiseGeometry.md) | canvas-tools | 5 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&d_geometry_builder` | `stopped_updating_geometry()` | `this` | `geometry_builder_stopped_updating_geometry()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/AddPointGeometryOperation.h
python scripts/gpq.py def GPlatesViewOperations::AddPointGeometryOperation --body
python scripts/gpq.py uses AddPointGeometryOperation --kind class
python scripts/gpq.py hier AddPointGeometryOperation
```
