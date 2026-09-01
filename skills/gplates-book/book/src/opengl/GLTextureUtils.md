# GLTextureUtils

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 439 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLTextureUtils.h` | C++ | 425 |
| `src/opengl/GLTextureUtils.cc` | C++ | 566 |

## Overview

`GLTextureUtils` is a namespace of free functions that do the repetitive,
low-level parts of populating `GLTexture` objects, used throughout the raster
and mask sources in `opengl` (`GLDataRasterSource`, `GLVisualRasterSource`,
`GLAgeGridMaskSource`, `GLScalarFieldDepthLayersSource`, and others). The
`initialise_texture_object_*D` functions allocate a texture's storage
(`glTexImage*D`) without specifying image contents; the `load_*_into_*texture_2D`
and `fill_float_texture_2D` overloads then upload actual data with the faster
`glTexSubImage2D` path, either from a raw pointer, a `QImage`, a single fill
colour, or a `GLPixelBuffer` (for pixel-buffer-object-based asynchronous
uploads). Distinct overloads exist per source shape — 8-bit RGBA, floating
point with one to four components, `GL_ARB_texture_float` formats — so
callers don't have to work out `glTexSubImage2D` format/type arguments
themselves.

`create_xy_clip_texture_2D`, `create_z_clip_texture_2D` and
`get_clip_texture_clip_space_to_texture_space_transform` are a small,
self-contained group used to build clip textures: small textures whose
texel values gate rendering by shape (a lit square in the middle, or a
black/white ramp) rather than holding image data, together with the matrix
that maps clip-space coordinates into the interior region of the 4x4 xy-clip
texture.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLTEXTUREUTILS_H` | macro | `None` | — |
| `initialise_texture_object_1D( GLRenderer &renderer, const GLTexture::shared_ptr_type &texture_object, GLenum target, GLint internalformat, GLsizei width, GLint border, bool mipmapped)` | function | `void` | Initialises the specified texture object as a 1D texture matching the specified parameters. |
| `initialise_texture_object_2D( GLRenderer &renderer, const GLTexture::shared_ptr_type &texture_object, GLenum target, GLint internalformat, GLsizei width, GLsizei height, GLint border, bool mipmapped)` | function | `void` | Initialises the specified texture object as a 2D texture matching the specified parameters. |
| `initialise_texture_object_3D( GLRenderer &renderer, const GLTexture::shared_ptr_type &texture_object, GLenum target, GLint internalformat, GLsizei width, GLsizei height, GLsizei depth, GLint border, bool mipmapped)` | function | `void` | Initialises the specified texture object as a 3D texture matching the specified parameters. |
| `load_image_into_texture_2D( GLRenderer &renderer, const GLTexture::shared_ptr_type &texture, const void *image, GLenum format, GLenum type, unsigned int image_width, unsigned int image_height, unsigned int texel_u_offset = 0, unsigned int texel_v_offset = 0)` | function | `void` | Loads the specified image into the specified texture. |
| `load_image_into_texture_2D( GLRenderer &renderer, const GLTexture::shared_ptr_type &texture, const GLPixelBuffer::shared_ptr_to_const_type &pixels, GLint pixels_offset, GLenum format, GLenum type, unsigned int image_width, unsigned int image_height, unsigned int texel_u_offset = 0, unsigned int texel_v_offset = 0)` | function | `void` | Same as the other overload of load\_image\_into\_texture\_2D but loads image from a pixel buffer. |
| `load_image_into_rgba8_texture_2D( GLRenderer &renderer, const GLTexture::shared_ptr_type &texture, const void *image, unsigned int image_width, unsigned int image_height, unsigned int texel_u_offset = 0, unsigned int texel_v_offset = 0)` | function | `void` | Loads the specified image into the specified RGBA texture. image must contains 4-byte (R,G,B,A) colour values in that order. |
| `load_image_into_rgba8_texture_2D( GLRenderer &renderer, const GLTexture::shared_ptr_type &texture, const GLPixelBuffer::shared_ptr_to_const_type &pixels, GLint pixels_offset, unsigned int image_width, unsigned int image_height, unsigned int texel_u_offset = 0, unsigned int texel_v_offset = 0)` | function | `void` | Same as the other overload of load\_image\_into\_rgba8\_texture\_2D but loads image from a pixel buffer. |
| `load_image_into_rgba8_texture_2D( GLRenderer &renderer, const GLTexture::shared_ptr_type &texture, const GPlatesGui::rgba8_t *image, unsigned int image_width, unsigned int image_height, unsigned int texel_u_offset = 0, unsigned int texel_v_offset = 0)` | function | `void` | Loads the specified RGBA8 image into the specified RGBA texture. |
| `load_argb32_qimage_into_rgba8_texture_2D( GLRenderer &renderer, const GLTexture::shared_ptr_type &texture, const QImage &argb32_qimage, unsigned int texel_u_offset = 0, unsigned int texel_v_offset = 0)` | function | `void` | Loads the specified QImage, must be QImage::Format\_ARGB32, into the specified texture. |
| `load_colour_into_rgba8_texture_2D( GLRenderer &renderer, const GLTexture::shared_ptr_type &texture, const GPlatesGui::rgba8_t &colour, unsigned int texel_width, unsigned int texel_height, unsigned int texel_u_offset = 0, unsigned int texel_v_offset = 0)` | function | `void` | Loads the specified region of the RGBA8 texture with a single colour. |
| `load_colour_into_rgba32f_texture_2D( GLRenderer &renderer, const GLTexture::shared_ptr_type &texture, const GPlatesGui::Colour &colour, unsigned int texel_width, unsigned int texel_height, unsigned int texel_u_offset = 0, unsigned int texel_v_offset = 0)` | function | `void` | Loads the specified region of the RGBA32F \*float-point\* texture with a single colour. |
| `fill_float_texture_2D( GLRenderer &renderer, const GLTexture::shared_ptr_type &texture, const GLfloat fill_value, GLenum format, unsigned int texel_width, unsigned int texel_height, unsigned int texel_u_offset = 0, unsigned int texel_v_offset = 0)` | function | `void` | Loads the specified \*floating-point\* fill value into the specified \*floating-point\* texture. |
| `fill_float_texture_2D( GLRenderer &renderer, const GLTexture::shared_ptr_type &texture, const GLfloat first_fill_value, const GLfloat second_fill_value, GLenum format, unsigned int texel_width, unsigned int texel_height, unsigned int texel_u_offset = 0, unsigned int texel_v_offset = 0)` | function | `void` | Loads the specified \*floating-point\* fill values into the specified \*floating-point\* texture. |
| `fill_float_texture_2D( GLRenderer &renderer, const GLTexture::shared_ptr_type &texture, const GLfloat first_fill_value, const GLfloat second_fill_value, const GLfloat third_fill_value, GLenum format, unsigned int texel_width, unsigned int texel_height, unsigned int texel_u_offset = 0, unsigned int texel_v_offset = 0)` | function | `void` | Loads the specified \*floating-point\* fill values into the specified \*floating-point\* texture. |
| `fill_float_texture_2D( GLRenderer &renderer, const GLTexture::shared_ptr_type &texture, const GLfloat red_fill_value, const GLfloat green_fill_value, const GLfloat blue_fill_value, const GLfloat alpha_fill_value, unsigned int texel_width, unsigned int texel_height, unsigned int texel_u_offset = 0, unsigned int texel_v_ ...` | function | `void` | Loads the specified \*floating-point\* fill values into the specified \*floating-point\* texture. |
| `create_xy_clip_texture_2D( GLRenderer &renderer)` | function | `GLTexture::shared_ptr_type` | Creates a new 4x4 texel clip texture whose centre 2x2 texels are white with the remaining texels black (including alpha channel). |
| `create_z_clip_texture_2D( GLRenderer &renderer)` | function | `GLTexture::shared_ptr_type` | Creates a new 2x1 texel clip texture whose first texel is black and second texel white (including alpha channel). |
| `get_clip_texture_clip_space_to_texture_space_transform` | variable | `GLMatrix` | Initialise clip texture transform to convert the clip-space range \[-1, 1\] to range \[0.25, 0.75\] to map to the interior 2x2 texel region of the 4x4 clip texture. |

