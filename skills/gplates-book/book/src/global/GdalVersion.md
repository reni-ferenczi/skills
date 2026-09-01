# GdalVersion

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 1479 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/global/GdalVersion.h` | C++ | 60 |

## Overview

[[[PROSE overview unit=global/GdalVersion tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=global/GdalVersion tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
