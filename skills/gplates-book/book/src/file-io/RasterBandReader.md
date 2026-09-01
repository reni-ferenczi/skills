# RasterBandReader

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1530 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/RasterBandReader.h` | C++ | 108 |
| `src/file-io/RasterBandReader.cc` | C++ | 99 |

## Overview

`RasterBandReader` narrows a `RasterReader` to one fixed band. `RasterReader`'s
methods all take a band number as a parameter because a raster file can carry
several bands; callers that only ever want one band (a single-band raster
layer, for instance) would otherwise have to thread that band number through
every call. `RasterBandReader` wraps a `RasterReader::non_null_ptr_type` plus
the chosen `band_number` and exposes the same `can_read`, `get_type`,
`get_proxied_raw_raster` and `get_raw_raster` operations without the band
argument, forwarding each call straight to the underlying `RasterReader` with
`d_band_number` filled in.

It is a thin, copyable adapter rather than an owner: several `RasterBandReader`
instances can share the same underlying `RasterReader` (each holding its own
band number), which is how `RasterBandReaderHandle` hands out per-band readers
backed by one shared reader.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::RasterBandReader`](#gplatesfileiorasterbandreader) | class | — | — | 0 | RasterBandReader is a wrapper around RasterReader that always reads the raster data from one particular band number. |

## Members

### `GPlatesFileIO::RasterBandReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RasterBandReader( const GPlatesGlobal::PointerTraits<RasterReader>::non_null_ptr_type &raster_reader, unsigned int band_number)` | constructor | `None` | public | Constructs a RasterBandReader using an existing raster\_reader, binding all reads to the given band\_number. band\_number must be greater than or equal to 1, and less than or equal to the number of bands in the source raster. |
| `RasterBandReader( const RasterBandReader &other)` | constructor | `None` | public | — |
| `~RasterBandReader()` | destructor | `None` | public | — |
| `get_filename` | field | `QString` | public | — |
| `get_band_number()` | method | `unsigned int` | public | — |
| `can_read()` | method | `bool` | public | — |
| `get_type( ReadErrorAccumulation *read_errors = NULL)` | method | `GPlatesPropertyValues::RasterType::Type` | public | — |
| `get_proxied_raw_raster( ReadErrorAccumulation *read_errors = NULL)` | method | `boost::optional<GPlatesGlobal::PointerTraits<GPlatesPropertyValues::RawRaster>::non_null_ptr_type>` | public | — |
| `get_raw_raster( const QRect &region = QRect(), ReadErrorAccumulation *read_errors = NULL)` | method | `boost::optional<GPlatesGlobal::PointerTraits<GPlatesPropertyValues::RawRaster>::non_null_ptr_type>` | public | — |
| `d_raster_reader` | field | `GPlatesGlobal::PointerTraits<RasterReader>::non_null_ptr_type` | private | — |
| `d_band_number` | field | `unsigned int` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_RASTERBANDREADER_H` | macro | `None` | — |

## Notes

`band_number` must be between 1 and the source raster's band count inclusive;
`can_read` checks this range together with the underlying reader's own
`can_read`, so an out-of-range band fails that check rather than throwing.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/RasterReader](RasterReader.md) | file-io | 50 |
| [file-io/GdalRasterReader](GdalRasterReader.md) | file-io | 43 |
| [property-values/ProxiedRasterCache](../property-values/ProxiedRasterCache.md) | property-values | 31 |
| [property-values/RawRaster](../property-values/RawRaster.md) | property-values | 24 |
| [qt-widgets/RasterPropertiesDialog](../qt-widgets/RasterPropertiesDialog.md) | qt-widgets | 23 |
| [file-io/RasterBandReaderHandle](RasterBandReaderHandle.md) | file-io | 22 |
| [file-io/RgbaRasterReader](RgbaRasterReader.md) | file-io | 22 |
| [qt-widgets/ImportRasterDialog](../qt-widgets/ImportRasterDialog.md) | qt-widgets | 18 |
| [qt-widgets/TimeDependentRasterPage](../qt-widgets/TimeDependentRasterPage.md) | qt-widgets | 17 |
| [opengl/GLScalarField3DGenerator](../opengl/GLScalarField3DGenerator.md) | opengl | 16 |
| [property-values/ProxiedRasterResolver](../property-values/ProxiedRasterResolver.md) | property-values | 15 |
| [qt-widgets/ImportScalarField3DDialog](../qt-widgets/ImportScalarField3DDialog.md) | qt-widgets | 15 |
| [qt-widgets/ScalarField3DDepthLayersPage](../qt-widgets/ScalarField3DDepthLayersPage.md) | qt-widgets | 15 |
| [property-values/RawRasterUtils](../property-values/RawRasterUtils.md) | property-values | 11 |
| [file-io/RasterFileCache](RasterFileCache.md) | file-io | 9 |
| [unit-test/MipmapperTest](../unit-test/MipmapperTest.md) | unit-test | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/RasterBandReader.h
python scripts/gpq.py def GPlatesFileIO::RasterBandReader --body
python scripts/gpq.py uses RasterBandReader --kind class
python scripts/gpq.py hier RasterBandReader
```
