# CreateSmallCircle

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 343 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/CreateSmallCircle.h` | C++ | 156 |
| `src/canvas-tools/CreateSmallCircle.cc` | C++ | 178 |

## Overview

Canvas tool for drawing small circles (geographic circles of constant latitude with respect to a rotation pole) on the globe. Inherits from both `QObject` and `CanvasTool` to handle mouse events and Qt signals. Uses a two-click interface: first click marks the centre point, second click specifies a point on the radius to define the circle size. Shift-click continues from the current centre to add additional radii, building concentric circles.

The tool maintains optional centre and radius points (`d_centre`, `d_point_on_radius`), a boolean state tracking whether a circle is mid-draw, and a collection of completed `SmallCircle` objects held by the associated widget. It renders circles through a `RenderedGeometryLayer` and responds to the widget's clear signal via Qt slot.

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

The `d_circle_is_being_drawn` boolean tracks a two-state drawing machine: the first click sets `d_centre`, the second click sets `d_point_on_radius` and completes the circle. On completion, the circle is appended to the collection held by the widget (via `d_small_circle_collection_ref`), not owned by the tool itself. Clearing the collection resets the state without clearing the current work-in-progress circle.

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
