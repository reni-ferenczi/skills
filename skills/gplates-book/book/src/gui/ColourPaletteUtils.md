# ColourPaletteUtils

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1076 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ColourPaletteUtils.h` | C++ | 190 |
| `src/gui/ColourPaletteUtils.cc` | C++ | 155 |

## Overview

Free-function helpers layered on top of `ColourPalette` and the CPT readers
in `file-io`. `read_cpt_raster_colour_palette` loads a `.cpt` file and
returns it as a `RasterColourPalette`, choosing between the regular
(real-valued) and categorical (integer-valued) CPT formats — it first
attempts `RegularCptReader`, and only falls back to
`CategoricalCptReader<boost::int32_t>` (when `allow_integer_colour_palette`
is set) if the regular parse yields no `ColourSlice` entries; a real-valued
palette is preferred when the file is ambiguous, since it can also colour
integer-valued raster data whereas a categorical one cannot colour
real-valued data.

`get_range` (overloaded for `ColourPalette<PaletteKeyType>` and for
`RasterColourPalette`) extracts the numeric extent a palette covers, for
callers such as `ColourScaleGenerator` that need to draw a scale bar or
remap values. It is implemented via the private
`Implementation::RangeVisitor`, a `ConstColourPaletteVisitor` that knows how
to pull a range out of each concrete palette kind that has one
(`AgeColourPalette`, `RegularCptColourPalette`, the categorical CPT
palettes); palette kinds with no numeric range (or with no entries) leave
`d_range` unset and `get_range` returns `boost::none`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ColourPaletteUtils::Implementation::RangeVisitor`](#gplatesguicolourpaletteutilsimplementationrangevisitor) | class | [`ConstColourPaletteVisitor`](ColourPalette.md) | — | 0 | Extract the range of values covered by a colour palette, which is also returned, adapted into an integer colour palette. |

## Members

### `GPlatesGui::ColourPaletteUtils::Implementation::RangeVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `get_range()` | method | `boost::optional< std::pair<double, double> >` | public | — |
| `visit_age_colour_palette( const AgeColourPalette &colour_palette)` | method | `void` | public | — |
| `visit_int32_categorical_cpt_colour_palette( const CategoricalCptColourPalette<boost::int32_t> &colour_palette)` | method | `void` | public | — |
| `visit_uint32_categorical_cpt_colour_palette( const CategoricalCptColourPalette<boost::uint32_t> &colour_palette)` | method | `void` | public | — |
| `visit_regular_cpt_colour_palette( const RegularCptColourPalette &colour_palette)` | method | `void` | public | — |
| `d_range` | field | `boost::optional< std::pair<double, double> >` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_COLOURPALETTEUTILS_H` | macro | `None` | — |
| `read_cpt_raster_colour_palette( const QString &palette_file_name, bool allow_integer_colour_palette, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type` | Reads the specified palette file and returns a raster colour palette. |
| `get_range( const ColourPalette<PaletteKeyType> &colour_palette)` | function | `boost::optional< std::pair<double, double> >` | — |
| `get_range( const RasterColourPalette &raster_colour_palette)` | function | `boost::optional< std::pair<double, double> >` | — |

## Notes

A CPT file containing only "BFN" (background/foreground/NaN) lines and no
actual colour entries parses successfully under *both* the regular and
categorical readers, since that part of the syntax is shared; when
`read_cpt_raster_colour_palette` cannot otherwise tell which format was
intended, it resolves the ambiguity in favour of the regular (real-valued)
palette, and only returns a categorical palette when it parsed non-empty
categorical entries. Callers passing `allow_integer_colour_palette = false`
should not assume a returned palette is a real error indicator — check
`RasterColourPaletteType::get_type()` as the header notes, since an empty
`RasterColourPalette::create()` is also returned on read failure.

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/RemappedColourPaletteParameters](../presentation/RemappedColourPaletteParameters.md) | presentation | 7 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 7 |
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](../qt-widgets/TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 7 |
| [gui/BuiltinColourPalettes](BuiltinColourPalettes.md) | gui | 3 |
| [gui/ColourScaleGenerator](ColourScaleGenerator.md) | gui | 1 |
| [view-operations/ScalarField3DRenderParameters](../view-operations/ScalarField3DRenderParameters.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ColourPaletteUtils.h
python scripts/gpq.py def GPlatesGui::ColourPaletteUtils::Implementation::RangeVisitor --body
python scripts/gpq.py uses RangeVisitor --kind class
python scripts/gpq.py hier RangeVisitor
```
