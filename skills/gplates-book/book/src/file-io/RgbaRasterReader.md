# RgbaRasterReader

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 583 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/RgbaRasterReader.h` | C++ | 214 |
| `src/file-io/RgbaRasterReader.cc` | C++ | 1034 |

## Overview

[[[PROSE overview unit=file-io/RgbaRasterReader tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::RgbaRasterReader`](#gplatesfileiorgbarasterreader) | class | [`RasterReaderImpl`](RasterReader.md) | — | 0 | Reads RGBA rasters. |

## Members

### `GPlatesFileIO::RgbaRasterReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RgbaRasterReader( const QString &filename, RasterReader *raster_reader, ReadErrorAccumulation *read_errors)` | constructor | `None` | public | — |
| `can_read()` | method | `bool` | public | — |
| `get_georeferencing()` | method | `boost::optional<GPlatesPropertyValues::Georeferencing::non_null_ptr_to_const_type>` | public | — |
| `get_spatial_reference_system()` | method | `boost::optional<GPlatesPropertyValues::SpatialReferenceSystem::non_null_ptr_to_const_type>` | public | — |
| `get_number_of_bands( ReadErrorAccumulation *read_errors)` | method | `unsigned int` | public | — |
| `get_size( ReadErrorAccumulation *read_errors)` | method | `std::pair<unsigned int, unsigned int>` | public | — |
| `get_proxied_raw_raster( unsigned int band_number, ReadErrorAccumulation *read_errors)` | method | `boost::optional<GPlatesPropertyValues::RawRaster::non_null_ptr_type>` | public | — |
| `get_raw_raster( unsigned int band_number, const QRect &region, ReadErrorAccumulation *read_errors)` | method | `boost::optional<GPlatesPropertyValues::RawRaster::non_null_ptr_type>` | public | — |
| `get_type( unsigned int band_number, ReadErrorAccumulation *read_errors)` | method | `GPlatesPropertyValues::RasterType::Type` | public | — |
| `report_recoverable_error( ReadErrorAccumulation *read_errors, ReadErrors::Description description)` | method | `void` | private | — |
| `report_failure_to_begin( ReadErrorAccumulation *read_errors, ReadErrors::Description description)` | method | `void` | private | — |
| `create_source_raster_file_cache_format_reader( ReadErrorAccumulation *read_errors)` | method | `void` | private | Creates a reader for the cached source raster. |
| `create_source_raster_file_cache( ReadErrorAccumulation *read_errors)` | method | `bool` | private | Creates a raster file cache for the source raster (returns false if unsuccessful). |
| `write_source_raster_file_cache( const QString &cache_filename, ReadErrorAccumulation *read_errors)` | method | `void` | private | — |
| `write_source_raster_file_cache_image_data( QFile &cache_file, QDataStream &out, RasterFileCacheFormat::BlockInfos &block_infos, ReadErrorAccumulation *read_errors)` | method | `void` | private | — |
| `hilbert_curve_traversal( unsigned int depth, unsigned int read_source_raster_depth, unsigned int write_source_raster_depth, unsigned int x_offset, unsigned int y_offset, unsigned int dimension, unsigned int hilbert_start_point, unsigned int hilbert_end_point, QDataStream &out, RasterFileCacheFormat::BlockInfos &block_i ...` | method | `void` | private | Traverse the Hilbert curve of blocks of the source raster using quad-tree recursion. |
| `read_source_raster_region( QImageReader &source_reader, const QRect &source_region, ReadErrorAccumulation *read_errors)` | method | `boost::shared_array<GPlatesGui::rgba8_t>` | private | Reads source raster from the specified region. |
| `MIN_IMAGE_ALLOCATION_BYTES_TO_ATTEMPT` | field | `int` | private | The minimum image allocation size to attempt - any image allocation lower than this size that fails will result in a thrown exception. |
| `MAX_IMAGE_ALLOCATION_BYTES_TO_ATTEMPT` | field | `quint64` | private | The maximum memory allocation to attempt for an image. |
| `d_source_raster_filename` | field | `QString` | private | — |
| `d_source_width` | field | `unsigned int` | private | — |
| `d_source_height` | field | `unsigned int` | private | — |
| `d_source_raster_file_cache_format_reader` | field | `boost::scoped_ptr<SourceRasterFileCacheFormatReader>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `unpack_region( const QRect &region, int full_width, int full_height, unsigned int &region_x_offset, unsigned int &region_y_offset, unsigned int &region_width, unsigned int &region_height)` | function | `bool` | — |
| `GPLATES_FILEIO_RGBARASTERREADER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/RgbaRasterReader tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/RasterReader](RasterReader.md) | file-io | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/RgbaRasterReader.h
python scripts/gpq.py def GPlatesFileIO::RgbaRasterReader --body
python scripts/gpq.py uses RgbaRasterReader --kind class
python scripts/gpq.py hier RgbaRasterReader
```
