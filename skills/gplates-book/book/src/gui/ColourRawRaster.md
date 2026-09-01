# ColourRawRaster

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 674 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ColourRawRaster.h` | C++ | 383 |

## Overview

This header turns a numeric `RawRaster` into a displayable `Rgba8RawRaster` by running every pixel through a `ColourPalette`. The primary `colour_raw_raster` overload is templated on the concrete raster type and does the actual pixel loop: for each value it checks `is_no_data_value`, looks the value up in the palette with `get_colour`, and writes either the resulting `Colour` (converted with `Colour::to_rgba8`) or a fully transparent `rgba8_t` into a freshly allocated destination buffer. The straightforward `std::transform` version is kept under `#if 0` next to a hand-unrolled loop, because profiling showed this inner loop hot enough to warrant it.

The remaining machinery exists to erase the raster's concrete type at the call site. `ColourRawRasterVisitorImpl` (via `TemplatedRawRasterVisitor`) double-dispatches onto whichever `RawRaster` subclass is actually present, and its nested `ColourRawRaster<RawRasterType, can_colour>` partial specialization uses a compile-time boolean — true only when the raster has data, has a no-data value, and its element type is compatible with the palette's key type (integral rasters always qualify; floating-point rasters only pair with a floating-point palette) — to select between doing the conversion and doing nothing. `colour_raw_raster_with_raster_colour_palette` then uses `boost::static_visitor` over the `RasterColourPalette` variant so callers holding a type-erased palette (the common case) don't need to know the palette's key type either.

The explicit specialization for `Rgba8RawRaster` is deliberately left undefined: an RGBA raster is already colour, and any attempt to instantiate it is a compile-time or link-time error rather than a silent no-op.

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

- A colour palette that returns `boost::none` for a value, and any no-data value, both map to fully transparent output rather than a visible colour or an error.
- Instantiating `colour_raw_raster<GPlatesPropertyValues::Rgba8RawRaster>` fails to link on purpose; the function template is declared but never defined for that raster type.
- `colour_raw_raster_with_raster_colour_palette` returns `boost::none` outright when the `RasterColourPalette` variant holds `RasterColourPalette::empty`.

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
