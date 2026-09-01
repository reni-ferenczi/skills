# CanvasToolWorkflows

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 243 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/CanvasToolWorkflows.h` | C++ | 278 |
| `src/gui/CanvasToolWorkflows.cc` | C++ | 332 |

## Overview

[[[PROSE overview unit=gui/CanvasToolWorkflows tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::CanvasToolWorkflows`](#gplatesguicanvastoolworkflows) | class | `QObject` | — | 0 | Manages the canvas tool 'workflows'. |

## Members

### `GPlatesGui::CanvasToolWorkflows`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `WorkflowType` | enum | `None` | public | The canvas tool work - corresponds to tabs on the tabbed canvas tool bar widget. |
| `ToolType` | enum | `None` | public | The type of canvas tool. |
| `CanvasToolWorkflows()` | constructor | `None` | public | — |
| `initialise( GPlatesCanvasTools::GeometryOperationState &geometry_operation_state, GPlatesCanvasTools::ModifyGeometryState &modify_geometry_state, GPlatesCanvasTools::MeasureDistanceState &measure_distance_state, const GPlatesCanvasTools::CanvasTool::status_bar_callback_type &status_bar_callback, GPlatesPresentation::Vi ...` | method | `void` | public | Call once everything is setup (including the GUI). |
| `activate()` | method | `void` | public | Call once the application's main window is visible. |
| `get_active_canvas_tool()` | method | `std::pair<WorkflowType, ToolType>` | public | Returns the currently active canvas tool workflow/tool. |
| `get_selected_canvas_tool_in_workflow( WorkflowType workflow)` | method | `ToolType` | public | Returns the currently selected tool in the specified workflow. |
| `is_canvas_tool_enabled( WorkflowType workflow, ToolType tool)` | method | `bool` | public | Returns true if the specified workflow/tool is currently enabled. |
| `does_workflow_contain_tool( WorkflowType workflow, ToolType tool)` | method | `bool` | public | Returns true if the specified workflow contains the specified tool. |
| `choose_canvas_tool( ToolType tool)` | method | `void` | public | Makes the specified canvas tool the currently active tool. |
| `choose_canvas_tool( GPlatesGui::CanvasToolWorkflows::WorkflowType workflow, boost::optional<GPlatesGui::CanvasToolWorkflows::ToolType> tool = boost::none)` | method | `void` | public | Makes the specified canvas workflow/tool the currently active workflow/tool. |
| `canvas_tool_enabled( GPlatesGui::CanvasToolWorkflows::WorkflowType workflow, GPlatesGui::CanvasToolWorkflows::ToolType tool, bool enable)` | method | `void` | public | Emitted when a canvas tool in a workflow is enabled/disabled. |
| `canvas_tool_activated( GPlatesGui::CanvasToolWorkflows::WorkflowType workflow, GPlatesGui::CanvasToolWorkflows::ToolType tool)` | method | `void` | public | Emitted when a canvas tool in a workflow is activated. |
| `handle_canvas_tool_enabled( GPlatesGui::CanvasToolWorkflows::WorkflowType workflow, GPlatesGui::CanvasToolWorkflows::ToolType tool, bool enable)` | method | `void` | private | This handler is connected to each individual workflow. |
| `canvas_tool_workflow_seq_type` | typedef | `std::vector< boost::shared_ptr<CanvasToolWorkflow> >` | private | Typedef for a sequence of canvas tool workflows. |
| `d_canvas_tool_workflows` | field | `canvas_tool_workflow_seq_type` | private | — |
| `d_active_workflow` | field | `WorkflowType` | private | The currently active workflow. |
| `create_canvas_tool_workflows( GPlatesCanvasTools::GeometryOperationState &geometry_operation_state, GPlatesCanvasTools::ModifyGeometryState &modify_geometry_state, GPlatesCanvasTools::MeasureDistanceState &measure_distance_state, const GPlatesCanvasTools::CanvasTool::status_bar_callback_type &status_bar_callback, GPlat ...` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_CANVASTOOLWORKFLOWS_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/CanvasToolWorkflows tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/CanvasToolBarDockWidget](../qt-widgets/CanvasToolBarDockWidget.md) | qt-widgets | 367 |
| [qt-widgets/ScalarField3DLayerOptionsWidget](../qt-widgets/ScalarField3DLayerOptionsWidget.md) | qt-widgets | 203 |
| [gui/Dialogs](Dialogs.md) | gui | 171 |
| [gui/TopologyTools](TopologyTools.md) | gui | 138 |
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](../qt-widgets/TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 124 |
| [gui/FileIOFeedback](FileIOFeedback.md) | gui | 90 |
| [qt-widgets/RasterLayerOptionsWidget](../qt-widgets/RasterLayerOptionsWidget.md) | qt-widgets | 81 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 76 |
| [gui/TopologyCanvasToolWorkflow](TopologyCanvasToolWorkflow.md) | gui | 70 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 70 |
| [qt-widgets/ReconstructScalarCoverageLayerOptionsWidget](../qt-widgets/ReconstructScalarCoverageLayerOptionsWidget.md) | qt-widgets | 69 |
| [qt-widgets/PythonConsoleDialog](../qt-widgets/PythonConsoleDialog.md) | qt-widgets | 67 |
| [qt-widgets/VisualLayerWidget](../qt-widgets/VisualLayerWidget.md) | qt-widgets | 66 |
| [qt-widgets/DrawStyleDialog](../qt-widgets/DrawStyleDialog.md) | qt-widgets | 60 |
| [gui/CanvasToolWorkflow](CanvasToolWorkflow.md) | gui | 47 |
| [qt-widgets/ReconstructionViewWidget](../qt-widgets/ReconstructionViewWidget.md) | qt-widgets | 46 |
| [qt-widgets/TopologyToolsWidget](../qt-widgets/TopologyToolsWidget.md) | qt-widgets | 46 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 44 |
| [qt-widgets/ModifyReconstructionPoleWidget](../qt-widgets/ModifyReconstructionPoleWidget.md) | qt-widgets | 43 |
| [gui/FeatureInspectionCanvasToolWorkflow](FeatureInspectionCanvasToolWorkflow.md) | gui | 41 |

*... and 57 more units.*

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `canvas_tool_workflow.get()` | `canvas_tool_enabled( GPlatesGui::CanvasToolWorkflows::WorkflowType, GPlatesGui::CanvasToolWorkflows::ToolType, bool)` | `this` | `handle_canvas_tool_enabled( GPlatesGui::CanvasToolWorkflows::WorkflowType, GPlatesGui::CanvasToolWorkflows::ToolType, bool)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/CanvasToolWorkflows.h
python scripts/gpq.py def GPlatesGui::CanvasToolWorkflows --body
python scripts/gpq.py uses CanvasToolWorkflows --kind class
python scripts/gpq.py hier CanvasToolWorkflows
```
