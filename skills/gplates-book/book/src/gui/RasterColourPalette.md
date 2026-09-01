# RasterColourPalette

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 794 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/RasterColourPalette.h` | C++ | 245 |
| `src/gui/RasterColourPalette.cc` | C++ | 127 |

## Overview

[[[PROSE overview unit=gui/RasterColourPalette tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=gui/RasterColourPalette tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
