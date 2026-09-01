# ZoomGlobe

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 1255 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/ZoomGlobe.h` | C++ | 119 |
| `src/canvas-tools/ZoomGlobe.cc` | C++ | 93 |

## Overview

[[[PROSE overview unit=canvas-tools/ZoomGlobe tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCanvasTools::ZoomGlobe`](#gplatescanvastoolszoomglobe) | class | [`GPlatesGui::GlobeCanvasTool`](../gui/GlobeCanvasTool.md) | — | 0 | This is the canvas tool used to zoom into a point on the globe by clicking. |

## Members

### `GPlatesCanvasTools::ZoomGlobe`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ZoomGlobe( GPlatesGui::Globe &globe_, GPlatesQtWidgets::GlobeCanvas &globe_canvas_, GPlatesViewOperations::RenderedGeometryCollection &rendered_geometry_collection, GPlatesQtWidgets::ViewportWindow &viewport_window_, GPlatesPresentation::ViewState &view_state_)` | constructor | `None` | public | Create a ZoomGlobe instance. |
| `handle_activation()` | method | `void` | public | — |
| `handle_deactivation()` | method | `void` | public | — |
| `handle_left_click( const GPlatesMaths::PointOnSphere &click_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_click_pos_on_globe, bool is_on_globe)` | method | `void` | public | — |
| `handle_shift_left_click( const GPlatesMaths::PointOnSphere &click_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_click_pos_on_globe, bool is_on_globe)` | method | `void` | public | — |
| `recentre_globe( const GPlatesMaths::PointOnSphere &click_pos_on_globe)` | method | `void` | private | — |
| `d_rendered_geometry_collection` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | Used to activate/deactivate focused geometry highlight rendered layer. |
| `d_viewport_window` | field | `GPlatesQtWidgets::ViewportWindow` | private | This is the View State used to pass messages to the status bar. |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | This is the view state (in the presentation tier). |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_CANVASTOOLS_ZOOMGLOBE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=canvas-tools/ZoomGlobe tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ViewCanvasToolWorkflow](../gui/ViewCanvasToolWorkflow.md) | gui | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/canvas-tools/ZoomGlobe.h
python scripts/gpq.py def GPlatesCanvasTools::ZoomGlobe --body
python scripts/gpq.py uses ZoomGlobe --kind class
python scripts/gpq.py hier ZoomGlobe
```
