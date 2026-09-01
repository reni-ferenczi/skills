# MeasureDistanceState

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 402 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/MeasureDistanceState.h` | C++ | 287 |
| `src/canvas-tools/MeasureDistanceState.cc` | C++ | 437 |

## Overview

`MeasureDistanceState` holds all the data behind the Measure Distance canvas tool, decoupled from rendering so the globe and map views (each with their own `MeasureDistance` instance) share one measurement session. It tracks two independent measurements: the "Quick Measure" pair of arbitrary clicked points (`d_quick_measure_start`/`d_quick_measure_end`), and the "Feature Measure" total length and area of whichever geometry is currently being digitised or is the focused feature's geometry.

The Feature Measure side follows the active `GPlatesViewOperations::GeometryBuilder` rather than owning geometry itself: `GeometryOperationState` broadcasts `switched_geometry_builder` whenever the tool workflow changes which builder is in use, and `MeasureDistanceState` reconnects its `stopped_updating_geometry_excluding_intermediate_moves` listener to the new builder each time (`switch_geometry_builder`, `make_signal_slot_connections_for_geometry_builder`). Whenever the geometry changes, `process_geometry_builder` walks the current geometry's points, summing great-circle distances between consecutive points with `calculate_distance_on_surface_of_sphere`, and — for polygons — computes an area via the anonymous `PolygonAreaVisitor`, which visits the geometry and scales `PolygonOnSphere::get_area()` by the earth radius squared. Distances and areas use the state's own `real_t` (`d_radius`, default `DEFAULT_RADIUS_OF_EARTH`), so changing the radius with `set_radius()` re-derives both measurements without needing a new geometry pass. All updates are exposed as Qt signals (`quick_measure_updated`, `feature_measure_updated`, highlight-changed signals) that the TaskPanel widgets and canvas tools listen to, rather than being polled.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::PolygonAreaVisitor`](#anonymouspolygonareavisitor) | class | [`GPlatesMaths::ConstGeometryOnSphereVisitor`](../maths/ConstGeometryOnSphereVisitor.md) | — | 0 | — |
| [`GPlatesCanvasTools::MeasureDistanceState`](#gplatescanvastoolsmeasuredistancestate) | class | `QObject` | — | 0 | Stores the state for the distance measuring tool, shared between globe and map. |

## Members

### `(anonymous)::PolygonAreaVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PolygonAreaVisitor( double radius)` | constructor | `None` | public | — |
| `visit_polygon_on_sphere( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere)` | method | `void` | public | — |
| `d_radius` | field | `double` | private | — |
| `d_area` | field | `boost::optional<double>` | private | — |

### `GPlatesCanvasTools::MeasureDistanceState`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `real_t` | typedef | `GPlatesMaths::Real` | private | — |
| `child_layer_ptr_type` | typedef | `GPlatesViewOperations::RenderedGeometryCollection::child_layer_owner_ptr_type` | private | — |
| `MeasureDistanceState( GPlatesViewOperations::RenderedGeometryCollection &rendered_geom_collection, GPlatesCanvasTools::GeometryOperationState &geometry_operation_state)` | constructor | `None` | public | Constructor |
| `quick_measure_add_point( const GPlatesMaths::PointOnSphere &point)` | method | `void` | public | Add a new point for the Quick Measure tool |
| `clear_quick_measure()` | method | `void` | public | Removes all points added to the Quick Measure tool |
| `get_quick_measure_distance()` | method | `boost::optional<double>` | public | Get the distance between the two Quick Measure points, if there are two such points |
| `set_feature_segment_points( const boost::optional<GPlatesMaths::PointOnSphere> &start, const boost::optional<GPlatesMaths::PointOnSphere> &end)` | method | `void` | public | Set the start and end points for the Feature Measure tool |
| `get_feature_segment_distance()` | method | `boost::optional<double>` | public | Get the distance between the two Feature Measure points, if there are two such points |
| `set_radius(real_t radius)` | method | `void` | public | Sets the radius of the earth and emits updated() if the new radius is different from the old radius |
| `get_radius()` | method | `real_t` | public | Gets the radius of the earth used by the measure distance tool |
| `handle_activation()` | method | `void` | public | Call this when the Measure Distance tool is activated |
| `handle_deactivation()` | method | `void` | public | Call this when the Measure Distance tool is deactivated |
| `is_active()` | method | `bool` | public | Returns whether the Measure Distance canvas tool is active or not |
| `get_current_geometry_builder_ptr()` | method | `GPlatesViewOperations::GeometryBuilder` | public | Returns pointer to current geometry builder; NULL if none |
| `set_quick_measure_highlight( bool is_highlighted)` | method | `void` | public | — |
| `set_feature_measure_highlight( bool is_highlighted)` | method | `void` | public | — |
| `d_radius` | field | `real_t` | private | The radius of the earth in kilometres |
| `d_quick_measure_start` | field | `boost::optional<GPlatesMaths::PointOnSphere>` | private | Quick measure tool start point |
| `d_quick_measure_end` | field | `boost::optional<GPlatesMaths::PointOnSphere>` | private | Quick measure tool end point |
| `d_geometry_operation_state_ptr` | field | `GPlatesCanvasTools::GeometryOperationState` | private | Determines which GeometryBuilder to get points from |
| `d_current_geometry_builder_ptr` | field | `GPlatesViewOperations::GeometryBuilder` | private | The current geometry builder |
| `d_feature_total_distance` | field | `boost::optional<double>` | private | The calculated total distance for Feature Measure tool; boost::none if no feature |
| `d_feature_area` | field | `boost::optional<double>` | private | The area of the selected polygon; boost::none if no polygon selected |
| `d_feature_segment_start` | field | `boost::optional<GPlatesMaths::PointOnSphere>` | private | The start point of the feature segment that is highlighted |
| `d_feature_segment_end` | field | `boost::optional<GPlatesMaths::PointOnSphere>` | private | The end point of the feature segment that is highlighted |
| `d_is_active` | field | `bool` | private | Whether the Measure Distance canvas tool is currently active |
| `d_is_quick_measure_highlighted` | field | `bool` | private | Whether the Quick Measure distance field in the TaskPanel is highlighted |
| `d_is_feature_measure_highlighted` | field | `bool` | private | Whether the Feature Measure segment distance field in the TaskPanel is highlighted |
| `DEFAULT_RADIUS_OF_EARTH` | field | `double` | private | The default radius value |
| `make_signal_slot_connections_for_geometry_operation_state()` | method | `void` | private | — |
| `make_signal_slot_connections_for_geometry_builder()` | method | `void` | private | — |
| `disconnect_signal_slot_connections_for_geometry_builder()` | method | `void` | private | — |
| `emit_quick_measure_updated()` | method | `void` | private | — |
| `emit_feature_measure_updated()` | method | `void` | private | — |
| `process_geometry_builder( const GPlatesViewOperations::GeometryBuilder *geometry_builder)` | method | `void` | private | — |
| `switch_geometry_builder( GPlatesViewOperations::GeometryBuilder *)` | method | `void` | private | — |
| `reexamine_geometry_builder()` | method | `void` | private | — |
| `quick_measure_cleared()` | method | `void` | public | Emitted when the Quick Measure state is cleared |
| `quick_measure_updated( boost::optional<GPlatesMaths::PointOnSphere> start, boost::optional<GPlatesMaths::PointOnSphere> end, boost::optional<double> distance)` | method | `void` | public | Emitted when the Quick Measure state is changed |
| `feature_measure_updated( double total_distance, boost::optional<double> area, boost::optional<GPlatesMaths::PointOnSphere> segment_start, boost::optional<GPlatesMaths::PointOnSphere> segment_end, boost::optional<double> segment_distance)` | method | `void` | public | Emitted when New/Selected Measure state is changed (and there is a feature) |
| `feature_measure_updated()` | method | `void` | public | Emitted when New/Selected Measure state is changed (and there is NO feature) |
| `feature_in_geometry_builder_changed()` | method | `void` | public | Emitted when the canvas tool needs to redraw the displayed feature |
| `quick_measure_highlight_changed( bool is_highlighted)` | method | `void` | public | Emitted when the Quick Measure distance field highlight is changed |
| `feature_measure_highlight_changed( bool is_highlighted)` | method | `void` | public | Emitted when the Feature Measure segment distance field highlight is changed |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `calculate_distance_between_optional_points( boost::optional<GPlatesMaths::PointOnSphere> start, boost::optional<GPlatesMaths::PointOnSphere> end, GPlatesMaths::real_t radius)` | function | `boost::optional<double>` | — |
| `get_area_of_polygon( const GPlatesViewOperations::GeometryBuilder *geometry_builder, double radius)` | function | `boost::optional<double>` | Returns the area of the polygon contained inside the geometry\_builder, which is assumed to be non-NULL. |
| `DEFAULT_RADIUS_OF_EARTH` | variable | `double` | — |
| `GPLATES_CANVASTOOLS_MEASUREDISTANCESTATE_H` | macro | `None` | — |

## Notes

- `d_current_geometry_builder_ptr` is a non-owning pointer set by `switch_geometry_builder`; each switch disconnects the previous builder's signal before reconnecting to the new one, so listeners never accumulate across geometry-builder changes.
- A geometry builder with zero or one point is treated as "no selection" for Feature Measure, and multipoint geometries are excluded entirely — only `POLYLINE`/`POLYGON` builds are measured.
- `set_radius()` is a no-op when the new radius is almost exactly equal to the current one (`GPlatesMaths::are_almost_exactly_equal`), so repeated calls with the same value do not re-emit updates or repeat the distance/area recomputation.

## Used by

| Unit | Component | References |
|---|---|---|
| [canvas-tools/MeasureDistance](MeasureDistance.md) | canvas-tools | 17 |
| [qt-widgets/MeasureDistanceWidget](../qt-widgets/MeasureDistanceWidget.md) | qt-widgets | 7 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 6 |
| [data-mining/deprecated/IsInRegionOfInterestVisitor](../data-mining/deprecated/IsInRegionOfInterestVisitor.md) | data-mining | 3 |
| [opengl/GLIntersect](../opengl/GLIntersect.md) | opengl | 3 |

## Related

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_geometry_operation_state_ptr` | `switched_geometry_builder( GPlatesViewOperations::GeometryBuilder *)` | `this` | `switch_geometry_builder( GPlatesViewOperations::GeometryBuilder *)` |
| `d_current_geometry_builder_ptr` | `stopped_updating_geometry_excluding_intermediate_moves()` | `this` | `reexamine_geometry_builder()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/canvas-tools/MeasureDistanceState.h
python scripts/gpq.py def GPlatesCanvasTools::MeasureDistanceState --body
python scripts/gpq.py uses MeasureDistanceState --kind class
python scripts/gpq.py hier MeasureDistanceState
```
