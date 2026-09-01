# GLDataRasterSource

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 464 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLDataRasterSource.h` | C++ | 262 |
| `src/opengl/GLDataRasterSource.cc` | C++ | 656 |

## Overview

`GLDataRasterSource` is the `GLMultiResolutionRasterSource` used when raster values are needed for numerical analysis rather than display — it loads floating-point (or integer) raster data through a `ProxiedRasterResolver` and packs it, unmodified, into a floating-point texture: the raw value in the red channel, the raster's per-pixel coverage (how much of that pixel is not the sentinel/no-data value) in green. This contrasts with `GLVisualRasterSource`, which applies a colour palette to turn the same kind of data into an RGBA8 colour for rendering; `GLDataRasterSource` does no such conversion, so consumers such as `GLRasterCoRegistration` see the source raster's actual numbers.

It requires the `GL_ARB_texture_float` extension (checked via `is_supported`) and prefers the two-channel `GL_RG32F` format over `GL_RGBA32F_ARB` when `GL_ARB_texture_rg` is also available, halving texture memory since only the red and green channels are ever used. `change_raster` lets a time-dependent raster series that shares georeferencing and dimensions swap its underlying data without rebuilding the whole `GLMultiResolutionRaster` pyramid; a dimension change instead requires constructing a new source.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLDataRasterSource`](#gplatesopenglgldatarastersource) | class | [`GLMultiResolutionRasterSource`](GLMultiResolutionRasterSource.md) | — | 0 | An arbitrary dimension source of floating-point data made accessible by a proxied raster. |

## Members

### `GPlatesOpenGL::GLDataRasterSource`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLDataRasterSource>` | public | A convenience typedef for a shared pointer to a non-const GLDataRasterSource. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLDataRasterSource>` | public | A convenience typedef for a shared pointer to a const GLDataRasterSource. |
| `is_supported( GLRenderer &renderer)` | method | `bool` | public | Returns true if GLDataRasterSource is supported on the runtime system. |
| `create( GLRenderer &renderer, const GPlatesPropertyValues::RawRaster::non_null_ptr_type &data_raster, unsigned int tile_texel_dimension = DEFAULT_TILE_TEXEL_DIMENSION)` | method | `boost::optional<non_null_ptr_type>` | public | Creates a GLDataRasterSource object. tile\_texel\_dimension must be a power-of-two - it is the OpenGL square texture dimension to use for the tiled textures that represent the multi-resolution raster. |
| `change_raster( GLRenderer &renderer, const GPlatesPropertyValues::RawRaster::non_null_ptr_type &data_raster)` | method | `bool` | public | Change to a new data raster of the same dimensions as the current internal raster. |
| `get_raster_width()` | method | `unsigned int` | public | — |
| `get_raster_height()` | method | `unsigned int` | public | — |
| `get_tile_texel_dimension()` | method | `unsigned int` | public | — |
| `get_target_texture_internal_format()` | method | `GLint` | public | — |
| `load_tile( unsigned int level, unsigned int texel_x_offset, unsigned int texel_y_offset, unsigned int texel_width, unsigned int texel_height, const GLTexture::shared_ptr_type &target_texture, GLRenderer &renderer)` | method | `cache_handle_type` | public | — |
| `d_proxied_raster_resolver` | field | `GPlatesGlobal::PointerTraits<GPlatesPropertyValues::ProxiedRasterResolver>::non_null_ptr_type` | private | The proxied raster resolver to get floating-point (or integer) data (and coverage) from the raster. |
| `d_raster_width` | field | `unsigned int` | private | Original raster width. |
| `d_raster_height` | field | `unsigned int` | private | Original raster height. |
| `d_tile_texture_internal_format` | field | `GLint` | private | Texture internal format of tile textures. |
| `d_tile_texel_dimension` | field | `unsigned int` | private | The number of texels along a tiles edge (horizontal or vertical since it's square). |
| `d_tile_pack_working_space` | field | `boost::scoped_array<float>` | private | Used as temporary space to pack data and coverage into red/green channels before loading texture. |
| `d_tile_edge_working_space` | field | `boost::scoped_array<float>` | private | Used as temporary space to duplicate a tile's vertical or horizontal edge when the data in the tile does not consume the full d\_tile\_texel\_dimension x d\_tile\_texel\_dimension area. |
| `d_logged_tile_load_failure_warning` | field | `bool` | private | We log a load-tile-failure warning message only once for each data raster source. |
| `GLDataRasterSource( GLRenderer &renderer, const GPlatesGlobal::PointerTraits<GPlatesPropertyValues::ProxiedRasterResolver>::non_null_ptr_type & proxy_raster_resolver, unsigned int raster_width, unsigned int raster_height, unsigned int tile_texel_dimension)` | constructor | `None` | private | — |
| `handle_error_loading_source_raster( unsigned int level, unsigned int texel_x_offset, unsigned int texel_y_offset, unsigned int texel_width, unsigned int texel_height, const GLTexture::shared_ptr_type &target_texture, GLRenderer &renderer)` | method | `void` | private | Emits warning to log and loads zero data/coverage values into target texture. |
| `pack_raster_data_into_tile_working_space( const GPlatesPropertyValues::RawRaster::non_null_ptr_type &raster_region, const GPlatesPropertyValues::CoverageRawRaster::non_null_ptr_type &raster_coverage, unsigned int texel_width, unsigned int texel_height, GLRenderer &renderer)` | method | `bool` | private | Packs raster data/coverage values into target texture. |
| `pack_raster_data_into_tile_working_space( const RealType *const region_data, const float *const coverage_data, unsigned int texel_width, unsigned int texel_height, GLRenderer &renderer)` | method | `void` | private | Handles packing of data/coverage values where data is either 'float' or 'double'. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLDATARASTERSOURCE_H` | macro | `None` | — |

## Notes

- `create` returns `boost::none` if the raster is not a proxied numeric raster, is uninitialised, or `is_supported` fails — always check the `boost::optional` result.
- `change_raster` returns `false`, without changing anything, if the new raster's dimensions differ from the current one; the caller must build a new `GLDataRasterSource` in that case. It cannot be used to change georeferencing alone — that requires a new `GLMultiResolutionRaster`.
- A tile-load failure is logged only once per source (`d_logged_tile_load_failure_warning`) and the tile is filled with zero data/coverage instead, so a persistently failing raster will not repeatedly spam the log.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/RasterLayerProxy](../app-logic/RasterLayerProxy.md) | app-logic | 9 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 5 |
| [opengl/GLRasterCoRegistration](GLRasterCoRegistration.md) | opengl | 2 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLDataRasterSource.h
python scripts/gpq.py def GPlatesOpenGL::GLDataRasterSource --body
python scripts/gpq.py uses GLDataRasterSource --kind class
python scripts/gpq.py hier GLDataRasterSource
```
