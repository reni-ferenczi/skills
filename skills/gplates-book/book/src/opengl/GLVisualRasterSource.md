# GLVisualRasterSource

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 332 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLVisualRasterSource.h` | C++ | 394 |
| `src/opengl/GLVisualRasterSource.cc` | C++ | 756 |

## Overview

[[[PROSE overview unit=opengl/GLVisualRasterSource tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLVisualRasterSource`](#gplatesopenglglvisualrastersource) | class | [`GLMultiResolutionRasterSource`](GLMultiResolutionRasterSource.md) | — | 0 | An arbitrary dimension source of fixed-point RGBA8 data made accessible by a proxied raster. |

## Members

### `GPlatesOpenGL::GLVisualRasterSource`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLVisualRasterSource>` | public | A convenience typedef for a shared pointer to a non-const GLVisualRasterSource. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLVisualRasterSource>` | public | A convenience typedef for a shared pointer to a const GLVisualRasterSource. |
| `create( GLRenderer &renderer, const GPlatesPropertyValues::RawRaster::non_null_ptr_type &raster, const GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type &raster_colour_palette, const GPlatesGui::Colour &raster_modulate_colour = GPlatesGui::Colour::get_white(), unsigned int tile_texel_dimension = DEFAULT_TILE_ ...` | method | `boost::optional<non_null_ptr_type>` | public | Creates a GLVisualRasterSource object. tile\_texel\_dimension must be a power-of-two - it is the OpenGL square texture dimension to use for the tiled textures that represent the multi-resolution raster. |
| `change_raster( GLRenderer &renderer, const GPlatesPropertyValues::RawRaster::non_null_ptr_type &raster, const GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type &raster_colour_palette)` | method | `bool` | public | Change to a new raster of the same dimensions as the current internal raster. |
| `change_modulate_colour( GLRenderer &renderer, const GPlatesGui::Colour &raster_modulate_colour)` | method | `void` | public | Change the colour to modulate the raster texture with. |
| `get_raster_width()` | method | `unsigned int` | public | — |
| `get_raster_height()` | method | `unsigned int` | public | — |
| `get_tile_texel_dimension()` | method | `unsigned int` | public | — |
| `get_target_texture_internal_format()` | method | `GLint` | public | — |
| `load_tile( unsigned int level, unsigned int texel_x_offset, unsigned int texel_y_offset, unsigned int texel_width, unsigned int texel_height, const GLTexture::shared_ptr_type &target_texture, GLRenderer &renderer)` | method | `cache_handle_type` | public | — |
| `Tile` | class | `None` | private | — |
| `tile_seq_type` | typedef | `std::vector<Tile>` | private | — |
| `LevelOfDetail` | class | `None` | private | — |
| `level_of_detail_seq_type` | typedef | `std::vector<LevelOfDetail::non_null_ptr_type>` | private | — |
| `d_proxied_raster_resolver` | field | `GPlatesGlobal::PointerTraits<GPlatesPropertyValues::ProxiedRasterResolver>::non_null_ptr_type` | private | The proxied raster resolver to get region/level data from raster and optionally converted to RGBA (using d\_raster\_colour\_palette). |
| `d_raster_colour_palette` | field | `GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type` | private | The colour palette used to convert non-RGBA raster data to RGBA. |
| `d_raster_width` | field | `unsigned int` | private | Original raster width. |
| `d_raster_height` | field | `unsigned int` | private | Original raster height. |
| `d_tile_texel_dimension` | field | `unsigned int` | private | The number of texels along a tiles edge (horizontal or vertical since it's square). |
| `d_raster_texture_cache` | field | `GPlatesUtils::ObjectCache<GLTexture>::shared_ptr_type` | private | Used for allocating temporary textures when modulating a raster tile with a colour. |
| `d_raster_data_subject_token` | field | `GPlatesUtils::SubjectToken` | private | Keeps track of changes to the raster data itself (the data sourced from the proxied raster resolver). |
| `d_levels` | field | `level_of_detail_seq_type` | private | The cached source textures across the different levels of detail. |
| `d_raster_modulate_colour` | field | `GPlatesGui::Colour` | private | The colour used to modulate the raster texture with - the default is white (1,1,1,1). |
| `d_full_screen_quad_drawable` | field | `GLCompiledDrawState::non_null_ptr_to_const_type` | private | Used to draw a coloured full-screen quad into render texture (for colour modulation of raster). |
| `d_tile_edge_working_space` | field | `boost::scoped_array<GPlatesGui::rgba8_t>` | private | Uses as temporary space to duplicate a tile's vertical or horizontal edge when the data in the tile does not consume the full d\_tile\_texel\_dimension x d\_tile\_texel\_dimension area. |
| `d_error_text_image_level_zero` | field | `QImage` | private | Images containing error messages when fail to load proxied raster tiles. |
| `d_error_text_image_mipmap_levels` | field | `QImage` | private | — |
| `d_logged_tile_load_failure_warning` | field | `bool` | private | We log a load-tile-failure warning message only once for each raster source. |
| `GLVisualRasterSource( GLRenderer &renderer, const GPlatesGlobal::PointerTraits<GPlatesPropertyValues::ProxiedRasterResolver>::non_null_ptr_type & proxy_raster_resolver, const GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type &raster_colour_palette, const GPlatesGui::Colour &raster_modulate_colour, unsigned in ...` | constructor | `None` | private | — |
| `initialise_level_of_detail_pyramid()` | method | `void` | private | — |
| `get_tile` | field | `Tile` | private | — |
| `load_proxied_raster_data_into_raster_texture( unsigned int level, unsigned int texel_x_offset, unsigned int texel_y_offset, unsigned int texel_width, unsigned int texel_height, const GLTexture::shared_ptr_type &raster_texture, Tile &tile, GLRenderer &renderer)` | method | `void` | private | — |
| `render_error_text_into_texture( unsigned int level, unsigned int texel_x_offset, unsigned int texel_y_offset, unsigned int texel_width, unsigned int texel_height, const GLTexture::shared_ptr_type &texture, GLRenderer &renderer)` | method | `void` | private | — |
| `write_raster_texture_into_tile_target_texture( GLRenderer &renderer, const GLTexture::shared_ptr_type &target_texture, const GLTexture::shared_ptr_type &raster_texture)` | method | `void` | private | — |
| `create_tile_texture( GLRenderer &renderer, const GLTexture::shared_ptr_type &texture)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `RASTER_CACHE_SIZE_FACTOR` | variable | `float` | The minimum number of textures in the raster cache, before any recycling can happen, is the number of objects in use in the cache multiplied by this factor. |
| `GPLATES_OPENGL_GLVISUALRASTERSOURCE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLVisualRasterSource tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLVisualLayers](GLVisualLayers.md) | opengl | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLVisualRasterSource.h
python scripts/gpq.py def GPlatesOpenGL::GLVisualRasterSource --body
python scripts/gpq.py uses GLVisualRasterSource --kind class
python scripts/gpq.py hier GLVisualRasterSource
```
