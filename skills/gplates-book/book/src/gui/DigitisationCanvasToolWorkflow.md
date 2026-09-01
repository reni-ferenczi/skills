# DigitisationCanvasToolWorkflow

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 461 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/DigitisationCanvasToolWorkflow.h` | C++ | 173 |
| `src/gui/DigitisationCanvasToolWorkflow.cc` | C++ | 453 |

## Overview

[[[PROSE overview unit=gui/DigitisationCanvasToolWorkflow tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::DigitisationCanvasToolWorkflow`](#gplatesguidigitisationcanvastoolworkflow) | class | [`CanvasToolWorkflow`](CanvasToolWorkflow.md) | — | 0 | The canvas tool workflow for digitising new features as point/multipoint/polyline/polygon. |

## Members

### `GPlatesGui::DigitisationCanvasToolWorkflow`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DigitisationCanvasToolWorkflow( CanvasToolWorkflows &canvas_tool_workflows, GPlatesCanvasTools::GeometryOperationState &geometry_operation_state, GPlatesCanvasTools::ModifyGeometryState &modify_geometry_state, GPlatesCanvasTools::MeasureDistanceState &measure_distance_state, const GPlatesCanvasTools::CanvasTool::status ...` | constructor | `None` | public | — |
| `initialise()` | method | `void` | public | — |
| `activate_workflow()` | method | `void` | protected | — |
| `deactivate_workflow()` | method | `void` | protected | — |
| `get_selected_globe_and_map_canvas_tools( CanvasToolWorkflows::ToolType selected_tool)` | method | `boost::optional< std::pair<GPlatesGui::GlobeCanvasTool *, GPlatesGui::MapCanvasTool *> >` | protected | — |
| `geometry_builder_stopped_updating_geometry_excluding_intermediate_moves()` | method | `void` | private | Focused feature geometry changes. |
| `d_digitise_geometry_builder` | field | `GPlatesViewOperations::GeometryBuilder` | private | — |
| `d_geometry_operation_state` | field | `GPlatesCanvasTools::GeometryOperationState` | private | — |
| `d_rendered_geom_collection` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | For rendering purposes |
| `d_globe_measure_distance_tool` | field | `boost::scoped_ptr<GlobeCanvasTool>` | private | For measuring distance in the 3D globe view. |
| `d_map_measure_distance_tool` | field | `boost::scoped_ptr<MapCanvasTool>` | private | For measuring distance in the 2D map view. |
| `d_globe_digitise_multipoint_tool` | field | `boost::scoped_ptr<GlobeCanvasTool>` | private | For digitising multipoints in the 3D globe view. |
| `d_map_digitise_multipoint_tool` | field | `boost::scoped_ptr<MapCanvasTool>` | private | For digitising multipoints in the 2D map view. |
| `d_globe_digitise_polyline_tool` | field | `boost::scoped_ptr<GlobeCanvasTool>` | private | For digitising polylines in the 3D globe view. |
| `d_map_digitise_polyline_tool` | field | `boost::scoped_ptr<MapCanvasTool>` | private | For digitising polylines in the 2D map view. |
| `d_globe_digitise_polygon_tool` | field | `boost::scoped_ptr<GlobeCanvasTool>` | private | For digitising polygons in the 3D globe view. |
| `d_map_digitise_polygon_tool` | field | `boost::scoped_ptr<MapCanvasTool>` | private | For digitising polygons in the 2D map view. |
| `d_globe_move_vertex_tool` | field | `boost::scoped_ptr<GlobeCanvasTool>` | private | For moving geometry vertices in the 3D globe view. |
| `d_map_move_vertex_tool` | field | `boost::scoped_ptr<MapCanvasTool>` | private | For moving geometry vertices in the 2D map view. |
| `d_globe_delete_vertex_tool` | field | `boost::scoped_ptr<GlobeCanvasTool>` | private | For deleting geometry vertices in the 3D globe view. |
| `d_map_delete_vertex_tool` | field | `boost::scoped_ptr<MapCanvasTool>` | private | For deleting geometry vertices in the 2D map view. |
| `d_globe_insert_vertex_tool` | field | `boost::scoped_ptr<GlobeCanvasTool>` | private | For inserting geometry vertices in the 3D globe view. |
| `d_map_insert_vertex_tool` | field | `boost::scoped_ptr<MapCanvasTool>` | private | For inserting geometry vertices in the 2D map view. |
| `create_canvas_tools( CanvasToolWorkflows &canvas_tool_workflows, GPlatesCanvasTools::GeometryOperationState &geometry_operation_state, GPlatesCanvasTools::ModifyGeometryState &modify_geometry_state, GPlatesCanvasTools::MeasureDistanceState &measure_distance_state, const GPlatesCanvasTools::CanvasTool::status_bar_callba ...` | method | `void` | private | — |
| `update_enable_state()` | method | `void` | private | — |
| `get_geometry_builder_parameters()` | method | `std::pair<unsigned int, GPlatesMaths::GeometryType::Value>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `WORKFLOW_RENDER_LAYER` | variable | `GPlatesViewOperations::RenderedGeometryCollection::MainLayerType` | The main rendered layer used by this canvas tool workflow. |
| `GPLATES_CANVASTOOLS_DIGITISATIONCANVASTOOLWORKFLOW_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/DigitisationCanvasToolWorkflow tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/CanvasToolWorkflows](CanvasToolWorkflows.md) | gui | 2 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&d_digitise_geometry_builder` | `stopped_updating_geometry_excluding_intermediate_moves()` | `this` | `geometry_builder_stopped_updating_geometry_excluding_intermediate_moves()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/DigitisationCanvasToolWorkflow.h
python scripts/gpq.py def GPlatesGui::DigitisationCanvasToolWorkflow --body
python scripts/gpq.py uses DigitisationCanvasToolWorkflow --kind class
python scripts/gpq.py hier DigitisationCanvasToolWorkflow
```
