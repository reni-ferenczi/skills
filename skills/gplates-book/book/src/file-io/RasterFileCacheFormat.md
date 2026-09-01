# RasterFileCacheFormat

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 385 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/RasterFileCacheFormat.h` | C++ | 422 |
| `src/file-io/RasterFileCacheFormat.cc` | C++ | 459 |

## Overview

[[[PROSE overview unit=file-io/RasterFileCacheFormat tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::(anonymous)::GetColourPaletteIdVisitor`](#gplatesfileioanonymousgetcolourpaletteidvisitor) | class | `boost::static_visitor<boost::optional<std::size_t> >` | — | 0 | — |
| [`GPlatesFileIO::RasterFileCacheFormat::Type`](#gplatesfileiorasterfilecacheformattype) | enum | — | — | 0 | The type of raster used to store. |
| [`GPlatesFileIO::RasterFileCacheFormat::LevelInfo`](#gplatesfileiorasterfilecacheformatlevelinfo) | struct | — | — | 0 | Information for the size and file location of a level (base or mipmap) of the mipmap pyramid. |
| [`GPlatesFileIO::RasterFileCacheFormat::BlockInfo`](#gplatesfileiorasterfilecacheformatblockinfo) | struct | — | — | 0 | Information for a block of encoded data. |
| [`GPlatesFileIO::RasterFileCacheFormat::BlockInfos`](#gplatesfileiorasterfilecacheformatblockinfos) | class | — | — | 0 | Keeps track of encoded blocks within an image. |
| [`GPlatesFileIO::RasterFileCacheFormat::UnsupportedVersion`](#gplatesfileiorasterfilecacheformatunsupportedversion) | class | [`GPlatesGlobal::Exception`](../global/GPlatesException.md) | — | 0 | Thrown when reading a file containing an unrecognised version number. |

## Members

### `GPlatesFileIO::(anonymous)::GetColourPaletteIdVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator()( const GPlatesGui::RasterColourPalette::empty &)` | operator | `boost::optional<std::size_t>` | public | — |
| `operator()( const GPlatesUtils::non_null_intrusive_ptr<ColourPaletteType> &colour_palette)` | operator | `boost::optional<std::size_t>` | public | — |

### `GPlatesFileIO::RasterFileCacheFormat::Type`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RGBA` | enumerator | `None` | — | — |
| `FLOAT` | enumerator | `None` | — | — |
| `DOUBLE` | enumerator | `None` | — | — |
| `UINT8` | enumerator | `None` | — | — |
| `UINT16` | enumerator | `None` | — | — |
| `INT16` | enumerator | `None` | — | — |
| `UINT32` | enumerator | `None` | — | — |
| `INT32` | enumerator | `None` | — | — |
| `NUM_TYPES` | enumerator | `None` | — | — |

### `GPlatesFileIO::RasterFileCacheFormat::LevelInfo`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `width` | field | `quint32` | public | — |
| `height` | field | `quint32` | public | — |
| `blocks_file_offset` | field | `quint64` | public | — |
| `num_blocks` | field | `quint32` | public | — |
| `STREAM_SIZE` | field | `unsigned int` | public | Size of sum of individual data members. |

### `GPlatesFileIO::RasterFileCacheFormat::BlockInfo`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `x_offset` | field | `quint32` | public | Pixel offsets locating block within the image of the source (or mipmapped) raster. |
| `y_offset` | field | `quint32` | public | Pixel offsets locating block within the image of the source (or mipmapped) raster. |
| `width` | field | `quint32` | public | Most blocks have BLOCK\_SIZE dimensions except those at right and bottom edges of source raster. |
| `height` | field | `quint32` | public | Most blocks have BLOCK\_SIZE dimensions except those at right and bottom edges of source raster. |
| `main_offset` | field | `quint64` | public | Offset within level of encoded data for the source (or mipmapped) raster. |
| `coverage_offset` | field | `quint64` | public | Offset within level of encoded data for the coverage (or mipmapped) raster. |
| `STREAM_SIZE` | field | `unsigned int` | public | Size of sum of individual data members. |

### `GPlatesFileIO::RasterFileCacheFormat::BlockInfos`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `BlockInfos( unsigned int image_width, unsigned int image_height)` | constructor | `None` | public | Constructor allocates \*un-initialised\* BlockInfo structures. |
| `get_num_blocks()` | method | `unsigned int` | public | Returns the number of blocks. |
| `get_block_info` | field | `BlockInfo` | public | Returns specified block. |
| `d_num_blocks_in_x_direction` | field | `unsigned int` | private | — |
| `d_num_blocks_in_y_direction` | field | `unsigned int` | private | — |
| `d_block_infos` | field | `std::vector<BlockInfo>` | private | — |

### `GPlatesFileIO::RasterFileCacheFormat::UnsupportedVersion`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UnsupportedVersion( const GPlatesUtils::CallStack::Trace &exception_source, quint32 unrecognised_version)` | constructor | `None` | public | — |
| `unrecognised_version()` | method | `quint32` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_unrecognised_version` | field | `quint32` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `RASTER_FILE_CACHE_EXTENSION` | variable | `QString` | All raster file caches have filenames that end with this. |
| `make_mipmap_filename_in_same_directory( const QString &source_filename, unsigned int band_number, boost::optional<std::size_t> colour_palette_id = boost::none)` | function | `QString` | — |
| `make_mipmap_filename_in_tmp_directory( const QString &source_filename, unsigned int band_number, boost::optional<std::size_t> colour_palette_id = boost::none)` | function | `QString` | — |
| `make_source_filename_in_same_directory( const QString &source_filename, unsigned int band_number)` | function | `QString` | — |
| `make_source_filename_in_tmp_directory( const QString &source_filename, unsigned int band_number)` | function | `QString` | — |
| `get_type_as_enum()` | function | `Type` | — |
| `GPLATES_FILEIO_RASTERFILECACHEFORMAT_H` | macro | `None` | — |
| `MAGIC_NUMBER` | variable | `boost::uint8_t` | The magic number that identifies a file as GPlates. |
| `VERSION_NUMBER` | variable | `boost::uint32_t` | The current version number of the GPlates raster file cache format. |
| `BLOCK_SIZE` | variable | `unsigned int` | The block size is the value is dimension of square blocks of image data, in the raster file cache, containing BLOCK\_SIZE x BLOCK\_SIZE pixels of data. |
| `Q_DATA_STREAM_VERSION` | variable | `int` | The QDataStream serialisation version. |
| `get_number_of_mipmapped_levels( const unsigned int source_raster_width, const unsigned int source_raster_height)` | function | `unsigned int` | Returns the number of mipmapped levels in total needed for a source raster of the specified dimensions. |
| `get_mipmap_dimensions( unsigned int &mipmap_width, unsigned int &mipmap_height, unsigned int mipmap_level, const unsigned int source_raster_width, const unsigned int source_raster_height)` | function | `void` | Returns the mipmap image dimensions for the specified source raster dimensions and mipmap level. |
| `get_writable_mipmap_cache_filename( const QString &source_filename, unsigned int band_number, boost::optional<std::size_t> colour_palette_id = boost::none)` | function | `boost::optional<QString>` | Returns the filename of a file that can be used for writing out a mipmaps file for the given source\_filename. |
| `get_existing_mipmap_cache_filename( const QString &source_filename, unsigned int band_number, boost::optional<std::size_t> colour_palette_id = boost::none)` | function | `boost::optional<QString>` | Returns the filename of an existing mipmap file for the given source\_filename, if any. |
| `get_writable_source_cache_filename( const QString &source_filename, unsigned int band_number)` | function | `boost::optional<QString>` | Returns the filename of a file that can be used for writing out a source raster file cache for the given source\_filename. |
| `get_existing_source_cache_filename( const QString &source_filename, unsigned int band_number)` | function | `boost::optional<QString>` | Returns the filename of an existing source raster file cache for the given source\_filename, if any. |
| `get_colour_palette_id( const GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type &colour_palette = GPlatesGui::RasterColourPalette::create())` | function | `boost::optional<std::size_t>` | Gets the colour palette id for the given colour\_palette. |

## Notes

[[[PROSE notes unit=file-io/RasterFileCacheFormat tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GdalRasterReader](GdalRasterReader.md) | file-io | 151 |
| [file-io/MipmappedRasterFormatWriter](MipmappedRasterFormatWriter.md) | file-io | 121 |
| [file-io/RgbaRasterReader](RgbaRasterReader.md) | file-io | 117 |
| [file-io/RasterFileCacheFormatReader](RasterFileCacheFormatReader.md) | file-io | 38 |
| [file-io/MipmappedRasterFormatReader](MipmappedRasterFormatReader.md) | file-io | 32 |
| [file-io/RasterFileCache](RasterFileCache.md) | file-io | 20 |
| [unit-test/MipmapperTest](../unit-test/MipmapperTest.md) | unit-test | 19 |
| [file-io/SourceRasterFileCacheFormatReader](SourceRasterFileCacheFormatReader.md) | file-io | 15 |
| [qt-widgets/ScalarField3DDepthLayersPage](../qt-widgets/ScalarField3DDepthLayersPage.md) | qt-widgets | 11 |
| [property-values/ProxiedRasterResolver](../property-values/ProxiedRasterResolver.md) | property-values | 10 |
| [file-io/RasterReader](RasterReader.md) | file-io | 9 |
| [qt-widgets/ImportScalarField3DDialog](../qt-widgets/ImportScalarField3DDialog.md) | qt-widgets | 5 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/RasterFileCacheFormat.h
python scripts/gpq.py def GPlatesFileIO::RasterFileCacheFormat::BlockInfos --body
python scripts/gpq.py uses BlockInfos --kind class
python scripts/gpq.py hier BlockInfos
```
