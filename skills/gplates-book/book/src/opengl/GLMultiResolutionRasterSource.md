# GLMultiResolutionRasterSource

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 1465 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLMultiResolutionRasterSource.h` | C++ | 244 |

## Overview

[[[PROSE overview unit=opengl/GLMultiResolutionRasterSource tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=opengl/GLMultiResolutionRasterSource tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
