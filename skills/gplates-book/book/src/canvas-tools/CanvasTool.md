# CanvasTool

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 842 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/CanvasTool.h` | C++ | 281 |

## Overview

[[[PROSE overview unit=canvas-tools/CanvasTool tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCanvasTools::CanvasTool`](#gplatescanvastoolscanvastool) | class | [`GPlatesUtils::ReferenceCount<CanvasTool>`](../utils/ReferenceCount.md) | — | 13 | Base class for canvas tools that do not need to be implemented differently for globe and map views. |

## Members

### `GPlatesCanvasTools::CanvasTool`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~CanvasTool()` | destructor | `None` | public | — |
| `status_bar_callback_type` | typedef | `boost::function< void ( const char * ) >` | public | Typedef for a function that takes a C string and displays it on the status bar. |
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<CanvasTool>` | public | Convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<CanvasTool\>. |
| `handle_activation()` | method | `void` | public | — |
| `handle_deactivation()` | method | `void` | public | — |
| `handle_left_click( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `handle_left_press( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `handle_left_drag( const GPlatesMaths::PointOnSphere &initial_point_on_sphere, bool was_on_earth, double initial_proximity_inclusion_threshold, const GPlatesMaths::PointOnSphere &current_point_on_sphere, bool is_on_earth, double current_proximity_inclusion_threshold, const boost::optional<GPlatesMaths::PointOnSphere> &c ...` | method | `void` | public | — |
| `handle_left_release_after_drag( const GPlatesMaths::PointOnSphere &initial_point_on_sphere, bool was_on_earth, double initial_proximity_inclusion_threshold, const GPlatesMaths::PointOnSphere &current_point_on_sphere, bool is_on_earth, double current_proximity_inclusion_threshold, const boost::optional<GPlatesMaths::Poi ...` | method | `void` | public | — |
| `handle_shift_left_click( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `handle_shift_left_drag( const GPlatesMaths::PointOnSphere &initial_point_on_sphere, bool was_on_earth, double initial_proximity_inclusion_threshold, const GPlatesMaths::PointOnSphere &current_point_on_sphere, bool is_on_earth, double current_proximity_inclusion_threshold, const boost::optional<GPlatesMaths::PointOnSphe ...` | method | `void` | public | — |
| `handle_shift_left_release_after_drag( const GPlatesMaths::PointOnSphere &initial_point_on_sphere, bool was_on_earth, double initial_proximity_inclusion_threshold, const GPlatesMaths::PointOnSphere &current_point_on_sphere, bool is_on_earth, double current_proximity_inclusion_threshold, const boost::optional<GPlatesMath ...` | method | `void` | public | — |
| `handle_ctrl_left_click( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `handle_ctrl_left_drag( const GPlatesMaths::PointOnSphere &initial_point_on_sphere, bool was_on_earth, double initial_proximity_inclusion_threshold, const GPlatesMaths::PointOnSphere &current_point_on_sphere, bool is_on_earth, double current_proximity_inclusion_threshold, const boost::optional<GPlatesMaths::PointOnSpher ...` | method | `bool` | public | — |
| `handle_ctrl_left_release_after_drag( const GPlatesMaths::PointOnSphere &initial_point_on_sphere, bool was_on_earth, double initial_proximity_inclusion_threshold, const GPlatesMaths::PointOnSphere &current_point_on_sphere, bool is_on_earth, double current_proximity_inclusion_threshold, const boost::optional<GPlatesMaths ...` | method | `bool` | public | — |
| `handle_shift_ctrl_left_click( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `handle_shift_ctrl_left_drag( const GPlatesMaths::PointOnSphere &initial_point_on_sphere, bool was_on_earth, double initial_proximity_inclusion_threshold, const GPlatesMaths::PointOnSphere &current_point_on_sphere, bool is_on_earth, double current_proximity_inclusion_threshold, const boost::optional<GPlatesMaths::PointO ...` | method | `bool` | public | — |
| `handle_shift_ctrl_left_release_after_drag( const GPlatesMaths::PointOnSphere &initial_point_on_sphere, bool was_on_earth, double initial_proximity_inclusion_threshold, const GPlatesMaths::PointOnSphere &current_point_on_sphere, bool is_on_earth, double current_proximity_inclusion_threshold, const boost::optional<GPlate ...` | method | `bool` | public | — |
| `handle_move_without_drag( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `CanvasTool( const status_bar_callback_type &status_bar_callback)` | constructor | `None` | protected | Constructs CanvasTool, given status\_bar\_callback that can be used by the canvas tool to set status bar messages. |
| `set_status_bar_message( const char *message)` | method | `void` | protected | Subclasses call this function to set text on the status bar. |
| `d_status_bar_callback` | field | `status_bar_callback_type` | private | The callback used to show text on the status bar. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_CANVASTOOLS_CANVASTOOL_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=canvas-tools/CanvasTool tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/DigitisationCanvasToolWorkflow](../gui/DigitisationCanvasToolWorkflow.md) | gui | 52 |
| [gui/FeatureInspectionCanvasToolWorkflow](../gui/FeatureInspectionCanvasToolWorkflow.md) | gui | 47 |
| [canvas-tools/CanvasToolAdapterForMap](CanvasToolAdapterForMap.md) | canvas-tools | 42 |
| [canvas-tools/MeasureDistance](MeasureDistance.md) | canvas-tools | 36 |
| [canvas-tools/SelectHellingerGeometries](SelectHellingerGeometries.md) | canvas-tools | 27 |
| [gui/PoleManipulationCanvasToolWorkflow](../gui/PoleManipulationCanvasToolWorkflow.md) | gui | 25 |
| [canvas-tools/CanvasToolAdapterForGlobe](CanvasToolAdapterForGlobe.md) | canvas-tools | 24 |
| [canvas-tools/MoveVertex](MoveVertex.md) | canvas-tools | 20 |
| [gui/SmallCircleCanvasToolWorkflow](../gui/SmallCircleCanvasToolWorkflow.md) | gui | 20 |
| [gui/ViewCanvasToolWorkflow](../gui/ViewCanvasToolWorkflow.md) | gui | 19 |
| [gui/CanvasToolWorkflows](../gui/CanvasToolWorkflows.md) | gui | 17 |
| [canvas-tools/CreateSmallCircle](CreateSmallCircle.md) | canvas-tools | 16 |
| [canvas-tools/InsertVertex](InsertVertex.md) | canvas-tools | 16 |
| [canvas-tools/SplitFeature](SplitFeature.md) | canvas-tools | 16 |
| [gui/TopologyCanvasToolWorkflow](../gui/TopologyCanvasToolWorkflow.md) | gui | 16 |
| [canvas-tools/DeleteVertex](DeleteVertex.md) | canvas-tools | 15 |
| [canvas-tools/DigitiseGeometry](DigitiseGeometry.md) | canvas-tools | 15 |
| [gui/HellingerCanvasToolWorkflow](../gui/HellingerCanvasToolWorkflow.md) | gui | 15 |
| [canvas-tools/ManipulatePole](ManipulatePole.md) | canvas-tools | 14 |
| [canvas-tools/ClickGeometry](ClickGeometry.md) | canvas-tools | 12 |

*... and 20 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/canvas-tools/CanvasTool.h
python scripts/gpq.py def GPlatesCanvasTools::CanvasTool --body
python scripts/gpq.py uses CanvasTool --kind class
python scripts/gpq.py hier CanvasTool
```
