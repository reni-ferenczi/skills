# RasterVisualLayerParams

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 782 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/RasterVisualLayerParams.h` | C++ | 214 |
| `src/presentation/RasterVisualLayerParams.cc` | C++ | 160 |

## Overview

[[[PROSE overview unit=presentation/RasterVisualLayerParams tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPresentation::RasterVisualLayerParams`](#gplatespresentationrastervisuallayerparams) | class | [`VisualLayerParams`](VisualLayerParams.md) | — | 0 | — |

## Members

### `GPlatesPresentation::RasterVisualLayerParams`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<RasterVisualLayerParams>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const RasterVisualLayerParams>` | public | — |
| `create( GPlatesAppLogic::LayerParams::non_null_ptr_type layer_params)` | method | `non_null_ptr_type` | public | — |
| `accept_visitor( ConstVisualLayerParamsVisitor &visitor)` | method | `void` | public | Override of virtual method in VisualLayerParams base. |
| `accept_visitor( VisualLayerParamsVisitor &visitor)` | method | `void` | public | Override of virtual method in VisualLayerParams base. |
| `handle_layer_modified( const GPlatesAppLogic::Layer &layer)` | method | `void` | public | Override of virtual method in VisualLayerParams base. |
| `create_default_colour_palette_parameters()` | method | `GPlatesPresentation::RemappedColourPaletteParameters` | public | The default colour palette parameters. |
| `set_colour_palette_parameters( const GPlatesPresentation::RemappedColourPaletteParameters &colour_palette_parameters)` | method | `void` | public | Sets the current colour palette. |
| `get_raster_type()` | method | `GPlatesPropertyValues::RasterType::Type` | public | Returns the type of the raster as an enumeration. |
| `set_opacity( const double &opacity)` | method | `void` | public | Sets the opacity of the raster. |
| `get_opacity()` | method | `double` | public | Gets the opacity of the raster. |
| `set_intensity( const double &intensity)` | method | `void` | public | Sets the intensity of the raster. |
| `get_intensity()` | method | `double` | public | Gets the intensity of the raster. |
| `get_modulate_colour()` | method | `GPlatesGui::Colour` | public | Returns the raster modulate colour. |
| `set_surface_relief_scale( float surface_relief_scale)` | method | `void` | public | Sets the height field scale factor adjustment to use for normal map. |
| `get_surface_relief_scale()` | method | `float` | public | Gets the height field scale factor adjustment to use for normal map. |
| `RasterVisualLayerParams( GPlatesAppLogic::LayerParams::non_null_ptr_type layer_params)` | constructor | `None` | protected | — |
| `d_colour_palette_parameters_initialised_from_raster` | field | `bool` | private | — |
| `d_colour_palette_parameters` | field | `GPlatesPresentation::RemappedColourPaletteParameters` | private | The current colour palette for this layer, whether set explicitly as loaded from a file, or auto-generated. |
| `d_raster_type` | field | `GPlatesPropertyValues::RasterType::Type` | private | The type of raster the last time we examined it. |
| `d_opacity` | field | `double` | private | The opacity of the raster in the range \[0,1\]. |
| `d_intensity` | field | `double` | private | The intensity of the raster in the range \[0,1\]. |
| `d_surface_relief_scale` | field | `float` | private | Gets the height field scale factor adjustment to use for normal map. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PRESENTATION_RASTERVISUALLAYERPARAMS_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=presentation/RasterVisualLayerParams tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/RasterLayerOptionsWidget](../qt-widgets/RasterLayerOptionsWidget.md) | qt-widgets | 45 |
| [presentation/TranscribeSession](TranscribeSession.md) | presentation | 11 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 5 |
| [presentation/ReconstructionGeometryRenderer](ReconstructionGeometryRenderer.md) | presentation | 4 |
| [presentation/VisualLayerRegistry](VisualLayerRegistry.md) | presentation | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/presentation/RasterVisualLayerParams.h
python scripts/gpq.py def GPlatesPresentation::RasterVisualLayerParams --body
python scripts/gpq.py uses RasterVisualLayerParams --kind class
python scripts/gpq.py hier RasterVisualLayerParams
```
