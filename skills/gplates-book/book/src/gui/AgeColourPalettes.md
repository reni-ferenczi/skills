# AgeColourPalettes

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 107 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/AgeColourPalettes.h` | C++ | 221 |
| `src/gui/AgeColourPalettes.cc` | C++ | 158 |

## Overview

[[[PROSE overview unit=gui/AgeColourPalettes tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=gui/AgeColourPalettes tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
