# RasterBandReaderHandle

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1632 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/RasterBandReaderHandle.h` | C++ | 71 |
| `src/file-io/RasterBandReaderHandle.cc` | C++ | 74 |

## Overview

`RasterBandReaderHandle` wraps a `RasterBandReader` by value and forwards every
call to it unchanged. It exists so a "proxied" `RawRaster` — one whose pixel
data has not been loaded yet — can carry a copyable, storable handle back to
the reader that will supply that data on demand: `RawRaster`'s
`WithProxiedData` data policy (see `property-values/RawRaster.h`) stores a
`RasterBandReaderHandle` and hands it to `ProxiedRasterResolver` when the
actual raster contents are finally needed. The extra layer over
`RasterBandReader` itself keeps that storage relationship separate from the
read-adapter relationship `RasterBandReader` has with `RasterReader`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::RasterBandReaderHandle`](#gplatesfileiorasterbandreaderhandle) | class | — | — | 0 | This class acts as a bridge between RasterBandReader and proxied RawRasters. |

## Members

### `GPlatesFileIO::RasterBandReaderHandle`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RasterBandReaderHandle( const RasterBandReader &raster_band_reader)` | constructor | `None` | public | — |
| `get_filename` | field | `QString` | public | — |
| `get_band_number()` | method | `unsigned int` | public | — |
| `can_read()` | method | `bool` | public | — |
| `get_type( ReadErrorAccumulation *read_errors = NULL)` | method | `GPlatesPropertyValues::RasterType::Type` | public | — |
| `get_raw_raster( const QRect &region = QRect(), ReadErrorAccumulation *read_errors = NULL)` | method | `boost::optional<GPlatesGlobal::PointerTraits<GPlatesPropertyValues::RawRaster>::non_null_ptr_type>` | public | — |
| `d_raster_band_reader` | field | `RasterBandReader` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_RASTERBANDREADERHANDLE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/MipmappedRasterFormatWriter](MipmappedRasterFormatWriter.md) | file-io | 8 |
| [file-io/GdalRasterReader](GdalRasterReader.md) | file-io | 4 |
| [property-values/ProxiedRasterCache](../property-values/ProxiedRasterCache.md) | property-values | 4 |
| [file-io/RasterFileCache](RasterFileCache.md) | file-io | 1 |
| [file-io/RasterReader](RasterReader.md) | file-io | 1 |
| [file-io/RasterWriter](RasterWriter.md) | file-io | 1 |
| [file-io/RgbaRasterReader](RgbaRasterReader.md) | file-io | 1 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 1 |
| [property-values/RawRaster](../property-values/RawRaster.md) | property-values | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/RasterBandReaderHandle.h
python scripts/gpq.py def GPlatesFileIO::RasterBandReaderHandle --body
python scripts/gpq.py uses RasterBandReaderHandle --kind class
python scripts/gpq.py hier RasterBandReaderHandle
```
