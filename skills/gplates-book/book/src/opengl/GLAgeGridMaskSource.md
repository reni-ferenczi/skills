# GLAgeGridMaskSource

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 234 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLAgeGridMaskSource.h` | C++ | 404 |
| `src/opengl/GLAgeGridMaskSource.cc` | C++ | 885 |

## Overview

`GLAgeGridMaskSource` is a `GLMultiResolutionRasterSource` that turns an age grid raster into a per-tile mask showing which sea-floor pixels are older than the current reconstruction time. Rather than storing one mask raster per reconstruction time, it re-derives the mask on the GPU whenever `update_reconstruction_time` reports a change, so a single age grid raster can drive the mask at any time in the animation.

Because fixed-function OpenGL has no 16-bit integer comparison, the age values and the reconstruction time are each split into a high and low byte and encoded into two 8-bit textures (`d_age_high_byte_tile_working_space` / `d_age_low_byte_tile_working_space`, converted via `convert_age_to_16_bit_integer`). `load_tile` then drives three render passes (`d_first_render_pass_state`, `d_second_render_pass_state`, `d_third_render_pass_state`, compiled once and replayed per tile) that compare the byte pairs and combine the results with the `GL_ARB_texture_env_dot3` extension to produce a single RGBA8 mask texture: the mask value replicated into RGB, and the age grid's coverage (valid-data) flag in alpha.

Age data itself comes from a `ProxiedRasterResolver` over the supplied age grid raster, so tiles are decoded on demand rather than the whole raster being loaded up front.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLAgeGridMaskSource`](#gplatesopenglglagegridmasksource) | class | [`GLMultiResolutionRasterSource`](GLMultiResolutionRasterSource.md) | — | 0 | An age grid mask raster that generates a mask for a specific reconstruction time. |

## Members

### `GPlatesOpenGL::GLAgeGridMaskSource`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLAgeGridMaskSource>` | public | A convenience typedef for a shared pointer to a non-const GLAgeGridMaskSource. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLAgeGridMaskSource>` | public | A convenience typedef for a shared pointer to a const GLAgeGridMaskSource. |
| `create( GLRenderer &renderer, const double &reconstruction_time, const GPlatesPropertyValues::RawRaster::non_null_ptr_type &age_grid_raster, unsigned int tile_texel_dimension = DEFAULT_TILE_TEXEL_DIMENSION)` | method | `boost::optional<non_null_ptr_type>` | public | Creates a GLAgeGridMaskSource object. tile\_texel\_dimension must be a power-of-two - it is the OpenGL square texture dimension to use for the tiled textures that represent the multi-resolution raster. |
| `get_raster_width()` | method | `unsigned int` | public | — |
| `get_raster_height()` | method | `unsigned int` | public | — |
| `get_tile_texel_dimension()` | method | `unsigned int` | public | — |
| `get_target_texture_internal_format()` | method | `GLint` | public | — |
| `load_tile( unsigned int level, unsigned int texel_x_offset, unsigned int texel_y_offset, unsigned int texel_width, unsigned int texel_height, const GLTexture::shared_ptr_type &target_texture, GLRenderer &renderer)` | method | `cache_handle_type` | public | — |
| `update_reconstruction_time( const double &reconstruction_time)` | method | `void` | public | Updates the reconstruction time - if it's changed since the last call then this source will invalidate itself and cause any connected clients to refresh their texture caches. |
| `Tile` | class | `None` | private | — |
| `tile_seq_type` | typedef | `std::vector<Tile>` | private | — |
| `LevelOfDetail` | class | `None` | private | — |
| `level_of_detail_seq_type` | typedef | `std::vector<LevelOfDetail::non_null_ptr_type>` | private | — |
| `d_current_reconstruction_time` | field | `GPlatesMaths::real_t` | private | The current reconstruction time determines whether to update the age grid mask. |
| `d_proxied_raster_resolver` | field | `GPlatesGlobal::PointerTraits<GPlatesPropertyValues::ProxiedRasterResolver>::non_null_ptr_type` | private | The proxied raster resolver to get region/level float-point data from the age grid raster. |
| `d_raster_width` | field | `unsigned int` | private | Original raster width. |
| `d_raster_height` | field | `unsigned int` | private | Original raster height. |
| `d_tile_texel_dimension` | field | `unsigned int` | private | The number of texels along a tiles edge (horizontal or vertical since it's square). |
| `d_age_grid_texture_cache` | field | `GPlatesUtils::ObjectCache<GLTexture>::shared_ptr_type` | private | Texture cache for the actual floating-point age values read from a proxied raster. |
| `d_intermediate_render_texture_cache` | field | `GPlatesUtils::ObjectCache<GLTexture>::shared_ptr_type` | private | Used for render textures to store intermediate results. |
| `d_levels` | field | `level_of_detail_seq_type` | private | The cached textures across the different levels of detail. |
| `d_full_screen_quad_drawable` | field | `GLCompiledDrawState::non_null_ptr_to_const_type` | private | Used to draw a textured full-screen quad into render texture. |
| `d_first_render_pass_state` | field | `GLCompiledDrawState::non_null_ptr_type` | private | The states used for each of the three render passes required to render an age grid mask. |
| `d_second_render_pass_state` | field | `GLCompiledDrawState::non_null_ptr_type` | private | — |
| `d_third_render_pass_state` | field | `GLCompiledDrawState::non_null_ptr_type` | private | — |
| `d_raster_min_age` | field | `float` | private | The minimum and maximum age grid values in the raster. |
| `d_raster_max_age` | field | `float` | private | — |
| `d_raster_inv_age_range_factor` | field | `float` | private | — |
| `d_current_reconstruction_time_high_byte` | field | `boost::uint8_t` | private | The current reconstruction time translated/scaled to a 16-bit unsigned integer where 0 is min age and 2^16 - 1 is max age. |
| `d_current_reconstruction_time_low_byte` | field | `boost::uint8_t` | private | — |
| `d_age_high_byte_tile_working_space` | field | `boost::scoped_array<GPlatesGui::rgba8_t>` | private | — |
| `d_age_low_byte_tile_working_space` | field | `boost::scoped_array<GPlatesGui::rgba8_t>` | private | — |
| `d_logged_tile_load_failure_warning` | field | `bool` | private | We log a load-tile-failure warning message only once for each coverage source. |
| `GLAgeGridMaskSource( GLRenderer &renderer, const double &reconstruction_time, const GPlatesGlobal::PointerTraits<GPlatesPropertyValues::ProxiedRasterResolver>::non_null_ptr_type & proxy_raster_resolver, unsigned int raster_width, unsigned int raster_height, unsigned int tile_texel_dimension, double min_age_in_raster, d ...` | constructor | `None` | private | — |
| `initialise_level_of_detail_pyramid()` | method | `void` | private | — |
| `get_tile` | field | `Tile` | private | — |
| `should_reload_high_and_low_byte_age_textures( GLRenderer &renderer, Tile &tile, GLTexture::shared_ptr_type &high_byte_age_texture, GLTexture::shared_ptr_type &low_byte_age_texture)` | method | `bool` | private | — |
| `load_age_grid_into_high_and_low_byte_tile( GLRenderer &renderer, const GPlatesPropertyValues::RawRaster::non_null_ptr_type &age_grid_age_tile, const GPlatesPropertyValues::CoverageRawRaster::non_null_ptr_type &age_grid_coverage_tile, GLTexture::shared_ptr_type &high_byte_age_texture, GLTexture::shared_ptr_type &low_byt ...` | method | `bool` | private | — |
| `load_age_grid_into_high_and_low_byte_tile( GLRenderer &renderer, const RealType *age_grid_age_tile, const float *age_grid_coverage_tile, GLTexture::shared_ptr_type &high_byte_age_texture, GLTexture::shared_ptr_type &low_byte_age_texture, unsigned int texel_width, unsigned int texel_height)` | method | `void` | private | — |
| `render_age_grid_mask( GLRenderer &renderer, const GLTexture::shared_ptr_type &target_texture, const GLTexture::shared_ptr_type &high_byte_age_texture, const GLTexture::shared_ptr_type &low_byte_age_texture)` | method | `void` | private | — |
| `render_age_grid_intermediate_mask( GLRenderer &renderer, const GLTexture::shared_ptr_type &intermediate_texture, const GLTexture::shared_ptr_type &high_byte_age_texture, const GLTexture::shared_ptr_type &low_byte_age_texture)` | method | `void` | private | — |
| `create_tile_texture( GLRenderer &renderer, const GLTexture::shared_ptr_type &texture)` | method | `void` | private | — |
| `convert_age_to_16_bit_integer( float age, boost::uint8_t &age_high_byte, boost::uint8_t &age_low_byte)` | method | `void` | private | Converts a floating-point age to a 16-bit unsigned integer. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `create_dot3_extract_red_channel()` | function | `std::vector<GLfloat>` | A 4-component texture environment colour used to extract red channel when used with GL\_ARB\_texture\_env\_dot3. |
| `GPLATES_OPENGL_GLAGEGRIDMASKSOURCE_H` | macro | `None` | — |

## Notes

- `create` returns `boost::none` (rather than throwing) if the supplied raster is not a proxied, numeric raster, or is uninitialised — callers must check the `boost::optional` before use.
- `tile_texel_dimension` must be a power of two and is silently clamped to the run-time system's maximum texture size.
- A tile-load failure is logged only once per source (`d_logged_tile_load_failure_warning`), so repeated failures for the same source do not flood the log.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/RasterLayerProxy](../app-logic/RasterLayerProxy.md) | app-logic | 34 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 32 |
| [qt-widgets/ImportRasterDialog](../qt-widgets/ImportRasterDialog.md) | qt-widgets | 8 |
| [opengl/GLVisualLayers](GLVisualLayers.md) | opengl | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLAgeGridMaskSource.h
python scripts/gpq.py def GPlatesOpenGL::GLAgeGridMaskSource --body
python scripts/gpq.py uses GLAgeGridMaskSource --kind class
python scripts/gpq.py hier GLAgeGridMaskSource
```
