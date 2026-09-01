# RasterWriter

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 546 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/RasterWriter.h` | C++ | 353 |
| `src/file-io/RasterWriter.cc` | C++ | 327 |

## Overview

[[[PROSE overview unit=file-io/RasterWriter tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::RasterWriter`](#gplatesfileiorasterwriter) | class | [`GPlatesUtils::ReferenceCount<RasterWriter>`](../utils/ReferenceCount.md) | — | 0 | — |
| [`GPlatesFileIO::RasterWriterImpl`](#gplatesfileiorasterwriterimpl) | class | `boost::noncopyable` | — | 2 | — |

## Members

### `GPlatesFileIO::RasterWriter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<RasterWriter>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const RasterWriter>` | public | — |
| `FormatHandler` | enum | `None` | public | Libraries that we use to write out rasters. |
| `FormatInfo` | struct | `None` | public | Holds information about a supported format. |
| `supported_formats_type` | typedef | `std::map<QString, FormatInfo>` | public | Typedef for a map of filename extensions for format information. |
| `get_supported_formats` | field | `supported_formats_type` | public | Retrieves information about formats supported when writing rasters. |
| `get_format( const QString &filename)` | method | `boost::optional<const FormatInfo &>` | public | Retrieves the file format information that would be used to write a raster to filename, or none if the filename extension is not supported. |
| `create( const QString &filename, unsigned int raster_width, unsigned int raster_height, unsigned int num_raster_bands, GPlatesPropertyValues::RasterType::Type raster_band_type, bool compress = false)` | method | `non_null_ptr_type` | public | Returns a RasterWriter to write data of the specified dimensions to filename. raster\_band\_type should match one of the band types supported by the file format. |
| `can_write()` | method | `bool` | public | Returns whether any data can be written to the internal buffer. |
| `get_filename` | field | `QString` | public | Returns the filename of the file that the RasterWriter was created with. |
| `get_size()` | method | `std::pair<unsigned int, unsigned int>` | public | Returns the size (width by height) of the raster. |
| `get_number_of_bands()` | method | `unsigned int` | public | Returns the number of bands as specified to create. |
| `get_raster_band_type()` | method | `GPlatesPropertyValues::RasterType::Type` | public | Returns the raster type of each band. |
| `set_georeferencing( const GPlatesPropertyValues::Georeferencing::non_null_ptr_to_const_type &georeferencing)` | method | `void` | public | Sets the georeferencing of pixel/line raster data. |
| `set_spatial_reference_system( const GPlatesPropertyValues::SpatialReferenceSystem::non_null_ptr_to_const_type& srs)` | method | `void` | public | Sets the raster's spatial reference system. |
| `write_region_data( const GPlatesPropertyValues::RawRaster::non_null_ptr_type &region_data, unsigned int band_number, unsigned int x_offset = 0, unsigned int y_offset = 0)` | method | `bool` | public | Writes the non-proxied RawRaster data region\_data to the specified offset (in the raster) of the specified band. |
| `write_file()` | method | `bool` | public | The final write to the filename passed into create. |
| `RasterWriter( const QString &filename, unsigned int raster_width, unsigned int raster_height, unsigned int num_raster_bands, GPlatesPropertyValues::RasterType::Type raster_band_type, bool compress)` | constructor | `None` | private | — |
| `d_impl` | field | `boost::scoped_ptr<RasterWriterImpl>` | private | — |
| `d_filename` | field | `QString` | private | — |
| `d_width` | field | `unsigned int` | private | — |
| `d_height` | field | `unsigned int` | private | — |
| `d_num_bands` | field | `unsigned int` | private | — |
| `d_band_type` | field | `GPlatesPropertyValues::RasterType::Type` | private | — |

### `GPlatesFileIO::RasterWriterImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~RasterWriterImpl()` | destructor | `None` | public | — |
| `can_write()` | method | `bool` | public | — |
| `set_georeferencing( const GPlatesPropertyValues::Georeferencing::non_null_ptr_to_const_type &georeferencing)` | method | `void` | public | — |
| `set_spatial_reference_system( const GPlatesPropertyValues::SpatialReferenceSystem::non_null_ptr_to_const_type& srs)` | method | `void` | public | — |
| `write_region_data( const GPlatesPropertyValues::RawRaster::non_null_ptr_type &region_data, unsigned int band_number, unsigned int x_offset, unsigned int y_offset)` | method | `bool` | public | — |
| `write_file()` | method | `bool` | public | — |
| `RasterWriterImpl()` | constructor | `None` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `add_supported_formats( RasterWriter::supported_formats_type &supported_formats, RasterWriter::FormatHandler format_handler)` | function | `void` | — |
| `GPLATES_FILE_IO_RASTERWRITER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/RasterWriter tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/RgbaRasterWriter](RgbaRasterWriter.md) | file-io | 51 |
| [file-io/GdalRasterWriter](GdalRasterWriter.md) | file-io | 31 |
| [gui/ExportAnimationRegistry](../gui/ExportAnimationRegistry.md) | gui | 29 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 16 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/RasterWriter.h
python scripts/gpq.py def GPlatesFileIO::RasterWriter --body
python scripts/gpq.py uses RasterWriter --kind class
python scripts/gpq.py hier RasterWriter
```
