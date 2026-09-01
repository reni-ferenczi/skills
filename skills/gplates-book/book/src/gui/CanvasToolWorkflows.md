# CanvasToolWorkflows

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 243 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/CanvasToolWorkflows.h` | C++ | 278 |
| `src/gui/CanvasToolWorkflows.cc` | C++ | 332 |

## Overview

This is the registry and switchboard for every interactive tool on the globe and
map. A *workflow* is one tab of the canvas tool bar — View, Feature Inspection,
Digitisation, Topology, Pole Manipulation, Small Circle, Hellinger — and the
central design decision is that each workflow keeps its own *selected* tool
independently, while only one of them is *active* at a time. That is what lets a
user leave a half-digitised polyline selected in the digitisation tab, switch to
feature inspection to look something up, and come back to the tool they were
using. `get_selected_canvas_tool_in_workflow()` answers the per-workflow
question; `get_active_canvas_tool()` answers the global one, and it is defined as
the selected tool of the active workflow.

The class itself is deliberately thin: it holds `NUM_WORKFLOWS`
`CanvasToolWorkflow` objects indexed directly by `WorkflowType`, plus the single
`d_active_workflow` index. Every query — `is_canvas_tool_enabled`,
`does_workflow_contain_tool`, `get_selected_canvas_tool_in_workflow` — forwards
straight to the workflow at that index, and `choose_canvas_tool` is the only
place any state changes: it deactivates the outgoing workflow, updates
`d_active_workflow`, and calls `activate(tool)` on the incoming one. All the real
per-tool behaviour lives in the seven `CanvasToolWorkflow` subclasses
(`ViewCanvasToolWorkflow`, `FeatureInspectionCanvasToolWorkflow`,
`DigitisationCanvasToolWorkflow`, `TopologyCanvasToolWorkflow`,
`PoleManipulationCanvasToolWorkflow`, `SmallCircleCanvasToolWorkflow`,
`HellingerCanvasToolWorkflow`), each of which owns the globe/map canvas-tool pair
for its tools and decides which of them are enabled.

`ViewportWindow` owns the single instance and is the reason the fan-in on this
page is so wide: `WorkflowType`/`ToolType` are the vocabulary the whole UI uses
to talk about tools, so dozens of dialogs and layer-option widgets include this
header just for the enums, and several — `CreateFeatureDialog`, `TopologyTools`,
`ModifyReconstructionPoleWidget` — call `choose_canvas_tool()` to move the user
to the right tool after an operation. In the other direction the two signals are
the notification channel: `canvas_tool_activated` is what makes
`ViewportWindow` swap the task-panel tab and what
`CanvasToolBarDockWidget` uses to keep its buttons in sync, and
`canvas_tool_enabled` is simply re-emitted from the individual workflows so
clients can connect to one object instead of seven.

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

**Three-phase construction, and the order is load-bearing.** The constructor does
almost nothing (it only sets `d_active_workflow` to `WORKFLOW_VIEW`);
`initialise()` builds the seven workflows, wires their `canvas_tool_enabled`
signals and calls `initialise()` on each; `activate()` then activates the default
workflow and emits the first `canvas_tool_activated`. `ViewportWindow` splits
these deliberately — `initialise()` runs only after the tool bar dock and task
panel exist (the workflows construct canvas tools that reference them), and
`activate()` runs only after the main window is visible, with a comment noting
that otherwise the default tool does not get activated because the globe canvas
is not yet shown. Every public accessor asserts `!d_canvas_tool_workflows.empty()`,
so calling anything before `initialise()` is an assertion failure rather than
undefined behaviour.

**`d_canvas_tool_workflows` is indexed by the enum, not searched.**
`create_canvas_tool_workflows` does `resize(NUM_WORKFLOWS)` and then assigns each
slot by name, so `WorkflowType` values are array indices. Adding a workflow means
adding the enumerator *before* `NUM_WORKFLOWS` and adding the matching `reset()`
— miss the second and you get a null `shared_ptr` that `initialise()` asserts on.
No index is range-checked in the accessors; passing `NUM_WORKFLOWS` walks off the
end.

**`ToolType` is not partitioned by workflow.** The same tool can appear in more
than one workflow (`TOOL_DRAG_GLOBE` and `TOOL_ZOOM_GLOBE` are in most of them),
and no workflow contains every tool. This is why there are two
`choose_canvas_tool` overloads. The single-argument one scans all workflows and
throws `GPlatesGlobal::PreconditionViolationError` if the tool is found in more
than one — so it is only safe for tools you know are unique, and code that wants
a shared tool must name the workflow explicitly. Passing a workflow/tool pair
where `does_workflow_contain_tool()` is false also ends in an exception, not a
silent no-op.

**`choose_canvas_tool` is a no-op when nothing changes, including the signal.**
The early return when the requested workflow and tool already match means
`canvas_tool_activated` is *not* re-emitted for a redundant selection. Anything
that relies on the signal to resynchronise its own state — a task-panel tab, a
tool-bar button — will not be corrected by re-choosing the current tool.
Conversely, when only the tool changes within the active workflow, the workflow
is not deactivated and reactivated; `CanvasToolWorkflow::activate()` deactivates
just the outgoing tool.

Smaller points:

- `TOOL_CHANGE_LIGHTING` sits inside an `#if 0` in the middle of the `ToolType`
  enum, with a comment about deferring the lighting tool until volume
  visualisation ships. Enabling it renumbers every subsequent enumerator — fine
  here because nothing persists these values, but worth knowing before you assume
  the numbering is stable.
- `handle_canvas_tool_enabled` asserts that `sender()` really is the workflow
  registered at the `workflow` index it was told about, i.e. it does not trust
  the signal's own arguments. Keep that check if you re-wire the connections.
- Everything is single-threaded Qt GUI code; `initialise()` also takes a
  `status_bar_callback_type` (a `boost::function` bound to `ViewportWindow`) that
  it merely forwards to each workflow, so the callback must outlive them.

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
