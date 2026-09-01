# SourceRasterFileCacheFormatReader

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 711 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/SourceRasterFileCacheFormatReader.h` | C++ | 519 |

## Overview

[[[PROSE overview unit=file-io/SourceRasterFileCacheFormatReader tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=file-io/SourceRasterFileCacheFormatReader tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
