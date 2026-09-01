# ChangeLightDirectionMap

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 1084 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/ChangeLightDirectionMap.h` | C++ | 88 |
| `src/canvas-tools/ChangeLightDirectionMap.cc` | C++ | 44 |

## Overview

A `MapCanvasTool` that will allow interactive manipulation of lighting direction on the map view. It stores references to the `RenderedGeometryCollection` for highlighting, the `ViewportWindow` for status messages, and the `MapTransform` for coordinate conversion. Currently unimplemented; changing light direction in 2D map views has not yet been built out.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCanvasTools::ChangeLightDirectionMap`](#gplatescanvastoolschangelightdirectionmap) | class | [`GPlatesGui::MapCanvasTool`](../gui/MapCanvasTool.md) | — | 0 | This is the canvas tool used to change the light direction. |

## Members

### `GPlatesCanvasTools::ChangeLightDirectionMap`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ChangeLightDirectionMap( GPlatesQtWidgets::MapCanvas &map_canvas_, GPlatesQtWidgets::MapView &map_view_, GPlatesViewOperations::RenderedGeometryCollection &rendered_geometry_collection, GPlatesQtWidgets::ViewportWindow &viewport_window_, GPlatesGui::MapTransform &map_transform_)` | constructor | `None` | public | Create a ChangeLightDirectionMap instance. |
| `d_rendered_geometry_collection` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | Used to activate/deactivate focused geometry highlight rendered layer. |
| `d_viewport_window_ptr` | field | `GPlatesQtWidgets::ViewportWindow` | private | This is the window that has the status bar. |
| `d_map_transform_ptr` | field | `GPlatesGui::MapTransform` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_CANVAS_TOOLS_CHANGELIGHTINGMAP_H` | macro | `None` | — |

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
python scripts/gpq.py file src/canvas-tools/ChangeLightDirectionMap.h
python scripts/gpq.py def GPlatesCanvasTools::ChangeLightDirectionMap --body
python scripts/gpq.py uses ChangeLightDirectionMap --kind class
python scripts/gpq.py hier ChangeLightDirectionMap
```
