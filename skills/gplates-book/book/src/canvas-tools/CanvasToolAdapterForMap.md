# CanvasToolAdapterForMap

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 388 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/CanvasToolAdapterForMap.h` | C++ | 248 |
| `src/canvas-tools/CanvasToolAdapterForMap.cc` | C++ | 414 |

## Overview

`CanvasToolAdapterForMap` is the map-side counterpart of `CanvasToolAdapterForGlobe`: it implements `GPlatesGui::MapCanvasTool`, whose events arrive as flat `QPointF` scene coordinates, and forwards them to the same widget-agnostic `CanvasTool` interface used by the globe. Unlike the globe adapter, which just repackages already-spherical coordinates, this one does real work — `invoke_canvas_tool_func()` converts each scene point to a `GPlatesMaths::PointOnSphere` via `qpointf_to_point_on_sphere()` and the map's `GPlatesGui::MapProjection`, computes the proximity-inclusion threshold at that point through `MapView::current_proximity_inclusion_threshold()`, and only then calls through a member-function pointer (`canvas_tool_click_func`, `canvas_tool_drag_func_with_default`/`_without_default`) into `d_canvas_tool_ptr`. The three private overloads of `invoke_canvas_tool_func()` centralise that conversion once for clicks, once for two-point drags, and once for drags with a "cancel/no-op" default action, so each public `handle_*` override is a short one-line call into whichever overload fits its signature.

If a click or drag point is not on the map surface, or fails to project back to a point on the sphere, the corresponding `handle_*` call is silently dropped — the code notes this is a known limitation until map clicks can snap to the map's edge the way globe clicks snap to the horizon.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCanvasTools::CanvasToolAdapterForMap`](#gplatescanvastoolscanvastooladapterformap) | class | [`GPlatesGui::MapCanvasTool`](../gui/MapCanvasTool.md) | — | 0 | Adapter class for CanvasTool -\> MapCanvasTool |

## Members

### `GPlatesCanvasTools::CanvasToolAdapterForMap`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CanvasToolAdapterForMap( const CanvasTool::non_null_ptr_type &canvas_tool_ptr, GPlatesQtWidgets::MapCanvas &map_canvas_, GPlatesQtWidgets::MapView &map_view_, GPlatesGui::MapTransform &map_transform_)` | constructor | `None` | public | Create a CanvasToolAdapterForMap instance. |
| `handle_activation()` | method | `void` | public | — |
| `handle_deactivation()` | method | `void` | public | — |
| `handle_left_press( const QPointF &click_point_on_scene, bool is_on_surface)` | method | `void` | public | — |
| `handle_left_click( const QPointF &click_point_on_scene, bool is_on_surface)` | method | `void` | public | — |
| `handle_left_drag( const QPointF &initial_point_on_scene, bool was_on_surface, const QPointF &current_point_on_scene, bool is_on_surface, const QPointF &translation)` | method | `void` | public | — |
| `handle_left_release_after_drag( const QPointF &initial_point_on_scene, bool was_on_surface, const QPointF &current_point_on_scene, bool is_on_surface, const QPointF &translation)` | method | `void` | public | — |
| `handle_shift_left_click( const QPointF &click_point_on_scene, bool is_on_surface)` | method | `void` | public | — |
| `handle_shift_left_drag( const QPointF &initial_point_on_scene, bool was_on_surface, const QPointF &current_point_on_scene, bool is_on_surface, const QPointF &translation)` | method | `void` | public | — |
| `handle_shift_left_release_after_drag( const QPointF &initial_point_on_scene, bool was_on_surface, const QPointF &current_point_on_scene, bool is_on_surface)` | method | `void` | public | — |
| `handle_ctrl_left_click( const QPointF &click_point_on_scene, bool is_on_surface)` | method | `void` | public | — |
| `handle_ctrl_left_drag( const QPointF &initial_point_on_scene, bool was_on_surface, const QPointF &current_point_on_scene, bool is_on_surface, const QPointF &translation)` | method | `void` | public | — |
| `handle_ctrl_left_release_after_drag( const QPointF &initial_point_on_scene, bool was_on_surface, const QPointF &current_point_on_scene, bool is_on_surface)` | method | `void` | public | — |
| `handle_shift_ctrl_left_click( const QPointF &click_point_on_scene, bool is_on_surface)` | method | `void` | public | — |
| `handle_shift_ctrl_left_drag( const QPointF &initial_point_on_scene, bool was_on_surface, const QPointF &current_point_on_scene, bool is_on_surface, const QPointF &translation)` | method | `void` | public | — |
| `handle_move_without_drag( const QPointF &current_point_on_scene, bool is_on_surface, const QPointF &translation)` | method | `void` | public | — |
| `invoke_canvas_tool_func( const QPointF &click_point_on_scene, bool is_on_surface, const canvas_tool_click_func &func)` | method | `void` | private | — |
| `invoke_canvas_tool_func( const QPointF &initial_point_on_scene, bool was_on_surface, const QPointF &current_point_on_scene, bool is_on_surface, const canvas_tool_drag_func_without_default &func)` | method | `void` | private | — |
| `invoke_canvas_tool_func( const QPointF &initial_point_on_scene, bool was_on_surface, const QPointF &current_point_on_scene, bool is_on_surface, const canvas_tool_drag_func_with_default &func)` | method | `bool` | private | — |
| `d_canvas_tool_ptr` | field | `CanvasTool::non_null_ptr_type` | private | A pointer to the CanvasTool instance that we wrap around |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_CANVASTOOLS_CANVASTOOLADAPTERFORMAP_H` | macro | `None` | — |

## Notes

As with the globe adapter, `handle_deactivation()` checks `map_view().isVisible()` before forwarding, specifically to avoid deactivating the wrapped `CanvasTool` twice when both a globe and a map adapter wrap the same instance. `handle_shift_ctrl_left_release_after_drag` is commented out in the header because the corresponding virtual is itself commented out in `MapCanvasTool`.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/DigitisationCanvasToolWorkflow](../gui/DigitisationCanvasToolWorkflow.md) | gui | 8 |
| [gui/FeatureInspectionCanvasToolWorkflow](../gui/FeatureInspectionCanvasToolWorkflow.md) | gui | 7 |
| [gui/TopologyCanvasToolWorkflow](../gui/TopologyCanvasToolWorkflow.md) | gui | 6 |
| [gui/HellingerCanvasToolWorkflow](../gui/HellingerCanvasToolWorkflow.md) | gui | 3 |
| [gui/PoleManipulationCanvasToolWorkflow](../gui/PoleManipulationCanvasToolWorkflow.md) | gui | 3 |
| [gui/SmallCircleCanvasToolWorkflow](../gui/SmallCircleCanvasToolWorkflow.md) | gui | 2 |
| [gui/ViewCanvasToolWorkflow](../gui/ViewCanvasToolWorkflow.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/canvas-tools/CanvasToolAdapterForMap.h
python scripts/gpq.py def GPlatesCanvasTools::CanvasToolAdapterForMap --body
python scripts/gpq.py uses CanvasToolAdapterForMap --kind class
python scripts/gpq.py hier CanvasToolAdapterForMap
```
