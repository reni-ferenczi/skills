# ManipulatePole

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 577 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/ManipulatePole.h` | C++ | 143 |
| `src/canvas-tools/ManipulatePole.cc` | C++ | 161 |

## Overview

Canvas tool for interactively adjusting plate rotation poles by dragging geometry on the globe. It delegates rotation accumulation to a `ModifyReconstructionPoleWidget`, which tracks the total rotation adjustment applied during the operation. Supports two drag modes: normal left-drag adjusts the pole, while shift-left-drag applies a different style of adjustment. Tracks drag state to ensure proper initialization and finalization of each manipulation.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCanvasTools::ManipulatePole`](#gplatescanvastoolsmanipulatepole) | class | [`CanvasTool`](CanvasTool.md) | — | 0 | This is the canvas tool used to interactively manipulate absolute rotations. |

## Members

### `GPlatesCanvasTools::ManipulatePole`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( const status_bar_callback_type &status_bar_callback, GPlatesViewOperations::RenderedGeometryCollection &rendered_geom_collection, GPlatesQtWidgets::ModifyReconstructionPoleWidget &pole_widget)` | method | `non_null_ptr_type` | public | — |
| `handle_activation()` | method | `void` | public | — |
| `handle_deactivation()` | method | `void` | public | — |
| `handle_left_drag( const GPlatesMaths::PointOnSphere &initial_point_on_sphere, bool was_on_earth, double initial_proximity_inclusion_threshold, const GPlatesMaths::PointOnSphere &current_point_on_sphere, bool is_on_earth, double current_proximity_inclussion_threshold, const boost::optional<GPlatesMaths::PointOnSphere> & ...` | method | `void` | public | — |
| `handle_left_release_after_drag( const GPlatesMaths::PointOnSphere &initial_point_on_sphere, bool was_on_earth, double initial_proximity_inclusion_threshold, const GPlatesMaths::PointOnSphere &current_point_on_sphere, bool is_on_earth, double current_proximity_inclussion_threshold, const boost::optional<GPlatesMaths::Po ...` | method | `void` | public | — |
| `handle_shift_left_drag( const GPlatesMaths::PointOnSphere &initial_point_on_sphere, bool was_on_earth, double initial_proximity_inclusion_threshold, const GPlatesMaths::PointOnSphere &current_point_on_sphere, bool is_on_earth, double current_proximity_inclussion_threshold, const boost::optional<GPlatesMaths::PointOnSph ...` | method | `void` | public | — |
| `handle_shift_left_release_after_drag( const GPlatesMaths::PointOnSphere &initial_point_on_sphere, bool was_on_earth, double initial_proximity_inclusion_threshold, const GPlatesMaths::PointOnSphere &current_point_on_sphere, bool is_on_earth, double current_proximity_inclussion_threshold, const boost::optional<GPlatesMat ...` | method | `void` | public | — |
| `ManipulatePole( const status_bar_callback_type &status_bar_callback, GPlatesViewOperations::RenderedGeometryCollection &rendered_geom_collection, GPlatesQtWidgets::ModifyReconstructionPoleWidget &pole_widget)` | constructor | `None` | private | — |
| `d_rendered_geom_collection` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | We need to change which canvas-tool layer is shown when this canvas-tool is activated. |
| `d_pole_widget_ptr` | field | `GPlatesQtWidgets::ModifyReconstructionPoleWidget` | private | This is the Modify Reconstruction Pole widget in the Task Panel. |
| `d_is_in_drag` | field | `bool` | private | Whether or not this pole-manipulation tool is currently in the midst of a pole-manipulating drag. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_CANVASTOOLS_MANIPULATEPOLE_H` | macro | `None` | — |

## Notes

The `d_is_in_drag` boolean ensures that `start_new_drag` is called exactly once per drag sequence; subsequent `handle_left_drag` or `handle_shift_left_drag` calls during the same drag only update the position. Left-drag and shift-left-drag are distinct interaction modes: normal drag rotates via one mechanism, shift-drag via another. Release calls finalize the accumulated rotation.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/PoleManipulationCanvasToolWorkflow](../gui/PoleManipulationCanvasToolWorkflow.md) | gui | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/canvas-tools/ManipulatePole.h
python scripts/gpq.py def GPlatesCanvasTools::ManipulatePole --body
python scripts/gpq.py uses ManipulatePole --kind class
python scripts/gpq.py hier ManipulatePole
```
