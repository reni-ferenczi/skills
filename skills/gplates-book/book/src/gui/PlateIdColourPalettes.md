# PlateIdColourPalettes

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 867 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/PlateIdColourPalettes.h` | C++ | 124 |
| `src/gui/PlateIdColourPalettes.cc` | C++ | 146 |

## Overview

[[[PROSE overview unit=gui/PlateIdColourPalettes tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::DefaultColours`](#anonymousdefaultcolours) | class | — | — | 0 | — |
| [`(anonymous)::RegionalColours`](#anonymousregionalcolours) | class | — | — | 0 | — |
| [`GPlatesGui::PlateIdColourPalette`](#gplatesguiplateidcolourpalette) | class | [`ColourPalette<GPlatesModel::integer_plate_id_type>`](ColourPalette.md) | — | 2 | Base class for colour palettes that colour by plate ID. |
| [`GPlatesGui::DefaultPlateIdColourPalette`](#gplatesguidefaultplateidcolourpalette) | class | [`PlateIdColourPalette`](PlateIdColourPalettes.md) | — | 0 | DefaultPlateIdColourPalette maps plate IDs to colours using a scheme that aims to make adjacent plates stand out from each other. |
| [`GPlatesGui::RegionalPlateIdColourPalette`](#gplatesguiregionalplateidcolourpalette) | class | [`PlateIdColourPalette`](PlateIdColourPalettes.md) | — | 0 | RegionalPlateIdColourPalette maps plate IDs to colours using a scheme that colours plates belonging to the same region with similar colours. |

## Members

### `(anonymous)::DefaultColours`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DefaultColours()` | constructor | `None` | public | — |
| `d_colours` | field | `std::vector<Colour>` | private | — |

### `(anonymous)::RegionalColours`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RegionalColours()` | constructor | `None` | public | — |
| `d_colours` | field | `std::vector<Colour>` | private | — |

### `GPlatesGui::PlateIdColourPalette`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `accept_visitor( ConstColourPaletteVisitor &visitor)` | method | `void` | public | — |
| `accept_visitor( ColourPaletteVisitor &visitor)` | method | `void` | public | — |

### `GPlatesGui::DefaultPlateIdColourPalette`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create()` | method | `non_null_ptr_type` | public | — |
| `get_colour( value_type plate_id)` | method | `boost::optional<Colour>` | public | — |
| `DefaultPlateIdColourPalette()` | constructor | `None` | private | — |

### `GPlatesGui::RegionalPlateIdColourPalette`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create()` | method | `non_null_ptr_type` | public | — |
| `get_colour( value_type plate_id)` | method | `boost::optional<Colour>` | public | — |
| `RegionalPlateIdColourPalette()` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_PLATEIDCOLOURPALETTES_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/PlateIdColourPalettes tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ColourSchemeContainer](ColourSchemeContainer.md) | gui | 3 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 3 |
| [gui/DrawStyleManager](DrawStyleManager.md) | gui | 2 |
| [gui/DrawStyleAdapters](DrawStyleAdapters.md) | gui | 1 |
| [gui/GenericColourScheme](GenericColourScheme.md) | gui | 1 |
| [qt-widgets/DrawStyleDialog](../qt-widgets/DrawStyleDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/PlateIdColourPalettes.h
python scripts/gpq.py def (anonymous)::DefaultColours --body
python scripts/gpq.py uses DefaultColours --kind class
python scripts/gpq.py hier DefaultColours
```
