# ChangeLightDirectionGlobe

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 983 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/ChangeLightDirectionGlobe.h` | C++ | 175 |
| `src/canvas-tools/ChangeLightDirectionGlobe.cc` | C++ | 285 |

## Overview

`ChangeLightDirectionGlobe` is the globe canvas tool for dragging the rendered light-direction arrow to change how lit rasters and other shaded layers are illuminated. Almost all of its own logic is delegated to `GPlatesViewOperations::ChangeLightDirectionOperation`: `handle_left_drag()` calls `start_drag()`/`update_drag()` on it (tracked by `d_is_in_drag` so the drag is only started once), `handle_left_release_after_drag()` calls `end_drag()`, and every non-drag mouse move forwards to `mouse_move()` so the operation can update hover highlighting.

The plain left-drag handlers move the light direction; the `ctrl_left_drag`/`shift_ctrl_left_drag` handlers (and their `_release_after_drag` counterparts) instead delegate to `GlobeCanvasTool`'s base-class reorientation handling to spin the globe, then call `d_change_light_direction_operation.mouse_move()` afterwards to keep the light-direction arrow correctly positioned when it is attached to the view frame rather than to the globe, since reorienting the view would otherwise leave it stale.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCanvasTools::ChangeLightDirectionGlobe`](#gplatescanvastoolschangelightdirectionglobe) | class | [`GPlatesGui::GlobeCanvasTool`](../gui/GlobeCanvasTool.md) | — | 0 | This is the canvas tool used to change the light direction by dragging a radial arrow (light direction). |

## Members

### `GPlatesCanvasTools::ChangeLightDirectionGlobe`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ChangeLightDirectionGlobe( GPlatesGui::Globe &globe_, GPlatesQtWidgets::GlobeCanvas &globe_canvas_, GPlatesViewOperations::RenderedGeometryCollection &rendered_geometry_collection, GPlatesViewOperations::RenderedGeometryCollection::MainLayerType main_rendered_layer_type, GPlatesQtWidgets::ViewportWindow &viewport_windo ...` | constructor | `None` | public | Create a ChangeLightDirectionGlobe instance. |
| `handle_activation()` | method | `void` | public | — |
| `handle_deactivation()` | method | `void` | public | — |
| `handle_left_drag( const GPlatesMaths::PointOnSphere &initial_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_initial_pos_on_globe, bool was_on_globe, const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, const GPlatesMaths: ...` | method | `void` | public | — |
| `handle_left_release_after_drag( const GPlatesMaths::PointOnSphere &initial_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_initial_pos_on_globe, bool was_on_globe, const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, const ...` | method | `void` | public | — |
| `handle_ctrl_left_drag( const GPlatesMaths::PointOnSphere &initial_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_initial_pos_on_globe, bool was_on_globe, const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, const GPlatesM ...` | method | `void` | public | — |
| `handle_ctrl_left_release_after_drag( const GPlatesMaths::PointOnSphere &initial_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_initial_pos_on_globe, bool was_on_globe, const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, ...` | method | `void` | public | — |
| `handle_shift_ctrl_left_drag( const GPlatesMaths::PointOnSphere &initial_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_initial_pos_on_globe, bool was_on_globe, const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, const GP ...` | method | `void` | public | — |
| `handle_shift_ctrl_left_release_after_drag( const GPlatesMaths::PointOnSphere &initial_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_initial_pos_on_globe, bool was_on_globe, const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_g ...` | method | `void` | public | — |
| `handle_move_without_drag( const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, const GPlatesMaths::PointOnSphere &oriented_centre_of_viewport)` | method | `void` | public | — |
| `d_viewport_window` | field | `GPlatesQtWidgets::ViewportWindow` | private | This is the View State used to pass messages to the status bar. |
| `d_change_light_direction_operation` | field | `GPlatesViewOperations::ChangeLightDirectionOperation` | private | Handles changes to the light direction for us. |
| `d_is_in_drag` | field | `bool` | private | Whether or not this tool is currently in the midst of a drag. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_CANVAS_TOOLS_CHANGELIGHTINGGLOBE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ViewCanvasToolWorkflow](../gui/ViewCanvasToolWorkflow.md) | gui | 12 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/canvas-tools/ChangeLightDirectionGlobe.h
python scripts/gpq.py def GPlatesCanvasTools::ChangeLightDirectionGlobe --body
python scripts/gpq.py uses ChangeLightDirectionGlobe --kind class
python scripts/gpq.py hier ChangeLightDirectionGlobe
```
