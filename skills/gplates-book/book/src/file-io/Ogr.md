# Ogr

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 12 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/Ogr.h` | C++ | 35 |

## Overview

A convenience header that ensures GDAL version information is accessible whenever the OGR library is used. It includes `GdalVersion.h` and the GDAL `ogrsf_frmts.h` header, providing a single include point for OGR-dependent code in the project.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_OGR_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/OgrWriter](OgrWriter.md) | file-io | 2 |
| [file-io/GdalUtils](GdalUtils.md) | file-io | 1 |
| [file-io/OgrReader](OgrReader.md) | file-io | 1 |
| [file-io/OgrUtils](OgrUtils.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/Ogr.h
```
