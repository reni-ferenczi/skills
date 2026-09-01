# CreateSmallCircle

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 343 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/CreateSmallCircle.h` | C++ | 156 |
| `src/canvas-tools/CreateSmallCircle.cc` | C++ | 178 |

## Overview

[[[PROSE overview unit=canvas-tools/CreateSmallCircle tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCanvasTools::CreateSmallCircle`](#gplatescanvastoolscreatesmallcircle) | class | `QObject`<br>[`CanvasTool`](CanvasTool.md) | — | 0 | Canvas tool used to measuring distances on the globe and map |

## Members

### `GPlatesCanvasTools::CreateSmallCircle`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( const status_bar_callback_type &status_bar_callback, GPlatesViewOperations::RenderedGeometryCollection &rendered_geom_collection, GPlatesViewOperations::RenderedGeometryCollection::MainLayerType main_rendered_layer_type, GPlatesQtWidgets::SmallCircleWidget &small_circle_widget)` | method | `non_null_ptr_type` | public | — |
| `handle_activation()` | method | `void` | public | — |
| `handle_deactivation()` | method | `void` | public | — |
| `handle_left_click( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `handle_move_without_drag( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `handle_shift_left_click( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | We'll use shift-left-click to continue drawing an additional circle after closing the current circle, so that we can build up multiple concentric circles in the same operation. |
| `handle_clear_geometries()` | method | `void` | private | Respond to the widget's clear signal. |
| `paint()` | method | `void` | private | — |
| `CreateSmallCircle( const status_bar_callback_type &status_bar_callback, GPlatesViewOperations::RenderedGeometryCollection &rendered_geom_collection, GPlatesViewOperations::RenderedGeometryCollection::MainLayerType main_rendered_layer_type, GPlatesQtWidgets::SmallCircleWidget &small_circle_widget)` | constructor | `None` | private | — |
| `d_rendered_geom_collection_ptr` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | For rendering purposes |
| `d_small_circle_layer_ptr` | field | `GPlatesViewOperations::RenderedGeometryLayer` | private | Small circle layer |
| `d_centre` | field | `boost::optional<GPlatesMaths::PointOnSphere>` | private | — |
| `d_point_on_radius` | field | `boost::optional<GPlatesMaths::PointOnSphere>` | private | — |
| `d_small_circle_widget_ptr` | field | `GPlatesQtWidgets::SmallCircleWidget` | private | — |
| `d_small_circle_collection_ref` | field | `GPlatesQtWidgets::SmallCircleWidget::small_circle_collection_type` | private | — |
| `d_circle_is_being_drawn` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_CANVASTOOLS_CREATESMALLCIRCLE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=canvas-tools/CreateSmallCircle tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/SmallCircleCanvasToolWorkflow](../gui/SmallCircleCanvasToolWorkflow.md) | gui | 4 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_small_circle_widget_ptr` | `clear_geometries()` | `this` | `handle_clear_geometries()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/canvas-tools/CreateSmallCircle.h
python scripts/gpq.py def GPlatesCanvasTools::CreateSmallCircle --body
python scripts/gpq.py uses CreateSmallCircle --kind class
python scripts/gpq.py hier CreateSmallCircle
```
