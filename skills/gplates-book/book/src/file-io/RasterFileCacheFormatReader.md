# RasterFileCacheFormatReader

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 749 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/RasterFileCacheFormatReader.h` | C++ | 516 |

## Overview

[[[PROSE overview unit=file-io/RasterFileCacheFormatReader tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::RasterFileCacheFormatReader`](#gplatesfileiorasterfilecacheformatreader) | class | — | `<class RawRasterType>` | 0 | Reads an image stored in a raster file cache by traversing a Hilbert curve of encoded blocks of raster data stored in the file. |

## Members

### `GPlatesFileIO::RasterFileCacheFormatReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RasterFileCacheFormatReader( quint32 version_number, QFile &file, QDataStream &in, unsigned int image_width, unsigned int image_height, unsigned int num_blocks, bool has_coverage)` | constructor | `None` | public | — |
| `~RasterFileCacheFormatReader()` | destructor | `None` | public | — |
| `read_raster( unsigned int x_offset, unsigned int y_offset, unsigned int width, unsigned int height)` | method | `boost::optional<typename RawRasterType::non_null_ptr_type>` | public | Reads the given region from the raster file cache. |
| `read_coverage( unsigned int x_offset, unsigned int y_offset, unsigned int width, unsigned int height)` | method | `boost::optional<GPlatesPropertyValues::CoverageRawRaster::non_null_ptr_type>` | public | Reads the given region from the raster file cache as a coverage. |
| `raster_element_type` | typedef | `typename RawRasterType::element_type` | private | — |
| `SortByFileOffset` | class | `None` | private | Used to sort blocks by file offset. |
| `is_valid_region( unsigned int x_offset, unsigned int y_offset, unsigned int width, unsigned int height)` | method | `bool` | private | — |
| `copy_region( T *region_data, unsigned int region_x_offset, unsigned int region_y_offset, unsigned int region_width, unsigned int region_height, const RasterFileCacheFormat::BlockInfos &block_infos, // Determines whether to use image file offset or coverage file offset... quint64 RasterFileCacheFormat::BlockInfo::*encod ...` | method | `void` | private | — |
| `copy_block_data_into_region( T *region_data, const unsigned int region_x_offset, const unsigned int region_y_offset, const unsigned int region_width, const unsigned int region_height, const T *block_data, const unsigned int block_x_offset, const unsigned int block_y_offset, const unsigned int block_width, const unsigne ...` | method | `void` | private | — |
| `read_block_data( T *data, unsigned int num_elements)` | method | `void` | private | — |
| `d_file` | field | `QFile` | private | — |
| `d_in` | field | `QDataStream` | private | — |
| `d_image_width` | field | `unsigned int` | private | — |
| `d_image_height` | field | `unsigned int` | private | — |
| `d_has_coverage` | field | `bool` | private | — |
| `d_block_infos` | field | `RasterFileCacheFormat::BlockInfos` | private | — |
| `d_no_data_value` | field | `boost::optional<raster_element_type>` | private | — |
| `d_raster_statistics` | field | `boost::optional<GPlatesPropertyValues::RasterStatistics>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILE_IO_RASTERFILECACHEFORMATREADER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/RasterFileCacheFormatReader tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/MipmappedRasterFormatReader](MipmappedRasterFormatReader.md) | file-io | 5 |
| [file-io/SourceRasterFileCacheFormatReader](SourceRasterFileCacheFormatReader.md) | file-io | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/RasterFileCacheFormatReader.h
python scripts/gpq.py def GPlatesFileIO::RasterFileCacheFormatReader --body
python scripts/gpq.py uses RasterFileCacheFormatReader --kind class
python scripts/gpq.py hier RasterFileCacheFormatReader
```
