# CanvasToolWorkflow

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 297 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/CanvasToolWorkflow.h` | C++ | 262 |
| `src/gui/CanvasToolWorkflow.cc` | C++ | 241 |

## Overview

[[[PROSE overview unit=gui/CanvasToolWorkflow tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::CanvasToolWorkflow`](#gplatesguicanvastoolworkflow) | class | `QObject` | — | 7 | Abstract base class for a canvas tool workflow. |

## Members

### `GPlatesGui::CanvasToolWorkflow`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~CanvasToolWorkflow()` | destructor | `None` | public | — |
| `initialise()` | method | `void` | public | Initialise the workflow - such as enable/disable canvas tools. |
| `activate( boost::optional<CanvasToolWorkflows::ToolType> select_tool = boost::none)` | method | `void` | public | Activate the workflow (if not already active) and select the specified tool. |
| `deactivate()` | method | `void` | public | De-activates the current workflow. |
| `get_workflow()` | method | `CanvasToolWorkflows::WorkflowType` | public | Returns the workflow type of this workflow. |
| `get_selected_tool()` | method | `CanvasToolWorkflows::ToolType` | public | Returns the currently selected tool in the workflow. |
| `contains_tool( CanvasToolWorkflows::ToolType tool)` | method | `bool` | public | Returns true if this workflow contains the specified tool. |
| `is_tool_enabled( CanvasToolWorkflows::ToolType tool)` | method | `bool` | public | Returns true if the specified tool is currently enabled. |
| `canvas_tool_enabled( GPlatesGui::CanvasToolWorkflows::WorkflowType workflow, GPlatesGui::CanvasToolWorkflows::ToolType tool, bool enable)` | method | `void` | public | Emitted when a canvas tool is enabled/disabled. |
| `CanvasToolWorkflow( GPlatesQtWidgets::GlobeCanvas &globe_canvas, GPlatesQtWidgets::MapView &map_view, CanvasToolWorkflows::WorkflowType workflow, CanvasToolWorkflows::ToolType selected_tool)` | constructor | `None` | protected | — |
| `is_workflow_active()` | method | `bool` | protected | Returns true if this workflow is currently active. |
| `emit_canvas_tool_enabled( GPlatesGui::CanvasToolWorkflows::ToolType tool, bool enable)` | method | `void` | protected | Emits the canvas\_tool\_enabled signal. |
| `activate_workflow()` | method | `void` | protected | Implemented by derived class to perform any setup when workflow is activated. |
| `deactivate_workflow()` | method | `void` | protected | Implemented by derived class to perform any cleanup when workflow is deactivated. |
| `activating_selected_tool()` | method | `void` | protected | Notifies derived class about to activate the currently selected canvas tool. |
| `deactivated_selected_tool()` | method | `void` | protected | Notifies derived class that the currently selected canvas tool has just been deactivated. |
| `get_selected_globe_and_map_canvas_tools( CanvasToolWorkflows::ToolType selected_tool)` | method | `boost::optional< std::pair<GPlatesGui::GlobeCanvasTool *, GPlatesGui::MapCanvasTool *> >` | protected | Implemented by derived class to return the specified globe and map canvas tool, or none if the selected tool does not exist in this workflow (ie, if contains\_tool returns false). |
| `enabled_tools_seq_type` | typedef | `std::vector<bool>` | private | Typedef for a sequence of flags specifying which tools are enabled in this workflow. |
| `d_globe_canvas_tool_adapter` | field | `GlobeCanvasToolAdapter` | private | Feeds mouse events from GlobeCanvas to our selected \*globe-view\* tool. |
| `d_map_canvas_tool_adapter` | field | `MapCanvasToolAdapter` | private | Feeds mouse events from MapView to our selected \*map-view\* tool. |
| `d_workflow` | field | `CanvasToolWorkflows::WorkflowType` | private | The type of this workflow. |
| `d_selected_tool` | field | `CanvasToolWorkflows::ToolType` | private | The currently selected tool for this workflow. |
| `d_is_workflow_active` | field | `bool` | private | Is true if this workflow is currently active. |
| `d_is_selected_tool_active` | field | `bool` | private | Is true if the selected tool is currently active. |
| `d_enabled_tools` | field | `enabled_tools_seq_type` | private | Flags recording which tools, in this workflow, are currently enabled. |
| `activate_selected_tool()` | method | `void` | private | — |
| `deactivate_selected_tool()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_CANVASTOOLWORKFLOW_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/CanvasToolWorkflow tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/CanvasToolWorkflows](CanvasToolWorkflows.md) | gui | 30 |
| [gui/FeatureInspectionCanvasToolWorkflow](FeatureInspectionCanvasToolWorkflow.md) | gui | 20 |
| [gui/TopologyCanvasToolWorkflow](TopologyCanvasToolWorkflow.md) | gui | 12 |
| [gui/DigitisationCanvasToolWorkflow](DigitisationCanvasToolWorkflow.md) | gui | 10 |
| [gui/PoleManipulationCanvasToolWorkflow](PoleManipulationCanvasToolWorkflow.md) | gui | 6 |
| [gui/ViewCanvasToolWorkflow](ViewCanvasToolWorkflow.md) | gui | 6 |
| [gui/HellingerCanvasToolWorkflow](HellingerCanvasToolWorkflow.md) | gui | 5 |
| [gui/SmallCircleCanvasToolWorkflow](SmallCircleCanvasToolWorkflow.md) | gui | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/CanvasToolWorkflow.h
python scripts/gpq.py def GPlatesGui::CanvasToolWorkflow --body
python scripts/gpq.py uses CanvasToolWorkflow --kind class
python scripts/gpq.py hier CanvasToolWorkflow
```
