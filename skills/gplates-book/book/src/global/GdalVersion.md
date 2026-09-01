# GdalVersion

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 1479 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/global/GdalVersion.h` | C++ | 60 |

## Overview

`GdalVersion.h` pulls in `<gdal_version.h>` and re-defines GDAL's `GDAL_COMPUTE_VERSION` macro under the `GPLATES_` prefix (as `GPLATES_GDAL_COMPUTE_VERSION` and `GPLATES_GDAL_VERSION_NUM`) so that version-gated `#if` checks against `GDAL_VERSION_NUM` compile even against GDAL releases older than 1.10, where `GDAL_COMPUTE_VERSION` does not exist yet. Without this, an `#if defined(GDAL_COMPUTE_VERSION) && GDAL_VERSION_NUM >= GDAL_COMPUTE_VERSION(2,3,0)` guard would fail to parse on older GDAL because the preprocessor still expands the unguarded macro call inside the `&&` operand.

Code that needs to branch on the installed GDAL version (readers/writers for raster and vector formats, spatial reference handling) includes this header and compares against `GPLATES_GDAL_VERSION_NUM` instead of GDAL's own macro.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GLOBAL_GDALVERSION_H` | macro | `None` | — |
| `GPLATES_GDAL_COMPUTE_VERSION` | macro_function | `((maj)*1000000+(min)*10000+(rev)*100)` | Same as defined in GDAL \>= 1.10... |
| `GPLATES_GDAL_VERSION_NUM` | macro | `(GPLATES_GDAL_COMPUTE_VERSION(GDAL_VERSION_MAJOR,GDAL_VERSION_MINOR,GDAL_VERSION_REV)+GDAL_VERSION_BUILD)` | Same as defined in GDAL \>= 1.10... |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 8 |
| [file-io/OgrWriter](../file-io/OgrWriter.md) | file-io | 6 |
| [file-io/GdalRasterReader](../file-io/GdalRasterReader.md) | file-io | 5 |
| [file-io/GsmlPropertyHandlers](../file-io/GsmlPropertyHandlers.md) | file-io | 3 |
| [property-values/SpatialReferenceSystem](../property-values/SpatialReferenceSystem.md) | property-values | 3 |
| [file-io/Gdal](../file-io/Gdal.md) | file-io | 1 |
| [file-io/Ogr](../file-io/Ogr.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/GdalVersion.h
```
