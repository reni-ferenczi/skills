# RasterWriter

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 546 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/RasterWriter.h` | C++ | 353 |
| `src/file-io/RasterWriter.cc` | C++ | 327 |

## Overview

`RasterWriter` is the write-side counterpart of `RasterReader`: a
format-independent facade over `RgbaRasterWriter` and `GdalRasterWriter`,
selected in the constructor from the output filename's extension via
`get_format()`, and held behind the `RasterWriterImpl` interface in `d_impl`
so callers never see GDAL or image-library types. `create()` fixes the
raster's dimensions, band count and `RasterType::Type` up front; if the
extension is unsupported, or the format does not support the requested band
type, `d_impl` is left null and a warning is logged, mirroring `RasterReader`'s
null-impl-on-failure pattern.

Writing is a three-step protocol: `create()` opens the writer, repeated
`write_region_data()` calls fill in `RawRaster` regions band by band (regions
may be written in pieces, and a no-data value carried by the first region with
one becomes the no-data value for the whole band — later regions must agree
with it), and a single `write_file()` call at the end commits everything,
along with any georeferencing and spatial reference system set via
`set_georeferencing()`/`set_spatial_reference_system()`, to disk. RGBA format
handlers accept only one colour band; GDAL handlers accept one colour band
(stored internally as four R/G/B/A bands) or several non-colour bands, but
never a mix of band types within one raster.

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

`write_file()` must be called exactly once, at the end; skipping it means no
file is ever written, and calling `can_write()` afterwards is expected to
fail. Any raster region never touched by `write_region_data()` is left with
undefined pixel values rather than a default fill. Regions with a no-data
value must all agree on that value once one has been set on a band — a
mismatch is a caller bug the writer does not reconcile for you.

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
