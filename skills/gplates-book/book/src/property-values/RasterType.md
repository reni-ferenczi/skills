# RasterType

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 949 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/RasterType.h` | C++ | 129 |
| `src/property-values/RasterType.cc` | C++ | 169 |

## Overview

[[[PROSE overview unit=property-values/RasterType tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=property-values/RasterType tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
