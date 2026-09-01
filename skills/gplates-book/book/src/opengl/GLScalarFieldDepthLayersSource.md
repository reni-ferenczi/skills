# GLScalarFieldDepthLayersSource

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 533 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLScalarFieldDepthLayersSource.h` | C++ | 332 |
| `src/opengl/GLScalarFieldDepthLayersSource.cc` | C++ | 1135 |

## Overview

[[[PROSE overview unit=opengl/GLScalarFieldDepthLayersSource tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLScalarFieldDepthLayersSource`](#gplatesopenglglscalarfielddepthlayerssource) | class | [`GLMultiResolutionRasterSource`](GLMultiResolutionRasterSource.md) | — | 0 | A raster source that contains depth layers for generating the scalar values and gradients for a 3D scalar field. |

## Members

### `GPlatesOpenGL::GLScalarFieldDepthLayersSource`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLScalarFieldDepthLayersSource>` | public | A convenience typedef for a shared pointer to a non-const GLScalarFieldDepthLayersSource. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLScalarFieldDepthLayersSource>` | public | A convenience typedef for a shared pointer to a const GLScalarFieldDepthLayersSource. |
| `DepthLayer` | struct | `None` | public | A single depth layer contributing to the 3D scalar field. |
| `depth_layer_seq_type` | typedef | `std::vector<DepthLayer>` | public | Typedef for a sequence of depth layers. |
| `is_supported( GLRenderer &renderer)` | method | `bool` | public | Returns true if GLScalarFieldDepthLayersSource is supported on the runtime system. |
| `create( GLRenderer &renderer, const depth_layer_seq_type &depth_layers, unsigned int tile_texel_dimension = DEFAULT_TILE_TEXEL_DIMENSION)` | method | `boost::optional<non_null_ptr_type>` | public | Creates a GLScalarFieldDepthLayersSource object from the specified depth layer rasters. tile\_texel\_dimension must be a power-of-two - it is the OpenGL square texture dimension to use for the tiled textures that represent the ... |
| `set_depth_layer( GLRenderer &renderer, unsigned int depth_layer_index)` | method | `void` | public | Sets the current depth layer that the output scalar values and gradients are generated from. depth\_layer\_index is the index into the depth layers passed into create. |
| `get_raster_width()` | method | `unsigned int` | public | — |
| `get_raster_height()` | method | `unsigned int` | public | — |
| `get_tile_texel_dimension()` | method | `unsigned int` | public | — |
| `get_target_texture_internal_format()` | method | `GLint` | public | — |
| `load_tile( unsigned int level, unsigned int texel_x_offset, unsigned int texel_y_offset, unsigned int texel_width, unsigned int texel_height, const GLTexture::shared_ptr_type &target_texture, GLRenderer &renderer)` | method | `cache_handle_type` | public | — |
| `ProxiedDepthLayer` | struct | `None` | private | A single depth layer with a proxied raw raster resolver to access the scalar field values. |
| `proxied_depth_layer_seq_type` | typedef | `std::vector<ProxiedDepthLayer>` | private | Typedef for a sequence of proxied depth layer raster resolvers. |
| `d_proxied_depth_layers` | field | `proxied_depth_layer_seq_type` | private | The proxied raster resolvers to get floating-point (or integer) data (and coverage) from the depth layers. |
| `d_raster_width` | field | `unsigned int` | private | Raster width. |
| `d_raster_height` | field | `unsigned int` | private | Raster height. |
| `d_num_depth_layers` | field | `unsigned int` | private | Number of depth layers. |
| `d_tile_texel_dimension` | field | `unsigned int` | private | The number of texels along a tiles edge (horizontal or vertical since it's square). |
| `d_level_of_detail_dimensions` | field | `std::vector< std::pair<unsigned int, unsigned int> >` | private | The dimensions of the different levels of detail. |
| `d_tile_scalar_data_working_space` | field | `boost::scoped_array<float>` | private | Used as temporary space for scalar data (and coverage). |
| `d_tile_scalar_gradient_data_working_space` | field | `boost::scoped_array<float>` | private | Used as temporary space for scalar+gradient data. |
| `d_tile_edge_working_space` | field | `boost::scoped_array<float>` | private | Used as temporary space to duplicate a tile's vertical or horizontal edge when the data in the tile does not consume the full d\_tile\_texel\_dimension x d\_tile\_texel\_dimension area. |
| `d_logged_tile_load_failure_warning` | field | `bool` | private | We log a load-tile-failure warning message only once for each data raster source. |
| `d_current_depth_layer_index` | field | `unsigned int` | private | The current depth layer we are using as a source. |
| `GLScalarFieldDepthLayersSource( GLRenderer &renderer, const proxied_depth_layer_seq_type &proxied_depth_layers, unsigned int raster_width, unsigned int raster_height, unsigned int tile_texel_dimension)` | constructor | `None` | private | — |
| `initialise_level_of_detail_dimensions()` | method | `void` | private | — |
| `generate_scalar_gradient_values( GLRenderer &renderer, const GLTexture::shared_ptr_type &target_texture, unsigned int texel_width, unsigned int texel_height, float depth_layer_radius[3], bool working_space_layer_loaded[3])` | method | `void` | private | — |
| `load_depth_layer_into_tile_working_space( GPlatesPropertyValues::ProxiedRasterResolver &proxied_depth_layer_resolver, unsigned int working_space_layer_index, unsigned int level, unsigned int src_scalar_map_texel_x_offset, unsigned int src_scalar_map_texel_y_offset, unsigned int src_scalar_map_texel_width, unsigned int ...` | method | `bool` | private | — |
| `load_default_scalar_gradient_values( unsigned int level, unsigned int texel_x_offset, unsigned int texel_y_offset, unsigned int texel_width, unsigned int texel_height, const GLTexture::shared_ptr_type &target_texture, GLRenderer &renderer)` | method | `void` | private | — |
| `pack_scalar_data_into_tile_working_space( const RealType *const src_region_data, const float *const src_coverage_data, unsigned int working_space_layer_index, unsigned int src_texel_x_offset, unsigned int src_texel_y_offset, unsigned int src_texel_width, unsigned int src_texel_height, unsigned int dst_texel_width, unsi ...` | method | `void` | private | — |
| `pack_scalar_data_into_tile_working_space( const GPlatesPropertyValues::RawRaster::non_null_ptr_type &src_raster_region, const GPlatesPropertyValues::CoverageRawRaster::non_null_ptr_type &src_raster_coverage, unsigned int working_space_layer_index, unsigned int src_texel_x_offset, unsigned int src_texel_y_offset, unsign ...` | method | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLSCALARFIELDDEPTHLAYERSSOURCE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLScalarFieldDepthLayersSource tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLScalarField3DGenerator](GLScalarField3DGenerator.md) | opengl | 12 |
| [opengl/GLMultiResolutionRaster](GLMultiResolutionRaster.md) | opengl | 7 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLScalarFieldDepthLayersSource.h
python scripts/gpq.py def GPlatesOpenGL::GLScalarFieldDepthLayersSource --body
python scripts/gpq.py uses GLScalarFieldDepthLayersSource --kind class
python scripts/gpq.py hier GLScalarFieldDepthLayersSource
```
