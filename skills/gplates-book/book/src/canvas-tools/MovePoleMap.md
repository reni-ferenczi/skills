# MovePoleMap

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 388 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/MovePoleMap.h` | C++ | 118 |
| `src/canvas-tools/MovePoleMap.cc` | C++ | 206 |

## Overview

[[[PROSE overview unit=canvas-tools/MovePoleMap tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCanvasTools::MovePoleMap`](#gplatescanvastoolsmovepolemap) | class | [`GPlatesGui::MapCanvasTool`](../gui/MapCanvasTool.md) | — | 0 | This is the map canvas tool used to move the pole location used by ManipulatePole tool for adjusting rotations. |

## Members

### `GPlatesCanvasTools::MovePoleMap`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MovePoleMap( const GPlatesViewOperations::MovePoleOperation::non_null_ptr_type &move_pole_operation, GPlatesQtWidgets::MapCanvas &map_canvas_, GPlatesQtWidgets::MapView &map_view_, GPlatesQtWidgets::ViewportWindow &viewport_window_, GPlatesPresentation::ViewState &view_state_)` | constructor | `None` | public | Create a MovePoleMap instance. |
| `handle_activation()` | method | `void` | public | — |
| `handle_deactivation()` | method | `void` | public | — |
| `handle_left_drag( const QPointF &initial_point_on_scene, bool was_on_surface, const QPointF &current_point_on_scene, bool is_on_surface, const QPointF &translation)` | method | `void` | public | — |
| `handle_left_release_after_drag( const QPointF &initial_point_on_scene, bool was_on_surface, const QPointF &current_point_on_scene, bool is_on_surface, const QPointF &translation)` | method | `void` | public | — |
| `handle_move_without_drag( const QPointF &current_point_on_scene, bool is_on_surface, const QPointF &translation)` | method | `void` | public | — |
| `d_viewport_window_ptr` | field | `GPlatesQtWidgets::ViewportWindow` | private | This is the window that has the status bar. |
| `d_move_pole_operation` | field | `GPlatesViewOperations::MovePoleOperation::non_null_ptr_type` | private | Handles changes to the pole location for us. |
| `d_is_in_drag` | field | `bool` | private | Whether or not this tool is currently in the midst of a drag. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_CANVAS_TOOLS_MOVEPOLEMAP_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=canvas-tools/MovePoleMap tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/PoleManipulationCanvasToolWorkflow](../gui/PoleManipulationCanvasToolWorkflow.md) | gui | 6 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/canvas-tools/MovePoleMap.h
python scripts/gpq.py def GPlatesCanvasTools::MovePoleMap --body
python scripts/gpq.py uses MovePoleMap --kind class
python scripts/gpq.py hier MovePoleMap
```
