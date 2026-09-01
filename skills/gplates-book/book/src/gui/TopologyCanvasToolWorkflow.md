# TopologyCanvasToolWorkflow

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 462 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/TopologyCanvasToolWorkflow.h` | C++ | 180 |
| `src/gui/TopologyCanvasToolWorkflow.cc` | C++ | 458 |

## Overview

Implements a workflow for building and editing topological features. The workflow manages five interactive tools: `ClickGeometry` for selecting features, and `BuildTopology` with three variants (for line, boundary, and network topologies), plus `EditTopology` for modifying existing topologies. Each tool has parallel globe and map implementations. The build tools are always enabled, while the edit tool is conditionally enabled based on the current active tool and whether a topological feature is focused. The workflow renders the focused feature and responds to feature focus changes to manage tool state.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::TopologyCanvasToolWorkflow`](#gplatesguitopologycanvastoolworkflow) | class | [`CanvasToolWorkflow`](CanvasToolWorkflow.md) | — | 0 | The canvas tool workflow for building/editing topological features. |

## Members

### `GPlatesGui::TopologyCanvasToolWorkflow`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TopologyCanvasToolWorkflow( CanvasToolWorkflows &canvas_tool_workflows, const GPlatesCanvasTools::CanvasTool::status_bar_callback_type &status_bar_callback, GPlatesPresentation::ViewState &view_state, GPlatesQtWidgets::ViewportWindow &viewport_window)` | constructor | `None` | public | — |
| `initialise()` | method | `void` | public | — |
| `activate_workflow()` | method | `void` | protected | — |
| `deactivate_workflow()` | method | `void` | protected | — |
| `get_selected_globe_and_map_canvas_tools( CanvasToolWorkflows::ToolType selected_tool)` | method | `boost::optional< std::pair<GlobeCanvasTool *, MapCanvasTool *> >` | protected | — |
| `handle_canvas_tool_activated( GPlatesGui::CanvasToolWorkflows::WorkflowType workflow, GPlatesGui::CanvasToolWorkflows::ToolType tool)` | method | `void` | private | Changed the selected canvas tool. |
| `draw_feature_focus()` | method | `void` | private | — |
| `update_enable_state()` | method | `void` | private | — |
| `d_canvas_tool_workflows` | field | `CanvasToolWorkflows` | private | For determining the curently active workflow/tool. |
| `d_feature_focus` | field | `FeatureFocus` | private | The focused feature, in part, determines which tools are enabled. |
| `d_rendered_geom_collection` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | For rendering purposes |
| `d_rendered_geometry_parameters` | field | `GPlatesViewOperations::RenderedGeometryParameters` | private | Parameters for rendering geometries in canvas tools. |
| `d_render_settings` | field | `RenderSettings` | private | Show/hide geometry settings. |
| `d_symbol_map` | field | `symbol_map_type` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | Used to get current topological sections. |
| `d_globe_click_geometry_tool` | field | `boost::scoped_ptr<GlobeCanvasTool>` | private | For clicking geometries in the 3D globe view. |
| `d_map_click_geometry_tool` | field | `boost::scoped_ptr<MapCanvasTool>` | private | For clicking geometries in the 2D map view. |
| `d_globe_build_line_topology_tool` | field | `boost::scoped_ptr<GlobeCanvasTool>` | private | For building line topologies in the 3D globe view. |
| `d_map_build_line_topology_tool` | field | `boost::scoped_ptr<MapCanvasTool>` | private | For building line topologies in the 2D map view. |
| `d_globe_build_boundary_topology_tool` | field | `boost::scoped_ptr<GlobeCanvasTool>` | private | For building boundary topologies in the 3D globe view. |
| `d_map_build_boundary_topology_tool` | field | `boost::scoped_ptr<MapCanvasTool>` | private | For building boundary topologies in the 2D map view. |
| `d_globe_build_network_topology_tool` | field | `boost::scoped_ptr<GlobeCanvasTool>` | private | For building network topologies in the 3D globe view. |
| `d_map_build_network_topology_tool` | field | `boost::scoped_ptr<MapCanvasTool>` | private | For building network topologies in the 2D map view. |
| `d_globe_edit_topology_tool` | field | `boost::scoped_ptr<GlobeCanvasTool>` | private | For editing topologies in the 3D globe view. |
| `d_map_edit_topology_tool` | field | `boost::scoped_ptr<MapCanvasTool>` | private | For editing topologies in the 2D map view. |
| `create_canvas_tools( CanvasToolWorkflows &canvas_tool_workflows, const GPlatesCanvasTools::CanvasTool::status_bar_callback_type &status_bar_callback, GPlatesPresentation::ViewState &view_state, GPlatesQtWidgets::ViewportWindow &viewport_window)` | method | `void` | private | — |
| `update_build_topology_tools()` | method | `void` | private | — |
| `update_edit_topology_tool()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `WORKFLOW_RENDER_LAYER` | variable | `GPlatesViewOperations::RenderedGeometryCollection::MainLayerType` | The main rendered layer used by this canvas tool workflow. |
| `is_active_and_enabled_tool( const CanvasToolWorkflows &canvas_tool_workflows, CanvasToolWorkflows::WorkflowType workflow, CanvasToolWorkflows::ToolType tool)` | function | `bool` | Returns true if the specified workflow/tool is the currently active tool (and also is enabled). |
| `GPLATES_GUI_TOPOLOGYCANVASTOOLWORKFLOW_H` | macro | `None` | — |

## Notes

The render layer is activated only while the workflow is active. The build topology tools are always enabled, but the edit topology tool is conditionally enabled: it's enabled when it's the current active tool, or when no build tools are active and a topological feature is focused. The edit tool uses feature focus extensively (to add topology sections), so the focus state changes dynamically while it is active. The workflow listens to canvas tool activation changes to update tool enable states via `handle_canvas_tool_activated()`.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/CanvasToolWorkflows](CanvasToolWorkflows.md) | gui | 2 |

## Related

**Qt signal/slot connections** (5 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&d_feature_focus` | `focus_changed( GPlatesGui::FeatureFocus &)` | `this` | `update_enable_state()` |
| `&canvas_tool_workflows` | `canvas_tool_activated( GPlatesGui::CanvasToolWorkflows::WorkflowType, GPlatesGui::CanvasToolWorkflows::ToolType)` | `this` | `handle_canvas_tool_activated( GPlatesGui::CanvasToolWorkflows::WorkflowType, GPlatesGui::CanvasToolWorkflows::ToolType)` |
| `&d_feature_focus` | `focus_changed(GPlatesGui::FeatureFocus &)` | `this` | `draw_feature_focus()` |
| `&d_feature_focus` | `focused_feature_modified(GPlatesGui::FeatureFocus &)` | `this` | `draw_feature_focus()` |
| `&d_rendered_geometry_parameters` | `parameters_changed(GPlatesViewOperations::RenderedGeometryParameters &)` | `this` | `draw_feature_focus()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/TopologyCanvasToolWorkflow.h
python scripts/gpq.py def GPlatesGui::TopologyCanvasToolWorkflow --body
python scripts/gpq.py uses TopologyCanvasToolWorkflow --kind class
python scripts/gpq.py hier TopologyCanvasToolWorkflow
```
