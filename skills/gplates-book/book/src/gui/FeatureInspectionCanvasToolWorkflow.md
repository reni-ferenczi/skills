# FeatureInspectionCanvasToolWorkflow

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 367 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/FeatureInspectionCanvasToolWorkflow.h` | C++ | 203 |
| `src/gui/FeatureInspectionCanvasToolWorkflow.cc` | C++ | 557 |

## Overview

[[[PROSE overview unit=gui/FeatureInspectionCanvasToolWorkflow tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::FeatureInspectionCanvasToolWorkflow`](#gplatesguifeatureinspectioncanvastoolworkflow) | class | [`CanvasToolWorkflow`](CanvasToolWorkflow.md) | — | 0 | The canvas tool workflow for query/editing a feature's properties including modifying its geometry using the MoveVertex tool, etc. |

## Members

### `GPlatesGui::FeatureInspectionCanvasToolWorkflow`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FeatureInspectionCanvasToolWorkflow( CanvasToolWorkflows &canvas_tool_workflows, GPlatesCanvasTools::GeometryOperationState &geometry_operation_state, GPlatesCanvasTools::ModifyGeometryState &modify_geometry_state, GPlatesCanvasTools::MeasureDistanceState &measure_distance_state, const GPlatesCanvasTools::CanvasTool::s ...` | constructor | `None` | public | — |
| `initialise()` | method | `void` | public | — |
| `activate_workflow()` | method | `void` | protected | — |
| `deactivate_workflow()` | method | `void` | protected | — |
| `get_selected_globe_and_map_canvas_tools( CanvasToolWorkflows::ToolType selected_tool)` | method | `boost::optional< std::pair<GPlatesGui::GlobeCanvasTool *, GPlatesGui::MapCanvasTool *> >` | protected | — |
| `draw_feature_focus()` | method | `void` | private | — |
| `update_enable_state()` | method | `void` | private | — |
| `d_canvas_tool_workflows` | field | `CanvasToolWorkflows` | private | For determining the curently active workflow/tool. |
| `d_feature_focus` | field | `FeatureFocus` | private | The focused feature, in part, determines which tools are enabled. |
| `d_focused_feature_geometry_builder` | field | `GPlatesViewOperations::GeometryBuilder` | private | — |
| `d_geometry_operation_state` | field | `GPlatesCanvasTools::GeometryOperationState` | private | — |
| `d_rendered_geom_collection` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | For rendering purposes |
| `d_rendered_geometry_parameters` | field | `GPlatesViewOperations::RenderedGeometryParameters` | private | Parameters for rendering geometries in canvas tools. |
| `d_render_settings` | field | `RenderSettings` | private | Show/hide geometry settings. |
| `d_symbol_map` | field | `GPlatesGui::symbol_map_type` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | Used to get current topological sections. |
| `d_viewport_window` | field | `GPlatesQtWidgets::ViewportWindow` | private | Used when restoring the clicked geometries on workflow activation. |
| `d_globe_measure_distance_tool` | field | `boost::scoped_ptr<GlobeCanvasTool>` | private | For measuring distance in the 3D globe view. |
| `d_map_measure_distance_tool` | field | `boost::scoped_ptr<MapCanvasTool>` | private | For measuring distance in the 2D map view. |
| `d_globe_click_geometry_tool` | field | `boost::scoped_ptr<GlobeCanvasTool>` | private | For clicking geometries in the 3D globe view. |
| `d_map_click_geometry_tool` | field | `boost::scoped_ptr<MapCanvasTool>` | private | For clicking geometries in the 2D map view. |
| `d_globe_move_vertex_tool` | field | `boost::scoped_ptr<GlobeCanvasTool>` | private | For moving geometry vertices in the 3D globe view. |
| `d_map_move_vertex_tool` | field | `boost::scoped_ptr<MapCanvasTool>` | private | For moving geometry vertices in the 2D map view. |
| `d_globe_delete_vertex_tool` | field | `boost::scoped_ptr<GlobeCanvasTool>` | private | For deleting geometry vertices in the 3D globe view. |
| `d_map_delete_vertex_tool` | field | `boost::scoped_ptr<MapCanvasTool>` | private | For deleting geometry vertices in the 2D map view. |
| `d_globe_insert_vertex_tool` | field | `boost::scoped_ptr<GlobeCanvasTool>` | private | For inserting geometry vertices in the 3D globe view. |
| `d_map_insert_vertex_tool` | field | `boost::scoped_ptr<MapCanvasTool>` | private | For inserting geometry vertices in the 2D map view. |
| `d_globe_split_feature_tool` | field | `boost::scoped_ptr<GlobeCanvasTool>` | private | For splitting features in the 3D globe view. |
| `d_map_split_feature_tool` | field | `boost::scoped_ptr<MapCanvasTool>` | private | For splitting features in the 2D map view. |
| `create_canvas_tools( CanvasToolWorkflows &canvas_tool_workflows, GPlatesCanvasTools::GeometryOperationState &geometry_operation_state, GPlatesCanvasTools::ModifyGeometryState &modify_geometry_state, GPlatesCanvasTools::MeasureDistanceState &measure_distance_state, const GPlatesCanvasTools::CanvasTool::status_bar_callba ...` | method | `void` | private | — |
| `get_geometry_builder_parameters()` | method | `std::pair<unsigned int, GPlatesMaths::GeometryType::Value>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `WORKFLOW_RENDER_LAYER` | variable | `GPlatesViewOperations::RenderedGeometryCollection::MainLayerType` | The main rendered layer used by this canvas tool workflow. |
| `GPLATES_GUI_FEATUREINSPECTIONCANVASTOOLWORKFLOW_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/FeatureInspectionCanvasToolWorkflow tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/CanvasToolWorkflows](CanvasToolWorkflows.md) | gui | 2 |

## Related

**Qt signal/slot connections** (5 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&d_feature_focus` | `focus_changed( GPlatesGui::FeatureFocus &)` | `this` | `update_enable_state()` |
| `&d_focused_feature_geometry_builder` | `stopped_updating_geometry_excluding_intermediate_moves()` | `this` | `update_enable_state()` |
| `&d_feature_focus` | `focus_changed(GPlatesGui::FeatureFocus &)` | `this` | `draw_feature_focus()` |
| `&d_feature_focus` | `focused_feature_modified(GPlatesGui::FeatureFocus &)` | `this` | `draw_feature_focus()` |
| `&d_rendered_geometry_parameters` | `parameters_changed(GPlatesViewOperations::RenderedGeometryParameters &)` | `this` | `draw_feature_focus()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/FeatureInspectionCanvasToolWorkflow.h
python scripts/gpq.py def GPlatesGui::FeatureInspectionCanvasToolWorkflow --body
python scripts/gpq.py uses FeatureInspectionCanvasToolWorkflow --kind class
python scripts/gpq.py hier FeatureInspectionCanvasToolWorkflow
```
