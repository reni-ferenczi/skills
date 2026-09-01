# GLUtils

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 275 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLUtils.h` | C++ | 681 |
| `src/opengl/GLUtils.cc` | C++ | 474 |

## Overview

`GLUtils` is a namespace, not a class, and it holds the two kinds of small shared
machinery that the rendering backend needs everywhere but that belong to no
single renderer. The first kind is a handful of helpers layered over
`GLRenderer`. Apart from `check_gl_errors` nothing here talks to OpenGL
directly: the texture helpers go through `GLRenderer::gl_bind_texture`,
`gl_enable_texture`, `gl_tex_env`, `gl_tex_gen` and `gl_load_texture_matrix`, so
the state they set joins the renderer's shadowed state block rather than being
poked in behind its back. The `create_full_screen_*_quad` functions build a
`GLVertexArray` from four `GLColourVertex` or `GLColourTextureVertex` corners
spanning clip space `[-1,1]` and compile it into a `GLCompiledDrawState` drawn as
`GL_QUADS`; the vertex array itself is then dropped, because the compiled draw
state holds shared references to the underlying buffers. This is how the backend
applies a texture across the whole of a render target.

`set_frustum_texture_state` is the projective-texturing primitive the cube
quad-tree raster path is built on. It enables object-linear texture coordinate
generation via `set_object_linear_tex_gen_state` — identity object planes for s,
t, r and q, so the generated coordinates are simply the vertex's own object-space
`(x,y,z,1)` — and then loads a texture matrix of clip-space-to-texture-space
times projection times view. The net effect is that a texture rendered through
one `GLCubeSubdivision` frustum can be looked up from geometry drawn through a
different one, which is what lets a raster tile, an age grid tile and a normal
map tile of different resolutions all be sampled by the same draw call.

The second kind is `QuadTreeClipSpaceTransform` and `QuadTreeUVTransform`, which
are pure arithmetic — no GL objects, no `GLRenderer`, nothing to release. They
answer the question "where does this quad-tree tile sit inside one of its
ancestors", in clip space `[-1,1]` and in texture space `[0,1]` respectively, and
in both directions; `QuadTreeUVTransform` delegates the actual quad-tree
bookkeeping to `QuadTreeClipSpaceTransform` and only re-bases the result into
`[0,1]`. The multi-resolution raster path needs this constantly because its
inputs are separate cube quad trees of differing depth: when one of them runs out
of resolution, `GLMultiResolutionStaticPolygonReconstructedRaster` keeps sampling
an ancestor's texture and folds the descendant's sub-rectangle into the texture
matrix with `inverse_transform`. `GLMultiResolutionCubeMesh` and
`GLMultiResolutionMapCubeMesh` use the clip-space form for the mirror-image case:
once traversal goes deeper than their pre-generated mesh quad tree they keep
reusing the ancestor's mesh drawable and start a non-identity clip-space
transform to clip it down to the current tile. `GLRasterCoRegistration` uses the
loose variants to place a seed frustum inside a raster frustum.

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

- `check_gl_errors` drains the error queue in a loop, so it clears any pending
  error for whoever calls next. On the first error it logs a `qWarning`, and in
  `GPLATES_DEBUG` builds it then calls `GPlatesGlobal::Abort` with the passed
  trace — every call site passes `GPLATES_ASSERTION_SOURCE`. It is deliberately
  only called after resource creation (texture allocation, buffer map/unmap,
  render-target construction) because `glGetError` is slow on some drivers; do
  not scatter it through per-frame code.
- `get_clip_space_to_texture_space_transform` returns a `const` reference to a
  function-local `static GLMatrix`, and that same call is the default argument of
  `set_frustum_texture_state`. Copy it before mutating, which is what
  `GLMultiResolutionStaticPolygonReconstructedRaster` does when it builds a tile
  texture matrix.
- `transform`, `loose_transform` and their inverses *post*-multiply the caller's
  matrix (`GLMatrix::gl_mult_matrix`), so in OpenGL order the last matrix
  multiplied in is the one applied to the vertex first. The established idiom is:
  start from an identity `GLMatrix`, apply the UV or clip-space transform, then
  post-multiply clip-to-texture, then the projection transform, then the view
  transform.
- The child constructor takes the parent transform but the resulting object is
  expressed relative to whatever node the *identity* transform was created at,
  not relative to the parent — scale doubles and the node offsets shift left by
  one and add the child offset at each level. To re-base a subtree you construct
  a fresh identity transform, as `GLMultiResolutionCubeMesh::get_child_node` does
  when it runs off the end of its pre-generated mesh tree. Note also that scale
  grows as `2^depth`, so the offsets are bounded by the quad-tree depth the
  caller is willing to descend.
- The `expand_tile_ratio` handed to these transforms must match the frustum
  expansion of the `GLCubeSubdivision` that produced the tiles.
  `get_expand_tile_ratio` is intentionally the same formula as
  `GLCubeSubdivision::get_expand_frustum_ratio`; if the two disagree, tile borders
  will not line up and bilinear filtering will show seams. `d_inverse_scale` and
  `d_inverse_expand_tile_ratio` are cached reciprocals kept only to avoid
  divisions — keep them consistent if you add state.
- Both transform classes are plain copyable values, cheap enough that
  `GLMultiResolutionStaticPolygonReconstructedRaster` allocates one per traversal
  node from a `boost::object_pool`, and safe to construct outside a render block.
  The `GLRenderer`-based helpers are not: they require an active renderer, and the
  quad builders each allocate a fresh vertex buffer, vertex element buffer and
  vertex array, so cache the returned `GLCompiledDrawState` rather than rebuilding
  it per frame.
- `set_object_linear_tex_gen_state` uses `GL_OBJECT_LINEAR`, which means texgen
  sees pre-modelview object-space positions; the view transform therefore has to
  be baked into the texture matrix by the caller. `set_frustum_texture_state`
  already does that, but a caller using the tex-gen helper on its own must.
- Everything these helpers configure — texture environment mode, texture
  coordinate generation, the texture matrix, `GL_QUADS` — is fixed-function
  state.

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
