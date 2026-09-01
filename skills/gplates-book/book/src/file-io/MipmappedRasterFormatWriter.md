# MipmappedRasterFormatWriter

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 150 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/MipmappedRasterFormatWriter.h` | C++ | 1318 |
| `src/file-io/MipmappedRasterFormatWriter.cc` | C++ | 62 |

## Overview

`MipmappedRasterFormatWriter` generates the on-disk mipmap cache files that
`file-io/MipmappedRasterFormatReader` reads back. The real writing logic
lives in `MipmappedRasterFormatWriterInternals::BaseMipmappedRasterFormatWriter<ProxiedRawRasterType, MipmapperType>`,
whose `write()` streams each mipmap level to its own `QTemporaryFile` first
(since block compression makes each level's final size unpredictable in
advance) and only concatenates them into the destination file once every
level has been generated, patching in the true total file size at the end so
a reader can detect a partially written file. Levels are produced by
`hilbert_curve_traversal`, a quad-tree recursion over the source raster's
blocks ordered along a Hilbert curve — the recursion's leaves are base-level
blocks, and each step back up the tree mipmaps its four children into one
parent block for the level above, so every mipmap level gets a Hilbert
ordering appropriate to its own block grid.

`MipmappedRasterFormatWriter<ProxiedRawRasterType, use_colour_palette, Enable>`
itself is deliberately left undefined and is specialised via `enable_if_c` on
the source raster's `element_type` and `has_no_data_value`, plus the
`use_colour_palette` flag (which only applies to integer rasters): one
specialisation for RGBA rasters with no no-data value, one for floating-point
rasters with a no-data value, and two for integer rasters with a no-data
value — one that mipmaps the integer data as floats (letting `GPlatesGui::Mipmapper`'s
integer specialisation do the int-to-float conversion), and one that first
converts the raster to RGBA via a `GPlatesGui::RasterColourPalette` and
mipmaps the colour data instead. All four specialisations share the same
constructor signature, including an unused `colour_palette` parameter where
it does not apply, purely so calling code can be written generically over
which specialisation gets instantiated.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::MipmappedRasterFormatWriterInternals::BaseMipmappedRasterFormatWriter`](#gplatesfileiomipmappedrasterformatwriterinternalsbasemipmappedrasterformatwriter) | class | — | `<class ProxiedRawRasterType, class MipmapperType>` | 4 | — |
| [`GPlatesFileIO::MipmappedRasterFormatWriter< ProxiedRawRasterType, false/*use_colour_palette*/, // Not applicable here typename boost::enable_if_c<!ProxiedRawRasterType::has_no_data_value && boost::is_same<typename ProxiedRawRasterType::element_type, GPlatesGui::rgba8_t>::value>::type >`](#gplatesfileiomipmappedrasterformatwriter-proxiedrawrastertype-falseuse_colour_palette--not-applicable-here-typename-boostenable_if_cproxiedrawrastertypehas_no_data_value--boostis_sametypename-proxiedrawrastertypeelement_type-gplatesguirgba8_tvaluetype-) | class | [`MipmappedRasterFormatWriterInternals::BaseMipmappedRasterFormatWriter< ProxiedRawRasterType, GPlatesGui::Mipmapper<GPlatesPropertyValues::Rgba8RawRaster> >`](MipmappedRasterFormatWriter.md) | `<class ProxiedRawRasterType>` | 0 | This specialisation is for rasters that have an element\_type of rgba8\_t and are without a no-data value. |
| [`GPlatesFileIO::MipmappedRasterFormatWriter< ProxiedRawRasterType, false/*use_colour_palette*/, // Not applicable here typename boost::enable_if_c<ProxiedRawRasterType::has_no_data_value && boost::is_floating_point<typename ProxiedRawRasterType::element_type>::value >::type >`](#gplatesfileiomipmappedrasterformatwriter-proxiedrawrastertype-falseuse_colour_palette--not-applicable-here-typename-boostenable_if_cproxiedrawrastertypehas_no_data_value--boostis_floating_pointtypename-proxiedrawrastertypeelement_typevalue-type-) | class | [`MipmappedRasterFormatWriterInternals::BaseMipmappedRasterFormatWriter< ProxiedRawRasterType, GPlatesGui::Mipmapper< typename GPlatesPropertyValues::RawRasterUtils ::ConvertProxiedRasterToUnproxiedRaster<ProxiedRawRasterType> ::unproxied_raster_type> >`](MipmappedRasterFormatWriter.md) | `<class ProxiedRawRasterType>` | 0 | This specialisation is for rasters that have a floating-point element\_type and that have a no-data value. |
| [`GPlatesFileIO::MipmappedRasterFormatWriter< ProxiedRawRasterType, false/*use_colour_palette*/, typename boost::enable_if_c<ProxiedRawRasterType::has_no_data_value && boost::is_integral<typename ProxiedRawRasterType::element_type>::value >::type >`](#gplatesfileiomipmappedrasterformatwriter-proxiedrawrastertype-falseuse_colour_palette-typename-boostenable_if_cproxiedrawrastertypehas_no_data_value--boostis_integraltypename-proxiedrawrastertypeelement_typevalue-type-) | class | [`MipmappedRasterFormatWriterInternals::BaseMipmappedRasterFormatWriter< ProxiedRawRasterType, GPlatesGui::Mipmapper< typename GPlatesPropertyValues::RawRasterUtils ::ConvertProxiedRasterToUnproxiedRaster<ProxiedRawRasterType> ::unproxied_raster_type> >`](MipmappedRasterFormatWriter.md) | `<class ProxiedRawRasterType>` | 0 | This specialisation is for rasters that have a integer element\_type and that have a no-data value and that do \*not\* convert to RGBA (using a colour palette) before mipmapping - in other words it gets mipmapped as a float raster. |
| [`GPlatesFileIO::MipmappedRasterFormatWriter< ProxiedRawRasterType, true/*use_colour_palette*/, typename boost::enable_if_c<ProxiedRawRasterType::has_no_data_value && boost::is_integral<typename ProxiedRawRasterType::element_type>::value >::type >`](#gplatesfileiomipmappedrasterformatwriter-proxiedrawrastertype-trueuse_colour_palette-typename-boostenable_if_cproxiedrawrastertypehas_no_data_value--boostis_integraltypename-proxiedrawrastertypeelement_typevalue-type-) | class | [`MipmappedRasterFormatWriterInternals::BaseMipmappedRasterFormatWriter< ProxiedRawRasterType, GPlatesGui::Mipmapper<GPlatesPropertyValues::Rgba8RawRaster> >`](MipmappedRasterFormatWriter.md) | `<class ProxiedRawRasterType>` | 0 | This specialisation is for rasters that have a integer element\_type and that have a no-data value and that convert to RGBA (using a colour palette) before mipmapping. |

## Members

### `GPlatesFileIO::MipmappedRasterFormatWriterInternals::BaseMipmappedRasterFormatWriter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `proxied_raster_element_type` | typedef | `typename ProxiedRawRasterType::element_type` | public | — |
| `source_raster_type` | typedef | `typename GPlatesPropertyValues::RawRasterUtils ::ConvertProxiedRasterToUnproxiedRaster<ProxiedRawRasterType>::unproxied_raster_type` | public | — |
| `source_raster_element_type` | typedef | `typename source_raster_type::element_type` | public | — |
| `mipmapper_type` | typedef | `MipmapperType` | public | — |
| `mipmapped_raster_type` | typedef | `typename mipmapper_type::output_raster_type` | public | — |
| `mipmapped_element_type` | typedef | `typename mipmapped_raster_type::element_type` | public | — |
| `coverage_raster_type` | typedef | `GPlatesPropertyValues::CoverageRawRaster` | public | — |
| `coverage_element_type` | typedef | `coverage_raster_type::element_type` | public | — |
| `BaseMipmappedRasterFormatWriter( typename ProxiedRawRasterType::non_null_ptr_type proxied_raw_raster, const GPlatesFileIO::RasterBandReaderHandle &source_raster_band_reader_handle)` | constructor | `None` | public | — |
| `write( const QString &filename)` | method | `void` | public | Creates mipmaps and writes a Mipmapped Raster Format file at filename. |
| `~BaseMipmappedRasterFormatWriter()` | destructor | `None` | protected | — |
| `create_source_region_mipmapper( const typename source_raster_type::non_null_ptr_type &source_region_raster)` | method | `boost::shared_ptr<mipmapper_type>` | protected | Create a mipmapper from the specified source raster region. |
| `has_coverage()` | method | `bool` | protected | Returns true if the mipmapped raster type has coverage data (determined by derived class). |
| `d_proxied_raw_raster` | field | `typename ProxiedRawRasterType::non_null_ptr_type` | protected | — |
| `d_source_raster_band_reader_handle` | field | `GPlatesFileIO::RasterBandReaderHandle` | protected | — |
| `d_source_raster_width` | field | `unsigned int` | protected | — |
| `d_source_raster_height` | field | `unsigned int` | protected | — |
| `d_num_levels` | field | `unsigned int` | protected | — |
| `MIPMAP_BYTE_STREAM_SIZE_THRESHOLD` | field | `unsigned int` | private | When the number of bytes written to a mipmap byte stream (attached to QByteArray) exceeds this threshold then we'll stream it to the mipmap file. |
| `hilbert_curve_traversal( unsigned int level, unsigned int x_offset, unsigned int y_offset, unsigned int dimension, unsigned int hilbert_start_point, unsigned int hilbert_end_point, const std::vector<boost::shared_ptr<QDataStream> > &temporary_mipmap_file_streams, const std::vector<boost::shared_ptr<QByteArray> > &tempo ...` | method | `boost::optional<boost::shared_ptr<mipmapper_type> >` | private | Traverse the Hilbert curve of blocks of the source (base level) raster using quad-tree recursion. |
| `get_source_raster_data( unsigned int x_offset, unsigned int y_offset)` | method | `boost::shared_ptr<mipmapper_type>` | private | Get source raster data (full-resolution data) of size 2\*BLOCK\_SIZE x 2\*BLOCK\_SIZE (or less near right or bottom edge of source raster) - to be used for generating mipmap data for a region of size BLOCK\_SIZE x BLOCK\_SIZE (or less). |
| `mipmap( mipmapper_type &mipmapper, QDataStream &mipmap_file_stream, QByteArray &mipmap_byte_array, QDataStream &mipmap_byte_stream, RasterFileCacheFormat::BlockInfo &mipmap_block_info, unsigned int mipmap_x_offset, unsigned int mipmap_y_offset)` | method | `void` | private | Mipmap source data (either from source raster or parent mipmap level) and write data to the specified mipmap stream and record stream offsets in block info. |
| `verify_mipmap_block_dimensions( const RasterFileCacheFormat::BlockInfos &mipmap_blocks, unsigned int level)` | method | `void` | private | Make sure the block dimensions are correct for the mipmap level. |
| `write_temporary_mipmap_file_to_output( QFile &temporary_mipmap_file, QDataStream &out)` | method | `void` | private | Appends the specified temporary mipmap file (contained encoded mipmap data) to the specified output stream. |

### `GPlatesFileIO::MipmappedRasterFormatWriter< ProxiedRawRasterType, false/*use_colour_palette*/, // Not applicable here typename boost::enable_if_c<!ProxiedRawRasterType::has_no_data_value && boost::is_same<typename ProxiedRawRasterType::element_type, GPlatesGui::rgba8_t>::value>::type >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `base_type` | typedef | `MipmappedRasterFormatWriterInternals::BaseMipmappedRasterFormatWriter< ProxiedRawRasterType, GPlatesGui::Mipmapper<GPlatesPropertyValues::Rgba8RawRaster> >` | private | — |
| `mipmapper_type` | typedef | `typename base_type::mipmapper_type` | private | — |
| `source_raster_type` | typedef | `typename base_type::source_raster_type` | private | — |
| `MipmappedRasterFormatWriter( typename ProxiedRawRasterType::non_null_ptr_type proxied_raw_raster, const GPlatesFileIO::RasterBandReaderHandle &source_raster_band_reader_handle, const GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type &colour_palette = GPlatesGui::RasterColourPalette::create())` | method | `None` | public | MipmappedRasterFormatWriterInternals::BaseMipmappedRasterFormatWriter::BaseMipmappedRasterFormatWriter. |
| `create_source_region_mipmapper( const typename source_raster_type::non_null_ptr_type &source_region_raster)` | method | `boost::shared_ptr<mipmapper_type>` | private | — |
| `has_coverage()` | method | `bool` | private | — |

### `GPlatesFileIO::MipmappedRasterFormatWriter< ProxiedRawRasterType, false/*use_colour_palette*/, // Not applicable here typename boost::enable_if_c<ProxiedRawRasterType::has_no_data_value && boost::is_floating_point<typename ProxiedRawRasterType::element_type>::value >::type >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `base_type` | typedef | `MipmappedRasterFormatWriterInternals::BaseMipmappedRasterFormatWriter< ProxiedRawRasterType, GPlatesGui::Mipmapper< typename GPlatesPropertyValues::RawRasterUtils ::ConvertProxiedR ...` | private | — |
| `mipmapper_type` | typedef | `typename base_type::mipmapper_type` | private | — |
| `source_raster_type` | typedef | `typename base_type::source_raster_type` | private | — |
| `source_raster_element_type` | typedef | `typename base_type::source_raster_element_type` | private | — |
| `MipmappedRasterFormatWriter( typename ProxiedRawRasterType::non_null_ptr_type proxied_raw_raster, const GPlatesFileIO::RasterBandReaderHandle &source_raster_band_reader_handle, const GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type &colour_palette = GPlatesGui::RasterColourPalette::create())` | method | `None` | public | MipmappedRasterFormatWriterInternals::BaseMipmappedRasterFormatWriter::BaseMipmappedRasterFormatWriter. |
| `create_source_region_mipmapper( const typename source_raster_type::non_null_ptr_type &source_region_raster)` | method | `boost::shared_ptr<mipmapper_type>` | private | — |
| `has_coverage()` | method | `bool` | private | — |

### `GPlatesFileIO::MipmappedRasterFormatWriter< ProxiedRawRasterType, false/*use_colour_palette*/, typename boost::enable_if_c<ProxiedRawRasterType::has_no_data_value && boost::is_integral<typename ProxiedRawRasterType::element_type>::value >::type >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `base_type` | typedef | `MipmappedRasterFormatWriterInternals::BaseMipmappedRasterFormatWriter< ProxiedRawRasterType, GPlatesGui::Mipmapper< typename GPlatesPropertyValues::RawRasterUtils ::ConvertProxiedR ...` | private | — |
| `mipmapper_type` | typedef | `typename base_type::mipmapper_type` | private | — |
| `source_raster_type` | typedef | `typename base_type::source_raster_type` | private | — |
| `source_raster_element_type` | typedef | `typename base_type::source_raster_element_type` | private | — |
| `MipmappedRasterFormatWriter( typename ProxiedRawRasterType::non_null_ptr_type proxied_raw_raster, const GPlatesFileIO::RasterBandReaderHandle &source_raster_band_reader_handle, const GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type &colour_palette = GPlatesGui::RasterColourPalette::create())` | method | `None` | public | MipmappedRasterFormatWriterInternals::BaseMipmappedRasterFormatWriter::BaseMipmappedRasterFormatWriter. |
| `create_source_region_mipmapper( const typename source_raster_type::non_null_ptr_type &source_region_raster)` | method | `boost::shared_ptr<mipmapper_type>` | private | — |
| `has_coverage()` | method | `bool` | private | — |

### `GPlatesFileIO::MipmappedRasterFormatWriter< ProxiedRawRasterType, true/*use_colour_palette*/, typename boost::enable_if_c<ProxiedRawRasterType::has_no_data_value && boost::is_integral<typename ProxiedRawRasterType::element_type>::value >::type >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `base_type` | typedef | `MipmappedRasterFormatWriterInternals::BaseMipmappedRasterFormatWriter< ProxiedRawRasterType, GPlatesGui::Mipmapper<GPlatesPropertyValues::Rgba8RawRaster> >` | private | NOTE: The type passed to the mipmapper is Rgba8RawRaster and \*not\* an integer raster. |
| `mipmapper_type` | typedef | `typename base_type::mipmapper_type` | private | — |
| `source_raster_type` | typedef | `typename base_type::source_raster_type` | private | — |
| `MipmappedRasterFormatWriter( typename ProxiedRawRasterType::non_null_ptr_type proxied_raw_raster, const GPlatesFileIO::RasterBandReaderHandle &source_raster_band_reader_handle, const GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type &colour_palette)` | method | `None` | public | MipmappedRasterFormatWriterInternals::BaseMipmappedRasterFormatWriter::BaseMipmappedRasterFormatWriter. |
| `create_source_region_mipmapper( const typename source_raster_type::non_null_ptr_type &source_region_raster)` | method | `boost::shared_ptr<mipmapper_type>` | private | — |
| `has_coverage()` | method | `bool` | private | — |
| `d_colour_palette` | field | `GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_nan_no_data_value( double &no_data_value)` | function | `bool` | — |
| `get_nan_no_data_value( float &no_data_value)` | function | `bool` | — |
| `get_nan_no_data_value( GPlatesGui::rgba8_t &no_data_value)` | function | `bool` | — |
| `GPLATES_FILEIO_MIPMAPPEDRASTERFORMATWRITER_H` | macro | `None` | — |
| `write( QDataStream &out, const T *data, unsigned int len)` | function | `void` | — |
| `get_nan_no_data_value( RasterElementType &no_data_value)` | function | `bool` | Returns the NAN no-data value for floating point element types (returns true), otherwise returns the default value for the element type (and returns false). |

## Notes

`write()` asserts (via `GPlatesGlobal::Assert`) that the supplied
`RasterBandReaderHandle` actually produces the expected `proxied_raster_element_type`
— a mismatch is treated as a programming error, not a recoverable input
error. `has_coverage()` is `false` only for the RGBA-without-no-data-value
specialisation, since GPlates keeps no-data information for RGBA in the
alpha channel rather than a separate coverage raster; every other
specialisation reports `true`. If the temporary directory rejects the
per-level `QTemporaryFile`, `write()` retries once using the destination
filename's own directory as the template before giving up and throwing
`ErrorOpeningFileForWritingException`.

## Used by

| Unit | Component | References |
|---|---|---|
| [property-values/ProxiedRasterResolver](../property-values/ProxiedRasterResolver.md) | property-values | 3 |
| [file-io/RasterFileCache](RasterFileCache.md) | file-io | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/MipmappedRasterFormatWriter.h
python scripts/gpq.py def GPlatesFileIO::MipmappedRasterFormatWriterInternals::BaseMipmappedRasterFormatWriter --body
python scripts/gpq.py uses BaseMipmappedRasterFormatWriter --kind class
python scripts/gpq.py hier BaseMipmappedRasterFormatWriter
```
