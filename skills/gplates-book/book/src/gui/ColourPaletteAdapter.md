# ColourPaletteAdapter

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 472 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ColourPaletteAdapter.h` | C++ | 239 |

## Overview

[[[PROSE overview unit=gui/ColourPaletteAdapter tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::StaticCastConverter`](#gplatesguistaticcastconverter) | struct | — | `<typename FromType, typename ToType>` | 0 | — |
| [`GPlatesGui::RealToBuiltInConverter`](#gplatesguirealtobuiltinconverter) | struct | — | `<typename T>` | 0 | — |
| [`GPlatesGui::ColourPaletteAdapter`](#gplatesguicolourpaletteadapter) | class | [`ColourPalette<ToType>`](ColourPalette.md) | `< typename FromType, typename ToType, class ConverterType = StaticCastConverter<FromType, ToType> >` | 0 | — |
| [`GPlatesGui::ColourPaletteAdapterInternals::ConvertColourPalette`](#gplatesguicolourpaletteadapterinternalsconvertcolourpalette) | struct | — | `< typename FromType, typename ToType, class ConverterType >` | 0 | — |
| [`GPlatesGui::ColourPaletteAdapterInternals::ConvertColourPalette<Type, Type, ConverterType>`](#gplatesguicolourpaletteadapterinternalsconvertcolourpalettetype-type-convertertype) | struct | — | `< typename Type, class ConverterType >` | 0 | — |

## Members

### `GPlatesGui::StaticCastConverter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `parameter_type` | typedef | `typename GPlatesUtils::Select < GPlatesUtils::TypeTraits<FromType>::is_built_in, FromType, const FromType & >::result` | public | — |
| `operator()( parameter_type value)` | operator | `ToType` | public | — |

### `GPlatesGui::RealToBuiltInConverter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator()( const GPlatesMaths::Real &value)` | operator | `T` | public | — |

### `GPlatesGui::ColourPaletteAdapter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `value_type` | typedef | `typename ColourPalette<ToType>::value_type` | public | — |
| `this_type` | typedef | `ColourPaletteAdapter<FromType, ToType, ConverterType>` | public | — |
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<this_type>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const this_type>` | public | — |
| `maybe_null_ptr_type` | typedef | `boost::intrusive_ptr<this_type>` | public | — |
| `maybe_null_ptr_to_const_type` | typedef | `boost::intrusive_ptr<const this_type>` | public | — |
| `create( SourceColourPalettePointerType adaptee, ConverterType convert = ConverterType())` | method | `non_null_ptr_type` | public | — |
| `get_colour( value_type value)` | method | `boost::optional<Colour>` | public | — |
| `accept_visitor( ConstColourPaletteVisitor &visitor)` | method | `void` | public | — |
| `accept_visitor( ColourPaletteVisitor &visitor)` | method | `void` | public | — |
| `ColourPaletteAdapter( typename ColourPalette<FromType>::non_null_ptr_type adaptee, ConverterType convert)` | constructor | `None` | private | Constructs a ColourPaletteAdapter that adapts the adaptee. |
| `d_adaptee` | field | `typename ColourPalette<FromType>::non_null_ptr_type` | private | — |
| `d_convert` | field | `ConverterType` | private | — |

### `GPlatesGui::ColourPaletteAdapterInternals::ConvertColourPalette`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `convert_colour_palette( typename ColourPalette<FromType>::non_null_ptr_type adaptee, ConverterType convert)` | method | `typename ColourPalette<ToType>::non_null_ptr_type` | public | — |

### `GPlatesGui::ColourPaletteAdapterInternals::ConvertColourPalette<Type, Type, ConverterType>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `convert_colour_palette( typename ColourPalette<Type>::non_null_ptr_type adaptee, ConverterType convert)` | method | `typename ColourPalette<Type>::non_null_ptr_type` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_COLOURPALETTEADAPTER_H` | macro | `None` | — |
| `convert_colour_palette( typename ColourPalette<FromType>::non_null_ptr_type adaptee, ConverterType convert)` | function | `typename ColourPalette<ToType>::non_null_ptr_type` | — |
| `convert_colour_palette( typename ColourPalette<FromType>::non_null_ptr_type adaptee)` | function | `typename ColourPalette<ToType>::non_null_ptr_type` | — |

## Notes

[[[PROSE notes unit=gui/ColourPaletteAdapter tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/BuiltinColourPalettes](BuiltinColourPalettes.md) | gui | 24 |
| [gui/ColourPaletteUtils](ColourPaletteUtils.md) | gui | 7 |
| [file-io/CptReader](../file-io/CptReader.md) | file-io | 5 |
| [gui/ColourPaletteRangeRemapper](ColourPaletteRangeRemapper.md) | gui | 4 |
| [gui/ColourScaleGenerator](ColourScaleGenerator.md) | gui | 4 |
| [file-io/MipmappedRasterFormatWriter](../file-io/MipmappedRasterFormatWriter.md) | file-io | 3 |
| [gui/ColourRawRaster](ColourRawRaster.md) | gui | 3 |
| [file-io/RasterFileCache](../file-io/RasterFileCache.md) | file-io | 1 |
| [gui/Palette](Palette.md) | gui | 1 |
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ColourPaletteAdapter.h
python scripts/gpq.py def GPlatesGui::ColourPaletteAdapter --body
python scripts/gpq.py uses ColourPaletteAdapter --kind class
python scripts/gpq.py hier ColourPaletteAdapter
```
