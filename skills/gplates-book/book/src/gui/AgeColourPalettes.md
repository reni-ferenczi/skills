# AgeColourPalettes

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 107 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/AgeColourPalettes.h` | C++ | 221 |
| `src/gui/AgeColourPalettes.cc` | C++ | 158 |

## Overview

This unit supplies the two built-in palettes that colour geometry by *feature age*
— the age of a feature relative to the current reconstruction time. They are
`ColourPalette<GPlatesMaths::Real>` specialisations, so the key they are indexed
by is a geological time in Ma rather than a plate id or a raster value. In
practice they are never used bare: `ColourSchemeContainer::create_built_in_colour_schemes`
pairs each one with a `GPlatesAppLogic::AgePropertyExtractor` via
`make_colour_scheme()` and registers the result under
`ColourSchemeCategory::FEATURE_AGE` as the "Default" and "Monochrome" entries the
user picks in the draw-style UI. The extractor is what turns a feature into an
age; the palette only turns an age into a `Colour`.

The reason `AgeColourPalette` exists as an intermediate abstract base — rather
than the two concrete palettes deriving from `ColourPalette` directly — is the
mutable `[lower, upper]` age window plus the visitor hook. Every other palette
family has its range baked into its data (a CPT file, a hard-coded table), so
code that wants to draw a colour scale needs a way to ask an age palette what
range it currently spans. That is exactly what
`ConstColourPaletteVisitor::visit_age_colour_palette` is for: the `RangeVisitor`
in `ColourPaletteUtils` and the one inside `ColourScaleGenerator` implement that
one hook to read `get_range()`, which lets the colour-scale widgets label the
bar without downcasting. The `d_default_*` pair exists only so `reset_bounds()`
can restore the constructor's window after the user has moved it.

The two concrete palettes differ in how they handle out-of-range ages, not just
in colour. `MonochromeAgeColourPalette` clamps: anything at or beyond a bound
gets that bound's colour, so `get_colour()` always yields a value.
`DefaultAgeColourPalette` normalises the age into a `[0, 1]` position and hands
it to a temporary `ColourSpectrum`, which returns `boost::none` outside that
interval — so it can, and does, return no colour for a feature outside the
window, and callers must be ready for that. It does special-case the infinities
first: a positive-infinity age (distant past) is pinned to the upper bound and
negative infinity (distant future) to the lower bound, so `GPlatesMaths::Real`
values coming from unbounded time periods still colour.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::AgeColourPalette`](#gplatesguiagecolourpalette) | class | [`ColourPalette<GPlatesMaths::Real>`](ColourPalette.md) | — | 2 | Abstract base class for colour palettes that colour by age. |
| [`GPlatesGui::DefaultAgeColourPalette`](#gplatesguidefaultagecolourpalette) | class | [`AgeColourPalette`](AgeColourPalettes.md) | — | 0 | DefaultAgeColourPalette maps age to colours using a rainbow of colours. |
| [`GPlatesGui::MonochromeAgeColourPalette`](#gplatesguimonochromeagecolourpalette) | class | [`AgeColourPalette`](AgeColourPalettes.md) | — | 0 | MonochromeAgeColourPalette maps age to colours using shades of grey. |

## Members

### `GPlatesGui::AgeColourPalette`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AgeColourPalette( const double default_upper_bound, const double default_lower_bound)` | constructor | `None` | public | — |
| `reset_bounds()` | method | `void` | public | — |
| `get_upper_bound()` | method | `GPlatesMaths::Real` | public | — |
| `set_upper_bound( const GPlatesMaths::Real &upper_bound_)` | method | `void` | public | — |
| `get_lower_bound()` | method | `GPlatesMaths::Real` | public | — |
| `set_lower_bound( const GPlatesMaths::Real &lower_bound_)` | method | `void` | public | — |
| `get_range()` | method | `std::pair<GPlatesMaths::Real, GPlatesMaths::Real>` | public | — |
| `set_range( const std::pair<GPlatesMaths::Real, GPlatesMaths::Real> &range)` | method | `void` | public | — |
| `accept_visitor( ConstColourPaletteVisitor &visitor)` | method | `void` | public | — |
| `accept_visitor( ColourPaletteVisitor &visitor)` | method | `void` | public | — |
| `get_background_colour()` | method | `Colour` | public | Returns the colour for ages younger than the lower bound. |
| `get_foreground_colour()` | method | `Colour` | public | Returns the colour for ages older than the upper bound. |
| `d_upper_bound` | field | `GPlatesMaths::Real` | protected | — |
| `d_lower_bound` | field | `GPlatesMaths::Real` | protected | — |
| `d_default_upper_bound` | field | `GPlatesMaths::Real` | private | — |
| `d_default_lower_bound` | field | `GPlatesMaths::Real` | private | — |

### `GPlatesGui::DefaultAgeColourPalette`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create()` | method | `non_null_ptr_type` | public | — |
| `get_colour( const GPlatesMaths::Real &geo_time)` | method | `boost::optional<Colour>` | public | — |
| `get_background_colour()` | method | `Colour` | public | — |
| `get_foreground_colour()` | method | `Colour` | public | — |
| `DefaultAgeColourPalette()` | constructor | `None` | private | — |
| `DEFAULT_UPPER_BOUND` | field | `double` | private | — |
| `DEFAULT_LOWER_BOUND` | field | `double` | private | — |

### `GPlatesGui::MonochromeAgeColourPalette`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create()` | method | `non_null_ptr_type` | public | — |
| `get_colour( const GPlatesMaths::Real &geo_time)` | method | `boost::optional<Colour>` | public | — |
| `get_background_colour()` | method | `Colour` | public | — |
| `get_foreground_colour()` | method | `Colour` | public | — |
| `MonochromeAgeColourPalette()` | constructor | `None` | private | — |
| `DEFAULT_UPPER_BOUND` | field | `double` | private | — |
| `DEFAULT_LOWER_BOUND` | field | `double` | private | — |
| `UPPER_COLOUR` | field | `Colour` | private | — |
| `LOWER_COLOUR` | field | `Colour` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `DEFAULT_UPPER_BOUND` | variable | `double` | — |
| `DEFAULT_LOWER_BOUND` | variable | `double` | — |
| `UPPER_COLOUR` | variable | `GPlatesGui::Colour` | — |
| `LOWER_COLOUR` | variable | `GPlatesGui::Colour` | — |
| `GPLATES_GUI_AGECOLOURPALETTES_H` | macro | `None` | — |

## Notes

**The "rainbow" in the class comment is stale.** `DefaultAgeColourPalette` builds
a default-constructed `ColourSpectrum`, whose defaults are white upper / black
lower over `[0, 1]`; the actual rainbow constructor in `ColourSpectrum.cc` is
inside an `#if 0` block. Working through `Colour::linearly_interpolate` (position
0 gives the *first* argument) and `ColourSpectrum::get_colour_at`'s inverted
`(upper - position)` term, the palette in this release runs black at the youngest
age to white at the oldest — i.e. the same greyscale ramp as
`MonochromeAgeColourPalette` but in the opposite direction. Do not trust the
Doxygen here; if you change `ColourSpectrum`'s defaults you silently change what
the "Default" feature-age colour scheme looks like.

`ColourSpectrum::get_colour_at`'s own comment claims it clamps positions outside
`[0, 1]`; it does not — it returns `boost::none`. (`get_colour_or_bound_colour`
is the clamping variant, and this unit does not use it.) That is what makes
`DefaultAgeColourPalette::get_colour` fallible while the monochrome one is not.
`get_background_colour()` and `get_foreground_colour()` dereference the optional
unconditionally, which is safe only because they pass exactly 0.0 and 1.0.

Nothing in the 2.5.0 tree calls `set_upper_bound`, `set_lower_bound`,
`set_range` or `reset_bounds` — the mutable-window API is present and reachable
(the palettes are held as non-const `non_null_ptr_type`) but currently unused, so
in practice both palettes stay on the 0–450 Ma default. If you do start moving
the bounds, note there is no validation: nothing keeps `d_lower_bound` below
`d_upper_bound`, and an equal pair divides by zero in both `get_colour`
implementations.

Lifetime is the usual GPlates intrusive-refcount pattern inherited from
`ColourPalette` / `GPlatesUtils::ReferenceCount`: constructors are private and
the static `create()` returns a `non_null_ptr_type`, so instances are always
heap-allocated and shared. Instances are cheap and stateless apart from the two
bounds, but `DefaultAgeColourPalette::get_colour` constructs a fresh
`ColourSpectrum` on every call, which matters if you ever put this palette on a
per-vertex path rather than a per-feature one.

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 55 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 54 |
| [qt-widgets/DrawStyleDialog](../qt-widgets/DrawStyleDialog.md) | qt-widgets | 40 |
| [gui/DrawStyleManager](DrawStyleManager.md) | gui | 34 |
| [gui/ColourSchemeContainer](ColourSchemeContainer.md) | gui | 30 |
| [gui/ColourScaleGenerator](ColourScaleGenerator.md) | gui | 29 |
| [api/PyColour](../api/PyColour.md) | api | 24 |
| [gui/ColourPaletteUtils](ColourPaletteUtils.md) | gui | 23 |
| [presentation/RemappedColourPaletteParameters](../presentation/RemappedColourPaletteParameters.md) | presentation | 23 |
| [presentation/TopologyNetworkVisualLayerParams](../presentation/TopologyNetworkVisualLayerParams.md) | presentation | 21 |
| [gui/DrawStyleAdapters](DrawStyleAdapters.md) | gui | 18 |
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](../qt-widgets/TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 18 |
| [presentation/VisualLayerRegistry](../presentation/VisualLayerRegistry.md) | presentation | 17 |
| [gui/BuiltinColourPalettes](BuiltinColourPalettes.md) | gui | 14 |
| [gui/PythonConfiguration](PythonConfiguration.md) | gui | 9 |
| [qt-widgets/ModifyReconstructionPoleWidget](../qt-widgets/ModifyReconstructionPoleWidget.md) | qt-widgets | 9 |
| [view-operations/ScalarField3DRenderParameters](../view-operations/ScalarField3DRenderParameters.md) | view-operations | 6 |
| [gui/GeometryFocusHighlight](GeometryFocusHighlight.md) | gui | 4 |
| [presentation/ReconstructVisualLayerParams](../presentation/ReconstructVisualLayerParams.md) | presentation | 3 |
| [presentation/TopologyGeometryVisualLayerParams](../presentation/TopologyGeometryVisualLayerParams.md) | presentation | 3 |

*... and 2 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/AgeColourPalettes.h
python scripts/gpq.py def GPlatesGui::AgeColourPalette --body
python scripts/gpq.py uses AgeColourPalette --kind class
python scripts/gpq.py hier AgeColourPalette
```
