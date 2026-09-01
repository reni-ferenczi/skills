# RgbaRasterWriter

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 860 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/RgbaRasterWriter.h` | C++ | 98 |
| `src/file-io/RgbaRasterWriter.cc` | C++ | 228 |

## Overview

[[[PROSE overview unit=file-io/RgbaRasterWriter tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::RgbaRasterWriter`](#gplatesfileiorgbarasterwriter) | class | [`RasterWriterImpl`](RasterWriter.md) | — | 0 | Writes RGBA rasters (with \*no\* support for georeferencing or spatial reference systems). |

## Members

### `GPlatesFileIO::RgbaRasterWriter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `get_supported_formats( RasterWriter::supported_formats_type &supported_formats)` | method | `void` | public | Adds information about the formats supported by this writer. |
| `RgbaRasterWriter( const QString &filename, const RasterWriter::FormatInfo &format_info, unsigned int raster_width, unsigned int raster_height, unsigned int num_raster_bands, GPlatesPropertyValues::RasterType::Type raster_band_type, bool compress = false)` | constructor | `None` | public | — |
| `can_write()` | method | `bool` | public | — |
| `set_georeferencing( const GPlatesPropertyValues::Georeferencing::non_null_ptr_to_const_type &georeferencing)` | method | `void` | public | — |
| `set_spatial_reference_system( const GPlatesPropertyValues::SpatialReferenceSystem::non_null_ptr_to_const_type& srs)` | method | `void` | public | — |
| `write_region_data( const GPlatesPropertyValues::RawRaster::non_null_ptr_type &region_data, unsigned int band_number, unsigned int x_offset, unsigned int y_offset)` | method | `bool` | public | — |
| `write_file()` | method | `bool` | public | — |
| `d_filename` | field | `QString` | private | — |
| `d_image` | field | `QImage` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILE_IO_RGBARASTERWRITER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/RgbaRasterWriter tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/RasterWriter](RasterWriter.md) | file-io | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/RgbaRasterWriter.h
python scripts/gpq.py def GPlatesFileIO::RgbaRasterWriter --body
python scripts/gpq.py uses RgbaRasterWriter --kind class
python scripts/gpq.py hier RgbaRasterWriter
```
