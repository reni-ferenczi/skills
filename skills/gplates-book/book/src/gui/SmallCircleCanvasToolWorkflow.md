# SmallCircleCanvasToolWorkflow

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1096 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/SmallCircleCanvasToolWorkflow.h` | C++ | 120 |
| `src/gui/SmallCircleCanvasToolWorkflow.cc` | C++ | 168 |

## Overview

[[[PROSE overview unit=gui/SmallCircleCanvasToolWorkflow tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::SmallCircleCanvasToolWorkflow`](#gplatesguismallcirclecanvastoolworkflow) | class | [`CanvasToolWorkflow`](CanvasToolWorkflow.md) | — | 0 | The canvas tool workflow for creating small circles. |

## Members

### `GPlatesGui::SmallCircleCanvasToolWorkflow`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SmallCircleCanvasToolWorkflow( CanvasToolWorkflows &canvas_tool_workflows, GPlatesCanvasTools::GeometryOperationState &geometry_operation_state, GPlatesCanvasTools::MeasureDistanceState &measure_distance_state, const GPlatesCanvasTools::CanvasTool::status_bar_callback_type &status_bar_callback, GPlatesPresentation::Vie ...` | constructor | `None` | public | — |
| `initialise()` | method | `void` | public | — |
| `activate_workflow()` | method | `void` | protected | — |
| `deactivate_workflow()` | method | `void` | protected | — |
| `get_selected_globe_and_map_canvas_tools( CanvasToolWorkflows::ToolType selected_tool)` | method | `boost::optional< std::pair<GPlatesGui::GlobeCanvasTool *, GPlatesGui::MapCanvasTool *> >` | protected | — |
| `d_rendered_geom_collection` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | For rendering purposes |
| `d_globe_create_small_circle_tool` | field | `boost::scoped_ptr<GlobeCanvasTool>` | private | For creating small circles in the 3D globe view. |
| `d_map_create_small_circle_tool` | field | `boost::scoped_ptr<MapCanvasTool>` | private | For creating small circles in the 2D map view. |
| `create_canvas_tools( CanvasToolWorkflows &canvas_tool_workflows, GPlatesCanvasTools::GeometryOperationState &geometry_operation_state, GPlatesCanvasTools::MeasureDistanceState &measure_distance_state, const GPlatesCanvasTools::CanvasTool::status_bar_callback_type &status_bar_callback, GPlatesPresentation::ViewState &vi ...` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `WORKFLOW_RENDER_LAYER` | variable | `GPlatesViewOperations::RenderedGeometryCollection::MainLayerType` | The main rendered layer used by this canvas tool workflow. |
| `GPLATES_GUI_SMALLCIRCLECANVASTOOLWORKFLOW_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/SmallCircleCanvasToolWorkflow tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/CanvasToolWorkflows](CanvasToolWorkflows.md) | gui | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/SmallCircleCanvasToolWorkflow.h
python scripts/gpq.py def GPlatesGui::SmallCircleCanvasToolWorkflow --body
python scripts/gpq.py uses SmallCircleCanvasToolWorkflow --kind class
python scripts/gpq.py hier SmallCircleCanvasToolWorkflow
```
