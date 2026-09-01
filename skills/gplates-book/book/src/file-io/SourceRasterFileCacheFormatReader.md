# SourceRasterFileCacheFormatReader

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 711 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/SourceRasterFileCacheFormatReader.h` | C++ | 519 |

## Overview

`SourceRasterFileCacheFormatReader` is the abstract, non-templated interface a caller uses to read back the on-disk cache of a decoded source raster (the cache that `RasterReader` implementations write so a raster does not need re-decoding, e.g. from GDAL, on every subsequent load). Its region-based `read_raster`/`read_coverage` methods let rendering code stream only the tile it currently needs rather than loading the whole raster into memory.

`SourceRasterFileCacheFormatReaderImpl<RawRasterType>` is the concrete implementation, templated on the raw raster pixel type so the same logic works for whichever `RawRasterType` the cache holds. Its constructor performs the same header validation pattern used by `ScalarField3DFileFormat::Reader` and `RasterFileCacheFormat` readers generally: check the file is large enough for a header, verify `RasterFileCacheFormat::MAGIC_NUMBER`, compare the recorded total file size against the actual size on disk to detect a cache left partially written by a crashed or killed GPlates instance, then dispatch on the version field. Version 1 is handled by the nested `VersionOneReader`, which reads the raster's stored pixel type, whether coverage data is present, and its dimensions and block count, then hands the remaining decode work to a `RasterFileCacheFormatReader<RawRasterType>`. A comment in the constructor notes the same versioning strategy as the scalar-field reader: `VersionOneReader` is expected to keep serving new format versions until a structural change forces a new reader class.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::SourceRasterFileCacheFormatReader`](#gplatesfileiosourcerasterfilecacheformatreader) | class | — | — | 1 | Reads a copy of a source image originating from a RasterReader and stored in a cached file for efficient retrieval/streaming during raster rendering. |
| [`GPlatesFileIO::SourceRasterFileCacheFormatReaderImpl`](#gplatesfileiosourcerasterfilecacheformatreaderimpl) | class | [`SourceRasterFileCacheFormatReader`](SourceRasterFileCacheFormatReader.md) | — | 0 | Implementation of SourceRasterFileCacheFormatReader for a specific template parameter RawRasterType representing the type of the source raster. |
| [`GPlatesFileIO::VersionOneReader`](#gplatesfileioversiononereader) | class | [`ReaderImpl`](ScalarField3DFileFormatReader.md) | — | 0 | A reader for version 1+ files. |

## Members

### `GPlatesFileIO::SourceRasterFileCacheFormatReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~SourceRasterFileCacheFormatReader()` | destructor | `None` | public | — |
| `get_raster_dimensions()` | method | `std::pair<unsigned int, unsigned int>` | public | Returns the dimensions of the source raster (width, height). |
| `read_raster( unsigned int x_offset, unsigned int y_offset, unsigned int width, unsigned int height)` | method | `boost::optional<GPlatesPropertyValues::RawRaster::non_null_ptr_type>` | public | Reads the given region from the source raster. |
| `read_coverage( unsigned int x_offset, unsigned int y_offset, unsigned int width, unsigned int height)` | method | `boost::optional<GPlatesPropertyValues::CoverageRawRaster::non_null_ptr_type>` | public | Reads the given region from the source raster as a coverage. |
| `get_raster_statistics()` | method | `boost::optional<GPlatesPropertyValues::RasterStatistics>` | public | Returns the raster statistics or boost::none if original raster did not provide any. |
| `get_file_info()` | method | `QFileInfo` | public | Retrieves information about the file that we are reading. |
| `get_filename()` | method | `QString` | public | Returns the filename of the file that we are reading. |

### `GPlatesFileIO::SourceRasterFileCacheFormatReaderImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SourceRasterFileCacheFormatReaderImpl( const QString &filename)` | constructor | `None` | public | Opens filename for reading as a source raster file cache. |

### `GPlatesFileIO::VersionOneReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `VersionOneReader( quint32 version_number, QFile &file, QDataStream &in)` | constructor | `None` | public | — |
| `~VersionOneReader()` | destructor | `None` | public | — |
| `get_raster_dimensions()` | method | `std::pair<unsigned int, unsigned int>` | public | — |
| `read_raster( unsigned int x_offset, unsigned int y_offset, unsigned int width, unsigned int height)` | method | `boost::optional<GPlatesPropertyValues::RawRaster::non_null_ptr_type>` | public | — |
| `read_coverage( unsigned int x_offset, unsigned int y_offset, unsigned int width, unsigned int height)` | method | `boost::optional<GPlatesPropertyValues::CoverageRawRaster::non_null_ptr_type>` | public | — |
| `get_raster_statistics()` | method | `boost::optional<GPlatesPropertyValues::RasterStatistics>` | public | — |
| `d_file` | field | `QFile` | private | — |
| `d_in` | field | `QDataStream` | private | — |
| `d_raster_width` | field | `unsigned int` | private | — |
| `d_raster_height` | field | `unsigned int` | private | — |
| `d_raster_file_cache_reader` | field | `boost::shared_ptr<RasterFileCacheFormatReader<RawRasterType> >` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILE_IO_SOURCERASTERFILECACHEFORMATREADER_H` | macro | `None` | — |
| `close()` | function | `void` | Closes the file, and no further reading is possible. |
| `get_raster_dimensions()` | function | `std::pair<unsigned int, unsigned int>` | Returns the dimensions of the source raster (width, height). |
| `read_raster( unsigned int x_offset, unsigned int y_offset, unsigned int width, unsigned int height)` | function | `boost::optional<GPlatesPropertyValues::RawRaster::non_null_ptr_type>` | Reads the given region from the source raster. |
| `read_coverage( unsigned int x_offset, unsigned int y_offset, unsigned int width, unsigned int height)` | function | `boost::optional<GPlatesPropertyValues::CoverageRawRaster::non_null_ptr_type>` | Reads the given region from the source raster as a coverage. |
| `get_raster_statistics()` | function | `boost::optional<GPlatesPropertyValues::RasterStatistics>` | Returns the raster statistics or boost::none if original raster did not provide any. |
| `get_file_info()` | function | `QFileInfo` | Retrieves information about the file that we are reading. |
| `get_filename()` | function | `QString` | Returns the filename of the file that we are reading. |
| `d_file` | variable | `QFile` | — |
| `d_in` | variable | `QDataStream` | — |
| `d_impl` | variable | `boost::scoped_ptr<ReaderImpl>` | — |
| `d_is_closed` | variable | `bool` | — |

## Notes

`read_raster`, `read_coverage` and `get_raster_statistics` silently return `boost::none` once `close()` has been called on the reader, rather than throwing — callers must not treat a `none` result after closing as "region out of bounds" without checking. The constructor throws `ErrorOpeningFileForReadingException` for an unopenable file, `FileFormatNotSupportedException` for a bad magic number, wrong recorded file size, or unexpected raster type, and `RasterFileCacheFormat::UnsupportedVersion` for an unrecognised version. The destructor closes the file automatically if `close()` was not already called.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GdalRasterReader](GdalRasterReader.md) | file-io | 29 |
| [file-io/RgbaRasterReader](RgbaRasterReader.md) | file-io | 6 |
| [file-io/RasterFileCache](RasterFileCache.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/SourceRasterFileCacheFormatReader.h
python scripts/gpq.py def GPlatesFileIO::VersionOneReader --body
python scripts/gpq.py uses VersionOneReader --kind class
python scripts/gpq.py hier VersionOneReader
```
