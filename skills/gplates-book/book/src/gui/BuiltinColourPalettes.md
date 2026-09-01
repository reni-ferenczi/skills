# BuiltinColourPalettes

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 391 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/BuiltinColourPalettes.h` | C++ | 469 |
| `src/gui/BuiltinColourPalettes.cc` | C++ | 1862 |

## Overview

[[[PROSE overview unit=gui/BuiltinColourPalettes tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::BuiltinColourPalettes::(anonymous)::InvertPaletteVisitor`](#gplatesguibuiltincolourpalettesanonymousinvertpalettevisitor) | class | [`ConstColourPaletteVisitor`](ColourPalette.md) | — | 0 | Palette visitor to return a new palette with inverted colours. |
| [`GPlatesGui::BuiltinColourPalettes::Age::Type`](#gplatesguibuiltincolourpalettesagetype) | enum | — | — | 0 | — |
| [`GPlatesGui::BuiltinColourPalettes::Topography::Type`](#gplatesguibuiltincolourpalettestopographytype) | enum | — | — | 0 | — |
| [`GPlatesGui::BuiltinColourPalettes::SCM::Type`](#gplatesguibuiltincolourpalettesscmtype) | enum | — | — | 0 | — |
| [`GPlatesGui::BuiltinColourPalettes::ColorBrewer::Sequential::Type`](#gplatesguibuiltincolourpalettescolorbrewersequentialtype) | enum | — | — | 0 | ColorBrewer sequential palette types. |
| [`GPlatesGui::BuiltinColourPalettes::ColorBrewer::Sequential::Classes`](#gplatesguibuiltincolourpalettescolorbrewersequentialclasses) | enum | — | — | 0 | There are between 3 and 9 classes available in ColorBrewer sequential palette types. |
| [`GPlatesGui::BuiltinColourPalettes::ColorBrewer::Diverging::Type`](#gplatesguibuiltincolourpalettescolorbrewerdivergingtype) | enum | — | — | 0 | ColorBrewer diverging palette types. |
| [`GPlatesGui::BuiltinColourPalettes::ColorBrewer::Diverging::Classes`](#gplatesguibuiltincolourpalettescolorbrewerdivergingclasses) | enum | — | — | 0 | There are between 3 and 11 classes available in ColorBrewer diverging palette types. |

## Members

### `GPlatesGui::BuiltinColourPalettes::(anonymous)::InvertPaletteVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `get_inverted_colour_palette()` | method | `boost::optional<ColourPalette<double>::non_null_ptr_type>` | public | — |
| `visit_regular_cpt_colour_palette( const RegularCptColourPalette &colour_palette)` | method | `void` | public | — |
| `d_inverted_colour_palette` | field | `boost::optional<ColourPalette<double>::non_null_ptr_type>` | private | — |
| `generate_inverted_colour_palette( const RegularCptColourPalette &colour_palette)` | method | `void` | private | — |

### `GPlatesGui::BuiltinColourPalettes::Age::Type`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Legacy` | enumerator | `None` | — | — |
| `Traditional` | enumerator | `None` | — | — |
| `Modern` | enumerator | `None` | — | — |

### `GPlatesGui::BuiltinColourPalettes::Topography::Type`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Etopo1` | enumerator | `None` | — | — |
| `Geo` | enumerator | `None` | — | — |
| `Relief` | enumerator | `None` | — | — |

### `GPlatesGui::BuiltinColourPalettes::SCM::Type`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Batlow` | enumerator | `None` | — | Sequential... |
| `Hawaii` | enumerator | `None` | — | — |
| `Oslo` | enumerator | `None` | — | — |
| `Lapaz` | enumerator | `None` | — | — |
| `Lajolla` | enumerator | `None` | — | — |
| `Buda` | enumerator | `None` | — | — |
| `Davos` | enumerator | `None` | — | — |
| `Tokyo` | enumerator | `None` | — | — |
| `Vik` | enumerator | `None` | — | Diverging... |
| `Roma` | enumerator | `None` | — | — |
| `Broc` | enumerator | `None` | — | — |
| `Berlin` | enumerator | `None` | — | — |
| `Lisbon` | enumerator | `None` | — | — |
| `Bam` | enumerator | `None` | — | — |
| `Oleron` | enumerator | `None` | — | Multi-sequential... |
| `Bukavu` | enumerator | `None` | — | — |

### `GPlatesGui::BuiltinColourPalettes::ColorBrewer::Sequential::Type`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `OrRd` | enumerator | `None` | — | — |
| `PuBu` | enumerator | `None` | — | — |
| `BuPu` | enumerator | `None` | — | — |
| `Oranges` | enumerator | `None` | — | — |
| `BuGn` | enumerator | `None` | — | — |
| `YlOrBr` | enumerator | `None` | — | — |
| `YlGn` | enumerator | `None` | — | — |
| `Reds` | enumerator | `None` | — | — |
| `RdPu` | enumerator | `None` | — | — |
| `Greens` | enumerator | `None` | — | — |
| `YlGnBu` | enumerator | `None` | — | — |
| `Purples` | enumerator | `None` | — | — |
| `GnBu` | enumerator | `None` | — | — |
| `Greys` | enumerator | `None` | — | — |
| `YlOrRd` | enumerator | `None` | — | — |
| `PuRd` | enumerator | `None` | — | — |
| `Blues` | enumerator | `None` | — | — |
| `PuBuGn` | enumerator | `None` | — | — |

### `GPlatesGui::BuiltinColourPalettes::ColorBrewer::Sequential::Classes`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Three` | enumerator | `None` | — | — |
| `Four` | enumerator | `None` | — | — |
| `Five` | enumerator | `None` | — | — |
| `Six` | enumerator | `None` | — | — |
| `Seven` | enumerator | `None` | — | — |
| `Eight` | enumerator | `None` | — | — |
| `Nine` | enumerator | `None` | — | — |

### `GPlatesGui::BuiltinColourPalettes::ColorBrewer::Diverging::Type`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Spectral` | enumerator | `None` | — | — |
| `RdYlGn` | enumerator | `None` | — | — |
| `RdBu` | enumerator | `None` | — | — |
| `PiYG` | enumerator | `None` | — | — |
| `PRGn` | enumerator | `None` | — | — |
| `RdYlBu` | enumerator | `None` | — | — |
| `BrBG` | enumerator | `None` | — | — |
| `RdGy` | enumerator | `None` | — | — |
| `PuOr` | enumerator | `None` | — | — |

### `GPlatesGui::BuiltinColourPalettes::ColorBrewer::Diverging::Classes`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Three` | enumerator | `None` | — | — |
| `Four` | enumerator | `None` | — | — |
| `Five` | enumerator | `None` | — | — |
| `Six` | enumerator | `None` | — | — |
| `Seven` | enumerator | `None` | — | — |
| `Eight` | enumerator | `None` | — | — |
| `Nine` | enumerator | `None` | — | — |
| `Ten` | enumerator | `None` | — | — |
| `Eleven` | enumerator | `None` | — | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `create_palette( QString palette_filename, bool invert)` | function | `GPlatesGui::ColourPalette<double>::non_null_ptr_type` | Create a colour palette from a CPT file. |
| `get_cpt_filename( Type type)` | function | `QString` | Returns the filename of the requested age CPT file (stored internally as a resource). |
| `get_cpt_filename( Type type)` | function | `QString` | Returns the filename of the requested topography CPT file (stored internally as a resource). |
| `get_cpt_filename( Type type)` | function | `QString` | Returns the filename of the requested SCM CPT file (stored internally as a resource). |
| `GPLATES_GUI_BUILTINCOLOURPALETTES_H` | macro | `None` | — |
| `create_scalar_colour_palette()` | function | `ColourPalette<double>::non_null_ptr_type` | The colour palette used when colouring by \*scalar\* value. |
| `create_gradient_colour_palette()` | function | `ColourPalette<double>::non_null_ptr_type` | The colour palette used when colouring by \*gradient\* magnitude. |
| `create_strain_rate_dilatation_colour_palette( double min_abs_strain_rate, double max_abs_strain_rate, const double &max_log_spacing = 0.3)` | function | `ColourPalette<double>::non_null_ptr_type` | A multi-colour colour palette used to colour strain rate dilatation in deformation networks. |
| `create_strain_rate_second_invariant_colour_palette( double min_abs_strain_rate, double max_abs_strain_rate, const double &max_log_spacing = 0.3)` | function | `ColourPalette<double>::non_null_ptr_type` | A multi-colour colour palette used to colour second invariant of strain rate in deformation networks. |
| `create_strain_rate_strain_rate_style_colour_palette( double min_strain_rate_style, double max_strain_rate_style)` | function | `ColourPalette<double>::non_null_ptr_type` | A multi-colour colour palette used to colour strain rate style in deformation networks. |
| `get_palette_name( Type type)` | function | `QString` | Returns a name for an age colour palette. |
| `create_palette( Type type, bool invert)` | function | `ColourPalette<double>::non_null_ptr_type` | Age grid colour palette. |
| `transcribe( GPlatesScribe::Scribe &scribe, Type &type, bool transcribed_construct_data)` | function | `GPlatesScribe::TranscribeResult` | Transcribe for sessions/projects. |
| `get_palette_name( Type type)` | function | `QString` | Returns a name for a topography colour palette. |
| `create_palette( Type type, bool invert)` | function | `ColourPalette<double>::non_null_ptr_type` | Topography colour palette. invert reverses the ordering of colours. |
| `transcribe( GPlatesScribe::Scribe &scribe, Type &type, bool transcribed_construct_data)` | function | `GPlatesScribe::TranscribeResult` | Transcribe for sessions/projects. |
| `get_palette_name( Type type)` | function | `QString` | Returns a name for a SCM colour palette. |
| `create_palette( Type type, bool invert)` | function | `ColourPalette<double>::non_null_ptr_type` | SCM colour palette. invert reverses the ordering of colours. |
| `transcribe( GPlatesScribe::Scribe &scribe, Type &type, bool transcribed_construct_data)` | function | `GPlatesScribe::TranscribeResult` | Transcribe for sessions/projects. |
| `get_palette_name( Type type)` | function | `QString` | Returns a name for a sequential ColorBrewer colour palette. |
| `create_palette( Type type, Classes classes, bool continuous, bool invert, const boost::optional<Colour> &nan_colour = boost::none)` | function | `ColourPalette<double>::non_null_ptr_type` | Create a sequential ColorBrewer colour palette over the range \[0,1\]. |
| `transcribe( GPlatesScribe::Scribe &scribe, Type &type, bool transcribed_construct_data)` | function | `GPlatesScribe::TranscribeResult` | Transcribe for sessions/projects. |
| `transcribe( GPlatesScribe::Scribe &scribe, Classes &classes, bool transcribed_construct_data)` | function | `GPlatesScribe::TranscribeResult` | — |
| `get_palette_name( Type type)` | function | `QString` | Returns a name for a diverging ColorBrewer colour palette. |
| `create_palette( Type type, Classes classes, bool continuous, bool invert, const boost::optional<Colour> &nan_colour = boost::none)` | function | `ColourPalette<double>::non_null_ptr_type` | Create a diverging ColorBrewer colour palette over the range \[-1,1\]. |
| `transcribe( GPlatesScribe::Scribe &scribe, Type &type, bool transcribed_construct_data)` | function | `GPlatesScribe::TranscribeResult` | Transcribe for sessions/projects. |
| `transcribe( GPlatesScribe::Scribe &scribe, Classes &classes, bool transcribed_construct_data)` | function | `GPlatesScribe::TranscribeResult` | — |

## Notes

[[[PROSE notes unit=gui/BuiltinColourPalettes tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ChooseBuiltinPaletteDialog](../qt-widgets/ChooseBuiltinPaletteDialog.md) | qt-widgets | 234 |
| [gui/BuiltinColourPaletteType](BuiltinColourPaletteType.md) | gui | 173 |
| [presentation/RasterVisualLayerParams](../presentation/RasterVisualLayerParams.md) | presentation | 7 |
| [presentation/TopologyNetworkVisualLayerParams](../presentation/TopologyNetworkVisualLayerParams.md) | presentation | 7 |
| [presentation/ReconstructScalarCoverageVisualLayerParams](../presentation/ReconstructScalarCoverageVisualLayerParams.md) | presentation | 5 |
| [view-operations/ScalarField3DRenderParameters](../view-operations/ScalarField3DRenderParameters.md) | view-operations | 5 |
| [presentation/RemappedColourPaletteParameters](../presentation/RemappedColourPaletteParameters.md) | presentation | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/BuiltinColourPalettes.h
python scripts/gpq.py def GPlatesGui::BuiltinColourPalettes::(anonymous)::InvertPaletteVisitor --body
python scripts/gpq.py uses InvertPaletteVisitor --kind class
python scripts/gpq.py hier InvertPaletteVisitor
```
