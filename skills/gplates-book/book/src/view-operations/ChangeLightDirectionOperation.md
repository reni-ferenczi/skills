# ChangeLightDirectionOperation

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 626 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/ChangeLightDirectionOperation.h` | C++ | 170 |
| `src/view-operations/ChangeLightDirectionOperation.cc` | C++ | 263 |

## Overview

`ChangeLightDirectionOperation` is the backend behind the "change light direction" canvas tool: the tool forwards mouse events (`mouse_move`, `start_drag`, `update_drag`, `end_drag`) to it, and it decides proximity, updates state and re-renders. It talks to `GPlatesGui::SceneLightingParameters` to read and write the current light direction, converting between view-space and world-space via `GPlatesGui::SimpleGlobeOrientation` whenever the light is attached to the view frame rather than the world. `GPlatesGui::ViewportZoom` is used to scale both the proximity threshold and the rendered arrow so hit-testing and the drawn arrow track the current zoom level.

The light direction is drawn as a `RenderedRadialArrow` into its own child layer of `RenderedGeometryCollection`, redrawn on every move/drag call with a highlighted or unhighlighted colour scheme depending on cursor proximity. The map-view symbol size is hard-coded to zero because dragging the light direction is only supported in the globe view.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::ChangeLightDirectionOperation`](#gplatesviewoperationschangelightdirectionoperation) | class | `boost::noncopyable` | — | 0 | Enables users to drag the light direction to a new location/direction. |

## Members

### `GPlatesViewOperations::ChangeLightDirectionOperation`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ChangeLightDirectionOperation( GPlatesGui::SceneLightingParameters &scene_lighting_parameters, GPlatesGui::SimpleGlobeOrientation &globe_orientation, GPlatesGui::ViewportZoom &viewport_zoom, RenderedGeometryCollection &rendered_geometry_collection, RenderedGeometryCollection::MainLayerType main_rendered_layer_type)` | constructor | `None` | public | — |
| `activate()` | method | `void` | public | Activate this operation. |
| `deactivate()` | method | `void` | public | Deactivate this operation. |
| `mouse_move( const GPlatesMaths::PointOnSphere &oriented_pos_on_sphere, const double &closeness_inclusion_threshold)` | method | `void` | public | The mouse has moved but it is not a drag because mouse button is not pressed. |
| `start_drag( const GPlatesMaths::PointOnSphere &oriented_pos_on_sphere, const double &closeness_inclusion_threshold)` | method | `void` | public | User has just clicked and dragged on the sphere. |
| `update_drag( const GPlatesMaths::PointOnSphere &oriented_pos_on_sphere)` | method | `void` | public | User is currently in the middle of dragging the mouse. |
| `end_drag( const GPlatesMaths::PointOnSphere &oriented_pos_on_sphere)` | method | `void` | public | User has released mouse button after dragging. |
| `ARROW_HIGHLIGHT_COLOUR` | field | `GPlatesGui::Colour` | private | Colour to use for highlighting the light direction arrow. |
| `SYMBOL_HIGHLIGHT_COLOUR` | field | `GPlatesGui::Colour` | private | Colour to use for highlighting the light direction symbol. |
| `ARROW_UNHIGHLIGHT_COLOUR` | field | `GPlatesGui::Colour` | private | Colour to use when \*not\* highlighting the light direction arrow. |
| `SYMBOL_UNHIGHLIGHT_COLOUR` | field | `GPlatesGui::Colour` | private | Colour to use when \*not\* highlighting the light direction symbol. |
| `ARROW_PROJECTED_LENGTH` | field | `float` | private | — |
| `ARROW_HEAD_PROJECTED_SIZE` | field | `float` | private | — |
| `RATIO_ARROW_LINE_WIDTH_TO_ARROW_HEAD_SIZE` | field | `float` | private | — |
| `SYMBOL_TYPE` | field | `RenderedRadialArrow::SymbolType` | private | — |
| `d_scene_lighting_parameters` | field | `GPlatesGui::SceneLightingParameters` | private | — |
| `d_globe_orientation` | field | `GPlatesGui::SimpleGlobeOrientation` | private | — |
| `d_viewport_zoom` | field | `GPlatesGui::ViewportZoom` | private | — |
| `d_rendered_geometry_collection` | field | `RenderedGeometryCollection` | private | This is where we render our geometries and activate our render layer. |
| `d_main_rendered_layer_type` | field | `RenderedGeometryCollection::MainLayerType` | private | The main rendered layer we're currently rendering into. |
| `d_light_direction_layer_ptr` | field | `RenderedGeometryCollection::child_layer_owner_ptr_type` | private | Rendered geometry layer used for light direction layer. |
| `d_is_dragging_light_direction` | field | `bool` | private | Did the user click on the light direction and is currently dragging it. |
| `create_rendered_geometry_layers()` | method | `void` | private | — |
| `get_world_space_light_direction()` | method | `GPlatesMaths::UnitVector3D` | private | — |
| `adjust_closeness_inclusion_threshold( const double &closeness_inclusion_threshold)` | method | `double` | private | Increase the closeness inclusion threshold from point width to arrowhead width. |
| `test_proximity_to_light_direction( const GPlatesMaths::PointOnSphere &oriented_pos_on_sphere, const double &closeness_inclusion_threshold)` | method | `bool` | private | — |
| `move_light_direction( const GPlatesMaths::UnitVector3D &world_space_light_direction)` | method | `void` | private | — |
| `render_light_direction( bool highlight)` | method | `void` | private | — |

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
| `GPLATES_VIEW_OPERATIONS_CHANGELIGHTDIRECTIONOPERATION_H` | macro | `None` | — |

## Notes

Unlike geometry-editing operations, light-direction changes are applied directly to `SceneLightingParameters` and are not pushed onto the undo stack — dragging the light has no undo/redo history. `adjust_closeness_inclusion_threshold` relies on a small-angle approximation (`arcsin(size) ~ size`) to expand the hit-test radius by the arrow head's size, so it is only accurate for small projected arrow sizes.

## Used by

| Unit | Component | References |
|---|---|---|
| [canvas-tools/ChangeLightDirectionGlobe](../canvas-tools/ChangeLightDirectionGlobe.md) | canvas-tools | 11 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/ChangeLightDirectionOperation.h
python scripts/gpq.py def GPlatesViewOperations::ChangeLightDirectionOperation --body
python scripts/gpq.py uses ChangeLightDirectionOperation --kind class
python scripts/gpq.py hier ChangeLightDirectionOperation
```
