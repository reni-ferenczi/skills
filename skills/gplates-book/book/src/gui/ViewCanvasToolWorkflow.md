# ViewCanvasToolWorkflow

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 944 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ViewCanvasToolWorkflow.h` | C++ | 121 |
| `src/gui/ViewCanvasToolWorkflow.cc` | C++ | 222 |

## Overview

[[[PROSE overview unit=gui/ViewCanvasToolWorkflow tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ViewCanvasToolWorkflow`](#gplatesguiviewcanvastoolworkflow) | class | [`CanvasToolWorkflow`](CanvasToolWorkflow.md) | — | 0 | The canvas tool workflow for view-related tools. |

## Members

### `GPlatesGui::ViewCanvasToolWorkflow`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ViewCanvasToolWorkflow( CanvasToolWorkflows &canvas_tool_workflows, const GPlatesCanvasTools::CanvasTool::status_bar_callback_type &status_bar_callback, GPlatesPresentation::ViewState &view_state, GPlatesQtWidgets::ViewportWindow &viewport_window)` | constructor | `None` | public | — |
| `initialise()` | method | `void` | public | — |
| `activate_workflow()` | method | `void` | protected | — |
| `deactivate_workflow()` | method | `void` | protected | — |
| `get_selected_globe_and_map_canvas_tools( CanvasToolWorkflows::ToolType selected_tool)` | method | `boost::optional< std::pair<GPlatesGui::GlobeCanvasTool *, GPlatesGui::MapCanvasTool *> >` | protected | — |
| `d_rendered_geom_collection` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | For rendering purposes |
| `d_globe_drag_globe_tool` | field | `boost::scoped_ptr<GlobeCanvasTool>` | private | For dragging the globe in the 3D globe view. |
| `d_map_drag_globe_tool` | field | `boost::scoped_ptr<MapCanvasTool>` | private | For dragging the globe in the 2D map view. |
| `d_globe_zoom_globe_tool` | field | `boost::scoped_ptr<GlobeCanvasTool>` | private | For zooming the globe in the 3D globe view. |
| `d_map_zoom_globe_tool` | field | `boost::scoped_ptr<MapCanvasTool>` | private | For zooming the globe in the 2D map view. |
| `d_globe_change_lighting_tool` | field | `boost::scoped_ptr<GlobeCanvasTool>` | private | For changing the lighting in the 3D globe view. |
| `d_map_change_lighting_tool` | field | `boost::scoped_ptr<MapCanvasTool>` | private | For changing the lighting in the 2D map view. |
| `create_canvas_tools( CanvasToolWorkflows &canvas_tool_workflows, const GPlatesCanvasTools::CanvasTool::status_bar_callback_type &status_bar_callback, GPlatesPresentation::ViewState &view_state, GPlatesQtWidgets::ViewportWindow &viewport_window)` | method | `void` | private | — |
| `update_enable_state()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `WORKFLOW_RENDER_LAYER` | variable | `GPlatesViewOperations::RenderedGeometryCollection::MainLayerType` | The main rendered layer used by this canvas tool workflow. |
| `GPLATES_GUI_VIEWCANVASTOOLWORKFLOW_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/ViewCanvasToolWorkflow tier=3]]]
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
python scripts/gpq.py file src/gui/ViewCanvasToolWorkflow.h
python scripts/gpq.py def GPlatesGui::ViewCanvasToolWorkflow --body
python scripts/gpq.py uses ViewCanvasToolWorkflow --kind class
python scripts/gpq.py hier ViewCanvasToolWorkflow
```
