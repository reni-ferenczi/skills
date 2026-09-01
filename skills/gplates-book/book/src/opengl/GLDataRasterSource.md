# GLDataRasterSource

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 464 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLDataRasterSource.h` | C++ | 262 |
| `src/opengl/GLDataRasterSource.cc` | C++ | 656 |

## Overview

[[[PROSE overview unit=opengl/GLDataRasterSource tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=opengl/GLDataRasterSource tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
