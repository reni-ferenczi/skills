# AdjustFittedPoleEstimate

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 50 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/AdjustFittedPoleEstimate.h` | C++ | 406 |
| `src/canvas-tools/AdjustFittedPoleEstimate.cc` | C++ | 878 |

## Overview

[[[PROSE overview unit=canvas-tools/AdjustFittedPoleEstimate tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCanvasTools::AdjustFittedPoleEstimate`](#gplatescanvastoolsadjustfittedpoleestimate) | class | `QObject`<br>[`CanvasTool`](CanvasTool.md) | — | 0 | Canvas tool used for adjusting the initial pole estimates for the hellinger tool. |

## Members

### `GPlatesCanvasTools::AdjustFittedPoleEstimate`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ActivePoleType` | enum | `None` | public | — |
| `GeometryFinder` | class | `None` | public | Visitor to find a rendered geometry's underlying geometry-on-sphere, if it has one. |
| `child_layer_ptr_type` | typedef | `GPlatesViewOperations::RenderedGeometryCollection::child_layer_owner_ptr_type` | public | Convenience typedef for GPlatesViewOperations::RenderedGeometryCollection::child\_layer\_owner\_ptr\_type |
| `create( const status_bar_callback_type &status_bar_callback, GPlatesViewOperations::RenderedGeometryCollection &rendered_geom_collection, GPlatesViewOperations::RenderedGeometryCollection::MainLayerType main_rendered_layer_type, GPlatesQtWidgets::HellingerDialog &hellinger_dialog)` | method | `non_null_ptr_type` | public | — |
| `handle_activation()` | method | `void` | public | — |
| `handle_deactivation()` | method | `void` | public | — |
| `handle_move_without_drag( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `handle_left_drag( const GPlatesMaths::PointOnSphere &initial_point_on_sphere, bool was_on_earth, double initial_proximity_inclusion_threshold, const GPlatesMaths::PointOnSphere &current_point_on_sphere, bool is_on_earth, double current_proximity_inclusion_threshold, const boost::optional<GPlatesMaths::PointOnSphere> &c ...` | method | `void` | public | — |
| `handle_left_release_after_drag( const GPlatesMaths::PointOnSphere &initial_point_on_sphere, bool was_on_earth, double initial_proximity_inclusion_threshold, const GPlatesMaths::PointOnSphere &current_point_on_sphere, bool is_on_earth, double current_proximity_inclusion_threshold, const boost::optional<GPlatesMaths::Poi ...` | method | `void` | public | — |
| `handle_left_press( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `handle_pole_estimate_12_lat_lon_changed( double lat, double lon)` | method | `void` | private | — |
| `handle_pole_estimate_12_angle_changed( double angle)` | method | `void` | private | — |
| `handle_pole_estimate_13_lat_lon_changed( double lat, double lon)` | method | `void` | private | — |
| `handle_pole_estimate_13_angle_changed( double angle)` | method | `void` | private | — |
| `GeometryTypeIndex` | enum | `None` | private | This enum is used in keeping track of which geometry in the pole\_estimate\_layer we're hovered over. |
| `update_local_values_from_hellinger_dialog()` | method | `void` | private | — |
| `update_hellinger_dialog_from_local_values()` | method | `void` | private | — |
| `update_current_pole_arrow_layer()` | method | `void` | private | — |
| `update_current_pole_and_angle_layer()` | method | `void` | private | — |
| `update_pole_estimate_and_arc_highlight( const GPlatesMaths::PointOnSphere &pole, const GPlatesMaths::PointOnSphere &reference_arc_end_point, const GPlatesMaths::PointOnSphere &relative_arc_end_point)` | method | `void` | private | — |
| `update_arc_and_end_point_highlight( const GPlatesMaths::PointOnSphere &end_point, const GPlatesMaths::PointOnSphere &pole)` | method | `void` | private | — |
| `update_angle()` | method | `void` | private | — |
| `paint()` | method | `void` | private | — |
| `mouse_is_over_a_highlight_geometry()` | method | `bool` | private | — |
| `AdjustFittedPoleEstimate( const status_bar_callback_type &status_bar_callback, GPlatesViewOperations::RenderedGeometryCollection &rendered_geom_collection, GPlatesViewOperations::RenderedGeometryCollection::MainLayerType main_rendered_layer_type, GPlatesQtWidgets::HellingerDialog &hellinger_dialog)` | constructor | `None` | private | — |
| `d_rendered_geom_collection_ptr` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | For rendering purposes |
| `d_hellinger_dialog_ptr` | field | `GPlatesQtWidgets::HellingerDialog` | private | — |
| `d_mouse_is_over_pole_estimate` | field | `bool` | private | — |
| `d_pole_is_being_dragged` | field | `bool` | private | — |
| `d_mouse_is_over_reference_arc` | field | `bool` | private | — |
| `d_reference_arc_is_being_draggged` | field | `bool` | private | — |
| `d_mouse_is_over_reference_arc_end_point` | field | `bool` | private | — |
| `d_reference_arc_end_point_is_being_dragged` | field | `bool` | private | — |
| `d_mouse_is_over_relative_arc` | field | `bool` | private | — |
| `d_relative_arc_is_being_dragged` | field | `bool` | private | — |
| `d_mouse_is_over_relative_arc_end_point` | field | `bool` | private | — |
| `d_relative_arc_end_point_is_being_dragged` | field | `bool` | private | — |
| `d_current_pole_arrow_layer_ptr` | field | `child_layer_ptr_type` | private | d\_pole\_arrow\_layer\_ptr layer for drawing the current pole arrow |
| `d_current_pole_and_angle_layer_ptr` | field | `child_layer_ptr_type` | private | d\_current\_pole\_and\_angle\_layer\_ptr layer for drawing the vertices arcs of the current pole and angle |
| `d_highlight_layer_ptr` | field | `child_layer_ptr_type` | private | d\_highlight\_layer\_ptr layer for highlighting whichever geometry (pole, reference-arc,or relative-arc) is hovered over and hence draggable / adjustable. |
| `d_current_pole_12` | field | `GPlatesMaths::PointOnSphere` | private | Coordinates, angles etc of geometries related to the initial pole estimates. "12" denotes variables associated with the pole representing the rotation between plate indices 1 and 2 "13" denotes those related to plate indices 1 and 3. |
| `d_current_angle_12` | field | `double` | private | — |
| `d_end_point_of_reference_arc_12` | field | `GPlatesMaths::PointOnSphere` | private | — |
| `d_end_point_of_relative_arc_12` | field | `GPlatesMaths::PointOnSphere` | private | — |
| `d_current_pole_13` | field | `GPlatesMaths::PointOnSphere` | private | — |
| `d_current_angle_13` | field | `double` | private | — |
| `d_end_point_of_reference_arc_13` | field | `GPlatesMaths::PointOnSphere` | private | — |
| `d_end_point_of_relative_arc_13` | field | `GPlatesMaths::PointOnSphere` | private | — |
| `d_has_been_activated` | field | `bool` | private | — |
| `d_active_pole_type` | field | `ActivePoleType` | private | d\_active\_pole\_type - the pole type which is currently or most recently selected/highlighted/dragged. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `VERTEX_COLOUR_POLE_12` | variable | `GPlatesGui::Colour` | — |
| `ARC_COLOUR_POLE_12` | variable | `GPlatesGui::Colour` | — |
| `VERTEX_COLOUR_POLE_13` | variable | `GPlatesGui::Colour` | — |
| `ARC_COLOUR_POLE_13` | variable | `GPlatesGui::Colour` | — |
| `VERTEX_HIGHLIGHT_COLOUR` | variable | `GPlatesGui::Colour` | We can use the same highlight colour - only one pole will be selected at any one time. |
| `POLE_SYMBOL` | variable | `GPlatesGui::Symbol` | — |
| `END_POINT_SYMBOL` | variable | `GPlatesGui::Symbol` | — |
| `POLE_HIGHLIGHT_SYMBOL` | variable | `GPlatesGui::Symbol` | — |
| `END_POINT_HIGHLIGHT_SYMBOL` | variable | `GPlatesGui::Symbol` | — |
| `INITIAL_ANGLE` | variable | `double` | — |
| `proximity_hit_index_compare( const GPlatesViewOperations::RenderedGeometryProximityHit &lhs, const GPlatesViewOperations::RenderedGeometryProximityHit &rhs)` | function | `bool` | Compare based on hit index. |
| `sort_proximity_by_index( GPlatesViewOperations::sorted_rendered_geometry_proximity_hits_type &sorted_proximity_seq)` | function | `void` | Sorts proximity hits by index. |
| `generate_new_relative_end_point( const GPlatesMaths::PointOnSphere &pole, const GPlatesMaths::PointOnSphere &reference_end_point, GPlatesMaths::PointOnSphere &relative_end_point, const double &angle)` | function | `void` | generate\_new\_relative\_end\_point The value of |
| `update_pole_and_angle_geometries( GPlatesCanvasTools::AdjustFittedPoleEstimate::child_layer_ptr_type &layer, const GPlatesMaths::PointOnSphere &pole, const GPlatesMaths::PointOnSphere &reference_arc_end_point, const GPlatesMaths::PointOnSphere &relative_arc_end_point)` | function | `void` | — |
| `GPLATES_CANVASTOOLS_ADJUSTFITTEDPOLEESTIMATE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=canvas-tools/AdjustFittedPoleEstimate tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/HellingerCanvasToolWorkflow](../gui/HellingerCanvasToolWorkflow.md) | gui | 19 |

## Related

**Qt signal/slot connections** (4 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_hellinger_dialog_ptr` | `pole_estimate_12_lat_lon_changed(double,double)` | `this` | `handle_pole_estimate_12_lat_lon_changed(double,double)` |
| `d_hellinger_dialog_ptr` | `pole_estimate_12_angle_changed(double)` | `this` | `handle_pole_estimate_12_angle_changed(double)` |
| `d_hellinger_dialog_ptr` | `pole_estimate_13_lat_lon_changed(double,double)` | `this` | `handle_pole_estimate_13_lat_lon_changed(double,double)` |
| `d_hellinger_dialog_ptr` | `pole_estimate_13_angle_changed(double)` | `this` | `handle_pole_estimate_13_angle_changed(double)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/canvas-tools/AdjustFittedPoleEstimate.h
python scripts/gpq.py def GPlatesCanvasTools::AdjustFittedPoleEstimate --body
python scripts/gpq.py uses AdjustFittedPoleEstimate --kind class
python scripts/gpq.py hier AdjustFittedPoleEstimate
```
