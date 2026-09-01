# MovePoleOperation

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 131 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/MovePoleOperation.h` | C++ | 236 |
| `src/view-operations/MovePoleOperation.cc` | C++ | 344 |

## Overview

`MovePoleOperation` is the reference-counted backend for the "Move Pole" canvas tools on both the globe and map views, structurally similar to `ChangeLightDirectionOperation` but manipulating a `GPlatesQtWidgets::MovePoleWidget`'s pole location instead of the light direction. Because the globe and map use different coordinate systems, it implements two separate hit tests: `test_proximity_to_pole_on_globe` uses the same spherical dot-product test as `ChangeLightDirectionOperation`, while `test_proximity_to_pole_on_map` compares planar distance in map *scene* coordinates (scaled by `GPlatesGui::ViewportZoom`), since a spherical proximity test is meaningless once the sphere has been projected onto the map. `start_drag_on_globe`/`start_drag_on_map` both defer to `MovePoleWidget::can_change_pole()` before allowing a drag, since the widget can refuse to move the pole (for example when it is constrained to the focused feature's stage pole).

As a `GPlatesUtils::ReferenceCount`-based type its constructor is private; instances are obtained only through the static `create()` factory, matching the `non_null_ptr_type` convention used elsewhere in the codebase.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::MovePoleOperation`](#gplatesviewoperationsmovepoleoperation) | class | `QObject`<br>[`GPlatesUtils::ReferenceCount<MovePoleOperation>`](../utils/ReferenceCount.md) | — | 0 | Enables users to drag the pole to a new location/direction. |

## Members

### `GPlatesViewOperations::MovePoleOperation`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<MovePoleOperation>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const MovePoleOperation>` | public | — |
| `create( GPlatesGui::ViewportZoom &viewport_zoom, RenderedGeometryCollection &rendered_geometry_collection, RenderedGeometryCollection::MainLayerType main_rendered_layer_type, GPlatesQtWidgets::MovePoleWidget &move_pole_widget)` | method | `non_null_ptr_type` | public | Create a new MovePoleOperation instance. |
| `activate()` | method | `void` | public | Activate this operation. |
| `deactivate()` | method | `void` | public | Deactivate this operation. |
| `mouse_move_on_globe( const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, const double &closeness_inclusion_threshold)` | method | `void` | public | The mouse has moved (in globe view) but it is not a drag because mouse button is not pressed. |
| `mouse_move_on_map( const QPointF &current_point_on_scene, const GPlatesMaths::PointOnSphere &current_point_on_sphere, const GPlatesGui::MapProjection &map_projection)` | method | `void` | public | The mouse has moved (in map view) but it is not a drag because mouse button is not pressed. |
| `start_drag_on_globe( const GPlatesMaths::PointOnSphere &oriented_initial_pos_on_globe, const double &closeness_inclusion_threshold)` | method | `bool` | public | User has just clicked and dragged on the globe. |
| `start_drag_on_map( const QPointF &initial_point_on_scene, const GPlatesMaths::PointOnSphere &initial_point_on_sphere, const GPlatesGui::MapProjection &map_projection)` | method | `bool` | public | User has just clicked and dragged on the map. |
| `update_drag( const GPlatesMaths::PointOnSphere &oriented_pos_on_sphere)` | method | `void` | public | User is currently in the middle of dragging the mouse. |
| `end_drag( const GPlatesMaths::PointOnSphere &oriented_pos_on_sphere)` | method | `void` | public | User has released mouse button after dragging. |
| `react_pole_changed()` | method | `void` | private | — |
| `ARROW_HIGHLIGHT_COLOUR` | field | `GPlatesGui::Colour` | private | Colour to use for highlighting the pole arrow. |
| `SYMBOL_HIGHLIGHT_COLOUR` | field | `GPlatesGui::Colour` | private | Colour to use for highlighting the pole symbol. |
| `ARROW_UNHIGHLIGHT_COLOUR` | field | `GPlatesGui::Colour` | private | Colour to use when \*not\* highlighting the pole arrow. |
| `SYMBOL_UNHIGHLIGHT_COLOUR` | field | `GPlatesGui::Colour` | private | Colour to use when \*not\* highlighting the pole symbol. |
| `ARROW_PROJECTED_LENGTH` | field | `float` | private | — |
| `ARROW_HEAD_PROJECTED_SIZE` | field | `float` | private | — |
| `RATIO_ARROW_LINE_WIDTH_TO_ARROW_HEAD_SIZE` | field | `float` | private | — |
| `SYMBOL_TYPE` | field | `RenderedRadialArrow::SymbolType` | private | — |
| `SYMBOL_SIZE` | field | `float` | private | — |
| `d_viewport_zoom` | field | `GPlatesGui::ViewportZoom` | private | — |
| `d_rendered_geometry_collection` | field | `RenderedGeometryCollection` | private | This is where we render our geometries and activate our render layer. |
| `d_main_rendered_layer_type` | field | `RenderedGeometryCollection::MainLayerType` | private | The main rendered layer we're currently rendering into. |
| `d_move_pole_widget` | field | `GPlatesQtWidgets::MovePoleWidget` | private | Used to get and set the pole location. |
| `d_pole_layer_ptr` | field | `RenderedGeometryCollection::child_layer_owner_ptr_type` | private | Rendered geometry layer used for pole location. |
| `d_is_dragging_pole` | field | `bool` | private | Did the user click on the pole and is currently dragging it. |
| `MovePoleOperation( GPlatesGui::ViewportZoom &viewport_zoom, RenderedGeometryCollection &rendered_geometry_collection, RenderedGeometryCollection::MainLayerType main_rendered_layer_type, GPlatesQtWidgets::MovePoleWidget &move_pole_widget)` | constructor | `None` | private | — |
| `create_rendered_geometry_layers()` | method | `void` | private | — |
| `adjust_closeness_inclusion_threshold( const double &closeness_inclusion_threshold)` | method | `double` | private | Increase the closeness inclusion threshold from point width to arrowhead width. |
| `test_proximity_to_pole_on_globe( const GPlatesMaths::PointOnSphere &oriented_pos_on_sphere, const double &closeness_inclusion_threshold)` | method | `bool` | private | — |
| `test_proximity_to_pole_on_map( const QPointF &point_on_scene, const GPlatesMaths::PointOnSphere &point_on_sphere, const GPlatesGui::MapProjection &map_projection)` | method | `bool` | private | — |
| `move_pole( const GPlatesMaths::PointOnSphere &pole)` | method | `void` | private | — |
| `render_pole( bool highlight)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `ARROW_HIGHLIGHT_COLOUR` | variable | `GPlatesGui::Colour` | Highlight arrow in yellow with some transparency. |
| `SYMBOL_HIGHLIGHT_COLOUR` | variable | `GPlatesGui::Colour` | Highlight symbol in red. |
| `ARROW_UNHIGHLIGHT_COLOUR` | variable | `GPlatesGui::Colour` | Unhighlight arrow in white. |
| `SYMBOL_UNHIGHLIGHT_COLOUR` | variable | `GPlatesGui::Colour` | Unhighlight symbol in white. |
| `ARROW_PROJECTED_LENGTH` | variable | `float` | — |
| `ARROW_HEAD_PROJECTED_SIZE` | variable | `float` | — |
| `RATIO_ARROW_LINE_WIDTH_TO_ARROW_HEAD_SIZE` | variable | `float` | — |
| `SYMBOL_TYPE` | variable | `GPlatesViewOperations::RenderedRadialArrow::SymbolType` | — |
| `SYMBOL_SIZE` | variable | `float` | — |
| `GPLATES_VIEW_OPERATIONS_MOVEPOLEOPERATION_H` | macro | `None` | — |

## Notes

The connection to `MovePoleWidget::pole_changed` is made in `activate()` and torn down in `deactivate()`, not held permanently, so `react_pole_changed()` can safely assume the pole is always unhighlighted when it fires (the mouse cannot be hovering the globe/map and editing the task-panel widget at the same time). Like `ChangeLightDirectionOperation`, pole moves are applied straight to `MovePoleWidget` and are not pushed onto the undo stack by this class.

## Used by

| Unit | Component | References |
|---|---|---|
| [canvas-tools/MovePoleMap](../canvas-tools/MovePoleMap.md) | canvas-tools | 15 |
| [canvas-tools/MovePoleGlobe](../canvas-tools/MovePoleGlobe.md) | canvas-tools | 13 |
| [gui/PoleManipulationCanvasToolWorkflow](../gui/PoleManipulationCanvasToolWorkflow.md) | gui | 3 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&d_move_pole_widget` | `pole_changed(boost::optional<GPlatesMaths::PointOnSphere>)` | `this` | `react_pole_changed()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/MovePoleOperation.h
python scripts/gpq.py def GPlatesViewOperations::MovePoleOperation --body
python scripts/gpq.py uses MovePoleOperation --kind class
python scripts/gpq.py hier MovePoleOperation
```
