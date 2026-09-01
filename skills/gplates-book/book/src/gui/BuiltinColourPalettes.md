# BuiltinColourPalettes

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 391 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/BuiltinColourPalettes.h` | C++ | 469 |
| `src/gui/BuiltinColourPalettes.cc` | C++ | 1862 |

## Overview

This is the catalogue of every colour palette GPlates ships with — not a class
hierarchy but a namespace of factory functions, each returning a fresh
`ColourPalette<double>::non_null_ptr_type`. It is the counterpart to
`AgeColourPalettes` (which colours *features* by age) on the raster and
scalar-field side: everything here maps a continuous `double` to a colour, and
the callers are the visual-layer parameter objects
(`RasterVisualLayerParams`, `TopologyNetworkVisualLayerParams`,
`ReconstructScalarCoverageVisualLayerParams`, `ScalarField3DRenderParameters`)
plus the palette-picking UI in `ChooseBuiltinPaletteDialog`.

There are two quite different construction routes hidden behind the uniform
return type, and knowing which is which matters when you add a palette. The
**named palette families** — `Age`, `Topography` and `SCM` (Fabio Crameri's
Scientific Colour Maps) — are backed by CPT files compiled into the binary as Qt
resources; each namespace has a private `get_cpt_filename()` mapping its enum to
a `:/…​.cpt` path, and all three `create_palette()` overloads are one-liners over
the shared file-loading `create_palette(QString, bool)` in the anonymous
namespace, which runs the file through
`ColourPaletteUtils::read_cpt_raster_colour_palette`. The **computed palettes** —
`create_scalar_colour_palette`, `create_gradient_colour_palette`, the three
`create_strain_rate_*` functions and both ColorBrewer `create_palette`
overloads — build a `RegularCptColourPalette` slice by slice in code. So adding
an SCM entry means adding a `.cpt` resource and two switch cases; adding a
strain-rate style means writing colour arithmetic.

Every route converges on the same final step: a `RegularCptColourPalette`
(keyed by `GPlatesMaths::Real`) wrapped by
`convert_colour_palette<…, double>(…, RealToBuiltInConverter<double>())`. That
is why each header comment repeats the warning that the returned object is a
`ColourPaletteAdapter` and a visitor will therefore see a
`RegularCptColourPalette` rather than anything named after the palette family —
there is no distinct type per built-in palette, and visitors such as the
`RangeVisitor`s in `ColourPaletteUtils` and `ColourScaleGenerator` can only
match on `visit_regular_cpt_colour_palette`. The enums here are the *identity* of
a palette; the object that carries a user's choice across sessions is
`BuiltinColourPaletteType`, which stores one of these enums plus a `Parameters`
struct (inversion, ColorBrewer class count, continuous vs. stepped) — which is
why every enum in this file has a matching `transcribe()` overload.

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

**The `transcribe()` string ids are a file-format contract.** Each carries an
explicit warning: the `GPlatesScribe::EnumValue` strings are what land in saved
sessions and `.gproj` files, so renaming an enumerator is fine but changing its
string id breaks backward and forward compatibility. Adding an enumerator means
adding it to `get_palette_name()`, to `get_cpt_filename()` or `get_colours()`,
*and* to `transcribe()`; miss the last one and old projects still load while new
ones silently lose the setting. The enumerator ordering is not part of the
contract — the protocol is by name, not by value.

**Assertions, not error handling, guard the built-in data.** The shared CPT
loader deliberately discards its `ReadErrorAccumulation` ("the age CPT file is
embedded and should just work") and then asserts that the result was a
real-valued palette; if `invert` is requested it asserts again that the visitor
produced something, which only holds if the loaded palette really was a
`RegularCptColourPalette`. Both `get_cpt_filename()` and `get_palette_name()`
end in `GPlatesGlobal::Abort` on an unhandled enum value, and the ColorBrewer
factories assert `colours.size() == classes`. A malformed or missing `.cpt`
resource is therefore an abort, not a user-visible error — correct for embedded
data, but it means a botched `.qrc` edit shows up as a crash on palette
selection.

**Inversion is done two incompatible ways.** For CPT-backed palettes it goes
through `InvertPaletteVisitor`, which rebuilds the slice list in reverse, mirrors
each slice's value range about the palette bounds, swaps each slice's lower and
upper colours, and swaps background with foreground — while deliberately leaving
the NaN colour alone. It quietly returns nothing (leading to the assertion above)
when the source palette has no range. For ColorBrewer it is just
`std::reverse` on the colour vector before the slices are built. If you add a
palette family, be clear which mechanism applies.

**ColorBrewer's `Classes` enums are their own values.** `Three = 3` and the rest
follow, so `std::size_t(classes)` is the actual class count and the code relies
on that. `continuous` changes the slice count as well as the appearance:
continuous uses `classes - 1` intervals blending between adjacent colours,
stepped uses `classes` intervals each a flat colour. The diverging palette is
further special-cased so that colours are only interpolated within `[-1, 0]` and
`[0, 1]`: an odd class count places a sample exactly at zero, while an even count
deliberately introduces a colour *discontinuity* at zero rather than blending
across it. Do not "simplify" that branch — it is preserving the ColorBrewer
design intent.

Smaller points:

- The ColorBrewer colour tables are generated, not hand-written. The Python
  script that produced them is preserved verbatim in a comment at the top of the
  `ColorBrewer` namespace, together with the upstream JSON source; regenerate
  rather than edit by hand.
- `get_colours()` lazily fills a function-local `static std::map` on first call,
  guarded by a plain `static bool` flag. This is not thread-safe under C++03
  semantics and there is no locking — everything here is assumed to run on the
  GUI thread.
- The strain-rate palettes are logarithmic. `min_abs_strain_rate` is silently
  floored at `1e-40` and `max` silently raised to `min`, so passing junk gives a
  degenerate palette rather than an error. `max_log_spacing` controls slice
  density in log space; passing a value at or below `1e-6` yields
  `num_slices_per_blend == 0`, which produces a palette with *no* interior
  slices — only background, foreground and (for dilatation) the zero slice.
- Every `create_*` call constructs a brand-new palette object; nothing here is
  cached or shared. Reading a CPT resource on each call makes
  `Age`/`Topography`/`SCM` `create_palette()` markedly more expensive than the
  computed ones — call it when the user changes a setting, not per frame.

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
