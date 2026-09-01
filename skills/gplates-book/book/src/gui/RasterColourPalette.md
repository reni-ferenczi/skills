# RasterColourPalette

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 794 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/RasterColourPalette.h` | C++ | 245 |
| `src/gui/RasterColourPalette.cc` | C++ | 127 |

## Overview

`GPlatesGui::ColourPalette<KeyType>` is a class template, so a palette keyed on
`double` and a palette keyed on `boost::int32_t` share no base class and cannot
be passed through the same pointer. That is fine inside a single templated
algorithm, but it is not fine at the boundaries where a palette has to be
stored, transcribed into a session, sent to `GPlatesOpenGL::GLVisualRasterSource`
or attached to a layer's parameters, because at those points the key type is a
runtime property of the raster rather than a compile-time fact.
`RasterColourPalette` is the erasure that makes that possible: one
reference-counted, `non_null_intrusive_ptr`-managed handle wrapping a
`boost::variant` over the three palette key types that can colour a non-RGBA
raster — `int32_t`, `uint32_t` and `double` — plus an `empty` alternative that
stands for "no palette". Because `empty` is a real alternative and not a null
pointer, the handle itself is never null and callers never have to distinguish
"missing palette" from "missing wrapper"; `RasterColourPaletteType::get_type()`
returning `INVALID` is, for instance, how `ColourPaletteUtils` reports that
reading a `.cpt` file produced nothing usable.

The unit is small because it deliberately does not interpret what it holds. It
offers exactly two ways to get back at the palette, and they dispatch on
different axes. `apply_visitor()` runs a `boost::static_visitor` over the
variant, so the visitor's overloads distinguish the *key* type — this is the
preferred route, and the callers that matter use it:
`ColourRawRaster::colour_raw_raster_with_raster_colour_palette` picks the
`colour_raw_raster<key_type>` instantiation this way, and
`RasterColourPaletteExtract::get_colour_palette<PaletteKeyType>()` is the same
mechanism reduced to a single question ("is it this key type?") via
`ExtractVisitor`, whose exact overload wins over its catch-all template.
`accept_visitor()` is the other axis: it forwards to the wrapped palette's own
`ColourPalette::accept_visitor`, so the visitor's overloads distinguish the
*concrete palette class* — `AgeColourPalette`, `PlateIdColourPalette`,
`RegularCptColourPalette`, the categorical CPT palettes — and the `empty` case
simply visits nothing. `RasterColourPaletteType::get_type()` exists as a plain
`switch`-friendly alternative to the first axis and is implemented with it.

The member `apply_visitor()` overloads are not just convenience.
`boost::apply_visitor` accepts any type that provides a member `apply_visitor`,
which is why `get_colour_palette()` can write
`boost::apply_visitor(visitor, raster_colour_palette)` against a
`RasterColourPalette` rather than reaching for its private variant. Removing or
renaming those members would break every such call site, not just the ones that
name them directly.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::VisitColourPaletteVisitor`](#anonymousvisitcolourpalettevisitor) | class | `boost::static_visitor<>` | `<class ColourPaletteVisitorType>` | 0 | A visitor that, in turn, visits a ConstColourPaletteVisitor or ColourPaletteVisitor. |
| [`(anonymous)::RasterColourPaletteTypeVisitor`](#anonymousrastercolourpalettetypevisitor) | class | `boost::static_visitor<GPlatesGui::RasterColourPaletteType::Type>` | — | 0 | — |
| [`GPlatesGui::RasterColourPalette`](#gplatesguirastercolourpalette) | class | [`GPlatesUtils::ReferenceCount<RasterColourPalette>`](../utils/ReferenceCount.md) | — | 0 | RasterColourPalette is a convenience wrapper around a boost::variant over pointers to ColourPalette\<int32\_t\>, ColourPalette\<uint32\_t\> and ColourPalette\<double\>; i.e those types of ColourPalettes that can be used to colour non-RGBA rasters. |
| [`GPlatesGui::RasterColourPaletteType::Type`](#gplatesguirastercolourpalettetypetype) | enum | — | — | 0 | — |
| [`GPlatesGui::RasterColourPaletteExtract::Implementation::ExtractVisitor`](#gplatesguirastercolourpaletteextractimplementationextractvisitor) | class | `boost::static_visitor< boost::optional<typename ColourPalette<PaletteKeyType>::non_null_ptr_type> >` | `<typename PaletteKeyType>` | 0 | — |

## Members

### `(anonymous)::VisitColourPaletteVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `VisitColourPaletteVisitor( ColourPaletteVisitorType &colour_palette_visitor)` | constructor | `None` | public | — |
| `operator()( const GPlatesGui::RasterColourPalette::empty &)` | operator | `void` | public | — |
| `operator()( const ColourPalettePtrType &colour_palette_ptr)` | operator | `void` | public | — |
| `d_colour_palette_visitor` | field | `ColourPaletteVisitorType` | private | — |

### `(anonymous)::RasterColourPaletteTypeVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator()( const GPlatesGui::RasterColourPalette::empty &)` | operator | `GPlatesGui::RasterColourPaletteType::Type` | public | — |
| `operator()( const GPlatesGui::ColourPalette<boost::int32_t>::non_null_ptr_type &)` | operator | `GPlatesGui::RasterColourPaletteType::Type` | public | — |
| `operator()( const GPlatesGui::ColourPalette<boost::uint32_t>::non_null_ptr_type &)` | operator | `GPlatesGui::RasterColourPaletteType::Type` | public | — |
| `operator()( const GPlatesGui::ColourPalette<double>::non_null_ptr_type &)` | operator | `GPlatesGui::RasterColourPaletteType::Type` | public | — |

### `GPlatesGui::RasterColourPalette`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<RasterColourPalette>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const RasterColourPalette>` | public | — |
| `create( const typename ColourPalette<PaletteKeyType>::non_null_ptr_type &colour_palette)` | method | `non_null_ptr_type` | public | Wrap a ColourPalette\<\> in a RasterColourPalette. |
| `create()` | method | `non_null_ptr_type` | public | Create an empty RasterColourPalette. |
| `accept_visitor( ConstColourPaletteVisitor &colour_palette_visitor)` | method | `void` | public | Accept a standard 'ConstColourPaletteVisitor' (as opposed to a boost variant visitor. |
| `accept_visitor( ColourPaletteVisitor &colour_palette_visitor)` | method | `void` | public | Accept a standard 'ColourPaletteVisitor' (as opposed to a boost variant visitor. |
| `empty` | struct | `None` | public | — |
| `variant_type` | typedef | `boost::variant< empty, // boost::variant requires the first type be default-constructible; signifies no colour palette. ColourPalette<boost::int32_t>::non_null_ptr_type, ColourPale ...` | public | — |
| `apply_visitor( const StaticVisitorType &visitor)` | method | `typename StaticVisitorType::result_type` | public | Apply a static visitor to the boost::variant wrapped in this instance. |
| `apply_visitor( StaticVisitorType &visitor)` | method | `typename StaticVisitorType::result_type` | public | Apply a static visitor to the boost::variant wrapped in this instance. |
| `RasterColourPalette()` | constructor | `None` | private | — |
| `RasterColourPalette( const ColourPalettePointerType &colour_palette)` | constructor | `None` | private | — |
| `d_colour_palette` | field | `variant_type` | private | — |

### `GPlatesGui::RasterColourPaletteType::Type`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `INVALID` | enumerator | `None` | — | — |
| `INT32` | enumerator | `None` | — | — |
| `UINT32` | enumerator | `None` | — | — |
| `DOUBLE` | enumerator | `None` | — | — |

### `GPlatesGui::RasterColourPaletteExtract::Implementation::ExtractVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator()( const typename ColourPalette<PaletteKeyType>::non_null_ptr_type &colour_palette)` | operator | `boost::optional<typename ColourPalette<PaletteKeyType>::non_null_ptr_type>` | public | Look for a specific ColourPalette type (specifically with key 'PaletteKeyType')... |
| `operator()( const VariantBoundedType &)` | operator | `boost::optional<typename ColourPalette<PaletteKeyType>::non_null_ptr_type>` | public | General operator catches everything else... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_RASTERCOLOURPALETTE_H` | macro | `None` | — |
| `get_type( const RasterColourPalette &raster_colour_palette)` | function | `RasterColourPaletteType::Type` | Returns the type of the ColourPalette encapsulated inside a RasterColourPalette. |
| `get_colour_palette( const RasterColourPalette &raster_colour_palette)` | function | `boost::optional<typename ColourPalette<PaletteKeyType>::non_null_ptr_type>` | — |

## Notes

**`empty` must stay first in the variant.** `boost::variant` requires its first
bounded type to be default-constructible, and none of the
`non_null_intrusive_ptr` alternatives are. Reordering the alternatives breaks
the default-constructed `RasterColourPalette` and, with it, `create()`.

**The wrapper is immutable; the palette inside it is not.** Both constructors
are private, so instances come only from the two `create()` overloads, and there
is no way to change `d_colour_palette` afterwards — which is why most of the
codebase passes `non_null_ptr_to_const_type`. That const-ness stops at the
wrapper, though. The variant holds *non-const* `ColourPalette<T>::non_null_ptr_type`,
and both `accept_visitor` overloads are `const` member functions, including the
one taking the mutating `ColourPaletteVisitor`. A
`RasterColourPalette::non_null_ptr_to_const_type` therefore still grants
mutable access to the wrapped palette; do not treat it as a deep-const handle.
Conversely `apply_visitor` has no non-const form, so a static visitor always
receives the variant alternatives by const reference — the visitors in the `.cc`
take `const &` for that reason.

**Wrong key type is a wrapping error, not a rejection.** `create()` is a
template with no constraint, and the private constructor takes any
`ColourPalettePointerType`; if the type is not one of the three bounded
alternatives the failure surfaces as a compile error inside `boost::variant`
rather than as anything this class reports. A palette keyed on
some other type must be run through `GPlatesGui::ColourPaletteAdapter` first,
which converts the key on `get_colour` and forwards `accept_visitor` straight to
its adaptee — so the class-hierarchy visitor sees the underlying palette and
never learns that an adapter is in the chain.

**Adding a fourth key type touches three places, and only one of them fails
loudly.** `variant_type` and `RasterColourPaletteType::Type` in the header, and
`RasterColourPaletteTypeVisitor` in the `.cc`. That last visitor has explicit
overloads and no catch-all, so a new alternative is a compile error there —
deliberately. The generic visitors, `VisitColourPaletteVisitor` and
`ExtractVisitor`, both end in a template catch-all, so they will absorb the new
alternative silently: `ExtractVisitor` will simply return `boost::none` for it.
So will every static visitor elsewhere in the tree that follows the same
pattern, such as the one in `ColourRawRaster`.

**Reference counting is atomic** (`GPlatesUtils::ReferenceCount` uses
`boost::detail::atomic_count`), so handing a palette to the raster worker paths
in `file-io` and `opengl` is safe as far as the count goes. Nothing here
synchronises the palette's own state.

## Used by

| Unit | Component | References |
|---|---|---|
| [property-values/ProxiedRasterResolver](../property-values/ProxiedRasterResolver.md) | property-values | 27 |
| [opengl/GLVisualLayers](../opengl/GLVisualLayers.md) | opengl | 22 |
| [presentation/RemappedColourPaletteParameters](../presentation/RemappedColourPaletteParameters.md) | presentation | 16 |
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](../qt-widgets/TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 16 |
| [gui/BuiltinColourPaletteType](BuiltinColourPaletteType.md) | gui | 14 |
| [file-io/RasterFileCache](../file-io/RasterFileCache.md) | file-io | 12 |
| [gui/ColourPaletteUtils](ColourPaletteUtils.md) | gui | 12 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 10 |
| [file-io/MipmappedRasterFormatWriter](../file-io/MipmappedRasterFormatWriter.md) | file-io | 9 |
| [file-io/RasterFileCacheFormat](../file-io/RasterFileCacheFormat.md) | file-io | 9 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 9 |
| [opengl/GLVisualRasterSource](../opengl/GLVisualRasterSource.md) | opengl | 8 |
| [qt-widgets/ColourScaleButton](../qt-widgets/ColourScaleButton.md) | qt-widgets | 7 |
| [qt-widgets/ColourScaleWidget](../qt-widgets/ColourScaleWidget.md) | qt-widgets | 7 |
| [qt-widgets/RemappedColourPaletteWidget](../qt-widgets/RemappedColourPaletteWidget.md) | qt-widgets | 7 |
| [unit-test/MipmapperTest](../unit-test/MipmapperTest.md) | unit-test | 7 |
| [file-io/MipmappedRasterFormatReader](../file-io/MipmappedRasterFormatReader.md) | file-io | 6 |
| [gui/ColourPaletteRangeRemapper](ColourPaletteRangeRemapper.md) | gui | 6 |
| [gui/ColourScaleGenerator](ColourScaleGenerator.md) | gui | 6 |
| [gui/ColourRawRaster](ColourRawRaster.md) | gui | 5 |

*... and 18 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/RasterColourPalette.h
python scripts/gpq.py def GPlatesGui::RasterColourPalette --body
python scripts/gpq.py uses RasterColourPalette --kind class
python scripts/gpq.py hier RasterColourPalette
```
