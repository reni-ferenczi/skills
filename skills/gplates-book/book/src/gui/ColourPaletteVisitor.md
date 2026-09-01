# ColourPaletteVisitor

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1229 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ColourPaletteVisitor.h` | C++ | 120 |

## Overview

[[[PROSE overview unit=gui/ColourPaletteVisitor tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ColourPaletteVisitorBase`](#gplatesguicolourpalettevisitorbase) | class | — | `<bool Const>` | 0 | This class is a base class for visitors that visit ColourPalettes. |
| [`GPlatesGui::ConstColourPaletteVisitor`](#gplatesguiconstcolourpalettevisitor) | typedef | — | — | 0 | This is the base class for visitors that visit const ColourPalettes. |
| [`GPlatesGui::ColourPaletteVisitor`](#gplatesguicolourpalettevisitor) | typedef | — | — | 0 | This is the base class for visitors that visit non-const ColourPalettes. |

## Members

### `GPlatesGui::ColourPaletteVisitorBase`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `age_colour_palette_type` | typedef | `typename GPlatesUtils::SetConst<AgeColourPalette, Const>::type` | public | Typedefs to give the supported derivations the appropriate const-ness. |
| `int32_categorical_cpt_colour_palette_type` | typedef | `typename GPlatesUtils::SetConst<CategoricalCptColourPalette<boost::int32_t>, Const>::type` | public | — |
| `uint32_categorical_cpt_colour_palette_type` | typedef | `typename GPlatesUtils::SetConst<CategoricalCptColourPalette<boost::uint32_t>, Const>::type` | public | — |
| `feature_type_colour_palette_type` | typedef | `typename GPlatesUtils::SetConst<FeatureTypeColourPalette, Const>::type` | public | — |
| `plate_id_colour_palette_type` | typedef | `typename GPlatesUtils::SetConst<PlateIdColourPalette, Const>::type` | public | — |
| `regular_cpt_colour_palette_type` | typedef | `typename GPlatesUtils::SetConst<RegularCptColourPalette, Const>::type` | public | — |
| `~ColourPaletteVisitorBase()` | destructor | `None` | public | — |
| `visit_age_colour_palette( age_colour_palette_type &)` | method | `void` | public | — |
| `visit_int32_categorical_cpt_colour_palette( int32_categorical_cpt_colour_palette_type &)` | method | `void` | public | — |
| `visit_uint32_categorical_cpt_colour_palette( uint32_categorical_cpt_colour_palette_type &)` | method | `void` | public | — |
| `visit_feature_type_colour_palette( feature_type_colour_palette_type &)` | method | `void` | public | — |
| `visit_plate_id_colour_palette( plate_id_colour_palette_type &)` | method | `void` | public | — |
| `visit_regular_cpt_colour_palette( regular_cpt_colour_palette_type &)` | method | `void` | public | — |
| `ColourPaletteVisitorBase()` | constructor | `None` | protected | — |

### `GPlatesGui::ConstColourPaletteVisitor`

*None.*

### `GPlatesGui::ColourPaletteVisitor`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_COLOURPALETTEVISITOR_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/ColourPaletteVisitor tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/BuiltinColourPalettes](BuiltinColourPalettes.md) | gui | 26 |
| [gui/ColourPaletteUtils](ColourPaletteUtils.md) | gui | 7 |
| [gui/CptColourPalette](CptColourPalette.md) | gui | 7 |
| [file-io/CptReader](../file-io/CptReader.md) | file-io | 4 |
| [gui/ColourPaletteRangeRemapper](ColourPaletteRangeRemapper.md) | gui | 4 |
| [gui/ColourScaleGenerator](ColourScaleGenerator.md) | gui | 4 |
| [gui/AgeColourPalettes](AgeColourPalettes.md) | gui | 3 |
| [gui/FeatureTypeColourPalette](FeatureTypeColourPalette.md) | gui | 3 |
| [gui/PlateIdColourPalettes](PlateIdColourPalettes.md) | gui | 3 |
| [gui/Palette](Palette.md) | gui | 2 |
| [gui/ColourSchemeContainer](ColourSchemeContainer.md) | gui | 1 |
| [gui/RasterColourPalette](RasterColourPalette.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ColourPaletteVisitor.h
python scripts/gpq.py def GPlatesGui::ColourPaletteVisitorBase --body
python scripts/gpq.py uses ColourPaletteVisitorBase --kind class
python scripts/gpq.py hier ColourPaletteVisitorBase
```
