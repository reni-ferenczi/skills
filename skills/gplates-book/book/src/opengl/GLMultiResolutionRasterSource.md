# GLMultiResolutionRasterSource

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 1465 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLMultiResolutionRasterSource.h` | C++ | 244 |

## Overview

`GLMultiResolutionRasterSource` is the pluggable-source interface behind `GLMultiResolutionRaster`: the raster itself handles tiling, level-of-detail selection and caching generically, while a `GLMultiResolutionRasterSource` implementation (`GLAgeGridMaskSource`, `GLDataRasterSource`, `GLNormalMapSource`, `GLScalarFieldDepthLayersSource`, `GLVisualRasterSource`, and others) supplies the actual texel data for a requested tile via `load_tile()`. This separation is what lets the same multi-resolution tiling and rendering machinery serve plain colour rasters, data (floating-point) rasters, age-grid masks, normal maps and scalar-field depth layers without duplicating the tiling logic in each.

`load_tile()`'s contract constrains callers and implementations symmetrically: `texel_x_offset`/`texel_y_offset` are always multiples of `get_tile_texel_dimension()`, so a source never has to handle a load crossing a tile boundary, and `texel_width`/`texel_height` are at most the tile dimension, only falling short at the raster's bottom-right edge. `invalidate()` lets a derived source announce that all previously loaded tiles are stale — its documented triggers are a new raster, a new colour scheme, or a reconstruction-time change that alters age-grid mask data — and clients watch this through the inherited `get_subject_token()`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLMultiResolutionRasterSource`](#gplatesopenglglmultiresolutionrastersource) | class | [`GPlatesUtils::ReferenceCount<GLMultiResolutionRasterSource>`](../utils/ReferenceCount.md) | — | 5 | Interface for an arbitrary dimension source of raster data that's used as input to a GLMultiResolutionRaster. |

## Members

### `GPlatesOpenGL::GLMultiResolutionRasterSource`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLMultiResolutionRasterSource>` | public | A convenience typedef for a shared pointer to a non-const GLMultiResolutionRasterSource. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLMultiResolutionRasterSource>` | public | A convenience typedef for a shared pointer to a const GLMultiResolutionRasterSource. |
| `cache_handle_type` | typedef | `boost::shared_ptr<void>` | public | Typedef for an opaque tile cache handle. |
| `DEFAULT_TILE_TEXEL_DIMENSION` | field | `unsigned int` | public | The default tile dimension is 256. |
| `~GLMultiResolutionRasterSource()` | destructor | `None` | public | — |
| `get_raster_width()` | method | `unsigned int` | public | — |
| `get_raster_height()` | method | `unsigned int` | public | — |
| `get_tile_texel_dimension()` | method | `unsigned int` | public | The requests to load\_tile \*must\* have texel offsets that are integer multiples of this tile dimension. |
| `get_target_texture_internal_format()` | method | `GLint` | public | Returns the texture internal format for the target textures passed to load\_tile (to store a tile's texture data). |
| `load_tile( unsigned int level, unsigned int texel_x_offset, unsigned int texel_y_offset, unsigned int texel_width, unsigned int texel_height, const GLTexture::shared_ptr_type &target_texture, GLRenderer &renderer)` | method | `cache_handle_type` | public | (you can pass NULL to gl\_tex\_image\_2D to create without loading image data). renderer is provided in case the data needs to be rendered into the texture. texel\_x\_offset and texel\_y\_offset are guaranteed to be a multiple of the tile texel ... |
| `GLMultiResolutionRasterSource()` | constructor | `None` | protected | — |
| `invalidate()` | method | `void` | protected | Used by derived classes to signal that the entire source data has changed - such as a new raster or a new colour scheme or a change in reconstruction time resulting in new age grid mask data. |
| `d_subject_token` | field | `GPlatesUtils::SubjectToken` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLMULTIRESOLUTIONRASTERSOURCE_H` | macro | `None` | — |

## Notes

`get_target_texture_internal_format()` textures are expected to use nearest-neighbour filtering in all cases: this best matches a raster's georeferencing, and older hardware supporting floating-point textures cannot bilinearly filter them anyway (any smoothing must be emulated in a shader by the client). Mipmap auto-generation is deliberately not used — a header comment explains it caused problems when the source is a GPU-rendered target (such as an age-grid mask) rather than a CPU-loaded texture, interacting badly with framebuffer-object mipmap support, and it is unnecessary anyway since resolution is already selected via the proxied raster's own mipmapped tiles, with anisotropic filtering handling aliasing near the horizon.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLMultiResolutionRaster](GLMultiResolutionRaster.md) | opengl | 13 |
| [opengl/GLAgeGridMaskSource](GLAgeGridMaskSource.md) | opengl | 9 |
| [opengl/GLDataRasterSource](GLDataRasterSource.md) | opengl | 9 |
| [opengl/GLNormalMapSource](GLNormalMapSource.md) | opengl | 9 |
| [opengl/GLScalarFieldDepthLayersSource](GLScalarFieldDepthLayersSource.md) | opengl | 8 |
| [opengl/GLVisualRasterSource](GLVisualRasterSource.md) | opengl | 8 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 6 |
| [app-logic/RasterLayerProxy](../app-logic/RasterLayerProxy.md) | app-logic | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLMultiResolutionRasterSource.h
python scripts/gpq.py def GPlatesOpenGL::GLMultiResolutionRasterSource --body
python scripts/gpq.py uses GLMultiResolutionRasterSource --kind class
python scripts/gpq.py hier GLMultiResolutionRasterSource
```
