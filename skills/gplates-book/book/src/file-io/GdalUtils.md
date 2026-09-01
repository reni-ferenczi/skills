# GdalUtils

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 779 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GdalUtils.h` | C++ | 181 |
| `src/file-io/GdalUtils.cc` | C++ | 412 |

## Overview

`GdalUtils` centralises the raw GDAL/OGR calls used by `GDALRasterReader`, `GDALRasterWriter`, `OgrReader` and `OgrWriter`, so those classes don't each reimplement driver registration, opening and closing. It also isolates the GDAL 1 vs. GDAL 2 API split for vector (OGR) data: GDAL 2 folded `OGRDataSource`/`OGRSFDriver`/`OGRSFDriverRegistrar` into the plain GDAL `GDALDataset`/`GDALDriver`/`GDALDriverManager` types, so the `vector_data_*_type` typedefs resolve to one family or the other depending on `GDAL_VERSION_MAJOR`, letting callers write GDAL-version-agnostic code against `GdalUtils::vector_data_source_type` and friends.

`open_raster()` additionally guards against a known issue on some older Linux systems where `GDALOpen()` can segfault on a malformed GMT GRD file: it installs a `SIGSEGV` handler around the call and uses `sigsetjmp`/`siglongjmp` to recover and report a normal read error instead of crashing the process, restoring the previous signal handler afterwards either way.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::GdalUtils::vector_data_driver_manager_type`](#gplatesfileiogdalutilsvector_data_driver_manager_type) | typedef | — | — | 0 | — |
| [`GPlatesFileIO::GdalUtils::vector_data_driver_type`](#gplatesfileiogdalutilsvector_data_driver_type) | typedef | — | — | 0 | — |
| [`GPlatesFileIO::GdalUtils::vector_data_source_type`](#gplatesfileiogdalutilsvector_data_source_type) | typedef | — | — | 0 | — |
| [`GPlatesFileIO::GdalUtils::big_int_type`](#gplatesfileiogdalutilsbig_int_type) | typedef | — | — | 0 | — |

## Members

### `GPlatesFileIO::GdalUtils::vector_data_driver_manager_type`

*None.*

### `GPlatesFileIO::GdalUtils::vector_data_driver_type`

*None.*

### `GPlatesFileIO::GdalUtils::vector_data_source_type`

*None.*

### `GPlatesFileIO::GdalUtils::big_int_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `open_gdal_version2( const QString &filename, unsigned int open_flags, // GDAL_OF_RASTER or GDAL_OF_VECTOR (and GDAL_OF_READONLY or GDAL_OF_UPDATE). ReadErrorAccumulation *read_errors)` | function | `GDALDataset` | — |
| `GPLATES_FILEIO_GDALUTILS_H` | macro | `None` | — |
| `register_all_drivers()` | function | `void` | A convenience function that wraps GDALAllRegister. |
| `get_raster_driver_manager()` | function | `GDALDriverManager` | A convenience function that wraps around GetGDALDriverManager for raster formats. |
| `open_raster( const QString &filename, bool update = false, ReadErrorAccumulation *read_errors = NULL)` | function | `GDALDataset` | A convenience function that wraps around GDALOpenEx for raster formats. |
| `close_raster( GDALDataset *gdal_data_set)` | function | `void` | Convenience function that wraps around GDALClose. |
| `get_vector_driver_manager()` | function | `vector_data_driver_manager_type` | A convenience function that wraps around GetGDALDriverManager for vector formats. |
| `create_data_source( vector_data_driver_type *vector_data_driver, const QString &pszName, char **papszOptions = NULL)` | function | `vector_data_source_type` | A convenience function that wraps around GDALDriver::Create() for vector formats. |
| `open_vector( const QString &filename, bool update = false, ReadErrorAccumulation *read_errors = NULL)` | function | `vector_data_source_type` | A convenience function that wraps around GDALOpenEx for vector formats. |
| `close_vector( vector_data_source_type *ogr_data_source)` | function | `void` | Convenience function that wraps around GDALClose. |

## Notes

- `register_all_drivers()` is idempotent (`GDALAllRegister` is only actually invoked the first time it is called) and is already called internally by `open_raster()`/`open_vector()`, so callers rarely need to call it directly.
- The `SIGSEGV` trap in `open_raster()` is a best-effort workaround for a specific known GDAL bug on some Linux systems; it is not a general-purpose crash handler and does not protect other GDAL calls in this file.
- `vector_data_source_type`, `vector_data_driver_type` and `vector_data_driver_manager_type` change meaning depending on `GDAL_VERSION_MAJOR`; do not assume they are always `GDALDataset`/`GDALDriver`/`GDALDriverManager` when reading code built against GDAL 1.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/OgrWriter](OgrWriter.md) | file-io | 35 |
| [file-io/GdalRasterReader](GdalRasterReader.md) | file-io | 24 |
| [file-io/GdalRasterWriter](GdalRasterWriter.md) | file-io | 23 |
| [file-io/OgrReader](OgrReader.md) | file-io | 12 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GdalUtils.h
python scripts/gpq.py def GPlatesFileIO::GdalUtils::vector_data_driver_manager_type --body
python scripts/gpq.py uses vector_data_driver_manager_type --kind typedef
```
