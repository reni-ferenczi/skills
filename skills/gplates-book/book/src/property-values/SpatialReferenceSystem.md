# SpatialReferenceSystem

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1238 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/SpatialReferenceSystem.h` | C++ | 145 |
| `src/property-values/SpatialReferenceSystem.cc` | C++ | 102 |

## Overview

[[[PROSE overview unit=property-values/SpatialReferenceSystem tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::SpatialReferenceSystem`](#gplatespropertyvaluesspatialreferencesystem) | class | [`GPlatesUtils::ReferenceCount<SpatialReferenceSystem>`](../utils/ReferenceCount.md) | — | 0 | A spatial reference system. |

## Members

### `GPlatesPropertyValues::SpatialReferenceSystem`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<SpatialReferenceSystem>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const SpatialReferenceSystem>` | public | — |
| `get_WGS84()` | method | `non_null_ptr_to_const_type` | public | Spatial reference system for standard "WGS84". |
| `create( const OGRSpatialReference &ogr_srs)` | method | `non_null_ptr_type` | public | Creates a spatial reference system. |
| `~SpatialReferenceSystem()` | destructor | `None` | public | — |
| `is_geographic()` | method | `bool` | public | Returns true if this spatial reference system is a geographic coordinate system. |
| `is_projected()` | method | `bool` | public | Returns true if this spatial reference system is a projected coordinate system. |
| `is_wgs84()` | method | `bool` | public | Returns true if the spatial reference system is WGS84. |
| `OGRSpatialReferenceReleaser` | struct | `None` | private | Release our reference count (ie, decrement OGR reference count in OGRSpatialReference) when all our boost 'd\_ogr\_srs' references to the OGRSpatialReference object are destroyed. |
| `d_ogr_srs` | field | `boost::shared_ptr<OGRSpatialReference>` | private | — |
| `SpatialReferenceSystem( const OGRSpatialReference &ogr_srs)` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `operator()( OGRSpatialReference *ogr_srs)` | operator | `void` | — |
| `GPLATES_PROPERTY_VALUES_SPATIALREFERENCESYSTEM_H` | macro | `None` | — |
| `DISABLE_MSVC_WARNING` | variable | `PUSH_MSVC_WARNINGS` | — |

## Notes

[[[PROSE notes unit=property-values/SpatialReferenceSystem tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [property-values/CoordinateTransformation](CoordinateTransformation.md) | property-values | 23 |
| [file-io/FeatureCollectionFileFormatConfigurations](../file-io/FeatureCollectionFileFormatConfigurations.md) | file-io | 10 |
| [file-io/OgrWriter](../file-io/OgrWriter.md) | file-io | 7 |
| [qt-widgets/OgrSrsWriteOptionDialog](../qt-widgets/OgrSrsWriteOptionDialog.md) | qt-widgets | 7 |
| [property-values/ProxiedRasterCache](ProxiedRasterCache.md) | property-values | 6 |
| [app-logic/ExtractRasterFeatureProperties](../app-logic/ExtractRasterFeatureProperties.md) | app-logic | 4 |
| [file-io/OgrFeatureCollectionWriter](../file-io/OgrFeatureCollectionWriter.md) | file-io | 4 |
| [file-io/RasterReader](../file-io/RasterReader.md) | file-io | 4 |
| [file-io/RasterWriter](../file-io/RasterWriter.md) | file-io | 4 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 4 |
| [app-logic/RasterLayerParams](../app-logic/RasterLayerParams.md) | app-logic | 3 |
| [app-logic/RasterLayerProxy](../app-logic/RasterLayerProxy.md) | app-logic | 3 |
| [file-io/GdalRasterWriter](../file-io/GdalRasterWriter.md) | file-io | 3 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 3 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 3 |
| [property-values/GmlFile](GmlFile.md) | property-values | 3 |
| [file-io/GsmlPropertyHandlers](../file-io/GsmlPropertyHandlers.md) | file-io | 2 |
| [qt-widgets/ImportScalarField3DDialog](../qt-widgets/ImportScalarField3DDialog.md) | qt-widgets | 2 |
| [file-io/GdalRasterReader](../file-io/GdalRasterReader.md) | file-io | 1 |
| [file-io/RgbaRasterReader](../file-io/RgbaRasterReader.md) | file-io | 1 |

*... and 1 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/SpatialReferenceSystem.h
python scripts/gpq.py def GPlatesPropertyValues::SpatialReferenceSystem --body
python scripts/gpq.py uses SpatialReferenceSystem --kind class
python scripts/gpq.py hier SpatialReferenceSystem
```
