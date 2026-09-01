# DeleteVertex

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 499 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/DeleteVertex.h` | C++ | 139 |
| `src/canvas-tools/DeleteVertex.cc` | C++ | 97 |

## Overview

`DeleteVertex` is a thin `CanvasTool` shell around `GPlatesViewOperations::DeleteVertexGeometryOperation`, which does the actual work of removing a vertex from the geometry currently being digitised or the focused feature's geometry. Every handler — activation, deactivation, left-click and hover — just forwards to the correspondingly named method on `d_delete_vertex_geometry_operation`, so this class exists mainly to plug that operation into the canvas-tool framework (`CanvasTool::create()`, the status-bar message, and the `handle_*` dispatch that `GPlatesGui::CanvasToolWorkflows` drives).

The operation object owns the interaction with `GPlatesViewOperations::GeometryBuilder` and `GeometryOperationState`, and is constructed once in `DeleteVertex`'s constructor with all the collaborators (rendered-geometry collection, canvas tool workflows, proximity threshold) it needs to highlight the vertex nearest the cursor and delete it on click.

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

`d_delete_vertex_geometry_operation` is a `boost::scoped_ptr` to a forward-declared type, so `DeleteVertex` needs a defined (non-inline) destructor even though it does nothing but note that the complete type must be visible at that point.

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
