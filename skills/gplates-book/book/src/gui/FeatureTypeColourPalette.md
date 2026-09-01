# FeatureTypeColourPalette

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 14 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/FeatureTypeColourPalette.h` | C++ | 94 |
| `src/gui/FeatureTypeColourPalette.cc` | C++ | 180 |

## Overview

Provides a color palette that maps `FeatureType` to `Colour` for rendering different feature types with distinct colors. The palette uses a hash of the feature type name to select from a palette of 18 base colors, with hardcoded overrides for well-known types (Coastline, Fault, MidOceanRidge, etc). Colors are generated lazily on first request and cached in a mutable map; this hash-based approach ensures colors remain stable when new feature types are added to the GPGIM, unlike index-based assignment which would break backward compatibility.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::FeatureTypeColourPalette`](#gplatesguifeaturetypecolourpalette) | class | [`ColourPalette<GPlatesModel::FeatureType>`](ColourPalette.md) | — | 0 | FeatureTypeColourPalette maps feature types to colours. |

## Members

### `GPlatesGui::FeatureTypeColourPalette`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create()` | method | `non_null_ptr_type` | public | The GPGIM is used to query all feature types available. |
| `get_colour( const GPlatesModel::FeatureType &feature_type)` | method | `boost::optional<Colour>` | public | — |
| `accept_visitor( ConstColourPaletteVisitor &visitor)` | method | `void` | public | — |
| `accept_visitor( ColourPaletteVisitor &visitor)` | method | `void` | public | — |
| `FeatureTypeColourPalette()` | constructor | `None` | private | — |
| `d_colours` | field | `std::map<GPlatesModel::FeatureType, Colour>` | private | A mapping of FeatureType to Colours. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `map_to_colour( unsigned int number)` | function | `Colour` | — |
| `generate_hash( const GPlatesModel::FeatureType &feature_type)` | function | `unsigned int` | The previous name of this function(hash) conflicts with a name in boost on mac os 10.7. |
| `create_colour( const GPlatesModel::FeatureType &feature_type)` | function | `Colour` | Assign a colour to a FeatureType. |
| `GPLATES_GUI_FEATURECOLOURPALETTE_H` | macro | `None` | — |

## Notes

The `d_colours` map is mutable, allowing `get_colour()` to cache generated colors for previously unseen feature types even when called on a const instance. Hard-wired color overrides in the constructor take precedence over the hash-based generation.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ColourSchemeContainer](ColourSchemeContainer.md) | gui | 1 |
| [gui/DrawStyleAdapters](DrawStyleAdapters.md) | gui | 1 |
| [gui/DrawStyleManager](DrawStyleManager.md) | gui | 1 |
| [gui/Palette](Palette.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/FeatureTypeColourPalette.h
python scripts/gpq.py def GPlatesGui::FeatureTypeColourPalette --body
python scripts/gpq.py uses FeatureTypeColourPalette --kind class
python scripts/gpq.py hier FeatureTypeColourPalette
```
