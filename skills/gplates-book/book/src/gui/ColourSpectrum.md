# ColourSpectrum

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1266 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ColourSpectrum.h` | C++ | 69 |
| `src/gui/ColourSpectrum.cc` | C++ | 93 |

## Overview

`ColourSpectrum` maps a scalar `position` to a `Colour` by linearly interpolating (via `Colour::linearly_interpolate`) between an `upper_colour` and a `lower_colour` across a `[lower_bound, upper_bound]` range — the building block used by continuous colour palettes such as `AgeColourPalettes` and `Palette` to turn a numeric value into a gradient colour rather than a discrete lookup.

It offers two ways to handle a position outside the configured bounds: `get_colour_at` returns `boost::none` so the caller can decide there is simply no colour for that value, while `get_colour_or_bound_colour` instead clamps by returning the colour at whichever bound was exceeded, so a caller that always wants a `Colour` (never `boost::none` for in-bounds inputs) can use it without a null check.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ColourSpectrum`](#gplatesguicolourspectrum) | class | — | — | 0 | — |

## Members

### `GPlatesGui::ColourSpectrum`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ColourSpectrum( const Colour& upper_colour = Colour::get_white(), const Colour& lower_colour = Colour::get_black(), const double upper_bound = 1.0, const double lower_bound = 0.0)` | constructor | `None` | public | — |
| `get_colour_at(double position)` | method | `boost::optional<GPlatesGui::Colour>` | public | Retrieves the colour along the colour spectrum at the given position. |
| `get_colour_or_bound_colour(double position)` | method | `boost::optional<GPlatesGui::Colour>` | public | — |
| `d_upper_colour` | field | `Colour` | protected | — |
| `d_lower_colour` | field | `Colour` | protected | — |
| `d_upper_bound` | field | `double` | protected | — |
| `d_lower_bound` | field | `double` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_COLOURSPECTRUM_H` | macro | `None` | — |

## Notes

- `get_colour_at`'s doc comment claims out-of-range positions are clamped, but the implementation actually returns `boost::none` for any `position` outside `[lower_bound, upper_bound]`; clamping behaviour is only in `get_colour_or_bound_colour`.
- The two accessors interpolate in opposite directions at the bounds: `get_colour_at` returns `lower_colour` at `lower_bound` and `upper_colour` at `upper_bound`, while `get_colour_or_bound_colour` returns `upper_colour` at `lower_bound` and `lower_colour` at `upper_bound` — they are not drop-in replacements for each other for in-range positions.
- The constructor only logs a `qWarning` if `upper_bound < lower_bound`; it does not reject or correct the values, so a misconfigured spectrum keeps running with an inverted range.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Palette](Palette.md) | gui | 17 |
| [gui/AgeColourPalettes](AgeColourPalettes.md) | gui | 7 |
| [gui/ColourPalette](ColourPalette.md) | gui | 1 |
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](../qt-widgets/TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ColourSpectrum.h
python scripts/gpq.py def GPlatesGui::ColourSpectrum --body
python scripts/gpq.py uses ColourSpectrum --kind class
python scripts/gpq.py hier ColourSpectrum
```
