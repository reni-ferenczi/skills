# SingleColourScheme

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 994 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/SingleColourScheme.h` | C++ | 85 |
| `src/gui/SingleColourScheme.cc` | C++ | 60 |

## Overview

A simple colour scheme that assigns a single fixed colour to all reconstruction geometries, regardless of their feature properties or type. Used when the user wants uniform rendering—all geometries appear in the same colour. Defaults to white if no colour is specified. Provides a factory function `make_single_colour_scheme()` to wrap construction in a `ColourScheme` pointer.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::SingleColourScheme`](#gplatesguisinglecolourscheme) | class | [`ColourScheme`](ColourScheme.md) | — | 1 | This class assigns a fixed colour to reconstruction geometries. |

## Members

### `GPlatesGui::SingleColourScheme`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SingleColourScheme()` | constructor | `None` | public | — |
| `SingleColourScheme( const Colour &colour)` | constructor | `None` | public | — |
| `get_colour( const GPlatesAppLogic::ReconstructionGeometry &reconstruction_geometry)` | method | `boost::optional<Colour>` | public | — |
| `get_colour( const GPlatesModel::FeatureHandle& feature_ptr)` | method | `boost::optional<Colour>` | public | — |
| `get_colour()` | method | `boost::optional<Colour>` | public | — |
| `d_colour` | field | `boost::optional<Colour>` | private | — |
| `DEFAULT_COLOUR` | field | `Colour` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `DEFAULT_COLOUR` | variable | `GPlatesGui::Colour` | — |
| `GPLATES_GUI_SINGLECOLOURSCHEME_H` | macro | `None` | — |
| `make_single_colour_scheme( const Colour &colour)` | function | `ColourScheme::non_null_ptr_type` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ColouringDialog](../qt-widgets/ColouringDialog.md) | qt-widgets | 3 |
| [gui/ColourSchemeContainer](ColourSchemeContainer.md) | gui | 2 |
| [qt-widgets/GlobeAndMapWidget](../qt-widgets/GlobeAndMapWidget.md) | qt-widgets | 2 |
| [gui/DrawStyleManager](DrawStyleManager.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/SingleColourScheme.h
python scripts/gpq.py def GPlatesGui::SingleColourScheme --body
python scripts/gpq.py uses SingleColourScheme --kind class
python scripts/gpq.py hier SingleColourScheme
```
