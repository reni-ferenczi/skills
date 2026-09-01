# MovePoleGlobe

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 982 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/MovePoleGlobe.h` | C++ | 119 |
| `src/canvas-tools/MovePoleGlobe.cc` | C++ | 142 |

## Overview

[[[PROSE overview unit=canvas-tools/MovePoleGlobe tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCanvasTools::MovePoleGlobe`](#gplatescanvastoolsmovepoleglobe) | class | [`GPlatesGui::GlobeCanvasTool`](../gui/GlobeCanvasTool.md) | — | 0 | This is the globe canvas tool used to move the pole location used by ManipulatePole tool for adjusting rotations. |

## Members

### `GPlatesCanvasTools::MovePoleGlobe`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MovePoleGlobe( const GPlatesViewOperations::MovePoleOperation::non_null_ptr_type &move_pole_operation, GPlatesGui::Globe &globe_, GPlatesQtWidgets::GlobeCanvas &globe_canvas_, GPlatesQtWidgets::ViewportWindow &viewport_window_)` | constructor | `None` | public | Create a MovePoleGlobe instance. |
| `handle_activation()` | method | `void` | public | — |
| `handle_deactivation()` | method | `void` | public | — |
| `handle_left_drag( const GPlatesMaths::PointOnSphere &initial_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_initial_pos_on_globe, bool was_on_globe, const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, const GPlatesMaths: ...` | method | `void` | public | — |
| `handle_left_release_after_drag( const GPlatesMaths::PointOnSphere &initial_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_initial_pos_on_globe, bool was_on_globe, const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, const ...` | method | `void` | public | — |
| `handle_move_without_drag( const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, const GPlatesMaths::PointOnSphere &oriented_centre_of_viewport)` | method | `void` | public | — |
| `d_viewport_window` | field | `GPlatesQtWidgets::ViewportWindow` | private | This is the View State used to pass messages to the status bar. |
| `d_move_pole_operation` | field | `GPlatesViewOperations::MovePoleOperation::non_null_ptr_type` | private | Handles changes to the pole location for us. |
| `d_is_in_drag` | field | `bool` | private | Whether or not this tool is currently in the midst of a drag. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_CANVAS_TOOLS_MOVEPOLEGLOBE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=canvas-tools/MovePoleGlobe tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/PoleManipulationCanvasToolWorkflow](../gui/PoleManipulationCanvasToolWorkflow.md) | gui | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/canvas-tools/MovePoleGlobe.h
python scripts/gpq.py def GPlatesCanvasTools::MovePoleGlobe --body
python scripts/gpq.py uses MovePoleGlobe --kind class
python scripts/gpq.py hier MovePoleGlobe
```
