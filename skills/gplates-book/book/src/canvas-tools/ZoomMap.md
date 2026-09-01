# ZoomMap

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 578 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/ZoomMap.h` | C++ | 115 |
| `src/canvas-tools/ZoomMap.cc` | C++ | 105 |

## Overview

A map canvas tool for zooming into the map view. Extends `MapCanvasTool` and responds to left clicks (zoom in) and shift+left clicks (zoom out) to adjust zoom level and reorient the map. It recenters the map on the clicked point using a private `recentre_map()` method and coordinates zoom through `ViewportZoom`. Manages the rendered geometry collection and provides status bar feedback through the viewport window.

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
python scripts/gpq.py file src/canvas-tools/ZoomMap.h
python scripts/gpq.py def GPlatesCanvasTools::ZoomMap --body
python scripts/gpq.py uses ZoomMap --kind class
python scripts/gpq.py hier ZoomMap
```
