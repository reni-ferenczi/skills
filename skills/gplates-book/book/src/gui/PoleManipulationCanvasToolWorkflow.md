# PoleManipulationCanvasToolWorkflow

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 289 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/PoleManipulationCanvasToolWorkflow.h` | C++ | 156 |
| `src/gui/PoleManipulationCanvasToolWorkflow.cc` | C++ | 327 |

## Overview

[[[PROSE overview unit=gui/PoleManipulationCanvasToolWorkflow tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::PoleManipulationCanvasToolWorkflow`](#gplatesguipolemanipulationcanvastoolworkflow) | class | [`CanvasToolWorkflow`](CanvasToolWorkflow.md) | — | 0 | The canvas tool workflow for manipulating rotation poles. |

## Members

### `GPlatesGui::PoleManipulationCanvasToolWorkflow`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PoleManipulationCanvasToolWorkflow( CanvasToolWorkflows &canvas_tool_workflows, const GPlatesCanvasTools::CanvasTool::status_bar_callback_type &status_bar_callback, GPlatesPresentation::ViewState &view_state, GPlatesQtWidgets::ViewportWindow &viewport_window)` | constructor | `None` | public | — |
| `initialise()` | method | `void` | public | — |
| `activate_workflow()` | method | `void` | protected | — |
| `deactivate_workflow()` | method | `void` | protected | — |
| `get_selected_globe_and_map_canvas_tools( CanvasToolWorkflows::ToolType selected_tool)` | method | `boost::optional< std::pair<GPlatesGui::GlobeCanvasTool *, GPlatesGui::MapCanvasTool *> >` | protected | — |
| `draw_feature_focus()` | method | `void` | private | — |
| `update_enable_state()` | method | `void` | private | — |
| `d_feature_focus` | field | `FeatureFocus` | private | The focused feature, in part, determines which tools are enabled. |
| `d_rendered_geom_collection` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | For rendering purposes |
| `d_rendered_geometry_parameters` | field | `GPlatesViewOperations::RenderedGeometryParameters` | private | Parameters for rendering geometries in canvas tools. |
| `d_render_settings` | field | `RenderSettings` | private | Show/hide geometry settings. |
| `d_symbol_map` | field | `GPlatesGui::symbol_map_type` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | Used to get current topological sections. |
| `d_globe_click_geometry_tool` | field | `boost::scoped_ptr<GlobeCanvasTool>` | private | For clicking geometries in the 3D globe view. |
| `d_map_click_geometry_tool` | field | `boost::scoped_ptr<MapCanvasTool>` | private | For clicking geometries in the 2D map view. |
| `d_globe_manipulate_pole_tool` | field | `boost::scoped_ptr<GlobeCanvasTool>` | private | For manipulating poles in the 3D globe view. |
| `d_map_manipulate_pole_tool` | field | `boost::scoped_ptr<MapCanvasTool>` | private | For manipulating poles in the 2D map view. |
| `d_globe_move_pole_tool` | field | `boost::scoped_ptr<GlobeCanvasTool>` | private | For moving poles in the 3D globe view. |
| `d_map_move_pole_tool` | field | `boost::scoped_ptr<MapCanvasTool>` | private | For moving poles in the 2D map view. |
| `create_canvas_tools( CanvasToolWorkflows &canvas_tool_workflows, const GPlatesCanvasTools::CanvasTool::status_bar_callback_type &status_bar_callback, GPlatesPresentation::ViewState &view_state, GPlatesQtWidgets::ViewportWindow &viewport_window)` | method | `void` | private | — |
| `update_manipulate_pole_tool()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `WORKFLOW_RENDER_LAYER` | variable | `GPlatesViewOperations::RenderedGeometryCollection::MainLayerType` | The main rendered layer used by this canvas tool workflow. |
| `GPLATES_GUI_POLEMANIPULATIONCANVASTOOLWORKFLOW_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/PoleManipulationCanvasToolWorkflow tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/CanvasToolWorkflows](CanvasToolWorkflows.md) | gui | 2 |

## Related

**Qt signal/slot connections** (4 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&d_feature_focus` | `focus_changed( GPlatesGui::FeatureFocus &)` | `this` | `update_enable_state()` |
| `&d_feature_focus` | `focus_changed(GPlatesGui::FeatureFocus &)` | `this` | `draw_feature_focus()` |
| `&d_feature_focus` | `focused_feature_modified(GPlatesGui::FeatureFocus &)` | `this` | `draw_feature_focus()` |
| `&d_rendered_geometry_parameters` | `parameters_changed(GPlatesViewOperations::RenderedGeometryParameters &)` | `this` | `draw_feature_focus()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/PoleManipulationCanvasToolWorkflow.h
python scripts/gpq.py def GPlatesGui::PoleManipulationCanvasToolWorkflow --body
python scripts/gpq.py uses PoleManipulationCanvasToolWorkflow --kind class
python scripts/gpq.py hier PoleManipulationCanvasToolWorkflow
```
