# GdalRasterReader

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 136 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GdalRasterReader.h` | C++ | 428 |
| `src/file-io/GdalRasterReader.cc` | C++ | 2387 |

## Overview

[[[PROSE overview unit=file-io/GdalRasterReader tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::ConvertIntegerBandsToRgbaPixels`](#anonymousconvertintegerbandstorgbapixels) | struct | — | `<typename RasterBandElementType, bool is_integer_signed>` | 0 | Handle conversion of 4-band integer data (of type RasterBandElementType that is larger than a byte) to 4-byte RGBA data. |
| [`(anonymous)::ConvertIntegerBandsToRgbaPixels<RasterBandElementType, true>`](#anonymousconvertintegerbandstorgbapixelsrasterbandelementtype-true) | struct | — | `<typename RasterBandElementType>` | 0 | This specialisation handles case where RasterBandElementType is a \*signed\* integer type. |
| [`(anonymous)::ConvertRgbaBandData`](#anonymousconvertrgbabanddata) | struct | — | `<typename RasterBandElementType, bool is_floating_point>` | 0 | Utilities to handle conversion of RGBA data. |
| [`(anonymous)::ConvertRgbaBandData<RasterBandElementType, true>`](#anonymousconvertrgbabanddatarasterbandelementtype-true) | struct | — | `<typename RasterBandElementType>` | 0 | — |
| [`GPlatesFileIO::GDALRasterReader`](#gplatesfileiogdalrasterreader) | class | [`RasterReaderImpl`](RasterReader.md) | — | 0 | Reads rasters using GDAL. |

## Members

### `(anonymous)::ConvertIntegerBandsToRgbaPixels`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `convert( GPlatesGui::rgba8_t *const dst_pixels, const RasterBandElementType *const src_rgba_pixels, unsigned int num_pixels)` | method | `void` | public | — |

### `(anonymous)::ConvertIntegerBandsToRgbaPixels<RasterBandElementType, true>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `convert( GPlatesGui::rgba8_t *const dst_pixels, const RasterBandElementType *const src_rgba_pixels, unsigned int num_pixels)` | method | `void` | public | — |

### `(anonymous)::ConvertRgbaBandData`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `make_no_data_pixels_transparent( RasterBandElementType *const rgba_pixels, unsigned int num_pixels, const RasterBandElementType red_no_data_value, const RasterBandElementType green_no_data_value, const RasterBandElementType blue_no_data_value, const RasterBandElementType alpha_no_data_value)` | method | `void` | public | Set the alpha channel to zero (ie, make transparent) any pixels that match the RGBA no-data value. |
| `convert_to_rgba8_pixels( GPlatesGui::rgba8_t *const dst_pixels, const RasterBandElementType *const src_rgba_pixels, unsigned int num_pixels)` | method | `void` | public | RasterBandElementType is larger than a byte so we convert to byte. |

### `(anonymous)::ConvertRgbaBandData<RasterBandElementType, true>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `make_no_data_pixels_transparent( RasterBandElementType *const rgba_pixels, unsigned int num_pixels, const RasterBandElementType red_no_data_value, const RasterBandElementType green_no_data_value, const RasterBandElementType blue_no_data_value, const RasterBandElementType alpha_no_data_value)` | method | `void` | public | Set the alpha channel to zero (ie, make transparent) any pixels that match the RGBA no-data value. |
| `convert_to_rgba8_pixels( GPlatesGui::rgba8_t *const dst_pixels, const RasterBandElementType *const src_rgba_pixels, unsigned int num_pixels)` | method | `void` | public | RasterBandElementType is larger than a byte so we convert to byte. |

### `GPlatesFileIO::GDALRasterReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GDALRasterReader( const QString &filename, RasterReader *raster_reader, ReadErrorAccumulation *read_errors)` | constructor | `None` | public | — |
| `~GDALRasterReader()` | destructor | `None` | public | — |
| `can_read()` | method | `bool` | public | — |
| `get_georeferencing()` | method | `boost::optional<GPlatesPropertyValues::Georeferencing::non_null_ptr_to_const_type>` | public | — |
| `get_spatial_reference_system()` | method | `boost::optional<GPlatesPropertyValues::SpatialReferenceSystem::non_null_ptr_to_const_type>` | public | — |
| `get_number_of_bands( ReadErrorAccumulation *read_errors)` | method | `unsigned int` | public | — |
| `get_size( ReadErrorAccumulation *read_errors)` | method | `std::pair<unsigned int, unsigned int>` | public | — |
| `get_proxied_raw_raster( unsigned int band_number, ReadErrorAccumulation *read_errors)` | method | `boost::optional<GPlatesPropertyValues::RawRaster::non_null_ptr_type>` | public | — |
| `get_raw_raster( unsigned int band_number, const QRect &region, ReadErrorAccumulation *read_errors)` | method | `boost::optional<GPlatesPropertyValues::RawRaster::non_null_ptr_type>` | public | — |
| `get_type( unsigned int band_number, ReadErrorAccumulation *read_errors)` | method | `GPlatesPropertyValues::RasterType::Type` | public | — |
| `RasterBand` | struct | `None` | private | Raster band information. |
| `initialise_source_raster_dimensions()` | method | `bool` | private | — |
| `is_colour_raster()` | method | `boost::optional<RasterBand::GDALRgbaBands>` | private | — |
| `report_recoverable_error( ReadErrorAccumulation *read_errors, ReadErrors::Description description)` | method | `void` | private | — |
| `report_failure_to_begin( ReadErrorAccumulation *read_errors, ReadErrors::Description description)` | method | `void` | private | — |
| `create_proxied_raw_raster( const RasterBand &raster_band, const GPlatesFileIO::RasterBandReaderHandle &raster_band_reader_handle, ReadErrorAccumulation *read_errors)` | method | `GPlatesPropertyValues::RawRaster::non_null_ptr_type` | private | — |
| `create_source_raster_file_cache_format_reader( RasterBand &raster_band, unsigned int band_number, ReadErrorAccumulation *read_errors)` | method | `boost::shared_ptr<GPlatesFileIO::SourceRasterFileCacheFormatReader>` | private | Creates a reader for the cached source raster. |
| `create_source_raster_file_cache_format_reader( RasterBand &raster_band, const QString &cache_filename, ReadErrorAccumulation *read_errors)` | method | `boost::shared_ptr<SourceRasterFileCacheFormatReader>` | private | — |
| `create_source_raster_file_cache( RasterBand &raster_band, unsigned int band_number, ReadErrorAccumulation *read_errors)` | method | `bool` | private | Creates a raster file cache for the source raster (returns false if unsuccessful). |
| `write_source_raster_file_cache( RasterBand &raster_band, const QString &cache_filename, ReadErrorAccumulation *read_errors)` | method | `void` | private | — |
| `write_source_raster_file_cache_image_data( RasterBand &raster_band, QFile &cache_file, QDataStream &out, RasterFileCacheFormat::BlockInfos &block_infos, ReadErrorAccumulation *read_errors, double &raster_min, double &raster_max, double &raster_sum, double &raster_sum_squares, qint64 &num_valid_raster_samples)` | method | `void` | private | — |
| `get_no_data_value( const RasterBand &raster_band, RasterElementType &no_data_value)` | method | `bool` | private | Returns the no-data value of the specified raster band. |
| `add_no_data_value( RawRasterType &raster, const RasterBand &raster_band)` | method | `void` | private | — |
| `get_statistics( RawRasterType &raster, const RasterBand &raster_band, ReadErrorAccumulation *read_errors)` | method | `boost::optional<GPlatesPropertyValues::RasterStatistics>` | private | — |
| `add_statistics( RawRasterType &raster, const RasterBand &raster_band, ReadErrorAccumulation *read_errors)` | method | `void` | private | — |
| `add_data( RasterElementType *result_buf, const RasterBand &raster_band, bool flip, unsigned int region_x_offset, unsigned int region_y_offset, unsigned int region_width, unsigned int region_height)` | method | `void` | private | — |
| `add_rgba_data( GPlatesGui::rgba8_t *result_buf, const RasterBand::GDALRgbaBands &gdal_rgba_raster_bands, bool flip, unsigned int region_x_offset, unsigned int region_y_offset, unsigned int region_width, unsigned int region_height)` | method | `void` | private | — |
| `read_data( const RasterBand &raster_band, bool flip, const QRect &region)` | method | `boost::optional<typename RawRasterType::non_null_ptr_type>` | private | — |
| `update_statistics( RawRasterType &source_region_data, double &raster_min, double &raster_max, double &raster_sum, double &raster_sum_squares, qint64 &num_valid_raster_samples)` | method | `void` | private | — |
| `hilbert_curve_traversal( RasterBand &raster_band, unsigned int depth, unsigned int read_source_raster_depth, unsigned int write_source_raster_depth, unsigned int x_offset, unsigned int y_offset, unsigned int dimension, unsigned int hilbert_start_point, unsigned int hilbert_end_point, QDataStream &out, RasterFileCacheFo ...` | method | `void` | private | Traverse the Hilbert curve of blocks of the source raster using quad-tree recursion. |
| `MIN_IMAGE_ALLOCATION_BYTES_TO_ATTEMPT` | field | `int` | private | The minimum image allocation size to attempt - any image allocation lower than this size that fails will result in a thrown exception. |
| `MAX_IMAGE_ALLOCATION_BYTES_TO_ATTEMPT` | field | `quint64` | private | The maximum memory allocation to attempt for an image. |
| `d_source_raster_filename` | field | `QString` | private | — |
| `d_dataset` | field | `GDALDataset` | private | Handle to the raster file. |
| `d_flip` | field | `bool` | private | GMT style GRDs are stored, and imported, upside-down. |
| `d_source_width` | field | `unsigned int` | private | — |
| `d_source_height` | field | `unsigned int` | private | — |
| `d_raster_bands` | field | `std::vector<RasterBand>` | private | — |
| `d_raster_band_file_cache_format_readers` | field | `std::vector<boost::shared_ptr<SourceRasterFileCacheFormatReader> >` | private | A source raster file cache reader for each raster band. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_raster_type_from_gdal_type( GDALDataType data_type)` | function | `GPlatesPropertyValues::RasterType::Type` | — |
| `get_gdal_type_from_raster_type( GPlatesPropertyValues::RasterType::Type raster_type)` | function | `GDALDataType` | — |
| `unpack_region( const QRect &region, int full_width, int full_height, unsigned int &region_x_offset, unsigned int &region_y_offset, unsigned int &region_width, unsigned int &region_height)` | function | `bool` | — |
| `GPLATES_FILEIO_GDALRASTERREADER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/GdalRasterReader tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [data-mining/deprecated/RegionOfInterestAssociationOperator](../data-mining/deprecated/RegionOfInterestAssociationOperator.md) | data-mining | 4 |
| [file-io/RasterReader](RasterReader.md) | file-io | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GdalRasterReader.h
python scripts/gpq.py def GPlatesFileIO::GDALRasterReader --body
python scripts/gpq.py uses GDALRasterReader --kind class
python scripts/gpq.py hier GDALRasterReader
```
