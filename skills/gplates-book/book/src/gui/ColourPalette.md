# ColourPalette

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 14 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ColourPalette.h` | C++ | 117 |

## Overview

[[[PROSE overview unit=gui/ColourPalette tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ConstColourPaletteVisitor`](#gplatesguiconstcolourpalettevisitor) | typedef | — | — | 3 | Forward declarations. |
| [`GPlatesGui::ColourPaletteVisitor`](#gplatesguicolourpalettevisitor) | typedef | — | — | 1 | — |
| [`GPlatesGui::ColourPalette`](#gplatesguicolourpalette) | class | [`GPlatesUtils::ReferenceCount<ColourPalette<KeyType> >`](../utils/ReferenceCount.md) | `<typename KeyType>` | 11 | ColourPalette maps KeyType values to Colours, the mapping being either continuous or discrete. |

## Members

### `GPlatesGui::ConstColourPaletteVisitor`

*None.*

### `GPlatesGui::ColourPaletteVisitor`

*None.*

### `GPlatesGui::ColourPalette`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `key_type` | typedef | `KeyType` | public | — |
| `value_type` | typedef | `typename GPlatesUtils::TypeTraits<key_type>::argument_type` | public | — |
| `this_type` | typedef | `ColourPalette<KeyType>` | public | — |
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<this_type>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const this_type>` | public | — |
| `maybe_null_ptr_type` | typedef | `boost::intrusive_ptr<this_type>` | public | — |
| `maybe_null_ptr_to_const_type` | typedef | `boost::intrusive_ptr<const this_type>` | public | — |
| `~ColourPalette()` | destructor | `None` | public | — |
| `get_colour( value_type value)` | method | `boost::optional<Colour>` | public | Retrieves the Colour associated with the value provided. boost::none if no Colour is assocated with the value. |
| `accept_visitor( ConstColourPaletteVisitor &)` | method | `void` | public | — |
| `accept_visitor( ColourPaletteVisitor &)` | method | `void` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_COLOURPALETTE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/ColourPalette tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/BuiltinColourPalettes](BuiltinColourPalettes.md) | gui | 283 |
| [gui/ColourRawRaster](ColourRawRaster.md) | gui | 39 |
| [opengl/GLScalarField3D](../opengl/GLScalarField3D.md) | opengl | 36 |
| [gui/ColourPaletteRangeRemapper](ColourPaletteRangeRemapper.md) | gui | 28 |
| [gui/RasterColourPalette](RasterColourPalette.md) | gui | 23 |
| [file-io/MipmappedRasterFormatWriter](../file-io/MipmappedRasterFormatWriter.md) | file-io | 21 |
| [gui/CptColourPalette](CptColourPalette.md) | gui | 19 |
| [gui/ColourScaleGenerator](ColourScaleGenerator.md) | gui | 18 |
| [gui/ColourPaletteUtils](ColourPaletteUtils.md) | gui | 17 |
| [gui/GlobeRenderedGeometryLayerPainter](GlobeRenderedGeometryLayerPainter.md) | gui | 17 |
| [gui/MapRenderedGeometryLayerPainter](MapRenderedGeometryLayerPainter.md) | gui | 17 |
| [presentation/TopologyNetworkVisualLayerParams](../presentation/TopologyNetworkVisualLayerParams.md) | presentation | 16 |
| [gui/ColourPaletteAdapter](ColourPaletteAdapter.md) | gui | 15 |
| [file-io/CptReader](../file-io/CptReader.md) | file-io | 14 |
| [gui/PlateIdColourPalettes](PlateIdColourPalettes.md) | gui | 12 |
| [presentation/RemappedColourPaletteParameters](../presentation/RemappedColourPaletteParameters.md) | presentation | 12 |
| [file-io/SourceRasterFileCacheFormatReader](../file-io/SourceRasterFileCacheFormatReader.md) | file-io | 10 |
| [gui/AgeColourPalettes](AgeColourPalettes.md) | gui | 8 |
| [opengl/GLVisualLayers](../opengl/GLVisualLayers.md) | opengl | 8 |
| [gui/FeatureTypeColourPalette](FeatureTypeColourPalette.md) | gui | 6 |

*... and 21 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ColourPalette.h
python scripts/gpq.py def GPlatesGui::ColourPalette --body
python scripts/gpq.py uses ColourPalette --kind class
python scripts/gpq.py hier ColourPalette
```
