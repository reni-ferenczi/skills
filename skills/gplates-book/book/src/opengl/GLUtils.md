# GLUtils

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 275 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLUtils.h` | C++ | 681 |
| `src/opengl/GLUtils.cc` | C++ | 474 |

## Overview

[[[PROSE overview unit=opengl/GLUtils tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLUtils::QuadTreeClipSpaceTransform`](#gplatesopenglglutilsquadtreeclipspacetransform) | class | — | — | 0 | Used to scale/translate the clip space \[-1, 1\] coordinates of a quad tree node relative to its ancestor node (or vice versa). |
| [`GPlatesOpenGL::GLUtils::QuadTreeUVTransform`](#gplatesopenglglutilsquadtreeuvtransform) | class | — | — | 0 | Used to scale/translate texture coordinates of a descendant quad tree node relative to its ancestor node (and vice versa). |

## Members

### `GPlatesOpenGL::GLUtils::QuadTreeClipSpaceTransform`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `get_expand_tile_ratio( unsigned int tile_texel_dimension, const double &tile_border_overlap_in_texels)` | method | `double` | public | Calculates a tile expand ratio for a tile of the specified texel dimension and the desired overlap in units of texels. |
| `QuadTreeClipSpaceTransform( const double &expand_tile_ratio = 1.0)` | constructor | `None` | public | Identity transformation. |
| `QuadTreeClipSpaceTransform( const QuadTreeClipSpaceTransform &parent_clip_space_transform, unsigned int x_offset, unsigned int y_offset)` | constructor | `None` | public | Scale/translate this quad tree child node relative to its parent. |
| `transform( GLMatrix &matrix)` | method | `void` | public | Post-multiplies matrix with the appropriate scale and translation. |
| `loose_transform( GLMatrix &matrix)` | method | `void` | public | Same as transform but suitable for a 'loose' tile - see GLCubeSubdivision for more details. |
| `inverse_transform( GLMatrix &matrix)` | method | `void` | public | Post-multiplies matrix with the inverse (of the appropriate scale and translation). |
| `inverse_loose_transform( GLMatrix &matrix)` | method | `void` | public | Same as inverse\_transform but suitable for a 'loose' tile - see GLCubeSubdivision for more details. |
| `get_translate_x()` | method | `double` | public | Returns the 'x' translate part of the transform. |
| `get_translate_y()` | method | `double` | public | Same as get\_translate\_x but for the 'y' component (instead of the 'x' component). |
| `get_loose_translate_x()` | method | `double` | public | Same as get\_translate\_x but suitable for a 'loose' tile - see GLCubeSubdivision for more details. |
| `get_loose_translate_y()` | method | `double` | public | Same as get\_translate\_y but suitable for a 'loose' tile - see GLCubeSubdivision for more details. |
| `get_inverse_translate_x()` | method | `double` | public | Returns the 'x' translate part of the \*inverse\* transform. |
| `get_inverse_translate_y()` | method | `double` | public | Same as get\_inverse\_translate\_x but for the 'y' component (instead of the 'x' component). |
| `get_inverse_loose_translate_x()` | method | `double` | public | Same as get\_inverse\_translate\_x but suitable for a 'loose' tile - see GLCubeSubdivision for more details. |
| `get_inverse_loose_translate_y()` | method | `double` | public | Same as get\_translate\_y but suitable for a 'loose' tile - see GLCubeSubdivision for more details. |
| `d_expand_tile_ratio` | field | `double` | private | — |
| `d_inverse_expand_tile_ratio` | field | `double` | private | — |
| `d_scale` | field | `double` | private | — |
| `d_inverse_scale` | field | `double` | private | — |
| `d_relative_x_node_offset` | field | `unsigned int` | private | — |
| `d_relative_y_node_offset` | field | `unsigned int` | private | — |

### `GPlatesOpenGL::GLUtils::QuadTreeUVTransform`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `get_expand_tile_ratio( unsigned int tile_texel_dimension, const double &tile_border_overlap_in_texels)` | method | `double` | public | Calculates a tile expand ratio for a tile of the specified texel dimension and the desired overlap in units of texels. |
| `QuadTreeUVTransform( const double &expand_tile_ratio = 1.0)` | constructor | `None` | public | Identity transformation. |
| `QuadTreeUVTransform( const QuadTreeUVTransform &parent_uv_transform, unsigned int x_offset, unsigned int y_offset)` | constructor | `None` | public | Scale/translate this quad tree child node relative to its parent. |
| `transform( GLMatrix &matrix)` | method | `void` | public | Post-multiplies matrix with the appropriate scale and translation. |
| `loose_transform( GLMatrix &matrix)` | method | `void` | public | Same as transform but suitable for a 'loose' tile - see GLCubeSubdivision for more details. |
| `inverse_transform( GLMatrix &matrix)` | method | `void` | public | Post-multiplies matrix with the inverse (of the appropriate scale and translation). |
| `inverse_loose_transform( GLMatrix &matrix)` | method | `void` | public | Same as inverse\_transform but suitable for a 'loose' tile - see GLCubeSubdivision for more details. |
| `get_translate_u()` | method | `double` | public | Returns the 'u' translate part of the transform. |
| `get_translate_v()` | method | `double` | public | Same as get\_translate\_u but for the 'v' component (instead of the 'u' component). |
| `get_loose_translate_u()` | method | `double` | public | Same as get\_translate\_u but suitable for a 'loose' tile - see GLCubeSubdivision for more details. |
| `get_loose_translate_v()` | method | `double` | public | Same as get\_translate\_v but suitable for a 'loose' tile - see GLCubeSubdivision for more details. |
| `get_inverse_translate_u()` | method | `double` | public | Returns the 'u' translate part of the \*inverse\* transform. |
| `get_inverse_translate_v()` | method | `double` | public | Same as get\_inverse\_translate\_u but for the 'v' component (instead of the 'u' component). |
| `get_inverse_loose_translate_u()` | method | `double` | public | Same as get\_inverse\_translate\_u but suitable for a 'loose' tile - see GLCubeSubdivision for more details. |
| `get_inverse_loose_translate_v()` | method | `double` | public | Same as get\_translate\_v but suitable for a 'loose' tile - see GLCubeSubdivision for more details. |
| `d_clip_space_transform` | field | `QuadTreeClipSpaceTransform` | private | Delegate the core quad-tree scaling/translation to QuadTreeClipSpaceTransform. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `create_object_plane( const GLdouble &x, const GLdouble &y, const GLdouble &z, const GLdouble &w)` | function | `std::vector<GLdouble>` | Converts an array of 4 numbers representing a tex gen plane into a std::vector. |
| `GPLATES_OPENGL_GLUTILS_H` | macro | `None` | — |
| `check_gl_errors( const GPlatesUtils::CallStack::Trace &assert_location)` | function | `void` | Checks if any OpenGL errors (see glGetError) have been recorded (by OpenGL) since the last call to this function. |
| `create_full_screen_2D_textured_quad( GLRenderer &renderer)` | function | `GLCompiledDrawState::non_null_ptr_type` | Creates a full-screen quad vertex array with 2D texture coordinates (in \[0,1\] range) and with all vertices containing the colour white - RGBA(1.0, 1.0, 1.0, 1.0). |
| `create_full_screen_2D_coloured_quad( GLRenderer &renderer, const GPlatesGui::rgba8_t &colour)` | function | `GLCompiledDrawState::non_null_ptr_type` | Creates a full-screen quad vertex array of the specified vertex colour. |
| `create_full_screen_2D_coloured_textured_quad( GLRenderer &renderer, const GPlatesGui::rgba8_t &colour)` | function | `GLCompiledDrawState::non_null_ptr_type` | Creates a full-screen quad vertex array with 2D texture coordinates (in \[0,1\] range) and with all vertices containing the specified vertex colour. |
| `get_clip_space_to_texture_space_transform` | variable | `GLMatrix` | Returns a matrix that converts (x,y) clip-space coordinates in the range \[-1,1\] to texture coordinates in the range \[0,1\]. |
| `set_full_screen_quad_texture_state( GLRenderer &renderer, const GLTexture::shared_ptr_to_const_type &texture, const unsigned int texture_unit = 0, const GLint tex_env_mode = GL_REPLACE, const boost::optional<const GLMatrix &> &texture_transform_matrix = boost::none, const GLenum texture_target = GL_TEXTURE_2D)` | function | `void` | Sets renderer state to translate/scale texture coordinates and then look up a texture. |
| `set_frustum_texture_state( GLRenderer &renderer, const GLTexture::shared_ptr_to_const_type &texture, const GLMatrix &projection_transform, const GLMatrix &view_transform, const unsigned int texture_unit = 0, const GLint tex_env_mode = GL_REPLACE, const boost::optional<const GLMatrix &> &texture_transform_matrix = get_c ...` | function | `void` | Sets renderer state to map (x,y,z) positions into texture coordinates using the specified frustum and then look up a texture. |
| `set_object_linear_tex_gen_state( GLRenderer &renderer, const unsigned int texture_unit = 0)` | function | `void` | Enables texture coordinate generation and sets the texture transform state on renderer to generate 4D texture coordinates (s,t,r,q) directly (object linear) from vertex (x,y,z) positions. |

## Notes

[[[PROSE notes unit=opengl/GLUtils tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 83 |
| [opengl/GLScalarField3D](GLScalarField3D.md) | opengl | 35 |
| [opengl/GLMultiResolutionMapCubeMesh](GLMultiResolutionMapCubeMesh.md) | opengl | 23 |
| [opengl/GLRasterCoRegistration](GLRasterCoRegistration.md) | opengl | 21 |
| [opengl/GLMultiResolutionCubeMesh](GLMultiResolutionCubeMesh.md) | opengl | 20 |
| [gui/LayerPainter](../gui/LayerPainter.md) | gui | 19 |
| [opengl/GLBufferObject](GLBufferObject.md) | opengl | 9 |
| [opengl/GLFilledPolygonsGlobeView](GLFilledPolygonsGlobeView.md) | opengl | 9 |
| [opengl/GLContext](GLContext.md) | opengl | 7 |
| [opengl/GLTextureUtils](GLTextureUtils.md) | opengl | 7 |
| [opengl/GLVisualRasterSource](GLVisualRasterSource.md) | opengl | 7 |
| [gui/FeedbackOpenGLToQPainter](../gui/FeedbackOpenGLToQPainter.md) | gui | 5 |
| [opengl/GLLight](GLLight.md) | opengl | 4 |
| [opengl/GLMultiResolutionRaster](GLMultiResolutionRaster.md) | opengl | 4 |
| [opengl/GLAgeGridMaskSource](GLAgeGridMaskSource.md) | opengl | 3 |
| [opengl/GLMultiResolutionCubeRaster](GLMultiResolutionCubeRaster.md) | opengl | 3 |
| [opengl/GLMultiResolutionCubeReconstructedRaster](GLMultiResolutionCubeReconstructedRaster.md) | opengl | 3 |
| [opengl/GLNormalMapSource](GLNormalMapSource.md) | opengl | 3 |
| [opengl/GLRenderTargetImpl](GLRenderTargetImpl.md) | opengl | 3 |
| [opengl/GLMultiResolutionRasterMapView](GLMultiResolutionRasterMapView.md) | opengl | 2 |

*... and 6 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLUtils.h
python scripts/gpq.py def GPlatesOpenGL::GLUtils::QuadTreeClipSpaceTransform --body
python scripts/gpq.py uses QuadTreeClipSpaceTransform --kind class
python scripts/gpq.py hier QuadTreeClipSpaceTransform
```
