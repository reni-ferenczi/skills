# RasterFileCache

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 6 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/RasterFileCache.h` | C++ | 377 |

## Overview

A template-based utility for creating and managing mipmap caches of raster files. Mipmapping generates downsampled pyramid copies of an image so that small regions can be accessed efficiently without reading the entire raster. This unit creates mipmap files on disk and regenerates them if the source raster is newer or the cached format is from a future GPlates version.

The main entry point, `create_mipmapped_raster_file_cache_format_reader()`, checks for an existing cache, creates one if necessary or regenerated if out of date, then returns a reader. For integer rasters with integer colour palettes, a separate palette-specific mipmap is created (indexed by palette memory address) and marked for deletion on exit.

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

The caller should not hold open file handles to the source raster when calling this function, as the cache may be removed during creation. Mipmap files for integer colour palettes are marked for deletion on exit because the palette ID is derived from the memory address of the palette object, which is not stable across application runs.

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
