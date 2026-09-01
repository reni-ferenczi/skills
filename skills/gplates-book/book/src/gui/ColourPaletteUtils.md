# ColourPaletteUtils

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1076 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ColourPaletteUtils.h` | C++ | 190 |
| `src/gui/ColourPaletteUtils.cc` | C++ | 155 |

## Overview

[[[PROSE overview unit=gui/ColourPaletteUtils tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=gui/ColourPaletteUtils tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
