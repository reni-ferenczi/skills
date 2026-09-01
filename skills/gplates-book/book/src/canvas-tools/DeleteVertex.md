# DeleteVertex

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 499 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/DeleteVertex.h` | C++ | 139 |
| `src/canvas-tools/DeleteVertex.cc` | C++ | 97 |

## Overview

[[[PROSE overview unit=canvas-tools/DeleteVertex tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCanvasTools::DeleteVertex`](#gplatescanvastoolsdeletevertex) | class | [`CanvasTool`](CanvasTool.md) | — | 0 | This is the canvas tool used to delete vertices from geometry. |

## Members

### `GPlatesCanvasTools::DeleteVertex`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~DeleteVertex()` | destructor | `None` | public | — |
| `create( const status_bar_callback_type &status_bar_callback, GPlatesViewOperations::GeometryBuilder &geometry_builder, GPlatesCanvasTools::GeometryOperationState &geometry_operation_state, GPlatesViewOperations::RenderedGeometryCollection &rendered_geometry_collection, GPlatesViewOperations::RenderedGeometryCollection: ...` | method | `non_null_ptr_type` | public | — |
| `handle_activation()` | method | `void` | public | — |
| `handle_deactivation()` | method | `void` | public | — |
| `handle_left_click( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `handle_move_without_drag( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `DeleteVertex( const status_bar_callback_type &status_bar_callback, GPlatesViewOperations::GeometryBuilder &geometry_builder, GPlatesCanvasTools::GeometryOperationState &geometry_operation_state, GPlatesViewOperations::RenderedGeometryCollection &rendered_geometry_collection, GPlatesViewOperations::RenderedGeometryColle ...` | constructor | `None` | private | Create a DeleteVertex instance. |
| `d_delete_vertex_geometry_operation` | field | `boost::scoped_ptr<GPlatesViewOperations::DeleteVertexGeometryOperation>` | private | Digitise operation for deleting a vertex from digitised or focused feature geometry. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_CANVASTOOLS_DELETEVERTEX_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=canvas-tools/DeleteVertex tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/FeatureInspectionCanvasToolWorkflow](../gui/FeatureInspectionCanvasToolWorkflow.md) | gui | 32 |
| [gui/DigitisationCanvasToolWorkflow](../gui/DigitisationCanvasToolWorkflow.md) | gui | 27 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/canvas-tools/DeleteVertex.h
python scripts/gpq.py def GPlatesCanvasTools::DeleteVertex --body
python scripts/gpq.py uses DeleteVertex --kind class
python scripts/gpq.py hier DeleteVertex
```
