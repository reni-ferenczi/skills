# GLNormalMapSource

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 165 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLNormalMapSource.h` | C++ | 385 |
| `src/opengl/GLNormalMapSource.cc` | C++ | 1306 |

## Overview

`GLNormalMapSource` is a `GLMultiResolutionRasterSource` that turns a floating-point scalar raster — a height field, or any other scalar field the user wants treated as one, such as gravity — into a tangent-space normal map for surface lighting. It is one of the tile sources a `GLMultiResolutionRaster` can be built from, alongside sources that hand back colour or age-mask tiles; `load_tile` fetches the source height data through a `GPlatesPropertyValues::ProxiedRasterResolver`, converts it, and returns the finished 8-bit RGBA normal texture (`GL_RGBA8`, x/y in the red/green channels, positive z in blue).

Normal generation can run on the GPU (`gpu_convert_height_field_to_normal_map`, using a small compiled shader program and a temporary floating-point height texture) or fall back to the CPU (`cpu_convert_height_field_to_normal_map`) when the runtime lacks floating-point non-power-of-two textures, `GL_EXT_framebuffer_object`, or fails to compile the generation shader; the constructor tests capabilities up front and downgrades `d_generate_normal_map_on_gpu` to false if shader creation fails. The height field is vertically exaggerated before differencing, combining a constant empirical factor, a factor derived from the raster's own min/max statistics, a factor derived from the raster's on-sphere resolution, and a caller-supplied `height_field_scale_factor`, all folded together in `get_height_field_scale`. `change_raster` lets a time-dependent raster with the same dimensions and georeferencing swap its underlying data without rebuilding the whole multi-resolution structure.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLNormalMapSource`](#gplatesopenglglnormalmapsource) | class | [`GLMultiResolutionRasterSource`](GLMultiResolutionRasterSource.md) | — | 0 | A raster source that converts a floating-point raster into a tangent-space normal map for surface lighting. |

## Members

### `GPlatesOpenGL::GLNormalMapSource`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLNormalMapSource>` | public | A convenience typedef for a shared pointer to a non-const GLNormalMapSource. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLNormalMapSource>` | public | A convenience typedef for a shared pointer to a const GLNormalMapSource. |
| `is_supported( GLRenderer &renderer)` | method | `bool` | public | Returns true if GLNormalMapSource is supported on the runtime system. |
| `create( GLRenderer &renderer, const GPlatesPropertyValues::RawRaster::non_null_ptr_type &height_field_raster, unsigned int tile_texel_dimension = DEFAULT_TILE_TEXEL_DIMENSION, float height_field_scale_factor = 1)` | method | `boost::optional<non_null_ptr_type>` | public | Creates a GLNormalMapSource object. tile\_texel\_dimension must be a power-of-two - it is the OpenGL square texture dimension to use for the tiled textures that represent the multi-resolution raster. |
| `change_raster( GLRenderer &renderer, const GPlatesPropertyValues::RawRaster::non_null_ptr_type &height_raster, float height_field_scale_factor = 1)` | method | `bool` | public | Change to a new (height) raster of the same dimensions as the current internal raster. height\_field\_scale\_factor is an adjustment to the internally determined height field scale based on the raster statistics (among other things). |
| `get_raster_width()` | method | `unsigned int` | public | — |
| `get_raster_height()` | method | `unsigned int` | public | — |
| `get_tile_texel_dimension()` | method | `unsigned int` | public | — |
| `get_target_texture_internal_format()` | method | `GLint` | public | — |
| `load_tile( unsigned int level, unsigned int texel_x_offset, unsigned int texel_y_offset, unsigned int texel_width, unsigned int texel_height, const GLTexture::shared_ptr_type &target_texture, GLRenderer &renderer)` | method | `cache_handle_type` | public | — |
| `set_max_highest_resolution_texel_size_on_unit_sphere( const double &max_highest_resolution_texel_size_on_unit_sphere)` | method | `void` | public | This is called by GLMultiResolutionRaster so that the normals in the highest resolution normal map can be scaled based on arc distance between two pixels. |
| `d_proxied_raster_resolver` | field | `GPlatesGlobal::PointerTraits<GPlatesPropertyValues::ProxiedRasterResolver>::non_null_ptr_type` | private | The proxied raster resolver to get floating-point (or integer) data (and coverage) from the raster. |
| `d_raster_width` | field | `unsigned int` | private | Original raster width. |
| `d_raster_height` | field | `unsigned int` | private | Original raster height. |
| `d_tile_texel_dimension` | field | `unsigned int` | private | The number of texels along a tiles edge (horizontal or vertical since it's square). |
| `d_constant_height_field_scale_factor` | field | `float` | private | The empirically determined constant height field scale factor that gives reasonable results for some test rasters. |
| `d_raster_statistics_height_field_scale_factor` | field | `float` | private | Height field scale factor based on the heightfield raster statistics (min/max). |
| `d_raster_resolution_height_field_scale_factor` | field | `float` | private | Height field scale factor based on the heightfield raster resolution (on the sphere). |
| `d_client_height_field_scale_factor` | field | `float` | private | Height field scale factor provided by the caller/client. |
| `d_generate_normal_map_on_gpu` | field | `bool` | private | If true then normals are generated on the GPU instead of CPU. |
| `d_level_of_detail_dimensions` | field | `std::vector< std::pair<unsigned int, unsigned int> >` | private | The dimensions of the different levels of detail. |
| `d_tile_height_data_working_space` | field | `boost::scoped_array<float>` | private | Used as temporary space for height data (and coverage). |
| `d_tile_normal_data_working_space` | field | `boost::scoped_array<GPlatesGui::rgba8_t>` | private | Used as temporary space for normal map data. |
| `d_height_field_texture_cache` | field | `GPlatesUtils::ObjectCache<GLTexture>::shared_ptr_type` | private | Used to allocate temporary height field textures when generating normals on the GPU. |
| `d_generate_normals_program_object` | field | `boost::optional<GLProgramObject::shared_ptr_type>` | private | Shader program to generate normals on the GPU. |
| `d_full_screen_quad_drawable` | field | `GLCompiledDrawState::non_null_ptr_to_const_type` | private | Used to draw a textured full-screen quad into render texture. |
| `d_logged_tile_load_failure_warning` | field | `bool` | private | We log a load-tile-failure warning message only once for each data raster source. |
| `GLNormalMapSource( GLRenderer &renderer, const GPlatesGlobal::PointerTraits<GPlatesPropertyValues::ProxiedRasterResolver>::non_null_ptr_type & proxy_raster_resolver, unsigned int raster_width, unsigned int raster_height, unsigned int tile_texel_dimension, const GPlatesPropertyValues::RasterStatistics &raster_statistics ...` | constructor | `None` | private | — |
| `initialise_level_of_detail_dimensions()` | method | `void` | private | — |
| `initialise_raster_statistics_height_field_scale_factor( const GPlatesPropertyValues::RasterStatistics &raster_statistics)` | method | `void` | private | — |
| `get_height_field_scale()` | method | `float` | private | Returns the height combined field scale combined from all the contributing scale factors. |
| `gpu_convert_height_field_to_normal_map( GLRenderer &renderer, const GLTexture::shared_ptr_type &target_texture, float lod_height_scale, unsigned int normal_map_texel_width, unsigned int normal_map_texel_height)` | method | `void` | private | — |
| `cpu_convert_height_field_to_normal_map( GLRenderer &renderer, const GLTexture::shared_ptr_type &target_texture, float lod_height_scale, unsigned int normal_map_texel_width, unsigned int normal_map_texel_height)` | method | `void` | private | — |
| `load_default_normal_map( unsigned int level, unsigned int texel_x_offset, unsigned int texel_y_offset, unsigned int texel_width, unsigned int texel_height, const GLTexture::shared_ptr_type &target_texture, GLRenderer &renderer)` | method | `void` | private | Emits warning to log and loads the default normal (0,0,1) into target texture. |
| `pack_height_data_into_tile_working_space( const GPlatesPropertyValues::RawRaster::non_null_ptr_type &src_raster_region, const GPlatesPropertyValues::CoverageRawRaster::non_null_ptr_type &src_raster_coverage, unsigned int src_texel_x_offset, unsigned int src_texel_y_offset, unsigned int src_texel_width, unsigned int src ...` | method | `bool` | private | Packs raster data/coverage values into target texture. |
| `pack_height_data_into_tile_working_space( const RealType *const src_region_data, const float *const src_coverage_data, unsigned int src_texel_x_offset, unsigned int src_texel_y_offset, unsigned int src_texel_width, unsigned int src_texel_height, unsigned int dst_texel_width, unsigned int dst_texel_height, GLRenderer &r ...` | method | `void` | private | Handles packing of data/coverage values where data is either 'float' or 'double'. |
| `create_normal_map_generation_shader_program( GLRenderer &renderer)` | method | `bool` | private | — |
| `create_height_tile_texture( GLRenderer &renderer, const GLTexture::shared_ptr_type &texture)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GENERATE_NORMAL_MAP_VERTEX_SHADER_SOURCE_FILE_NAME` | variable | `QString` | Vertex shader source to generate normals from a height field. |
| `GENERATE_NORMAL_MAP_FRAGMENT_SHADER_SOURCE_FILE_NAME` | variable | `QString` | Fragment shader source to generate normals from a height field. |
| `GPLATES_OPENGL_GLNORMALMAPSOURCE_H` | macro | `None` | — |

## Notes

- `create` returns `boost::none` (not an exception) if the raster is not a proxy raster, is uninitialised, holds colour RGBA pixels instead of numeric data, or `is_supported` fails — callers must check the optional rather than assume a normal map is always available.
- `change_raster` requires the new raster to have the same dimensions as the original; a resolution change instead requires building a whole new `GLNormalMapSource` (and, per the header, a georeferencing change instead requires a new `GLMultiResolutionRaster`).
- `is_supported` only requires vertex/fragment shader support for *this* class, since it can generate normals on the CPU; the header notes that shaders are nonetheless effectively required because normal maps are consumed by lighting code elsewhere that does need them.
- A tile-load failure logs a warning only once per source (`d_logged_tile_load_failure_warning`) before falling back to a flat default normal `(0,0,1)` via `load_default_normal_map`.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLMultiResolutionRaster](GLMultiResolutionRaster.md) | opengl | 18 |
| [opengl/GLVisualLayers](GLVisualLayers.md) | opengl | 6 |

## Related

**Shader programs compiled by this unit**

| Shader unit | Component |
|---|---|
| [shaders/normal_map_source](../qt-resources/opengl/normal_map_source.md) | shaders |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLNormalMapSource.h
python scripts/gpq.py def GPlatesOpenGL::GLNormalMapSource --body
python scripts/gpq.py uses GLNormalMapSource --kind class
python scripts/gpq.py hier GLNormalMapSource
```
