# ViewCanvasToolWorkflow

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 944 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ViewCanvasToolWorkflow.h` | C++ | 121 |
| `src/gui/ViewCanvasToolWorkflow.cc` | C++ | 222 |

## Overview

A concrete `CanvasToolWorkflow` that manages view-manipulation tools — dragging the globe, zooming, and changing lighting. It maintains paired tools (one `GlobeCanvasTool` for 3D globe view, one `MapCanvasTool` for 2D map view) for each of the three operations, created via `create_canvas_tools()` and selected via `get_selected_globe_and_map_canvas_tools()`.

When activated, this workflow makes its selected tool pair active on the canvas; when deactivated, it disables them. The workflow updates tool availability via `update_enable_state()` based on the current application state.

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

*None.*

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
