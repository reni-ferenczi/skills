# RasterReader

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 400 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/RasterReader.h` | C++ | 330 |
| `src/file-io/RasterReader.cc` | C++ | 569 |

## Overview

[[[PROSE overview unit=file-io/RasterReader tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::FormatAccumulator`](#anonymousformataccumulator) | class | — | — | 0 | — |
| [`GPlatesFileIO::RasterReader`](#gplatesfileiorasterreader) | class | [`GPlatesUtils::ReferenceCount<RasterReader>`](../utils/ReferenceCount.md) | — | 0 | — |
| [`GPlatesFileIO::RasterReaderImpl`](#gplatesfileiorasterreaderimpl) | class | `boost::noncopyable` | — | 2 | — |

## Members

### `(anonymous)::FormatAccumulator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FormatAccumulator( std::map<QString, QStringList> &descriptions_to_ext)` | constructor | `None` | public | — |
| `operator()( const std::pair<const QString, RasterReader::FormatInfo> &format)` | operator | `void` | public | — |
| `d_descriptions_to_ext` | field | `std::map<QString, QStringList>` | private | — |

### `GPlatesFileIO::RasterReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<RasterReader>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const RasterReader>` | public | — |
| `FormatHandler` | enum | `None` | public | Libraries that we use to read in rasters. |
| `FormatInfo` | struct | `None` | public | Holds information about a supported format. |
| `create( const QString &filename, ReadErrorAccumulation *read_errors = NULL)` | method | `non_null_ptr_type` | public | Returns a RasterReader to read data from filename. |
| `get_filename` | field | `QString` | public | Returns the filename of the file that the RasterReader was created with. |
| `can_read()` | method | `bool` | public | Returns whether the file, as given in the constructor, is capable of yielding any raster data at all. |
| `get_georeferencing()` | method | `boost::optional<GPlatesPropertyValues::Georeferencing::non_null_ptr_to_const_type>` | public | Returns the georeferencing of pixel/line raster data to georeference coordinates. |
| `get_spatial_reference_system()` | method | `boost::optional<GPlatesPropertyValues::SpatialReferenceSystem::non_null_ptr_to_const_type>` | public | Returns the raster's spatial reference system. |
| `get_number_of_bands( ReadErrorAccumulation *read_errors = NULL)` | method | `unsigned int` | public | Returns the number of bands in the raster. |
| `get_size( ReadErrorAccumulation *read_errors = NULL)` | method | `std::pair<unsigned int, unsigned int>` | public | Returns the size (width by height) of the raster. |
| `get_type( unsigned int band_number, ReadErrorAccumulation *read_errors = NULL)` | method | `GPlatesPropertyValues::RasterType::Type` | public | Returns the data type of the given band\_number. band\_number must be between 1 and get\_number\_of\_bands inclusive. |
| `get_proxied_raw_raster( unsigned int band_number, ReadErrorAccumulation *read_errors = NULL)` | method | `boost::optional<GPlatesPropertyValues::RawRaster::non_null_ptr_type>` | public | Returns a proxied RawRaster, that can be used to get actual data from the given band\_number at a later time. band\_number must be between 1 and get\_number\_of\_bands inclusive. |
| `get_raw_raster( unsigned int band_number, const QRect &region = QRect(), ReadErrorAccumulation *read_errors = NULL)` | method | `boost::optional<GPlatesPropertyValues::RawRaster::non_null_ptr_type>` | public | Returns a non-proxied RawRaster, that contains data from the given region in the given band\_number. |
| `create_raster_band_reader_handle( unsigned int band_number)` | method | `RasterBandReaderHandle` | public | Same interface but for the specified raster band. |
| `get_supported_formats()` | method | `std::map<QString, FormatInfo>` | public | Retrieves information about formats supported when reading rasters. |
| `get_supported_formats( FormatHandler format_handler)` | method | `std::map<QString, FormatInfo>` | public | Retrieves information about formats supported by format\_handler when reading rasters. |
| `get_file_dialog_filters()` | method | `QString` | public | Gets a string that can be used as the filter string in a QFileDialog. |
| `get_file_dialog_filters( FormatHandler format_handler)` | method | `QString` | public | Gets a string that can be used as the filter string in a QFileDialog. |
| `RasterReader( const QString &filename, ReadErrorAccumulation *read_errors)` | constructor | `None` | private | — |
| `d_impl` | field | `boost::scoped_ptr<RasterReaderImpl>` | private | — |
| `d_filename` | field | `QString` | private | — |

### `GPlatesFileIO::RasterReaderImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~RasterReaderImpl()` | destructor | `None` | public | — |
| `can_read()` | method | `bool` | public | — |
| `get_georeferencing()` | method | `boost::optional<GPlatesPropertyValues::Georeferencing::non_null_ptr_to_const_type>` | public | — |
| `get_spatial_reference_system()` | method | `boost::optional<GPlatesPropertyValues::SpatialReferenceSystem::non_null_ptr_to_const_type>` | public | — |
| `get_number_of_bands( ReadErrorAccumulation *read_errors)` | method | `unsigned int` | public | — |
| `get_size( ReadErrorAccumulation *read_errors)` | method | `std::pair<unsigned int, unsigned int>` | public | — |
| `get_proxied_raw_raster( unsigned int band_number, ReadErrorAccumulation *read_errors)` | method | `boost::optional<GPlatesPropertyValues::RawRaster::non_null_ptr_type>` | public | — |
| `get_raw_raster( unsigned int band_number, const QRect &region, ReadErrorAccumulation *read_errors)` | method | `boost::optional<GPlatesPropertyValues::RawRaster::non_null_ptr_type>` | public | — |
| `get_type( unsigned int band_number, ReadErrorAccumulation *read_errors)` | method | `GPlatesPropertyValues::RasterType::Type` | public | — |
| `RasterReaderImpl( RasterReader *raster_reader)` | constructor | `None` | protected | — |
| `create_raster_band_reader_handle( unsigned int band_number)` | method | `RasterBandReaderHandle` | protected | — |
| `d_raster_reader` | field | `RasterReader` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `parse_filename( const QString filename, QString &root, int &time)` | function | `bool` | Returns true if the filename is of the required form (i.e. \<root\>-\<time\>.grd), and sets the value of time. |
| `transform_if( InputIterator begin, InputIterator end, OutputIterator result, UnaryOperator op, Predicate pred)` | function | `OutputIterator` | — |
| `add_supported_formats( std::map<QString, RasterReader::FormatInfo> &formats, RasterReader::FormatHandler format_handler)` | function | `void` | — |
| `create_file_dialog_filter_string( const QString &description, QStringList exts)` | function | `QString` | Creates a single entry in the filters string. |
| `create_file_dialog_filters_string( const std::map<QString, RasterReader::FormatInfo> &formats)` | function | `QString` | — |
| `GPLATES_FILEIO_RASTERREADER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/RasterReader tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GdalRasterReader](GdalRasterReader.md) | file-io | 30 |
| [opengl/GLNormalMapSource](../opengl/GLNormalMapSource.md) | opengl | 20 |
| [opengl/GLDataRasterSource](../opengl/GLDataRasterSource.md) | opengl | 19 |
| [file-io/RgbaRasterReader](RgbaRasterReader.md) | file-io | 17 |
| [opengl/GLScalarFieldDepthLayersSource](../opengl/GLScalarFieldDepthLayersSource.md) | opengl | 17 |
| [opengl/GLScalarField3DGenerator](../opengl/GLScalarField3DGenerator.md) | opengl | 16 |
| [property-values/ProxiedRasterCache](../property-values/ProxiedRasterCache.md) | property-values | 15 |
| [opengl/GLAgeGridMaskSource](../opengl/GLAgeGridMaskSource.md) | opengl | 14 |
| [opengl/GLVisualRasterSource](../opengl/GLVisualRasterSource.md) | opengl | 13 |
| [qt-widgets/ScalarField3DDepthLayersPage](../qt-widgets/ScalarField3DDepthLayersPage.md) | qt-widgets | 9 |
| [qt-widgets/ImportRasterDialog](../qt-widgets/ImportRasterDialog.md) | qt-widgets | 8 |
| [qt-widgets/TimeDependentRasterPage](../qt-widgets/TimeDependentRasterPage.md) | qt-widgets | 8 |
| [qt-widgets/ImportScalarField3DDialog](../qt-widgets/ImportScalarField3DDialog.md) | qt-widgets | 6 |
| [file-io/RasterBandReader](RasterBandReader.md) | file-io | 5 |
| [property-values/ProxiedRasterResolver](../property-values/ProxiedRasterResolver.md) | property-values | 5 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/RasterReader.h
python scripts/gpq.py def GPlatesFileIO::RasterReader --body
python scripts/gpq.py uses RasterReader --kind class
python scripts/gpq.py hier RasterReader
```
