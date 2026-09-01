# ColourRawRaster

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 674 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ColourRawRaster.h` | C++ | 383 |

## Overview

[[[PROSE overview unit=gui/ColourRawRaster tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ColourRawRaster::ColourRawRasterInternals::ColourPaletteFunctor`](#gplatesguicolourrawrastercolourrawrasterinternalscolourpalettefunctor) | class | — | `<class RawRasterType>` | 0 | This helper functor wraps around a ColourPalette. |
| [`GPlatesGui::ColourRawRaster::ColourRawRasterInternals::ColourRawRasterVisitorImpl`](#gplatesguicolourrawrastercolourrawrasterinternalscolourrawrastervisitorimpl) | class | — | `<typename T>` | 0 | Contains the logic of ColourRawRasterVisitor. |
| [`GPlatesGui::ColourRawRaster::ColourRawRasterInternals::ColourRawRasterVisitor`](#gplatesguicolourrawrastercolourrawrasterinternalscolourrawrastervisitor) | class | [`GPlatesPropertyValues::TemplatedRawRasterVisitor<ColourRawRasterVisitorImpl<T> >`](../property-values/RawRaster.md) | `<typename T>` | 0 | A visitor that attempts to colour a raster of unknown type. |
| [`GPlatesGui::ColourRawRaster::ColourRawRasterInternals::ColourRawRasterVisitorWithRasterColourPalette`](#gplatesguicolourrawrastercolourrawrasterinternalscolourrawrastervisitorwithrastercolourpalette) | class | `boost::static_visitor< boost::optional<GPlatesPropertyValues::Rgba8RawRaster::non_null_ptr_type> >` | — | 0 | — |

## Members

### `GPlatesGui::ColourRawRaster::ColourRawRasterInternals::ColourPaletteFunctor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `raster_element_type` | typedef | `typename RawRasterType::element_type` | public | — |
| `ColourPaletteFunctor( const RawRasterType &raster, const ColourPalette<raster_element_type> &colour_palette)` | constructor | `None` | public | — |
| `operator()( raster_element_type value)` | operator | `rgba8_t` | public | — |
| `d_raster` | field | `RawRasterType` | private | — |
| `d_colour_palette` | field | `ColourPalette<raster_element_type>` | private | — |

### `GPlatesGui::ColourRawRaster::ColourRawRasterInternals::ColourRawRasterVisitorImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ColourRawRasterVisitorImpl( const typename ColourPalette<T>::non_null_ptr_type &colour_palette)` | constructor | `None` | public | — |
| `coloured_raster()` | method | `boost::optional<GPlatesPropertyValues::Rgba8RawRaster::non_null_ptr_type>` | public | — |
| `ColourRawRaster` | class | `None` | private | — |
| `ColourRawRaster<RawRasterType, /* can_colour = */ true>` | class | `None` | private | — |
| `do_visit( RawRasterType &source)` | method | `void` | private | — |
| `d_colour_palette` | field | `typename ColourPalette<T>::non_null_ptr_type` | private | — |
| `d_coloured_raster` | field | `boost::optional<GPlatesPropertyValues::Rgba8RawRaster::non_null_ptr_type>` | private | — |

### `GPlatesGui::ColourRawRaster::ColourRawRasterInternals::ColourRawRasterVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `base_type` | typedef | `GPlatesPropertyValues::TemplatedRawRasterVisitor<ColourRawRasterVisitorImpl<T> >` | private | — |
| `ColourRawRasterVisitor( const typename ColourPalette<T>::non_null_ptr_type &colour_palette)` | constructor | `None` | public | — |

### `GPlatesGui::ColourRawRaster::ColourRawRasterInternals::ColourRawRasterVisitorWithRasterColourPalette`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ColourRawRasterVisitorWithRasterColourPalette( GPlatesPropertyValues::RawRaster &raster)` | constructor | `None` | public | — |
| `operator()( const RasterColourPalette::empty &)` | operator | `result_type` | public | — |
| `operator()( const GPlatesUtils::non_null_intrusive_ptr<ColourPaletteType> &colour_palette)` | operator | `result_type` | public | — |
| `d_raster` | field | `GPlatesPropertyValues::RawRaster` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_COLOURRAWRASTER_H` | macro | `None` | — |
| `TRANSPARENT_COLOUR` | variable | `rgba8_t` | — |
| `colour_raw_raster( RawRasterType &source, const typename ColourPalette<typename RawRasterType::element_type>::non_null_ptr_type &colour_palette)` | function | `GPlatesPropertyValues::Rgba8RawRaster::non_null_ptr_type` | Colours a RawRaster of type RawRasterType with the given colour\_palette, which must be of the correct type for the raster that you want to colour. |
| `colour_raw_raster( GPlatesPropertyValues::Rgba8RawRaster &source, const ColourPalette<rgba8_t>::non_null_ptr_type &palette)` | function | `GPlatesPropertyValues::Rgba8RawRaster::non_null_ptr_type` | — |
| `colour_raw_raster( GPlatesPropertyValues::RawRaster &source, const typename ColourPalette<T>::non_null_ptr_type &colour_palette)` | function | `boost::optional<GPlatesPropertyValues::Rgba8RawRaster::non_null_ptr_type>` | Colours a RawRaster, without knowing which specific derivation it is. |
| `colour_raw_raster_with_raster_colour_palette( GPlatesPropertyValues::RawRaster &source, const GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type &colour_palette)` | function | `boost::optional<GPlatesPropertyValues::Rgba8RawRaster::non_null_ptr_type>` | Colours a RawRaster using a RasterColourPalette. |

## Notes

[[[PROSE notes unit=gui/ColourRawRaster tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/MipmappedRasterFormatWriter](../file-io/MipmappedRasterFormatWriter.md) | file-io | 5 |
| [property-values/ProxiedRasterResolver](../property-values/ProxiedRasterResolver.md) | property-values | 5 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ColourRawRaster.h
python scripts/gpq.py def GPlatesGui::ColourRawRaster::ColourRawRasterInternals::ColourRawRasterVisitorImpl --body
python scripts/gpq.py uses ColourRawRasterVisitorImpl --kind class
python scripts/gpq.py hier ColourRawRasterVisitorImpl
```
