# ColourSpectrum

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1266 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ColourSpectrum.h` | C++ | 69 |
| `src/gui/ColourSpectrum.cc` | C++ | 93 |

## Overview

[[[PROSE overview unit=gui/ColourSpectrum tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=gui/ColourSpectrum tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
