# ColourPaletteRangeRemapper

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 712 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ColourPaletteRangeRemapper.h` | C++ | 273 |

## Overview

Provides functions to remap the value ranges of colour palettes. The `remap_colour_palette_range()` functions take a source palette and new lower/upper bounds, then scale and translate each colour slice in the palette to fit the new range. The module uses visitor pattern: `RangeRemapperVisitor` handles regular CPT palettes and `RasterColourPaletteRangeRemapperVisitor` handles raster palettes. Currently, only `RegularCptColourPalette` is fully supported; other types return none.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ColourPaletteRangeRemapperInternals::RangeRemapperVisitor`](#gplatesguicolourpaletterangeremapperinternalsrangeremappervisitor) | class | [`ConstColourPaletteVisitor`](ColourPalette.md) | — | 0 | — |
| [`GPlatesGui::ColourPaletteRangeRemapperInternals::RasterColourPaletteRangeRemapperVisitor`](#gplatesguicolourpaletterangeremapperinternalsrastercolourpaletterangeremappervisitor) | class | `boost::static_visitor< boost::optional<ColourPalette<double>::non_null_ptr_type> >` | — | 0 | — |

## Members

### `GPlatesGui::ColourPaletteRangeRemapperInternals::RangeRemapperVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RangeRemapperVisitor( const double &remapped_lower_bound, const double &remapped_upper_bound)` | constructor | `None` | public | — |
| `get_remapped_colour_palette()` | method | `boost::optional<ColourPalette<double>::non_null_ptr_type>` | public | — |
| `visit_regular_cpt_colour_palette( const RegularCptColourPalette &colour_palette)` | method | `void` | public | — |
| `d_remapped_lower_bound` | field | `double` | private | — |
| `d_remapped_upper_bound` | field | `double` | private | — |
| `d_remapped_colour_palette` | field | `boost::optional<ColourPalette<double>::non_null_ptr_type>` | private | — |
| `generate_remapped_colour_palette( const boost::optional<Colour> &background_colour, const boost::optional<Colour> &foreground_colour, const boost::optional<Colour> &nan_colour, double lower_bound, double upper_bound, const std::vector<ColourSlice> &colour_slices)` | method | `void` | private | — |

### `GPlatesGui::ColourPaletteRangeRemapperInternals::RasterColourPaletteRangeRemapperVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RasterColourPaletteRangeRemapperVisitor( const double &remapped_lower_bound, const double &remapped_upper_bound)` | constructor | `None` | public | — |
| `operator()( const GPlatesGui::RasterColourPalette::empty &)` | operator | `boost::optional<ColourPalette<double>::non_null_ptr_type>` | public | — |
| `operator()( const GPlatesUtils::non_null_intrusive_ptr<ColourPaletteType> &colour_palette)` | operator | `boost::optional<ColourPalette<double>::non_null_ptr_type>` | public | — |
| `d_remapped_lower_bound` | field | `double` | private | — |
| `d_remapped_upper_bound` | field | `double` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_COLOURPALETTERANGEREMAPPER_H` | macro | `None` | — |
| `get_double_value( double d)` | function | `double` | — |
| `get_double_value( GPlatesMaths::Real r)` | function | `double` | — |
| `remap_colour_palette_range( const GPlatesUtils::non_null_intrusive_ptr< ColourPalette<KeyType> > &colour_palette, const double &remapped_lower_bound, const double &remapped_upper_bound)` | function | `boost::optional<ColourPalette<double>::non_null_ptr_type>` | — |
| `remap_colour_palette_range( const RasterColourPalette::non_null_ptr_to_const_type &colour_palette, const double &remapped_lower_bound, const double &remapped_upper_bound)` | function | `boost::optional<ColourPalette<double>::non_null_ptr_type>` | — |

## Notes

The helper function `get_double_value()` handles conversion from both `double` and `GPlatesMaths::Real` to enable templated implementations over different key types.

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/RemappedColourPaletteParameters](../presentation/RemappedColourPaletteParameters.md) | presentation | 2 |
| [view-operations/ScalarField3DRenderParameters](../view-operations/ScalarField3DRenderParameters.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ColourPaletteRangeRemapper.h
python scripts/gpq.py def GPlatesGui::ColourPaletteRangeRemapperInternals::RangeRemapperVisitor --body
python scripts/gpq.py uses RangeRemapperVisitor --kind class
python scripts/gpq.py hier RangeRemapperVisitor
```
