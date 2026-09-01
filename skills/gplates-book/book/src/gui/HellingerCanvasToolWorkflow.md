# HellingerCanvasToolWorkflow

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 991 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/HellingerCanvasToolWorkflow.h` | C++ | 116 |
| `src/gui/HellingerCanvasToolWorkflow.cc` | C++ | 184 |

## Overview

A canvas tool workflow for performing pole fits using the Hellinger method, a technique for determining optimal rotations. It manages two interactive tools: `SelectHellingerGeometries` for selecting and manipulating pole fit data points, and `AdjustFittedPoleEstimate` for refining the computed pole estimate. Each tool is available in both 3D globe and 2D map views via adapters.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::HellingerCanvasToolWorkflow`](#gplatesguihellingercanvastoolworkflow) | class | [`CanvasToolWorkflow`](CanvasToolWorkflow.md) | — | 0 | The canvas tool workflow for performing pole fits by the method of Hellinger |

## Members

### `GPlatesGui::HellingerCanvasToolWorkflow`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `HellingerCanvasToolWorkflow( CanvasToolWorkflows &canvas_tool_workflows, const GPlatesCanvasTools::CanvasTool::status_bar_callback_type &status_bar_callback, GPlatesPresentation::ViewState &view_state, GPlatesQtWidgets::ViewportWindow &viewport_window)` | constructor | `None` | public | — |
| `initialise()` | method | `void` | public | — |
| `activate_workflow()` | method | `void` | protected | — |
| `deactivate_workflow()` | method | `void` | protected | — |
| `get_selected_globe_and_map_canvas_tools( CanvasToolWorkflows::ToolType selected_tool)` | method | `boost::optional< std::pair<GPlatesGui::GlobeCanvasTool *, GPlatesGui::MapCanvasTool *> >` | protected | — |
| `d_rendered_geom_collection` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | For rendering purposes |
| `d_globe_select_hellinger_geometries_tool` | field | `boost::scoped_ptr<GlobeCanvasTool>` | private | For manipulating hellinger geometries in the 3D globe view. |
| `d_map_select_hellinger_geometries_tool` | field | `boost::scoped_ptr<MapCanvasTool>` | private | For manipulating hellinger geometries in the 2D map view. |
| `d_globe_adjust_pole_estimate_tool` | field | `boost::scoped_ptr<GlobeCanvasTool>` | private | For adjusting the pole estimate in the 3D globe view. |
| `d_map_adjust_pole_estimate_tool` | field | `boost::scoped_ptr<MapCanvasTool>` | private | For adjusting the pole estimate in the 2D map view. |
| `d_hellinger_dialog_ptr` | field | `GPlatesQtWidgets::HellingerDialog` | private | — |
| `create_canvas_tools( CanvasToolWorkflows &canvas_tool_workflows, const GPlatesCanvasTools::CanvasTool::status_bar_callback_type &status_bar_callback, GPlatesPresentation::ViewState &view_state, GPlatesQtWidgets::ViewportWindow &viewport_window)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `WORKFLOW_RENDER_LAYER` | variable | `GPlatesViewOperations::RenderedGeometryCollection::MainLayerType` | The main rendered layer used by this canvas tool workflow. |
| `GPLATES_GUI_HELLINGERCANVASTOOLWORKFLOW_H` | macro | `None` | — |

## Notes

The `d_hellinger_dialog_ptr` is not owned — it is obtained from `ViewportWindow::dialogs()` and must remain valid for the lifetime of the workflow. The same underlying canvas tools are wrapped in separate adapters for globe and map views.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/CanvasToolWorkflows](CanvasToolWorkflows.md) | gui | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/HellingerCanvasToolWorkflow.h
python scripts/gpq.py def GPlatesGui::HellingerCanvasToolWorkflow --body
python scripts/gpq.py uses HellingerCanvasToolWorkflow --kind class
python scripts/gpq.py hier HellingerCanvasToolWorkflow
```
