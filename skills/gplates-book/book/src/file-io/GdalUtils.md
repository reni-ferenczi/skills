# GdalUtils

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 779 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GdalUtils.h` | C++ | 181 |
| `src/file-io/GdalUtils.cc` | C++ | 412 |

## Overview

[[[PROSE overview unit=file-io/GdalUtils tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=file-io/GdalUtils tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
