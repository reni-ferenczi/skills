# RasterFileCache

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 6 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/RasterFileCache.h` | C++ | 377 |

## Overview

[[[PROSE overview unit=file-io/RasterFileCache tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILE_IO_RASTERFILECACHE_H` | macro | `None` | — |
| `create_mipmapped_raster_file_cache_format_reader( const typename ProxiedRawRasterType::non_null_ptr_type &proxied_raw_raster, GPlatesFileIO::RasterBandReaderHandle raster_band_reader_handle, const GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type &colour_palette = GPlatesGui::RasterColourPalette::create())` | function | `boost::shared_ptr<MipmappedRasterFormatReader<MipmappedRasterType> >` | — |
| `create_mipmap_file( const typename ProxiedRawRasterType::non_null_ptr_type &proxied_raw_raster, GPlatesFileIO::RasterBandReaderHandle raster_band_reader_handle, const GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type &colour_palette)` | function | `bool` | — |
| `create_mipmapped_raster_file_cache_format_reader( const typename ProxiedRawRasterType::non_null_ptr_type &proxied_raw_raster, GPlatesFileIO::RasterBandReaderHandle raster_band_reader_handle, const GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type &colour_palette)` | function | `boost::shared_ptr<MipmappedRasterFormatReader<MipmappedRasterType> >` | — |

## Notes

[[[PROSE notes unit=file-io/RasterFileCache tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [property-values/ProxiedRasterResolver](../property-values/ProxiedRasterResolver.md) | property-values | 5 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/RasterFileCache.h
```
