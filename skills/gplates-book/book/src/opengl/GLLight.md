# GLLight

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 153 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLLight.h` | C++ | 299 |
| `src/opengl/GLLight.cc` | C++ | 557 |

## Overview

[[[PROSE overview unit=opengl/GLLight tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLLight`](#gplatesopenglgllight) | class | [`GPlatesUtils::ReferenceCount<GLLight>`](../utils/ReferenceCount.md) | — | 0 | A directional light that encodes light direction for both the 3D globe view and the 2D map views. |

## Members

### `GPlatesOpenGL::GLLight`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLLight>` | public | A convenience typedef for a shared pointer to a non-const GLLight. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLLight>` | public | A convenience typedef for a shared pointer to a const GLLight. |
| `is_supported( GLRenderer &renderer)` | method | `bool` | public | Returns true if lighting is supported on the runtime system. |
| `create( GLRenderer &renderer, const GPlatesGui::SceneLightingParameters &scene_lighting_params = GPlatesGui::SceneLightingParameters(), const GLMatrix &view_orientation = GLMatrix::IDENTITY, boost::optional<GPlatesGui::MapProjection::non_null_ptr_to_const_type> map_projection = boost::none)` | method | `non_null_ptr_type` | public | Creates a GLLight object. |
| `set_scene_lighting( GLRenderer &renderer, const GPlatesGui::SceneLightingParameters &scene_lighting_params, const GLMatrix &view_orientation = GLMatrix::IDENTITY, boost::optional<GPlatesGui::MapProjection::non_null_ptr_to_const_type> map_projection = boost::none)` | method | `void` | public | Updates internal state due to changes in these parameters. view\_orientation is the orientation of the view direction relative to the globe (in 3D globe views) or relative to the unrotated map (in 2D map views). |
| `get_map_projection()` | method | `boost::optional<GPlatesGui::MapProjection::non_null_ptr_to_const_type>` | public | Returns the map projection if view used for light is a 2D map view (not the 3D globe view). |
| `get_map_view_constant_lighting( GLRenderer &renderer)` | method | `float` | public | Returns the ambient and diffuse lighting for the 2D map views when no surface normal mapping is used (ie, when the surface normal is constant across the map and perpendicular to the map). |
| `get_map_view_light_direction_cube_map_texture( GLRenderer &renderer)` | method | `GLTexture::shared_ptr_to_const_type` | public | Returns the hardware cube map texture containing the \*world-space\* light direction(s) for the current 2D map view (with map projection specified in set\_scene\_lighting). |
| `d_subject_token` | field | `GPlatesUtils::SubjectToken` | private | Used to inform clients that we have been updated. |
| `d_scene_lighting_params` | field | `GPlatesGui::SceneLightingParameters` | private | The parameters used to surface light the reconstructed raster. |
| `d_view_orientation` | field | `GLMatrix` | private | This is the orientation of the view direction relative to the globe (in 3D globe views) or relative to the unrotated map (in 2D map views). |
| `d_globe_view_light_direction` | field | `GPlatesMaths::UnitVector3D` | private | The world-space light direction for the 3D globe view (includes conversion from view-space). |
| `d_map_view_constant_lighting` | field | `float` | private | The ambient+diffuse lighting for the 2D map views (includes conversion from view-space) when the normal mapping is \*not\* used (ie, surface is constant across map and perpendicular to map). |
| `d_map_projection` | field | `boost::optional<GPlatesGui::MapProjection::non_null_ptr_to_const_type>` | private | The map projection if the light direction is (constant) in 2D map-space. |
| `d_map_view_light_direction_cube_texture_dimension` | field | `unsigned int` | private | The dimension of the square faces of the light direction cube texture (for the 2D map views). |
| `d_map_view_light_direction_cube_texture` | field | `GLTexture::shared_ptr_type` | private | The hardware cube map encoding the light direction(s) for a 2D map view. |
| `d_render_map_view_light_direction_program_object` | field | `boost::optional<GLProgramObject::shared_ptr_type>` | private | Shader program to render light direction into cube texture for 2D map views. |
| `create_map_view_light_direction_cube_texture( GLRenderer &renderer, const GLTexture::shared_ptr_type &map_view_light_direction_cube_texture)` | method | `void` | private | — |
| `GLLight( GLRenderer &renderer, const GPlatesGui::SceneLightingParameters &scene_lighting_params, const GLMatrix &view_orientation, boost::optional<GPlatesGui::MapProjection::non_null_ptr_to_const_type> map_projection)` | constructor | `None` | private | — |
| `create_shader_programs( GLRenderer &renderer)` | method | `void` | private | — |
| `update_map_view( GLRenderer &renderer)` | method | `void` | private | — |
| `update_globe_view( GLRenderer &renderer)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `MAP_VIEW_LIGHT_DIRECTION_CUBE_TEXTURE_DIMENSION` | variable | `unsigned int` | Dimension of the map view light direction cube texture. |
| `RENDER_MAP_VIEW_LIGHT_DIRECTION_VERTEX_SHADER_SOURCE_FILE_NAME` | variable | `QString` | Vertex shader source code to render light direction into cube texture for a 2D map view. |
| `RENDER_MAP_VIEW_LIGHT_DIRECTION_FRAGMENT_SHADER_SOURCE_FILE_NAME` | variable | `QString` | Fragment shader source code to render light direction into cube texture for a 2D map view. |
| `GPLATES_OPENGL_GLLIGHT_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLLight tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLVisualLayers](GLVisualLayers.md) | opengl | 20 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 17 |
| [opengl/GLScalarField3D](GLScalarField3D.md) | opengl | 8 |
| [gui/LayerPainter](../gui/LayerPainter.md) | gui | 5 |
| [opengl/GLFilledPolygonsGlobeView](GLFilledPolygonsGlobeView.md) | opengl | 5 |
| [gui/Globe](../gui/Globe.md) | gui | 2 |
| [qt-widgets/ImportScalarField3DDialog](../qt-widgets/ImportScalarField3DDialog.md) | qt-widgets | 2 |
| [gui/GlobeRenderedGeometryCollectionPainter](../gui/GlobeRenderedGeometryCollectionPainter.md) | gui | 1 |

## Related

**Shader programs compiled by this unit**

| Shader unit | Component |
|---|---|
| [shaders/light](../qt-resources/opengl/light.md) | shaders |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLLight.h
python scripts/gpq.py def GPlatesOpenGL::GLLight --body
python scripts/gpq.py uses GLLight --kind class
python scripts/gpq.py hier GLLight
```
