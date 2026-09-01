# MipmappedRasterFormatReader

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 797 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/MipmappedRasterFormatReader.h` | C++ | 490 |

## Overview

`MipmappedRasterFormatReader<RawRasterType>` reads back the on-disk mipmap
cache files GPlates generates for large rasters, so `RasterReader` and
`ProxiedRasterResolver` can fetch a region of a given mipmap level without
decoding the whole level. `RawRasterType` is the type of the *mipmapped*
rasters stored in the file, not the source raster's type — mipmap files are
generated per raster-value type, matched by `RasterFileCacheFormat::get_type_as_enum`.
Construction validates the file eagerly: magic number, recorded total file
size against the actual file size (to catch a mipmap file left behind by a
previous run that crashed mid-write), and a version number, before
dispatching to a version-specific inner reader — currently only
`VersionOneReader`.

The public class is a thin, non-template-parameter-dependent facade: it opens
the file, parses the shared header, and forwards `read_level`,
`read_coverage` and `get_raster_statistics` to a `ReaderImpl` chosen at
construction time. `VersionOneReader` is that `ReaderImpl` for the current
(version 1) on-disk format: it reads the per-level `LevelInfo` table (width,
height, file offset, block count) up front and creates one
`RasterFileCacheFormatReader<RawRasterType>` per mipmap level, each of which
does the actual seeking and block decoding for its level on demand. The
commented-out `VersionThreeReader` branch documents the intended path for
introducing a structurally different format in a later version while keeping
`VersionOneReader` for versions that only change block encoding.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::MipmappedRasterFormatReader`](#gplatesfileiomipmappedrasterformatreader) | class | — | — | 0 | MipmappedRasterFormatReader reads mipmapped images from a mipmapped raster file. |
| [`GPlatesFileIO::VersionOneReader`](#gplatesfileioversiononereader) | class | [`ReaderImpl`](ScalarField3DFileFormatReader.md) | — | 0 | A reader for version 1+ files. |

## Members

### `GPlatesFileIO::MipmappedRasterFormatReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MipmappedRasterFormatReader( const QString &filename)` | constructor | `None` | public | Opens filename for reading as a mipmapped raster file. |

### `GPlatesFileIO::VersionOneReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `VersionOneReader( quint32 version_number, QFile &file, QDataStream &in)` | constructor | `None` | public | — |
| `~VersionOneReader()` | destructor | `None` | public | — |
| `get_number_of_levels()` | method | `unsigned int` | public | — |
| `read_level( unsigned int level, unsigned int x_offset, unsigned int y_offset, unsigned int width, unsigned int height)` | method | `boost::optional<typename RawRasterType::non_null_ptr_type>` | public | — |
| `read_coverage( unsigned int level, unsigned int x_offset, unsigned int y_offset, unsigned int width, unsigned int height)` | method | `boost::optional<GPlatesPropertyValues::CoverageRawRaster::non_null_ptr_type>` | public | — |
| `get_raster_statistics( unsigned int level)` | method | `boost::optional<GPlatesPropertyValues::RasterStatistics>` | public | — |
| `d_file` | field | `QFile` | private | — |
| `d_in` | field | `QDataStream` | private | — |
| `d_level_infos` | field | `std::vector<RasterFileCacheFormat::LevelInfo>` | private | — |
| `d_raster_file_cache_readers` | field | `std::vector<boost::shared_ptr<RasterFileCacheFormatReader<RawRasterType> > >` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_MIPMAPPEDRASTERFORMATREADER_H` | macro | `None` | — |
| `close()` | function | `void` | Closes the file, and no further reading is possible. |
| `get_number_of_levels()` | function | `unsigned int` | Returns the number of levels in the current mipmapped raster file. |
| `read_level( unsigned int level, unsigned int x_offset, unsigned int y_offset, unsigned int width, unsigned int height)` | function | `boost::optional<typename RawRasterType::non_null_ptr_type>` | Reads the given region from the mipmap at the given level. |
| `read_coverage( unsigned int level, unsigned int x_offset, unsigned int y_offset, unsigned int width, unsigned int height)` | function | `boost::optional<GPlatesPropertyValues::CoverageRawRaster::non_null_ptr_type>` | Reads the given region from the coverage raster at the given level. |
| `get_raster_statistics( unsigned int level)` | function | `boost::optional<GPlatesPropertyValues::RasterStatistics>` | Returns the raster statistics or boost::none if original raster did not provide any. |
| `get_file_info()` | function | `QFileInfo` | Retrieves information about the file that we are reading. |
| `get_filename()` | function | `QString` | Returns the filename of the file that we are reading. |
| `d_file` | variable | `QFile` | — |
| `d_in` | variable | `QDataStream` | — |
| `d_impl` | variable | `boost::scoped_ptr<ReaderImpl>` | — |
| `d_is_closed` | variable | `bool` | — |

## Notes

`level` here is relative to the mipmap file's own numbering, not the source
raster: level 0 is the first size *smaller* than the source raster, because
the source raster itself is never stored in the mipmap file. Once `close()`
is called (or `d_is_closed` is otherwise set), every read method returns
`boost::none` instead of touching the closed `QFile`; the destructor closes
the file automatically if the caller never called `close()` explicitly. The
constructor throws `ErrorOpeningFileForReadingException`,
`FileFormatNotSupportedException` or `RasterFileCacheFormat::UnsupportedVersion`
on a bad or unreadable file, so construction is not exception-safe to skip —
callers must be prepared to catch these on every load.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/RasterReader](RasterReader.md) | file-io | 20 |
| [property-values/ProxiedRasterResolver](../property-values/ProxiedRasterResolver.md) | property-values | 12 |
| [file-io/RasterFileCache](RasterFileCache.md) | file-io | 6 |
| [opengl/GLNormalMapSource](../opengl/GLNormalMapSource.md) | opengl | 2 |
| [opengl/GLAgeGridMaskSource](../opengl/GLAgeGridMaskSource.md) | opengl | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/MipmappedRasterFormatReader.h
python scripts/gpq.py def GPlatesFileIO::VersionOneReader --body
python scripts/gpq.py uses VersionOneReader --kind class
python scripts/gpq.py hier VersionOneReader
```
