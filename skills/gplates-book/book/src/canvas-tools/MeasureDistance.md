# MeasureDistance

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 37 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/MeasureDistance.h` | C++ | 309 |
| `src/canvas-tools/MeasureDistance.cc` | C++ | 516 |

## Overview

[[[PROSE overview unit=canvas-tools/MeasureDistance tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCanvasTools::MeasureDistance`](#gplatescanvastoolsmeasuredistance) | class | `QObject`<br>[`CanvasTool`](CanvasTool.md) | — | 0 | Canvas tool used to measuring distances on the globe and map |

## Members

### `GPlatesCanvasTools::MeasureDistance`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( const status_bar_callback_type &status_bar_callback, GPlatesViewOperations::GeometryBuilder &geometry_builder, GeometryOperationState &geometry_operation_state, GPlatesViewOperations::RenderedGeometryCollection &rendered_geom_collection, GPlatesViewOperations::RenderedGeometryCollection::MainLayerType main_rend ...` | method | `non_null_ptr_type` | public | — |
| `handle_activation()` | method | `void` | public | — |
| `handle_deactivation()` | method | `void` | public | — |
| `handle_left_click( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `handle_move_without_drag( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `child_layer_ptr_type` | typedef | `GPlatesViewOperations::RenderedGeometryCollection::child_layer_owner_ptr_type` | private | Convenience typedef for GPlatesViewOperations::RenderedGeometryCollection::child\_layer\_owner\_ptr\_type |
| `MeasureDistance( const status_bar_callback_type &status_bar_callback, GPlatesViewOperations::GeometryBuilder &geometry_builder, GeometryOperationState &geometry_operation_state, GPlatesViewOperations::RenderedGeometryCollection &rendered_geom_collection, GPlatesViewOperations::RenderedGeometryCollection::MainLayerType ...` | constructor | `None` | private | — |
| `d_geometry_builder` | field | `GPlatesViewOperations::GeometryBuilder` | private | The geometry builder (either digitised geometry or focused feature geometry) to measure. |
| `d_geometry_operation_state` | field | `GeometryOperationState` | private | Lets others know which geometry builder we are targeting. |
| `d_rendered_geom_collection_ptr` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | For rendering purposes |
| `d_measure_distance_state_ptr` | field | `GPlatesCanvasTools::MeasureDistanceState` | private | A pointer to the state of the measure distance tool |
| `d_line_to_point_mapping` | field | `std::vector<GPlatesViewOperations::GeometryBuilder::PointIndex>` | private | A mapping from rendered line segment indices to point indices, such that the i-th element of this vector is the index of the point at the beginning of the i-th rendered line segment. |
| `d_main_rendered_layer_type` | field | `GPlatesViewOperations::RenderedGeometryCollection::MainLayerType` | private | The main rendered layer we're currently rendering into. |
| `d_geometry_layer_ptr` | field | `child_layer_ptr_type` | private | Rendered geometry layer for drawing geometry |
| `d_highlight_layer_ptr` | field | `child_layer_ptr_type` | private | Rendered geometry layer for mouse-over highlighting |
| `d_label_layer_ptr` | field | `child_layer_ptr_type` | private | Rendered geometry layer for the text label |
| `d_label_text` | field | `boost::optional<QString>` | private | Text of label to display, if any |
| `d_label_position` | field | `boost::optional<GPlatesMaths::PointOnSphere>` | private | Position of label to display, if any |
| `d_highlight_start` | field | `boost::optional<GPlatesMaths::PointOnSphere>` | private | Start point of mouse-over highlight, if any |
| `d_highlight_end` | field | `boost::optional<GPlatesMaths::PointOnSphere>` | private | End point of mouse-over highlight, if any |
| `QUICK_MEASURE_LINE_COLOUR` | field | `GPlatesGui::Colour` | private | The colour in which Quick Measure points and lines are rendered |
| `FEATURE_MEASURE_LINE_COLOUR` | field | `GPlatesGui::Colour` | private | The colour in which Feature Measure points and lines are rendered |
| `HIGHLIGHT_COLOUR` | field | `GPlatesGui::Colour` | private | The colour in which to render the mouse-over line highlight |
| `LABEL_COLOUR` | field | `GPlatesGui::Colour` | private | The colour in which to render the label |
| `LABEL_SHADOW_COLOUR` | field | `GPlatesGui::Colour` | private | The colour in which to render the shadow under the label |
| `POINT_SIZE` | field | `float` | private | The size of points |
| `LINE_WIDTH` | field | `float` | private | The thickness of lines |
| `LABEL_PRECISION` | field | `int` | private | Number of decimal places for distance labels |
| `LABEL_X_OFFSET` | field | `int` | private | Horizontal offset from mouse cursor (pixels) |
| `LABEL_Y_OFFSET` | field | `int` | private | Vertial offset from mouse cursor (pixels) |
| `make_signal_slot_connections()` | method | `void` | private | Creates signal/slot connections |
| `paint()` | method | `void` | private | Does the drawing for this canvas tool |
| `paint_quick_measure()` | method | `void` | private | Does drawing for Quick Measure |
| `paint_feature_measure()` | method | `void` | private | Does drawing for Feature Measure |
| `paint_highlight()` | method | `void` | private | Does drawing for mouse-over highlight |
| `paint_label()` | method | `void` | private | Does drawing of text label if there is currently one |
| `render_point_on_sphere( const GPlatesMaths::PointOnSphere &point_on_sphere, const GPlatesGui::Colour &colour, LayerPointerType layer_ptr)` | method | `void` | private | Places a point into a RenderedGeometryLayer. |
| `render_line( const GPlatesMaths::PointOnSphere &start, const GPlatesMaths::PointOnSphere &end, const GPlatesGui::Colour &colour, LayerPointerType layer_ptr)` | method | `bool` | private | Places a line into a RenderedGeometryLayer. |
| `render_multiple_line_segments( GPlatesViewOperations::GeometryBuilder::point_const_iterator_type begin, GPlatesViewOperations::GeometryBuilder::point_const_iterator_type end, const GPlatesGui::Colour &colour, bool is_polygon, LayerPointerType layer_ptr)` | method | `void` | private | Places multiple line segments into a RenderedGeometryLayer, assumes two or more points. |
| `add_distance_label_and_highlight( double distance, const GPlatesMaths::PointOnSphere &label_position, const GPlatesMaths::PointOnSphere &highlight_start, const GPlatesMaths::PointOnSphere &highlight_end, bool is_quick_measure)` | method | `void` | private | Adds distance label and mouse-over highlight, and (always) repaints |
| `remove_distance_label_and_highlight()` | method | `void` | private | Removes distance label and mouse-over highlight, and repaints if necessary |
| `feature_changed()` | method | `void` | public | — |
| `handle_quick_measure_cleared()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `QUICK_MEASURE_LINE_COLOUR` | variable | `GPlatesGui::Colour` | — |
| `FEATURE_MEASURE_LINE_COLOUR` | variable | `GPlatesGui::Colour` | — |
| `HIGHLIGHT_COLOUR` | variable | `GPlatesGui::Colour` | — |
| `LABEL_COLOUR` | variable | `GPlatesGui::Colour` | — |
| `LABEL_SHADOW_COLOUR` | variable | `GPlatesGui::Colour` | — |
| `POINT_SIZE` | variable | `float` | — |
| `LINE_WIDTH` | variable | `float` | — |
| `LABEL_PRECISION` | variable | `int` | — |
| `LABEL_X_OFFSET` | variable | `int` | — |
| `LABEL_Y_OFFSET` | variable | `int` | — |
| `GPLATES_CANVASTOOLS_MEASUREDISTANCE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=canvas-tools/MeasureDistance tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/DigitisationCanvasToolWorkflow](../gui/DigitisationCanvasToolWorkflow.md) | gui | 7 |
| [gui/FeatureInspectionCanvasToolWorkflow](../gui/FeatureInspectionCanvasToolWorkflow.md) | gui | 7 |
| [gui/SmallCircleCanvasToolWorkflow](../gui/SmallCircleCanvasToolWorkflow.md) | gui | 3 |

## Related

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_measure_distance_state_ptr` | `feature_in_geometry_builder_changed()` | `this` | `feature_changed()` |
| `d_measure_distance_state_ptr` | `quick_measure_cleared()` | `this` | `handle_quick_measure_cleared()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/canvas-tools/MeasureDistance.h
python scripts/gpq.py def GPlatesCanvasTools::MeasureDistance --body
python scripts/gpq.py uses MeasureDistance --kind class
python scripts/gpq.py hier MeasureDistance
```
