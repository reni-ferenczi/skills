# ColourPalette

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 14 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ColourPalette.h` | C++ | 117 |

## Overview

This header declares the one abstraction every colour lookup in GPlates funnels
through: a pure-virtual, reference-counted template whose only real job is to turn
a key of type `KeyType` into an optional `Colour`. It is header-only and tiny — the
whole class is a destructor, `get_colour()`, and a pair of `accept_visitor()`
overloads — but it is the seam between the things that *have* a value (a plate id,
an age, a feature type, a raster's scalar band) and the things that decide what
colour that value should be.

The header's own comment draws the line against `ColourScheme`, and the distinction
is the design intent: a `ColourScheme` is handed a reconstruction geometry and is
responsible for extracting some property from it; a `ColourPalette` never sees a
geometry and only knows about the extracted key. Splitting the two means the code
that digs a plate id out of a `ReconstructionGeometry` is written once, and any
number of palettes — `DefaultPlateIdColourPalette`, `RegionalPlateIdColourPalette`,
a `CategoricalCptColourPalette` loaded from a CPT file — can be swapped behind it.
The same palette objects are reused far outside the geometry-colouring path: the
raster and scalar-field pipelines (`ColourRawRaster`, `GLScalarField3D`,
`MipmappedRasterFormatWriter`) colour sample values through exactly this interface,
and `ColourScaleGenerator` renders a palette into the colour-scale widget.

Two mechanisms exist purely to work around the fact that the template makes
`ColourPalette<double>` and `ColourPalette<boost::int32_t>` unrelated C++ types.
`ColourPaletteAdapter<FromType, ToType, ConverterType>` wraps a palette of one key
type and presents it as a palette of another, converting the key on the way in and
forwarding both `get_colour()` and `accept_visitor()` to the adaptee.
`RasterColourPalette` goes the other way and erases the key type entirely, holding a
`boost::variant` over the three instantiations a non-RGBA raster can use (`int32_t`,
`uint32_t`, `double`) plus an `empty` state for "no palette". Where a palette must
be handled by concrete type rather than through `get_colour()` — writing it out,
building a legend — the `ColourPaletteVisitorBase<Const>` double dispatch declared
in `ColourPaletteVisitor.h` provides it; the forward-declared typedefs at the top of
this header are the only reason it can be mentioned in the virtual signatures
without an include.

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

`value_type` is not `KeyType`. It is
`GPlatesUtils::TypeTraits<KeyType>::argument_type`, which resolves to `KeyType` by
value for built-in types and pointers, and to `const KeyType &` for everything else.
Overriding `get_colour()` in a subclass therefore means spelling the parameter as
`ColourPalette<K>::value_type` (or `typename ColourPalette<ToType>::value_type`, as
`ColourPaletteAdapter` does) rather than guessing the signature — writing `KeyType`
directly silently produces an overload instead of an override for class key types.

Lifetime is intrusive reference counting: `ColourPalette` derives from
`GPlatesUtils::ReferenceCount<ColourPalette<KeyType> >`, so palettes are always
passed as `non_null_ptr_type` / `non_null_ptr_to_const_type` and never by value or
raw pointer. The CRTP base is parameterised on `ColourPalette<KeyType>`, not on the
concrete subclass, which is why the pointer typedefs on subclasses can convert to
the base's. `ColourPaletteAdapter` takes ownership of the palette it adapts, so an
adapted palette outlives the pointer you handed to `create()` only through the
adapter.

Only `get_colour()` is pure virtual. Both `accept_visitor()` overloads have empty
default bodies, so a palette that does not override them is silently not visited —
this is deliberate (not every palette has a corresponding `visit_*` hook on
`ColourPaletteVisitorBase`), but it means a new palette type is invisible to
visitors, and to anything built on them, until both the override and a new `visit_*`
method are added. Adding that method touches every existing visitor implementation.

The reference count itself is a `boost::detail::atomic_count` member of the
`ReferenceCount` base, so acquiring and releasing pointers is thread safe;
`get_colour()` is not, and neither is anything a subclass does inside it.
`intrusive_ptr_release()` deletes through a `static_cast` to `ColourPalette<KeyType>`,
which is correct here only because the destructor is virtual.

One consequence of that per-base counter is worth knowing before following the
header's advice to multiply inherit for a palette serving several key types: each
`ColourPalette<K>` base then carries its own independent count, so the object must
be owned through one chosen base pointer type throughout. `ColourPaletteAdapter`
sidesteps the problem by composition and is the route the existing subclasses take.

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
