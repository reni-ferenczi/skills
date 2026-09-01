# ExportRasterAnimationStrategy

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 447 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ExportRasterAnimationStrategy.h` | C++ | 162 |
| `src/gui/ExportRasterAnimationStrategy.cc` | C++ | 1503 |

## Overview

[[[PROSE overview unit=gui/ExportRasterAnimationStrategy tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::raster_visual_layer_seq_type`](#anonymousraster_visual_layer_seq_type) | typedef | — | — | 0 | Typedef for sequence of raster visual layer. |
| [`(anonymous)::ColourRaster`](#anonymouscolourraster) | struct | — | — | 0 | Information about a colour raster. |
| [`(anonymous)::colour_raster_seq_type`](#anonymouscolour_raster_seq_type) | typedef | — | — | 0 | Typedef for a sequence of (reconstructed) colour rasters. |
| [`(anonymous)::NumericalRaster`](#anonymousnumericalraster) | struct | — | — | 0 | Information about a numerical raster and its bands. |
| [`(anonymous)::numerical_raster_seq_type`](#anonymousnumerical_raster_seq_type) | typedef | — | — | 0 | Typedef for a sequence of (reconstructed) numerical rasters. |
| [`GPlatesGui::ExportRasterAnimationStrategy`](#gplatesguiexportrasteranimationstrategy) | class | `QObject`<br>[`GPlatesGui::ExportAnimationStrategy`](ExportAnimationStrategy.md) | — | 0 | Concrete implementation of the ExportAnimationStrategy class for saving (colour or numerical) raster data (unwrapped to latitude/longitude) to a file at each timestep. |

## Members

### `(anonymous)::raster_visual_layer_seq_type`

*None.*

### `(anonymous)::ColourRaster`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ColourRaster( const QString &layer_name_, const GPlatesAppLogic::ResolvedRaster::non_null_ptr_to_const_type &resolved_raster_, const GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type &raster_colour_palette_, const GPlatesGui::Colour &raster_modulate_colour_, float surface_relief_scale_)` | constructor | `None` | public | — |
| `layer_name` | field | `QString` | public | The name of the raster (visual) layer. |
| `resolved_raster` | field | `GPlatesAppLogic::ResolvedRaster::non_null_ptr_to_const_type` | public | The information needed to render a raster as colours (using GLVisualLayers to render). |
| `raster_colour_palette` | field | `GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type` | public | — |
| `raster_modulate_colour` | field | `GPlatesGui::Colour` | public | — |
| `surface_relief_scale` | field | `float` | public | — |

### `(anonymous)::colour_raster_seq_type`

*None.*

### `(anonymous)::NumericalRaster`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Band` | struct | `None` | public | — |
| `NumericalRaster( const QString &layer_name_, const GPlatesAppLogic::RasterLayerProxy::non_null_ptr_type &layer_proxy_, const std::vector<Band> &numerical_bands_)` | constructor | `None` | public | — |
| `layer_name` | field | `QString` | public | The name of the raster (visual) layer. |
| `layer_proxy` | field | `GPlatesAppLogic::RasterLayerProxy::non_null_ptr_type` | public | The layer proxy to get the raster band data from. |
| `numerical_bands` | field | `std::vector<Band>` | public | Only the bands containing numerical (non-colour) data. |

### `(anonymous)::numerical_raster_seq_type`

*None.*

### `GPlatesGui::ExportRasterAnimationStrategy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ExportRasterAnimationStrategy>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<ExportRasterAnimationStrategy\>. |
| `Configuration` | class | `None` | public | Configuration options. |
| `const_configuration_ptr` | typedef | `boost::shared_ptr<const Configuration>` | public | Typedef for a shared pointer to const Configuration. |
| `create( ExportAnimationContext &export_animation_context, const const_configuration_ptr &export_configuration)` | method | `non_null_ptr_type` | public | — |
| `~ExportRasterAnimationStrategy()` | destructor | `None` | public | — |
| `do_export_iteration( std::size_t frame_index)` | method | `bool` | public | Does one frame of export. |
| `ExportRasterAnimationStrategy( GPlatesGui::ExportAnimationContext &export_animation_context, const const_configuration_ptr &export_configuration)` | constructor | `None` | protected | Protected constructor to prevent instantiation on the stack. |
| `d_configuration` | field | `const_configuration_ptr` | private | Export configuration parameters. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `substitute_placeholder( const QString &output_filebasename, const QString &placeholder, const QString &placeholder_replacement)` | function | `QString` | — |
| `calculate_output_basename( const QString &output_filename_prefix, const QString &layer_name)` | function | `QString` | — |
| `get_visible_raster_visual_layers( raster_visual_layer_seq_type &visible_raster_visual_layers, GPlatesPresentation::ViewState &view_state)` | function | `void` | Get the visible raster layers. |
| `get_visible_colour_rasters( GPlatesOpenGL::GLRenderer &renderer, GPlatesPresentation::ViewState &view_state, colour_raster_seq_type &colour_rasters)` | function | `void` | Get the all rasters from the set of visible layers. |
| `get_visible_numerical_rasters( GPlatesOpenGL::GLRenderer &renderer, GPlatesPresentation::ViewState &view_state, numerical_raster_seq_type &numerical_rasters)` | function | `void` | Get the rasters containing numerical bands from the set of visible layers. |
| `get_export_raster_projection_and_parameters( const GPlatesGui::ExportRasterAnimationStrategy::Configuration &configuration, unsigned int &raster_width, unsigned int &raster_height, GPlatesPropertyValues::Georeferencing::lat_lon_extents_type &lat_lon_extents)` | function | `GPlatesGui::MapProjection::non_null_ptr_type` | Determines the raster map projection and calculates the export raster dimensions from resolution and lat/lon extents. |
| `create_gl_renderer( GPlatesGui::ExportAnimationContext &export_animation_context)` | function | `GPlatesOpenGL::GLRenderer::non_null_ptr_type` | — |
| `setup_tile_for_rendering( const unsigned int export_raster_width, const unsigned int export_raster_height, const bool export_raster_grid_line_registration, const GPlatesPropertyValues::Georeferencing::lat_lon_extents_type &pixel_rendering_lat_lon_extents, GPlatesOpenGL::GLRenderer &renderer, GPlatesOpenGL::GLTileRender ...` | function | `void` | Setup a tile for rendering. |
| `read_colour_tile_data( GPlatesOpenGL::GLRenderer &renderer, const GPlatesOpenGL::GLPixelBuffer::shared_ptr_type &tile_pixel_buffer, const unsigned int tile_width, const unsigned int tile_height)` | function | `GPlatesPropertyValues::Rgba8RawRaster::non_null_ptr_type` | Reads coloured tile data and returns as an RGBA8 raw raster. |
| `read_numerical_band_tile_data( GPlatesOpenGL::GLRenderer &renderer, const GPlatesOpenGL::GLPixelBuffer::shared_ptr_type &tile_pixel_buffer, const unsigned int tile_width, const unsigned int tile_height)` | function | `GPlatesPropertyValues::FloatRawRaster::non_null_ptr_type` | Reads a numerical band's tile data and returns as a float raw raster. |
| `export_colour_raster( const ColourRaster &raster, const QString &filename, const unsigned int export_raster_width, const unsigned int export_raster_height, const bool export_raster_grid_line_registration, const bool export_raster_compress, const GPlatesPropertyValues::Georeferencing::non_null_ptr_type &georeferencing, ...` | function | `void` | — |
| `export_numerical_raster_band( const GPlatesOpenGL::GLMultiResolutionCubeRasterInterface::non_null_ptr_type &band_data, const unsigned int raster_band_index, const unsigned int export_raster_width, const unsigned int export_raster_height, const bool export_raster_grid_line_registration, const GPlatesPropertyValues::Geor ...` | function | `void` | — |
| `export_numerical_raster( const NumericalRaster &raster, const QString &filename, const unsigned int export_raster_width, const unsigned int export_raster_height, const bool export_raster_grid_line_registration, const bool export_raster_compress, const GPlatesPropertyValues::Georeferencing::non_null_ptr_type &georeferen ...` | function | `void` | — |
| `GPLATES_GUI_EXPORTRASTERANIMATIONSTRATEGY_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/ExportRasterAnimationStrategy tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ExportRasterOptionsWidget](../qt-widgets/ExportRasterOptionsWidget.md) | qt-widgets | 54 |
| [gui/ExportAnimationRegistry](ExportAnimationRegistry.md) | gui | 15 |
| [opengl/GLVisualLayers](../opengl/GLVisualLayers.md) | opengl | 3 |
| [file-io/GdalRasterWriter](../file-io/GdalRasterWriter.md) | file-io | 1 |
| [file-io/RasterWriter](../file-io/RasterWriter.md) | file-io | 1 |
| [file-io/RgbaRasterWriter](../file-io/RgbaRasterWriter.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ExportRasterAnimationStrategy.h
python scripts/gpq.py def GPlatesGui::ExportRasterAnimationStrategy --body
python scripts/gpq.py uses ExportRasterAnimationStrategy --kind class
python scripts/gpq.py hier ExportRasterAnimationStrategy
```
