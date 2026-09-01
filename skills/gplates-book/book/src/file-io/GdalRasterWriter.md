# GdalRasterWriter

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 431 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GdalRasterWriter.h` | C++ | 368 |
| `src/file-io/GdalRasterWriter.cc` | C++ | 999 |

## Overview

[[[PROSE overview unit=file-io/GdalRasterWriter tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::GDALRasterWriter`](#gplatesfileiogdalrasterwriter) | class | [`RasterWriterImpl`](RasterWriter.md) | — | 0 | Writes colour and numerical rasters using GDAL with support for georeferencing and spatial reference systems. |

## Members

### `GPlatesFileIO::GDALRasterWriter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `get_supported_formats( RasterWriter::supported_formats_type &supported_formats)` | method | `void` | public | Adds information about the formats supported by this writer. |
| `GDALRasterWriter( const QString &filename, const RasterWriter::FormatInfo &format_info, unsigned int raster_width, unsigned int raster_height, unsigned int num_raster_bands, GPlatesPropertyValues::RasterType::Type raster_band_type, bool compress = false)` | constructor | `None` | public | — |
| `~GDALRasterWriter()` | destructor | `None` | public | — |
| `can_write()` | method | `bool` | public | — |
| `set_georeferencing( const GPlatesPropertyValues::Georeferencing::non_null_ptr_to_const_type &georeferencing)` | method | `void` | public | — |
| `set_spatial_reference_system( const GPlatesPropertyValues::SpatialReferenceSystem::non_null_ptr_to_const_type& srs)` | method | `void` | public | — |
| `write_region_data( const GPlatesPropertyValues::RawRaster::non_null_ptr_type &region_data, unsigned int band_number, unsigned int x_offset, unsigned int y_offset)` | method | `bool` | public | — |
| `write_file()` | method | `bool` | public | — |
| `WriteNumericalRegionDataVisitorImpl` | class | `None` | private | Visits a numerical raw raster and writes its data to our (in-memory) raster. |
| `WriteNumericalRegionDataVisitor` | typedef | `GPlatesPropertyValues::TemplatedRawRasterVisitor<WriteNumericalRegionDataVisitorImpl>` | private | — |
| `InternalFormatInfo` | class | `None` | private | Information not contained in GPlatesFileIO::RasterWriter::FormatInfo. |
| `format_desc_to_internal_format_info_map_type` | typedef | `std::map<QString, InternalFormatInfo>` | private | Map format descriptions to internal format information. |
| `s_format_desc_to_internal_format_info_map` | field | `format_desc_to_internal_format_info_map_type` | private | Track internal format information by the format description. |
| `add_supported_format( GPlatesFileIO::RasterWriter::supported_formats_type &supported_formats, const QString &filename_extension, const QString &format_description, const QString &format_mime_type, const InternalFormatInfo &internal_format_info)` | method | `void` | private | Adds the supported format information and records format-description to internal format info mapping. |
| `get_internal_format_info` | field | `InternalFormatInfo` | private | Finds the internal format info from format description. |
| `write_colour_region_data( GPlatesPropertyValues::RawRaster &region_data, unsigned int x_offset, unsigned int y_offset)` | method | `bool` | private | — |
| `write_numerical_region_data( GPlatesPropertyValues::RawRaster &region_data, unsigned int band_number, unsigned int x_offset, unsigned int y_offset)` | method | `bool` | private | — |
| `d_filename` | field | `QString` | private | — |
| `d_num_raster_bands` | field | `unsigned int` | private | — |
| `d_raster_band_type` | field | `GPlatesPropertyValues::RasterType::Type` | private | — |
| `d_compress` | field | `bool` | private | — |
| `d_raster_band_no_data_values` | field | `std::vector< boost::optional<double> >` | private | The optional no-data value for each raster band. |
| `d_internal_format_info` | field | `InternalFormatInfo` | private | Extra information concerning the raster format being written. |
| `d_in_memory_dataset` | field | `GDALDataset` | private | Handle to the in-memory buffer. |
| `d_file_driver` | field | `GDALDriver` | private | Used to copy the in-memory dataset to the file. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_gdal_type_from_raster_type( GPlatesPropertyValues::RasterType::Type raster_type)` | function | `GDALDataType` | — |
| `does_driver_support_creation( const char *driver_name)` | function | `bool` | Returns true if the driver can create files (supports 'CREATECOPY'). |
| `get_supported_band_types( const char *driver_name)` | function | `std::vector<GPlatesPropertyValues::RasterType::Type>` | Determines which GDAL data (band) types are supported by the specified GDAL driver. |
| `s_format_desc_to_internal_format_info_map` | variable | `GPlatesFileIO::GDALRasterWriter::format_desc_to_internal_format_info_map_type` | — |
| `GPLATES_FILE_IO_GDALRASTERWRITER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/GdalRasterWriter tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/RasterWriter](RasterWriter.md) | file-io | 30 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GdalRasterWriter.h
python scripts/gpq.py def GPlatesFileIO::GDALRasterWriter --body
python scripts/gpq.py uses GDALRasterWriter --kind class
python scripts/gpq.py hier GDALRasterWriter
```
