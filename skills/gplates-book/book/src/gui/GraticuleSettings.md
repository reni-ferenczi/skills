# GraticuleSettings

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 924 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/GraticuleSettings.h` | C++ | 154 |
| `src/gui/GraticuleSettings.cc` | C++ | 80 |

## Overview

`GraticuleSettings` is a small value type holding the user's preferences for
the lat/lon grid drawn on the globe and map: spacing in radians for latitude
and longitude, a colour, and a line-width hint. A spacing of zero suppresses
that axis's lines entirely. `SphericalGrid` and `MapGrid` consume an instance
to know what to draw, and `ViewState` owns the live setting that
`ConfigureGraticulesDialog` edits. It participates in project/session
serialisation via `transcribe()`, falling back field-by-field to the defaults
in `DEFAULT_GRATICULE_DELTA_LAT`/`_LON`/`_COLOUR` (30 degrees and translucent
silver) when a field is missing from older saved data, so new settings fields
can be added without breaking backward compatibility.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::GraticuleSettings`](#gplatesguigraticulesettings) | class | `boost::equality_comparable<GraticuleSettings>` | — | 0 | — |

## Members

### `GPlatesGui::GraticuleSettings`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DEFAULT_GRATICULE_DELTA_LAT` | field | `double` | public | Default graticule spacing in latitude and longitude. |
| `DEFAULT_GRATICULE_DELTA_LON` | field | `double` | public | — |
| `DEFAULT_GRATICULE_COLOUR` | field | `GPlatesGui::Colour` | public | Default graticule colour. |
| `GraticuleSettings( double delta_lat = DEFAULT_GRATICULE_DELTA_LAT, double delta_lon = DEFAULT_GRATICULE_DELTA_LON, const GPlatesGui::Colour &colour = DEFAULT_GRATICULE_COLOUR)` | constructor | `None` | public | Constructs a GraticuleSettings. |
| `get_delta_lat()` | method | `double` | public | — |
| `set_delta_lat( double delta_lat)` | method | `void` | public | — |
| `get_delta_lon()` | method | `double` | public | — |
| `set_delta_lon( double delta_lon)` | method | `void` | public | — |
| `set_colour( const GPlatesGui::Colour &colour)` | method | `void` | public | — |
| `get_line_width_hint()` | method | `float` | public | — |
| `set_line_width_hint( float line_width_hint)` | method | `void` | public | — |
| `d_delta_lat` | field | `double` | private | — |
| `d_delta_lon` | field | `double` | private | — |
| `d_colour` | field | `GPlatesGui::Colour` | private | — |
| `d_line_width_hint` | field | `float` | private | — |
| `transcribe( GPlatesScribe::Scribe &scribe, bool transcribed_construct_data)` | method | `GPlatesScribe::TranscribeResult` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_default_graticules_colour()` | function | `GPlatesGui::Colour` | — |
| `DEFAULT_GRATICULE_DELTA_LAT` | variable | `double` | — |
| `DEFAULT_GRATICULE_DELTA_LON` | variable | `double` | — |
| `DEFAULT_GRATICULE_COLOUR` | variable | `GPlatesGui::Colour` | — |
| `GPLATES_GUI_GRATICULESETTINGS_H` | macro | `None` | — |

## Notes

Equality (`boost::equality_comparable`) compares floating-point fields with
`GPlatesMaths::are_almost_exactly_equal()` rather than `==`.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ConfigureGraticulesDialog](../qt-widgets/ConfigureGraticulesDialog.md) | qt-widgets | 12 |
| [gui/SphericalGrid](SphericalGrid.md) | gui | 9 |
| [gui/MapGrid](MapGrid.md) | gui | 8 |
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 4 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 2 |
| [gui/Map](Map.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/GraticuleSettings.h
python scripts/gpq.py def GPlatesGui::GraticuleSettings --body
python scripts/gpq.py uses GraticuleSettings --kind class
python scripts/gpq.py hier GraticuleSettings
```
