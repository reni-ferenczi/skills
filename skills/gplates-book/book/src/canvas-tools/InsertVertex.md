# InsertVertex

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 438 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/InsertVertex.h` | C++ | 148 |
| `src/canvas-tools/InsertVertex.cc` | C++ | 110 |

## Overview

[[[PROSE overview unit=canvas-tools/InsertVertex tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCanvasTools::InsertVertex`](#gplatescanvastoolsinsertvertex) | class | [`CanvasTool`](CanvasTool.md) | — | 0 | This is the canvas tool used to insert vertices into geometry. |

## Members

### `GPlatesCanvasTools::InsertVertex`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( const status_bar_callback_type &status_bar_callback, GPlatesViewOperations::GeometryBuilder &geometry_builder, GPlatesCanvasTools::GeometryOperationState &geometry_operation_state, GPlatesViewOperations::RenderedGeometryCollection &rendered_geometry_collection, GPlatesViewOperations::RenderedGeometryCollection: ...` | method | `non_null_ptr_type` | public | — |
| `~InsertVertex()` | destructor | `None` | public | — |
| `handle_activation()` | method | `void` | public | — |
| `handle_deactivation()` | method | `void` | public | — |
| `handle_left_click( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `handle_left_drag( const GPlatesMaths::PointOnSphere &initial_point_on_sphere, bool was_on_earth, double initial_proximity_inclusion_threshold, const GPlatesMaths::PointOnSphere &current_point_on_sphere, bool is_on_earth, double current_proximity_inclusion_threshold, const boost::optional<GPlatesMaths::PointOnSphere> &c ...` | method | `void` | public | — |
| `handle_move_without_drag( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `InsertVertex( const status_bar_callback_type &status_bar_callback, GPlatesViewOperations::GeometryBuilder &geometry_builder, GPlatesCanvasTools::GeometryOperationState &geometry_operation_state, GPlatesViewOperations::RenderedGeometryCollection &rendered_geometry_collection, GPlatesViewOperations::RenderedGeometryColle ...` | constructor | `None` | private | Create a InsertVertex instance. |
| `d_insert_vertex_geometry_operation` | field | `boost::scoped_ptr<GPlatesViewOperations::InsertVertexGeometryOperation>` | private | Digitise operation for inserting a vertex into digitised or focused feature geometry. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_CANVASTOOLS_INSERTVERTEX_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=canvas-tools/InsertVertex tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/DigitisationCanvasToolWorkflow](../gui/DigitisationCanvasToolWorkflow.md) | gui | 2 |
| [gui/FeatureInspectionCanvasToolWorkflow](../gui/FeatureInspectionCanvasToolWorkflow.md) | gui | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/canvas-tools/InsertVertex.h
python scripts/gpq.py def GPlatesCanvasTools::InsertVertex --body
python scripts/gpq.py uses InsertVertex --kind class
python scripts/gpq.py hier InsertVertex
```
