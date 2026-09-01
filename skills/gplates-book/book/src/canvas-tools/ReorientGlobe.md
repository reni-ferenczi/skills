# ReorientGlobe

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 1254 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/ReorientGlobe.h` | C++ | 133 |
| `src/canvas-tools/ReorientGlobe.cc` | C++ | 123 |

## Overview

A globe canvas tool for reorienting the 3D globe view. Extends `GlobeCanvasTool` and translates mouse drag events on the globe canvas into view rotations. It supports both regular rotation (left drag) and an alternative rotation mode (shift+left drag) to provide flexible navigation of the 3D globe. It manages the rendered geometry collection to control visibility of focused geometry highlights and passes status bar feedback through the viewport window.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCanvasTools::ReorientGlobe`](#gplatescanvastoolsreorientglobe) | class | [`GPlatesGui::GlobeCanvasTool`](../gui/GlobeCanvasTool.md) | — | 0 | This is the canvas tool used to re-orient the globe by dragging. |

## Members

### `GPlatesCanvasTools::ReorientGlobe`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ReorientGlobe( GPlatesGui::Globe &globe_, GPlatesQtWidgets::GlobeCanvas &globe_canvas_, GPlatesViewOperations::RenderedGeometryCollection &rendered_geometry_collection, GPlatesQtWidgets::ViewportWindow &viewport_window_)` | constructor | `None` | public | Create a ReorientGlobe instance. |
| `handle_activation()` | method | `void` | public | — |
| `handle_deactivation()` | method | `void` | public | — |
| `handle_left_drag( const GPlatesMaths::PointOnSphere &initial_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_initial_pos_on_globe, bool was_on_globe, const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, const GPlatesMaths: ...` | method | `void` | public | — |
| `handle_left_release_after_drag( const GPlatesMaths::PointOnSphere &initial_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_initial_pos_on_globe, bool was_on_globe, const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, const ...` | method | `void` | public | — |
| `handle_shift_left_drag( const GPlatesMaths::PointOnSphere &initial_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_initial_pos_on_globe, bool was_on_globe, const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, const GPlates ...` | method | `void` | public | — |
| `handle_shift_left_release_after_drag( const GPlatesMaths::PointOnSphere &initial_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_initial_pos_on_globe, bool was_on_globe, const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, ...` | method | `void` | public | — |
| `d_rendered_geometry_collection` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | Used to activate/deactivate focused geometry highlight rendered layer. |
| `d_viewport_window_ptr` | field | `GPlatesQtWidgets::ViewportWindow` | private | This is the View State used to pass messages to the status bar. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_CANVASTOOLS_REORIENTGLOBE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ViewCanvasToolWorkflow](../gui/ViewCanvasToolWorkflow.md) | gui | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/canvas-tools/ReorientGlobe.h
python scripts/gpq.py def GPlatesCanvasTools::ReorientGlobe --body
python scripts/gpq.py uses ReorientGlobe --kind class
python scripts/gpq.py hier ReorientGlobe
```
