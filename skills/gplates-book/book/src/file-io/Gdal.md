# Gdal

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1479 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/Gdal.h` | C++ | 40 |

## Overview

Wrapper header for GDAL (Geospatial Data Abstraction Library) includes. This header ensures consistent and system-appropriate inclusion of GDAL functionality across the codebase, including version macros from `GdalVersion`. It is used by GPlates' raster and vector readers/writers to access GDAL's data format support.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_GDAL_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GdalUtils](GdalUtils.md) | file-io | 2 |
| [file-io/GdalRasterReader](GdalRasterReader.md) | file-io | 1 |
| [file-io/GdalRasterWriter](GdalRasterWriter.md) | file-io | 1 |
| [file-io/OgrReader](OgrReader.md) | file-io | 1 |
| [file-io/OgrWriter](OgrWriter.md) | file-io | 1 |
| [file-io/StandaloneBundle](StandaloneBundle.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/Gdal.h
```
