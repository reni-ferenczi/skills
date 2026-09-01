# CanvasToolWorkflow

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 297 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/CanvasToolWorkflow.h` | C++ | 262 |
| `src/gui/CanvasToolWorkflow.cc` | C++ | 241 |

## Overview

Abstract base for one "tab" of related canvas tools — a *workflow* such as
digitisation, feature inspection, or topology editing, each grouping the
`CanvasToolWorkflows::ToolType` values that make sense together. A concrete
subclass supplies which globe/map tool pair backs each `ToolType` it
supports (`get_selected_globe_and_map_canvas_tools`), and hooks for setup and
teardown when the whole workflow is switched in or out
(`activate_workflow`/`deactivate_workflow`). The base class owns the
`GlobeCanvasToolAdapter` and `MapCanvasToolAdapter` that route mouse events
from `GlobeCanvas`/`MapView` to whichever concrete `GlobeCanvasTool`/
`MapCanvasTool` is currently selected, so subclasses never touch the adapters
directly.

`activate()`/`deactivate()` implement the state machine: activating a
workflow calls the derived class's `activate_workflow()` once, then activates
the selected tool; switching tools within an already-active workflow
deactivates the old tool and activates the new one without re-running
`activate_workflow()`. Individual tools can also be independently enabled or
disabled (`emit_canvas_tool_enabled`) — for example because another tool left
the application in a state where the current selection no longer makes
sense — and the currently selected tool is auto-activated or -deactivated
to track its own enabled flag while the workflow is active. `CanvasToolWorkflows`
is the concrete owner that switches between the seven `CanvasToolWorkflow`
subclasses as the user changes tabs.

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

`activate_selected_tool()` silently does nothing if the selected tool is
currently disabled (this is the normal path when switching tabs leaves a
disabled tool selected), but if the workflow is active and the tool is
enabled, it asserts (`GPlatesGlobal::Assert`) that
`get_selected_globe_and_map_canvas_tools` actually returns a tool and that no
tool is already active — a derived class that reports `contains_tool() ==
true` for a tool it cannot actually supply, or that double-activates, is a
programming error, not a runtime condition to recover from.
`is_tool_enabled`/`emit_canvas_tool_enabled` likewise assert the `ToolType`
is within `d_enabled_tools`, which is sized to `CanvasToolWorkflows::NUM_TOOLS`
and defaults every tool to disabled.

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
