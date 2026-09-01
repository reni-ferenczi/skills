# PanMap

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 1253 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/PanMap.h` | C++ | 118 |
| `src/canvas-tools/PanMap.cc` | C++ | 83 |

## Overview

[[[PROSE overview unit=canvas-tools/PanMap tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCanvasTools::PanMap`](#gplatescanvastoolspanmap) | class | [`GPlatesGui::MapCanvasTool`](../gui/MapCanvasTool.md) | — | 0 | This is the canvas tool used to re-orient the globe by dragging. |

## Members

### `GPlatesCanvasTools::PanMap`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PanMap( GPlatesQtWidgets::MapCanvas &map_canvas_, GPlatesQtWidgets::MapView &map_view_, GPlatesViewOperations::RenderedGeometryCollection &rendered_geometry_collection, GPlatesQtWidgets::ViewportWindow &view_state_, GPlatesGui::MapTransform &map_transform_)` | constructor | `None` | public | Create a PanMap instance. |
| `handle_activation()` | method | `void` | public | — |
| `handle_deactivation()` | method | `void` | public | — |
| `handle_left_drag( const QPointF &initial_point_on_scene, bool was_on_surface, const QPointF &current_point_on_scene, bool is_on_surface, const QPointF &translation )` | method | `void` | public | — |
| `handle_shift_left_drag( const QPointF &initial_point_on_scene, bool was_on_surface, const QPointF &current_point_on_scene, bool is_on_surface, const QPointF &translation)` | method | `void` | public | — |
| `d_rendered_geometry_collection` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | Used to activate/deactivate focused geometry highlight rendered layer. |
| `d_view_state_ptr` | field | `GPlatesQtWidgets::ViewportWindow` | private | This is the View State used to pass messages to the status bar. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_CANVASTOOLS_PANMAP_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=canvas-tools/PanMap tier=3]]]
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
python scripts/gpq.py file src/canvas-tools/PanMap.h
python scripts/gpq.py def GPlatesCanvasTools::PanMap --body
python scripts/gpq.py uses PanMap --kind class
python scripts/gpq.py hier PanMap
```
