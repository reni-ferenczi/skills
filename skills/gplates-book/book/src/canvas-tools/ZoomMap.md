# ZoomMap

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 578 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/ZoomMap.h` | C++ | 115 |
| `src/canvas-tools/ZoomMap.cc` | C++ | 105 |

## Overview

[[[PROSE overview unit=canvas-tools/ZoomMap tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCanvasTools::ZoomMap`](#gplatescanvastoolszoommap) | class | [`GPlatesGui::MapCanvasTool`](../gui/MapCanvasTool.md) | — | 0 | This is the canvas tool used to re-orient the globe by dragging. |

## Members

### `GPlatesCanvasTools::ZoomMap`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ZoomMap( GPlatesQtWidgets::MapCanvas &map_canvas_, GPlatesQtWidgets::MapView &map_view_, GPlatesViewOperations::RenderedGeometryCollection &rendered_geometry_collection, GPlatesQtWidgets::ViewportWindow &viewport_window_, GPlatesGui::MapTransform &map_transform_, GPlatesGui::ViewportZoom &viewport_zoom_)` | constructor | `None` | public | Create a PanMap instance. |
| `handle_activation()` | method | `void` | public | — |
| `handle_deactivation()` | method | `void` | public | — |
| `handle_left_click( const QPointF &point_on_scene, bool is_on_surface)` | method | `void` | public | — |
| `handle_shift_left_click( const QPointF &point_on_scene, bool is_on_surface)` | method | `void` | public | — |
| `recentre_map( const QPointF &point_on_scene)` | method | `void` | private | — |
| `d_rendered_geometry_collection` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | Used to activate/deactivate focused geometry highlight rendered layer. |
| `d_viewport_window_ptr` | field | `GPlatesQtWidgets::ViewportWindow` | private | This is the window that has the status bar. |
| `d_map_transform_ptr` | field | `GPlatesGui::MapTransform` | private | — |
| `d_viewport_zoom_ptr` | field | `GPlatesGui::ViewportZoom` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_CANVASTOOLS_ZOOMMAP_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=canvas-tools/ZoomMap tier=3]]]
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
python scripts/gpq.py file src/canvas-tools/ZoomMap.h
python scripts/gpq.py def GPlatesCanvasTools::ZoomMap --body
python scripts/gpq.py uses ZoomMap --kind class
python scripts/gpq.py hier ZoomMap
```
