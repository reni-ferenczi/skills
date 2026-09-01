# RasterBandReaderHandle

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1632 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/RasterBandReaderHandle.h` | C++ | 71 |
| `src/file-io/RasterBandReaderHandle.cc` | C++ | 74 |

## Overview

[[[PROSE overview unit=file-io/RasterBandReaderHandle tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=file-io/RasterBandReaderHandle tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
