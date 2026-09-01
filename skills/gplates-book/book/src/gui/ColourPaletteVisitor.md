# ColourPaletteVisitor

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1229 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ColourPaletteVisitor.h` | C++ | 120 |

## Overview

The visitor interface for double-dispatching over the small closed set of
concrete `ColourPalette` implementations (`AgeColourPalette`,
`CategoricalCptColourPalette<int32_t>`/`<uint32_t>`, `FeatureTypeColourPalette`,
`PlateIdColourPalette`, `RegularCptColourPalette`). `ColourPaletteVisitorBase<Const>`
is templated on constness so a single definition serves both const and
non-const traversal: `GPlatesUtils::SetConst` adjusts each `visit_*`
parameter's type accordingly, and `ConstColourPaletteVisitor` /
`ColourPaletteVisitor` are the two instantiations client code actually names.
Every `visit_*` method has a default no-op body, so a concrete visitor
(`ColourPaletteUtils::Implementation::RangeVisitor`, `ColourPaletteRangeRemapper`,
`ColourScaleGenerator`, and others) only needs to override the palette kinds
it cares about.

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

Adding a new concrete `ColourPalette` kind requires a matching `visit_*`
method here (with a default no-op body, to avoid breaking existing
visitors) and an `accept_visitor` override on the new palette class that
calls it — this header only defines the dispatch surface, not which
palettes exist.

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
