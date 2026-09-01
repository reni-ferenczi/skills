# SelectHellingerGeometries

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 302 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/SelectHellingerGeometries.h` | C++ | 286 |
| `src/canvas-tools/SelectHellingerGeometries.cc` | C++ | 398 |

## Overview

A canvas tool for selecting and manipulating geometries to fit a rotation pole (Hellinger pole fitting). Extends both `QObject` and `CanvasTool` to integrate Qt's signal/slot mechanism with globe interaction. It contains an inner `GeometryFinder` visitor class that extracts `PointOnSphere` coordinates from various rendered geometry types (point, multipoint, and symbol geometries like circles, crosses, squares, and triangles). The tool tracks detailed mouse interaction state (editable pick hover, selectable pick hover, drag state) and communicates with `HellingerDialog` via Qt signals to coordinate pole fitting workflows.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCanvasTools::SelectHellingerGeometries`](#gplatescanvastoolsselecthellingergeometries) | class | `QObject`<br>[`CanvasTool`](CanvasTool.md) | — | 0 | Canvas tool used for fitting points to a rotation pole. |

## Members

### `GPlatesCanvasTools::SelectHellingerGeometries`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GeometryFinder` | class | `None` | public | Visitor to find a rendered geometry's point-on-sphere, if it has one. |
| `create( const status_bar_callback_type &status_bar_callback, GPlatesViewOperations::RenderedGeometryCollection &rendered_geom_collection, GPlatesViewOperations::RenderedGeometryCollection::MainLayerType main_rendered_layer_type, GPlatesQtWidgets::HellingerDialog &hellinger_dialog)` | method | `non_null_ptr_type` | public | — |
| `handle_activation()` | method | `void` | public | — |
| `handle_deactivation()` | method | `void` | public | — |
| `handle_left_click( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `handle_move_without_drag( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `handle_shift_left_click( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `handle_left_drag( const GPlatesMaths::PointOnSphere &initial_point_on_sphere, bool was_on_earth, double initial_proximity_inclusion_threshold, const GPlatesMaths::PointOnSphere &current_point_on_sphere, bool is_on_earth, double current_proximity_inclusion_threshold, const boost::optional<GPlatesMaths::PointOnSphere> &c ...` | method | `void` | public | — |
| `handle_left_release_after_drag( const GPlatesMaths::PointOnSphere &initial_point_on_sphere, bool was_on_earth, double initial_proximity_inclusion_threshold, const GPlatesMaths::PointOnSphere &current_point_on_sphere, bool is_on_earth, double current_proximity_inclusion_threshold, const boost::optional<GPlatesMaths::Poi ...` | method | `void` | public | — |
| `handle_left_press( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `handle_shift_left_drag( const GPlatesMaths::PointOnSphere &initial_point_on_sphere, bool was_on_earth, double initial_proximity_inclusion_threshold, const GPlatesMaths::PointOnSphere &current_point_on_sphere, bool is_on_earth, double current_proximity_inclusion_threshold, const boost::optional<GPlatesMaths::PointOnSphe ...` | method | `void` | public | — |
| `set_default_tool_status_message()` | method | `void` | private | — |
| `paint()` | method | `void` | private | — |
| `set_up_connections()` | method | `void` | private | — |
| `handle_finished_editing()` | method | `void` | private | — |
| `handle_begin_editing()` | method | `void` | private | — |
| `handle_begin_new_pick()` | method | `void` | private | — |
| `SelectHellingerGeometries( const status_bar_callback_type &status_bar_callback, GPlatesViewOperations::RenderedGeometryCollection &rendered_geom_collection, GPlatesViewOperations::RenderedGeometryCollection::MainLayerType main_rendered_layer_type, GPlatesQtWidgets::HellingerDialog &hellinger_dialog)` | constructor | `None` | private | — |
| `d_rendered_geom_collection_ptr` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | For rendering purposes |
| `d_hellinger_dialog_ptr` | field | `GPlatesQtWidgets::HellingerDialog` | private | — |
| `d_mouse_is_over_editable_pick` | field | `bool` | private | — |
| `d_mouse_is_over_selectable_pick` | field | `bool` | private | — |
| `d_pick_is_being_dragged` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_CANVASTOOLS_SELECTHELLINGERGEOMETRIES_H` | macro | `None` | — |

## Notes

The tool is tightly coupled to `HellingerDialog` via Qt signals; changes to signal names (`finished_editing`, `begin_new_pick`, `begin_edit_pick`) or their emission points affect tool behavior. State tracking relies on boolean flags that must be coordinated across mouse events and dialog callbacks.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/HellingerCanvasToolWorkflow](../gui/HellingerCanvasToolWorkflow.md) | gui | 2 |

## Related

**Qt signal/slot connections** (3 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_hellinger_dialog_ptr` | `finished_editing()` | `this` | `handle_finished_editing()` |
| `d_hellinger_dialog_ptr` | `begin_new_pick()` | `this` | `handle_begin_new_pick()` |
| `d_hellinger_dialog_ptr` | `begin_edit_pick()` | `this` | `handle_begin_editing()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/canvas-tools/SelectHellingerGeometries.h
python scripts/gpq.py def GPlatesCanvasTools::SelectHellingerGeometries --body
python scripts/gpq.py uses SelectHellingerGeometries --kind class
python scripts/gpq.py hier SelectHellingerGeometries
```
