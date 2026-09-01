# MoveVertex

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 777 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/MoveVertex.h` | C++ | 181 |
| `src/canvas-tools/MoveVertex.cc` | C++ | 184 |

## Overview

A canvas tool for interactive vertex editing on the globe. Extends `CanvasTool` and handles mouse clicks and drags on geometry vertices, delegating the actual vertex movement to `MoveVertexGeometryOperation`. It integrates with digitisation and feature inspection workflows, using proximity thresholds to snap to nearby vertices and providing status bar feedback during editing. Manages drag state to distinguish between single clicks and multi-point dragging operations.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCanvasTools::MoveVertex`](#gplatescanvastoolsmovevertex) | class | [`CanvasTool`](CanvasTool.md) | — | 0 | This is the canvas tool used to move individual vertices of geometry. |

## Members

### `GPlatesCanvasTools::MoveVertex`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( const status_bar_callback_type &status_bar_callback, GPlatesViewOperations::GeometryBuilder &geometry_builder, GPlatesCanvasTools::GeometryOperationState &geometry_operation_state, GPlatesCanvasTools::ModifyGeometryState &modify_geometry_state, GPlatesViewOperations::RenderedGeometryCollection &rendered_geometr ...` | method | `non_null_ptr_type` | public | — |
| `~MoveVertex()` | destructor | `None` | public | — |
| `handle_activation()` | method | `void` | public | — |
| `handle_deactivation()` | method | `void` | public | — |
| `handle_left_click( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `handle_left_press( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `handle_left_drag( const GPlatesMaths::PointOnSphere &initial_point_on_sphere, bool was_on_earth, double initial_proximity_inclusion_threshold, const GPlatesMaths::PointOnSphere &current_point_on_sphere, bool is_on_earth, double current_proximity_inclusion_threshold, const boost::optional<GPlatesMaths::PointOnSphere> &c ...` | method | `void` | public | — |
| `handle_left_release_after_drag( const GPlatesMaths::PointOnSphere &initial_point_on_sphere, bool was_on_earth, double initial_proximity_inclusion_threshold, const GPlatesMaths::PointOnSphere &current_point_on_sphere, bool is_on_earth, double current_proximity_inclusion_threshold, const boost::optional<GPlatesMaths::Poi ...` | method | `void` | public | — |
| `handle_move_without_drag( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `MoveVertex( const status_bar_callback_type &status_bar_callback, GPlatesViewOperations::GeometryBuilder &geometry_builder, GPlatesCanvasTools::GeometryOperationState &geometry_operation_state, GPlatesCanvasTools::ModifyGeometryState &modify_geometry_state, GPlatesViewOperations::RenderedGeometryCollection &rendered_geo ...` | constructor | `None` | private | Create a MoveVertex instance. |
| `d_move_vertex_geometry_operation` | field | `boost::scoped_ptr<GPlatesViewOperations::MoveVertexGeometryOperation>` | private | Digitise operation for moving a vertex in digitised geometry. |
| `d_is_in_drag` | field | `bool` | private | Whether or not this tool is currently in the midst of a drag. |
| `handle_left_drag( bool &is_in_drag, GPlatesViewOperations::MoveVertexGeometryOperation *move_vertex_geometry_operation, const GPlatesMaths::PointOnSphere &oriented_initial_pos_on_globe, const double &closeness_inclusion_threshold, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_CANVASTOOLS_MOVEVERTEX_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/DigitisationCanvasToolWorkflow](../gui/DigitisationCanvasToolWorkflow.md) | gui | 4 |
| [gui/FeatureInspectionCanvasToolWorkflow](../gui/FeatureInspectionCanvasToolWorkflow.md) | gui | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/canvas-tools/MoveVertex.h
python scripts/gpq.py def GPlatesCanvasTools::MoveVertex --body
python scripts/gpq.py uses MoveVertex --kind class
python scripts/gpq.py hier MoveVertex
```
