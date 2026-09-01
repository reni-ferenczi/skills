# SceneLightingParameters

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1023 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/SceneLightingParameters.h` | C++ | 237 |
| `src/gui/SceneLightingParameters.cc` | C++ | 130 |

## Overview

`GPlatesGui::SceneLightingParameters` is a plain value object holding the scene's lighting configuration: whether lighting is enabled per primitive type (geometry, filled geometry, direction arrows, rasters, scalar fields), the ambient light contribution, and separate light directions for the 3D globe view and the 2D map view. It has no rendering logic of its own — `opengl/GLLight` and the painters in `gui` read it to decide how to shade what they draw, and `qt-widgets/LightingWidget` is the UI that edits it via `presentation/ViewState`.

The light direction can either stay attached to the view frame (rotating with the camera) or stay fixed in the world frame (fixed to the globe); `is_light_direction_attached_to_view_frame()` records which mode is active, and the free `transform_globe_*_light_direction_*` functions convert a direction between view-space and world-space accordingly, using either a `GPlatesMaths::Rotation` or a `GPlatesOpenGL::GLMatrix` to describe the current view transform.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::SceneLightingParameters`](#gplatesguiscenelightingparameters) | class | `boost::equality_comparable<SceneLightingParameters>` | — | 0 | Parameters to control scene lighting such as light direction, ambient light level, etc. |

## Members

### `GPlatesGui::SceneLightingParameters`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LightingPrimitiveType` | enum | `None` | public | The types of primitives that lighting can be individually enabled/disabled for. |
| `SceneLightingParameters()` | constructor | `None` | public | The initial light direction in the 3D globe views is along x-axis which is latitude/longitude (0,0) which is initially facing the user when GPlates starts. |
| `enable_lighting( LightingPrimitiveType lighting_primitive_type, bool enable = true)` | method | `void` | public | Enables (or disables) scene lighting for the specified lighting primitive. |
| `is_lighting_enabled( LightingPrimitiveType lighting_primitive_type)` | method | `bool` | public | Returns true if scene lighting is enabled for the specified lighting primitive. |
| `set_ambient_light_contribution( const double &ambient_light_contribution)` | method | `void` | public | Sets the ambient light contribution - must be in the range \[0,1\]. |
| `set_globe_view_light_direction( const GPlatesMaths::UnitVector3D &light_direction)` | method | `void` | public | Sets the globe view light direction. |
| `set_map_view_light_direction( const GPlatesMaths::UnitVector3D &map_view_light_direction)` | method | `void` | public | Sets the map view light direction. |
| `set_light_direction_attached_to_view_frame( bool light_direction_attached_to_view_frame = true)` | method | `void` | public | Enables (or disables) scene lighting. |
| `is_light_direction_attached_to_view_frame()` | method | `bool` | public | Returns true if light direction is attached to the view frame (and hence rotates as the view rotates). |
| `operator==( const SceneLightingParameters &rhs)` | operator | `bool` | public | Equality comparison operator. |
| `lighting_primitives_enable_state_type` | typedef | `std::bitset<NUM_LIGHTING_PRIMITIVE_TYPES>` | private | Type contains lighting enabled state. |
| `d_lighting_primitives_enable_state` | field | `lighting_primitives_enable_state_type` | private | Determines what lighting is enabled for. |
| `d_light_direction_attached_to_view_frame` | field | `bool` | private | — |
| `d_ambient_light_contribution` | field | `double` | private | — |
| `d_globe_view_light_direction` | field | `GPlatesMaths::UnitVector3D` | private | The light direction for the 3D globe views. |
| `d_map_view_light_direction` | field | `GPlatesMaths::UnitVector3D` | private | The light direction for the 2D map views. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `operator==( const SceneLightingParameters &rhs)` | operator | `bool` | — |
| `GPLATES_GUI_SCENELIGHTINGPARAMETERS_H` | macro | `None` | — |
| `transform_globe_view_space_light_direction_to_world_space( const GPlatesMaths::UnitVector3D &view_space_light_direction, const GPlatesMaths::Rotation &view_space_transform)` | function | `GPlatesMaths::UnitVector3D` | Convenience function to reverse rotate the light direction (in view-space) back to world-space. |
| `transform_globe_view_space_light_direction_to_world_space( const GPlatesMaths::UnitVector3D &view_space_light_direction, const GPlatesOpenGL::GLMatrix &view_space_transform)` | function | `GPlatesMaths::UnitVector3D` | Convenience function to reverse rotate the light direction (in view-space) back to world-space. |
| `transform_globe_world_space_light_direction_to_view_space( const GPlatesMaths::UnitVector3D &world_space_light_direction, const GPlatesMaths::Rotation &view_space_transform)` | function | `GPlatesMaths::UnitVector3D` | Convenience function to rotate the light direction (in world-space) to view-space. |
| `transform_globe_world_space_light_direction_to_view_space( const GPlatesMaths::UnitVector3D &world_space_light_direction, const GPlatesOpenGL::GLMatrix &view_space_transform)` | function | `GPlatesMaths::UnitVector3D` | Convenience function to rotate the light direction (in world-space) to view-space. |

## Notes

The ambient light contribution must lie in `[0, 1]`; diffuse contribution is `1 - ambient`, and ambient does not use the light direction at all. An ambient value of 1.0 leaves input colours unchanged (lighting is effectively off). The 2D map view's light direction is currently constant regardless of `is_light_direction_attached_to_view_frame()` — only the 3D globe view direction actually rotates.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/LightingWidget](../qt-widgets/LightingWidget.md) | qt-widgets | 40 |
| [opengl/GLLight](../opengl/GLLight.md) | opengl | 18 |
| [view-operations/ChangeLightDirectionOperation](../view-operations/ChangeLightDirectionOperation.md) | view-operations | 8 |
| [gui/LayerPainter](LayerPainter.md) | gui | 7 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](../opengl/GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 7 |
| [opengl/GLScalarField3D](../opengl/GLScalarField3D.md) | opengl | 4 |
| [opengl/GLVisualLayers](../opengl/GLVisualLayers.md) | opengl | 4 |
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 4 |
| [opengl/GLFilledPolygonsGlobeView](../opengl/GLFilledPolygonsGlobeView.md) | opengl | 2 |
| [gui/GlobeRenderedGeometryLayerPainter](GlobeRenderedGeometryLayerPainter.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/SceneLightingParameters.h
python scripts/gpq.py def GPlatesGui::SceneLightingParameters --body
python scripts/gpq.py uses SceneLightingParameters --kind class
python scripts/gpq.py hier SceneLightingParameters
```
