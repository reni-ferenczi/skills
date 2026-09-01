# RasterType

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 949 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/RasterType.h` | C++ | 129 |
| `src/property-values/RasterType.cc` | C++ | 169 |

## Overview

`RasterType` is a namespace, not a class: an enumeration of raster element types plus the two compile-time maps that connect that enumeration to real C++ types. It exists because raster handling in GPlates is statically typed — `RawRasterImpl<T, ...>` is a template and `RawRasterVisitor` has one `visit` overload per instantiation — while the outside world (GDAL band types, the import wizard's combo boxes, saved layer parameters) deals in a runtime tag. `RasterType::Type` is that tag, and it is the value the rest of the code stores, compares and serialises.

The two maps are exact mirrors of each other. `GetEnumAsType<E>::type` goes enum → C++ type and is used where an enumerator is a template argument; `get_type_as_enum<T>()` goes C++ type → enum and is what `RawRasterUtils::get_raster_type` uses, via a visitor over `RawRaster`, to recover the tag from a concrete raster. Both are declared in the header and only the `get_type_as_enum` specialisations live in the `.cc`, so adding a raster element type means touching the enum, both maps, `get_type_as_string`, the `RawRasterImpl` typedefs and the `RawRasterVisitor` overloads in `RawRaster.h`, and the GDAL translation tables in `GPlatesFileIO::GDALRasterReader` / `GDALRasterWriter`.

The element types are deliberately Qt's fixed-width integers (`qint8` … `quint32`) rather than the `boost::int*_t` family — `RawRaster.h` records that this was done so raster data could be streamed through `QDataStream` without the type ambiguities the boost typedefs caused on some platforms. `FLOAT` and `DOUBLE`, by contrast, map to plain `float` and `double` with no width guarantee, on the same assumption GDAL makes. `RGBA8` maps to `GPlatesGui::rgba8_t`, which is why the `is_*` predicates classify it as neither integer nor floating point.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::RasterType::Type`](#gplatespropertyvaluesrastertypetype) | enum | — | — | 0 | An enumeration of data types that can be found in rasters. |
| [`GPlatesPropertyValues::RasterType::GetEnumAsType`](#gplatespropertyvaluesrastertypegetenumastype) | struct | — | `<Type>` | 0 | Default type returned for UNINITIALISED and UNKNOWN enums. |
| [`GPlatesPropertyValues::RasterType::GetEnumAsType<INT8>`](#gplatespropertyvaluesrastertypegetenumastypeint8) | struct | — | `<>` | 0 | Default type returned for UNINITIALISED and UNKNOWN enums. |
| [`GPlatesPropertyValues::RasterType::GetEnumAsType<UINT8>`](#gplatespropertyvaluesrastertypegetenumastypeuint8) | struct | — | `<>` | 0 | Default type returned for UNINITIALISED and UNKNOWN enums. |
| [`GPlatesPropertyValues::RasterType::GetEnumAsType<INT16>`](#gplatespropertyvaluesrastertypegetenumastypeint16) | struct | — | `<>` | 0 | Default type returned for UNINITIALISED and UNKNOWN enums. |
| [`GPlatesPropertyValues::RasterType::GetEnumAsType<UINT16>`](#gplatespropertyvaluesrastertypegetenumastypeuint16) | struct | — | `<>` | 0 | Default type returned for UNINITIALISED and UNKNOWN enums. |
| [`GPlatesPropertyValues::RasterType::GetEnumAsType<INT32>`](#gplatespropertyvaluesrastertypegetenumastypeint32) | struct | — | `<>` | 0 | Default type returned for UNINITIALISED and UNKNOWN enums. |
| [`GPlatesPropertyValues::RasterType::GetEnumAsType<UINT32>`](#gplatespropertyvaluesrastertypegetenumastypeuint32) | struct | — | `<>` | 0 | Default type returned for UNINITIALISED and UNKNOWN enums. |
| [`GPlatesPropertyValues::RasterType::GetEnumAsType<FLOAT>`](#gplatespropertyvaluesrastertypegetenumastypefloat) | struct | — | `<>` | 0 | Default type returned for UNINITIALISED and UNKNOWN enums. |
| [`GPlatesPropertyValues::RasterType::GetEnumAsType<DOUBLE>`](#gplatespropertyvaluesrastertypegetenumastypedouble) | struct | — | `<>` | 0 | Default type returned for UNINITIALISED and UNKNOWN enums. |
| [`GPlatesPropertyValues::RasterType::GetEnumAsType<RGBA8>`](#gplatespropertyvaluesrastertypegetenumastypergba8) | struct | — | `<>` | 0 | Default type returned for UNINITIALISED and UNKNOWN enums. |

## Members

### `GPlatesPropertyValues::RasterType::Type`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UNINITIALISED` | enumerator | `None` | — | — |
| `INT8` | enumerator | `None` | — | — |
| `UINT8` | enumerator | `None` | — | — |
| `INT16` | enumerator | `None` | — | — |
| `UINT16` | enumerator | `None` | — | — |
| `INT32` | enumerator | `None` | — | — |
| `UINT32` | enumerator | `None` | — | — |
| `FLOAT` | enumerator | `None` | — | — |
| `DOUBLE` | enumerator | `None` | — | — |
| `RGBA8` | enumerator | `None` | — | — |
| `UNKNOWN` | enumerator | `None` | — | — |

### `GPlatesPropertyValues::RasterType::GetEnumAsType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `type` | typedef | `void` | public | Default type returned for UNINITIALISED and UNKNOWN enums. |

### `GPlatesPropertyValues::RasterType::GetEnumAsType<INT8>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `type` | typedef | `qint8` | public | Default type returned for UNINITIALISED and UNKNOWN enums. |

### `GPlatesPropertyValues::RasterType::GetEnumAsType<UINT8>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `type` | typedef | `quint8` | public | Default type returned for UNINITIALISED and UNKNOWN enums. |

### `GPlatesPropertyValues::RasterType::GetEnumAsType<INT16>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `type` | typedef | `qint16` | public | Default type returned for UNINITIALISED and UNKNOWN enums. |

### `GPlatesPropertyValues::RasterType::GetEnumAsType<UINT16>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `type` | typedef | `quint16` | public | Default type returned for UNINITIALISED and UNKNOWN enums. |

### `GPlatesPropertyValues::RasterType::GetEnumAsType<INT32>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `type` | typedef | `qint32` | public | Default type returned for UNINITIALISED and UNKNOWN enums. |

### `GPlatesPropertyValues::RasterType::GetEnumAsType<UINT32>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `type` | typedef | `quint32` | public | Default type returned for UNINITIALISED and UNKNOWN enums. |

### `GPlatesPropertyValues::RasterType::GetEnumAsType<FLOAT>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `type` | typedef | `float` | public | Default type returned for UNINITIALISED and UNKNOWN enums. |

### `GPlatesPropertyValues::RasterType::GetEnumAsType<DOUBLE>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `type` | typedef | `double` | public | Default type returned for UNINITIALISED and UNKNOWN enums. |

### `GPlatesPropertyValues::RasterType::GetEnumAsType<RGBA8>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `type` | typedef | `GPlatesGui::rgba8_t` | public | Default type returned for UNINITIALISED and UNKNOWN enums. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_type_as_enum()` | function | `Type` | — |
| `GPLATES_PROPERTYVALUES_RASTERTYPE_H` | macro | `None` | — |
| `get_type_as_string( Type type)` | function | `QString` | — |
| `is_signed_integer( Type type)` | function | `bool` | — |
| `is_unsigned_integer( Type type)` | function | `bool` | — |
| `is_integer( Type type)` | function | `bool` | — |
| `is_floating_point( Type type)` | function | `bool` | — |

## Notes

**Both maps fail silently rather than at compile time.** The primary `GetEnumAsType` template yields `void`, and the primary `get_type_as_enum<T>()` returns `UNKNOWN`. An element type nobody specialised therefore compiles cleanly and produces a nonsense answer at run time. If you add a raster element type and forget one half of the pair, nothing will tell you.

**The round trip is not a bijection.** `UNINITIALISED` and `UNKNOWN` both map to `void`, and `get_type_as_enum<void>()` returns `UNINITIALISED` — so `UNKNOWN` cannot survive a trip through `GetEnumAsType`. `UNINITIALISED` is a real, reachable state (it is the tag of `UninitialisedRawRaster`, the `RawRasterImpl<void, WithoutData, ...>` typedef); `UNKNOWN` is the "we could not classify this" answer.

**The enumerators are unnumbered.** `Type` has no explicit values, so its numeric encoding depends on declaration order. Anything that persists a `RasterType::Type` as an integer — layer parameters written into a project file, cached raster metadata — is coupled to that order; inserting an enumerator anywhere but at the end changes the meaning of existing data.

**`is_integer` excludes `RGBA8`,** even though `rgba8_t` is four unsigned bytes, and `is_floating_point` excludes it too. The RGBA case is meant to be distinguished separately — `RawRasterUtils::does_raster_contain_numerical_data` is the predicate that actually splits colour rasters from data rasters, and it is defined as the complement of the colour case rather than in terms of these helpers. `UNINITIALISED` and `UNKNOWN` answer false to all four predicates.

**`get_type_as_string` returns the enumerator's spelling,** not a display string; it is the fallback for `UNKNOWN` via `default:`, so an out-of-range integer cast to `Type` stringifies as `UNKNOWN` rather than asserting.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GdalRasterWriter](../file-io/GdalRasterWriter.md) | file-io | 86 |
| [file-io/GdalRasterReader](../file-io/GdalRasterReader.md) | file-io | 63 |
| [property-values/RawRasterUtils](RawRasterUtils.md) | property-values | 37 |
| [qt-widgets/ImportRasterDialog](../qt-widgets/ImportRasterDialog.md) | qt-widgets | 29 |
| [qt-widgets/RasterPropertiesDialog](../qt-widgets/RasterPropertiesDialog.md) | qt-widgets | 28 |
| [file-io/RasterWriter](../file-io/RasterWriter.md) | file-io | 23 |
| [file-io/RgbaRasterWriter](../file-io/RgbaRasterWriter.md) | file-io | 21 |
| [qt-widgets/TimeDependentRasterPage](../qt-widgets/TimeDependentRasterPage.md) | qt-widgets | 11 |
| [app-logic/RasterLayerParams](../app-logic/RasterLayerParams.md) | app-logic | 9 |
| [file-io/RasterReader](../file-io/RasterReader.md) | file-io | 8 |
| [gui/Mipmapper](../gui/Mipmapper.md) | gui | 8 |
| [presentation/RasterVisualLayerParams](../presentation/RasterVisualLayerParams.md) | presentation | 8 |
| [file-io/MipmappedRasterFormatWriter](../file-io/MipmappedRasterFormatWriter.md) | file-io | 6 |
| [file-io/RasterBandReader](../file-io/RasterBandReader.md) | file-io | 5 |
| [qt-widgets/RasterLayerOptionsWidget](../qt-widgets/RasterLayerOptionsWidget.md) | qt-widgets | 4 |
| [gui/ExportAnimationRegistry](../gui/ExportAnimationRegistry.md) | gui | 3 |
| [property-values/ProxiedRasterResolver](ProxiedRasterResolver.md) | property-values | 3 |
| [file-io/RasterBandReaderHandle](../file-io/RasterBandReaderHandle.md) | file-io | 2 |
| [file-io/RasterFileCache](../file-io/RasterFileCache.md) | file-io | 2 |
| [file-io/RgbaRasterReader](../file-io/RgbaRasterReader.md) | file-io | 2 |

*... and 4 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/RasterType.h
python scripts/gpq.py def GPlatesPropertyValues::RasterType::Type --body
python scripts/gpq.py uses Type --kind enum
```