## Notes

- All the `load_*`/`fill_*` functions require the destination texture to
  already exist and be large enough (created via `initialise_texture_object_2D`
  or equivalent, or with existing content from a prior `glTexImage2D`) —
  they upload into a sub-region with `glTexSubImage2D` rather than allocate
  storage.
- `load_colour_into_rgba32f_texture_2D` and the four-value overload of
  `fill_float_texture_2D` require the `GL_ARB_texture_float` extension; the
  single/two/three-value `fill_float_texture_2D` overloads require a
  matching floating-point-friendly `format` (documented per overload) and
  the same extension.
- `load_image_into_texture_2D` temporarily sets `GL_UNPACK_ALIGNMENT` to 1
  (since texel rows aren't necessarily 4-byte aligned) and restores it to 4
  afterward, making raw `glPixelStorei` calls outside `GLRenderer`'s state
  tracking — a `FIXME` in the source flags this as something that should be
  routed through `GLRenderer` instead.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLDataRasterSource](GLDataRasterSource.md) | opengl | 13 |
| [opengl/GLNormalMapSource](GLNormalMapSource.md) | opengl | 11 |
| [opengl/GLVisualRasterSource](GLVisualRasterSource.md) | opengl | 11 |
| [opengl/GLAgeGridMaskSource](GLAgeGridMaskSource.md) | opengl | 9 |
| [opengl/GLScalarFieldDepthLayersSource](GLScalarFieldDepthLayersSource.md) | opengl | 9 |
| [opengl/GLContext](GLContext.md) | opengl | 7 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 5 |
| [opengl/GLMultiResolutionCubeMesh](GLMultiResolutionCubeMesh.md) | opengl | 4 |
| [opengl/GLMultiResolutionMapCubeMesh](GLMultiResolutionMapCubeMesh.md) | opengl | 4 |
| [opengl/GLMultiResolutionRasterMapView](GLMultiResolutionRasterMapView.md) | opengl | 4 |
| [opengl/GLFilledPolygonsGlobeView](GLFilledPolygonsGlobeView.md) | opengl | 1 |
| [opengl/GLMultiResolutionCubeRaster](GLMultiResolutionCubeRaster.md) | opengl | 1 |
| [opengl/GLMultiResolutionCubeReconstructedRaster](GLMultiResolutionCubeReconstructedRaster.md) | opengl | 1 |
| [opengl/GLMultiResolutionRaster](GLMultiResolutionRaster.md) | opengl | 1 |
| [opengl/GLMultiResolutionRasterSource](GLMultiResolutionRasterSource.md) | opengl | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLTextureUtils.h
```
