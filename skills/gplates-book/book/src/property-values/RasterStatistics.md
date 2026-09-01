# RasterStatistics

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 285 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/RasterStatistics.h` | C++ | 45 |

## Overview

`RasterStatistics` is a plain aggregate of the four summary values (`minimum`, `maximum`, `mean`, `standard_deviation`) that describe a raster band's data distribution. Each field is independently optional because a given raster source or cache format may supply only some of them, or none at all; consumers such as colour-mapping and mipmap generation code must check each field before using it rather than assuming the whole struct is populated.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::RasterStatistics`](#gplatespropertyvaluesrasterstatistics) | struct | — | — | 0 | RasterStatistics contains optional statistics about a raster. |

## Members

### `GPlatesPropertyValues::RasterStatistics`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `minimum` | field | `boost::optional<double>` | public | — |
| `maximum` | field | `boost::optional<double>` | public | — |
| `mean` | field | `boost::optional<double>` | public | — |
| `standard_deviation` | field | `boost::optional<double>` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_RASTERSTATISTICS_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GdalRasterReader](../file-io/GdalRasterReader.md) | file-io | 117 |
| [gui/Mipmapper](../gui/Mipmapper.md) | gui | 60 |
| [file-io/MipmappedRasterFormatWriter](../file-io/MipmappedRasterFormatWriter.md) | file-io | 25 |
| [gui/ColourRawRaster](../gui/ColourRawRaster.md) | gui | 23 |
| [file-io/SourceRasterFileCacheFormatReader](../file-io/SourceRasterFileCacheFormatReader.md) | file-io | 17 |
| [file-io/RasterFileCacheFormatReader](../file-io/RasterFileCacheFormatReader.md) | file-io | 16 |
| [qt-widgets/RasterLayerOptionsWidget](../qt-widgets/RasterLayerOptionsWidget.md) | qt-widgets | 10 |
| [file-io/MipmappedRasterFormatReader](../file-io/MipmappedRasterFormatReader.md) | file-io | 9 |
| [app-logic/RasterLayerParams](../app-logic/RasterLayerParams.md) | app-logic | 8 |
| [opengl/GLNormalMapSource](../opengl/GLNormalMapSource.md) | opengl | 8 |
| [property-values/RawRaster](RawRaster.md) | property-values | 8 |
| [property-values/RawRasterUtils](RawRasterUtils.md) | property-values | 7 |
| [presentation/RasterVisualLayerParams](../presentation/RasterVisualLayerParams.md) | presentation | 5 |
| [qt-widgets/RasterPropertiesDialog](../qt-widgets/RasterPropertiesDialog.md) | qt-widgets | 5 |
| [app-logic/ExtractRasterFeatureProperties](../app-logic/ExtractRasterFeatureProperties.md) | app-logic | 1 |
| [opengl/GLAgeGridMaskSource](../opengl/GLAgeGridMaskSource.md) | opengl | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/RasterStatistics.h
python scripts/gpq.py def GPlatesPropertyValues::RasterStatistics --body
python scripts/gpq.py uses RasterStatistics --kind struct
python scripts/gpq.py hier RasterStatistics
```
